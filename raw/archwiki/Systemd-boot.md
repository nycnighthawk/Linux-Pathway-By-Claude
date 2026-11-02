---
{"title": "Systemd-boot", "url": "https://wiki.archlinux.org/title/Systemd-boot", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Systemd-boot

Related articles

-   [Arch boot process](../en/Arch_boot_process.html "Arch boot process")
-   [Secure Boot](../en/Secure_Boot.html "Secure Boot")
-   [Unified Extensible Firmware Interface](../en/Unified_Extensible_Firmware_Interface.html "Unified Extensible Firmware Interface")

[systemd-boot(7)](https://man.archlinux.org/man/systemd-boot.7), previously called **gummiboot** (German for \"rubber dinghy\") and sometimes referred to as *sd-boot*, is an easy-to-configure [UEFI](../en/Unified_Extensible_Firmware_Interface.html "UEFI") [boot manager](../en/Boot_manager.html "Boot manager"). It provides a textual menu to select the boot entry and an editor for the kernel command line.

Note that *systemd-boot* can only start EFI executables (e.g., the Linux kernel [EFI boot stub](../en/EFI_boot_stub.html "EFI boot stub"), [UEFI shell](../en/UEFI_shell.html "UEFI shell"), [GRUB](../en/GRUB.html "GRUB"), or the [Windows Boot Manager](https://learn.microsoft.com/en-us/windows-hardware/drivers/bringup/boot-and-uefi#understanding-the-windows-boot-manager)) from the [EFI system partition](../en/EFI_system_partition.html "EFI system partition") it is installed to or from an Extended Boot Loader Partition (XBOOTLDR partition) on the same disk.

**Note** In the entire article *`esp`* denotes the mountpoint of the [EFI system partition](../en/EFI_system_partition.html "EFI system partition") and *`boot`* denotes the mountpoint of the optional XBOOTLDR partition. It is assumed that you have [chrooted](../en/Chroot.html "Chroot") to the system\'s mount point.

## Supported file systems {#Supported_file_systems}

systemd-boot inherits the support for the file systems [from the firmware](../en/Arch_boot_process.html#UEFI "Arch boot process") (i.e. at least FAT12, FAT16 and FAT32). Additionally it loads any [UEFI drivers](../en/Unified_Extensible_Firmware_Interface.html#UEFI_drivers "Unified Extensible Firmware Interface") placed in *`esp`*`/EFI/systemd/drivers/`.

## Installation {#Installation}

*systemd-boot* is shipped with the [systemd](https://archlinux.org/packages/?name=systemd) package which is a dependency of the [base](https://archlinux.org/packages/?name=base) meta package, so no additional packages need to be installed manually.

## Installing the UEFI boot manager {#Installing_the_UEFI_boot_manager}

To install *systemd-boot*, first make sure that the system is booted into UEFI mode and [UEFI variables](../en/Unified_Extensible_Firmware_Interface.html#UEFI_variables "Unified Extensible Firmware Interface") are accessible. This can be verified by running `efivar --list` or, if [efivar](https://archlinux.org/packages/?name=efivar) is not installed, by running `ls /sys/firmware/efi/efivars` (if the directory exists, the system is booted into UEFI mode.)

Use [bootctl(1)](https://man.archlinux.org/man/bootctl.1) to install *systemd-boot* to the ESP:

    # bootctl install

This will copy the *systemd-boot* UEFI boot manager to the ESP, create a UEFI boot entry for it and set it as the first in the UEFI boot order.

-   On an x64 UEFI, `/usr/lib/systemd/boot/efi/systemd-bootx64.efi` will be copied to *`esp`*`/EFI/systemd/systemd-bootx64.efi` and *`esp`*`/EFI/BOOT/BOOTX64.EFI`.
-   On an IA32 UEFI, `/usr/lib/systemd/boot/efi/systemd-bootia32.efi` will be copied to *`esp`*`/EFI/systemd/systemd-bootia32.efi` and *`esp`*`/EFI/BOOT/BOOTIA32.EFI`.
-   An already existing old `systemd-bootx64.efi` will be kept as fallback and copied to `systemd-boot-fallbackx64.efi`, together with an automatically created UEFI boot entry \"Fallback Linux Boot Manager\".

The UEFI boot entry will be called \"Linux Boot Manager\" and will point to, depending on the [UEFI bitness](../en/Unified_Extensible_Firmware_Interface.html#UEFI_firmware_bitness "Unified Extensible Firmware Interface"), either `\EFI\systemd\systemd-bootx64.efi` or `\EFI\systemd\systemd-bootia32.efi` on the ESP.

**Note**

-   When running `bootctl install`, *systemd-boot* will try to locate the ESP at `/efi`, `/boot`, and `/boot/efi`. Setting *`esp`* to a different location requires passing the `--esp-path=`*`esp`* option. (See [bootctl(1) § OPTIONS](https://man.archlinux.org/man/bootctl.1#OPTIONS) for details.)
-   Installing *systemd-boot* will overwrite any existing *`esp`*`/EFI/BOOT/BOOTX64.EFI` (or *`esp`*`/EFI/BOOT/BOOTIA32.EFI` on IA32 UEFI), e.g. Microsoft\'s version of the file.
-   *bootctl* refrains from operating on UEFI variables/boot entries when running in pid namespace, which is the case for [arch-chroot(8)](https://man.archlinux.org/man/arch-chroot.8)\'s non-systemd mode. To create the boot entry in the chroot environment, use `arch-chroot -S` instead.

To conclude the installation, [configure](#Configuration) *systemd-boot*.

### Installation using XBOOTLDR {#Installation_using_XBOOTLDR}

**This article or section is a candidate for moving to [Partitioning#Discrete partitions](../en/Partitioning.html#Discrete_partitions "Partitioning").**

**Notes:** All partitioning info should be moved to partitioning, to leave only steps relevant to installing systemd-boot if you have such a setup. (Discuss in [Talk:Systemd-boot](../en/Talk:Systemd-boot.html))

A separate [/boot partition](../en/Partitioning.html#/boot "Partitioning") of type \"Linux extended boot\" (XBOOTLDR) can be created to keep the kernel and initramfs separate from the ESP. This is particularly helpful to [dual boot with Windows](../en/Dual_boot_with_Windows.html "Dual boot with Windows") with an existing ESP that is too small. [Grml](#Grml_on_ESP) or [Archiso](#Archiso_on_ESP) are also possible use cases.

Prepare an ESP as usual and create another partition for XBOOTLDR on the same physical drive. The XBOOTLDR partition must have a partition type GUID of `bc13c2ff-59e6-4262-a352-b275fd6f7172` [\[1\]](https://uapi-group.org/specifications/specs/boot_loader_specification/) (`ea00` type for [gdisk](../en/GPT_fdisk.html "Gdisk"), `xbootldr` type for [fdisk](../en/Fdisk.html "Fdisk")). The size of the XBOOTLDR partition should be large enough to accommodate all of the kernels you are going to install.

**Note**

-   *systemd-boot* does not do a file system check like it does for the ESP. Hence, it is possible to use any file system that your UEFI implementation can read.
-   UEFI may skip loading partitions other than the ESP when a \"fast boot\" mode is enabled. This can lead to *systemd-boot* failing to find entries on the XBOOTLDR partition; in that case, disable the \"fast boot\" mode.
-   The XBOOTLDR partition must be on the same physical disk as the ESP for *systemd-boot* to recognize it.

During install, mount the ESP to `/mnt/efi` and the XBOOTLDR partition to `/mnt/boot`.

Once in chroot, use the command:

    # bootctl --esp-path=/efi --boot-path=/boot install

To conclude the installation, [configure](#Configuration) *systemd-boot*.

### Updating the UEFI boot manager {#Updating_the_UEFI_boot_manager}

Whenever there is a new version of *systemd-boot*, the UEFI boot manager can be optionally reinstalled by the user. This can be done manually or automatically; the two approaches are described thereafter.

**Note** The UEFI boot manager is a standalone EFI executable and any version can be used to boot the system (partial updates do not apply, since pacman only installs the *systemd-boot* installer, not *systemd-boot* itself.) However, new versions may add new features or fix bugs, so it is probably a good idea to update *systemd-boot*.

**Warning** If you have [Secure Boot](../en/Secure_Boot.html "Secure Boot") enabled, you need to sign the boot manager update. See [#Signing for Secure Boot](#Signing_for_Secure_Boot).

#### Manual update {#Manual_update}

Use *bootctl* to update *systemd-boot*:

    # bootctl update

**Note** As with `bootctl install`, *systemd-boot* will try to locate the ESP at `/efi`, `/boot`, and `/boot/efi`. Setting *`esp`* to a different location requires passing the `--esp-path=`*`esp`* option.

#### Automatic update {#Automatic_update}

**The factual accuracy of this article or section is disputed.**

**Reason:** `systemctl enqueue-marked` does not restart the service when it is inactive. See the discussion at [Arch\'s GitLab](https://gitlab.archlinux.org/archlinux/packaging/packages/systemd/-/merge_requests/39) for more details. For the time being, either install [systemd-boot-pacman-hook](https://aur.archlinux.org/packages/systemd-boot-pacman-hook/)^AUR^ (preferred), which will update the boot loader when the [systemd](https://archlinux.org/packages/?name=systemd) package is updated, or enable `systemd-boot-update.service`, which will try to update the boot loader on every system start-up. (Discuss in [Talk:Systemd-boot](../en/Talk:Systemd-boot.html))

As of [systemd](https://archlinux.org/packages/?name=systemd) version 261.2-1, when the package is upgraded and an installed *systemd-boot* is detected, its `post_upgrade()` function marks `systemd-boot-update.service` for restart. The `35-systemd-enqueue-marked.hook` pacman hook subsequently runs `systemctl enqueue-marked`, which runs the marked service:

    # bootctl --variables=no --graceful update

There is no need to enable the service or install a separate pacman hook. Automatic detection searches for the ESP at `/efi`, `/boot`, or `/boot/efi`. If *`esp`* is not one of these paths, update it manually with `bootctl --esp-path=`*`esp`*` update`. The command updates all installed versions of *systemd-boot* in the ESP if a newer version is available in `/usr/lib/systemd/boot/efi/`. It looks for a *systemd-boot* file ending in `.efi.signed` first to allow users to sign the image for use with [Secure Boot](../en/Secure_Boot.html "Secure Boot").

### Signing for Secure Boot {#Signing_for_Secure_Boot}

If you have [Secure Boot](../en/Secure_Boot.html "Secure Boot") enabled, you may want to add a pacman hook to automatically sign the boot manager upon every upgrade of the package:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pacman.d/hooks/80-secureboot.hook
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Trigger]
Operation = Install
Operation = Upgrade
Type = Path
Target = usr/lib/systemd/boot/efi/systemd-boot*.efi

[Action]
Description = Signing systemd-boot EFI binary for Secure Boot
When = PostTransaction
Exec = /bin/sh -c 'while read -r f; do /usr/lib/systemd/systemd-sbsign sign --private-key /path/to/keyfile.key --certificate /path/to/certificate.crt --output "${f}.signed" "$f"; done;'
Depends = sh
NeedsTargets
```

Replace *`/path/to/keyfile.key`* and *`/path/to/certificate.crt`* with your signing key and certificate respectively. For better understanding of this hook, consult [systemd-sbsign(1)](https://man.archlinux.org/man/systemd-sbsign.1).

The created `/usr/lib/systemd/boot/efi/systemd-boot*.efi.`*`signed`* will automatically be picked up by `bootctl install` or `bootctl update`. See [bootctl(1) § SIGNED .EFI FILES](https://man.archlinux.org/man/bootctl.1#SIGNED_.EFI_FILES).

As an alternative, use [sbctl](../en/Unified_Extensible_Firmware_Interface/Secure_Boot.html#Automatic_signing_with_the_pacman_hook "Unified Extensible Firmware Interface/Secure Boot").

## Configuration {#Configuration}

**Tip**

-   After changing the configuration, run `bootctl` (without any arguments) to make sure that systemd-boot will be able to parse it properly.
-   The [kernel-install](../en/Kernel-install.html "Kernel-install") utility can be used to automatically generate configuration files compatible with systemd-boot. This section describes how to do so manually.

### Loader configuration {#Loader_configuration}

The loader configuration is stored in the file *`esp`*`/loader/loader.conf`. See [loader.conf(5) § OPTIONS](https://man.archlinux.org/man/loader.conf.5#OPTIONS) for details.

A loader configuration example is provided below:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/loader.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
default  arch.conf
timeout  4
console-mode max
editor   no
```

**Tip**

-   `default` and `timeout` can be changed in the boot menu itself and changes will be stored as UEFI variables `LoaderEntryDefault` and `LoaderConfigTimeout`, overriding these options.
-   `bootctl set-default ""` and `bootctl set-timeout ""` can be used to clear the UEFI variables overriding the `default` and `timeout` options, respectively.
-   A basic loader configuration file is located at `/usr/share/systemd/bootctl/loader.conf`.
-   If the boot manager---during the entry selection---appears distorted/uses the wrong resolution you can try to set the `console-mode` to `auto` (uses heuristics to select the best resolution), `keep` (keeps the firmware provided resolution) or `2` (tries to select the first non-UEFI-standard resolution).

#### Remember last entry {#Remember_last_entry}

The `default` can be changed to `@saved` in order to remember the last picked entry on startup. This is useful for when dual booting Windows and the surprise windows auto update pushes you into Linux.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/loader.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
default @saved
...
```

Consult [loader.conf(5)](https://man.archlinux.org/man/loader.conf.5) for more details.

### Adding loaders {#Adding_loaders}

*systemd-boot* will search for *.conf* files in `/loader/entries/` on the [EFI system partition](../en/EFI_system_partition.html "EFI system partition") it was launched from and additionally the [XBOOTLDR](#Installation_using_XBOOTLDR) partition on the same disk.

**Note**

-   Entries in *`esp`*`/loader/entries/*.conf` can only use files (e.g. kernels, initramfs, images, etc.) in *`esp`*`/` and entries in *`boot`*`/loader/entries/*.conf` can only use files in *`boot`*`/`.
-   The file path parameters are relative to the root of your EFI system partition or XBOOTLDR partition. E.g., if your EFI system partition or XBOOTLDR partition is mounted at `/boot`, then the `/boot/vmlinuz-linux` file must be specified in the `linux` key as `/vmlinuz-linux`.
-   When [Secure Boot](../en/Secure_Boot.html "Secure Boot") is active, [unified kernel images](../en/Unified_kernel_image.html "Unified kernel image") (UKIs) with an embedded `.cmdline` ignore all command line options passed to them (either using a boot entry with `options` or interactively). When Secure Boot is not active, the options passed via the command line override the embedded `.cmdline`.

An example of loader files launching Arch from a volume using its [UUID](../en/Persistent_block_device_naming.html#by-uuid "UUID") *`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`* is:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/arch.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title   Arch Linux
linux   /vmlinuz-linux
initrd  /initramfs-linux.img
options root=UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx rw
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/arch-fallback.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title   Arch Linux (fallback initramfs)
linux   /vmlinuz-linux
initrd  /initramfs-linux-fallback.img
options root=UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx rw
```

See the [Boot Loader Specification](https://uapi-group.org/specifications/specs/boot_loader_specification/#type-1-boot-loader-specification-entries) for details on all configuration options.

*systemd-boot* will automatically check at boot time for **Windows Boot Manager** at the location `/EFI/Microsoft/Boot/Bootmgfw.efi`, **Apple macOS Boot Manager** in firmware, [UEFI shell](../en/UEFI_shell.html "UEFI shell") `/shellx64.efi` and **EFI Default Loader** `/EFI/BOOT/bootx64.efi`, as well as specially prepared kernel files found in `/EFI/Linux/`. When detected, corresponding entries with titles `auto-windows`, `auto-osx`, `auto-efi-shell` and `auto-efi-default`, respectively, will be generated. These entries do not require manual loader configuration. However, it does not auto-detect other EFI applications (unlike [rEFInd](../en/REFInd.html "REFInd")), so for booting the Linux kernel, manual configuration entries must be created.

**Tip**

-   The available boot entries which have been configured can be listed with the command `bootctl list`.
-   An example entry file is located at `/usr/share/systemd/bootctl/arch.conf`.
-   The [kernel parameters](../en/Kernel_parameters.html "Kernel parameters") for scenarios such as [LVM](../en/LVM.html "LVM"), [LUKS](../en/Dm-crypt.html "LUKS"), [dm-crypt](../en/Dm-crypt.html "Dm-crypt") or [Btrfs](../en/Btrfs.html "Btrfs") can be found on the relevant pages.

**Note** If [external microcode initramfs images](../en/Microcode.html#Microcode_in_a_separate_initramfs_file "Microcode") are used (e.g. when using [Booster](../en/Booster.html "Booster") as the initramfs generator), `/boot/amd-ucode.img` or `/boot/intel-ucode.img` must be specified in a separate `initrd` and always be placed **first**, before the main initramfs image.

#### UEFI Shells or other EFI applications {#UEFI_Shells_or_other_EFI_applications}

In case you installed a [UEFI shell](../en/UEFI_shell.html "UEFI shell") with the package [edk2-shell](https://archlinux.org/packages/?name=edk2-shell), *systemd-boot* will auto-detect and create a new entry if the EFI file is placed in *`esp`*`/shellx64.efi`. To perform this an example command after installing the package would be:

    # cp /usr/share/edk2-shell/x64/Shell.efi /boot/shellx64.efi

Otherwise in case you installed [other EFI applications](../en/REFInd.html#Tools "REFInd") into the ESP, you can use the following snippets.

**Note** The file path parameter for the `efi` line is relative to the root of your [EFI system partition](../en/EFI_system_partition.html "EFI system partition"). If your EFI system partition is mounted at `/boot` and your EFI binaries reside at `/boot/EFI/xx.efi` and `/boot/yy.efi`, then you would specify the parameters as `efi /EFI/xx.efi` and `efi /yy.efi` respectively.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/fwupd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title  Firmware updater
efi     /EFI/tools/fwupdx64.efi
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/gdisk.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title  GPT fdisk (gdisk)
efi     /EFI/tools/gdisk_x64.efi
```

##### Memtest86+ {#Memtest86+}

You need to install [memtest86+-efi](https://archlinux.org/packages/?name=memtest86%2B-efi) for this to work. Also sign the EFI binary when using Secure Boot.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/memtest.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title Memtest86+
efi /memtest86+/memtest86x64.efi
```

For IA32 UEFI, specify `/memtest86+/memtest86ia32.efi` instead.

##### Netboot {#Netboot}

*systemd-boot* can chainload [Netboot](../en/Netboot.html "Netboot"). Download the `ipxe-arch.efi` EFI binary and signature, verify it and place it as proposed in *`esp`*`/EFI/arch_netboot/arch_netboot.efi`.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/arch_netboot.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title Arch Linux Netboot
efi /EFI/arch_netboot/arch_netboot.efi
```

##### GRUB {#GRUB}

*systemd-boot* can chainload [GRUB](../en/GRUB.html "GRUB"). The location of the `grubx64.efi` binary matches the used `--bootloader-id=` when GRUB was installed to the ESP.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/grub.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title GRUB
efi /EFI/GRUB/grubx64.efi
```

#### Boot from another disk {#Boot_from_another_disk}

*systemd-boot* [cannot](https://github.com/systemd/systemd/issues/3252) launch EFI binaries from partitions other than the ESP it is launched from or the XBOOTLDR partition on the same disk, but it can direct the [UEFI shell](../en/UEFI_shell.html "UEFI shell") to do so.

First, install [edk2-shell](https://archlinux.org/packages/?name=edk2-shell) as [described above](#UEFI_Shells_or_other_EFI_applications). In the UEFI shell, use the *map* command to take notes of the **FS alias** (ex: HD0a66666a2, HD0b, FS1, or BLK7) of the partition with the corresponding PARTUUID.

Then, use the `exit` command to boot back into Linux, where you can create a new loader entry to run the target EFI program through the UEFI shell:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/windows.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title   Windows
efi     /shellx64.efi
options -nointerrupt -nomap -noversion HD0b:EFI\Microsoft\Boot\Bootmgfw.efi
```

Ensure that the `efi` path matches the location where the `shellx64.efi` has been copied in the *esp* partition. Also, note that the `shellx64.efi` EFI file can be moved elsewhere to avoid the automatic entry creation by *systemd-boot*.

Replace `HD0b` with the previously noted *FS alias*.

-   The `-nointerrupt` option prevents interrupting the target EFI program with `Ctrl+c`.
-   The `-nomap -noversion` options hide the default UEFI shell greeting.
-   To have the UEFI shell automatically return to the boot manager if the target EFI program exits (e.g. due to an error), add the `-exit` option.
-   You can also add the `-noconsoleout` option if there is still unnecessary output in the UEFI shell.

### Booting into UEFI firmware setup {#Booting_into_UEFI_firmware_setup}

systemd-boot will automatically add an entry to boot into UEFI firmware setup if your device\'s firmware supports rebooting into setup from the OS.

### Kernel parameters editor with password protection {#Kernel_parameters_editor_with_password_protection}

Alternatively you can install [systemd-boot-password](https://aur.archlinux.org/packages/systemd-boot-password/)^AUR^ which supports `password` basic configuration option. Use `sbpctl generate` to generate a value for this option.

Install *systemd-boot-password* with the following command:

    # sbpctl install esp

With enabled editor you will be prompted for your password before you can edit kernel parameters.

## Tips and tricks {#Tips_and_tricks}

### Keys inside the boot menu {#Keys_inside_the_boot_menu}

You can use `t` and `T` while in the menu to adjust the menu timeout and `e` to edit the kernel parameters for this boot. Press `h` to see a short list of useful hotkeys. See [systemd-boot(7) § KEY BINDINGS](https://man.archlinux.org/man/systemd-boot.7#KEY_BINDINGS) for the full list of available key bindings inside the boot menu.

### Choosing next boot {#Choosing_next_boot}

The boot manager is integrated with the systemctl command, allowing you to choose what option you want to boot after a reboot. For example, suppose you have built a custom kernel and created an entry file *`esp`*`/loader/entries/arch-custom.conf` to boot into it, you can just launch

    $ systemctl reboot --boot-loader-entry=arch-custom.conf

and your system will reboot into that entry maintaining the default option intact for subsequent boots. To see a list of possible entries pass the `--boot-loader-entry=help` option.

If you want to boot into the firmware of your motherboard directly, then you can use this command:

    $ systemctl reboot --firmware-setup

### Unified kernel images {#Unified_kernel_images}

[Unified kernel images](../en/Unified_kernel_image.html "Unified kernel image") (UKIs) in *`esp`*`/EFI/Linux/` are automatically sourced by systemd-boot, and do not need an entry in *`esp`*`/loader/entries`. (Note that unified kernel images must have a `.efi` extension to be identified by *systemd-boot*.)

**Tip** Files in *`esp`*`/loader/entries/` will be booted first if no `default` is set in *`esp`*`/loader/loader.conf`. Remove those entries, or set the default with the full file name, i.e. `default arch-linux.efi`

### Grml on ESP {#Grml_on_ESP}

**Note** The following instructions are not exclusive to Grml. With slight adjustments, installing other software (e.g., [SystemRescueCD](https://www.system-rescue-cd.org/)) is possible.

**Tip** A `PKGBUILD` is available: [grml-systemd-boot](https://aur.archlinux.org/packages/grml-systemd-boot/)^AUR^.

[Grml](https://grml.org/) is a small live system with a collection of software for system administration and rescue.

In order to install Grml on the ESP, we only need to copy the kernel `vmlinuz`, the initramfs `initrd.img`, and the squashed image `grml64-small.squashfs` from the iso file to the ESP. To do so, first download [grml64-small.iso](https://grml.org/) and mount the file (the mountpoint is henceforth denoted *mnt*); the kernel and initramfs are located in *`mnt`*`/boot/grml64small/`, and the squashed image resides in *`mnt`*`/live/grml64-small/`.

Next, create a directory for Grml in your ESP,

    # mkdir -p esp/grml

and copy the above-mentioned files in there:

    # cp mnt/boot/grml64small/vmlinuz esp/grml
    # cp mnt/boot/grml64small/initrd.img esp/grml
    # cp mnt/live/grml64-small/grml64-small.squashfs esp/grml

In the last step, create an boot entry for systemd-boot: In *`esp`*`/loader/entries` create a `grml.conf` file with the following content:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/grml.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title   Grml Live Linux
linux   /grml/vmlinuz
initrd  /grml/initrd.img
options apm=power-off boot=live live-media-path=/grml/ nomce net.ifnames=0
```

For an overview of the available boot options, consult the [cheatcode for Grml](https://github.com/grml/grml-live/blob/master/config/media-files/GRMLBASE/GRML/GRML_NAME/grml-cheatcodes.txt).

### Archiso on ESP {#Archiso_on_ESP}

**Tip** A `PKGBUILD` is available: [archiso-systemd-boot](https://aur.archlinux.org/packages/archiso-systemd-boot/)^AUR^.

As with Grml it is possible to use the Arch Linux ISO. To do this we need to copy the kernel `vmlinuz-linux`, the initramfs `initramfs-linux.img`, and the squashfs image `airootfs.sfs` from the ISO file to the EFI system partition.

First download [archlinux-YYYY.MM.DD-x86_64.iso](https://archlinux.org/download/).

Next, create a directory for archiso in your ESP:

    # mkdir -p esp/EFI/archiso

Extract the contents of the `arch` directory in there:

    # bsdtar -v -x --no-same-permissions --strip-components 1 -f archlinux-YYYY.MM.DD-x86_64.iso -C esp/EFI/archiso arch

In the last step, create a boot entry for the systemd-boot: In *`esp`*`/loader/entries` create a `arch-rescue.conf` file with the following content:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/entries/arch-rescue.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
title   Arch Linux (rescue system)
linux   /EFI/archiso/boot/x86_64/vmlinuz-linux
initrd  /EFI/archiso/boot/x86_64/initramfs-linux.img
options archisobasedir=/EFI/archiso archisosearchfilename=/EFI/archiso/boot/x86_64/vmlinuz-linux
```

For an overview of the available boot options, consult the [README.bootparams for mkinitcpio-archiso](https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio-archiso/-/blob/master/docs/README.bootparams).

#### Recovery Arch image on the ESP with Secure Boot {#Recovery_Arch_image_on_the_ESP_with_Secure_Boot}

The official Arch ISO does not currently support [Secure Boot](../en/Secure_Boot.html "Secure Boot"). As a result, Secure Boot must be disabled to boot into the ISO for recovery or maintenance. This undermines system security and is not an ideal approach.

An alternative is to create a signed [unified kernel image](../en/Unified_kernel_image.html "Unified kernel image") (UKI) using [mkosi](../en/Mkosi.html "Mkosi"), assuming Secure Boot is already configured and functioning properly on your system. This allows you to boot into a signed recovery Arch environment without disabling Secure Boot or carrying an Arch ISO USB drive wherever your laptop goes.

[https://swsnr.de/archlinux-rescue-image-with-mkosi/](https://swsnr.de/archlinux-rescue-image-with-mkosi/) describes how to set up Secure Boot-compatible Arch recovery images. A practical starting point with a sane mkosi configuration you can add your packages to is available at [https://codeberg.org/swsnr/rescue-image](https://codeberg.org/swsnr/rescue-image).

### systemd-boot on BIOS systems {#systemd-boot_on_BIOS_systems}

If you need a boot loader for BIOS systems that follows [The Boot Loader Specification](https://uapi-group.org/specifications/specs/boot_loader_specification/), then systemd-boot can be pressed into service on BIOS systems. The [Clover](../en/Clover.html "Clover") boot loader supports booting from BIOS systems and provides an emulated UEFI environment.

## Troubleshooting {#Troubleshooting}

### systemd-boot does not display my boot entry {#systemd-boot_does_not_display_my_boot_entry}

This may be caused by a variety of issues with the configuration file, such as the path to the kernel being specified incorrectly. To check, run:

    # bootctl

### Installing after booting in BIOS mode {#Installing_after_booting_in_BIOS_mode}

**Note** This is not recommended.

If booted in BIOS mode, you can still install *systemd-boot*, however this process requires you to tell firmware to launch *systemd-boot\'*s EFI file at boot:

-   you have a working UEFI Shell somewhere else.
-   your firmware interface provides a way of properly setting the EFI file that needs to be loaded at boot time.
-   some firmware may use the default *`esp`*`/EFI/BOOT/BOOTX64.EFI` if there is no other entry set in the UEFI.

If you can do it, the installation is easier: go into your UEFI Shell or your firmware configuration interface and change your machine\'s default EFI file to *`esp`*`/EFI/systemd/systemd-bootx64.efi`.

**Note** The firmware interface of Dell Latitude series provides everything you need to setup UEFI boot but the UEFI Shell will not be able to write to the computer\'s ROM.

### Manual entry using efibootmgr {#Manual_entry_using_efibootmgr}

If the `bootctl install` command failed, you can create a UEFI boot entry manually using [efibootmgr](https://archlinux.org/packages/?name=efibootmgr):

    # efibootmgr --create --disk /dev/sdX --part Y --loader '\EFI\systemd\systemd-bootx64.efi' --label "Linux Boot Manager" --unicode

where `/dev/sd`*`XY`* is the [EFI system partition](../en/EFI_system_partition.html "EFI system partition").

**Note** The path to the EFI binary must use the backslash (`\`) as the separator

### Manual entry using bcdedit from Windows {#Manual_entry_using_bcdedit_from_Windows}

If for any reason you need to create a UEFI boot entry from Windows, you can use the following commands from an Administrator prompt:

    > bcdedit /copy "{bootmgr}" /d "Linux Boot Manager"
    > bcdedit /set "{guid}" path \EFI\systemd\systemd-bootx64.efi

Replace *`guid`* with the id returned by the first command. You can also set it as the default entry using

    > bcdedit /default "{guid}"

### Menu does not appear after Windows upgrade {#Menu_does_not_appear_after_Windows_upgrade}

See [UEFI#Windows changes boot order](../en/Unified_Extensible_Firmware_Interface.html#Windows_changes_boot_order "UEFI").

### Add support for Windows BitLocker TPM unlocking {#Add_support_for_Windows_BitLocker_TPM_unlocking}

To stop BitLocker from requesting the recovery key, add the following to *loader.conf*:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
esp/loader/loader.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
reboot-for-bitlocker yes
```

This will set the *BootNext* UEFI variable, whereby *Windows Boot Manager* is loaded without BitLocker requiring the recovery key. This is a one-time change, and *systemd-boot* remains the default boot loader. There is no need to specify Windows as an entry if it was autodetected.

This is an experimental feature, so make sure to consult [loader.conf(5)](https://man.archlinux.org/man/loader.conf.5).

## See also {#See_also}

-   [https://systemd.io/BOOT/](https://systemd.io/BOOT/)
-   [https://bbs.archlinux.org/viewtopic.php?id=254374](https://bbs.archlinux.org/viewtopic.php?id=254374)
-   [https://uapi-group.org/specifications/specs/boot_loader_specification/](https://uapi-group.org/specifications/specs/boot_loader_specification/)
