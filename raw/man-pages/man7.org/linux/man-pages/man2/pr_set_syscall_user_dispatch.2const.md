---
{"title": "PR_SET_SYSCALL_USER_DISPATCH(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_set_syscall_user_dispatch.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_SYSCALL_USER_DISPATCH(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_SYSCALL_USER_DISPATCH(2const) PR_SET_SYSCALL_USER_DISPATCH(2const)

## [](#NAME)NAME

           PR_SET_SYSCALL_USER_DISPATCH - set the system-call user dispatch
           mechanism for the calling thread

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_SYSCALL_USER_DISPATCH, long op, ...);

           int prctl(PR_SET_SYSCALL_USER_DISPATCH, PR_SYS_DISPATCH_ON,
                     unsigned long off, unsigned long size, int8_t *switch);
           int prctl(PR_SET_SYSCALL_USER_DISPATCH, PR_SYS_DISPATCH_OFF, 0L, 0L, 0L);

## [](#DESCRIPTION)DESCRIPTION

           Configure the Syscall User Dispatch mechanism for the calling
           thread.  This mechanism allows an application to selectively
           intercept system calls so that they can be handled within the
           application itself.  Interception takes the form of a thread-
           directed SIGSYS signal that is delivered to the thread when it
           makes a system call.  If intercepted, the system call is not
           executed by the kernel.

           PR_SYS_DISPATCH_ON
                  Enable this mechanism.

                  Once enabled, further system calls will be selectively
                  intercepted, depending on a control variable provided by
                  user space.  In this case, off and size respectively
                  identify the offset and size of a single contiguous memory
                  region in the process address space from where system calls
                  are always allowed to be executed, regardless of the
                  control variable.  (Typically, this area would include the
                  area of memory containing the C library.)

                  switch points to a variable that is a fast switch to
                  allow/block system call execution without the overhead of
                  doing another system call to re-configure Syscall User
                  Dispatch.  This control variable can either be set to
                  SYSCALL_DISPATCH_FILTER_BLOCK to block system calls from
                  executing or to SYSCALL_DISPATCH_FILTER_ALLOW to
                  temporarily allow them to be executed.  This value is
                  checked by the kernel on every system call entry, and any
                  unexpected value will raise an uncatchable SIGSYS at that
                  time, killing the application.

                  When a system call is intercepted, the kernel sends a
                  thread-directed SIGSYS signal to the triggering thread.
                  Various fields will be set in the siginfo_t structure (see
                  sigaction(2)) associated with the signal:

                  •  si_signo will contain SIGSYS.

                  •  si_call_addr will show the address of the system call
                     instruction.

                  •  si_syscall and si_arch will indicate which system call
                     was attempted.

                  •  si_code will contain SYS_USER_DISPATCH.

                  •  si_errno will be set to 0.

                  The program counter will be as though the system call
                  happened (i.e., the program counter will not point to the
                  system call instruction).

                  When the signal handler returns to the kernel, the system
                  call completes immediately and returns to the calling
                  thread, without actually being executed.  If necessary
                  (i.e., when emulating the system call on user space.), the
                  signal handler should set the system call return value to a
                  sane value, by modifying the register context stored in the
                  ucontext argument of the signal handler.  See sigaction(2),
                  sigreturn(2), and getcontext(3) for more information.

           PR_SYS_DISPATCH_OFF
                  Syscall User Dispatch is disabled for that thread.

           The setting is not preserved across fork(2), clone(2), or
           execve(2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT switch is an invalid address.

           EINVAL op is PR_SYS_DISPATCH_ON and the memory range specified is
                  outside the address space of the process.

           EINVAL op is invalid.

## [](#STANDARDS)STANDARDS

           Linux.  x86 only.

## [](#HISTORY)HISTORY

           Linux 5.11 (x86).

## [](#SEE_ALSO)SEE ALSO

           prctl(2)

           For more information, see the kernel source file Documentation/
           admin-guide/syscall-user-dispatch.rst

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

    Linux man-pages 6.19            2026-0P2R-_0S8ET_SYSCALL_USER_DISPATCH(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html)

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
