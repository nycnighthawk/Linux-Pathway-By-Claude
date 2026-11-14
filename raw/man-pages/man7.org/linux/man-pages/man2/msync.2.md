---
{"title": "msync(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/msync.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# msync(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    msync(2)                   System Calls Manual                   msync(2)

## [](#NAME)NAME

           msync - synchronize a file with a memory map

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/mman.h>

           int msync(size_t length;
                     void addr[length], size_t length, int flags);

## [](#DESCRIPTION)DESCRIPTION

           msync() flushes changes made to the in-core copy of a file that
           was mapped into memory using mmap(2) back to the filesystem.
           Without use of this call, there is no guarantee that changes are
           written back before munmap(2) is called.  To be more precise, the
           part of the file that corresponds to the memory area starting at
           addr and having length length is updated.

           The flags argument should specify exactly one of MS_ASYNC and
           MS_SYNC, and may additionally include the MS_INVALIDATE bit.
           These bits have the following meanings:

           MS_ASYNC
                  Specifies that an update be scheduled, but the call returns
                  immediately.

           MS_SYNC
                  Requests an update and waits for it to complete.

           MS_INVALIDATE
                  Asks to invalidate other mappings of the same file (so that
                  they can be updated with the fresh values just written).

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EBUSY  MS_INVALIDATE was specified in flags, and a memory lock
                  exists for the specified address range.

           EINVAL addr is not a multiple of PAGESIZE; or any bit other than
                  MS_ASYNC | MS_INVALIDATE | MS_SYNC is set in flags; or both
                  MS_SYNC and MS_ASYNC are set in flags.

           ENOMEM The indicated memory (or part of it) was not mapped.

## [](#VERSIONS)VERSIONS

           According to POSIX, either MS_SYNC or MS_ASYNC must be specified
           in flags, and indeed failure to include one of these flags will
           cause msync() to fail on some systems.  However, Linux permits a
           call to msync() that specifies neither of these flags, with
           semantics that are (currently) equivalent to specifying MS_ASYNC.
           (Since Linux 2.6.19, MS_ASYNC is in fact a no-op, since the kernel
           properly tracks dirty pages and flushes them to storage as
           necessary.)  Notwithstanding the Linux behavior, portable, future-
           proof applications should ensure that they specify either MS_SYNC
           or MS_ASYNC in flags.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           SUSv1, POSIX.1-1996.

           This call was introduced in Linux 1.3.21, and then used EFAULT
           instead of ENOMEM.  In Linux 2.4.19, this was changed to the POSIX
           value ENOMEM.

           On POSIX systems on which msync() is available, both
           _POSIX_MAPPED_FILES and _POSIX_SYNCHRONIZED_IO are defined in
           <unistd.h> to a value greater than 0.  (See also sysconf(3).)

## [](#SEE_ALSO)SEE ALSO

           mmap(2)

           B.O. Gallmeister, POSIX.4, O'Reilly, pp. 128–129 and 389–391.

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

    Linux man-pages 6.19            2026-02-11                       msync(2)

------------------------------------------------------------------------

Pages that refer to this page: [madvise(2)](../man2/madvise.2.html),  [mmap2(2)](../man2/mmap2.2.html),  [mmap(2)](../man2/mmap.2.html),  [remap_file_pages(2)](../man2/remap_file_pages.2.html),  [sync_file_range(2)](../man2/sync_file_range.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [nfs(5)](../man5/nfs.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [fanotify(7)](../man7/fanotify.7.html),  [inotify(7)](../man7/inotify.7.html),  [xfs_io(8)](../man8/xfs_io.8.html)

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
