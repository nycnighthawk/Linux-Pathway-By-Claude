---
{"title": "pscap(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pscap.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pscap(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PSCAP:(8)            System Administration Utilities            PSCAP:(8)

## [](#NAME)NAME

           pscap - a program to see capabilities

## [](#SYNOPSIS)SYNOPSIS

           pscap [ -a ] [ -p pid ] [ --tree ]

## [](#DESCRIPTION)DESCRIPTION

           pscap is a program that prints out a report of process
           capabilities. If the application has any capabilities, it will be
           in the report. By giving a pid with the -p command line option,
           only the process specified with the pid is reported. If a process
           is not in the report, it has dropped all capabilities. If the
           process has partial capabilities, it is further examined to see if
           it has an open-ended bounding set. If this is found to be true, a
           '+' symbol is added. If the process has ambient capabilities, an
           '@' symbol is added.

           The command name in the output may be followed by an asterisk mark
           (*). This mark denotes processes which run in child user
           namespaces (relative to the user namespace of pscap itself).

           The --tree option causes the output of the program to be mapped
           into a tree structure so that the relationships between processes
           can be studied to see what capabilities might be leaked to child
           processes.  In tree mode, each process label is shown as
           command(pid:account).

## [](#SEE_ALSO)SEE ALSO

           netcap(8), filecap(8), capabilities(7), ps(8).

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

    Red Hat                         March 2026                      PSCAP:(8)

------------------------------------------------------------------------

Pages that refer to this page: [capabilities(7)](../man7/capabilities.7.html),  [filecap(8)](../man8/filecap.8.html),  [netcap(8)](../man8/netcap.8.html)

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
