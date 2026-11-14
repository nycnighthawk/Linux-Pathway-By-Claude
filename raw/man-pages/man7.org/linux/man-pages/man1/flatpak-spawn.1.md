---
{"title": "flatpak-spawn(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-spawn.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-spawn(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK SPAWN(1)              flatpak spawn              FLATPAK SPAWN(1)

## [](#NAME)NAME

           flatpak-spawn - Run commands in a sandbox

## [](#SYNOPSIS)SYNOPSIS

           flatpak-spawn [OPTION...] COMMAND [ARGUMENT...]

## [](#DESCRIPTION)DESCRIPTION

           Unlike other flatpak commands, flatpak-spawn is available to
           applications inside the sandbox. It runs COMMAND outside the
           sandbox: either in another sandbox, or on the host.

           When called without --host, flatpak-spawn uses the Flatpak portal
           to create a copy of the sandbox it was called from, optionally
           using tighter permissions and optionally the latest version of the
           app and runtime (see --latest-version).

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -v, --verbose
               Print debug information

           --forward-fd=FD
               Forward a file descriptor

           --clear-env
               Run with a clean environment

           --watch-bus
               Make the spawned command exit when flatpak-spawn itself exits;
               notably, this occurs when its connection to the session bus is
               closed.

           --env=VAR=VALUE
               Set an environment variable

           --latest-version
               Use the latest version of the refs that are used to set up the
               sandbox

           --no-network
               Run without network access

           --sandbox
               Run fully sandboxed. See the documentation for the --sandbox
               option in flatpak-run(1)

               See the --sandbox-expose and --sandbox-expose-ro options for
               selective file access.

           --sandbox-expose=NAME
               Expose read-write access to a file in the sandbox.

               Note that absolute paths or subdirectories are not allowed.
               The files must be in the sandbox subdirectory of the instance
               directory (i.e.  ~/.var/app/$APP_ID/sandbox).

               This option is useful in combination with --sandbox (otherwise
               the instance directory is accessible anyway).

           --sandbox-expose-ro=NAME
               Expose readonly access to a file in the sandbox.

               Note that absolute paths or subdirectories are not allowed.
               The files must be in the sandbox subdirectory of the instance
               directory (i.e.  ~/.var/app/$APP_ID/sandbox).

               This option is useful in combination with --sandbox (otherwise
               the instance directory is accessible anyway).

           --host
               Run the command unsandboxed on the host. This requires access
               to the org.freedesktop.Flatpak D-Bus interface.

           --directory=DIR
               The working directory in which to run the command.

               Note that the given directory must exist in the sandbox or,
               when used in conjunction with --host, on the host.

## [](#EXAMPLES)EXAMPLES

           $ flatpak-spawn ls /var/run

## [](#SEE_ALSO)SEE ALSO

           flatpak(1)

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

    flatpak                                                  FLATPAK SPAWN(1)

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
