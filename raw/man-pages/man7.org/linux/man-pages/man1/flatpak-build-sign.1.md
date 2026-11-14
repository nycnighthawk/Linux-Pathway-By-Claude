---
{"title": "flatpak-build-sign(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-build-sign.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-build-sign(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK BUILD-SIGN(1)       flatpak build-sign      FLATPAK BUILD-SIGN(1)

## [](#NAME)NAME

           flatpak-build-sign - Sign an application or runtime

## [](#SYNOPSIS)SYNOPSIS

           flatpak build-sign [OPTION...] LOCATION ID [BRANCH]

## [](#DESCRIPTION)DESCRIPTION

           Signs the commit for a specified application or runtime in a local
           repository.  LOCATION is the location of the repository.  ID is
           the name of the application, or runtime if --runtime is specified.
           If BRANCH is not specified, it is assumed to be "master".

           Applications can also be signed during build-export, but it is
           sometimes useful to add additional signatures later.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           --gpg-sign=KEYID
               Sign the commit with this GPG key. This option can be used
               multiple times.

           --gpg-homedir=PATH
               GPG Homedir to use when looking for keyrings

           --runtime
               Sign a runtime instead of an app.

           --arch=ARCH
               The architecture to use. See flatpak --supported-arches for
               architectures supported by the host.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak build-sign
           --gpg-sign=D8BA6573DDD2418027736F1BC33B315E53C1E9D6 /some/repo
           org.my.App

## [](#SEE_ALSO)SEE ALSO

           ostree(1), flatpak(1), flatpak-build-export(1), flatpak-build(1),

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

    flatpak                                             FLATPAK BUILD-SIGN(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-build-commit-from(1)](../man1/flatpak-build-commit-from.1.html),  [flatpak-build-export(1)](../man1/flatpak-build-export.1.html)

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
