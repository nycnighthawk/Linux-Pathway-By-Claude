---
{"title": "yum-cron(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/yum-cron.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-cron(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-cron(8)                                                   yum-cron(8)

## [](#NAME)NAME

           yum-cron - an interface to conveniently call yum from cron

## [](#SYNOPSIS)SYNOPSIS

           yum-cron [config-file]

## [](#DESCRIPTION)DESCRIPTION

           yum-cron is an alternate interface to yum that is optimised to be
           convenient to call from cron.  It provides methods to keep
           repository metadata up to date, and to check for, download, and
           apply updates.  Rather than accepting many different command line
           arguments, the different functions of yum-cron can be accessed
           through config files.

           config-file is used to optionally specify the path to the
           configuration file to use.  If it is not given, the default
           configuration file will be used.  It is useful to be able to
           specify different configuration files for different use cases.
           For example, one configuration file might be set to update the
           repository metadata, and a line could be added to the crontab to
           run yum-cron frequently using this file.  Then, another
           configuration file might be set to install updates, and yum-cron
           could be run from cron using this file just once each day.

## [](#FILES)FILES

           /etc/yum/yum-cron.conf
           /etc/yum/yum-cron-hourly.conf
           /etc/yum/yum-cron-security.conf

## [](#SEE_ALSO)SEE ALSO

           yum(8)

## [](#AUTHORS)AUTHORS

           See the Authors file included with this program.

## [](#BUGS)BUGS

           There of course aren't any bugs, but if you find any, you should
           email
            the mailing list, yum@lists.baseurl.org, or consult bugzilla.

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

    Nick Jacek                                                    yum-cron(8)

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
