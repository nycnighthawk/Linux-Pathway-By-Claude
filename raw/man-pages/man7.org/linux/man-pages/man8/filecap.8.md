---
{"title": "filecap(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/filecap.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# filecap(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FILECAP:(8)          System Administration Utilities          FILECAP:(8)

## [](#NAME)NAME

           filecap - a program to see capabilities

## [](#SYNOPSIS)SYNOPSIS

           filecap [ -a | -d | /dir | /dir/file [cap1 cap2 ...] ]

## [](#DESCRIPTION)DESCRIPTION

           filecap is a program that prints out a report of programs with
           file based capabilities. If a file is not in the report or there
           is no report at all, no capabilities were found. For expedience,
           the default is to check only the directories in the PATH
           environmental variable. If the -a command line option is given,
           then all directories will be checked. If a directory is passed, it
           will recursively check that directory. If a path to a file is
           given, it will only check that file. If a file is given followed
           by capabilities, then the capabilities are written to the file.

## [](#OPTIONS)OPTIONS

           -a     This tells the program to show all capabilities starting
                  from the / directory. Normally the PATH environmental
                  variable is used to show you capabilities on files you are
                  likely to execute.

           -d     This dumps all capabilities for reference.

## [](#EXAMPLES)EXAMPLES

           To check file capabilities in $PATH:
           filecap

           To check file capabilities of whole system:
           filecap -a

           To check file capabilities recursively in a directory:
           filecap /usr

           To check file capabilities of a specific program:
           filecap /bin/passwd

           To list all possible capabilities:
           filecap -d

           To set a file capability on a specific program:
           filecap /bin/ping net_raw net_admin

           To remove file capabilities on a specific program:
           filecap /bin/ping none

## [](#SEE_ALSO)SEE ALSO

           pscap(8), netcap(8), capabilities(7).

## [](#AUTHOR)AUTHOR

           Steve Grubb

## [](#COLOPHON)COLOPHON

           This page is part of the libcap-ng (capabilities commands and
           library (NG)) project.  Information about the project can be found
           at ⟨https://people.redhat.com/sgrubb/libcap-ng/⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           tarball fetched from
           ⟨https://people.redhat.com/sgrubb/libcap-ng/index.html⟩ on
           2026-08-04.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Red Hat                          Aug 2018                     FILECAP:(8)

------------------------------------------------------------------------

Pages that refer to this page: [capabilities(7)](../man7/capabilities.7.html),  [captest(8)](../man8/captest.8.html),  [netcap(8)](../man8/netcap.8.html),  [pscap(8)](../man8/pscap.8.html)

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
