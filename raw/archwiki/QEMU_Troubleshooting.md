---
{"title": "QEMU/Troubleshooting", "url": "https://wiki.archlinux.org/title/QEMU/Troubleshooting", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# QEMU/Troubleshooting

\

## Mouse cursor is jittery or erratic {#Mouse_cursor_is_jittery_or_erratic}

If the cursor jumps around the screen uncontrollably, adding an [environment variable](../../en/Environment_variable.html "Environment variable") before starting QEMU might help:

    export SDL_VIDEO_X11_DGAMOUSE=0

## No visible Cursor {#No_visible_Cursor}

Add `-display default,show-cursor=on` to QEMU\'s options to see a mouse cursor.

If that still does not work, make sure you have set your display device appropriately, for example: `-vga qxl`.

Another option to try is `-usb -device usb-tablet` as mentioned in [QEMU#Mouse integration](../../en/QEMU.html#Mouse_integration "QEMU"). This overrides the default PS/2 mouse emulation and synchronizes pointer location between host and guest as an added bonus.

## Two different mouse cursors are visible {#Two_different_mouse_cursors_are_visible}

Apply the tip [QEMU#Mouse integration](../../en/QEMU.html#Mouse_integration "QEMU").

## Keyboard issues when using VNC {#Keyboard_issues_when_using_VNC}

When using VNC, you might experience keyboard problems described (in gory details) [here](https://www.berrange.com/posts/2010/07/04/more-than-you-or-i-ever-wanted-to-know-about-virtual-keyboard-handling/). The solution is *not* to use the `-k` option on QEMU, and to use `gvncviewer` from [gtk-vnc](https://archlinux.org/packages/?name=gtk-vnc). See also [this](https://www.mail-archive.com/libvir-list@redhat.com/msg13340.html) message posted on libvirt\'s mailing list.

## Keyboard seems broken or the arrow keys do not work {#Keyboard_seems_broken_or_the_arrow_keys_do_not_work}

Should you find that some of your keys do not work or \"press\" the wrong key (in particular, the arrow keys), you likely need to specify your keyboard layout as an option. The keyboard layouts can be found in `/usr/share/qemu/keymaps/`.

    $ qemu-system-x86_64 -k keymap disk_image

## Could not read keymap file {#Could_not_read_keymap_file}

    qemu-system-x86_64: -display vnc=0.0.0.0:0: could not read keymap file: 'en'

is caused by an invalid *keymap* passed to the `-k` argument. For example, `en` is invalid, but `en-us` is valid - see `/usr/share/qemu/keymaps/`.

## Guest display stretches on window resize {#Guest_display_stretches_on_window_resize}

To restore default window size, press `Ctrl+Alt+u`.

## ioctl(KVM_CREATE_VM) failed: 16 Device or resource busy {#ioctl(KVM_CREATE_VM)_failed:_16_Device_or_resource_busy}

If an error message like this is printed when starting QEMU with `-enable-kvm` option:

    ioctl(KVM_CREATE_VM) failed: 16 Device or resource busy
    failed to initialize KVM: Device or resource busy

that means another [hypervisor](../../en/Category:Hypervisors.html "Hypervisor") is currently running. It is not recommended or possible to run several hypervisors in parallel.

## libgfapi error message {#libgfapi_error_message}

The error message displayed at startup:

    Failed to open module: libgfapi.so.0: cannot open shared object file: No such file or directory

[Install](../../en/Help:Reading.html#Installation_of_packages "Install") [glusterfs](https://archlinux.org/packages/?name=glusterfs) or ignore the error message as GlusterFS is a optional dependency.

## Kernel panic on LIVE-environments {#Kernel_panic_on_LIVE-environments}

If you start a live-environment (or better: booting a system) you may encounter this:

    [ end Kernel panic - not syncing: VFS: Unable to mount root fs on unknown block(0,0)

or some other boot hindering process (e.g. cannot unpack initramfs, cant start service foo). Try starting the virtual machine with the `-m VALUE` switch and an appropriate amount of RAM, if the ram is to low you will probably encounter similar issues as above/without the memory-switch.

## Windows 7 guest suffers low-quality sound {#Windows_7_guest_suffers_low-quality_sound}

Using the `hda` audio driver for Windows 7 guest may result in low-quality sound. Changing the audio driver to `ac97` by passing the `-soundhw ac97` arguments to QEMU and installing the AC97 driver from [Realtek AC\'97 Audio Codecs](https://www.realtek.com/Download/ToDownload?type=agree&downloadid=3204)^\[[dead\ link](https://en.wikipedia.org/wiki/Wikipedia:Link_rot "wikipedia:Wikipedia:Link rot")\ 2025-08-16---SSL\ error\]^ in the guest may solve the problem. See [Red Hat Bugzilla -- Bug 1176761](https://bugzilla.redhat.com/show_bug.cgi?id=1176761#c16) for more information.

## Could not access KVM kernel module: Permission denied {#Could_not_access_KVM_kernel_module:_Permission_denied}

If you encounter the following error:

    libvirtError: internal error: process exited while connecting to monitor: Could not access KVM kernel module: Permission denied failed to initialize KVM: Permission denied

Systemd 234 assigns a dynamic ID for the `kvm` group (see [FS#54943](https://bugs.archlinux.org/task/54943)). To avoid this error, you need edit the file `/etc/libvirt/qemu.conf` and change the line with `group = "78"` to `group = "kvm"`.

## \"System Thread Exception Not Handled\" when booting a Windows virtual machine {#\"System_Thread_Exception_Not_Handled\"_when_booting_a_Windows_virtual_machine}

Windows 8 or Windows 10 guests may raise a generic compatibility exception at boot, namely \"System Thread Exception Not Handled\", which tends to be caused by legacy drivers acting strangely on real machines. On KVM machines this issue can generally be solved by setting the CPU model to `core2duo`.

## Certain Windows games/applications crashing/causing a bluescreen {#Certain_Windows_games/applications_crashing/causing_a_bluescreen}

Occasionally, applications running in the virtual machine may crash unexpectedly, whereas they would run normally on a physical machine. If, while running `dmesg -wH` as root, you encounter an error mentioning `MSR`, the reason for those crashes is that KVM injects a [General protection fault](https://en.wikipedia.org/wiki/General_protection_fault "wikipedia:General protection fault") (GPF) when the guest tries to access unsupported [Model-specific registers](https://en.wikipedia.org/wiki/Model-specific_register "wikipedia:Model-specific register") (MSRs) - this often results in guest applications/OS crashing. A number of those issues can be solved by passing the `ignore_msrs=1` option to the KVM module, which will ignore unimplemented MSRs.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/kvm.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
options kvm ignore_msrs=1
```

Cases where adding this option might help:

-   GeForce Experience complaining about an unsupported CPU being present.
-   StarCraft 2 and L.A. Noire reliably blue-screening Windows 10 with `KMODE_EXCEPTION_NOT_HANDLED`. The blue screen information does not identify a driver file in these cases.

**Warning** While this is normally safe and some applications might not work without this, silently ignoring unknown MSR accesses could potentially break other software within the virtual machine or other virtual machine.

## High interrupt latency and microstuttering {#High_interrupt_latency_and_microstuttering}

This problem manifests itself as small pauses (stutters) and is particularly noticeable in graphics-intensive applications, such as games.

-   One of the causes is CPU power saving features, which are controlled by [CPU frequency scaling](../../en/CPU_frequency_scaling.html "CPU frequency scaling"). Change this to `performance` for all processor cores.
-   Another possible cause is PS/2 inputs. Switch from PS/2 to Virtio inputs, see [PCI passthrough via OVMF#Passing keyboard/mouse via Evdev](../../en/PCI_passthrough_via_OVMF.html#Passing_keyboard/mouse_via_Evdev "PCI passthrough via OVMF").

## QXL video causes low resolution {#QXL_video_causes_low_resolution}

QEMU 4.1.0 introduced a regression where QXL video can fall back to low resolutions, when being displayed through spice. [\[1\]](https://bugs.launchpad.net/qemu/+bug/1843151) For example, when KMS starts, text resolution may become as low as 4x10 characters. When trying to increase GUI resolution, it may go to the lowest supported resolution.

As a workaround, create your device in this form:

    -device qxl-vga,max_outputs=1...

## Virtual machine not booting when using a Secure Boot enabled OVMF {#Virtual_machine_not_booting_when_using_a_Secure_Boot_enabled_OVMF}

`OVMF_CODE.secboot.4m.fd` and `OVMF_CODE.secboot.fd` files from [edk2-ovmf](https://archlinux.org/packages/?name=edk2-ovmf) are built with [SMM](https://en.wikipedia.org/wiki/System_Management_Mode "wikipedia:System Management Mode") support. If S3 support is not disabled in the virtual machine, then the virtual machine might not boot at all.

Add the `-global ICH9-LPC.disable_s3=1` option to the *qemu* command.

See [FS#59465](https://bugs.archlinux.org/task/59465) and [https://github.com/tianocore/edk2/blob/master/OvmfPkg/README](https://github.com/tianocore/edk2/blob/master/OvmfPkg/README) for more details and the required options to use Secure Boot in QEMU.

## Virtual machine not booting into Arch ISO {#Virtual_machine_not_booting_into_Arch_ISO}

When trying to boot the virtual machine for the first time from an Arch ISO image, the boot process hangs. Adding `console=ttyS0` to kernel boot options by pressing `e` in the boot menu you will get more boot messages and the following error:

    :: Mounting '/dev/disk/by-label/ARCH_202204' to '/run/archiso/bootmnt'
    Waiting 30 seconds for device /dev/disk/by-label/ARCH_202204 ...
    ERROR: '/dev/disk/by-label/ARCH_202204' device did not show up after 30 seconds...
       Falling back to interactive prompt
       You can try to fix the problem manually, log out when you are finished
    sh: can't access tty; job control turned off

The error message does not give a good clue as to what the real issue is. The problem is with the default 128MB of RAM that QEMU allocates to the virtual machine. Increasing the limit to 1024MB with `-m 1024` solves the issue and lets the system boot. You can continue installing Arch Linux as usual after that. Once the installation is complete, the memory allocation for the virtual machine can be decreased. The need for 1024MB is due to RAM disk requirements and size of the installation media. See [this message on the arch-releng mailing list](https://lists.archlinux.org/archives/list/arch-releng@lists.archlinux.org/message/D5HSGOFTPGYI6IZUEB3ZNAX4D3F3ID37/) and [this forum thread](https://bbs.archlinux.org/viewtopic.php?id=204023).

## Guest CPU interrupts are not firing {#Guest_CPU_interrupts_are_not_firing}

If you are writing your own operating system by following the [OSDev wiki](https://wiki.osdev.org/), or are simply getting stepping through the guest architecture assembly code using QEMU\'s `gdb` interface using the `-s` flag, it is useful to know that many emulators, QEMU included, usually implement some CPU interrupts leaving many hardware interrupts unimplemented. One way to know if your code is firing an interrupt, is by using the `-d int` argument.

to enable showing interrupts/exceptions on stdout.

To see what other guest debugging features QEMU has to offer:

    $ qemu-system-x86_64 -d help

or replace `x86_64` for your chosen guest architecture.

## KDE with sddm does not start spice-vdagent at login automatically {#KDE_with_sddm_does_not_start_spice-vdagent_at_login_automatically}

Remove or comment out `X-GNOME-Autostart-Phase=WindowManager` from `/etc/xdg/autostart/spice-vdagent.desktop`. [\[2\]](https://github.com/systemd/systemd/issues/18791)

## Bluetooth audio quality drops after QEMU starts {#Bluetooth_audio_quality_drops_after_QEMU_starts}

Disable the [WirePlumber](../../en/WirePlumber.html "WirePlumber") profile\'s auto-switching feature to prevent it from using mono audio profiles.

    $ wpctl settings --save bluetooth.autoswitch-to-headset-profile false

## Linux guest boot hangs with GRUB in UEFI mode {#Linux_guest_boot_hangs_with_GRUB_in_UEFI_mode}

After updating to [edk2-ovmf](https://archlinux.org/packages/?name=edk2-ovmf) 202505-1 or newer, it becomes impossible to boot many Linux distributions that use GRUB in UEFI mode (known examples include versions of Rocky Linux, Debian, RHEL and Fedora). This also extends to the distributions\' live ISO images.

Issue tracker: [archlinux/packaging/packages/edk2#9](https://gitlab.archlinux.org/archlinux/packaging/packages/edk2/-/issues/9)

As of [edk2-ovmf](https://archlinux.org/packages/?name=edk2-ovmf) 202508-1, this issue still persists.

### Symptoms {#Symptoms}

-   When attempting to boot a GRUB menu entry:
    -   the graphical SPICE console freezes
    -   exception information reporting a page fault is printed to the serial console
    -   CPU usage for QEMU is pinned at 100% on 1 core

#### Example of serial console output {#Example_of_serial_console_output}

    !!!! X64 Exception Type - 0E(#PF - Page-Fault)  CPU Apic ID - 00000000 !!!!
    ExceptionData - 0000000000000003  I:0 R:0 U:0 W:1 P:1 PK:0 SS:0 SGX:0
    RIP  - 00000000766CBCF0, CS  - 0000000000000038, RFLAGS - 0000000000210046
    RAX  - 00000000766E7000, RCX - 00000000766E7000, RDX - 0000000000000000
    RBX  - 000000007E7B7F18, RSP - 000000007FE6C278, RBP - 000000007F9EC018
    RSI  - 0000000000000000, RDI - 0000000076709078
    R8   - 0000000000000000, R9  - 000000007BCC1195, R10 - 000000007D41D7F1
    R11  - 0000000000000077, R12 - 000000007DCD9000, R13 - 000000007E7B7F18
    R14  - 000000007DC4D768, R15 - 000000007DC4D770
    DS   - 0000000000000030, ES  - 0000000000000030, FS  - 0000000000000030
    GS   - 0000000000000030, SS  - 0000000000000030
    CR0  - 0000000080010033, CR2 - 00000000766E7000, CR3 - 000000007FC01000
    CR4  - 0000000000000668, CR8 - 0000000000000000
    DR0  - 0000000000000000, DR1 - 0000000000000000, DR2 - 0000000000000000
    DR3  - 0000000000000000, DR6 - 00000000FFFF0FF0, DR7 - 0000000000000400
    GDTR - 000000007F9DC000 0000000000000047, LDTR - 0000000000000000
    IDTR - 000000007F494018 0000000000000FFF,   TR - 0000000000000000
    FXSAVE_STATE - 000000007FE6BED0
    !!!! Find image based on IP(0x766CBCF0) (No PDB)  (ImageBase=000000006B676EE0, EntryPoint=000000006C58B537) !!!!

### Workarounds {#Workarounds}

-   [Manually downgrade](../../en/Downgrading_packages.html "Downgrading packages") [edk2-ovmf](https://archlinux.org/packages/?name=edk2-ovmf) to 202411-1 and hold version until fix is released
-   Apply patch from Debian\'s edk2 as detailed [on the issue tracker](https://gitlab.archlinux.org/archlinux/packaging/packages/edk2/-/issues/10#note_317309) and add a fwcfg line with needed guests.
-   Install Fedora\'s EDK2-OVMF [edk2-ovmf-fedora](https://aur.archlinux.org/packages/edk2-ovmf-fedora/)^AUR^ alongside [edk2-ovmf](https://archlinux.org/packages/?name=edk2-ovmf), and change the firmware path on launch for needed guests.
