---
{"title": "enosys(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/enosys.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# enosys(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [EXIT STATUS](#EXIT_STATUS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ENOSYS(1)                     User Commands                     ENOSYS(1)

## [](#NAME)NAME

           enosys - utility to make syscalls fail with ENOSYS

## [](#SYNOPSIS)SYNOPSIS

           enosys [--syscall|-s syscall] command

## [](#DESCRIPTION)DESCRIPTION

           enosys is a simple command to execute a child process for which
           certain syscalls fail with errno ENOSYS.

           It can be used to test the behavior of applications in the face of
           missing syscalls as would happen when running on old kernels.

## [](#OPTIONS)OPTIONS

           -s, --syscall
               Syscall to block with ENOSYS. Can be specified multiple times.
               An alternative error number or name can be specified with a
               colon.

           -i, --ioctl
               Ioctl to block with ENOTTY. Can be specified multiple times.
               An alternative error number or name can be specified with a
               colon.

           -l, --list
               List syscalls known to enosys.

           -m, --list-ioctl
               List ioctls known to enosys.

           -d, --dump[=file]
               Dump seccomp bytecode filter to standard output.

               The dump can for example be used by setpriv --seccomp-filter.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXAMPLES)EXAMPLES

               # fail syscall "fallocate" with ENOSYS
               enosys -s fallocate ...

               # fail syscall "fallocate" with ENOMEM
               enosys -s fallocate:ENOMEM ...

               # fail syscall "fallocate" with value 12/ENOMEM
               enosys -s fallocate:12 ...

               # fail ioctl FIOCLEX with ENOTTY
               enosys -i FIOCLEX ...

               # fail ioctl FIOCLEX with ENOMEM
               enosys -i FIOCLEX:ENOMEM ...

               # fail ioctl FIOCLEX with value 12/ENOMEM
               enosys -i FIOCLEX:12 ...

## [](#EXIT_STATUS)EXIT STATUS

           enosys exits with the status code of the executed process. The
           following values have special meanings:

           1
               internal error

           2
               system does not provide the necessary functionality

## [](#AUTHORS)AUTHORS

           Thomas Weißschuh <thomas@t-8ch.de>

## [](#SEE_ALSO)SEE ALSO

           syscall(2)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The enosys command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                      ENOSYS(1)

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
