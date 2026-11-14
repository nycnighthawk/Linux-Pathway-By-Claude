---
{"title": "dump-acct(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dump-acct.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dump-acct(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DUMP_ACCT(8)             System Manager's Manual             DUMP_ACCT(8)

## [](#NAME)NAME

           dump-acct - print an acct/pacct file in human-readable format

## [](#SYNOPSIS)SYNOPSIS

           dump-acct [-r|--reverse] [-R|--raw] [-n|--num recs] [--byte-swap]
           [--format] [--ahz freq] [-h|--help] [files]

## [](#DESCRIPTION)DESCRIPTION

           The dump-acct command transforms the output file from the accton
           format to the human-readable format: one record per line.  Each
           record consists of severald fields which are separated by
           character "|" (the meaning of concreate field depends on the
           version of kernel package - with which the accton file was
           created).

## [](#OPTIONS)OPTIONS

           The following options are supported:

           -r, --reverse
                  Print the output in reverse order.

           -R, --raw
                  The records will be printed without any parsing.

           -n, --num NUMRECS
                  Display only the first NUMRECS number of records.

           --byteswap
                  Swap the bytes (relative to your system's native byte
                  order) in --raw output.

           --format
                  Set output format with --raw option.

           --ahz FREQ
                  Set the AHZ (platform dependent frequency in Hertz) to
                  FREQ.

           -h, --help
                  Print a help message and the default location of the
                  process accounting file and exit.

## [](#SEE_ALSO)SEE ALSO

           accton(8), lastcomm(1)

## [](#COLOPHON)COLOPHON

           This page is part of the psacct (process accounting utilities)
           project.  Information about the project can be found at 
           ⟨http://www.gnu.org/software/acct/⟩.  If you have a bug report for
           this manual page, see ⟨http://www.gnu.org/software/acct/⟩.  This
           page was obtained from the tarball acct-6.6.4.tar.gz fetched from
           ⟨http://ftp.gnu.org/gnu/acct/⟩ on 2026-08-04.  If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Linux accounting system      2009 December 2                 DUMP_ACCT(8)

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
