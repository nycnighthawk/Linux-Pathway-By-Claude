---
{"title": "mcookie(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mcookie.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mcookie(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MCOOKIE(1)                    User Commands                    MCOOKIE(1)

## [](#NAME)NAME

           mcookie - generate magic cookies for xauth

## [](#SYNOPSIS)SYNOPSIS

           mcookie [options]

## [](#DESCRIPTION)DESCRIPTION

           mcookie generates a 128-bit random hexadecimal number for use with
           the X authority system. Typical usage:

              xauth add :0 . mcookie

           The "random" number generated is actually the MD5 message digest
           of random information coming from one of the sources getrandom(2)
           system call, /dev/urandom, /dev/random, or the libc pseudo-random
           functions, in this preference order. See also the option --file.

## [](#OPTIONS)OPTIONS

           -f, --file file
               Use this file as an additional source of randomness (for
               example /dev/urandom). When file is '-', characters are read
               from standard input.

           -m, --max-size number
               Read from file only this number of bytes. This option is meant
               to be used when reading additional randomness from a file or
               device.

               The number argument may be followed by the multiplicative
               suffixes KiB=1024, MiB=1024*1024, and so on for GiB, TiB, PiB,
               EiB, ZiB and YiB (the "iB" is optional, e.g., "K" has the same
               meaning as "KiB") or the suffixes KB=1000, MB=1000*1000, and
               so on for GB, TB, PB, EB, ZB and YB.

           -v, --verbose
               Inform where randomness originated, with amount of entropy
               read from each source.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#FILES)FILES

           /dev/urandom

           /dev/random

## [](#BUGS)BUGS

           It is assumed that none of the randomness sources will block.

## [](#SEE_ALSO)SEE ALSO

           md5sum(1), X(7), xauth(1), rand(3)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The mcookie command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     MCOOKIE(1)

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
