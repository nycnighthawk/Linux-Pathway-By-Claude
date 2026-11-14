---
{"title": "yum-updatesd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/yum-updatesd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-updatesd(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-updatesd(8)                                           yum-updatesd(8)

## [](#NAME)NAME

           yum-updatesd - Update notifier daemon

## [](#SYNOPSIS)SYNOPSIS

           yum-updatesd

## [](#DESCRIPTION)DESCRIPTION

           yum-updatesd provides notification of updates which are available
           to be applied to your system.  This notification can be done
           either via syslog, email or over dbus.  Configuration is done via
           the yum-updatesd.conf(5)  file.

## [](#SEE_ALSO)SEE ALSO

           yum(8)
           yum-updatesd.conf(5)
           http://yum.baseurl.org/

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

    Jeremy Katz                                               yum-updatesd(8)

------------------------------------------------------------------------

Pages that refer to this page: [yum-updatesd.conf(5)](../man5/yum-updatesd.conf.5.html),  [yum(8@@yum)](../man8/yum.8@@yum.html)

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
