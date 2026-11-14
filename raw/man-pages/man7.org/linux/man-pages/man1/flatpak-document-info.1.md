---
{"title": "flatpak-document-info(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-document-info.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-document-info(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK DOCUMENT-IN(1)    flatpak document-info    FLATPAK DOCUMENT-IN(1)

## [](#NAME)NAME

           flatpak-document-info - Show information about exported files

## [](#SYNOPSIS)SYNOPSIS

           flatpak document-info [OPTION...] FILE

## [](#DESCRIPTION)DESCRIPTION

           Shows information about an exported file, such as the document id,
           the fuse path, the original location in the filesystem, and the
           per-application permissions.

           FILE can either be a file in the fuse filesystem at
           /run/user/$UID/doc/, or a file anywhere else.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak document-info ~/Sources/gtk/gail-3.0.pc

               id: dd32c34a
               path: /run/user/1000/doc/dd32c34a/gail-3.0.pc
               origin: /home/mclasen/Sources/gtk/gail-3.0.pc
               permissions:
                       org.gnome.gedit read, write

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-document-export(1),
           flatpak-document-unexport(1), flatpak-documents(1)

## [](#COLOPHON)COLOPHON

           This page is part of the flatpak (a tool for building and
           distributing desktop applications on Linux) project.  Information
           about the project can be found at ⟨http://flatpak.org/⟩.  It is
           not known how to report bugs for this man page; if you know,
           please send a mail to man-pages@man7.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/flatpak/flatpak⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    flatpak                                            FLATPAK DOCUMENT-IN(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-document-export(1)](../man1/flatpak-document-export.1.html),  [flatpak-documents(1)](../man1/flatpak-documents.1.html),  [flatpak-document-unexport(1)](../man1/flatpak-document-unexport.1.html)

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
