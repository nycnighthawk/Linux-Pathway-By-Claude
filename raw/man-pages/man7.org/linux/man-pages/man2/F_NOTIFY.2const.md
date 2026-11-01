---
{"title": "F_NOTIFY(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/F_NOTIFY.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# F_NOTIFY(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    F_NOTIFY(2const)                                         F_NOTIFY(2const)

## [](#NAME)NAME

           F_NOTIFY - file and directory change notification

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE
           #include <fcntl.h>

           int fcntl(int fd, F_NOTIFY, int arg);

## [](#DESCRIPTION)DESCRIPTION

           Provide notification when the directory referred to by fd or any
           of the files that it contains is changed.  The events to be
           notified are specified in arg, which is a bit mask specified by
           ORing together zero or more of the following bits:

           DN_ACCESS
                  A file was accessed (read(2), pread(2), readv(2), and
                  similar)

           DN_MODIFY
                  A file was modified (write(2), pwrite(2), writev(2),
                  truncate(2), ftruncate(2), and similar).

           DN_CREATE
                  A file was created (open(2), creat(2), mknod(2), mkdir(2),
                  link(2), symlink(2), rename(2) into this directory).

           DN_DELETE
                  A file was unlinked (unlink(2), rename(2) to another
                  directory, rmdir(2)).

           DN_RENAME
                  A file was renamed within this directory (rename(2)).

           DN_ATTRIB
                  The attributes of a file were changed (chown(2), chmod(2),
                  utime(2), utimensat(2), and similar).

           (In order to obtain these definitions, the _GNU_SOURCE feature
           test macro must be defined before including any header files.)

           Directory notifications are normally "one-shot", and the
           application must reregister to receive further notifications.
           Alternatively, if DN_MULTISHOT is included in arg, then
           notification will remain in effect until explicitly removed.

           A series of F_NOTIFY requests is cumulative, with the events in
           arg being added to the set already monitored.  To disable
           notification of all events, make an F_NOTIFY call specifying arg
           as 0.

           Notification occurs via delivery of a signal.  The default signal
           is SIGIO, but this can be changed using the F_SETSIG operation to
           fcntl().  (Note that SIGIO is one of the nonqueuing standard
           signals; switching to the use of a real-time signal means that
           multiple notifications can be queued to the process.)  In the
           latter case, the signal handler receives a siginfo_t structure as
           its second argument (if the handler was established using
           SA_SIGINFO) and the si_fd field of this structure contains the
           file descriptor which generated the notification (useful when
           establishing notification on multiple directories).

           Especially when using DN_MULTISHOT, a real time signal should be
           used for notification, so that multiple notifications can be
           queued.

           NOTE: New applications should use the inotify interface (available
           since Linux 2.6.13), which provides a much superior interface for
           obtaining notifications of filesystem events.  See inotify(7).

## [](#RETURN_VALUE)RETURN VALUE

           Zero.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           See fcntl(2).

           ENOTDIR
                  fd does not refer to a directory.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4.

## [](#SEE_ALSO)SEE ALSO

           fcntl(2)

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

    Linux man-pages 6.19            2025-07-20               F_NOTIFY(2const)

------------------------------------------------------------------------

Pages that refer to this page: [fcntl(2)](../man2/fcntl.2.html)

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
