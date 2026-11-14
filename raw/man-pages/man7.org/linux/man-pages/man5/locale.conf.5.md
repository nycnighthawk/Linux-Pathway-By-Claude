---
{"title": "locale.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/locale.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# locale.conf(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LOCALE.CONF(5)                 locale.conf                 LOCALE.CONF(5)

## [](#NAME)NAME

           locale.conf - Configuration file for locale settings

## [](#SYNOPSIS)SYNOPSIS

           /etc/locale.conf

## [](#DESCRIPTION)DESCRIPTION

           The /etc/locale.conf file configures system-wide locale settings.
           It is read at early boot by systemd(1).

           The format of locale.conf is a newline-separated list of
           environment-like shell-compatible variable assignments, ignoring
           comments and empty lines. It is possible to source the
           configuration from shell scripts, however, beyond mere variable
           assignments, no shell features are supported, allowing
           applications to read the file without implementing a shell
           compatible execution engine. See os-release(5) for a detailed
           description of the format.

           Note that the kernel command line options locale.LANG=,
           locale.LANGUAGE=, locale.LC_CTYPE=, locale.LC_NUMERIC=,
           locale.LC_TIME=, locale.LC_COLLATE=, locale.LC_MONETARY=,
           locale.LC_MESSAGES=, locale.LC_PAPER=, locale.LC_NAME=,
           locale.LC_ADDRESS=, locale.LC_TELEPHONE=, locale.LC_MEASUREMENT=,
           locale.LC_IDENTIFICATION= may be used to override the locale
           settings at boot.

           The locale settings configured in /etc/locale.conf are system-wide
           and are inherited by every service or user, unless overridden or
           unset by individual programs or users.

           Depending on the operating system, other configuration files might
           be checked for locale configuration as well, however only as
           fallback.

           /etc/locale.conf can be updated using systemd-localed.service(8).
           localectl(1) may be used to alter the settings in this file during
           runtime from the command line. Use systemd-firstboot(1) to
           customize them on mounted (but not booted) system images.

## [](#OPTIONS)OPTIONS

           The following locale settings may be set using /etc/locale.conf:
           LANG=, LANGUAGE=, LC_CTYPE=, LC_NUMERIC=, LC_TIME=, LC_COLLATE=,
           LC_MONETARY=, LC_MESSAGES=, LC_PAPER=, LC_NAME=, LC_ADDRESS=,
           LC_TELEPHONE=, LC_MEASUREMENT=, LC_IDENTIFICATION=. Note that
           LC_ALL may not be configured in this file. For details about the
           meaning and semantics of these settings, refer to locale(7).

## [](#EXAMPLE)EXAMPLE

           Example 1. German locale with English messages

           /etc/locale.conf:

               # Custom settings

               LANG=de_DE.UTF-8
               LC_MESSAGES=en_US.UTF-8

## [](#SEE_ALSO)SEE ALSO

           systemd(1), locale(7), localectl(1), systemd-localed.service(8),
           systemd-firstboot(1)

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                          LOCALE.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [localectl(1)](../man1/localectl.1.html),  [systemd(1)](../man1/systemd.1.html),  [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [vconsole.conf(5)](../man5/vconsole.conf.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-localed.service(8)](../man8/systemd-localed.service.8.html)

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
