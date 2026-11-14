---
{"title": "systemd-ask-password-console.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-ask-password-wall.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-ask-password-console.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTE...ERVICE(8)  systemd-ask-password-console.service SYSTE...ERVICE(8)

## [](#NAME)NAME

           systemd-ask-password-console.service, systemd-ask-password-
           console.path, systemd-ask-password-wall.service, systemd-ask-
           password-wall.path - Query the user for system passwords on the
           console and via wall

## [](#SYNOPSIS)SYNOPSIS

               systemd-ask-password-console.service
               systemd-ask-password-console.path
               systemd-ask-password-wall.service
               systemd-ask-password-wall.path

## [](#DESCRIPTION)DESCRIPTION

           systemd-ask-password-console.service is a system service that
           queries the user for system passwords (such as hard disk
           encryption keys and SSL certificate passphrases) on the console.
           It is intended to be used during boot to ensure proper handling of
           passwords necessary for boot.  systemd-ask-password-wall.service
           is a system service that informs all logged in users for system
           passwords via wall(1). It is intended to be used after boot to
           ensure that users are properly notified.

           See the developer documentation[1] for more information about the
           system password logic.

           Note that these services invoke systemd-tty-ask-password-agent(1)
           with either the --watch --console or --watch --wall command line
           parameters.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-tty-ask-password-agent(1), wall(1)

## [](#NOTES)NOTES

            1. developer documentation
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

    systemd 262~devel                                       SYSTE...ERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-ask-password(1)](../man1/systemd-ask-password.1.html),  [systemd-tty-ask-password-agent(1)](../man1/systemd-tty-ask-password-agent.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
