---
{"title": "dh_installsysusers(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installsysusers.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installsysusers(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLSYSUSERS(1)           Debhelper           DH_INSTALLSYSUSERS(1)

## [](#NAME)NAME

           dh_installsysusers - install and integrates systemd sysusers files

## [](#SYNOPSIS)SYNOPSIS

           dh_installsysusers [debhelper options]

## [](#DESCRIPTION)DESCRIPTION

           dh_installsysusers is a debhelper program that is responsible for
           installing package maintainer supplied systemd sysusers files.

           It also finds the systemd sysusers files installed in a package
           and generates relevant integration snippets for enabling the users
           on installation.  These snippets are added to the package by
           dh_installdeb(1).

## [](#FILES)FILES

           debian/package.sysusers
               If the file exist, it will be installed as
               /usr/lib/sysusers.d/package.conf.

## [](#OPTIONS)OPTIONS

           --name=name
               When this parameter is used, dh_installsysusers looks for and
               installs files named debian/package.name.sysusers instead of
               the usual debian/package.sysusers.

               Furthermore, the file is installed as
               /usr/lib/sysusers.d/name.conf rather than
               /usr/lib/sysusers.d/package.conf.

## [](#NOTES)NOTES

           This command is not idempotent. dh_prep(1) should be called
           between invocations of this command (with the same arguments).
           Otherwise, it may cause multiple instances of the same text to be
           added to maintainer scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

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

    13.23                           2025-01-02          DH_INSTALLSYSUSERS(1)

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
