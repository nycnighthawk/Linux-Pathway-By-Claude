---
{"title": "Improving performance/Boot process", "url": "https://wiki.archlinux.org/title/Improving_performance/Boot_process", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Improving performance/Boot process

Related articles

-   [Improving performance](../../en/Improving_performance.html "Improving performance")
-   [Silent boot](../../en/Silent_boot.html "Silent boot")
-   [Daemon](../../en/Systemd.html "Daemon")
-   [Kexec](../../en/Kexec.html "Kexec")

Improving the boot performance of a system can provide reduced boot wait times and serves as a means to learn more about how certain system files and scripts interact with one another. This article attempts to aggregate methods on how to improve the boot performance of an Arch Linux system.

## Analyzing the boot process {#Analyzing_the_boot_process}

### Using systemd-analyze {#Using_systemd-analyze}

[systemd](../../en/Systemd.html "Systemd") provides a tool called `systemd-analyze` that can be used to show timing details about the boot process, including an svg plot showing units waiting for their dependencies. You can see which unit files are causing your boot process to slow down. You can then optimize your system accordingly.

To see how much time was spent in kernelspace and userspace on boot, simply use:

    $ systemd-analyze

**Tip** If you boot via [UEFI](../../en/Unified_Extensible_Firmware_Interface.html "UEFI") and use a boot loader which implements systemd\'s [Boot Loader Interface](https://systemd.io/BOOT_LOADER_INTERFACE/) (which currently [systemd-boot](../../en/Systemd-boot.html "Systemd-boot") and [GRUB](../../en/GRUB.html "GRUB") do), *systemd-analyze* can additionally show you how much time was spent in the EFI firmware and the boot loader itself.

To list the started unit files, sorted by the time each of them took to start up:

    $ systemd-analyze blame

At some points of the boot process, things can not proceed until a given unit succeeds. To see which units find themselves at these critical points in the startup chain, do:

    $ systemd-analyze critical-chain

You can also create an SVG file which describes your boot process graphically, similar to [Bootchart](../../en/Bootchart.html "Bootchart"):

    $ systemd-analyze plot > plot.svg

See [systemd-analyze(1)](https://man.archlinux.org/man/systemd-analyze.1) for details.

### Using bootchart2 {#Using_bootchart2}

You could also use [Bootchart2](../../en/Bootchart.html#Bootchart2 "Bootchart") to visualize the boot sequence.

## Compiling a custom kernel {#Compiling_a_custom_kernel}

Compiling a custom kernel can reduce boot time and memory usage. Though with the standardization of the 64-bit architecture and the modular nature of the Linux kernel, these benefits may not be as great as expected. See [Kernel#Compilation](../../en/Kernel.html#Compilation "Kernel") for more info.

Compression level of modules of official kernel is built with `ZSTD_CLEVEL=19`. But `ZSTD_CLEVEL=1` may be better for SSD.

It is recommended to make modules for storage and file system for your root volume built-in to allow [running without initramfs](../../en/Arch_boot_process.html#Running_without_initramfs "Arch boot process").

## Initramfs {#Initramfs}

If possible in your setup, [running without initramfs](../../en/Arch_boot_process.html#Running_without_initramfs "Arch boot process") should provide the fastest way.

[mkinitcpio](../../en/Mkinitcpio.html "Mkinitcpio") uses the optional `base` hook by default, faster boot times can be achieved by omitting it. See [Mkinitcpio#Common hooks](../../en/Mkinitcpio.html#Common_hooks "Mkinitcpio") for more details. See also [Fsck#Boot time checking](../../en/Fsck.html#Boot_time_checking "Fsck") if replacing the `fsck` hook.

In a similar approach to [#Compiling a custom kernel](#Compiling_a_custom_kernel), the initramfs can be slimmed down. A simple way is to include the [mkinitcpio](../../en/Mkinitcpio.html "Mkinitcpio") `autodetect` hook. [Booster](../../en/Booster.html "Booster") generates initramfs smaller than [mkinitcpio](../../en/Mkinitcpio.html "Mkinitcpio") or [dracut](../../en/Dracut.html "Dracut") with fast single binary init. See [Minimal initramfs](../../en/Minimal_initramfs.html "Minimal initramfs") or [Booster#Removing modules](../../en/Booster.html#Removing_modules "Booster").

Depending on your hardware (processor and storage speed), using [lz4](https://archlinux.org/packages/?name=lz4) instead of the default [zstd](https://archlinux.org/packages/?name=zstd) compression option may be quicker since the faster decompression speed at boot time usually offsets the slightly larger size of the initramfs that has to be read from disk. See [Mkinitcpio#COMPRESSION](../../en/Mkinitcpio.html#COMPRESSION "Mkinitcpio").

You can also minimize [Microcode image](../../en/Microcode.html#Microcode_in_a_separate_initramfs_file "Microcode") [\[1\]](https://gitlab.archlinux.org/archlinux/packaging/packages/intel-ucode/-/merge_requests/2) by intel-ucode if you use [running without initramfs](../../en/Arch_boot_process.html#Running_without_initramfs "Arch boot process") or [Booster](../../en/Booster.html#Microcode_updates "Booster"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pacman.d/hooks/shrink-intel-ucode
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Trigger]
Type = Package
Operation = Install
Operation = Upgrade
Target = intel-ucode

[Action]
Description = Minimizing intel-ucode.img ...
When = PostTransaction
Depends = iucode-tool
Exec = /usr/bin/iucode_tool -S /usr/lib/firmware/intel-ucode --overwrite --write-earlyfw=/boot/intel-ucode.img
```

## Choose the adequate way to start for services {#Choose_the_adequate_way_to_start_for_services}

One central feature of systemd is [D-Bus](../../en/D-Bus.html "D-Bus") and socket activation. This feature should be preferred for most cases as it causes services to be started only when they are first accessed and is generally a good thing (e.g. having `cups.service` enabled at boot time is usually not useful for desktop use, enable instead `cups.socket` which will only start the service when actually printing).

However, if you know that a service (like [upower](https://archlinux.org/packages/?name=upower)) will always be started during boot, then the overall boot time might be reduced by starting it as early as possible. This can be achieved (if the service file is set up for it, which in most cases it is) by [enabling](../../en/Help:Reading.html#Control_of_systemd_units "Enabling") `upower.service`.

This will cause systemd to start UPower as soon as possible, without causing races with the socket or D-Bus activation.

## Staggered spin-up {#Staggered_spin-up}

Some hardware implements [staggered spin-up](https://en.wikipedia.org/wiki/Spin-up#Staggered_spin-up "wikipedia:Spin-up"), which causes the OS to probe ATA interfaces serially, which can spin up the drives one-by-one and reduce the peak power usage. This slows down the boot speed, and on most consumer hardware provides no benefits at all since the drives will already spin-up immediately when the power is turned on. To check if SSS is being used:

    # dmesg | grep SSS

If it was not used during boot, there will be no output.

To disable it, add the `libahci.ignore_sss=1` [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter").

## Filesystem mounts {#Filesystem_mounts}

Thanks to [mkinitcpio](../../en/Mkinitcpio.html "Mkinitcpio")\'s `fsck` hook, you can avoid a possibly costly remount of the root partition by changing `ro` to `rw` on the kernel line: options can be set with `rootflags=`**`rw`**`,`*`other_mount_options`*. The entry must be removed from the `/etc/fstab` file, otherwise the `systemd-remount-fs.service` will continue to try applying these settings. Alternatively, one could try to mask that unit.

If [Btrfs](../../en/Btrfs.html "Btrfs") is in use for the root filesystem, there is no need for a fsck on every boot like other filesystems. If this is the case, [mkinitcpio](../../en/Mkinitcpio.html "Mkinitcpio")\'s `fsck` hook can be removed. You may also want to mask the `systemd-fsck-root.service`, or tell it not to fsck the root filesystem from the kernel command line using `fsck.mode=skip`. Without [mkinitcpio](../../en/Mkinitcpio.html "Mkinitcpio")\'s `fsck` hook, systemd will still fsck any relevant filesystems with the `systemd-fsck@.service`

You can also remove API filesystems from `/etc/fstab`, as systemd will mount them itself (see `pacman -Ql systemd | grep '\.mount$'` for a list). It is not uncommon for users to have a `/tmp` entry carried over from sysvinit, but you may have noticed from the command above that systemd already takes care of this. Ergo, it may be safely removed.

Other filesystems, like `/home` or [EFI system partition](../../en/EFI_system_partition.html "EFI system partition"), can be mounted with custom mount units. Adding `noauto,x-systemd.automount` to mount options will buffer all access to that partition, and will fsck and mount it on first access, reducing the number of filesystems it must fsck/mount during the boot process.

**Note**

-   This will make your `/home` filesystem type `autofs`, which is ignored by [locate](../../en/Locate.html "Locate") by default. The speedup of automounting `/home` may not be more than a second or two, depending on your system, so this trick may not be worth it.
-   If the system is installed into a *btrfs* subvolume (specifically: the root directory `/` itself is a subvolume) and `/home` is a separate file system, you may also want to prevent the creation of a `/home` subvolume. Mask the `home.conf` tmpfile: `ln -s /dev/null /etc/tmpfiles.d/home.conf`.

## Less output during boot {#Less_output_during_boot}

For some systems, particularly those with an SSD, the slow performance of the TTY is actually a bottleneck, and so less output means faster booting. See the [Silent boot](../../en/Silent_boot.html "Silent boot") article for suggestions.

## Changing boot loader {#Changing_boot_loader}

Changing your [boot loader](../../en/Boot_loader.html "Boot loader") (e.g. a simpler boot loader such as [systemd-boot](../../en/Systemd-boot.html "Systemd-boot")) may reduce boot time by seconds.

If your setup allows it, try using only an [EFI boot stub](../../en/EFI_boot_stub.html "EFI boot stub") for even shorter boot times.

## Suspend to RAM {#Suspend_to_RAM}

The best way to reduce boot time is not booting at all. Consider [suspending your system to RAM](../../en/Power_management/Suspend_and_hibernate.html "Power management/Suspend and hibernate") instead.
