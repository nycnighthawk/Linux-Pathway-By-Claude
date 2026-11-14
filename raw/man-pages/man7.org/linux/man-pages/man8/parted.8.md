---
{"title": "parted(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/parted.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# parted(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMANDS](#COMMANDS) \| [UNITS](#UNITS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PARTED(8)                   GNU Parted Manual                   PARTED(8)

## [](#NAME)NAME

           parted - a partition manipulation program

## [](#SYNOPSIS)SYNOPSIS

           parted [options] [device [command [options...]...]]

## [](#DESCRIPTION)DESCRIPTION

           parted is a program to manipulate disk partitions.  It supports
           multiple partition table formats, including MS-DOS and GPT.  It is
           useful for creating space for new operating systems, reorganising
           disk usage, and copying data to new hard disks.

           This manual page documents parted briefly.  Complete documentation
           is distributed with the package in GNU Info format.

## [](#OPTIONS)OPTIONS

           -h, --help
                  displays a help message

           -l, --list
                  lists partition layout on all block devices

           -m, --machine
                  displays machine parseable output

           -j, --json
                  displays JSON output

           -s, --script
                  never prompts for user intervention. Automatically answers
                  'NO' if a warning is encountered, eg. when shrinking a
                  partition.

           -f, --fix
                  automatically answer "fix" to exceptions in script mode

           -v, --version
                  displays the version

           -a alignment-type, --align alignment-type
                  Set alignment for newly created partitions, valid alignment
                  types are:

                  none   Use the minimum alignment allowed by the disk type.

                  cylinder
                         Align partitions to cylinders.

                  minimal
                         Use minimum alignment as given by the disk topology
                         information. This and the opt value will use layout
                         information provided by the disk to align the
                         logical partition table addresses to actual physical
                         blocks on the disks.  The min value is the minimum
                         alignment needed to align the partition properly to
                         physical blocks, which avoids performance
                         degradation.

                  optimal
                         Use optimum alignment as given by the disk topology
                         information. This aligns to a multiple of the
                         physical block size in a way that guarantees optimal
                         performance.

## [](#COMMANDS)COMMANDS

           [device]
                  The block device to be used.  When none is given, parted
                  will use the first block device it finds.

           [command [options]]
                  Specifies the command to be executed.  If no command is
                  given, parted will present a command prompt.  Possible
                  commands are:

                  help [command]
                         Print general help, or help on command if specified.

                  align-check type partition
                         Check if partition satisfies the alignment
                         constraint of type.  type must be "minimal" or
                         "optimal".

                  mklabel label-type
                         Create a new disklabel (partition table) of label-
                         type.  label-type should be one of "aix", "amiga",
                         "bsd", "dvh", "gpt", "loop", "mac", "msdos", "pc98",
                         or "sun".

                  mkpart [part-type name fs-type] start end
                         Create a new partition. part-type may be specified
                         only with msdos and dvh partition tables, it should
                         be one of "primary", "logical", or "extended".  name
                         is required for GPT partition tables and fs-type is
                         optional.  fs-type can be one of "btrfs", "exfat",
                         "ext2", "ext3", "ext4", "fat16", "fat32", "hfs",
                         "hfs+", "linux-swap", "ntfs", "reiserfs", "udf", or
                         "xfs".

                  name partition name
                         Set the name of partition to name. This option works
                         only on Mac, PC98, and GPT disklabels. The name can
                         be placed in double quotes, if necessary.  And
                         depending on the shell may need to also be wrapped
                         in single quotes so that the shell doesn't strip off
                         the double quotes.

                  print print-type
                         Display the partition table.  print-type is
                         optional, and can be one of devices, free, list, or
                         all.

                  quit   Exit from parted.

                  rescue start end
                         Rescue a lost partition that was located somewhere
                         between start and end.  If a partition is found,
                         parted will ask if you want to create an entry for
                         it in the partition table.

                  resizepart partition end
                         Change the end position of partition.  Note that
                         this does not modify any filesystem present in the
                         partition.

                  rm partition
                         Delete partition.

                  select device
                         Choose device as the current device to edit. device
                         should usually be a Linux hard disk device, but it
                         can be a partition, software raid device, or an LVM
                         logical volume if necessary.

                  set partition flag state
                         Change the state of the flag on partition to state.
                         Supported flags are: "boot", "root", "swap",
                         "hidden", "raid", "lvm", "lba", "legacy_boot",
                         "irst", "msftres", "esp", "chromeos_kernel",
                         "bls_boot", "linux-home", "no_automount",
                         "bios_grub", and "palo".  state should be either
                         "on" or "off".

                  unit unit
                         Set unit as the unit to use when displaying
                         locations and sizes, and for interpreting those
                         given by the user when not suffixed with an explicit
                         unit.  unit can be one of "s" (sectors), "B"
                         (bytes), "kB", "MB", "KiB", "MiB", "GB", "GiB",
                         "TB", "TiB", "%" (percentage of device size), "cyl"
                         (cylinders), "chs" (cylinders, heads, sectors), or
                         "compact" (megabytes for input, and a human-friendly
                         form for output).

                  toggle partition flag
                         Toggle the state of flag on partition.

                  type partition id or uuid
                         On MS-DOS set the type aka. partition id of
                         partition to id. The id is a value between "0x01"
                         and "0xff". On GPT the type-uuid of partition to
                         uuid.

                  disk_set flag state
                         Change a flag on the disk to state. A flag can be
                         either "on" or "off".  Some or all of these flags
                         will be available, depending on what disk abel you
                         are using.  Supported flags are: "pmbr_boot" on GPT
                         to enable the boot flag on the GPT's protective MBR
                         partition.

                  disk_toggle flag
                         Toggle the state of the disk flag.

                  version
                         Display version information and a copyright message.

## [](#UNITS)UNITS

           parted will compute sensible ranges for the locations you specify
           when using units like "GB", "MB", etc. Use the sector unit "s" or
           IEC binary units like "GiB", "MiB", to specify exact locations.
           When you specify start or end values using IEC binary units like
           "MiB", "GiB", "TiB", etc., parted treats those values as exact,
           and equivalent to the same number specified in bytes (i.e., with
           the "B" suffix), in that it provides no helpful range of
           sloppiness.  Contrast that with a partition start request of
           "4GB", which may actually resolve to some sector up to 500MB
           before or after that point.  Thus, when creating a partition in an
           exact location you should use units of bytes ("B"), sectors ("s"),
           or IEC binary units like "MiB", "GiB", but not "MB", "GB", etc.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to <bug-parted@gnu.org>

## [](#SEE_ALSO)SEE ALSO

           fdisk(8), mkfs(8), The parted program is fully documented in the
           info(1) format GNU partitioning software manual.

## [](#AUTHOR)AUTHOR

           This manual page was written by Timshel Knoll
           <timshel@debian.org>, for the Debian GNU/Linux system (but may be
           used by others).

## [](#COLOPHON)COLOPHON

           This page is part of the GNU parted (partition table manipulation)
           project.  Information about the project can be found at 
           ⟨http://www.gnu.org/software/parted/⟩.  If you have a bug report
           for this manual page, send it to bug-parted@gnu.org.  This page
           was obtained from the project's upstream Git repository
           ⟨git://git.savannah.gnu.org/parted.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-26.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    parted                      2021 September 28                   PARTED(8)

------------------------------------------------------------------------

Pages that refer to this page: [addpart(8)](../man8/addpart.8.html),  [btrfs-filesystem(8)](../man8/btrfs-filesystem.8.html),  [cfdisk(8)](../man8/cfdisk.8.html),  [delpart(8)](../man8/delpart.8.html),  [partprobe(8)](../man8/partprobe.8.html),  [partx(8)](../man8/partx.8.html),  [resizepart(8)](../man8/resizepart.8.html),  [sfdisk(8)](../man8/sfdisk.8.html)

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
