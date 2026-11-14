---
{"title": "dh_installgsettings(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installgsettings.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installgsettings(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLGSETTINGS(1)          Debhelper          DH_INSTALLGSETTINGS(1)

## [](#NAME)NAME

           dh_installgsettings - install GSettings overrides and set
           dependencies

## [](#SYNOPSIS)SYNOPSIS

           dh_installgsettings [debhelper options] [--priority=<number>]

## [](#DESCRIPTION)DESCRIPTION

           dh_installgsettings is a debhelper program that is responsible for
           installing GSettings override files and generating appropriate
           dependencies on the GSettings backend.

           The dependency on the backend will be generated in
           ${misc:Depends}.

## [](#FILES)FILES

           debian/package.gsettings-override
               Installed into
               usr/share/glib-2.0/schemas/10_package.gschema.override in the
               package build directory, with "package" replaced by the
               package name.

               The format of the file is the following:

                 [org.gnome.mypackage]
                 boolean-setting=true
                 string-setting='string'
                 ...

## [](#OPTIONS)OPTIONS

           --priority priority
               Use priority (which should be a 2-digit number) as the
               override priority instead of 10. Higher values than ten can be
               used by derived distributions (20), blend distributions (50),
               or site-specific packages (90).

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Laurent Bigonville <bigon@debian.org>, Josselin Mouette
           <joss@debian.org>

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

    13.23                           2025-01-02         DH_INSTALLGSETTINGS(1)

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
