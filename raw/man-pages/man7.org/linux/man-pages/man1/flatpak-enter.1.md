---
{"title": "flatpak-enter(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-enter.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-enter(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK ENTER(1)              flatpak enter              FLATPAK ENTER(1)

## [](#NAME)NAME

           flatpak-enter - Enter an application or runtime's sandbox

## [](#SYNOPSIS)SYNOPSIS

           flatpak enter [OPTION...] INSTANCE COMMAND [ARG...]

## [](#DESCRIPTION)DESCRIPTION

           Enter a running sandbox.

           INSTANCE must be either the pid of a process running in a flatpak
           sandbox, or the ID of a running application, or the instance ID of
           a running sandbox. You can use flatpak ps to find the instance IDs
           of running flatpaks.

           COMMAND is the command to run in the sandbox. Extra arguments are
           passed on to the command.

           This creates a new process within the running sandbox, with the
           same environment. This is useful when you want to debug a problem
           with a running application.

           This command works as a regular user if the system support
           unprivileged user namespace. If that is not available you need to
           run run it like: sudo -E flatpak enter.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak enter 15345 sh

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-run(1) flatpak-ps(1)

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

    flatpak                                                  FLATPAK ENTER(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-run(1)](../man1/flatpak-run.1.html)

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
