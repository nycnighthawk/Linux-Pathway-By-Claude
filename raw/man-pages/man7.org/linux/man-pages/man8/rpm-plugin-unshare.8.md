---
{"title": "rpm-plugin-unshare(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpm-plugin-unshare.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-plugin-unshare(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-PLUGIN-UNSHARE(8)    System Manager's Manual    RPM-PLUGIN-UNSHARE(8)

## [](#NAME)NAME

           rpm-plugin-unshare - Unshare plugin for the RPM Package Manager

## [](#DESCRIPTION)DESCRIPTION

           This plugin allows using various Linux-specific namespace-related
           technologies inside transactions, such as to harden and limit
           scriptlet access to resources.

## [](#CONFIGURATION)CONFIGURATION

           This plugin implements the following configurables:

           %__transaction_unshare_paths

               A colon-separated list of paths to privately mount during
               scriptlet execution. Typical examples would be `/tmp` to
               protect against insecure temporary file usage inside
               scriptlets, and `/home` to prevent scriptlets from accessing
               user home directories. When path unsharing is enabled, any
               mounts made from scriptlets are also private to the scriptlet
               (and vice versa, mount changes on the host are not visible to
               the scriptlet).

               Private mounts in chroot-operations is unimplemented.

           %__transaction_unshare_nonet

               Non-zero value disables network access during scriptlet
               execution.

           See rpm-plugins(8) on how to control plugins in general.

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

    RPM 6.1.90                      2026-08-03          RPM-PLUGIN-UNSHARE(8)

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
