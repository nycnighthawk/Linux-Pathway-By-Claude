---
{"title": "mountpoint(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mountpoint.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mountpoint(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                     |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MOUNTPOINT(1)                 User Commands                 MOUNTPOINT(1)

## [](#NAME)NAME

           mountpoint - see if a directory or file is a mountpoint

## [](#SYNOPSIS)SYNOPSIS

           mountpoint [-d|-q] directory|file

           mountpoint -x device

## [](#DESCRIPTION)DESCRIPTION

           mountpoint checks whether the given directory or file is a
           mountpoint. On kernels that support the statmount(2) system call
           (Linux 6.8 and newer), it uses that interface. On older kernels,
           it falls back to reading /proc/self/mountinfo.

## [](#OPTIONS)OPTIONS

           -d, --fs-devno
               Show the major/minor numbers of the device that is mounted on
               the given directory.

           -q, --quiet
               Be quiet - don’t print anything.

           --nofollow
               Do not follow symbolic link if it the last element of the
               directory path.

           -x, --devno
               Show the major/minor numbers of the given blockdevice on
               standard output.

           --show
               Print the mountpoint path for the given path. This resolves
               the given directory or file to its actual mountpoint, which is
               useful with bind mounts, symbolic links, or paths within
               filesystems. This option requires kernel support for the
               statmount(2) system call (Linux 6.8 and newer). On older
               kernels, this option will fail with an error message.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           mountpoint has the following exit status values:

           0
               success; the directory is a mountpoint, or device is block
               device on --devno

           1
               failure; incorrect invocation, permissions or system error

           32
               failure; the directory is not a mountpoint, or device is not a
               block device on --devno

## [](#ENVIRONMENT)ENVIRONMENT

           LIBMOUNT_DEBUG=all
               Enable libmount debug output.

## [](#NOTES)NOTES

           The util-linux mountpoint implementation was written from scratch
           for libmount. The original version for sysvinit suite was written
           by Miquel van Smoorenburg.

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           mount(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The mountpoint command is part of the util-linux package which can
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                  MOUNTPOINT(1)

------------------------------------------------------------------------

Pages that refer to this page: [mount(2)](../man2/mount.2.html)

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
