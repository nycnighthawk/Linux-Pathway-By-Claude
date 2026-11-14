---
{"title": "systemd-userdbd.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-userdbd.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-userdbd.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-U....SERVICE(8)  systemd-userdbd.service  SYSTEMD-U....SERVICE(8)

## [](#NAME)NAME

           systemd-userdbd.service, systemd-userdbd - JSON User/Group Record
           Query Multiplexer/NSS Compatibility

## [](#SYNOPSIS)SYNOPSIS

           systemd-userdbd.service

           /usr/lib/systemd/systemd-userdbd

## [](#DESCRIPTION)DESCRIPTION

           systemd-userdbd is a system service that multiplexes user/group
           lookups to all local services that provide JSON user/group record
           definitions to the system. In addition it synthesizes JSON
           user/group records from classic UNIX/glibc NSS user/group records
           in order to provide full backwards compatibility. It may also pick
           up statically defined JSON user/group records from files in
           /etc/userdb/, /run/userdb/, /run/host/userdb/ and /usr/lib/userdb/
           with the ".user" or ".group" extension. For more details about the
           extensions read the nss-systemd(8) manpage.

           Most of systemd-userdbd's functionality is accessible through the
           userdbctl(1) command.

           The user and group records this service provides access to follow
           the JSON User Records[1] and JSON Group Record[2] definitions.
           This service implements the User/Group Record Lookup API via
           Varlink[3], and multiplexes access other services implementing
           this API, too. It is thus both server and client of this API.

           This service provides three distinct Varlink[4] services:
           io.systemd.Multiplexer provides a single, unified API for querying
           JSON user and group records. Internally it talks to all other
           user/group record services running on the system in parallel and
           forwards any information discovered. This simplifies clients
           substantially since they need to talk to a single service only
           instead of all of them in parallel.  io.systemd.NameServiceSwitch
           provides compatibility with classic UNIX/glibc NSS user records,
           i.e. converts struct passwd and struct group records as acquired
           with APIs such as getpwnam(1) to JSON user/group records, thus
           hiding the differences between the services as much as possible.
           io.systemd.DropIn makes JSON user/group records from the
           aforementioned drop-in directories available.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), nss-systemd(8), userdbctl(1), systemd-homed.service(8)

## [](#NOTES)NOTES

            1. JSON User Records
               https://systemd.io/USER_RECORD

            2. JSON Group Record
               https://systemd.io/GROUP_RECORD

            3. User/Group Record Lookup API via Varlink
               https://systemd.io/USER_GROUP_API

            4. Varlink
               https://varlink.org/

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

    systemd 262~devel                                 SYSTEMD-U....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [userdbctl(1)](../man1/userdbctl.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [nss-systemd(8)](../man8/nss-systemd.8.html)

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
