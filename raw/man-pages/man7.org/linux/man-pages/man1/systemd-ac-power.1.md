---
{"title": "systemd-ac-power(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-ac-power.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-ac-power(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-AC-POWER(1)          systemd-ac-power         SYSTEMD-AC-POWER(1)

## [](#NAME)NAME

           systemd-ac-power - Report whether we are connected to an external
           power source

## [](#SYNOPSIS)SYNOPSIS

           systemd-ac-power [OPTIONS...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-ac-power may be used to check whether the system is
           running on AC power or not. By default, it will simply return
           success (if we can detect that we are running on AC power) or
           failure, with no output. This can be useful for example to debug
           ConditionACPower= (see systemd.unit(5)).

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -v, --verbose
               Show result as text instead of just returning success or
               failure.

               Added in version 253.

           --low
               Instead of showing AC power state, show low battery state. In
               this case, will return zero if all batteries are currently
               discharging and below 5% of maximum charge. Returns non-zero
               otherwise.

               Added in version 254.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success (running on AC power), 0 is returned, a non-zero
           failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1)

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

    systemd 262~devel                                     SYSTEMD-AC-POWER(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
