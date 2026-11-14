---
{"title": "dh_installemacsen(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installemacsen.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installemacsen(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLEMACSEN(1)            Debhelper            DH_INSTALLEMACSEN(1)

## [](#NAME)NAME

           dh_installemacsen - register an Emacs add on package

## [](#SYNOPSIS)SYNOPSIS

           dh_installemacsen [debhelper options] [-n] [--priority=n]
           [--flavor=foo]

## [](#DESCRIPTION)DESCRIPTION

           dh_installemacsen is a debhelper program that is responsible for
           installing files used by the Debian emacsen-common package into
           package build directories.

           It also automatically generates the preinst postinst and prerm
           commands needed to register a package as an Emacs add on package.
           The commands are added to the maintainer scripts by dh_installdeb.
           See dh_installdeb(1) for an explanation of how this works.

## [](#FILES)FILES

           debian/package.emacsen-compat
               Installed into usr/lib/emacsen-common/packages/compat/package
               in the package build directory.

           debian/package.emacsen-install
               Installed into usr/lib/emacsen-common/packages/install/package
               in the package build directory.

           debian/package.emacsen-remove
               Installed into usr/lib/emacsen-common/packages/remove/package
               in the package build directory.

           debian/package.emacsen-startup
               Installed into etc/emacs/site-start.d/50package.el in the
               package build directory. Use --priority to use a different
               priority than 50.

## [](#OPTIONS)OPTIONS

           -n, --no-scripts
               Do not modify postinst/prerm scripts.

           --priority=n
               Sets the priority number of a site-start.d file. Default is
               50.

           --flavor=foo
               Sets the flavor a site-start.d file will be installed in.
               Default is emacs, alternatives include xemacs and emacs20.

## [](#NOTES)NOTES

           Note that this command is not idempotent. dh_prep(1) should be
           called between invocations of this command. Otherwise, it may
           cause multiple instances of the same text to be added to
           maintainer scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7) "usr/share/doc/emacsen-common/debian-emacs-policy.gz"

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Joey Hess <joeyh@debian.org>

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

    13.23                           2025-01-02           DH_INSTALLEMACSEN(1)

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
