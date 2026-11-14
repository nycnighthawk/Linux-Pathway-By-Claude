---
{"title": "losetup(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/losetup.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# losetup(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [LOOP DEVICE LIFECYCLE](#LOOP_DEVICE_LIFECYCLE) \| [ENCRYPTION](#ENCRYPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLE](#EXAMPLE) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LOSETUP(8)                System Administration                LOSETUP(8)

## [](#NAME)NAME

           losetup - set up and control loop devices

## [](#SYNOPSIS)SYNOPSIS

           Set up a loop device:

           losetup [options] -f|loopdev file

           Get info:

           losetup [-l] [-a|loopdev]

           losetup -j file [-o offset]

           Recalibrate the size of a loop device:

           losetup -c loopdev

           Detach loop devices:

           losetup -d loopdev ...

           losetup -D

           Prevent loop devices from getting listed:

           losetup --remove loopdev ...

## [](#DESCRIPTION)DESCRIPTION

           losetup is used to associate loop devices with regular files or
           block devices, to detach loop devices, and to query the status of
           a loop device. If only the loopdev argument is given, the status
           of the corresponding loop device is shown. If no option is given,
           all loop devices are shown.

           Note that the old output format (i.e., losetup -a) with
           comma-delimited strings is deprecated in favour of the --list
           output format.

           It is possible to create multiple independent loop devices for the
           same backing file. This setup may be dangerous, can cause data
           loss, corruption, and overwrites. Use --nooverlap with --find
           during setup to avoid this problem.

           The loop device setup is not an atomic operation when used with
           --find, and losetup does not protect this operation by any lock.
           The number of attempts is internally restricted to a maximum of
           16. It is recommended to use for example flock(1) to avoid a
           collision in heavily parallel use cases.

## [](#OPTIONS)OPTIONS

           The size and offset arguments may be followed by the
           multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on
           for GiB, TiB, PiB, EiB, ZiB and YiB (the "iB" is optional, e.g.,
           "K" has the same meaning as "KiB") or the suffixes KB (=1000), MB
           (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB.

           -a, --all
               Show the status of all loop devices. Note that not all
               information is accessible for unprivileged users. See also
               --list. The old output format (as printed without --list) is
               deprecated.

           -d, --detach loopdev...
               Detach the file or device associated with the specified loop
               device(s). Note that since Linux v3.7 kernel uses "lazy device
               destruction". The detach operation does not return EBUSY error
               anymore if device is actively used by system, but it is marked
               by autoclear flag and destroyed later. Even if the device is
               not used, the loop device can be destroyed later. If you need
               to wait for a complete removal of the loop device, call
               udevadm settle after losetup.

           -D, --detach-all
               Detach all associated loop devices.

           -f, --find [file]
               Find the first unused loop device. If a file argument is
               present, use the found device as loop device. Otherwise, just
               print its name.

           --show
               Display the name of the assigned loop device if the -f option
               and a file argument are present.

           -L, --nooverlap
               Check for conflicts between loop devices to avoid situation
               when the same backing file is shared between more loop
               devices. If the file is already used by another device then
               re-use the device rather than a new one. The option makes
               sense only with --find.

           -j, --associated file [-o offset]
               Show the status of all loop devices associated with the given
               file.

           -o, --offset offset
               The data start is moved offset bytes into the specified file
               or device. The offset may be followed by the multiplicative
               suffixes; see above.

           --loop-ref string
               Set the reference string. The backwardly compatible default is
               to use the backing filename as a reference in the loop setup
               ioctl (aka lo_file_name). This option overrides this default
               behavior and sets the reference to the string. The reference
               may be used by udevd in /dev/loop/by-ref. The Linux kernel
               does not use the reference at all, but it could be used by
               some old utils that cannot read the backing file from sysfs.
               The reference is readable only for the root user (see --output
               +REF) and it is restricted to 64 bytes.

           --sizelimit size
               The data end is set to no more than size bytes after the data
               start. The size may be followed by the multiplicative
               suffixes; see above.

           -b, --sector-size size
               Set the logical sector size of the loop device in bytes (since
               Linux 4.14). The option may be used when creating a new loop
               device as well as a stand-alone command to modify sector size
               of the already existing loop device.

           -c, --set-capacity loopdev
               Force the loop driver to reread the size of the file
               associated with the specified loop device.

           -P, --partscan
               Force the kernel to scan the partition table on a newly
               created loop device. Note that the partition table parsing
               depends on sector sizes. The default is sector size is 512
               bytes, otherwise you need to use the option --sector-size
               together with --partscan.

           -r, --read-only
               Set up a read-only loop device.

           --direct-io[=on|off]
               Enable or disable direct I/O for the backing file. The default
               is off. Specifying either --direct-io or --direct-io=on will
               enable it. But, --direct-io=off can be provided to explicitly
               turn it off.

           -l, --list
               If a loop device or the -a option is specified, print the
               default columns for either the specified loop device or all
               loop devices; the default is to print info about all devices.
               See also --output, --noheadings, --raw, and --json.

           -O, --output column[,column]...
               Specify the columns that are to be printed for the --list
               output. Use --help to get a list of all supported columns.

           --output-all
               Output all available columns.

           -n, --noheadings
               Don’t print headings for --list output format.

           --raw
               Use the raw --list output format.

           -J, --json
               Use JSON format for --list output.

           --remove loopdev...
               Remove the specified loop device(s). The loop device must be
               unused (not associated with any backing file). This option
               removes the device node from the system. In most cases,
               --detach is sufficient for normal use. See the LOOP DEVICE
               LIFECYCLE section below.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#LOOP_DEVICE_LIFECYCLE)LOOP DEVICE LIFECYCLE

           Loop devices go through several states during their lifecycle:

           Creation
               When losetup associates a loop device with a backing file, it
               automatically creates the device node (e.g., /dev/loop0) if it
               doesn’t already exist. This happens on-demand when you use
               options like -f or specify a loop device explicitly. The
               device is created using the LOOP_CTL_ADD ioctl.

           Detachment
               The -d (--detach) option disassociates the backing file from
               the loop device using the LOOP_CLR_FD ioctl. After detachment,
               the loop device node remains in /dev and can be reused for
               another backing file. Use lsblk -a to see all loop device
               nodes, including unused ones.

           Removal
               The --remove option completely removes the loop device node
               from the system using the LOOP_CTL_REMOVE ioctl. The device
               must be detached first (not associated with any backing file).
               After removal, the device node disappears from /dev.

## [](#ENCRYPTION)ENCRYPTION

           Cryptoloop is no longer supported in favor of dm-crypt. For more
           details see cryptsetup(8).

## [](#EXIT_STATUS)EXIT STATUS

           losetup returns 0 on success, nonzero on failure. When losetup
           displays the status of a loop device, it returns 1 if the device
           is not configured and 2 if an error occurred which prevented
           determining the status of the device.

## [](#NOTES)NOTES

           Since version 2.37 losetup uses LOOP_CONFIGURE ioctl to set up a
           new loop device by one ioctl call. The old versions use
           LOOP_SET_FD and LOOP_SET_STATUS64 ioctls to do the same.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

           LIBSMARTCOLS_JSON=compact|lines
               Control JSON output format when using --json. Supported values
               are compact for JSON output with minimal whitespace, and lines
               for JSON Lines format (one JSON object per line). If unset or
               set to any other value, pretty-printed JSON is used.

           LOOPDEV_DEBUG=all
               Enable loopdev debug output.

           ULPATH_DEBUG=all
               Enable path debug output.

           ULSYSFS_DEBUG=all
               Enable sysfs debug output.

## [](#FILES)FILES

           /dev/loop[0..N]
               loop block devices

           /dev/loop-control
               loop control device

## [](#EXAMPLE)EXAMPLE

           The following commands can be used as an example of using the loop
           device.

               # dd if=/dev/zero of=~/file.img bs=1024k count=10
               # losetup --find --show ~/file.img
               /dev/loop0
               # mkfs -t ext2 /dev/loop0
               # mount /dev/loop0 /mnt
               ...
               # umount /dev/loop0
               # losetup --detach /dev/loop0

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>, based on the original version from
           Theodore Ts’o <tytso@athena.mit.edu>.

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The losetup command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     LOSETUP(8)

------------------------------------------------------------------------

Pages that refer to this page: [loop(4)](../man4/loop.4.html),  [cryptsetup-open(8)](../man8/cryptsetup-open.8.html),  [cryptsetup-tcryptDump(8)](../man8/cryptsetup-tcryptDump.8.html),  [e2image(8)](../man8/e2image.8.html),  [mount(8)](../man8/mount.8.html),  [umount(8)](../man8/umount.8.html)

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
