---
{"title": "process_madvise(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/process_madvise.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# process_madvise(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    process_madvise(2)         System Calls Manual         process_madvise(2)

## [](#NAME)NAME

           process_madvise - give advice about use of memory to a process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/mman.h>

           ssize_t process_madvise(size_t n;
                                   int pidfd, const struct iovec iovec[n],
                                   size_t n, int advice, unsigned int flags);

## [](#DESCRIPTION)DESCRIPTION

           The process_madvise() system call is used to give advice or
           directions to the kernel about the address ranges of another
           process or of the calling process.  It provides the advice for the
           address ranges described by iovec and n.  The goal of such advice
           is to improve system or application performance.

           The pidfd argument is a PID file descriptor (see pidfd_open(2))
           that specifies the process to which the advice is to be applied.

           The pointer iovec points to an array of iovec structures,
           described in iovec(3type).

           n specifies the number of elements in the array of iovec
           structures.  This value must be less than or equal to IOV_MAX
           (defined in <limits.h> or accessible via the call
           sysconf(_SC_IOV_MAX)).

           If manipulating another process, or before Linux 6.13, the advice
           argument is one of the following values:

           MADV_COLD
                  See madvise(2).

           MADV_COLLAPSE
                  See madvise(2).

           MADV_PAGEOUT
                  See madvise(2).

           MADV_WILLNEED
                  See madvise(2).

           Since Linux 6.13, when manipulating the calling process, any
           advice flag is permitted.

           The flags argument is reserved for future use; currently, this
           argument must be specified as 0.

           The n and iovec arguments are checked before applying any advice.
           If n is too big, or iovec is invalid, then an error will be
           returned immediately and no advice will be applied.

           The advice might be applied to only a part of iovec if one of its
           elements points to an invalid memory region in the remote process.
           No further elements will be processed beyond that point.  (See the
           discussion regarding partial advice in RETURN VALUE.)

           Since Linux 5.12, permission to apply advice to another process is
           governed by ptrace access mode PTRACE_MODE_READ_FSCREDS check (see
           ptrace(2)); in addition, because of the performance implications
           of applying the advice, the caller must have the CAP_SYS_NICE
           capability (see capabilities(7)).

## [](#RETURN_VALUE)RETURN VALUE

           On success, process_madvise() returns the number of bytes advised.
           This return value may be less than the total number of requested
           bytes, if an error occurred after some iovec elements were already
           processed.  The caller should check the return value to determine
           whether a partial advice occurred.

           On error, -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  pidfd is not a valid PID file descriptor.

           EFAULT The memory described by iovec is outside the accessible
                  address space of the process referred to by pidfd.

           EINVAL flags is not 0.

           EINVAL The sum of the iov_len values of iovec overflows a ssize_t
                  value.

           EINVAL n is too large.

           ENOMEM Could not allocate memory for internal copies of the iovec
                  structures.

           EPERM  The caller does not have permission to access the address
                  space of the process pidfd.

           ESRCH  The target process does not exist (i.e., it has terminated
                  and been waited on).

           See madvise(2) for advice-specific errors.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 5.10, glibc 2.36.

           Support for this system call is optional, depending on the setting
           of the CONFIG_ADVISE_SYSCALLS configuration option.

           When this system call first appeared in Linux 5.10, permission to
           apply advice to another process was entirely governed by ptrace
           access mode PTRACE_MODE_ATTACH_FSCREDS check (see ptrace(2)).
           This requirement was relaxed in Linux 5.12 so that the caller
           didn't require full control over the target process.

## [](#SEE_ALSO)SEE ALSO

           madvise(2), pidfd_open(2), process_vm_readv(2),
           process_vm_write(2)

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

    Linux man-pages 6.19            2026-02-22             process_madvise(2)

------------------------------------------------------------------------

Pages that refer to this page: [madvise(2)](../man2/madvise.2.html),  [pidfd_open(2)](../man2/pidfd_open.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [iovec(3type)](../man3/iovec.3type.html)

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
