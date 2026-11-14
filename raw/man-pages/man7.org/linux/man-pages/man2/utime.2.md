---
{"title": "utime(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/utime.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# utime(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    utime(2)                   System Calls Manual                   utime(2)

## [](#NAME)NAME

           utime, utimes - change file last access and modification times

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <utime.h>

           int utime(const char *path,
                     const struct utimbuf *_Nullable times);

           #include <sys/time.h>

           int utimes(const char *path,
                     const struct timeval times[_Nullable 2]);

## [](#DESCRIPTION)DESCRIPTION

           Note: modern applications may prefer to use the interfaces
           described in utimensat(2).

           The utime() system call changes the access and modification times
           of the inode specified by path to the actime and modtime fields of
           times respectively.  The status change time (ctime) will be set to
           the current time, even if the other time stamps don't actually
           change.

           If times is NULL, then the access and modification times of the
           file are set to the current time.

           Changing timestamps is permitted when: either the process has
           appropriate privileges, or the effective user ID equals the user
           ID of the file, or times is NULL and the process has write
           permission for the file.

           The utimbuf structure is:

               struct utimbuf {
                   time_t actime;       /* access time */
                   time_t modtime;      /* modification time */
               };

           The utime() system call allows specification of timestamps with a
           resolution of 1 second.

           The utimes() system call is similar, but the times argument refers
           to an array rather than a structure.  The elements of this array
           are timeval structures, which allow a precision of 1 microsecond
           for specifying timestamps.  The timeval structure is:

               struct timeval {
                   long tv_sec;        /* seconds */
                   long tv_usec;       /* microseconds */
               };

           times[0] specifies the new access time, and times[1] specifies the
           new modification time.  If times is NULL, then analogously to
           utime(), the access and modification times of the file are set to
           the current time.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES Search permission is denied for one of the directories in
                  the path prefix of path (see also path_resolution(7)).

           EACCES times is NULL, the caller's effective user ID does not
                  match the owner of the file, the caller does not have write
                  access to the file, and the caller is not privileged
                  (Linux: does not have either the CAP_DAC_OVERRIDE or the
                  CAP_FOWNER capability).

           EFAULT path points to an invalid address.

           ENOENT path does not exist.

           EPERM  times is not NULL, the caller's effective UID does not
                  match the owner of the file, and the caller is not
                  privileged (Linux: does not have the CAP_FOWNER
                  capability).

           EROFS  path resides on a read-only filesystem.

## [](#STANDARDS)STANDARDS

           utime()
                  None.

           utimes()
                  POSIX.1-2024.

## [](#HISTORY)HISTORY

           utime()
                  SVr4, POSIX.1-2001.  Obsoleted in POSIX.1-2008.  Removed in
                  POSIX.1-2024.

           utimes()
                  4.3BSD, POSIX.1-2001.

## [](#NOTES)NOTES

           Linux does not allow changing the timestamps on an immutable file,
           or setting the timestamps to something other than the current time
           on an append-only file.

## [](#SEE_ALSO)SEE ALSO

           chattr(1), touch(1), futimesat(2), stat(2), utimensat(2),
           futimens(3), futimes(3), inode(7)

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

    Linux man-pages 6.19            2026-02-08                       utime(2)

------------------------------------------------------------------------

Pages that refer to this page: [indent(1)](../man1/indent.1.html),  [F_NOTIFY(2const)](../man2/F_NOTIFY.2const.html),  [futimesat(2)](../man2/futimesat.2.html),  [stat(2)](../man2/stat.2.html),  [statx(2)](../man2/statx.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [utimensat(2)](../man2/utimensat.2.html),  [ctime(3)](../man3/ctime.3.html),  [futimes(3)](../man3/futimes.3.html),  [timeval(3type)](../man3/timeval.3type.html),  [capabilities(7)](../man7/capabilities.7.html),  [inode(7)](../man7/inode.7.html),  [landlock(7)](../man7/landlock.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [time(7)](../man7/time.7.html),  [mount(8)](../man8/mount.8.html)

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
