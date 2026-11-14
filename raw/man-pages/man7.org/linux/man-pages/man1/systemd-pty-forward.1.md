---
{"title": "systemd-pty-forward(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-pty-forward.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-pty-forward(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-PTY-FORWARD(1)     systemd-pty-forward     SYSTEMD-PTY-FORWARD(1)

## [](#NAME)NAME

           systemd-pty-forward - Run a command with a custom terminal
           background color or title

## [](#SYNOPSIS)SYNOPSIS

           systemd-pty-forward [OPTIONS...] {COMMAND}

## [](#DESCRIPTION)DESCRIPTION

           systemd-pty-forward can be used to run a command with a custom
           terminal background color or title.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --background=COLOR
               Change the terminal background color to the specified ANSI
               color as long as the command runs. The color specified should
               be an ANSI X3.64 SGR background color, i.e. strings such as
               "40", "41", ..., "47", "48;2;...", "48;5;...". See ANSI Escape
               Code (Wikipedia)[1] for details.

               Example: "--background=44" for a blue background.

               Added in version 258.

           --title=TITLE
               Change the terminal title to the specified string as long as
               the command runs.

               Added in version 258.

           --quiet, -q
               Suppresses additional informational output while running.

               Added in version 258.

           --read-only
               Do not accept any user input on standard input.

               Added in version 258.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#NOTES)NOTES

            1. ANSI Escape Code (Wikipedia)
               https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters

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

    systemd 262~devel                                  SYSTEMD-PTY-FORWARD(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
