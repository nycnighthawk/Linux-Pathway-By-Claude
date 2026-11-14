---
{"title": "dh_installcatalogs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installcatalogs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installcatalogs(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLCATALOGS(1)           Debhelper           DH_INSTALLCATALOGS(1)

## [](#NAME)NAME

           dh_installcatalogs - install and register SGML Catalogs

## [](#SYNOPSIS)SYNOPSIS

           dh_installcatalogs [debhelper options] [-n]

## [](#DESCRIPTION)DESCRIPTION

           dh_installcatalogs is a debhelper program that installs and
           registers SGML catalogs. It complies with the Debian XML/SGML
           policy.

           Catalogs will be registered in a supercatalog, in
           /etc/sgml/package.cat.

           This command automatically adds maintainer script snippets for
           registering and unregistering the catalogs and supercatalogs
           (unless -n is used). These snippets are inserted into the
           maintainer scripts and the triggers file by dh_installdeb; see
           dh_installdeb(1) for an explanation of Debhelper maintainer script
           snippets.

           A dependency on sgml-base will be added to ${misc:Depends}, so be
           sure your package uses that variable in debian/control.

## [](#FILES)FILES

           debian/package.sgmlcatalogs
               Lists the catalogs to be installed per package. Each line in
               that file should be of the form "source dest", where source
               indicates where the catalog resides in the source tree, and
               dest indicates the destination location for the catalog under
               the package build area. dest should start with
               /usr/share/sgml/.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

## [](#OPTIONS)OPTIONS

           -n, --no-scripts
               Do not modify postinst/postrm/prerm scripts nor add an
               activation trigger.

## [](#NOTES)NOTES

           Note that this command is not idempotent. dh_prep(1) should be
           called between invocations of this command. Otherwise, it may
           cause multiple instances of the same text to be added to
           maintainer scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           /usr/share/doc/sgml-base-doc/

## [](#AUTHOR)AUTHOR

           Adam Di Carlo <aph@debian.org>

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

    13.23                           2025-01-02          DH_INSTALLCATALOGS(1)

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
