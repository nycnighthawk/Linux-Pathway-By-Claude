---
{"title": "getsubids(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/getsubids.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getsubids(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GETSUBIDS(1)                  User Commands                  GETSUBIDS(1)

## [](#NAME)NAME

           getsubids - get the subordinate id ranges for a user

## [](#SYNOPSIS)SYNOPSIS

           getsubids [options] USER

## [](#DESCRIPTION)DESCRIPTION

           The getsubids command lists the subordinate user ID ranges for a
           given user. The subordinate group IDs can be listed using the -g
           option.

## [](#OPTIONS)OPTIONS

           The options which apply to the getsubids command are:

           -g
               List the subordinate group ID ranges.

           -h
               Display help message and exit.

## [](#EXAMPLE)EXAMPLE

           For example, to obtain the subordinate UIDs of the testuser:

               $ getsubids testuser
               0: testuser 100000 65536

           This command output provides (in order from left to right) the
           list index, username, UID range start, and number of UIDs in
           range.

## [](#SEE_ALSO)SEE ALSO

           login.defs(5), newgidmap(1), newuidmap(1), subgid(5), subuid(5),
           useradd(8), userdel(8).  usermod(8),

## [](#COLOPHON)COLOPHON

           This page is part of the shadow-utils (utilities for managing
           accounts and shadow password files) project.  Information about
           the project can be found at 
           ⟨https://github.com/shadow-maint/shadow⟩.  If you have a bug report
           for this manual page, send it to
           pkg-shadow-devel@alioth-lists.debian.net.  This page was obtained
           from the tarball shadow-4.19.0.tar fetched from
           ⟨https://github.com/shadow-maint/shadow/releases⟩ on 2026-08-04.
           If you discover any rendering problems in this HTML version of the
           page, or you believe there is a better or more up-to-date source
           for the page, or you have corrections or improvements to the
           information in this COLOPHON (which is not part of the original
           manual page), send a mail to man-pages@man7.org

    shadow-utils 4.19.0             08/04/2026                   GETSUBIDS(1)

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
