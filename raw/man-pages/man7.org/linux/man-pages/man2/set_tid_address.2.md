---
{"title": "set_tid_address(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/set_tid_address.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# set_tid_address(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    set_tid_address(2)         System Calls Manual         set_tid_address(2)

## [](#NAME)NAME

           set_tid_address - set pointer to thread ID

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           pid_t syscall(SYS_set_tid_address, int *tidptr);

           Note: glibc provides no wrapper for set_tid_address(),
           necessitating the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           For each thread, the kernel maintains two attributes (addresses)
           called set_child_tid and clear_child_tid.  These two attributes
           contain the value NULL by default.

           set_child_tid
                  If a thread is started using clone(2) with the
                  CLONE_CHILD_SETTID flag, set_child_tid is set to the value
                  passed in the ctid argument of that system call.

                  When set_child_tid is set, the very first thing the new
                  thread does is to write its thread ID at this address.

           clear_child_tid
                  If a thread is started using clone(2) with the
                  CLONE_CHILD_CLEARTID flag, clear_child_tid is set to the
                  value passed in the ctid argument of that system call.

           The system call set_tid_address() sets the clear_child_tid value
           for the calling thread to tidptr.

           When a thread whose clear_child_tid is not NULL terminates, then,
           if the thread is sharing memory with other threads, then 0 is
           written at the address specified in clear_child_tid and the kernel
           performs the following operation:

               futex(clear_child_tid, FUTEX_WAKE, 1, NULL, NULL, 0);

           The effect of this operation is to wake a single thread that is
           performing a futex wait on the memory location.  Errors from the
           futex wake operation are ignored.

## [](#RETURN_VALUE)RETURN VALUE

           set_tid_address() always returns the caller's thread ID.

## [](#ERRORS)ERRORS

           set_tid_address() always succeeds.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.5.48.

           Details as given here are valid since Linux 2.5.49.

## [](#SEE_ALSO)SEE ALSO

           clone(2), futex(2), gettid(2)

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

    Linux man-pages 6.19            2026-02-08             set_tid_address(2)

------------------------------------------------------------------------

Pages that refer to this page: [clone(2)](../man2/clone.2.html),  [PR_GET_TID_ADDRESS(2const)](../man2/PR_GET_TID_ADDRESS.2const.html),  [syscalls(2)](../man2/syscalls.2.html),  [futex(7)](../man7/futex.7.html)

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
