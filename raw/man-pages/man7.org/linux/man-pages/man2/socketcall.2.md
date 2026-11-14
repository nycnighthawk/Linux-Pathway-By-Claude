---
{"title": "socketcall(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/socketcall.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# socketcall(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    socketcall(2)              System Calls Manual              socketcall(2)

## [](#NAME)NAME

           socketcall - socket system calls

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/net.h>        /* Definition of SYS_* constants */
           #include <sys/syscall.h>      /* Definition of SYS_socketcall */
           #include <unistd.h>

           int syscall(SYS_socketcall, int call, unsigned long *args);

           Note: glibc provides no wrapper for socketcall(), necessitating
           the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           socketcall() is a common kernel entry point for the socket system
           calls.  call determines which socket function to invoke.  args
           points to a block containing the actual arguments, which are
           passed through to the appropriate call.

           User programs should call the appropriate functions by their usual
           names.  Only standard library implementors and kernel hackers need
           to know about socketcall().

           call              Man page
           SYS_SOCKET        socket(2)
           SYS_BIND          bind(2)
           SYS_CONNECT       connect(2)
           SYS_LISTEN        listen(2)
           SYS_ACCEPT        accept(2)
           SYS_GETSOCKNAME   getsockname(2)
           SYS_GETPEERNAME   getpeername(2)
           SYS_SOCKETPAIR    socketpair(2)
           SYS_SEND          send(2)
           SYS_RECV          recv(2)
           SYS_SENDTO        sendto(2)
           SYS_RECVFROM      recvfrom(2)
           SYS_SHUTDOWN      shutdown(2)
           SYS_SETSOCKOPT    setsockopt(2)
           SYS_GETSOCKOPT    getsockopt(2)
           SYS_SENDMSG       sendmsg(2)
           SYS_RECVMSG       recvmsg(2)
           SYS_ACCEPT4       accept4(2)
           SYS_RECVMMSG      recvmmsg(2)
           SYS_SENDMMSG      sendmmsg(2)

## [](#VERSIONS)VERSIONS

           On some architectures —for example, x86-64 and ARM— there is no
           socketcall() system call; instead socket(2), accept(2), bind(2),
           and so on really are implemented as separate system calls.

## [](#STANDARDS)STANDARDS

           Linux.

           On x86-32, socketcall() was historically the only entry point for
           the sockets API.  However, starting in Linux 4.3, direct system
           calls are provided on x86-32 for the sockets API.  This
           facilitates the creation of seccomp(2) filters that filter sockets
           system calls (for new user-space binaries that are compiled to use
           the new entry points) and also provides a (very) small performance
           improvement.

## [](#SEE_ALSO)SEE ALSO

           accept(2), bind(2), connect(2), getpeername(2), getsockname(2),
           getsockopt(2), listen(2), recv(2), recvfrom(2), recvmsg(2),
           send(2), sendmsg(2), sendto(2), setsockopt(2), shutdown(2),
           socket(2), socketpair(2)

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

    Linux man-pages 6.19            2026-02-08                  socketcall(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [seccomp_syscall_resolve_name(3)](../man3/seccomp_syscall_resolve_name.3.html)

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
