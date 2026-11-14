---
{"title": "yum-updatesd.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/yum-updatesd.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-updatesd.conf(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [PARAMETERS](#PARAMETERS) \| [\[main\] OPTIONS](#%5Bmain%5D_OPTIONS) \| [MAIL OPTIONS](#MAIL_OPTIONS) \| [SYSLOG OPTIONS](#SYSLOG_OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-updatesd.conf(5) yum-updatesd configuration file yum-updatesd.conf(5)

## [](#NAME)NAME

           yum-updatesd.conf - Configuration file for yum-updatesd(8).

## [](#DESCRIPTION)DESCRIPTION

           yum-updatesd uses a configuration file at /etc/yum/yum-
           updatesd.conf.

           Additional configuration information is read from the main
           yum.conf (5) configuration file.

## [](#PARAMETERS)PARAMETERS

           There is one section in the yum-updatesd configuration file, main,
           which defines all of the global configuration options.

## [](#%5Bmain%5D_OPTIONS)\[main\] OPTIONS

           The [main] section must exist for yum-updatesd to do anything. It
           consists of the following options:

           run_interval
                  Number of seconds to wait between checks for available
                  updates.

           updaterefresh
                  Minimum number of seconds between update information
                  refreshes to avoid hitting the server too often.

           emit_via
                  List of ways to emit update notification.  Valid values are
                  `email', `dbus' and `syslog'.

           do_update
                  Boolean option to decide whether or not updates should be
                  automatically applied.  Defaults to False.

           do_download_deps
                  Boolean option to decide whether or not updates should be
                  automatically downloaded.  Defaults to False.

           do_download_deps
                  Boolean option to automatically download dependencies of
                  packages which need updating as well.  Defaults to False.

## [](#MAIL_OPTIONS)MAIL OPTIONS

           email_to
                  List of email addresses to send update notification to.
                  Defaults to `root@localhost'.

           email_from
                  Email address for update notifications to be from.
                  Defaults to `yum-updatesd@localhost'.

## [](#SYSLOG_OPTIONS)SYSLOG OPTIONS

           syslog_facility
                  What syslog facility should be used.  Defaults to `DAEMON'.

           syslog_level
                  Level of syslog messages.  Defaults to `WARN'.

## [](#FILES)FILES

           /etc/yum/yum-updatesd.conf

## [](#SEE_ALSO)SEE ALSO

           yum-updatesd(8) yum.conf(5)

## [](#COLOPHON)COLOPHON

           This page is part of the yum (Yum Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/yum⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/yum.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2021-04-02.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Jeremy Katz                                          yum-updatesd.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [yum-updatesd(8)](../man8/yum-updatesd.8.html)

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
