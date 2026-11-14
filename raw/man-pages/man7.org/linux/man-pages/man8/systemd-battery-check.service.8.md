---
{"title": "systemd-battery-check.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-battery-check.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-battery-check.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-BA...K.SERVICE(8) systemd-battery-check SYSTEMD-BA...K.SERVICE(8)

## [](#NAME)NAME

           systemd-battery-check.service, systemd-battery-check - Check
           battery level whether there's enough charge, and power off if not

## [](#SYNOPSIS)SYNOPSIS

           systemd-battery-check.service

           /usr/lib/systemd/systemd-battery-check [OPTIONS...]

## [](#DESCRIPTION)DESCRIPTION

           This service checks the presence of an external power supply and
           the battery level during the early boot stage to determine whether
           there is sufficient power to carry on with the booting process.

           systemd-battery-check returns success if the device is connected
           to an AC power source or if the battery charge is greater than 5%.
           It returns failure otherwise.

## [](#OPTIONS)OPTIONS

           The following options are understood by systemd-battery-check:

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success (running on AC power or battery capacity greater than
           5%), 0 is returned, a non-zero failure code otherwise.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           The following variables are understood:

           systemd.battery_check=BOOL
               Takes a boolean. If specified with false,
               systemd-battery-check command will return immediately with
               exit status 0 without checking battery capacity and AC power
               existence, and the service systemd-battery-check.service will
               succeed. This may be useful when the command wrongly detects
               and reports battery capacity percentage or AC power existence,
               or when you want to boot the system forcibly.

               Added in version 254.

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

    systemd 262~devel                               SYSTEMD-BA...K.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
