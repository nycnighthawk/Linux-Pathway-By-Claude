---
{"title": "PCI passthrough via OVMF/Troubleshooting", "url": "https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF/Troubleshooting", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# PCI passthrough via OVMF/Troubleshooting

If your issue is not mentioned below, you may want to browse [QEMU#Troubleshooting](../../en/QEMU.html#Troubleshooting "QEMU").

## QEMU 4.0: Unable to load graphics drivers/BSOD/Graphics stutter after driver install using Q35 {#QEMU_4.0:_Unable_to_load_graphics_drivers/BSOD/Graphics_stutter_after_driver_install_using_Q35}

Starting with [QEMU](../../en/QEMU.html "QEMU") 4.0, the Q35 machine type changes the default `kernel_irqchip` from `off` to `split`, which breaks some guest devices, such as [NVIDIA](../../en/NVIDIA.html "NVIDIA") graphics (the driver fails to load / black screen / code 43 / graphics stutters, usually when mouse moving).

Switch to full [KVM](../../en/KVM.html "KVM") mode instead by adding `<ioapic driver='kvm'/>` under [libvirt](../../en/Libvirt.html "Libvirt")\'s `<features>` tag in your virtual machine configuration or by adding `kernel_irqchip=on` in the `-machine` QEMU arg.

## QEMU 5.0: host-passthrough with kernel version 5.5 to 5.8.1 when using Zen 2 processors: Windows 10 BSOD loop \'KERNEL SECURITY CHECK FAILURE\' {#QEMU_5.0:_host-passthrough_with_kernel_version_5.5_to_5.8.1_when_using_Zen_2_processors:_Windows_10_BSOD_loop_'KERNEL_SECURITY_CHECK_FAILURE'}

**Note** As of kernel version 5.8.2, disabling STIBP is not required anymore.

Starting with QEMU 5.0 virtual machines running on Zen 2 and kernels newer than 5.4 will cause a BSOD loop of: \'KERNEL SECURITY CHECK FAILURE\'. This can be fixed by either updating to kernel version 5.8.2 or higher, or disabling STIBP:

     <cpu mode='host-passthrough' ...>
       ...
       <feature policy='disable' name='amd-stibp'/>
       ...
     </cpu>

This requires libvirt 6.5 or higher. On older versions, several workarounds exist:

-   Switch CPU mode from `host-passthrough` to `host-model`. This only works on libvirt 6.4 or lower.
-   Manually patch [qemu-desktop](https://archlinux.org/packages/?name=qemu-desktop) in order to revert [this commit](https://github.com/qemu/qemu/commit/143c30d4d346831a09e59e9af45afdca0331e819).
-   On qemu commandline, add `amd-stibp=off` to the cpu flags string. This can also be invoked through libvirt via a `<qemu:commandline>` entry.

## \"Error 43: Driver failed to load\" with mobile (Optimus/max-q) NVIDIA GPUs {#\"Error_43:_Driver_failed_to_load\"_with_mobile_(Optimus/max-q)_NVIDIA_GPUs}

This error occurs because the NVIDIA driver wants to check the status of the power supply. If no battery is present, the driver does not work. Whether [Libvirt](../../en/Libvirt.html "Libvirt") or QEMU, by default none of them provide the possibility to simulate a battery. This might also result in a reduced screen resolution and the NVIDIA Desktop Manager refusing to load when right-clicking the desktop, saying it requires Windows 10, a compatible GPU and the NVIDIA graphics driver.

You can however create and add a custom acpi table file to the virtual machine which will do the work.

First you have to create the custom acpi table file by saving the following file as SSDT1.dat (base64 encoded here):

    echo 'U1NEVKEAAAAB9EJPQ0hTAEJYUENTU0RUAQAAAElOVEwYEBkgoA8AFVwuX1NCX1BDSTAGABBMBi5f
    U0JfUENJMFuCTwVCQVQwCF9ISUQMQdAMCghfVUlEABQJX1NUQQCkCh8UK19CSUYApBIjDQELcBcL
    cBcBC9A5C1gCCywBCjwKPA0ADQANTElPTgANABQSX0JTVACkEgoEAAALcBcL0Dk=' | base64 -d > SSDT1.dat

Next you must add the processed file to the main domain of the virtual machine:

    <domain xmlns:qemu="http://libvirt.org/schemas/domain/qemu/1.0" type="kvm">
      ...
      <qemu:commandline>
        <qemu:arg value="-acpitable"/>
        <qemu:arg value="file=/path/to/your/SSDT1.dat"/>
      </qemu:commandline>
    </domain>

Make sure your XML file has the correct namespace in the `<domain>` tag as visible above, otherwise the XML verification will fail [\[1\]](https://www.reddit.com/r/VFIO/comments/ebo2uk/nvidia_geforce_rtx_2060_mobile_success_qemu_ovmf/).

## \"BAR 3: cannot reserve \[mem\]\" error in dmesg after starting virtual machine {#\"BAR_3:_cannot_reserve_[mem]\"_error_in_dmesg_after_starting_virtual_machine}

**This article or section needs expansion.**

**Reason:** This error is actually related to the boot_vgs issue and should be merged together with everything else concerning GPU ROMs. (Discuss in [Talk:PCI passthrough via OVMF/Troubleshooting#UEFI (OVMF) Compatibility in VBIOS](/index.php?title=Talk:PCI_passthrough_via_OVMF/Troubleshooting&action=edit&redlink=1 "Talk:PCI passthrough via OVMF/Troubleshooting (page does not exist)"))

With respect to [this article](https://www.linuxquestions.org/questions/linux-kernel-70/kernel-fails-to-assign-memory-to-pcie-device-4175487043/):

If you still have code 43 check [dmesg(1)](https://man.archlinux.org/man/dmesg.1) for memory reservation errors after starting up your virtual machine, if you have similar it could be the case:

    vfio-pci 0000:09:00.0: BAR 3: cannot reserve [mem 0xf0000000-0xf1ffffff 64bit pref]

Find out a PCI Bridge your graphics card is connected to. This will give actual hierarchy of devices:

    $ lspci -t

Before starting the virtual machine run the following lines, replacing IDs with actual values from previous output.

    # echo 1 > /sys/bus/pci/devices/0000\:00\:03.1/remove
    # echo 1 > /sys/bus/pci/rescan

**Note** Probably setting [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter") `video=efifb:off` is required as well. [\[2\]](https://pve.proxmox.com/wiki/Pci_passthrough#BAR_3:_can.27t_reserve_.5Bmem.5D_error)

In addition try adding kernel parameter `pci=realloc` which also [helps with hotplugging issues](https://github.com/Dunedan/mbp-2016-linux/issues/60#issuecomment-396311301).

## UEFI (OVMF) compatibility in VBIOS {#UEFI_(OVMF)_compatibility_in_VBIOS}

**This article or section is being considered for removal.**

**Reason:** Flashing your guest GPU for the purpose of a GPU passthrough is **never** good advice. A full section should be dedicated to VBIOS compatibility. (Discuss in [Talk:PCI passthrough via OVMF/Troubleshooting#UEFI (OVMF) Compatibility in VBIOS](/index.php?title=Talk:PCI_passthrough_via_OVMF/Troubleshooting&action=edit&redlink=1 "Talk:PCI passthrough via OVMF/Troubleshooting (page does not exist)"))

With respect to [this article](https://pve.proxmox.com/wiki/Pci_passthrough#How_to_known_if_card_is_UEFI_.28ovmf.29_compatible):

Error 43 can be caused by the GPU\'s VBIOS without UEFI support. To check whenever your VBIOS supports it, you will have to use [rom-parser](https://github.com/awilliam/rom-parser):

    $ git clone https://github.com/awilliam/rom-parser
    $ cd rom-parser && make

Dump the GPU VBIOS:

    # echo 1 > /sys/bus/pci/devices/0000:01:00.0/rom
    # cat /sys/bus/pci/devices/0000:01:00.0/rom > /tmp/image.rom
    # echo 0 > /sys/bus/pci/devices/0000:01:00.0/rom

And test it for compatibility:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ./rom-parser /tmp/image.rom
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Valid ROM signature found @600h, PCIR offset 190h
    PCIR: type 0 (x86 PC-AT), vendor: 10de, device: 1184, class: 030000
    PCIR: revision 0, vendor revision: 1
Valid ROM signature found @fa00h, PCIR offset 1ch
    PCIR: type 3 (EFI), vendor: 10de, device: 1184, class: 030000
    PCIR: revision 3, vendor revision: 0
        EFI: Signature Valid, Subsystem: Boot, Machine: X64
    Last image
```

To be UEFI compatible, you need a \"type 3 (EFI)\" in the result. If it is not there, try updating your GPU VBIOS. GPU manufacturers often share VBIOS upgrades on their support pages. A large database of known compatible and working VBIOSes (along with their UEFI compatibility status!) is available on [TechPowerUp](https://www.techpowerup.com/vgabios/).

Updated VBIOS can be used in the virtual machine without flashing. To load it in QEMU:

    -device vfio-pci,host=07:00.0,......,romfile=/path/to/your/gpu/bios.bin \

And in libvirt:

    <hostdev>
         ...
         <rom file='/path/to/your/gpu/bios.bin'/>
         ...
       </hostdev>

One should compare VBIOS versions between host and guest systems using [nvflash](https://www.techpowerup.com/download/nvidia-nvflash/) (Linux versions under *Show more versions*) or [GPU-Z](https://www.techpowerup.com/download/techpowerup-gpu-z/) (in Windows guest). To check the currently loaded VBIOS:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ./nvflash --version
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
Version               : 80.04.XX.00.97
...
UEFI Support          : No
UEFI Version          : N/A
UEFI Variant Id       : N/A ( Unknown )
UEFI Signer(s)        : Unsigned
...
```

And to check a given VBIOS file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ./nvflash --version NV299MH.rom
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
Version               : 80.04.XX.00.95
...
UEFI Support          : Yes
UEFI Version          : 0x10022 (Jul  2 2013 @ 16377903 )
UEFI Variant Id       : 0x0000000000000004 ( GK1xx )
UEFI Signer(s)        : Microsoft Corporation UEFI CA 2011
...
```

If the external ROM did not work as it should in the guest, you will have to flash the newer VBIOS image to the GPU. In some cases it is possible to create your own VBIOS image with UEFI support using [GOPUpd](https://www.win-raid.com/t892f16-AMD-and-Nvidia-GOP-update-No-requests-DIY.html) tool, however this is risky and may result in GPU brick.

**Warning** Failure during flashing may \"brick\" your GPU - recovery may be possible, but rarely easy and often requires additional hardware. **DO NOT** flash VBIOS images for other GPU models (different boards may use different VBIOSes, clocks, fan configuration). If it breaks, you get to keep all the pieces.

In order to avoid the irreparable damage to your graphics adapter it is necessary to unload the NVIDIA kernel driver first:

    # modprobe -r nvidia_modeset nvidia

Flashing the VBIOS can be done with:

    # ./nvflash romfile.bin

**Warning** **DO NOT** interrupt the flashing process, even if it looks like it is stuck. Flashing should take about a minute on most GPUs, but may take longer.

## Slowed down audio pumped through HDMI on the video card {#Slowed_down_audio_pumped_through_HDMI_on_the_video_card}

For some users, the virtual machine\'s audio slows down/starts stuttering/becomes demonic after a while when it is pumped through HDMI on the video card. This usually also slows down graphics. A possible solution consists of enabling MSI (Message Signal-Based Interrupts) instead of the default (Line-Based Interrupts).

In order to check whether MSI is supported or enabled, run the following command as root:

    # lspci -vs device | grep 'MSI:'

where *`device`* is the GPU\'s PCI address (e.g. `01:00.0`).

The output should be similar to:

    Capabilities: [60] MSI: Enable- Count=1/1 Maskable- 64bit+

A `-` after `Enable` means MSI is supported, but not used by the virtual machine, while a `+` says that the virtual machine is using it.

The procedure to enable it is quite complex, instructions and an overview of the setting can be found [here](https://forums.guru3d.com/showthread.php?t=378044).

On a Linux guest you can use [modinfo(8)](https://man.archlinux.org/man/modinfo.8) to see if there is option to enable MSI, for example:

    $ modinfo snd_hda_intel | grep msi

If there is, one can enable it by adding the relevant option to a [custom modprobe.d file](../../en/Kernel_module.html#Using_modprobe.d "Kernel module"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/snd-hda-intel.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
options snd-hda-intel enable_msi=1
```

Other hints can be found on the [lime-technology\'s wiki](https://lime-technology.com/wiki/index.php/UnRAID_6/VM_Guest_Support#Enable_MSI_for_Interrupts_to_Fix_HDMI_Audio_Support)^\[[dead\ link](https://en.wikipedia.org/wiki/Wikipedia:Link_rot "wikipedia:Wikipedia:Link rot")\ 2023-05-06---HTTP 404\]^, or [in this article](https://vfio.blogspot.it/2014/09/vfio-interrupts-and-how-to-coax-windows.html).

A UI tool called [MSI Utility (FOSS Version 2)](https://forums.guru3d.com/threads/windows-line-based-vs-message-signaled-based-interrupts-msi-tool.378044/) works with Windows 10 64-bit and simplifies the process.

In order to fix the issues, enabling MSI on the `.0` function of a NVIDIA card

    01:00.0 VGA compatible controller: NVIDIA Corporation GM206 [GeForce GTX 960] (rev a1) (prog-if 00 [VGA controller])

is not enough; it will also be required to enable it on the other function

    01:00.1 Audio device: NVIDIA Corporation Device 0fba (rev a1)

to fix the issue.

## No HDMI audio output on host when intel_iommu is enabled {#No_HDMI_audio_output_on_host_when_intel_iommu_is_enabled}

If after enabling `intel_iommu` the HDMI output device of Intel GPU becomes unusable on the host, setting the [kernel parameters](../../en/Kernel_parameters.html "Kernel parameters") `intel_iommu=on,igfx_off` might bring the audio back. Please read [iommu.html](https://docs.kernel.org/arch/x86/iommu.html#graphics-problems) for details about setting `igfx_off`.

## X does not start after enabling vfio_pci {#X_does_not_start_after_enabling_vfio_pci}

This is related to the host GPU being detected as a secondary GPU, which causes X to fail/crash when it tries to load a driver for the guest GPU. To circumvent this, a [Xorg configuration file](../../en/Xorg.html#Configuration "Xorg") specifying the BusID for the host GPU is required. The correct BusID can be acquired from `lspci -n` or the Xorg log [\[3\]](https://www.redhat.com/archives/vfio-users/2016-August/msg00025.html). Note that the value from the `lspci` output is hexadecimal and should be converted to decimal in the `.conf` file.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/X11/xorg.conf.d/10-intel.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Section "Device"
        Identifier "Intel GPU"
        Driver "modesetting"
        BusID  "PCI:0:2:0"
EndSection
```

## Chromium ignores integrated graphics for acceleration {#Chromium_ignores_integrated_graphics_for_acceleration}

[Chromium](../../en/Chromium.html "Chromium") and friends will try to detect as many GPUs as they can in the system and pick which one is preferred (usually discrete NVIDIA/AMD graphics).

It tries to pick a GPU by looking at PCI devices, not OpenGL renderers available in the system. The result is that Chromium may ignore the integrated GPU available for rendering and try to use the dedicated GPU bound to the `vfio-pci` driver (and unusable on the host system), regardless of whenever a guest virtual machine is running or not.

This results in software rendering being used (leading to higher CPU load, which may also result in choppy video playback, scrolling and general lack of smoothness).

This can be fixed by [explicitly telling Chromium which GPU you want to use](../../en/Chromium/Tips_and_tricks.html#Forcing_specific_GPU "Chromium/Tips and tricks").

## Virtual machine only uses one core {#Virtual_machine_only_uses_one_core}

For some users, even if [IOMMU](../../en/PCI_passthrough_via_OVMF.html#Setting_up_IOMMU "IOMMU") is enabled and the core count is set to more than `1`, the virtual machine still only uses one CPU core and thread. To solve this enable \"Manually set CPU topology\" in [virt-manager](../../en/Virt-manager.html "Virt-manager") and set it to the desirable amount of CPU sockets, cores and threads. Keep in mind that \"Threads\" refers to the thread count per CPU core, not the total count.

## Passthrough seems to work but no output is displayed {#Passthrough_seems_to_work_but_no_output_is_displayed}

If you are using [virt-manager](../../en/Virt-manager.html "Virt-manager"), ensure that [UEFI](../../en/Unified_Extensible_Firmware_Interface.html "UEFI") firmware is selected for your virtual machine. Also, make sure you have passed the correct device to the virtual machine.

## Host lockup after virtual machine shutdown {#Host_lockup_after_virtual_machine_shutdown}

This issue seems to primarily affect users running a Windows 10 guest and usually after the virtual machine has been run for a prolonged period of time: the host will experience multiple CPU core lockups (see [\[4\]](https://bbs.archlinux.org/viewtopic.php?id=206050&p=2)).

To fix this try enabling Message Signal-Based Interrupts (MSI) on the GPU passed through to the guest. A good guide for how to do this can be found in [\[5\]](https://forums.guru3d.com/threads/windows-line-based-vs-message-signaled-based-interrupts.378044/). You can also download this application for Windows here [\[6\]](https://github.com/TechtonicSoftware/MSIInturruptEnabler) that should make the process easier.

## Host lockup if guest is left running during sleep {#Host_lockup_if_guest_is_left_running_during_sleep}

VFIO-enabled virtual machines tend to become unstable if left running through a sleep/wakeup cycle and have been known to cause the host machine to lockup when an attempt is then made to shut them down.

In order to avoid this, one can simply prevent the host from going into sleep while the guest is running using the following [libvirt hook](../../en/Libvirt.html#Hooks "Libvirt") script and [systemd unit](../../en/Systemd.html#Writing_unit_files "Systemd"). The hook file needs [executable](../../en/Help:Reading.html#Make_executable "Executable") permissions to work.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/libvirt/hooks/qemu
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

OBJECT="$1"
OPERATION="$2"

case "$OPERATION" in
    prepare)
        systemctl start libvirt-nosleep@"$OBJECT"
        ;;
    release)
        systemctl stop libvirt-nosleep@"$OBJECT"
        ;;
    *)
        exit 0
        ;;
esac
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/libvirt-nosleep@.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=Preventing sleep while libvirt domain "%i" is running

[Service]
Type=simple
ExecStart=/usr/bin/systemd-inhibit --what=sleep --why="Libvirt domain \"%i\" is running" --who=%U --mode=block sleep infinity
```

## Bluescreen at boot since Windows 10 1803 {#Bluescreen_at_boot_since_Windows_10_1803}

Since Windows 10 1803, there is a problem when you are using \"host-passthrough\" as cpu model. The machine may be unable to boot and it either starts boot looping or you may get a BSOD. You can workaround this by using the following [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter"):

    # echo 1 > /sys/module/kvm/parameters/ignore_msrs

To make it permanently you can create a [modprobe.d file](../../en/Kernel_module.html#Using_modprobe.d "Kernel module") `kvm.conf`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/kvm.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
options kvm ignore_msrs=1
```

To prevent clogging up [dmesg](../../en/Core_utilities.html#Essentials "Dmesg") with \"ignored rdmsr\" messages you can additionally add:

    options kvm report_ignored_msrs=0

## AMD Ryzen / BIOS updates (AGESA) yields \"Error: internal error: Unknown PCI header type '127'\" {#AMD_Ryzen_/_BIOS_updates_(AGESA)_yields_\"Error:_internal_error:_Unknown_PCI_header_type_‘127’\"}

AMD users have been experiencing breakage of their KVM setups after updating the BIOS on their motherboard. There is a kernel [patch](https://clbin.com/VCiYJ)^\[[dead\ link](https://en.wikipedia.org/wiki/Wikipedia:Link_rot "wikipedia:Wikipedia:Link rot")\ 2024-07-30---HTTP 404\]^, (see [Kernel/Arch build system](../../en/Kernel/Arch_build_system.html "Kernel/Arch build system") for instruction on compiling kernels with custom patches) that can resolve the issue as of now (28th July 2019), but this is not the first time AMD has made an error of this very nature, so take this into account if you are considering updating your BIOS in the future as a VFIO user.

## AMD GPU not resetting properly yielding \"Error: internal error: Unknown PCI header type '127'\" (Separate issue from the one above) {#AMD_GPU_not_resetting_properly_yielding_\"Error:_internal_error:_Unknown_PCI_header_type_‘127’\"_(Separate_issue_from_the_one_above)}

Passing through an AMD GPU may result into a problem known as the \"AMD reset bug\". Upon power cycling the guest, the GPU does not properly reset its state, which causes the device to malfunction until the host is also rebooted. This is usually paired with a `code 43` driver error in a Windows guest, and the message `Error: internal error: Unknown PCI header type '127'` in the libvirt log on the host.

In the past, this meant having to use workarounds to manually reset the GPU, or resorting to the use of kernel patches that were unlikely to land in upstream. Currently, the recommended solution that does not require patching of the kernel is to install [vendor-reset-git](https://aur.archlinux.org/packages/vendor-reset-git/)^AUR^ or [vendor-reset-lowell80-dkms-git](https://aur.archlinux.org/packages/vendor-reset-lowell80-dkms-git/)^AUR^ and making sure the `vendor-reset` kernel module is loaded before booting the guest.

For convenience, you can load the module automatically, either [at boot time](../../en/Kernel_module.html#systemd "Kernel module") or with a [libvirt hook](../../en/Libvirt.html#Hooks "Libvirt"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/libvirt/hooks/qemu
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

OPERATION="$2"

case "$OPERATION" in
    prepare)
        modprobe -s vendor-reset
        ;;
    release)
        modprobe -sr vendor-reset
        ;;
    *)
        exit 0
        ;;
esac
```

Make the file [executable](../../en/Help:Reading.html#Make_executable "Executable"), if needed.

**Note** Make sure you do not have any of the AMD reset bug kernel patches installed if you are using [vendor-reset-git](https://aur.archlinux.org/packages/vendor-reset-git/)^AUR^ or [vendor-reset-lowell80-dkms-git](https://aur.archlinux.org/packages/vendor-reset-lowell80-dkms-git/)^AUR^.

## Host crashes when hotplugging NVIDIA card with USB {#Host_crashes_when_hotplugging_NVIDIA_card_with_USB}

If attempting to hotplug an NVIDIA card with a USB port, you may have to blacklist the `i2c_nvidia_gpu` driver. You can achieve this by creating a [modprobe.d file](../../en/Kernel_module.html#Using_modprobe.d "Kernel module"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/blacklist.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
blacklist i2c_nvidia_gpu
```

## Host unable to boot and stuck in black screen after enabling vfio {#Host_unable_to_boot_and_stuck_in_black_screen_after_enabling_vfio}

If debug kernel messages during boot are enabled by adding with the `debug ignore_loglevel` [kernel parameters](../../en/Kernel_parameters.html "Kernel parameters"), you may see boot stuck with the last message similar to:

    vfio-pci 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=io+mem:owns=none

This can be mitigated by disconnecting the passed-through GPU from your monitor. You may reconnect the passed-through GPU to a monitor after the host has booted.

If you do not want to plug the cable in each time you boot the host, you can disable the framebuffer in your boot loader to bypass this message. For [UEFI](../../en/Unified_Extensible_Firmware_Interface.html "UEFI") systems you can add `video=efifb:off` as a [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter"). For legacy support, use `video=vesafb:off` instead or in conjunction. Note that doing this may cause issues with [Xorg](../../en/Xorg.html "Xorg").

If you encounter problems with Xorg, the following solution may help (remember to substitute with your own values):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/X11/xorg.conf.d/10-amd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Section "Device"
        Identifier "AMD GPU"
        Driver "amdgpu"
        BusID  "PCI:0:2:0"
EndSection
```

## AER errors when passing through PCIe USB hub {#AER_errors_when_passing_through_PCIe_USB_hub}

In some cases, passing through a PCIe USB hub, such as one connected to the guest GPU, might fail with AER errors similar to the following:

    kernel: pcieport 0000:00:01.1: AER: Uncorrected (Non-Fatal) error received: 0000:00:01.1
    kernel: pcieport 0000:00:01.1: AER: PCIe Bus Error: severity=Uncorrected (Non-Fatal), type=Transaction Layer, (Requester ID)
    kernel: pcieport 0000:00:01.1: AER:   device [8086:1905] error status/mask=00100000/00000000
    kernel: pcieport 0000:00:01.1: AER:    [20] UnsupReq               (First)
    kernel: pcieport 0000:00:01.1: AER:   TLP Header: 00000000 00000000 00000000 00000000
    kernel: pcieport 0000:00:01.1: AER: device recovery successful

## Reserved Memory Region Reporting (RMRR) Conflict {#Reserved_Memory_Region_Reporting_(RMRR)_Conflict}

If you run into an issue passing through a device because of the BIOS\'s usage of RMRR, like the error below:

    vfio-pci 0000:01:00.1: Device is ineligible for IOMMU domain attach due to platform RMRR requirement. Contact your platform vendor.

You can try the patches here: [\[7\]](https://github.com/kiler129/relax-intel-rmrr)

## Too-low frequency limit for AMD GPU passed-through to virtual machine {#Too-low_frequency_limit_for_AMD_GPU_passed-through_to_virtual_machine}

On some machines with AMD GPUs, binding the devices to `vfio-pci` may be insufficient to prevent interference from the host, since the [amdgpu](../../en/AMDGPU.html "Amdgpu") driver on the host may query global ATIF methods which can alter the behavior of the GPU.

For example, a user with a Dell Precision 7540 laptop containing a Radon Pro WX 3200 AMD GPU reported that, with the AMD GPU bound to `vfio-pci`, the passed-through AMD GPU was limited to `501 MHz` instead of the correct `1295 MHz` limit. [Blacklisting](../../en/Kernel_module.html#Blacklisting "Blacklisting") the amdgpu kernel module using the kernel command line was a workaround.

See [this kernel mailing list discussion](https://lore.kernel.org/regressions/092b825a-10ff-e197-18a1-d3e3a097b0e3@leemhuis.info/T/) for further details.

## Host clocksource is HPET rather than TSC {#Host_clocksource_is_HPET_rather_than_TSC}

If the clocksource of your host machine is HPET, you may see severely crippled performance in games. While this issue also occurs when running games outside of a virtual machine, unaware users will likely begin troubleshooting their virtual machine when the issue is actually with their host system.

To see your current clocksource, run this command on your host machine:

    $ cat /sys/devices/system/clocksource/clocksource*/current_clocksource

If your clocksource is HPET, you can try to force it to TSC by setting the [kernel parameters](../../en/Kernel_parameters.html "Kernel parameters") `clocksource=tsc` and `tsc=reliable`. See [this Reddit thread](https://www.reddit.com/r/linux_gaming/comments/rsvjqb/psa_if_your_clocksource_is_hpet_rather_than_tsc/) for more information.

## Code 43 while Resizable Bar is turned on in the bios {#Code_43_while_Resizable_Bar_is_turned_on_in_the_bios}

If you own a GPU that supports Resizable BAR / SAM and have the corresponding BIOS option enabled, you might get code 43 because this feature is disabled in QEMU [\[8\]](https://github.com/qemu/qemu/commit/3412d8ec9810b819f8b79e8e0c6b87217c876e32). Linux Kernel release 6.1 added option to manipulate PCIe Resizable BARs through [sysfs](https://en.wikipedia.org/wiki/sysfs "wikipedia:sysfs"), so you can try permanently resizing it using a [udev](../../en/Udev.html "Udev") rule:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/udev/rules.d/01-amd.rules
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x1002", ATTR{device}=="0x73bf", ATTR{resource0_resize}="14"
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x1002", ATTR{device}=="0x73bf", ATTR{resource2_resize}="8"
```

Alternatively, to temporarily resize the PCIe BAR, you can write the new size to `/sys/bus/pci/devices/`**`device_address`**`/resource`**`number`**`_resize`, where *device_address* is the address of your GPU, such as `0000:03:00.0` (note that for changing this parameter, no driver can be loaded for the device).

You can confirm values using `lspci -vvvxxxx`.

AMD graphics processors may require a specific value to be set for BAR 2, which is 8 MB, even though the maximum supported value is 256 MB. However, this requirement may depend on several factors, such as the QEMU version on your system. If you have already exhausted other options to prevent error code 43, set the value to `3` in the `resource2_resize` file, which will force BAR 2 to be set to 8 MB.

## Operating system hangs {#Operating_system_hangs}

If your virtualized OS (particularly Windows) hangs when the GPU is attached, you can also try opening your motherboard\'s settings and:

-   disabling `Re-Size BAR Support`,
-   disabling `Above 4G memory / Crypto Currency mining`,
-   enabling `SR-IOV`,
-   changing `Max TOLUD` from `dynamic` to a specific value,
-   switching your `Initiate Graphic Adapter` from `PEG` to `IGD`.

At the very least, VEGA cards seem to be picky about those settings and won\'t actually work unless you change them.

## GPU timeouts when running games in the virtual machine {#GPU_timeouts_when_running_games_in_the_virtual_machine}

Starting with recent kernels (6.12+ for AMD, 5.x for Intel), split lock detection is enabled by default. This causes a forced 10ms pause for the process creating the split lock, which can result in GPU timeouts and similar virtual machine hanging. This behavior can be disabled by running:

    # sysctl -w kernel.split_lock_mitigate=0

This can be applied automatically with a [sysctl](../../en/Sysctl.html "Sysctl") configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/sysctl.d/split-lock.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
kernel.split_lock_mitigate = 0
```

## vfio: DMA mapping failed, unable to continue {#vfio:_DMA_mapping_failed,_unable_to_continue}

When starting the virtual machine, an error like `qemu: hardware error: vfio: DMA mapping failed, unable to continue` may occur and prevent the VM from booting. To fix this, add the following to the XML file: [\[9\]](https://github.com/tianocore/edk2/discussions/4662#discussioncomment-6541549)

    <cpu>
      <maxphysaddr mode="passthrough" limit="40"/>
    </cpu>

If directly using QEMU, the example above would be `-cpu host,host-phys-bits-limit=`**`0x28`**.

If the VM still doesn\'t work, try decreasing the value (like **39** and **0x27**, respectively).

You can use [lscpu(1)](https://man.archlinux.org/man/lscpu.1) to see the actual address size of your CPU and use it rather than the values shown above. Unless you need a large address space, it\'s safer to choose the physical address size intead of the virtual size.

## vIOMMU: Failed to set vIOMMU: aw-bits X \> host aw-bits Y {#vIOMMU:_Failed_to_set_vIOMMU:_aw-bits_X_>_host_aw-bits_Y}

When starting the virtual machine, an error like the following may occur:

    libvirt.libvirtError: internal error: QEMU unexpectedly closed the monitor (vm='win11'): 2025-08-30T21:38:26.333149Z qemu-system-x86_64: -device {"driver":"vfio-pci","host":"0000:03:00.0","id":"hostdev0","bus":"pci.5","addr":"0x0"}: vfio 0000:03:00.0: Failed to set vIOMMU: aw-bits 48 > host aw-bits 39

Add `caching_mode="on" aw_bits="`**`number_of_bits`**`"` to the following section in your XML. Usually on x86 the default is either 39 or 48 bits [\[10\]](https://patchew.org/QEMU/20240123181753.413961-1-eric.auger@redhat.com/), but [you can use your own CPU\'s address size instead](#vfio:_DMA_mapping_failed,_unable_to_continue).

     <devices>
      ... other entries ...
      <iommu model="intel">
        <driver intremap="on" caching_mode="on" eim="on" aw_bits="39"/>
      </iommu>
     </devices>

For more information:

-   [Proxmox forum thread discussing this](https://forum.proxmox.com/threads/vm-wont-start-with-pci-passthrough-after-upgrade-to-9-0.169586/post-795732)
-   [libvirt options](https://libvirt.org/formatdomain.html#iommu-devices)

## The VM stucks during boot when using Looking Glass {#The_VM_stucks_during_boot_when_using_Looking_Glass}

Sometimes, when using [Looking Glass](../../en/PCI_passthrough_via_OVMF.html#Using_Looking_Glass_to_stream_guest_screen_to_the_host "PCI passthrough via OVMF"), the VM may get stuck indefinitely at the boot process [\[11\]](https://www.reddit.com/r/VFIO/comments/16a8xzb/comment/k87n4ai/). This might be caused by divergences between P-Core and E-Core specs on new processors with hybrid architectures.

To solve this, follow [these instructions](#vfio:_DMA_mapping_failed,_unable_to_continue). It\'s better to pick the physical address size instead of the virtual address size [\[12\]](https://www.reddit.com/r/VFIO/comments/16a8xzb/comment/le7obu0/).
