---
{"title": "sync(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sync.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sync(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sync(2)                    System Calls Manual                    sync(2)

## [](#NAME)NAME

           sync, syncfs - commit filesystem caches to disk

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           void sync(void);

           int syncfs(int fd);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           sync():
               _XOPEN_SOURCE >= 500
                   || /* Since glibc 2.19: */ _DEFAULT_SOURCE
                   || /* glibc <= 2.19: */ _BSD_SOURCE

           syncfs():
               _GNU_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           sync() causes all pending modifications to filesystem metadata and
           cached file data to be written to the underlying filesystems.

           syncfs() is like sync(), but synchronizes just the filesystem
           containing file referred to by the open file descriptor fd.

## [](#RETURN_VALUE)RETURN VALUE

           syncfs() returns 0 on success; on error, it returns -1 and sets
           errno to indicate the error.

## [](#ERRORS)ERRORS

           sync() is always successful.

           syncfs() can fail for at least the following reasons:

           EBADF  fd is not a valid file descriptor.

           EIO    An error occurred during synchronization.  This error may
                  relate to data written to any file on the filesystem, or on
                  metadata related to the filesystem itself.

           ENOSPC Disk space was exhausted while synchronizing.

           ENOSPC
           EDQUOT Data was written to a file on NFS or another filesystem
                  which does not allocate space at the time of a write(2)
                  system call, and some previous write failed due to
                  insufficient storage space.

## [](#VERSIONS)VERSIONS

           According to the standard specification (i.e., POSIX.1), sync()
           schedules the writes, but may return before the actual writing is
           done.  However Linux waits for I/O completions, and thus sync() or
           syncfs() provide the same guarantees as fsync() called on every
           file in the system or filesystem respectively.

## [](#STANDARDS)STANDARDS

           sync() POSIX.1-2024.

           syncfs()
                  Linux.

## [](#HISTORY)HISTORY

           sync() POSIX.1-2001, SVr4, 4.3BSD.

           syncfs()
                  Linux 2.6.39, glibc 2.14.

           Since glibc 2.2.2, the Linux prototype for sync() is as listed
           above, following the various standards.  In glibc 2.2.1 and
           earlier, it was "int sync(void)", and sync() always returned 0.

           In mainline kernel versions prior to Linux 5.8, syncfs() will fail
           only when passed a bad file descriptor (EBADF).  Since Linux 5.8,
           syncfs() will also report an error if one or more inodes failed to
           be written back since the last syncfs() call.

## [](#BUGS)BUGS

           Before Linux 1.3.20, Linux did not wait for I/O to complete before
           returning.

## [](#SEE_ALSO)SEE ALSO

           sync(1), fdatasync(2), fsync(2)

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

    Linux man-pages 6.19            2026-02-08                        sync(2)

------------------------------------------------------------------------

Pages that refer to this page: [pv(1)](../man1/pv.1.html),  [sync(1)](../man1/sync.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [bdflush(2)](../man2/bdflush.2.html),  [fsync(2)](../man2/fsync.2.html),  [mount(2)](../man2/mount.2.html),  [reboot(2)](../man2/reboot.2.html),  [sync_file_range(2)](../man2/sync_file_range.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [fclose(3)](../man3/fclose.3.html),  [fflush(3)](../man3/fflush.3.html),  [nfs(5)](../man5/nfs.5.html),  [ctrlaltdel(8)](../man8/ctrlaltdel.8.html),  [fdisk(8)](../man8/fdisk.8.html),  [fsck.minix(8)](../man8/fsck.minix.8.html),  [mke2fs(8)](../man8/mke2fs.8.html),  [mount(8)](../man8/mount.8.html),  [xfs_io(8)](../man8/xfs_io.8.html),  [xfs_quota(8)](../man8/xfs_quota.8.html)

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
