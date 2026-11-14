---
{"title": "fcntl(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/fcntl64.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fcntl(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    fcntl(2)                   System Calls Manual                   fcntl(2)

## [](#NAME)NAME

           fcntl - manipulate file descriptor

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <fcntl.h>

           int fcntl(int fd, int op, ...);

## [](#DESCRIPTION)DESCRIPTION

           fcntl() performs one of the operations described below on the open
           file descriptor fd.  The operation is determined by op.

           Certain of the operations below are supported only since a
           particular Linux kernel version.  The preferred method of checking
           whether the host kernel supports a particular operation is to
           invoke fcntl() with the desired op value and then test whether the
           call failed with EINVAL, indicating that the kernel does not
           recognize this value.

       Duplicating a file descriptor
           F_DUPFD(2const)
           F_DUPFD_CLOEXEC(2const)

       File descriptor flags
           F_GETFD(2const)
           F_SETFD(2const)

       File status flags
           F_GETFL(2const)
           F_SETFL(2const)

       Advisory record locking
           F_SETLK(2const)
           F_SETLKW(2const)
           F_GETLK(2const)

       Open file description locks (non-POSIX)
           F_OFD_SETLK(2const)
           F_OFD_SETLKW(2const)
           F_OFD_GETLK(2const)

       Managing signals
           F_GETOWN(2const)
           F_SETOWN(2const)
           F_GETOWN_EX(2const)
           F_SETOWN_EX(2const)
           F_GETSIG(2const)
           F_SETSIG(2const)

       Leases
           F_SETLEASE(2const)
           F_GETLEASE(2const)

       Delegations
           F_SETDELEG(2const)
           F_GETDELEG(2const)

       File and directory change notification (dnotify)
           F_NOTIFY(2const)

       Changing the capacity of a pipe
           F_SETPIPE_SZ(2const)
           F_GETPIPE_SZ(2const)

       File Sealing
           F_ADD_SEALS(2const)
           F_GET_SEALS(2const)

       File read/write hints
           F_GET_RW_HINT(2const)
           F_SET_RW_HINT(2const)
           F_GET_FILE_RW_HINT(2const)
           F_SET_FILE_RW_HINT(2const)

## [](#RETURN_VALUE)RETURN VALUE

           For a successful call, the return value depends on the operation.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES or EAGAIN
                  Operation is prohibited by locks held by other processes.

           EAGAIN The operation is prohibited because the file has been
                  memory-mapped by another process.

           EBADF  fd is not an open file descriptor

           EINVAL The value specified in op is not recognized by this kernel.

## [](#VERSIONS)VERSIONS

           POSIX.1-2024 specifies FD_CLOFORK and F_DUPFD_CLOFORK, but Linux
           doesn't support them.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           4.3BSD, SVr4, POSIX.1-1988.

## [](#SEE_ALSO)SEE ALSO

           dup2(2), flock(2), open(2), socket(2), lockf(3), capabilities(7),
           feature_test_macros(7), lslocks(8)

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

    Linux man-pages 6.19            2026-02-08                       fcntl(2)

------------------------------------------------------------------------

Pages that refer to this page: [flock(1)](../man1/flock.1.html),  [pipesz(1)](../man1/pipesz.1.html),  [accept(2)](../man2/accept.2.html),  [bpf(2)](../man2/bpf.2.html),  [chmod(2)](../man2/chmod.2.html),  [clone(2)](../man2/clone.2.html),  [close(2)](../man2/close.2.html),  [dup(2)](../man2/dup.2.html),  [eventfd(2)](../man2/eventfd.2.html),  [execve(2)](../man2/execve.2.html),  [fallocate(2)](../man2/fallocate.2.html),  [fcntl_locking(2)](../man2/fcntl_locking.2.html),  [F_DUPFD(2const)](../man2/F_DUPFD.2const.html),  [F_GETDELEG(2const)](../man2/F_GETDELEG.2const.html),  [F_GETFD(2const)](../man2/F_GETFD.2const.html),  [F_GETFL(2const)](../man2/F_GETFL.2const.html),  [F_GETLEASE(2const)](../man2/F_GETLEASE.2const.html),  [F_GETPIPE_SZ(2const)](../man2/F_GETPIPE_SZ.2const.html),  [F_GET_RW_HINT(2const)](../man2/F_GET_RW_HINT.2const.html),  [F_GET_SEALS(2const)](../man2/F_GET_SEALS.2const.html),  [F_GETSIG(2const)](../man2/F_GETSIG.2const.html),  [flock(2)](../man2/flock.2.html),  [F_NOTIFY(2const)](../man2/F_NOTIFY.2const.html),  [fork(2)](../man2/fork.2.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [gettid(2)](../man2/gettid.2.html),  [inotify_init(2)](../man2/inotify_init.2.html),  [ioctl(2)](../man2/ioctl.2.html),  [ioctl_console(2)](../man2/ioctl_console.2.html),  [memfd_create(2)](../man2/memfd_create.2.html),  [memfd_secret(2)](../man2/memfd_secret.2.html),  [mknod(2)](../man2/mknod.2.html),  [mmap(2)](../man2/mmap.2.html),  [mount(2)](../man2/mount.2.html),  [NS_GET_USERNS(2const)](../man2/NS_GET_USERNS.2const.html),  [open(2)](../man2/open.2.html),  [perf_event_open(2)](../man2/perf_event_open.2.html),  [pidfd_getfd(2)](../man2/pidfd_getfd.2.html),  [pipe(2)](../man2/pipe.2.html),  [read(2)](../man2/read.2.html),  [recv(2)](../man2/recv.2.html),  [select_tut(2)](../man2/select_tut.2.html),  [send(2)](../man2/send.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [signalfd(2)](../man2/signalfd.2.html),  [socket(2)](../man2/socket.2.html),  [statfs(2)](../man2/statfs.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [timerfd_create(2)](../man2/timerfd_create.2.html),  [truncate(2)](../man2/truncate.2.html),  [userfaultfd(2)](../man2/userfaultfd.2.html),  [write(2)](../man2/write.2.html),  [audit_open(3)](../man3/audit_open.3.html),  [dbopen(3)](../man3/dbopen.3.html),  [fopen(3)](../man3/fopen.3.html),  [lockf(3)](../man3/lockf.3.html),  [sd_event_add_io(3)](../man3/sd_event_add_io.3.html),  [shm_open(3)](../man3/shm_open.3.html),  [sockatmark(3)](../man3/sockatmark.3.html),  [statvfs(3)](../man3/statvfs.3.html),  [nfs(5)](../man5/nfs.5.html),  [proc_locks(5)](../man5/proc_locks.5.html),  [proc_sys_fs(5)](../man5/proc_sys_fs.5.html),  [systemd.socket(5)](../man5/systemd.socket.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [credentials(7)](../man7/credentials.7.html),  [epoll(7)](../man7/epoll.7.html),  [inotify(7)](../man7/inotify.7.html),  [landlock(7)](../man7/landlock.7.html),  [man-pages(7)](../man7/man-pages.7.html),  [pipe(7)](../man7/pipe.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [signal(7)](../man7/signal.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [socket(7)](../man7/socket.7.html),  [tcp(7)](../man7/tcp.7.html),  [lslocks(8)](../man8/lslocks.8.html),  [mount(8)](../man8/mount.8.html)

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
