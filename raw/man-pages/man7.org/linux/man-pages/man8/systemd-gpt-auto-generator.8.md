---
{"title": "systemd-gpt-auto-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-gpt-auto-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-gpt-auto-generator(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-...ENERATOR(8)  systemd-gpt-auto-generator SYSTEMD-...ENERATOR(8)

## [](#NAME)NAME

           systemd-gpt-auto-generator - Generator for automatically
           discovering and mounting root, /home/, /srv/, /var/ and /var/tmp/
           partitions, as well as discovering and enabling swap partitions,
           based on GPT partition type GUIDs

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-gpt-auto-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-gpt-auto-generator is a unit generator that automatically
           discovers the root partition, /home/, /srv/, /var/, /var/tmp/, the
           EFI System Partition (ESP), the Extended Boot Loader Partition
           (XBOOTLDR), and swap partitions and creates mount and swap units
           for them, based on the partition type GUIDs of GUID partition
           tables (GPT). See UEFI Specification[1], chapter 5 for more
           details. It implements the UAPI.2 Discoverable Partitions
           Specification[2].

           Note that this generator has no effect on non-GPT systems. It will
           also not create mount point configuration for directories which
           already contain files or if the mount point is explicitly
           configured in fstab(5). Additionally no unit will be created for
           the ESP or the XBOOTLDR partition if mount entries are found in
           the /boot/ or /efi/ hierarchies in fstab(5).

           If the units this generator creates are overridden, for example by
           units in directories with higher precedence, drop-ins and
           additional dependencies created by this generator might still be
           used.

           When run in the initial RAM disk (initrd) this generator can
           automatically search for the root file system. Specifically:

           •   It will look for the root partition on the same physical disk
               where the EFI System Partition (ESP) is located. Note that
               support from the boot loader is required for this to work: the
               EFI variable LoaderDevicePartUUID of the
               4a67b082-0a4c-41cf-b6c7-440b29bb8c4f vendor UUID is used to
               determine from which partition (and hence disk) the system was
               booted. If the boot loader does not set this variable, this
               generator will not be able to detect the root partition. See
               the Boot Loader Interface[3] for details.

           •   Alternatively, it will look for the root file system on a
               loopback block device whose ".lo_name" field is set to one of
               the literal strings "rootdisk" or "rootdisk.raw". This field
               can be set via losetup's --loop-ref= string. For images
               downloaded via systemd-import-generator(8) make sure to set
               the "blockdev" option and set the local name string to
               "rootdisk" to achieve this effect. Note that discovery of the
               root file system on loopback block devices like this is only
               done if "root=gpt-auto" or "root=dissect" is specified
               explicitly on the kernel command line, unlike the discovery
               based on the boot loader reported ESP which is also enabled if
               no "root=" parameter is specified at all. (The latter relies
               on systemd-udevd.service's /dev/gpt-auto-root block device
               symlink generation).

           •   It will also generate a unit file mounting the EFI System
               Partition (ESP) to /sysefi/, if applicable. Unlike the file
               systems mentioned above this mount is not activated by default
               however, but can be pulled in by services requiring ESP access
               from within the initrd. Note that this mount point is
               initrd-specific and does not make use of autofs. The ESP is
               typically mounted at a different place and via autofs once the
               system transitions out of the initrd.

           When run on the host system (i.e. after successfully transitioning
           out of the initrd into the root filesystem) this generator will
           look for all other partitions on the same physical disk as the
           root partition. For this discovery, boot loader support is not
           required. Moreover, it is not required that the root partition was
           automatically discovered by the initrd (as described above) for
           the discovery of the non-root file partitions to take place. Or in
           other words: automatic discovery of the root file system and of
           the non-root file systems are independent operations, that do not
           rely on each other, and are done during two distinct phases of the
           boot process (one in the initrd, the other after). These
           partitions will not be searched for on systems where the root file
           system is distributed on multiple disks, for example via btrfs
           RAID.

           The root partition can be configured explicitly by symlinking
           /run/systemd/volatile-root to /dev/block/$major:$minor. This is
           especially useful if the root mount has been replaced by some form
           of volatile file system (overlayfs).

           systemd-gpt-auto-generator is useful for centralizing file system
           configuration in the partition table and making configuration in
           /etc/fstab or on the kernel command line unnecessary.

           This generator looks for the partitions based on their partition
           type GUID. The following partition type GUIDs are identified:

           Table 1. Partition Type GUIDs
           ┌─────────────────────────┬──────────────────────────────────────┬───────────────┬──────────────┬───────────────────┐
           │ Partition               │ GUID                                 │ Name          │ Mount Point  │ Explanation       │
           │ Type                    │                                      │               │              │                   │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_ROOT_X86_64      │ 4f68bce3-e8cd-4db1-96e7-fbcaf984b709 │ Root          │ /            │ The first         │
           │                         │                                      │ Partition     │              │ partition         │
           │                         │                                      │ (x86-64)      │              │ with this         │
           │                         │                                      │               │              │ type UUID,        │
           │                         │                                      │               │              │ located on        │
           │                         │                                      │               │              │ the same          │
           │                         │                                      │               │              │ disk as the       │
           │                         │                                      │               │              │ ESP used for      │
           │                         │                                      │               │              │ booting, is       │
           │                         │                                      │               │              │ used as the       │
           │                         │                                      │               │              │ root file         │
           │                         │                                      │               │              │ system / on       │
           │                         │                                      │               │              │ AMD64 /           │
           │                         │                                      │               │              │ 64-bit x86        │
           │                         │                                      │               │              │ systems.          │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_ROOT_ARM64       │ b921b045-1df0-41c3-af44-4c6f280d3fae │ Root          │ /            │ The first         │
           │                         │                                      │ Partition     │              │ partition         │
           │                         │                                      │ (64-bit ARM)  │              │ with this         │
           │                         │                                      │               │              │ type UUID,        │
           │                         │                                      │               │              │ located on        │
           │                         │                                      │               │              │ the same          │
           │                         │                                      │               │              │ disk as the       │
           │                         │                                      │               │              │ ESP used for      │
           │                         │                                      │               │              │ booting, is       │
           │                         │                                      │               │              │ used as the       │
           │                         │                                      │               │              │ root file         │
           │                         │                                      │               │              │ system / on       │
           │                         │                                      │               │              │ AArch64 /         │
           │                         │                                      │               │              │ 64-bit ARM        │
           │                         │                                      │               │              │ systems.          │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_ROOT_ALPHA       │ ...                                  │ Root          │ /            │ The first         │
           │ SD_GPT_ROOT_ARC         │                                      │ partitions    │              │ partition         │
           │ SD_GPT_ROOT_ARM         │                                      │ for other     │              │ with the          │
           │ SD_GPT_ROOT_ARM64       │                                      │ architectures │              │ type UUID         │
           │ SD_GPT_ROOT_IA64        │                                      │               │              │ matching the      │
           │ SD_GPT_ROOT_LOONGARCH64 │                                      │               │              │ architecture,     │
           │ SD_GPT_ROOT_MIPS        │                                      │               │              │ located on        │
           │ SD_GPT_ROOT_MIPS64      │                                      │               │              │ the same          │
           │ SD_GPT_ROOT_MIPS_LE     │                                      │               │              │ disk as the       │
           │ SD_GPT_ROOT_MIPS64_LE   │                                      │               │              │ ESP used for      │
           │ SD_GPT_ROOT_PARISC      │                                      │               │              │ booting, is       │
           │ SD_GPT_ROOT_PPC         │                                      │               │              │ used as the       │
           │ SD_GPT_ROOT_PPC64       │                                      │               │              │ root file         │
           │ SD_GPT_ROOT_PPC64_LE    │                                      │               │              │ system /.         │
           │ SD_GPT_ROOT_RISCV32     │                                      │               │              │ For the full      │
           │ SD_GPT_ROOT_RISCV64     │                                      │               │              │ list and          │
           │ SD_GPT_ROOT_S390        │                                      │               │              │ constant          │
           │ SD_GPT_ROOT_S390X       │                                      │               │              │ values, see       │
           │ SD_GPT_ROOT_TILEGX      │                                      │               │              │ UAPI.2            │
           │ SD_GPT_ROOT_X86         │                                      │               │              │ Discoverable      │
           │ SD_GPT_ROOT_X86_64      │                                      │               │              │ Partitions        │
           │ SD_GPT_USR_ALPHA        │                                      │               │              │ Specification[2]. │
           │ SD_GPT_USR_ARC          │                                      │               │              │                   │
           │ SD_GPT_USR_ARM          │                                      │               │              │                   │
           │ SD_GPT_USR_IA64         │                                      │               │              │                   │
           │ SD_GPT_USR_LOONGARCH64  │                                      │               │              │                   │
           │ SD_GPT_USR_MIPS_LE      │                                      │               │              │                   │
           │ SD_GPT_USR_MIPS64_LE    │                                      │               │              │                   │
           │ SD_GPT_USR_PARISC       │                                      │               │              │                   │
           │ SD_GPT_USR_PPC          │                                      │               │              │                   │
           │ SD_GPT_USR_PPC64        │                                      │               │              │                   │
           │ SD_GPT_USR_PPC64_LE     │                                      │               │              │                   │
           │ SD_GPT_USR_RISCV32      │                                      │               │              │                   │
           │ SD_GPT_USR_RISCV64      │                                      │               │              │                   │
           │ SD_GPT_USR_S390         │                                      │               │              │                   │
           │ SD_GPT_USR_S390X        │                                      │               │              │                   │
           │ SD_GPT_USR_TILEGX       │                                      │               │              │                   │
           │ SD_GPT_USR_X86          │                                      │               │              │                   │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_HOME             │ 933ac7e1-2eb4-4f13-b844-0e14e2aef915 │ Home          │ /home/       │ The first         │
           │                         │                                      │ Partition     │              │ partition with    │
           │                         │                                      │               │              │ this type UUID on │
           │                         │                                      │               │              │ the same disk as  │
           │                         │                                      │               │              │ the root          │
           │                         │                                      │               │              │ partition is      │
           │                         │                                      │               │              │ mounted to        │
           │                         │                                      │               │              │ /home/.           │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_SRV              │ 3b8f8425-20e0-4f3b-907f-1a25a76f98e8 │ Server Data   │ /srv/        │ The first         │
           │                         │                                      │ Partition     │              │ partition with    │
           │                         │                                      │               │              │ this type UUID on │
           │                         │                                      │               │              │ the same disk as  │
           │                         │                                      │               │              │ the root          │
           │                         │                                      │               │              │ partition is      │
           │                         │                                      │               │              │ mounted to /srv/. │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_VAR              │ 4d21b016-b534-45c2-a9fb-5c16e091fd2d │ Variable Data │ /var/        │ The first         │
           │                         │                                      │ Partition     │              │ partition with    │
           │                         │                                      │               │              │ this type UUID on │
           │                         │                                      │               │              │ the same disk as  │
           │                         │                                      │               │              │ the root          │
           │                         │                                      │               │              │ partition is      │
           │                         │                                      │               │              │ mounted to /var/  │
           │                         │                                      │               │              │ — under the       │
           │                         │                                      │               │              │ condition its     │
           │                         │                                      │               │              │ partition UUID    │
           │                         │                                      │               │              │ matches the first │
           │                         │                                      │               │              │ 128 bit of the    │
           │                         │                                      │               │              │ HMAC-SHA256 of    │
           │                         │                                      │               │              │ the GPT type uuid │
           │                         │                                      │               │              │ of this partition │
           │                         │                                      │               │              │ keyed by the      │
           │                         │                                      │               │              │ machine ID of the │
           │                         │                                      │               │              │ installation      │
           │                         │                                      │               │              │ stored in         │
           │                         │                                      │               │              │ machine-id(5).    │
           │                         │                                      │               │              │ This can be       │
           │                         │                                      │               │              │ generated using   │
           │                         │                                      │               │              │ systemd-id128(1). │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_TMP              │ 7ec6f557-3bc5-4aca-b293-16ef5df639d1 │ Temporary     │ /var/tmp/    │ The first         │
           │                         │                                      │ Data          │              │ partition with    │
           │                         │                                      │ Partition     │              │ this type UUID on │
           │                         │                                      │               │              │ the same disk as  │
           │                         │                                      │               │              │ the root          │
           │                         │                                      │               │              │ partition is      │
           │                         │                                      │               │              │ mounted to        │
           │                         │                                      │               │              │ /var/tmp/.        │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_SWAP             │ 0657fd6d-a4ab-43c4-84e5-0933c84b4f4f │ Swap          │ n/a          │ All partitions    │
           │                         │                                      │               │              │ with this type    │
           │                         │                                      │               │              │ UUID on the same  │
           │                         │                                      │               │              │ disk as the root  │
           │                         │                                      │               │              │ partition are     │
           │                         │                                      │               │              │ used as swap.     │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_ESP              │ c12a7328-f81f-11d2-ba4b-00a0c93ec93b │ EFI System    │ /efi/ or     │ The first         │
           │                         │                                      │ Partition     │ /boot/ once  │ partition with    │
           │                         │                                      │ (ESP)         │ the system   │ this type UUID    │
           │                         │                                      │               │ transitioned │ located on the    │
           │                         │                                      │               │ out of the   │ same disk as the  │
           │                         │                                      │               │ initrd,      │ root partition is │
           │                         │                                      │               │ /sysefi/     │ mounted to /boot/ │
           │                         │                                      │               │ before       │ or /efi/, see     │
           │                         │                                      │               │              │ below.            │
           ├─────────────────────────┼──────────────────────────────────────┼───────────────┼──────────────┼───────────────────┤
           │ SD_GPT_XBOOTLDR         │ bc13c2ff-59e6-4262-a352-b275fd6f7172 │ Extended Boot │ /boot/       │ The first         │
           │                         │                                      │ Loader        │              │ partition with    │
           │                         │                                      │ Partition     │              │ this type UUID    │
           │                         │                                      │               │              │ located on the    │
           │                         │                                      │               │              │ same disk as the  │
           │                         │                                      │               │              │ root partition is │
           │                         │                                      │               │              │ mounted to        │
           │                         │                                      │               │              │ /boot/, see       │
           │                         │                                      │               │              │ below.            │
           └─────────────────────────┴──────────────────────────────────────┴───────────────┴──────────────┴───────────────────┘

           This generator understands the following attribute flags for
           partitions:

           Table 2. Partition Attribute Flags
           ┌──────────────────────────────────┬────────────────────┬─────────────────┬───────────────┐
           │ Flag                             │ Value              │ Applicable to   │ Explanation   │
           ├──────────────────────────────────┼────────────────────┼─────────────────┼───────────────┤
           │ SD_GPT_FLAG_READ_ONLY            │ 0x1000000000000000 │ /, /home/,      │ Partition is  │
           │                                  │                    │ /srv/, /var/,   │ mounted       │
           │                                  │                    │ /var/tmp/,      │ read-only     │
           │                                  │                    │ Extended Boot   │               │
           │                                  │                    │ Loader          │               │
           │                                  │                    │ Partition       │               │
           ├──────────────────────────────────┼────────────────────┼─────────────────┼───────────────┤
           │ SD_GPT_FLAG_NO_AUTO              │ 0x8000000000000000 │ /, /home/,      │ Partition is  │
           │                                  │                    │ /srv/, /var/,   │ not mounted   │
           │                                  │                    │ /var/tmp/,      │ automatically │
           │                                  │                    │ Extended Boot   │               │
           │                                  │                    │ Loader          │               │
           │                                  │                    │ Partition       │               │
           ├──────────────────────────────────┼────────────────────┼─────────────────┼───────────────┤
           │ SD_GPT_FLAG_NO_BLOCK_IO_PROTOCOL │ 0x0000000000000002 │ EFI System      │ Partition is  │
           │                                  │                    │ Partition (ESP) │ not mounted   │
           │                                  │                    │                 │ automatically │
           └──────────────────────────────────┴────────────────────┴─────────────────┴───────────────┘

           The /home/, /srv/, /var/, /var/tmp/ and swap partitions may be
           encrypted in LUKS format. In this case, a device mapper device is
           set up under the names /dev/mapper/home, /dev/mapper/srv,
           /dev/mapper/var, /dev/mapper/tmp or /dev/mapper/swap. Note that
           this might create conflicts if the same partition is listed in
           /etc/crypttab with a different device mapper device name.

           When systemd is running in the initrd the / partition may be
           encrypted with LUKS as well. In this case, a device mapper device
           is set up under the name /dev/mapper/root, and a sysroot.mount is
           set up that mounts the device under /sysroot. For more
           information, see bootup(7).

           Mount and automount units for the EFI System Partition (ESP) and
           Extended Boot Loader Partition (XBOOTLDR) are generated on EFI
           systems. If the disk contains an XBOOTLDR partition, as defined in
           the UAPI.1 Boot Loader Specification[4], it is made available at
           /boot/. This generator creates an automount unit; the mount will
           only be activated on-demand when accessed. The mount point will be
           created if necessary.

           The ESP is mounted to /boot/ if that directory is not used for
           XBOOTLDR, and otherwise to /efi/. Same as for /boot/, an automount
           unit is used. The mount point will be created if necessary. These
           apply once the system transitioned out of the initrd phase. Before
           that, if components in the initrd require ESP access, it will be
           mounted to /sysefi/.

           No configuration is created for mount points that are configured
           in fstab(5) or when the target directory contains files.

           When using this generator in conjunction with btrfs file systems,
           make sure to set the correct default subvolumes on them, using
           btrfs subvolume set-default.

           If the system was booted via systemd-stub(7) and the stub reported
           to userspace that the kernel image was measured to a TPM2 PCR,
           then any discovered root and /var/ volume identifiers (and volume
           encryption keys, in case they are encrypted) will be automatically
           measured into PCR 15 on activation, via systemd-pcrfs@.service(8).
           Moreover, information about the LUKS key slot used to unlock the
           volume is measured into NvPCR "cryptsetup". Finally, if the root
           or /usr/ partition is protected via Verity its root hash and the
           serial/issuer of the key used for the provided root hash signature
           (if any) are measured into the NvPCR "verity".

           Mount constraint metadata contained in the file systems is
           validated by pulling in systemd-validatefs@.service(8) for
           generated mounts.

           systemd-gpt-auto-generator implements systemd.generator(7).

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-gpt-auto-generator understands the following kernel
           command line parameters:

           systemd.gpt_auto, rd.systemd.gpt_auto
               Those options take an optional boolean argument, and default
               to yes. The generator is enabled by default, and a false value
               may be used to disable it (e.g.  "systemd.gpt_auto=0").

               Added in version 242.

           systemd.image_policy=
               Takes an image dissection policy string as argument (as per
               systemd.image-policy(7)), and allows enforcing a policy on
               dissection and use of the automatically discovered GPT
               partition table entries.

               Note that the specified image policy is not taken into account
               for automatic root or /usr/ file system discovery unless
               root=dissect/mount.usr=dissect (or root=dissect-force) are
               specified. (The policy will always be applied to the other
               auto-discoverable partition types.)

               Added in version 254.

           systemd.image_filter=
               Takes an image dissection filter string as argument (as per
               systemd.image-filter(7)), and allows enforcing a set of
               globbing patterns on the partition matching of the
               automatically discovered GPT partition table entries.

               Note that the specified image filter is not taken into account
               for automatic root or /usr/ file system discovery unless
               root=dissect/mount.usr=dissect (or root=dissect-force) are
               specified. (The filter will always be applied to the other
               auto-discoverable partition types.)

               Added in version 258.

           root=, rootfstype=, rootflags=
               When root= is used with the special value "gpt-auto", basic
               automatic discovery of the root partition based on the GPT
               partition type is enabled. Use of the root partition is
               delayed until factory reset mode is left, in case it is
               enabled during the current boot. See Factory Reset[5] for more
               information on that. If "gpt-auto-force" is specified
               automatic discovery of the root partition is enabled, ignoring
               any factory reset mode.

               If root= is set to the special value "dissect" full automatic
               discovery of the root partition based on GPT partition
               information is enabled. This is a superset of root=gpt-auto,
               as it automatically configures Verity partitions (including
               signature-based setup) following the logic defined for that in
               the UAPI.2 Discoverable Partitions Specification[6]. Moreover
               it takes the configured image policy and image filter into
               account for all partition types, including the root file
               system.  "root=dissect" will wait for the factory reset phase
               to be completed if it is in effect before activating the root
               file system. Use "root=dissect-force" to ignore the factory
               reset phase and activate the root file system immediately.

               Any other value (i.e. besides "gpt-auto", "gpt-auto-force",
               "dissect", "dissect-force") disables automatic root file
               system discovery.

               If root= is not specified at all on the kernel command line
               automatic discovery of the root partition via the ESP reported
               by the boot loader is also enabled (taking factory reset state
               into account, i.e. equivalent to "root=gpt-auto"), however in
               this case discovery based on the loopback block device
               ".lo_name" field is not enabled.

               The rootfstype= and rootflags= options are used to select the
               file system type and options when the root file system is
               automatically discovered.

               Added in version 242.

           mount.usr=, mount.usrfstype=, mount.usrflags=
               Similar to root=, rootfstype=, rootflags= (see above), but
               applies to the /usr/ partition instead. Note that the
               "gpt-auto", "gpt-auto-force", "dissect-force" settings that
               root= understands are not supported by mount.usr= (however
               "dissect" is).

               Also note that automatic partition discovery for /usr/ must be
               enabled explicitly, unlike the discovery for the root file
               system, which is enabled if no root= parameter is passed at
               all.

               Added in version 258.

           rw, ro
               Mount the root partition read-write or read-only initially.

               Note that unlike most kernel command line options these
               settings do not override configuration in the file system, and
               the file system may be remounted later. See
               systemd-remount-fs.service(8).

               Added in version 242.

           systemd.swap=
               Takes a boolean argument or enables the option if specified
               without an argument. If disabled, automatic discovery of swap
               partition(s) based on GPT partition type is disabled. Defaults
               to enabled.

               Added in version 254.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.mount(5), systemd.swap(5),
           systemd-fstab-generator(8), systemd-cryptsetup@.service(8),
           systemd-pcrfs@.service(8), systemd-validatefs@.service(8),
           machine-id(5), cryptsetup(8), fstab(5), btrfs(8)

## [](#NOTES)NOTES

            1. UEFI Specification
               https://uefi.org/specifications

            2. UAPI.2 Discoverable Partitions Specification
               https://uapi-group.org/specifications/specs/discoverable_partitions_specification

            3. Boot Loader Interface
               https://systemd.io/BOOT_LOADER_INTERFACE

            4. UAPI.1 Boot Loader Specification
               https://uapi-group.org/specifications/specs/boot_loader_specification

            5. Factory Reset
               https://systemd.io/FACTORY_RESET

            6. UAPI.2 Discoverable Partitions Specification
               https://uapi-group.org/specifications/specs/discoverable_partitions_specification/

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                  SYSTEMD-...ENERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [repart.d(5)](../man5/repart.d.5.html),  [systemd.mount(5)](../man5/systemd.mount.5.html),  [sysupdate.d(5)](../man5/sysupdate.d.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd-boot(7)](../man7/systemd-boot.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.generator(7)](../man7/systemd.generator.7.html),  [systemd.image-filter(7)](../man7/systemd.image-filter.7.html),  [systemd.image-policy(7)](../man7/systemd.image-policy.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [systemd-stub(7)](../man7/systemd-stub.7.html),  [systemd-fstab-generator(8)](../man8/systemd-fstab-generator.8.html),  [systemd-import-generator(8)](../man8/systemd-import-generator.8.html),  [systemd-pcrphase.service(8)](../man8/systemd-pcrphase.service.8.html),  [systemd-remount-fs.service(8)](../man8/systemd-remount-fs.service.8.html),  [systemd-validatefs@.service(8)](../man8/systemd-validatefs@.service.8.html)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
