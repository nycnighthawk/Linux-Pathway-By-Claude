---
{"title": "systemd-tty-ask-password-agent(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-tty-ask-password-agent.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-tty-ask-password-agent(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD...D-AGENT(1)  systemd-tty-ask-password-agent SYSTEMD...D-AGENT(1)

## [](#NAME)NAME

           systemd-tty-ask-password-agent - List or process pending systemd
           password requests

## [](#SYNOPSIS)SYNOPSIS

           systemd-tty-ask-password-agent [OPTIONS...] [VARIABLE=VALUE...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-tty-ask-password-agent is a password agent that handles
           password requests of the system, for example for hard disk
           encryption passwords or SSL certificate passwords that need to be
           queried at boot-time or during runtime.

           systemd-tty-ask-password-agent implements the Password Agents
           Specification[1], and is one of many possible response agents
           which answer to queries formulated with systemd-ask-password(1).

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --list
               Lists all currently pending system password requests.

               Added in version 186.

           --query
               Process all currently pending system password requests by
               querying the user on the calling TTY.

               Added in version 186.

           --watch
               Continuously process password requests.

               Added in version 186.

           --wall
               Forward password requests to wall(1) instead of querying the
               user on the calling TTY.

               Added in version 186.

           --plymouth
               Ask question with plymouth(8) instead of querying the user on
               the calling TTY.

               Added in version 186.

           --console[=DEVICE]
               Ask question on TTY DEVICE instead of querying the user on the
               calling TTY. If DEVICE is not specified, /dev/console will be
               used.

               Added in version 186.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), systemd-ask-password-console.service(8),
           wall(1), plymouth(8)

## [](#NOTES)NOTES

            1. Password Agents Specification
               https://systemd.io/PASSWORD_AGENTS/

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

    systemd 262~devel                                    SYSTEMD...D-AGENT(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-ask-password(1)](../man1/systemd-ask-password.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-ask-password-console.service(8)](../man8/systemd-ask-password-console.service.8.html)

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
