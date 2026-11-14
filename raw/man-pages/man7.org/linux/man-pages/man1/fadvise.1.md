---
{"title": "fadvise(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/fadvise.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fadvise(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FADVISE(1)                    User Commands                    FADVISE(1)

## [](#NAME)NAME

           fadvise - utility to use the *posix_fadvise*(2) system call

## [](#SYNOPSIS)SYNOPSIS

           fadvise [-a advice] [-o offset] [-l length] filename

           fadvise [-a advice] [-o offset] [-l length] -d file-descriptor

## [](#DESCRIPTION)DESCRIPTION

           fadvise is a simple command wrapping posix_fadvise(2) system call
           that is for predeclaring an access pattern for file data.

## [](#OPTIONS)OPTIONS

           -d, --fd file-descriptor
               Apply the advice to the file specified with the file
               descriptor instead of open a file specified with a filename.

           -a, --advice advice
               See the command output with --help option for available values
               for advice. If this option is omitted, "dontneed" is used as
               default advice.

           -o, --offset offset
               Specifies the beginning offset of the range, in bytes. If this
               option is omitted, 0 is used as default advice.

           -l, --length length
               Specifies the length of the range, in bytes. If this option is
               omitted, 0 is used as default advice.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           fadvise has the following exit status values:

           0
               success

           1
               unspecified failure

## [](#AUTHORS)AUTHORS

           Masatake YAMATO <yamato@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           posix_fadvise(2)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The fadvise command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     FADVISE(1)

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
