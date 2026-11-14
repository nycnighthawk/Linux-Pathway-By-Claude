---
{"title": "systemd-xdg-autostart-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-xdg-autostart-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-xdg-autostart-generator(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEM...NERATOR(8)  systemd-xdg-autostart-generator  SYSTEM...NERATOR(8)

## [](#NAME)NAME

           systemd-xdg-autostart-generator - User unit generator for XDG
           autostart files

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/user-generators/systemd-xdg-autostart-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-xdg-autostart-generator is a generator that creates
           .service units for XDG autostart[1] files. This permits desktop
           environments to delegate startup of these applications to
           systemd(1) .

           Units created by systemd-xdg-autostart-generator can be started by
           the desktop environment using "xdg-desktop-autostart.target". See
           systemd.special(7) for more details.

           XDG autostart may be conditionalized using both standardized and
           non-standardized keys. In order to handle these, the generator may
           create one or more ExecCondition= entries. For non-standardized
           keys, well-known helper binaries provided by Desktop Environments
           are used. All external helpers must detect their corresponding
           desktop environment and must return success when run in a
           different environment. This is important as all ExecCondition=
           directives must succeed for an application to be started.

           Table 1.  Special XDG desktop file entries that are processed
           ┌────────────────────────────┬───────────────────────────────────┐
           │ Entry                      │ Handling                          │
           ├────────────────────────────┼───────────────────────────────────┤
           │ Hidden=, X-systemd-skip=   │ No service will be                │
           │                            │ generated if set to true          │
           ├────────────────────────────┼───────────────────────────────────┤
           │ OnlyShowIn=, NotShowIn=    │ ExecCondition= using              │
           │                            │ systemd-xdg-autostart-condition   │
           ├────────────────────────────┼───────────────────────────────────┤
           │ TryExec=                   │ No service will be generated if   │
           │                            │ the binary does not exist or      │
           │                            │ cannot be executed                │
           ├────────────────────────────┼───────────────────────────────────┤
           │ AutostartCondition=        │ ExecCondition= using              │
           │ (GNOME extension)          │ gnome-systemd-autostart-condition │
           ├────────────────────────────┼───────────────────────────────────┤
           │ X-GNOME-Autostart-Phase=   │ No service will be generated if   │
           │                            │ set to any value                  │
           ├────────────────────────────┼───────────────────────────────────┤
           │ X-KDE-autostart-condition= │ ExecCondition= using              │
           │                            │ kde-systemd-start-condition       │
           └────────────────────────────┴───────────────────────────────────┘

           systemd-xdg-autostart-generator implements systemd.generator(7).

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.service(5), systemd.target(5)

## [](#NOTES)NOTES

            1. XDG autostart
               https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                     SYSTEM...NERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.generator(7)](../man7/systemd.generator.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html)

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
