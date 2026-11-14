---
{"title": "umask(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/umask.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# umask(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    umask(2)                   System Calls Manual                   umask(2)

## [](#NAME)NAME

           umask - set file mode creation mask

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/stat.h>

           mode_t umask(mode_t mask);

## [](#DESCRIPTION)DESCRIPTION

           umask() sets the calling process's file mode creation mask (umask)
           to mask & 0777 (i.e., only the file permission bits of mask are
           used), and returns the previous value of the mask.

           The umask is used by open(2), mkdir(2), and other system calls
           that create files to modify the permissions placed on newly
           created files or directories.  Specifically, permissions in the
           umask are turned off from the mode argument to open(2) and
           mkdir(2).

           Alternatively, if the parent directory has a default ACL (see
           acl(5)), the umask is ignored, the default ACL is inherited, the
           permission bits are set based on the inherited ACL, and permission
           bits absent in the mode argument are turned off.  For example, the
           following default ACL is equivalent to a umask of 022:

               u::rwx,g::r-x,o::r-x

           Combining the effect of this default ACL with a mode argument of
           0666 (rw-rw-rw-), the resulting file permissions would be 0644
           (rw-r--r--).

           The constants that should be used to specify mask are described in
           inode(7).

           The typical default value for the process umask is S_IWGRP |
           S_IWOTH (octal 022).  In the usual case where the mode argument to
           open(2) is specified as:

               S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH

           (octal 0666) when creating a new file, the permissions on the
           resulting file will be:

               S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH

           (because 0666 & ~022 = 0644; i.e., rw-r--r--).

## [](#RETURN_VALUE)RETURN VALUE

           This system call always succeeds and the previous value of the
           mask is returned.

## [](#STANDARDS)STANDARDS

           POSIX.1-2008.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4, 4.3BSD.

## [](#NOTES)NOTES

           A child process created via fork(2) inherits its parent's umask.
           The umask is left unchanged by execve(2).

           It is impossible to use umask() to fetch a process's umask without
           at the same time changing it.  A second call to umask() would then
           be needed to restore the umask.  The nonatomicity of these two
           steps provides the potential for races in multithreaded programs.

           Since Linux 4.7, the umask of any process can be viewed via the
           Umask field of /proc/pid/status.  Inspecting this field in
           /proc/self/status allows a process to retrieve its umask without
           at the same time changing it.

           The umask setting also affects the permissions assigned to POSIX
           IPC objects (mq_open(3), sem_open(3), shm_open(3)), FIFOs
           (mkfifo(3)), and UNIX domain sockets (unix(7)) created by the
           process.  The umask does not affect the permissions assigned to
           System V IPC objects created by the process (using msgget(2),
           semget(2), shmget(2)).

## [](#SEE_ALSO)SEE ALSO

           chmod(2), mkdir(2), open(2), stat(2), acl(5)

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

    Linux man-pages 6.19            2026-02-08                       umask(2)

------------------------------------------------------------------------

Pages that refer to this page: [git-init(1)](../man1/git-init.1.html),  [systemd-mount(1)](../man1/systemd-mount.1.html),  [clone(2)](../man2/clone.2.html),  [mkdir(2)](../man2/mkdir.2.html),  [mknod(2)](../man2/mknod.2.html),  [open(2)](../man2/open.2.html),  [spu_create(2)](../man2/spu_create.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unshare(2)](../man2/unshare.2.html),  [fopen(3)](../man3/fopen.3.html),  [mkfifo(3)](../man3/mkfifo.3.html),  [mkstemp(3)](../man3/mkstemp.3.html),  [mode_t(3type)](../man3/mode_t.3type.html),  [shm_open(3)](../man3/shm_open.3.html),  [proc_pid_status(5)](../man5/proc_pid_status.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [pthreads(7)](../man7/pthreads.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [unix(7)](../man7/unix.7.html)

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
