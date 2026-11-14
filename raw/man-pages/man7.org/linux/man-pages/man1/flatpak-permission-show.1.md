---
{"title": "flatpak-permission-show(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-permission-show.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-permission-show(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK PERMISSION-(1)   flatpak permission-show   FLATPAK PERMISSION-(1)

## [](#NAME)NAME

           flatpak-permission-show - Show permissions

## [](#SYNOPSIS)SYNOPSIS

           flatpak permission-show [OPTION...] APP_ID

## [](#DESCRIPTION)DESCRIPTION

           Lists dynamic permissions for the given app which are stored in
           the Flatpak permission store.

           The permission store is used by portals. Each portal generally has
           its own table in the permission store, and the format of the table
           entries is specific to each portal.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-permissions(1), flatpak-permission-remove(1),
           flatpak-permission-reset(1), flatpak-permission-set(1)

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

    flatpak                                            FLATPAK PERMISSION-(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-permission-remove(1)](../man1/flatpak-permission-remove.1.html),  [flatpak-permission-reset(1)](../man1/flatpak-permission-reset.1.html),  [flatpak-permissions(1)](../man1/flatpak-permissions.1.html),  [flatpak-permission-set(1)](../man1/flatpak-permission-set.1.html)

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
