---
{"title": "dh_usrlocal(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_usrlocal.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_usrlocal(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [CONFORMS TO](#CONFORMS_TO) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_USRLOCAL(1)                  Debhelper                  DH_USRLOCAL(1)

## [](#NAME)NAME

           dh_usrlocal - migrate usr/local directories to maintainer scripts

## [](#SYNOPSIS)SYNOPSIS

           dh_usrlocal [debhelper options] [-n]

## [](#DESCRIPTION)DESCRIPTION

           dh_usrlocal is a debhelper program that can be used for building
           packages that will provide a subdirectory in /usr/local when
           installed.

           It finds subdirectories of usr/local in the package build
           directory, and removes them, replacing them with maintainer script
           snippets (unless -n is used) to create the directories at install
           time, and remove them when the package is removed, in a manner
           compliant with Debian policy. These snippets are inserted into the
           maintainer scripts by dh_installdeb. See dh_installdeb(1) for an
           explanation of debhelper maintainer script snippets.

           When the DEB_RULES_REQUIRES_ROOT environment variable is not
           (effectively) binary-targets, the directories in /usr/local will
           be handled as if they were owned by root:root (see below).

           When the DEB_RULES_REQUIRES_ROOT environment variable has an
           effective value of binary-targets, the owners, groups and
           permissions will be preserved with the sole exception where the
           directory is owned by root:root.

           If a directory is owned by root:root, then ownership will be
           determined at install time.  The ownership and permission bits
           will either be root:root mode 0755 or root:staff mode 02775.  The
           actual choice depends on whether the system has
           /etc/staff-group-for-usr-local (as documented in the Debian Policy
           Manual §9.1.2 since version 4.1.4)

## [](#OPTIONS)OPTIONS

           -n, --no-scripts
               Do not modify postinst/prerm scripts.

## [](#NOTES)NOTES

           Note that this command is not idempotent. dh_prep(1) should be
           called between invocations of this command. Otherwise, it may
           cause multiple instances of the same text to be added to
           maintainer scripts.

## [](#CONFORMS_TO)CONFORMS TO

           Debian policy, version 2.2

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Andrew Stribblehill <ads@debian.org>

## [](#COLOPHON)COLOPHON

           This page is part of the debhelper (helper programs for
           debian/rules) project.  Information about the project can be found
           at [unknown -- if you know, please contact man-pages@man7.org] If
           you have a bug report for this manual page, send it to
           submit@bugs.debian.org.  This page was obtained from the project's
           upstream Git repository
           ⟨https://salsa.debian.org/debian/debhelper.git⟩ on 2026-08-03.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    13.29                           2026-01-15                 DH_USRLOCAL(1)

------------------------------------------------------------------------

Pages that refer to this page: [debhelper(7)](../man7/debhelper.7.html)

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
