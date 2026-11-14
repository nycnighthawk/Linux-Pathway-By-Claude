---
{"title": "socketpair(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/socketpair.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# socketpair(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    socketpair(2)              System Calls Manual              socketpair(2)

## [](#NAME)NAME

           socketpair - create a pair of connected sockets

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>

           int socketpair(int domain, int type, int protocol, int sv[2]);

## [](#DESCRIPTION)DESCRIPTION

           The socketpair() call creates an unnamed pair of connected sockets
           in the specified domain, of the specified type, and using the
           optionally specified protocol.  For further details of these
           arguments, see socket(2).

           The file descriptors used in referencing the new sockets are
           returned in sv[0] and sv[1].  The two sockets are
           indistinguishable.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, errno is
           set to indicate the error, and sv is left unchanged

           On Linux (and other systems), socketpair() does not modify sv on
           failure.  A requirement standardizing this behavior was added in
           POSIX.1-2008 TC2.

## [](#ERRORS)ERRORS

           EAFNOSUPPORT
                  The specified address family is not supported on this
                  machine.

           EFAULT The address sv does not specify a valid part of the process
                  address space.

           EMFILE The per-process limit on the number of open file
                  descriptors has been reached.

           ENFILE The system-wide limit on the total number of open files has
                  been reached.

           EOPNOTSUPP
                  The specified protocol does not support creation of socket
                  pairs.

           EPROTONOSUPPORT
                  The specified protocol is not supported on this machine.

## [](#VERSIONS)VERSIONS

           On Linux, the only supported domains for this call are AF_UNIX (or
           synonymously, AF_LOCAL) and AF_TIPC (since Linux 4.12).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, 4.2BSD.

           It is generally portable to/from non-BSD systems supporting clones
           of the BSD socket layer (including System V variants).

           SOCK_CLOEXEC
           SOCK_NONBLOCK
                  POSIX.1-2024; Linux 2.6.27.  (See socket(2).)

## [](#SEE_ALSO)SEE ALSO

           pipe(2), read(2), socket(2), write(2), socket(7), unix(7)

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

    Linux man-pages 6.19            2025-10-29                  socketpair(2)

------------------------------------------------------------------------

Pages that refer to this page: [pipe(2)](../man2/pipe.2.html),  [socket(2)](../man2/socket.2.html),  [socketcall(2)](../man2/socketcall.2.html),  [SO_PEERSEC(2const)](../man2/SO_PEERSEC.2const.html),  [syscalls(2)](../man2/syscalls.2.html),  [sockaddr(3type)](../man3/sockaddr.3type.html),  [fifo(7)](../man7/fifo.7.html),  [pipe(7)](../man7/pipe.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [socket(7)](../man7/socket.7.html),  [unix(7)](../man7/unix.7.html)

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
