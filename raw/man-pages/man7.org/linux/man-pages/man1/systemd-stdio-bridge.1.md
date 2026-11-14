---
{"title": "systemd-stdio-bridge(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-stdio-bridge.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-stdio-bridge(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-STDIO-BRIDGE(1)    systemd-stdio-bridge   SYSTEMD-STDIO-BRIDGE(1)

## [](#NAME)NAME

           systemd-stdio-bridge - D-Bus proxy

## [](#SYNOPSIS)SYNOPSIS

           systemd-stdio-bridge [OPTIONS...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-stdio-bridge implements a proxy between STDIN/STDOUT and a
           D-Bus bus. It expects to receive an open connection via
           STDIN/STDOUT when started, and will create a new connection to the
           specified bus. It will then forward messages between the two
           connections. This program is suitable for socket activation: the
           first connection may be a pipe or a socket and must be passed as
           either standard input, or as an open file descriptor according to
           the protocol described in sd_listen_fds(3). The second connection
           will be made by default to the local system bus, but this can be
           influenced by the --user, --system, --machine=, and --bus-path=
           options described below.

           sd-bus(3) uses systemd-stdio-bridge to forward D-Bus connections
           over ssh(1), or to connect to the bus of a different user, see
           sd_bus_set_address(3).

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --user
               Talk to the service manager of the calling user, rather than
               the service manager of the system.

           --system
               Talk to the service manager of the system. This is the implied
               default.

           -M, --machine=
               Execute operation on a local container. Specify a container
               name to connect to, optionally prefixed by a user name to
               connect as and a separating "@" character. If the special
               string ".host" is used in place of the container name, a
               connection to the local system is made (which is useful to
               connect to a specific user's user bus: "--user
               --machine=lennart@.host"). If the "@" syntax is not used, the
               connection is made as root user. If the "@" syntax is used
               either the left hand side or the right hand side may be
               omitted (but not both) in which case the local user name and
               ".host" are implied.

           -p PATH, --bus-path=PATH
               Path to the bus address. Default:
               "unix:path=/run/dbus/system_bus_socket"

               Added in version 251.

           -q, --quiet
               Suppresses error logging on failure.

               Added in version 259.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           dbus-daemon(1), dbus-broker(1), D-Bus[1], systemd(1)

## [](#NOTES)NOTES

            1. D-Bus
               https://www.freedesktop.org/wiki/Software/dbus

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

    systemd 262~devel                                 SYSTEMD-STDIO-BRIDGE(1)

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
