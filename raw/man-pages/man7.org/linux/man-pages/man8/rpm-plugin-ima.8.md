---
{"title": "rpm-plugin-ima(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpm-plugin-ima.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-plugin-ima(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-PLUGIN-IMA(8)        System Manager's Manual        RPM-PLUGIN-IMA(8)

## [](#NAME)NAME

           rpm-plugin-ima - IMA plugin for the RPM Package Manager

## [](#DESCRIPTION)DESCRIPTION

           Integrity Measurement Architecture (IMA) and the Linux Extended
           Verification Module (EVM) allow to detect when files have been
           accidentally or maliciously altered. This plugin puts IMA/EVM
           signatures in the security.ima extended file attribute during
           installation. This requires packages to contain the signatures -
           typically by being signed with rpmsign --signfiles.

## [](#CONFIGURATION)CONFIGURATION

           The %_ima_sign_config_files macro controls whether signatures
           should also be written for config files.

           See rpm-plugins(8) on how to control plugins in general.

## [](#SEE_ALSO)SEE ALSO

           evmctl(1), rpmsign(1), rpm(8)

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

    RPM 6.1.90                      2026-08-03              RPM-PLUGIN-IMA(8)

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
