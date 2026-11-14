---
{"title": "rpm-plugin-syslog(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpm-plugin-syslog.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-plugin-syslog(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [OUTPUT](#OUTPUT) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-PLUGIN-SYSLOG(8)     System Manager's Manual     RPM-PLUGIN-SYSLOG(8)

## [](#NAME)NAME

           rpm-plugin-syslog - Syslog plugin for the RPM Package Manager

## [](#DESCRIPTION)DESCRIPTION

           The plugin writes basic information about rpm(8) transactions to
           the syslog - like transactions run and packages installed or
           removed.

## [](#CONFIGURATION)CONFIGURATION

           %__transaction_syslog_target
               Specify target output for the plugin. Supported values are:
               •   syslog: system log (default)
               •   stderr: standard error

           See rpm-plugins(8) on how to control plugins in general.

## [](#OUTPUT)OUTPUT

           The plugin uses rpm as its syslog identity.

           The package level output during transactions is as follows:

           OPERATION NEVRA [(from: RELNEVRA)]: STATUS

           OPERATION is one of:
           •   cleanup: cleanup of the previous version in upgrade or
               downgrade
           •   downgrade: downgrade an installed package to an older version
           •   erase: erase package from the system
           •   install: install a new package on the system
           •   replace: replace (obsolete) a previously installed package
               with another one
           •   restore: restore permissions and similar on an installed
               package
           •   upgrade: upgrade an installed package to a newer version

           NEVRA identifies the transaction element being operated on. Note
           that operations downgrade, replace and upgrade consist of two
           elements: install of one package version and removal of another.
           In these cases, the related element identifier RELNEVRA is
           indicated in parentheses after from:.  STATUS is one of success or
           failure.

## [](#EXAMPLES)EXAMPLES

           journalctl -t rpm
               Inspect RPM transaction history on a systemd-based OS.

           Package aaa upgrade from 1.2-1 to 2.0-1
               upgrade: aaa-2.0-1.noarch (from: aaa-1.2-1.noarch): success
               cleanup: aaa-1.2-1.noarch (from: aaa-2.0-1.noarch): success

           Package bbb 1.3-5 obsoleting aaa 1.2-1
               replace: bbb-1.3-5.noarch (from: aaa-1.2-1.noarch): success
               erase: aaa-1.2-1.noarch (from: bbb-1.3-5.noarch): success

           Package aaa 1.2-1 install failure
               install: aaa-1.2-1.noarch: failure

## [](#SEE_ALSO)SEE ALSO

           rpm(8), rpm-plugins(8), rpm-version(7) journalctl(1) syslog(3)

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

    RPM 6.1.90                      2026-08-03           RPM-PLUGIN-SYSLOG(8)

------------------------------------------------------------------------

Pages that refer to this page: [rpm-plugins(8)](../man8/rpm-plugins.8.html)

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
