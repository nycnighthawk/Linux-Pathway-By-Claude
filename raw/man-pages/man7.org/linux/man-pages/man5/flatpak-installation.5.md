---
{"title": "flatpak-installation(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/flatpak-installation.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-installation(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLES](#EXAMPLES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK INSTALLATION(5)    flatpak installation   FLATPAK INSTALLATION(5)

## [](#NAME)NAME

           flatpak-installation - Configuration for an installation location

## [](#DESCRIPTION)DESCRIPTION

           flatpak can operate in system-wide or per-user mode. The
           system-wide data is located in $prefix/var/lib/flatpak/, and the
           per-user data is in $HOME/.local/share/flatpak/.

           In addition to the default installation locations, more
           system-wide installations can be defined via configuration files
           /etc/flatpak/installations.d/, which must have the .conf extension
           and follow the format described below.

## [](#FILE_FORMAT)FILE FORMAT

           The installation config file format is using the same .ini file
           format that is used for systemd unit files or application .desktop
           files.

       [Installation ...]
           All the configuration for the the installation location with name
           NAME is contained in the [Installation "NAME"] group.

           The following keys are recognized:

           Path (string)
               The path for this installation. This key is mandatory.

           DisplayName (string)
               The name to use when showing this installation in the UI.

           Priority (integer)
               A priority for this installation.

           StorageType (string)
               The type of storage used for this installation. Possible
               values include: network, mmc, sdcard, harddisk.

## [](#EXAMPLES)EXAMPLES

               [Installation "extra"]
               Path=/location/of/sdcard
               DisplayName=Extra Installation
               StorageType=sdcard

## [](#COLOPHON)COLOPHON

           This page is part of the flatpak (a tool for building and
           distributing desktop applications on Linux) project.  Information
           about the project can be found at ⟨http://flatpak.org/⟩.  It is
           not known how to report bugs for this man page; if you know,
           please send a mail to man-pages@man7.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/flatpak/flatpak⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    flatpak                                           FLATPAK INSTALLATION(5)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html)

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
