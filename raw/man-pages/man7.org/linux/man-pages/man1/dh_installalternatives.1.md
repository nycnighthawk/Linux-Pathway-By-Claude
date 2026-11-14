---
{"title": "dh_installalternatives(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installalternatives.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installalternatives(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLALTERNATIVES(1)       Debhelper       DH_INSTALLALTERNATIVES(1)

## [](#NAME)NAME

           dh_installalternatives - install declarative alternative rules

## [](#SYNOPSIS)SYNOPSIS

           dh_installalternatives [debhelper options]

## [](#DESCRIPTION)DESCRIPTION

           dh_installalternatives is a debhelper program that is responsible
           for parsing the declarative alternatives format and insert the
           relevant maintscripts snippets to interface with
           update-alternatives(1)

## [](#FILES)FILES

           debian/package.alternatives
               An example of the format:

                   Name: editor
                   Link: /usr/bin/editor
                   Alternative: /usr/bin/vim.basic
                   Dependents:
                     /usr/share/man/man1/editor.1.gz editor.1.gz /usr/share/man/man1/vim.1.gz
                     /usr/share/man/fr/man1/editor.1.gz editor.fr.1.gz /usr/share/man/fr/man1/vim.1.gz
                     /usr/share/man/it/man1/editor.1.gz editor.it.1.gz /usr/share/man/it/man1/vim.1.gz
                     /usr/share/man/pl/man1/editor.1.gz editor.pl.1.gz /usr/share/man/pl/man1/vim.1.gz
                     /usr/share/man/ru/man1/editor.1.gz editor.ru.1.gz /usr/share/man/ru/man1/vim.1.gz
                   Priority: 50

               The fields Link, Name, Alternative, and Priority are mandatory
               and correspond to the update-alternatives(1) --install
               parameters link, name, path, and priority respectively.

               The Dependents field is optional and consists of one or more
               lines. Each non-empty line must contain exactly 3 space
               separated values that match (in order) the values passed to
               the --slave parameter for update-alternatives(1).

## [](#OPTIONS)OPTIONS

           -n, --no-scripts
               Do not modify postinst/postrm/prerm scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

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

    13.25~1.gbp3d6378               2025-08-08      DH_INSTALLALTERNATIVES(1)

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
