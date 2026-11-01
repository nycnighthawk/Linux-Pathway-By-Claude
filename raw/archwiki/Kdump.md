---
{"title": "Kdump", "url": "https://wiki.archlinux.org/title/Kdump", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Kdump

Related articles

-   [Kexec](../en/Kexec.html "Kexec")

[Kdump](https://docs.kernel.org/admin-guide/kdump/kdump.html) is a standard Linux mechanism to dump machine memory content on kernel crash. Kdump is based on [Kexec](../en/Kexec.html "Kexec"). Kdump utilizes two kernels: the regular system kernel and kdump capture kernel (called from now on, the kdump kernel). System kernel is the normal kernel, booted with the `crashkernel` parameter - we need to tell the system kernel to reserve some amount of physical memory where the kdump kernel will be loaded/executed. Then it is necessary to load the kdump kernel in advance, because when the system kernel crashes, there is no reliable way to read data from disk, for example, given that such kernel is broken.

Once a kernel crash happens, the system kernel crash handler uses the [Kexec](../en/Kexec.html "Kexec") mechanism to boot the kdump kernel in its pre-reserved memory. The memory from system kernel is preserved in such kexec boot, and it is accessible from the kdump kernel at the moment of crash. Once the kdump kernel is booted, the user can collect the file `/proc/vmcore` to get access to memory of the crashed system kernel. Such crash dump can be saved to disk or copied over network to some other machine for further post-mortem investigation.

In server production environments, the system and kdump kernels could be different - system kernel needs a lot of features and is compiled with a many kernel flags/drivers, while the kdump kernel goal is to be minimalistic and take as small amount of memory as possible, e.g. it could be compiled without network support if we store the crash dump to disk only. But for desktops and in general, for non-specific setups, the same kernel is used both as system and kdump kernels. It means we will load the same kernel code twice - one time as normal system kernel, another one to the reserved memory area, but with different kernel parameters.

## Alternatives to setup kdump {#Alternatives_to_setup_kdump}

### The automatic way: kdumpst {#The_automatic_way:_kdumpst}

**Note** kdumpst implicitly depends on GRUB and does not work with other [boot loaders](../en/Boot_loader.html "Boot loader"), see [https://gitlab.freedesktop.org/gpiccoli/kdumpst/-/issues/21](https://gitlab.freedesktop.org/gpiccoli/kdumpst/-/issues/21)

The [kdumpst](https://aur.archlinux.org/packages/kdumpst/)^AUR^ tool is an automatic way for loading kdump. It is highly customizable - it defaults to another method of log collecting (called pstore), but can be easily set to use kdump (a matter of setting `USE_PSTORE_RAM=0` on `/usr/share/kdumpst.d/00-default`. The tool also fallbacks to kdump in case pstore RAM region is not available.

After installing kdumpst, one can check the journal and the following message means kdump is loaded: `kdumpst: panic kexec loaded successfully`. If a kernel crash happens, the kdump will be collected and in the subsequent boot, a message indicates the success of the operation: `kdumpst: logs saved in "/var/crash/kdumpst/logs"`. In that folder, the user will find a lightweight zip blob, that included a dmesg plus some extra data. The vmcore itself is saved on `/var/crash/kdumpst/crash`. For questions/issues, the #kdump IRC channel at OFTC could be used, or open issues in the kdumpst repository.

### The automatic way: simple-kdump {#The_automatic_way:_simple-kdump}

The [simple-kdump](https://aur.archlinux.org/packages/simple-kdump/)^AUR^ tool provides a simple and easy-to-config way to setup and collect kdump. Unlike [kdumpst](https://aur.archlinux.org/packages/kdumpst/)^AUR^, it is boot loader independent, has one and only one objective, save the vmcore file to `/var/crash/`.

It is mostly all the manual setups mentioned in later sections with slightly better organization using systemd, but re-use the Arch Linux kernels (or whatever kernel the end user choose), so it is super flex and simple.

After installing [simple-kdump](https://aur.archlinux.org/packages/simple-kdump/)^AUR^, fill `/etc/conf.d/simple-kdump.conf` using any booting kernel/initramfs combination, which has the `CONFIG_PROC_VMCORE=y` enabled. It is recommended to use the Arch Linux linux or linux-lts kernel, which already have all the needed features enabled.

Then add `crashkernel=[size]` [kernel parameter](../en/Kernel_parameter.html "Kernel parameter") and reboot. Recommended to use value no smaller than 512M

Finally enable and start `simple-kdump-setup.service`, then refer to [#Testing kdump by crashing the kernel](#Testing_kdump_by_crashing_the_kernel) to verify the kdump behavior.

The kexec kernel should reach target `Emergency Mode to collect vmcore`, with a prompt asking login for the emergency shell. You can ignore that login as the vmcore collection will happen at the background and reboot automatically.

After the reboot, there should be a new crash dump at `/var/crash/crashdump-*`.

**Note** The default `BOOT_OPTIONS` in `/etc/conf.d/simple-kdump.conf` are placeholders (`root=/dev/os/root`). They must be replaced with the same `root=`, `rootflags=`, `rootfstype=` and any decryption parameters used by your normal boot, otherwise the kexec kernel cannot mount the root filesystem and `/var/crash/` will stay empty. Do **not** include `crashkernel=` or `quiet`; the service appends `nr_cpus=1 reset_devices systemd.unit=emergency-kdump.target` itself. After editing, run `systemctl restart simple-kdump-setup.service` to reload the kexec image.

**Note** If the root filesystem is on [dm-crypt](../en/Dm-crypt.html "Dm-crypt")/LUKS, the kexec environment will prompt for the passphrase on the console before it can write the vmcore. This requires an additional `1G` of memory for the kexec kernel for the keyslot, on top of the memory needed for the crashkernel itself. The `encrypt` hook (or `sd-encrypt`) must also be present in the initramfs used for kdump (it is, by default, on installs that already boot from LUKS). For fully unattended capture, store the dump on a separate, unencrypted partition and adjust `simple-kdump-collect.service` accordingly, or temporarily unlock the root device via a keyfile embedded in the initramfs (see [Dm-crypt/Device encryption#Keyfiles](../en/Dm-crypt/Device_encryption.html#Keyfiles "Dm-crypt/Device encryption")).

### Manual steps {#Manual_steps}

In case the preference is for doing that manually, the below guide will help with that.

#### Compiling kernel {#Compiling_kernel}

Both System/kdump kernels requires some configuration flags that may not be set by default. Please consult [Kernel Compilation](../en/Kernel_Compilation.html "Kernel Compilation") article for more information about compiling a custom kernel in Arch. Here we will emphasize on Kdump specific configurations. Current default Arch kernel builds have these flags already set. You can verify if your running kernel has these set by looking in `/proc/config.gz`.

Please note that, the default [linux](https://archlinux.org/packages/?name=linux) and [linux-lts](https://archlinux.org/packages/?name=linux-lts) kernels all have the needed options enabled. But unfortunately the default kernels have debug info striped, thus one still needs to recompile the kernel to have all the debug info so that the vmcore can be properly analyzed.

To create a kernel you need to edit the kernel `.config` file and enable following configuration options:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
.config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
CONFIG_DEBUG_INFO=y
CONFIG_CRASH_DUMP=y
CONFIG_PROC_VMCORE=y
CONFIG_DEBUG_INFO=y
COFNIG_DEBUG_INFO_BTF=y
```

The last two are for the extra debuginfo so that tools like [crash](https://archlinux.org/packages/?name=crash) or [drgn](https://archlinux.org/packages/?name=drgn) can analyze the vmcore. (Or is there a way to use debuginfod to download the kernel debuginfo?)

Also change package base name to something like **linux-kdump** to distinguish the kernel from the default Arch one. Compile kernel package and install it. Save *./src/linux-X.Y/vmlinux* uncompressed system kernel binary - it contains debug symbols and you will need them later when analyzing the crash.

For reference, some details about building a kdump kernel or configuring the kernel parameters for kdump could be found in the kernel [Kdump](https://docs.kernel.org/admin-guide/kdump/kdump.html) documentation.

#### Reuse existing kernel and initramfs {#Reuse_existing_kernel_and_initramfs}

The simplest way to setup kdump is to use the existing kernel and initramfs. The example here will use [linux](https://archlinux.org/packages/?name=linux) kernel as an example, which generates its initramfs at `/boot/initramfs-linux.img`.

The core idea is to boot the kexec environment just as a regular Arch Linux boot sequence. But with extra systemd options to slightly change the boot sequence (to skip re-setup kexec environment, collect vmcore, and reboot).

Thus we do not need to generate a special initramfs, unlike other distros (and our default initramfs generated by [mkinitcpio](../en/Mkinitcpio.html "Mkinitcpio") is already way smaller than our competitors).

#### Setup the kdump kernel {#Setup_the_kdump_kernel}

First, you need to reserve memory in the system kernel, for the kdump kernel loading. Edit your boot loader configuration and add `crashkernel=[size]` [kernel parameter](../en/Kernel_parameter.html "Kernel parameter").

Depending on the machine and how the kdump kernel was built, something from *256M* to *512M* is usually enough - it worth trying after setting everything to check if it succeeds. Note that the reserved memory is unavailable to the system kernel.

Reboot into your system kernel. To make sure that the kernel is booted with correct options please check the files `/proc/cmdline` and `/sys/kernel/kexec_crash_size` to see if the memory was indeed pre-reserved (sometimes it is possible, though rare, that such memory reservation fails - if it happens, check the `dmesg` to get more information).

Next you need to tell [Kexec](../en/Kexec.html "Kexec") that you want to use your kdump kernel. Specify your kernel, initramfs file, root device and other parameters if needed: (here we use default [linux](https://archlinux.org/packages/?name=linux) kernel)

    # kexec -p /boot/vmlinuz-linux --initrd=/boot/initramfs-linux.img] --append="root=[root-device] irqpoll nr_cpus=1 reset_devices"

It loads the kdump kernel into the reserved area. Without the `-p` flag *kexec* would boot the kernel right away, but in presence of such flag, the kdump kernel will be loaded into the reserved memory but its boot is postponed until a crash happens.

**Note** The parameter `nr_cpus=1` restricts the CPUs to 1 in the kdump environment, which is both memory saving (CPUs structures consume memory!) and also safer, as it restricts the surface for potential concurrency issues. If that option for some reason fails, there is another one to be used, instead: `maxcpus=1`. The second one consumes a bit more memory, since it initializes other CPUS structures but disables such CPUS except CPU0, whereas the `nr_cpus` one effectively drops the other CPUs structures. More information in the kernel [CPU hotplug](https://docs.kernel.org/core-api/cpu_hotplug.html) docs.

Instead of running *kexec* manually you might want to setup [Systemd](../en/Systemd.html "Systemd") service that will run kexec on boot:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/kdump.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=Load the kdump kernel
After=local-fs.target

[Service]
Type=oneshot
RemainAfterExit=true
ExecStart=/usr/bin/kexec -p /boot/vmlinuz-linux --initrd=/boot/initramfs-linux.img --append="root=[root-device] irqpoll nr_cpus=1 reset_devices systemd.mask=kdump.service"
ExecStop=/usr/bin/kexec -p -u

[Install]
WantedBy=multi-user.target
```

Then [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") `kdump.service`.

Note, since the service is enabled, and our kexec environment boots exactly like a regular boot, it will try to start `kdump.service` but fail since there is not enough memory. Thus in the `--append=` option, `systemd.mask=kdump.service` is specified to avoid the kdump service itself.

To check whether the crash kernel is already loaded please run following command:

    $ cat /sys/kernel/kexec_crash_loaded

#### Testing kdump by crashing the kernel {#Testing_kdump_by_crashing_the_kernel}

If you want to test crash then you can use *sysrq* for this.

**Warning** a kernel crash may corrupt data on your disks, run it at your own risk!

    # sync; echo 1 > /proc/sys/kernel/sysrq; echo c > /proc/sysrq-trigger

Once crash happens kexec will load your kdump kernel, which should look exactly like a regular boot, but with much smaller memory (the reserved size) and only one CPU core.

#### Saving the crashed kernel memory {#Saving_the_crashed_kernel_memory}

Once booted into the kdump kernel, the idea is to save the relevant contents from `/proc/vmcore` to analyze it later. Though this is exposed as a file (hence it is possible to copy it, like in `cp /proc/vmcore /root/vmcore.crashdump`, this is not the recommended way. The vmcore is a full copy of system memory, so this file will have 64G if your machine has 64G, for example. It includes all data from all the userpace loaded, as well as free memory. So, the best way for saving it is use the `makedumpfile` utility. Such application is able to remove free memory and userspace irrelevant data, as well as compress the vmcore! Example of the usage:

    # makedumpfile -z -d 31 /proc/vmcore /root/vmcore.crashdump_compressed

You can also save out the dmesg log from the crashed kernel using this command:

    # makedumpfile --dump-dmesg /proc/vmcore /root/vmcore.dmesg

The following systemd service can be used to automatically save the crash dumps and reboot into the system kernel again:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/kdump-save.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=Save the kernel crash dump after a crash
After=multi-user.target

[Service]
Type=idle
ExecStart=/bin/sh -c 'mkdir -p /var/crash/ && /usr/bin/makedumpfile -z -d 31 /proc/vmcore "/var/crash/crashdump-$$(date +%%F-%%T)"'
ExecStopPost=/usr/bin/systemctl reboot
UMask=0077
```

This can be invoked from the kdump kernel command line - for that, we should edit the kdump load service as below:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/kdump.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=Load the kdump kernel
After=local-fs.target

[Service]
Type=oneshot
RemainAfterExit=true
ExecStart=/usr/bin/kexec -p /boot/vmlinuz-linux --initrd=/boot/initramfs-linux.img --append="root=[root-device] irqpoll nr_cpus=1 reset_devices systemd.mask=kdump.service systemd.unit=kdump-save.service"
ExecStop=/usr/bin/kexec -p -u

[Install]
WantedBy=multi-user.target
```

#### Early kdump using mkinitcpio {#Early_kdump_using_mkinitcpio}

You might encounter a situation where the kernel crashes before the systemd service can be started. In this case, it might be helpful to run kexec as a mkinitcpio hook rather than a service.

First make a copy of your initramfs. This will be used to run the crash kernel.

    # cp /boot/initramfs-linux.img /boot/initramfs-linux-crash.img

Next, create the mkinitcpio install file. This builds allows us to build the main initramfs with a copy of the crash initramfs for the crash kernel and the

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/initcpio/install/kdump
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
build() {
        add_binary kexec
        add_file /boot/initramfs-linux-crash.img /crash/initramfs.img
        add_file /boot/vmlinuz-linux /crash/vmlinuz
        add_runscript
}

help() {
        cat <<HELPEOF
Installs the crash kernel on boot
HELPEOF
}
```

Next, make the mkinitcpio hook file. This runs kexec as an earlyhook, hopefully before anything in the kernel can crash. An important note here is that we run the kernel in emergency mode, because running the kernel in rescue or normal might might just lead to another the same crash happening in the crash kernel.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/initcpio/hook/kdump
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
run_earlyhook() {
    msg 'Loading crash kernel..'
    if [ -e /crash/vmlinuz ]; then
        if [ -e /crash/initramfs.img ]; then
            kexec -p /crash/vmlinuz --initrd=/crash/initramfs.img --append="root=[root-device] irqpoll nr_cpus=1 reset_devices emergency"
        else
            msg 'No initramfs found'
        fi
    else
        msg 'No vmlinuz found'
    fi
}
```

Now run mkinitcpio with the new hook

    # mkinitcpio -A kdump

When the crash happens, you will be loaded into emergency kernel mode. After entering your password, you will be at a terminal. The first thing you will need to do is make your root filesystem writable.

    $ mount -o remount, rw /

Now you can save the dump using makedumpfile (see [#Saving the crashed kernel memory](#Saving_the_crashed_kernel_memory))

## Analyzing the kernel core dump {#Analyzing_the_kernel_core_dump}

The best way for studying the saved kernel core dump involves tools aimed specifically at that. The most common alternative is the gdb-based [crash](https://archlinux.org/packages/?name=crash). Run *crash* as in

    $ crash vmlinux path/crash.dump

Where the *vmlinux* should contain debug symbols included in order to extract more information from the saved crash dump.

Follow *man crash* or [\[1\]](https://crash-utility.github.io/crash_whitepaper.html) for more information about debugging practices.

Another recent alternative is [drgn](https://archlinux.org/packages/?name=drgn), a python-based and fully scriptable tool to extract information from the vmcore.

## See also {#See_also}

-   [https://docs.kernel.org/admin-guide/kdump/kdump.html](https://docs.kernel.org/admin-guide/kdump/kdump.html) - Official kdump documentation
-   [https://www.dedoimedo.com/computers/www.dedoimedo.com-crash-book.pdf](https://www.dedoimedo.com/computers/www.dedoimedo.com-crash-book.pdf) - The crash book
-   [https://gitlab.freedesktop.org/gpiccoli/kdumpst/](https://gitlab.freedesktop.org/gpiccoli/kdumpst/) - kdumpst repository
-   [https://crash-utility.github.io](https://crash-utility.github.io) - The crash website
-   [https://drgn.readthedocs.io/](https://drgn.readthedocs.io/) - The drgn documentation website
