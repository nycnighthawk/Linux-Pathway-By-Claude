---
{"title": "sysfs(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sysfs.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysfs(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sysfs(2)                   System Calls Manual                   sysfs(2)

## [](#NAME)NAME

           sysfs - get filesystem type information

## [](#SYNOPSIS)SYNOPSIS

           [[deprecated]] int sysfs(int option, const char *fsname);
           [[deprecated]] int sysfs(int option, unsigned int fs_index, char *buf);
           [[deprecated]] int sysfs(int option);

## [](#DESCRIPTION)DESCRIPTION

           Note: if you are looking for information about the sysfs
           filesystem that is normally mounted at /sys, see sysfs(5).

           The (obsolete) sysfs() system call returns information about the
           filesystem types currently present in the kernel.  The specific
           form of the sysfs() call and the information returned depends on
           the option in effect:

           1  Translate the filesystem identifier string fsname into a
              filesystem type index.

           2  Translate the filesystem type index fs_index into a null-
              terminated filesystem identifier string.  This string will be
              written to the buffer pointed to by buf.  Make sure that buf
              has enough space to accept the string.

           3  Return the total number of filesystem types currently present
              in the kernel.

           The numbering of the filesystem type indexes begins with zero.

## [](#RETURN_VALUE)RETURN VALUE

           On success, sysfs() returns the filesystem index for option 1,
           zero for option 2, and the number of currently configured
           filesystems for option 3.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Either fsname or buf is outside your accessible address
                  space.

           EINVAL fsname is not a valid filesystem type identifier; fs_index
                  is out-of-bounds; option is invalid.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           SVr4.

           This System-V derived system call is obsolete; don't use it.  On
           systems with /proc, the same information can be obtained via
           /proc; use that interface instead.

## [](#BUGS)BUGS

           There is no libc or glibc support.  There is no way to guess how
           large buf should be.

## [](#SEE_ALSO)SEE ALSO

           proc(5), sysfs(5)

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

    Linux man-pages 6.19            2026-02-08                       sysfs(2)

------------------------------------------------------------------------

Pages that refer to this page: [statfs(2)](../man2/statfs.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [filesystems(5)](../man5/filesystems.5.html)

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
