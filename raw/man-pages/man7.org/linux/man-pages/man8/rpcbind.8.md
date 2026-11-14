---
{"title": "rpcbind(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpcbind.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpcbind(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [LINUX PORT](#LINUX_PORT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPCBIND(8)                System Manager's Manual              RPCBIND(8)

## [](#NAME)NAME

           rpcbind — universal addresses to RPC program number mapper

## [](#SYNOPSIS)SYNOPSIS

           rpcbind [-adfhilsvw]

## [](#DESCRIPTION)DESCRIPTION

           The rpcbind utility is a server that converts RPC program numbers
           into universal addresses.  It must be running on the host to be
           able to make RPC calls on a server on that machine.

           When an RPC service is started, it tells rpcbind the address at
           which it is listening, and the RPC program numbers it is prepared
           to serve.  When a client wishes to make an RPC call to a given
           program number, it first contacts rpcbind on the server machine to
           determine the address where RPC requests should be sent.

           The rpcbind utility should be started before any other RPC
           service.  Normally, standard RPC servers are started by port
           monitors, so rpcbind must be started before port monitors are
           invoked.

           When rpcbind is started, it checks that certain name-to-address
           translation-calls function correctly.  If they fail, the network
           configuration databases may be corrupt.  Since RPC services cannot
           function correctly in this situation, rpcbind reports the
           condition and terminates.

           The rpcbind utility can only be started by the super-user.

## [](#OPTIONS)OPTIONS

           -a      When debugging (-d), do an abort on errors.

           -d      Run in debug mode.  In this mode, rpcbind will log
                   additional information during operation, and will abort on
                   certain errors if -a is also specified.  With this option,
                   the name-to-address translation consistency checks are
                   shown in detail.

           -f      Do not fork and become a background process.

           -h      Specify specific IP addresses to bind to for UDP requests.
                   This option may be specified multiple times and can be
                   used to restrict the interfaces rpcbind will respond to.
                   When specifying IP addresses with -h, rpcbind will
                   automatically add 127.0.0.1 and if IPv6 is enabled, ::1 to
                   the list.  If no -h option is specified, rpcbind will bind
                   to INADDR_ANY, which could lead to problems on a multi-
                   homed host due to rpcbind returning a UDP packet from a
                   different IP address than it was sent to.  Note that when
                   rpcbind is controlled via systemd's socket activation, the
                   -h option is ignored. In this case, you need to edit the
                   ListenStream and ListenDgram definitions in
                   /usr/lib/systemd/system/rpcbind.socket instead.

           -i      “Insecure” mode.  Allow calls to SET and UNSET from any
                   host.  Normally rpcbind accepts these requests only from
                   the loopback interface for security reasons.  This change
                   is necessary for programs that were compiled with earlier
                   versions of the rpc library and do not make those requests
                   using the loopback interface.

           -l      Turn on libwrap connection logging.

           -s      Cause rpcbind to change to the user daemon as soon as
                   possible.  This causes rpcbind to use non-privileged ports
                   for outgoing connections, preventing non-privileged
                   clients from using rpcbind to connect to services from a
                   privileged port.

           -v      Print rpcbind version and builtin configuration and exit.

           -w      Cause rpcbind to do a "warm start" by read a state file
                   when rpcbind starts up. The state file is created when
                   rpcbind terminates.

## [](#FILES)FILES

           The rpcbind utility tries to load configuration file in following
           order:

           /etc/rpcbind.conf
           /etc/default/rpcbind
           /etc/sysconfig/rpcbind

## [](#NOTES)NOTES

           All RPC servers must be restarted if rpcbind is restarted.

## [](#SEE_ALSO)SEE ALSO

           rpcinfo(8)

## [](#LINUX_PORT)LINUX PORT

## [](#COLOPHON)COLOPHON

           This page is part of the rpcbind (convert RPC numbers to universal
           addresses) project.  Information about the project can be found at
           http://sourceforge.net/projects/rpcbind/.  If you have a bug
           report for this manual page, see
           ⟨http://sourceforge.net/p/rpcbind/bugs/?source=navbar⟩.  This page
           was obtained from the project's upstream Git repository
           ⟨git://linux-nfs.org/~steved/rpcbind⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    GNU                         September 14, 1992                 RPCBIND(8)

------------------------------------------------------------------------

Pages that refer to this page: [statd(8)](../man8/statd.8.html)

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
