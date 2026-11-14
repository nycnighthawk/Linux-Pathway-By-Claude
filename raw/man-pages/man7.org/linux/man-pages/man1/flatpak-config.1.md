---
{"title": "flatpak-config(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-config.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-config(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK CONFIG(1)             flatpak config            FLATPAK CONFIG(1)

## [](#NAME)NAME

           flatpak-config - Manage configuration

## [](#SYNOPSIS)SYNOPSIS

           flatpak config [OPTION...]

           flatpak config [OPTION...] --set KEY VALUE

           flatpak config [OPTION...] --unset|--get KEY

## [](#DESCRIPTION)DESCRIPTION

           The flatpak config command shows or modifies the configuration of
           a flatpak installation. The following keys are supported:

           languages
               The languages that are included when installing Locale
               extensions. The value is a semicolon-separated list of
               two-letter language codes, or one of the special values * or
               *all*. If this key is unset, flatpak defaults to including the
               extra-languages key and the current locale.

           extra-languages
               This key is used when languages is not set, and it defines
               extra locale extensions on top of the system configured
               languages. The value is a semicolon-separated list of locale
               identifiers (language, optional locale, optional codeset,
               optional modifier) as documented by setlocale(3) (for example,
               en;en_DK;zh_HK.big5hkscs;uz_UZ.utf8@cyrillic).

           report-os-info
               If this key is set to false or the no-report-os-info file
               exists at FLATPAK_CONFIG_DIR Flatpak will not report the OS
               name, version, and architecture from /etc/os-release to the
               Flatpak remote via the Flatpak-Os-Info HTTP header when
               pulling objects. The default value of the key if unset is
               true.

           For configuration of individual remotes, see
           flatpak-remote-modify(1). For configuration of individual
           applications, see flatpak-override(1).

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           --list
               Print all keys and their values.

           --set
               Set key KEY to VALUE.

           --unset
               Unset key KEY.

           --get
               Print value of KEY.

           -u, --user
               Configure per-user installation.

           --system
               Configure system-wide installation.

           --installation=NAME
               Configure the system-wide installation specified by NAME among
               those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak config --set languages "sv;en;fi"

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-remote-modify(1), flatpak-override(1)

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

    flatpak                                                 FLATPAK CONFIG(1)

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
