---
{"title": "get_robust_list(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/get_robust_list.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# get_robust_list(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    get_robust_list(2)         System Calls Manual         get_robust_list(2)

## [](#NAME)NAME

           get_robust_list, set_robust_list - get/set list of robust futexes

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>   /* Definition of struct robust_list_head */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_get_robust_list, int pid,
                        struct robust_list_head **head_ptr, size_t *sizep);
           long syscall(SYS_set_robust_list,
                        struct robust_list_head *head, size_t size);

           Note: glibc provides no wrappers for these system calls,
           necessitating the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           These system calls deal with per-thread robust futex lists.  These
           lists are managed in user space: the kernel knows only about the
           location of the head of the list.  A thread can inform the kernel
           of the location of its robust futex list using set_robust_list().
           The address of a thread's robust futex list can be obtained using
           get_robust_list().

           The purpose of the robust futex list is to ensure that if a thread
           accidentally fails to unlock a futex before terminating or calling
           execve(2), another thread that is waiting on that futex is
           notified that the former owner of the futex has died.  This
           notification consists of two pieces: the FUTEX_OWNER_DIED bit is
           set in the futex word, and the kernel performs a futex(2)
           FUTEX_WAKE operation on one of the threads waiting on the futex.

           The get_robust_list() system call returns the head of the robust
           futex list of the thread whose thread ID is specified in pid.  If
           pid is 0, the head of the list for the calling thread is returned.
           The list head is stored in the location pointed to by head_ptr.
           The size of the object pointed to by **head_ptr is stored in
           sizep.

           Permission to employ get_robust_list() is governed by a ptrace
           access mode PTRACE_MODE_READ_REALCREDS check; see ptrace(2).

           The set_robust_list() system call requests the kernel to record
           the head of the list of robust futexes owned by the calling
           thread.  The head argument is the list head to record.  The size
           argument should be sizeof(*head).

## [](#RETURN_VALUE)RETURN VALUE

           The set_robust_list() and get_robust_list() system calls return
           zero when the operation is successful, an error code otherwise.

## [](#ERRORS)ERRORS

           The set_robust_list() system call can fail with the following
           error:

           EINVAL size does not equal sizeof(struct robust_list_head).

           The get_robust_list() system call can fail with the following
           errors:

           EFAULT The head of the robust futex list can't be stored at the
                  location head.

           EPERM  The calling process does not have permission to see the
                  robust futex list of the thread with the thread ID pid, and
                  does not have the CAP_SYS_PTRACE capability.

           ESRCH  No thread with the thread ID pid could be found.

## [](#VERSIONS)VERSIONS

           These system calls were added in Linux 2.6.17.

## [](#NOTES)NOTES

           These system calls are not needed by normal applications.

           A thread can have only one robust futex list; therefore
           applications that wish to use this functionality should use the
           robust mutexes provided by glibc.

           In the initial implementation, a thread waiting on a futex was
           notified that the owner had died only if the owner terminated.
           Starting with Linux 2.6.28, notification was extended to include
           the case where the owner performs an execve(2).

           The thread IDs mentioned in the main text are kernel thread IDs of
           the kind returned by clone(2) and gettid(2).

## [](#SEE_ALSO)SEE ALSO

           futex(2), pthread_mutexattr_setrobust(3)

           Documentation/robust-futexes.rst and
           Documentation/robust-futex-ABI.rst in the Linux kernel source tree

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

    Linux man-pages 6.19            2026-02-08             get_robust_list(2)

------------------------------------------------------------------------

Pages that refer to this page: [execve(2)](../man2/execve.2.html),  [futex(2)](../man2/futex.2.html),  [gettid(2)](../man2/gettid.2.html),  [ptrace(2)](../man2/ptrace.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [exit(3)](../man3/exit.3.html),  [pthread_mutexattr_setrobust(3)](../man3/pthread_mutexattr_setrobust.3.html),  [capabilities(7)](../man7/capabilities.7.html),  [futex(7)](../man7/futex.7.html)

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
