---
{"title": "ustat(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ustat.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ustat(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ustat(2)                   System Calls Manual                   ustat(2)

## [](#NAME)NAME

           ustat - get filesystem statistics

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/types.h>
           #include <unistd.h>    /* libc[45] */
           #include <ustat.h>     /* glibc2 */

           [[deprecated]] int ustat(dev_t dev, struct ustat *ubuf);

## [](#DESCRIPTION)DESCRIPTION

           ustat() returns information about a mounted filesystem.  dev is a
           device number identifying a device containing a mounted
           filesystem.  ubuf is a pointer to a ustat structure that contains
           the following members:

               daddr_t f_tfree;      /* Total free blocks */
               ino_t   f_tinode;     /* Number of free inodes */
               char    f_fname[6];   /* Filsys name */
               char    f_fpack[6];   /* Filsys pack name */

           The last two fields, f_fname and f_fpack, are not implemented and
           will always be filled with null bytes ('\0').

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned and the ustat structure pointed to by
           ubuf will be filled in.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT ubuf points outside of your accessible address space.

           EINVAL dev does not refer to a device containing a mounted
                  filesystem.

           ENOSYS The mounted filesystem referenced by dev does not support
                  this operation, or any version of Linux before Linux
                  1.3.16.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           SVr4.  Removed in glibc 2.28.

           ustat() is deprecated and has been provided only for
           compatibility.  All new programs should use statfs(2) instead.

       HP-UX notes
           The HP-UX version of the ustat structure has an additional field,
           f_blksize, that is unknown elsewhere.  HP-UX warns: For some
           filesystems, the number of free inodes does not change.  Such
           filesystems will return -1 in the field f_tinode.  For some
           filesystems, inodes are dynamically allocated.  Such filesystems
           will return the current number of free inodes.

## [](#SEE_ALSO)SEE ALSO

           stat(2), statfs(2)

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

    Linux man-pages 6.19            2026-02-08                       ustat(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html)

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
