---
{"title": "listen(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/listen.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# listen(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    listen(2)                  System Calls Manual                  listen(2)

## [](#NAME)NAME

           listen - listen for connections on a socket

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>

           int listen(int sockfd, int backlog);

## [](#DESCRIPTION)DESCRIPTION

           listen() marks the socket referred to by sockfd as a passive
           socket, that is, as a socket that will be used to accept incoming
           connection requests using accept(2).

           The sockfd argument is a file descriptor that refers to a socket
           of type SOCK_STREAM or SOCK_SEQPACKET.

           The backlog argument defines the maximum length to which the queue
           of pending connections for sockfd may grow.  If a connection
           request arrives when the queue is full, the client may receive an
           error with an indication of ECONNREFUSED or, if the underlying
           protocol supports retransmission, the request may be ignored so
           that a later reattempt at connection succeeds.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EADDRINUSE
                  Another socket is already listening on the same port.

           EADDRINUSE
                  (Internet domain sockets) The socket referred to by sockfd
                  had not previously been bound to an address and, upon
                  attempting to bind it to an ephemeral port, it was
                  determined that all port numbers in the ephemeral port
                  range are currently in use.  See the discussion of
                  /proc/sys/net/ipv4/ip_local_port_range in ip(7).

           EBADF  The argument sockfd is not a valid file descriptor.

           ENOTSOCK
                  The file descriptor sockfd does not refer to a socket.

           EOPNOTSUPP
                  The socket is not of a type that supports the listen()
                  operation.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           4.2BSD, POSIX.1-2001.

## [](#NOTES)NOTES

           To accept connections, the following steps are performed:

               (1)  A socket is created with socket(2).

               (2)  The socket is bound to a local address using bind(2), so
                    that other sockets may be connect(2)ed to it.

               (3)  A willingness to accept incoming connections and a queue
                    limit for incoming connections are specified with
                    listen().

               (4)  Connections are accepted with accept(2).

           The behavior of the backlog argument on TCP sockets changed with
           Linux 2.2.  Now it specifies the queue length for completely
           established sockets waiting to be accepted, instead of the number
           of incomplete connection requests.  The maximum length of the
           queue for incomplete sockets can be set using
           /proc/sys/net/ipv4/tcp_max_syn_backlog.  When syncookies are
           enabled there is no logical maximum length and this setting is
           ignored.  See tcp(7) for more information.

           If the backlog argument is greater than the value in
           /proc/sys/net/core/somaxconn, then it is silently capped to that
           value.  Since Linux 5.4, the default in this file is 4096; in
           earlier kernels, the default value is 128.  Before Linux 2.4.25,
           this limit was a hard coded value, SOMAXCONN, with the value 128.

## [](#EXAMPLES)EXAMPLES

           See bind(2).

## [](#SEE_ALSO)SEE ALSO

           accept(2), bind(2), connect(2), socket(2), socket(7)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-11                      listen(2)

------------------------------------------------------------------------

Pages that refer to this page: [accept(2)](../man2/accept.2.html),  [bind(2)](../man2/bind.2.html),  [connect(2)](../man2/connect.2.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [socket(2)](../man2/socket.2.html),  [socketcall(2)](../man2/socketcall.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [io_uring_prep_listen(3)](../man3/io_uring_prep_listen.3.html),  [proc_sys_net(5)](../man5/proc_sys_net.5.html),  [proc_sys_net_ipv4(5)](../man5/proc_sys_net_ipv4.5.html),  [services(5)](../man5/services.5.html),  [systemd.socket(5)](../man5/systemd.socket.5.html),  [epoll(7)](../man7/epoll.7.html),  [ip(7)](../man7/ip.7.html),  [sctp(7)](../man7/sctp.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [sock_diag(7)](../man7/sock_diag.7.html),  [socket(7)](../man7/socket.7.html),  [tcp(7)](../man7/tcp.7.html),  [unix(7)](../man7/unix.7.html),  [vsock(7)](../man7/vsock.7.html)

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
