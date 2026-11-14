---
{"title": "systemd-socket-activate(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-socket-activate.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-socket-activate(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-...-ACTIVATE(1)  systemd-socket-activate  SYSTEMD-...-ACTIVATE(1)

## [](#NAME)NAME

           systemd-socket-activate - Test socket activation of daemons

## [](#SYNOPSIS)SYNOPSIS

           systemd-socket-activate [OPTIONS...] COMMAND [ARGS...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-socket-activate may be used to launch a socket-activated
           service program from the command line for testing purposes. It may
           also be used to launch individual instances of the service program
           per connection.

           The daemon to launch and its options should be specified after
           options intended for systemd-socket-activate.

           If the --inetd option is given, the socket file descriptor will be
           used as the standard input and output of the launched process.
           Otherwise, standard input and output will be inherited, and
           sockets will be passed through file descriptors 3 and higher.
           Sockets passed through $LISTEN_FDS to systemd-socket-activate will
           be passed through to the daemon, in the original positions. Other
           sockets specified with --listen= will use consecutive descriptors.
           By default, systemd-socket-activate listens on a stream socket,
           use --datagram and --seqpacket to listen on datagram or sequential
           packet sockets instead (see below).

## [](#OPTIONS)OPTIONS

           -l address, --listen=address
               Listen on this address. Takes a string like "2000" or
               "127.0.0.1:2001".

               Added in version 230.

           -a, --accept
               Launch an instance of the service program for each connection
               and pass the connection socket. May not be combined with
               --now.

               Added in version 230.

           -d, --datagram
               Listen on a datagram socket (SOCK_DGRAM), instead of a stream
               socket (SOCK_STREAM). May not be combined with --seqpacket.

               Added in version 230.

           --seqpacket
               Listen on a sequential packet socket (SOCK_SEQPACKET), instead
               of a stream socket (SOCK_STREAM). May not be combined with
               --datagram.

               Added in version 230.

           --inetd
               Use the inetd protocol for passing file descriptors, i.e. as
               standard input and standard output, instead of the new-style
               protocol for passing file descriptors using $LISTEN_FDS (see
               above).

               Added in version 230.

           -E VAR[=VALUE], --setenv=VAR[=VALUE]
               Add this variable to the environment of the launched process.
               If VAR is followed by "=", assume that it is a variable–value
               pair. Otherwise, obtain the value from the environment of
               systemd-socket-activate itself.

               Added in version 230.

           --fdname=NAME[:NAME...]
               Specify names for the file descriptors passed. This is
               equivalent to setting FileDescriptorName= in socket unit
               files, and enables use of sd_listen_fds_with_names(3).
               Multiple entries may be specifies using separate options or by
               separating names with colons (":") in one option. In case more
               names are given than descriptors, superfluous ones will be
               ignored. In case less names are given than descriptors, the
               remaining file descriptors will be unnamed.

               Added in version 230.

           --now
               Start the service program instantly, instead of waiting for a
               connection on the socket(s). May not be combined with
               --accept.

               Added in version 258.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           $LISTEN_FDS, $LISTEN_PID, $LISTEN_PIDFDID, $LISTEN_FDNAMES
               See sd_listen_fds(3).

               Added in version 230.

           $SYSTEMD_LOG_TARGET, $SYSTEMD_LOG_LEVEL, $SYSTEMD_LOG_TIME,
           $SYSTEMD_LOG_COLOR, $SYSTEMD_LOG_LOCATION
               Same as in systemd(1).

               Added in version 230.

## [](#EXAMPLES)EXAMPLES

           Example 1. Run an echo server on port 2000

               $ systemd-socket-activate -l 2000 --inetd -a cat

           Example 2. Run a socket-activated instance of systemd-journal-
           gatewayd(8)

               $ systemd-socket-activate -l 19531 /usr/lib/systemd/systemd-journal-gatewayd

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.socket(5), systemd.service(5), systemd-run(1),
           sd_listen_fds(3), sd_listen_fds_with_names(3), cat(1)

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

    systemd 262~devel                                 SYSTEMD-...-ACTIVATE(1)

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
