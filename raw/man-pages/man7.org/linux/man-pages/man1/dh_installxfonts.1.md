---
{"title": "dh_installxfonts(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installxfonts.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installxfonts(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLXFONTS(1)             Debhelper             DH_INSTALLXFONTS(1)

## [](#NAME)NAME

           dh_installxfonts - register X fonts

## [](#SYNOPSIS)SYNOPSIS

           dh_installxfonts [debhelper options]

## [](#DESCRIPTION)DESCRIPTION

           dh_installxfonts is a debhelper program that is responsible for
           registering X fonts, so their corresponding fonts.dir,
           fonts.alias, and fonts.scale be rebuilt properly at install time.

           Before calling this program, you should have installed any X fonts
           provided by your package into the appropriate location in the
           package build directory, and if you have fonts.alias or
           fonts.scale files, you should install them into the correct
           location under etc/X11/fonts in your package build directory.

           Your package should depend on xfonts-utils so that the
           update-fonts-* commands are available. (This program adds that
           dependency to ${misc:Depends}.)

           This program automatically generates the postinst and postrm
           commands needed to register X fonts. These commands are inserted
           into the maintainer scripts by dh_installdeb. See dh_installdeb(1)
           for an explanation of how this works.

## [](#NOTES)NOTES

           See update-fonts-alias(8), update-fonts-scale(8), and
           update-fonts-dir(8) for more information about X font
           installation.

           See Debian policy, section 11.8.5. for details about doing fonts
           the Debian way.

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

    13.29                           2026-01-15            DH_INSTALLXFONTS(1)

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
