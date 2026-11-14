---
{"title": "flatpak-make-current(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-make-current.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-make-current(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK MAKE-CURREN(1)     flatpak make-current    FLATPAK MAKE-CURREN(1)

## [](#NAME)NAME

           flatpak-make-current - Make a specific version of an app current

## [](#SYNOPSIS)SYNOPSIS

           flatpak make-current [OPTION...] APP BRANCH

## [](#DESCRIPTION)DESCRIPTION

           Makes a particular branch of an application current. Only the
           current branch of an app has its exported files (such as desktop
           files and icons) made visible to the host.

           When a new branch is installed it will automatically be made
           current, so this command is often not needed.

           Unless overridden with the --user or --installation options, this
           command changes the default system-wide installation.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               Update a per-user installation.

           --system
               Update the default system-wide installation.

           --installation=NAME
               Updates a system-wide installation specified by NAME among
               those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --arch=ARCH
               The architecture to make current for. See flatpak
               --supported-arches for architectures supported by the host.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak --user make-current org.gnome.gedit 3.14

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-install(1), flatpak-list(1)

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

    flatpak                                            FLATPAK MAKE-CURREN(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-install(1)](../man1/flatpak-install.1.html),  [flatpak-run(1)](../man1/flatpak-run.1.html)

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
