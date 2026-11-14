---
{"title": "blockdev(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/blockdev.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# blockdev(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMANDS](#COMMANDS) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BLOCKDEV(8)               System Administration               BLOCKDEV(8)

## [](#NAME)NAME

           blockdev - call block device ioctls from the command line

## [](#SYNOPSIS)SYNOPSIS

           blockdev [-q] [-v] command [command...] device [device...]

           blockdev --report [device...]

           blockdev -h|-V

## [](#DESCRIPTION)DESCRIPTION

           The utility blockdev allows one to call block device ioctls from
           the command line.

## [](#OPTIONS)OPTIONS

           -q
               Be quiet.

           -v
               Be verbose.

           --report
               Print a report for the specified device. It is possible to
               give multiple devices. If none is given, all devices which
               appear in /proc/partitions are shown. Note that the partition
               StartSec is in 512-byte sectors.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#COMMANDS)COMMANDS

           It is possible to give multiple devices and multiple commands.

           --flushbufs
               Flush buffers.

           --getalignoff
               Get alignment offset.

           --getbsz
               Print the blocksize in bytes. This size does not describe
               device topology. It’s the size used internally by the kernel
               and it may be modified (for example) by filesystem driver on
               mount.

           --getdiscardzeroes
               Get discard zeroes support status.

           --getdiskseq
               Get disk sequence number.

           --getzonesz
               Get zone size in 512-byte sectors.

           --getfra
               Get filesystem readahead in 512-byte sectors.

           --getiomin
               Get minimum I/O size.

           --getioopt
               Get optimal I/O size.

           --getmaxsect
               Get max sectors per request.

           --getpbsz
               Get physical block (sector) size.

           --getra
               Print readahead (in 512-byte sectors).

           --getro
               Get read-only. Print 1 if the device is read-only, 0
               otherwise.

           --getsize64
               Print device size in bytes.

           --getsize
               Print device size (32-bit!) in sectors. Deprecated in favor of
               the --getsz option.

           --getss
               Print logical sector size in bytes - usually 512.

           --getsz
               Get size in 512-byte sectors.

           --rereadpt
               Reread partition table.

           --setbsz bytes
               Set blocksize. Note that the block size is specific to the
               current file descriptor opening the block device, so the
               change of block size only persists for as long as blockdev has
               the device open, and is lost once blockdev exits.

           --setfra sectors
               Set filesystem readahead (same as --setra on 2.6 kernels).

           --setra sectors
               Set readahead (in 512-byte sectors).

           --setro
               Set read-only. The currently active access to the device may
               not be affected by the change. For example, a filesystem
               already mounted in read-write mode will not be affected. The
               change applies after remount.

           --setrw
               Set read-write.

## [](#AUTHORS)AUTHORS

           blockdev was written by Andries E. Brouwer and rewritten by Karel
           Zak.

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The blockdev command is part of the util-linux package which can
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                    BLOCKDEV(8)

------------------------------------------------------------------------

Pages that refer to this page: [fdisk(8)](../man8/fdisk.8.html),  [mount(8)](../man8/mount.8.html),  [sfdisk(8)](../man8/sfdisk.8.html),  [systemd-udevd.service(8)](../man8/systemd-udevd.service.8.html)

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
