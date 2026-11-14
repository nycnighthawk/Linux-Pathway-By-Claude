---
{"title": "wipefs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/wipefs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# wipefs(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXAMPLES](#EXAMPLES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WIPEFS(8)                 System Administration                 WIPEFS(8)

## [](#NAME)NAME

           wipefs - wipe a signature from a device

## [](#SYNOPSIS)SYNOPSIS

           wipefs [options] device...

           wipefs [--backup] -o offset device...

           wipefs [--backup] -a device...

## [](#DESCRIPTION)DESCRIPTION

           wipefs can erase filesystem, raid or partition-table signatures
           (magic strings) from the specified device to make the signatures
           invisible for libblkid. wipefs does not erase the filesystem
           itself nor any other data from the device.

           When used without any options, wipefs lists all visible
           filesystems and the offsets of their basic signatures. The default
           output is subject to change. So whenever possible, you should
           avoid using default outputs in your scripts. Always explicitly
           define expected columns by using --output columns-list in
           environments where a stable output is required.

           wipefs calls the BLKRRPART ioctl when it has erased a
           partition-table signature to inform the kernel about the change.
           The ioctl is called as the last step and when all specified
           signatures from all specified devices are already erased. This
           feature can be used to wipe content on partition devices as well
           as a partition table on a disk device, for example by wipefs -a
           /dev/sdc1 /dev/sdc2 /dev/sdc.

           Note that some filesystems and some partition tables store more
           magic strings on the device (e.g., FAT, ZFS, GPT). The wipefs
           command (since v2.31) lists all the offsets where magic strings
           have been detected.

           When option -a is used, all magic strings that are visible for
           libblkid(3) are erased. In this case the wipefs scans the device
           again after each modification (erase) until no magic string is
           found.

           Note that by default wipefs does not erase nested partition tables
           on non-whole disk devices. For this the option --force is
           required.

## [](#OPTIONS)OPTIONS

           -a, --all
               Erase all available signatures. The set of erased signatures
               can be restricted with the -t option. When performed on a
               partitioned whole-disk device like /dev/sdX, it will erase
               only the partition tables, not the content of the partitions.

           -b, --backup[=dir]
               Create a signature backup to the file
               wipefs-<devname>-<offset>.bak in $HOME or the directory
               specified as the optional argument. For more details see the
               EXAMPLE section.

           -f, --force
               Force erasure, even if the filesystem is mounted. This is also
               required in order to erase a nested partition-table signature
               on a non-whole disk device.

           -J, --json
               Use JSON output format.

           --lock[=mode]
               Use an exclusive BSD lock for the device or file that is
               operated upon. The optional argument mode can be yes (1), no
               (0), or nonblock. If the mode argument is omitted, it defaults
               to yes. This option overrides the environment variable
               $LOCK_BLOCK_DEVICE. The default is to not use any lock at all,
               but using a lock is recommended to avoid collisions with
               systemd-udevd(8) or other tools.

           -i, --noheadings
               Do not print a header line.

           -O, --output list
               Specify which output columns to print. Use --help to get a
               list of all supported columns.

           -n, --no-act
               Causes everything to be done except for the write(2) call.

           -o, --offset offset
               Specify the location (in bytes) of the signature which should
               be erased from the device. The offset number may include a
               "0x" prefix; then the number will be interpreted as a hex
               value. It is possible to specify multiple -o options.

               The offset argument may be followed by the multiplicative
               suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB,
               TiB, PiB, EiB, ZiB and YiB (the "iB" is optional, e.g., "K"
               has the same meaning as "KiB"), or the suffixes KB (=1000), MB
               (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB.

           -p, --parsable
               Print out in parsable instead of printable format. Encode all
               potentially unsafe characters of a string to the corresponding
               hex value prefixed by '\x'.

           -q, --quiet
               Suppress any messages after a successful signature wipe.

           -t, --types list
               Limit the set of printed or erased signatures. More than one
               type may be specified in a comma-separated list. The list or
               individual types can be prefixed with 'no' to specify the
               types on which no action should be taken. For more details see
               mount(8).

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBBLKID_DEBUG=all
               Enable libblkid debug output.

           LOCK_BLOCK_DEVICE=<mode>
               Use exclusive BSD lock. The mode is "1" or "0". See --lock for
               more details.

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

           LIBSMARTCOLS_JSON=compact|lines
               Control JSON output format when using --json. Supported values
               are compact for JSON output with minimal whitespace, and lines
               for JSON Lines format (one JSON object per line). If unset or
               set to any other value, pretty-printed JSON is used.

## [](#EXAMPLES)EXAMPLES

           wipefs /dev/sda*
               Prints information about sda and all partitions on sda.

           wipefs --all --backup /dev/sdb
               Erases all signatures from the device /dev/sdb and creates a
               signature backup file ~/wipefs-sdb-<offset>.bak for each
               signature.

           dd if=~/wipefs-sdb-0x00000438.bak of=/dev/sdb seek=$((0x00000438))
           bs=1 conv=notrunc
               Restores an ext2 signature from the backup file
               ~/wipefs-sdb-0x00000438.bak.

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           blkid(8), findfs(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The wipefs command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                      WIPEFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.mount(5)](../man5/systemd.mount.5.html),  [systemd.swap(5)](../man5/systemd.swap.5.html),  [blkid(8)](../man8/blkid.8.html),  [btrfs-device(8)](../man8/btrfs-device.8.html),  [cfdisk(8)](../man8/cfdisk.8.html),  [cryptsetup(8)](../man8/cryptsetup.8.html),  [fdisk(8)](../man8/fdisk.8.html),  [mkfs.btrfs(8)](../man8/mkfs.btrfs.8.html),  [sfdisk(8)](../man8/sfdisk.8.html)

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
