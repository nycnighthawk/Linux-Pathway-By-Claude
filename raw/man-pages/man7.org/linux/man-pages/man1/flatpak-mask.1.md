---
{"title": "flatpak-mask(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-mask.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-mask(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK MASK(1)                flatpak mask               FLATPAK MASK(1)

## [](#NAME)NAME

           flatpak-mask - Mask out updates and automatic installation

## [](#SYNOPSIS)SYNOPSIS

           flatpak mask [OPTION...] PATTERN...

## [](#DESCRIPTION)DESCRIPTION

           Flatpak maintains a list of patterns that define which refs are
           masked. A masked ref will never be updated or automatically
           installed (for example a masked extension marked auto-download
           will not be downloaded). You can still manually install such refs,
           but once they are installed the version will be pinned.

           The patterns are just a partial ref, with the * character matching
           anything within that part of the ref. Here are some example
           patterns:

               org.some.App
               org.some.App//unstable
               app/org.domain.*
               org.some.App/arm

           To list the current set of masks, run this command without any
           patterns.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           --remove
               Instead of adding the patterns, remove matching patterns.

           -u, --user
               Mask refs in a per-user installation.

           --system
               Mask refs in the default system-wide installation.

           --installation=NAME
               Mask refs in a system-wide installation specified by NAME
               among those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           -v, --verbose
               Print debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak mask

           $ flatpak mask org.broken.App

           $ flatpak mask --remove org.broken.App

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-update(1),

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

    flatpak                                                   FLATPAK MASK(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html)

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
