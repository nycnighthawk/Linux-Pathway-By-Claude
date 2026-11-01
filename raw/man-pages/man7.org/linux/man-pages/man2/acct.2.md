---
{"title": "acct(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/acct.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# acct(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    acct(2)                    System Calls Manual                    acct(2)

## [](#NAME)NAME

           acct - switch process accounting on or off

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int acct(const char *_Nullable path);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           acct():
               Since glibc 2.21:
                   _DEFAULT_SOURCE
               In glibc 2.19 and 2.20:
                   _DEFAULT_SOURCE || (_XOPEN_SOURCE && _XOPEN_SOURCE < 500)
               Up to and including glibc 2.19:
                   _BSD_SOURCE || (_XOPEN_SOURCE && _XOPEN_SOURCE < 500)

## [](#DESCRIPTION)DESCRIPTION

           The acct() system call enables or disables process accounting.  If
           called with the pathname of an existing file as its argument,
           accounting is turned on, and records for each terminating process
           are appended to the file as it terminates.  An argument of NULL
           causes accounting to be turned off.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES Write permission is denied for the specified file, or
                  search permission is denied for one of the directories in
                  the path prefix of path (see also path_resolution(7)), or
                  path is not a regular file.

           EFAULT path points outside your accessible address space.

           EIO    Error writing to the file path.

           EISDIR path is a directory.

           ELOOP  Too many symbolic links were encountered in resolving path.

           ENAMETOOLONG
                  path was too long.

           ENFILE The system-wide limit on the total number of open files has
                  been reached.

           ENOENT The specified path does not exist.

           ENOMEM Out of memory.

           ENOSYS BSD process accounting has not been enabled when the
                  operating system kernel was compiled.  The kernel
                  configuration parameter controlling this feature is
                  CONFIG_BSD_PROCESS_ACCT.

           ENOTDIR
                  A component used as a directory in path is not in fact a
                  directory.

           EPERM  The calling process has insufficient privilege to enable
                  process accounting.  On Linux, the CAP_SYS_PACCT capability
                  is required.

           EROFS  path refers to a file on a read-only filesystem.

           EUSERS There are no more free file structures or we ran out of
                  memory.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           SVr4, 4.3BSD.

## [](#NOTES)NOTES

           No accounting is produced for programs running when a system crash
           occurs.  In particular, nonterminating processes are never
           accounted for.

           The structure of the records written to the accounting file is
           described in acct(5).

## [](#SEE_ALSO)SEE ALSO

           acct(5)

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

    Linux man-pages 6.19            2025-05-17                        acct(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [acct(5)](../man5/acct.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [feature_test_macros(7)](../man7/feature_test_macros.7.html)

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
