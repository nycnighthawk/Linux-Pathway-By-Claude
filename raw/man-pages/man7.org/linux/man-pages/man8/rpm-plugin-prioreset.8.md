---
{"title": "rpm-plugin-prioreset(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpm-plugin-prioreset.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-plugin-prioreset(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-PLUGIN-PRIORESET(8)  System Manager's Manual  RPM-PLUGIN-PRIORESET(8)

## [](#NAME)NAME

           rpm-plugin-prioreset - Plugin for the RPM Package Manager to fix
           issues with priorities of daemons on SysV init

## [](#DESCRIPTION)DESCRIPTION

           In general scriptlets run with the same priority as rpm(8) itself.
           However on legacy SysV init systems, properties of the parent
           process can be inherited by the actual daemons on restart. As a
           result daemons may end up with unwanted nice or ionice values.
           This plugin resets the scriptlet process priorities after forking,
           and can be used to counter that effect. Should not be used with
           systemd(1) because it's not needed there, and the effect is
           counter-productive.

## [](#CONFIGURATION)CONFIGURATION

           There are currently no options for this plugin in particular. See
           rpm-plugins(8) on how to control plugins in general.

## [](#SEE_ALSO)SEE ALSO

           rpm(8), rpm-plugins(8)

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

    RPM 6.1.90                      2026-08-03        RPM-PLUGIN-PRIORESET(8)

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
