---
{"title": "fifo(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/fifo.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fifo(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    fifo(7)              Miscellaneous Information Manual             fifo(7)

## [](#NAME)NAME

           fifo - first-in first-out special file, named pipe

## [](#DESCRIPTION)DESCRIPTION

           A FIFO special file (a named pipe) is similar to a pipe, except
           that it is accessed as part of the filesystem.  It can be opened
           by multiple processes for reading or writing.  When processes are
           exchanging data via the FIFO, the kernel passes all data
           internally without writing it to the filesystem.  Thus, the FIFO
           special file has no contents on the filesystem; the filesystem
           entry merely serves as a reference point so that processes can
           access the pipe using a name in the filesystem.

           The kernel maintains exactly one pipe object for each FIFO special
           file that is opened by at least one process.  The FIFO must be
           opened on both ends (reading and writing) before data can be
           passed.  Normally, opening the FIFO blocks until the other end is
           opened also.

           A process can open a FIFO in nonblocking mode.  In this case,
           opening for read-only succeeds even if no one has opened on the
           write side yet and opening for write-only fails with ENXIO (no
           such device or address) unless the other end has already been
           opened.

           Under Linux, opening a FIFO for read and write will succeed both
           in blocking and nonblocking mode.  POSIX leaves this behavior
           undefined.  This can be used to open a FIFO for writing while
           there are no readers available.  A process that uses both ends of
           the connection in order to communicate with itself should be very
           careful to avoid deadlocks.

## [](#NOTES)NOTES

           For details of the semantics of I/O on FIFOs, see pipe(7).

           When a process tries to write to a FIFO that is not opened for
           read on the other side, the process is sent a SIGPIPE signal.

           FIFO special files can be created by mkfifo(3), and are indicated
           by ls -l with the file type 'p'.

## [](#SEE_ALSO)SEE ALSO

           mkfifo(1), open(2), pipe(2), sigaction(2), signal(2),
           socketpair(2), mkfifo(3), pipe(7)

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

    Linux man-pages 6.19            2026-02-08                        fifo(7)

------------------------------------------------------------------------

Pages that refer to this page: [open(2)](../man2/open.2.html),  [mkfifo(3)](../man3/mkfifo.3.html),  [sd_is_fifo(3)](../man3/sd_is_fifo.3.html),  [systemd.socket(5)](../man5/systemd.socket.5.html),  [pipe(7)](../man7/pipe.7.html),  [signal(7)](../man7/signal.7.html)

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
