---
{"title": "accton(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/accton.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# accton(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ACCTON(8)                System Manager's Manual                ACCTON(8)

## [](#NAME)NAME

           accton -  turns process accounting on or off

## [](#SYNOPSIS)SYNOPSIS

           accton [OPTION] on|off|filename

           accton [ -V | --version ] [ -h | --help ]

## [](#DESCRIPTION)DESCRIPTION

           accton filename turns on process accounting.

## [](#OPTIONS)OPTIONS

           -V, --version
                  Print the version number of ac to standard output and quit.
           -h, --help
                  Prints the usage string and default locations of system
                  files to standard output and exits.
           on     Turns on process accounting using the default accounting
                  file name.
           off    Turns off process accounting.

## [](#FILES)FILES

           acct   The system wide process accounting file. See acct(5) (or
                  pacct(5)) for further details.

## [](#AUTHOR)AUTHOR

           The GNU accounting utilities were written by Noel Cragg
           <noel@gnu.ai.mit.edu>. The man page was adapted from the
           accounting texinfo page by Susan Kleinmann <sgk@sgk.tiac.net>.

## [](#SEE_ALSO)SEE ALSO

           acct(5), ac(1)

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

                                 2008 November 24                   ACCTON(8)

------------------------------------------------------------------------

Pages that refer to this page: [acct(5)](../man5/acct.5.html),  [dump-acct(8)](../man8/dump-acct.8.html),  [dump-utmp(8)](../man8/dump-utmp.8.html)

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
