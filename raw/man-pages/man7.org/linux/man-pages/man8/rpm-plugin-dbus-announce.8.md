---
{"title": "rpm-plugin-dbus-announce(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpm-plugin-dbus-announce.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-plugin-dbus-announce(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [D-BUS SIGNALS](#D-BUS_SIGNALS) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-PLUGI...-ANNOUNCE(8) System Manager's Manual RPM-PLUGI...-ANNOUNCE(8)

## [](#NAME)NAME

           rpm-plugin-dbus-announce - D-Bus plugin for the RPM Package
           Manager

## [](#DESCRIPTION)DESCRIPTION

           The plugin writes basic information about rpm transactions to the
           system D-Bus - like packages installed or removed. Other programs
           can subscribe to the signals to be notified of the packages on the
           system change.

## [](#D-BUS_SIGNALS)D-BUS SIGNALS

           Sends StartTransaction, EndTransaction, StartTransactionDetails
           and EndTransactionDetails messages from the /org/rpm/Transaction
           object with the org.rpm.Transaction interface.

           The first two signals pass the DB cookie as a string and the
           transaction id as an unsigned 32 bit integer.

           The second two signals, those "details", also pass the DB cookie
           as a string and the transaction id as an unsigned 32 bit integer
           and then in addition an array of strings containing space-
           separated string of values describing the operation and the
           package NEVRA which are part of the transaction. The last argument
           is a signed integer with the transaction result.

           The package operation can be one of "added", "removed", "rpmdb" or
           "restored" (quotes for clarity only).

## [](#CONFIGURATION)CONFIGURATION

           There are currently no options for this plugin in particular. See
           rpm-plugins(8) on how to control plugins in general.

## [](#SEE_ALSO)SEE ALSO

           dbus-monitor(1), rpm-plugins(8)

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03       RPM-PLUGI...-ANNOUNCE(8)

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
