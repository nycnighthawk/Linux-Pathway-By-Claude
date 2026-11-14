---
{"title": "systemd-bsod.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-bsod.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-bsod.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-BSOD.SERVICE(8)        systemd-bsod       SYSTEMD-BSOD.SERVICE(8)

## [](#NAME)NAME

           systemd-bsod.service, systemd-bsod - Displays boot-time emergency
           log message in full screen

## [](#SYNOPSIS)SYNOPSIS

           systemd-bsod.service

           /usr/lib/systemd/systemd-bsod [OPTIONS...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-bsod.service is used to display a blue screen which
           contains a message relating to a boot failure, including a QR code
           which can be scanned to get helpful information about the failure.

## [](#OPTIONS)OPTIONS

           The following options are understood by systemd-bsod:

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

           -c, --continuous
               When specified, systemd-bsod waits continuously for changes in
               the journal if it does not find any emergency messages on the
               initial attempt.

               Added in version 255.

           --tty=
               Specify the TTY to output to. By default, systemd-bsod will
               automatically find a free VT to display the message on. If
               this option is specified a TTY may be selected explicitly. Use
               --tty=/dev/tty to direct output to the terminal the command is
               invoked on.

               Added in version 256.

## [](#EXIT_STATUS)EXIT STATUS

           On success (displaying the journal message successfully), 0 is
           returned, a non-zero failure code otherwise.

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

    systemd 262~devel                                 SYSTEMD-BSOD.SERVICE(8)

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
