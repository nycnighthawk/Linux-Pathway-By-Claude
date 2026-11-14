---
{"title": "dump-utmp(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dump-utmp.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dump-utmp(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSYS](#SYNOPSYS) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DUMP_UTMP(8)             System Manager's Manual             DUMP_UTMP(8)

## [](#NAME)NAME

           dump-utmp - print a utmp file in human-readable format

## [](#SYNOPSYS)SYNOPSYS

           dump-utmp [-hrR] [-n <recs>] <files>
                 [--num <recs>] [--raw] [--reverse] [--help]

## [](#OPTIONS)OPTIONS

           The following options are supported:

           -h, --help
                  Print a help message and the default location of the
                  process accounting file and exit.

           -r, --reverse
                  Print the output in reverse order.

           -R, --raw
                  The records will be printed without any parsing.

           -n, --num NUMRECS
                  Display only the first NUMRECS number of records.

## [](#SEE_ALSO)SEE ALSO

           accton(8), lastcomm(1), utmp(5)

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

    Linux accounting system      2009 December 2                 DUMP_UTMP(8)

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
