---
{"title": "close(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/close.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# close(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    close(2)                   System Calls Manual                   close(2)

## [](#NAME)NAME

           close - close a file descriptor

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int close(int fd);

## [](#DESCRIPTION)DESCRIPTION

           close() closes a file descriptor, so that it no longer refers to
           any file and may be reused.  Any record locks (see fcntl(2)) held
           on the file it was associated with, and owned by the process, are
           removed regardless of the file descriptor that was used to obtain
           the lock.  This has some unfortunate consequences and one should
           be extra careful when using advisory record locking.  See fcntl(2)
           for discussion of the risks and consequences as well as for the
           (probably preferred) open file description locks.

           If fd is the last file descriptor referring to the underlying open
           file description (see open(2)), the resources associated with the
           open file description are freed; if the file descriptor was the
           last reference to a file which has been removed using unlink(2),
           the file is deleted.

## [](#RETURN_VALUE)RETURN VALUE

           close() returns zero on success.  On error, -1 is returned, and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  fd isn't a valid open file descriptor.

           EINTR  The close() call was interrupted by a signal; see
                  signal(7).

           EIO    An I/O error occurred.

           ENOSPC
           EDQUOT On NFS, these errors are not normally reported against the
                  first write which exceeds the available storage space, but
                  instead against a subsequent write(2), fsync(2), or
                  close().

           See CAVEATS for a discussion of why close() should not be retried
           after an error.

## [](#STANDARDS)STANDARDS

           POSIX.1-2008.

## [](#HISTORY)HISTORY

           4.3BSD, SVr4, POSIX.1-1988.

## [](#NOTES)NOTES

           The close-on-exec file descriptor flag can be used to ensure that
           a file descriptor is automatically closed upon a successful
           execve(2); see fcntl(2) for details.

## [](#CAVEATS)CAVEATS

           A successful close does not guarantee that the data has been
           successfully saved to disk, as the kernel uses the buffer cache to
           defer writes.  Typically, filesystems do not flush buffers when a
           file is closed.  If you need to be sure that the data is
           physically stored on the underlying disk, use fsync(2).  (It will
           depend on the disk hardware at this point.)

       Multithreaded processes and close()
           It is probably unwise to close file descriptors while they may be
           in use by system calls in other threads in the same process.
           Since a file descriptor may be reused, there are some obscure race
           conditions that may cause unintended side effects.

           Furthermore, consider the following scenario where two threads are
           performing operations on the same file descriptor:

           (1)  One thread is blocked in an I/O system call on the file
                descriptor.  For example, it is trying to write(2) to a pipe
                that is already full, or trying to read(2) from a stream
                socket which currently has no available data.

           (2)  Another thread closes the file descriptor.

           The behavior in this situation varies across systems.  On some
           systems, when the file descriptor is closed, the blocking system
           call returns immediately with an error.

           On Linux (and possibly some other systems), the behavior is
           different: the blocking I/O system call holds a reference to the
           underlying open file description, and this reference keeps the
           description open until the I/O system call completes.  (See
           open(2) for a discussion of open file descriptions.)  Thus, the
           blocking system call in the first thread may successfully complete
           after the close() in the second thread.

       Dealing with error returns from close()
           A careful programmer will check the return value of close(), since
           it is quite possible that errors on a previous write(2) operation
           are reported only on the final close() that releases the open file
           description.  Failing to check the return value when closing a
           file may lead to silent loss of data.  This can especially be
           observed with NFS and with disk quota.

           Note, however, that a failure return should be used only for
           diagnostic purposes (i.e., a warning to the application that there
           may still be I/O pending or there may have been failed I/O) or
           remedial purposes (e.g., writing the file once more or creating a
           backup).

           Retrying the close() after a failure return is the wrong thing to
           do, since this may cause a reused file descriptor from another
           thread to be closed.  This can occur because the Linux kernel
           always releases the file descriptor early in the close operation,
           freeing it for reuse; the steps that may return an error, such as
           flushing data to the filesystem or device, occur only later in the
           close operation.

           Many other implementations similarly always close the file
           descriptor (except in the case of EBADF, meaning that the file
           descriptor was invalid) even if they subsequently report an error
           on return from close().  POSIX.1-2008 was silent on this point.

           A careful programmer who wants to know about I/O errors may
           precede close() with a call to fsync(2).

           The EINTR error is a somewhat special case.  Regarding the EINTR
           error, POSIX.1-2008 said:

                  If close() is interrupted by a signal that is to be caught,
                  it shall return -1 with errno set to EINTR and the state of
                  fd is unspecified.

           This permits the behavior that occurs on Linux and many other
           implementations, where, as with other errors that may be reported
           by close(), the file descriptor is guaranteed to be closed.
           However, it also permits another possibility: that the
           implementation returns an EINTR error and keeps the file
           descriptor open.  (According to its documentation, HP-UX's close()
           does this.)  The caller must then once more use close() to close
           the file descriptor, to avoid file descriptor leaks.  This
           divergence in implementation behaviors provides a difficult hurdle
           for portable applications, since on many implementations, close()
           must not be called again after an EINTR error, and on at least
           one, close() must be called again.

           POSIX.1-2024 standardized the behavior of HP-UX, making Linux and
           many other implementations non-conforming.  There are no plans to
           change the behavior on Linux.

## [](#SEE_ALSO)SEE ALSO

           close_range(2), fcntl(2), fsync(2), open(2), shutdown(2),
           unlink(2), fclose(3)

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

    Linux man-pages 6.19            2026-02-08                       close(2)

------------------------------------------------------------------------

Pages that refer to this page: [bpf(2)](../man2/bpf.2.html),  [close_range(2)](../man2/close_range.2.html),  [dup(2)](../man2/dup.2.html),  [epoll_create(2)](../man2/epoll_create.2.html),  [eventfd(2)](../man2/eventfd.2.html),  [flock(2)](../man2/flock.2.html),  [fsmount(2)](../man2/fsmount.2.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [open(2)](../man2/open.2.html),  [perfmonctl(2)](../man2/perfmonctl.2.html),  [read(2)](../man2/read.2.html),  [shutdown(2)](../man2/shutdown.2.html),  [signalfd(2)](../man2/signalfd.2.html),  [socket(2)](../man2/socket.2.html),  [spu_create(2)](../man2/spu_create.2.html),  [spu_run(2)](../man2/spu_run.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [timerfd_create(2)](../man2/timerfd_create.2.html),  [write(2)](../man2/write.2.html),  [closedir(3)](../man3/closedir.3.html),  [dbopen(3)](../man3/dbopen.3.html),  [fclose(3)](../man3/fclose.3.html),  [fcloseall(3)](../man3/fcloseall.3.html),  [fts(3)](../man3/fts.3.html),  [getdtablesize(3)](../man3/getdtablesize.3.html),  [io_uring_prep_close(3)](../man3/io_uring_prep_close.3.html),  [io_uring_prep_close_direct(3)](../man3/io_uring_prep_close_direct.3.html),  [io_uring_prep_fixed_fd_install(3)](../man3/io_uring_prep_fixed_fd_install.3.html),  [mkfifo(3)](../man3/mkfifo.3.html),  [\_\_pmconnectlogger(3)](../man3/__pmconnectlogger.3.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [sd_varlink_call_and_upgrade(3)](../man3/sd_varlink_call_and_upgrade.3.html),  [sd_varlink_reply_and_upgrade(3)](../man3/sd_varlink_reply_and_upgrade.3.html),  [shm_open(3)](../man3/shm_open.3.html),  [stdio(3)](../man3/stdio.3.html),  [nfs(5)](../man5/nfs.5.html),  [systemd.socket(5)](../man5/systemd.socket.5.html),  [cpuset(7)](../man7/cpuset.7.html),  [epoll(7)](../man7/epoll.7.html),  [fanotify(7)](../man7/fanotify.7.html),  [inotify(7)](../man7/inotify.7.html),  [io_uring_cancelation(7)](../man7/io_uring_cancelation.7.html),  [pipe(7)](../man7/pipe.7.html),  [shm_overview(7)](../man7/shm_overview.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [socket(7)](../man7/socket.7.html),  [spufs(7)](../man7/spufs.7.html)

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
