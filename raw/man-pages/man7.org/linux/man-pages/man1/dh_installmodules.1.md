---
{"title": "dh_installmodules(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installmodules.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installmodules(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLMODULES(1)            Debhelper            DH_INSTALLMODULES(1)

## [](#NAME)NAME

           dh_installmodules - register kernel modules

## [](#SYNOPSIS)SYNOPSIS

           dh_installmodules [debhelper options] [-n] [--name=name]

## [](#DESCRIPTION)DESCRIPTION

           dh_installmodules is a debhelper program that is responsible for
           registering kernel modules.

           Kernel modules are searched for in the package build directory and
           if found, preinst, postinst and postrm commands are automatically
           generated to run depmod and register the modules when the package
           is installed.  These commands are inserted into the maintainer
           scripts by dh_installdeb(1).

## [](#FILES)FILES

           debian/package.modprobe
               Installed to usr/lib/modprobe.d/package.conf in the package
               build directory.  Before compat version 14, files get
               installed under etc/modprobe.d instead.

## [](#OPTIONS)OPTIONS

           -n, --no-scripts
               Do not modify preinst/postinst/postrm scripts.

           --name=name
               When this parameter is used, dh_installmodules looks for and
               installs files named debian/package.name.modprobe instead of
               the usual debian/package.modprobe

## [](#NOTES)NOTES

           Note that this command is not idempotent. dh_prep(1) should be
           called between invocations of this command. Otherwise, it may
           cause multiple instances of the same text to be added to
           maintainer scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

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

    13.25~1.gbp3d6378               2025-08-08           DH_INSTALLMODULES(1)

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
