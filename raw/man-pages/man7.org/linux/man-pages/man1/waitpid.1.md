---
{"title": "waitpid(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/waitpid.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# waitpid(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WAITPID(1)                    User Commands                    WAITPID(1)

## [](#NAME)NAME

           waitpid - utility to wait for arbitrary processes

## [](#SYNOPSIS)SYNOPSIS

           waitpid [-v] [--timeout|-t seconds] PID[:inode]...

## [](#DESCRIPTION)DESCRIPTION

           waitpid is a simple command to wait for arbitrary non-child
           processes.

           It exits after all processes whose PIDs have been passed as
           arguments have exited.

           Optionally, a process can be addressed with the format PID:inode.
           The inode identifies the unique process’s file descriptor. To
           retrieve a process’s inode number you can use the getino(1)
           utility.

## [](#OPTIONS)OPTIONS

           -v, --verbose
               Be more verbose.

           -t, --timeout seconds
               Maximum wait time.

           -e, --exited
               Don’t error on already exited PIDs.

           -c, --count count
               Number of process exits to wait for.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           waitpid has the following exit status values:

           0
               success

           1
               unspecified failure

           2
               system does not provide necessary functionality

           3
               timeout expired

## [](#AUTHORS)AUTHORS

           Thomas Weißschuh <thomas@t-8ch.de>

## [](#SEE_ALSO)SEE ALSO

           waitpid(2), wait(1P), getino(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The waitpid command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     WAITPID(1)

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
