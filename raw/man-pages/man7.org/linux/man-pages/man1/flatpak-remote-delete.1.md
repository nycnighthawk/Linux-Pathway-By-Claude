---
{"title": "flatpak-remote-delete(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-remote-delete.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-remote-delete(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK REMOTE-DELE(1)    flatpak remote-delete    FLATPAK REMOTE-DELE(1)

## [](#NAME)NAME

           flatpak-remote-delete - Delete a remote repository

## [](#SYNOPSIS)SYNOPSIS

           flatpak remote-delete [OPTION...] NAME

## [](#DESCRIPTION)DESCRIPTION

           Removes a remote repository from the flatpak repository
           configuration.  NAME is the name of an existing remote.

           Unless overridden with the --system, --user, or --installation
           options, this command uses either the default system-wide
           installation or the per-user one, depending on which has the
           specified REMOTE.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               Modify the per-user configuration.

           --system
               Modify the default system-wide configuration.

           --installation=NAME
               Modify a system-wide installation specified by NAME among
               those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --force
               Remove remote even if its in use by installed apps or
               runtimes.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak --user remote-delete dried-raisins

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-remote-add(1), flatpak-remote-modify(1),
           flatpak-remotes(1)

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

    flatpak                                            FLATPAK REMOTE-DELE(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-remote-add(1)](../man1/flatpak-remote-add.1.html),  [flatpak-remote-modify(1)](../man1/flatpak-remote-modify.1.html),  [flatpak-remotes(1)](../man1/flatpak-remotes.1.html)

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
