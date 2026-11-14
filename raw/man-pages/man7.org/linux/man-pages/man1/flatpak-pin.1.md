---
{"title": "flatpak-pin(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-pin.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-pin(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK PIN(1)                 flatpak pin                 FLATPAK PIN(1)

## [](#NAME)NAME

           flatpak-pin - Pin runtimes to prevent automatic removal

## [](#SYNOPSIS)SYNOPSIS

           flatpak pin [OPTION...] PATTERN...

## [](#DESCRIPTION)DESCRIPTION

           Flatpak maintains a list of patterns that define which refs are
           pinned. A pinned ref will never be automatically uninstalled (as
           are unused runtimes periodically). This can be useful if for
           example you are using a runtime for development purposes.

           Runtimes that are explicitly installed, rather than installed as a
           dependency of something else, are automatically pinned.

           The patterns are just a partial ref, with the * character matching
           anything within that part of the ref. Only runtimes can be pinned,
           not apps. Here are some example patterns:

               org.some.Runtime
               org.some.Runtime//unstable
               runtime/org.domain.*
               org.some.Runtime/arm

           To list the current set of pins, run this command without any
           patterns.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           --remove
               Instead of adding the patterns, remove matching patterns.

           -u, --user
               Pin refs in a per-user installation.

           --system
               Pin refs in the default system-wide installation.

           --installation=NAME
               Pin refs in a system-wide installation specified by NAME among
               those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           -v, --verbose
               Print debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak pin

           $ flatpak pin org.freedesktop.Platform//19.08

           $ flatpak pin --remove org.freedesktop.Platform//19.08

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-uninstall(1),

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

    flatpak                                                    FLATPAK PIN(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-update(1)](../man1/flatpak-update.1.html)

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
