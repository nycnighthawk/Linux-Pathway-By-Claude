---
{"title": "readdir(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/readdir.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# readdir(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    readdir(2)                 System Calls Manual                 readdir(2)

## [](#NAME)NAME

           readdir - read directory entry

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_readdir, unsigned int fd,
                       struct old_linux_dirent *dirp, unsigned int count);

           Note: There is no definition of struct old_linux_dirent; see
           VERSIONS.

## [](#DESCRIPTION)DESCRIPTION

           This is not the function you are interested in.  Look at
           readdir(3) for the POSIX conforming C library interface.  This
           page documents the bare kernel system call interface, which is
           superseded by getdents(2).

           readdir() reads one old_linux_dirent structure from the directory
           referred to by the file descriptor fd into the buffer pointed to
           by dirp.  The argument count is ignored; at most one
           old_linux_dirent structure is read.

           The old_linux_dirent structure is declared (privately in Linux
           kernel file fs/readdir.c) as follows:

               struct old_linux_dirent {
                   unsigned long d_ino;     /* inode number */
                   unsigned long d_offset;  /* offset to this old_linux_dirent */
                   unsigned short d_namlen; /* length of this d_name */
                   char  d_name[1];         /* filename (null-terminated) */
               }

           d_ino is an inode number.  d_offset is the distance from the start
           of the directory to this old_linux_dirent.  d_reclen is the size
           of d_name, not counting the terminating null byte ('\0').  d_name
           is a null-terminated filename.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 1 is returned.  On end of directory, 0 is returned.
           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  Invalid file descriptor fd.

           EFAULT Argument points outside the calling process's address
                  space.

           EINVAL Result buffer is too small.

           ENOENT No such directory.

           ENOTDIR
                  File descriptor does not refer to a directory.

## [](#VERSIONS)VERSIONS

           You will need to define the old_linux_dirent structure yourself.
           However, probably you should use readdir(3) instead.

           This system call does not exist on x86-64.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#SEE_ALSO)SEE ALSO

           getdents(2), readdir(3)

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

    Linux man-pages 6.19            2026-02-08                     readdir(2)

------------------------------------------------------------------------

Pages that refer to this page: [fanotify_mark(2)](../man2/fanotify_mark.2.html),  [getdents(2)](../man2/getdents.2.html),  [read(2)](../man2/read.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [seekdir(3)](../man3/seekdir.3.html),  [fanotify(7)](../man7/fanotify.7.html)

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
