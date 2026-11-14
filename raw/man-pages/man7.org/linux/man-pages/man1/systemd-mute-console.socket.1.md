---
{"title": "systemd-mute-console(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-mute-console.socket.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-mute-console(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-MUTE-CONSOLE(1)    systemd-mute-console   SYSTEMD-MUTE-CONSOLE(1)

## [](#NAME)NAME

           systemd-mute-console, systemd-mute-console@.service, systemd-mute-
           console.socket - Temporarily mute kernel log output and service
           manager status output to the system console

## [](#SYNOPSIS)SYNOPSIS

           systemd-mute-console [OPTIONS...]

           systemd-mute-console@.service

           systemd-mute-console.socket

## [](#DESCRIPTION)DESCRIPTION

           The systemd-mute-console tool and service may be used to
           temporarily mute the log output of the kernel as well as the
           status output of the service manager to the system console. It may
           be used by tools running on the console to ensure their terminal
           output is not interrupted by unrelated messages.

           The tool can be invoked directly in which case it will mute the
           two outputs and then issue an sd_notify(3) "READY=1" notification
           once that is completed. On SIGINT or SIGTERM output is unmuted
           again. Alternatively it can be invoked via Varlink IPC.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --kernel=bool, --pid1=bool
               Individually controls which output to mute. If true is
               specified the respective output is muted, if false the output
               is left as is. Defaults to true.

               Added in version 259.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-firstboot(1)

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

    systemd 262~devel                                 SYSTEMD-MUTE-CONSOLE(1)

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
