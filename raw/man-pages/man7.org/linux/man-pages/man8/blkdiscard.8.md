---
{"title": "blkdiscard(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/blkdiscard.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# blkdiscard(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BLKDISCARD(8)             System Administration             BLKDISCARD(8)

## [](#NAME)NAME

           blkdiscard - discard sectors on a device

## [](#SYNOPSIS)SYNOPSIS

           blkdiscard [options] [-o offset] [-l length] device

## [](#DESCRIPTION)DESCRIPTION

           blkdiscard is used to discard device sectors. This is useful for
           solid-state drives (SSDs) and thinly-provisioned storage. Unlike
           fstrim(8), this command is used directly on the block device.

           By default, blkdiscard will discard all blocks on the device.
           Options may be used to modify this behavior based on range or
           size, as explained below.

           The device argument is the pathname of the block device.

           WARNING: All data in the discarded region on the device will be
           lost!

           Since util-linux v2.41, fdisk has the ability to discard sectors
           on both partitions and unpartitioned areas using the 'T' command.
           Additionally, sfdisk has the option --discard-free to discard
           unpartitioned areas.

## [](#OPTIONS)OPTIONS

           The offset and length arguments may be followed by the
           multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on
           for GiB, TiB, PiB, EiB, ZiB and YiB (the "iB" is optional, e.g.,
           "K" has the same meaning as "KiB") or the suffixes KB (=1000), MB
           (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB.

           -f, --force
               Disable all checking. Since v2.36 the block device is open in
               exclusive mode (O_EXCL) by default to avoid collision with
               mounted filesystem or another kernel subsystem. The --force
               option disables the exclusive access mode.

           -o, --offset offset
               Byte offset into the device from which to start discarding.
               The provided value must be aligned to the device sector size.
               The default value is zero.

           -l, --length length
               The number of bytes to discard (counting from the starting
               point). The provided value must be aligned to the device
               sector size. If the specified value extends past the end of
               the device, blkdiscard will stop at the device size boundary.
               The default value extends to the end of the device.

           -p, --step length
               The number of bytes to discard within one iteration. The
               default is to discard all by one ioctl call.

           -q, --quiet
               Suppress warning messages.

           -s, --secure
               Perform a secure discard. A secure discard is the same as a
               regular discard except that all copies of the discarded blocks
               that were possibly created by garbage collection must also be
               erased. This requires support from the device.

           -z, --zeroout
               Zero-fill rather than discard.

           -v, --verbose
               Display the aligned values of offset and length. If the --step
               option is specified, it prints the discard progress every
               second.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           blkdiscard has the following exit status values:

           0
               success

           1
               failure; incorrect invocation, permissions or any other
               generic error

           2
               failure; since v2.39, the device does not support discard
               operation

## [](#ENVIRONMENT)ENVIRONMENT

           LIBBLKID_DEBUG=all
               Enable libblkid debug output.

## [](#AUTHORS)AUTHORS

           Lukas Czerner <lczerner@redhat.com>, Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           fstrim(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The blkdiscard command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                  BLKDISCARD(8)

------------------------------------------------------------------------

Pages that refer to this page: [fstrim(8)](../man8/fstrim.8.html),  [sfdisk(8)](../man8/sfdisk.8.html)

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
