---
{"title": "setsid(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/setsid.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setsid(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SETSID(1)                     User Commands                     SETSID(1)

## [](#NAME)NAME

           setsid - run a program in a new session

## [](#SYNOPSIS)SYNOPSIS

           setsid [options] program [arguments]

## [](#DESCRIPTION)DESCRIPTION

           setsid runs a program in a new session. The command calls fork(2)
           if already a process group leader. Otherwise, it executes a
           program in the current process. This default behavior is possible
           to override by the --fork option.

## [](#OPTIONS)OPTIONS

           -c, --ctty
               Set the controlling terminal to the current one.

           -f, --fork
               Always create a new process.

           -w, --wait
               Wait for the execution of the program to end, and return the
               exit status of this program as the exit status of setsid.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#AUTHORS)AUTHORS

           Rick Sladkey <jrs@world.std.com>

## [](#SEE_ALSO)SEE ALSO

           setsid(2)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The setsid command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                      SETSID(1)

------------------------------------------------------------------------

Pages that refer to this page: [socat(1)](../man1/socat.1.html),  [setsid(2)](../man2/setsid.2.html)

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
