---
{"title": "rpm-plugins(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpm-plugins.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-plugins(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-PLUGINS(8)           System Manager's Manual           RPM-PLUGINS(8)

## [](#NAME)NAME

           rpm-plugins - Plugins for the RPM Package Manager

## [](#DESCRIPTION)DESCRIPTION

           RPM plugins provide functionality that is not suited to be used
           everywhere. They may not be built or shipped on some platforms or
           may not be installed or be disabled on some systems.

           This allows plugins to interface with systems that may not
           acceptable as a dependency for RPM and to provide functionality
           that may be unwanted under some circumstances.

## [](#CONFIGURATION)CONFIGURATION

           Some plugins can be configured by specific macros or influenced by
           command line parameters. But most can only be turned on or off.
           See the plugin's man page for details.

           Plugins are controlled by a macro %__transaction_NAME which is set
           to the location of the plugin file. Undefining the macro or
           setting it to %{nil} will prevent the plugin from being run.

           This can be done on the RPM command line e.g. with
           --undefine=__transaction_syslog. To disable a plugin permanently,
           place a macros.* file in /etc/rpm/ that contains

               %__transaction_NAME %{nil}

           Another option is to remove the plugin from the system if it is
           packaged in its own sub package.

           For some operations it may be desirable to disable all plugins at
           once. This can be done by passing --noplugins to rpm(8) at the
           command line.

## [](#SEE_ALSO)SEE ALSO

           rpm(8), rpm-plugin-audit(8), rpm-plugin-ima(8),
           rpm-plugin-prioreset(8), rpm-plugin-selinux(8),
           rpm-plugin-syslog(8), rpm-plugin-systemd-inhibit(8)

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

    RPM 6.1.90                      2026-08-03                 RPM-PLUGINS(8)

------------------------------------------------------------------------

Pages that refer to this page: [rpm(8)](../man8/rpm.8.html),  [rpm-plugin-audit(8)](../man8/rpm-plugin-audit.8.html),  [rpm-plugin-dbus-announce(8)](../man8/rpm-plugin-dbus-announce.8.html),  [rpm-plugin-fapolicyd(8)](../man8/rpm-plugin-fapolicyd.8.html),  [rpm-plugin-ima(8)](../man8/rpm-plugin-ima.8.html),  [rpm-plugin-prioreset(8)](../man8/rpm-plugin-prioreset.8.html),  [rpm-plugin-selinux(8)](../man8/rpm-plugin-selinux.8.html),  [rpm-plugin-syslog(8)](../man8/rpm-plugin-syslog.8.html),  [rpm-plugin-systemd-inhibit(8)](../man8/rpm-plugin-systemd-inhibit.8.html),  [rpm-plugin-unshare(8)](../man8/rpm-plugin-unshare.8.html)

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
