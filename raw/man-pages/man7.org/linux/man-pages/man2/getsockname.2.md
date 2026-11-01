---
{"title": "getsockname(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getsockname.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# getsockname(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getsockname(2)             System Calls Manual             getsockname(2)

## [](#NAME)NAME

           getsockname - get socket name

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>

           int getsockname(int sockfd, struct sockaddr *restrict addr,
                           socklen_t *restrict addrlen);

## [](#DESCRIPTION)DESCRIPTION

           getsockname() returns the current address to which the socket
           sockfd is bound, in the buffer pointed to by addr.  The addrlen
           argument should be initialized to indicate the amount of space (in
           bytes) pointed to by addr.  On return it contains the actual size
           of the socket address.

           The returned address is truncated if the buffer provided is too
           small; in this case, addrlen will return a value greater than was
           supplied to the call.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  The argument sockfd is not a valid file descriptor.

           EFAULT The addr argument points to memory not in a valid part of
                  the process address space.

           EINVAL addrlen is invalid (e.g., is negative).

           ENOBUFS
                  Insufficient resources were available in the system to
                  perform the operation.

           ENOTSOCK
                  The file descriptor sockfd does not refer to a socket.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4, 4.2BSD.

## [](#SEE_ALSO)SEE ALSO

           bind(2), socket(2), getifaddrs(3), ip(7), socket(7), unix(7)

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

    Linux man-pages 6.19            2025-10-29                 getsockname(2)

------------------------------------------------------------------------

Pages that refer to this page: [bind(2)](../man2/bind.2.html),  [connect(2)](../man2/connect.2.html),  [getpeername(2)](../man2/getpeername.2.html),  [socket(2)](../man2/socket.2.html),  [socketcall(2)](../man2/socketcall.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [bindresvport(3)](../man3/bindresvport.3.html),  [getifaddrs(3)](../man3/getifaddrs.3.html),  [getnameinfo(3)](../man3/getnameinfo.3.html),  [if_nameindex(3)](../man3/if_nameindex.3.html),  [io_uring_prep_cmd_getsockname(3)](../man3/io_uring_prep_cmd_getsockname.3.html),  [io_uring_prep_cmd_sock(3)](../man3/io_uring_prep_cmd_sock.3.html),  [sd_is_fifo(3)](../man3/sd_is_fifo.3.html),  [sockaddr(3type)](../man3/sockaddr.3type.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [socket(7)](../man7/socket.7.html),  [unix(7)](../man7/unix.7.html)

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
