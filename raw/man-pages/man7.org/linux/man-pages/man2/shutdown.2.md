---
{"title": "shutdown(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/shutdown.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# shutdown(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    shutdown(2)                System Calls Manual                shutdown(2)

## [](#NAME)NAME

           shutdown - shut down part of a full-duplex connection

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>

           int shutdown(int sockfd, int how);

## [](#DESCRIPTION)DESCRIPTION

           The shutdown() call causes all or part of a full-duplex connection
           on the socket associated with sockfd to be shut down.  If how is
           SHUT_RD, further receptions will be disallowed.  If how is
           SHUT_WR, further transmissions will be disallowed.  If how is
           SHUT_RDWR, further receptions and transmissions will be
           disallowed.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  sockfd is not a valid file descriptor.

           EINVAL An invalid value was specified in how (but see BUGS).

           ENOTCONN
                  The specified socket is not connected.

           ENOTSOCK
                  The file descriptor sockfd does not refer to a socket.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, 4.4BSD (first appeared in 4.2BSD).

## [](#NOTES)NOTES

           The constants SHUT_RD, SHUT_WR, SHUT_RDWR have the value 0, 1, 2,
           respectively, and are defined in <sys/socket.h> since
           glibc-2.1.91.

## [](#BUGS)BUGS

           Checks for the validity of how are done in domain-specific code,
           and before Linux 3.7 not all domains performed these checks.  Most
           notably, UNIX domain sockets simply ignored invalid values.  This
           problem was fixed for UNIX domain sockets in Linux 3.7.

## [](#SEE_ALSO)SEE ALSO

           close(2), connect(2), socket(2), socket(7)

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

    Linux man-pages 6.19            2025-10-29                    shutdown(2)

------------------------------------------------------------------------

Pages that refer to this page: [close(2)](../man2/close.2.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [recv(2)](../man2/recv.2.html),  [send(2)](../man2/send.2.html),  [socket(2)](../man2/socket.2.html),  [socketcall(2)](../man2/socketcall.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [io_uring_prep_shutdown(3)](../man3/io_uring_prep_shutdown.3.html),  [sd_listen_fds(3)](../man3/sd_listen_fds.3.html),  [sd_varlink_reply_and_upgrade(3)](../man3/sd_varlink_reply_and_upgrade.3.html),  [systemd.socket(5)](../man5/systemd.socket.5.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [sock_diag(7)](../man7/sock_diag.7.html),  [socket(7)](../man7/socket.7.html),  [lsof(8)](../man8/lsof.8.html)

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
