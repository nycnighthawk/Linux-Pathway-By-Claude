---
{"title": "org.freedesktop.timesync1(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/org.freedesktop.timesync1.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# org.freedesktop.timesync1(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [INTRODUCTION](#INTRODUCTION) \| [THE MANAGER OBJECT](#THE_MANAGER_OBJECT) \| [EXAMPLES](#EXAMPLES) \| [VERSIONING](#VERSIONING) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ORG.FRE...TIMESYNC1(5)  org.freedesktop.timesync1  ORG.FRE...TIMESYNC1(5)

## [](#NAME)NAME

           org.freedesktop.timesync1 - The D-Bus interface of
           systemd-timesyncd

## [](#INTRODUCTION)INTRODUCTION

           systemd-timesyncd.service(8) is a system service that may be used
           to synchronize the local system clock with a remote Network Time
           Protocol (NTP) server. This page describes the D-Bus interface.

## [](#THE_MANAGER_OBJECT)THE MANAGER OBJECT

           The service exposes the following interfaces on the Manager object
           on the bus:

               node /org/freedesktop/timesync1 {
                 interface org.freedesktop.timesync1.Manager {
                   methods:
                     SetRuntimeNTPServers(in  as runtime_servers);
                   properties:
                     readonly as LinkNTPServers = ['...', ...];
                     readonly as SystemNTPServers = ['...', ...];
                     readonly as RuntimeNTPServers = ['...', ...];
                     readonly as FallbackNTPServers = ['...', ...];
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
                     readonly s ServerName = '...';
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
                     readonly (iay) ServerAddress = ...;
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly t RootDistanceMaxUSec = ...;
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly t PollIntervalMinUSec = ...;
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly t PollIntervalMaxUSec = ...;
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
                     readonly t PollIntervalUSec = ...;
                     readonly (uuuuittayttttbtt) NTPMessage = ...;
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
                     readonly x Frequency = ...;
                 };
                 interface org.freedesktop.DBus.Peer { ... };
                 interface org.freedesktop.DBus.Introspectable { ... };
                 interface org.freedesktop.DBus.Properties { ... };
               };

           Provides information about the manager.

## [](#EXAMPLES)EXAMPLES

           Example 1. Introspect org.freedesktop.timesync1.Manager on the bus

               $ gdbus introspect --system \
                 --dest org.freedesktop.timesync1 \
                 --object-path /org/freedesktop/timesync1

## [](#VERSIONING)VERSIONING

           These D-Bus interfaces follow the usual interface versioning
           guidelines[1].

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-timesyncd.service(8)

## [](#NOTES)NOTES

            1. the usual interface versioning guidelines
               https://0pointer.de/blog/projects/versioning-dbus.html

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

    systemd 262~devel                                  ORG.FRE...TIMESYNC1(5)

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
