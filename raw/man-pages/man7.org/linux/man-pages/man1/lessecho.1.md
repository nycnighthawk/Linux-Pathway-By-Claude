---
{"title": "lessecho(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lessecho.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lessecho(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LESSECHO(1)              General Commands Manual              LESSECHO(1)

## [](#NAME)NAME

           lessecho - expand metacharacters

## [](#SYNOPSIS)SYNOPSIS

           lessecho [-a] [-ox] [-cx] [-pn] [-dn] [-mx] [-nn] [-ex] file ...

           lessecho --version

## [](#DESCRIPTION)DESCRIPTION

           lessecho is a program that simply echos its arguments on standard
           output.  But any metacharacter in the output is preceded by an
           "escape" character, which by default is a backslash.  lessecho is
           invoked internally by less, and is not intended to be used
           directly by humans.

## [](#OPTIONS)OPTIONS

           A summary of options is included below.

           -ex    Specifies "x", rather than backslash, to be the escape char
                  for metachars.  If x is "-", no escape char is used and
                  arguments containing metachars are surrounded by quotes
                  instead.

           -ox    Specifies "x", rather than double-quote, to be the open
                  quote character, which is used if the -e- option is
                  specified.

           -cx    Specifies "x" to be the close quote character.

           -pn    Specifies "n" to be the open quote character, as an
                  integer.

           -dn    Specifies "n" to be the close quote character, as an
                  integer.

           -mx    Specifies "x" to be a metachar.  By default, no characters
                  are considered metachars.

           -nn    Specifies "n" to be a metachar, as an integer.

           -fn    Specifies "n" to be the escape char for metachars, as an
                  integer.

           -a     Specifies that all arguments are to be quoted.  The default
                  is that only arguments containing metacharacters are
                  quoted.

## [](#SEE_ALSO)SEE ALSO

           less(1)

## [](#AUTHOR)AUTHOR

           This manual page was written by Thomas Schoepf
           <schoepf@debian.org>, for the Debian GNU/Linux system (but may be
           used by others).

           Report bugs at https://github.com/gwsw/less/issues.

## [](#COLOPHON)COLOPHON

           This page is part of the less (A file pager) project.  Information
           about the project can be found at 
           ⟨http://www.greenwoodsoftware.com/less/⟩.  If you have a bug report
           for this manual page, see
           ⟨http://www.greenwoodsoftware.com/less/faq.html#bugs⟩.  This page
           was obtained from the tarball less-704.tar.gz fetched from
           ⟨http://www.greenwoodsoftware.com/less/download.html⟩ on
           2026-08-04.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    less 704                       30 May 2026                    LESSECHO(1)

------------------------------------------------------------------------

Pages that refer to this page: [less(1)](../man1/less.1.html)

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
