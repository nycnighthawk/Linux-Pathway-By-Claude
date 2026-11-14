---
{"title": "rmdir(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/rmdir.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rmdir(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    rmdir(2)                   System Calls Manual                   rmdir(2)

## [](#NAME)NAME

           rmdir - delete a directory

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int rmdir(const char *path);

## [](#DESCRIPTION)DESCRIPTION

           rmdir() deletes a directory, which must be empty.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES Write access to the directory containing path was not
                  allowed, or one of the directories in the path prefix of
                  path did not allow search permission.  (See also
                  path_resolution(7).)

           EBUSY  path is currently in use by the system or some process that
                  prevents its removal.  On Linux, this means path is
                  currently used as a mount point or is the root directory of
                  the calling process.

           EFAULT path points outside your accessible address space.

           EINVAL path has .  as last component.

           ELOOP  Too many symbolic links were encountered in resolving path.

           ENAMETOOLONG
                  path was too long.

           ENOENT A directory component in path does not exist or is a
                  dangling symbolic link.

           ENOMEM Insufficient kernel memory was available.

           ENOTDIR
                  path, or a component used as a directory in path, is not,
                  in fact, a directory.

           ENOTEMPTY
                  path contains entries other than .  and ..; or, path has ..
                  as its final component.  POSIX.1 also allows EEXIST for
                  this condition.

           EPERM  The directory containing path has the sticky bit (S_ISVTX)
                  set and the process's effective user ID is neither the user
                  ID of the file to be deleted nor that of the directory
                  containing it, and the process is not privileged (Linux:
                  does not have the CAP_FOWNER capability).

           EPERM  The filesystem containing path does not support the removal
                  of directories.

           EROFS  path refers to a directory on a read-only filesystem.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4, 4.3BSD.

## [](#BUGS)BUGS

           Infelicities in the protocol underlying NFS can cause the
           unexpected disappearance of directories which are still being
           used.

## [](#SEE_ALSO)SEE ALSO

           rm(1), rmdir(1), chdir(2), chmod(2), mkdir(2), rename(2),
           unlink(2), unlinkat(2)

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

    Linux man-pages 6.19            2026-02-08                       rmdir(2)

------------------------------------------------------------------------

Pages that refer to this page: [rmdir(1)](../man1/rmdir.1.html),  [fanotify_mark(2)](../man2/fanotify_mark.2.html),  [F_NOTIFY(2const)](../man2/F_NOTIFY.2const.html),  [mkdir(2)](../man2/mkdir.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unlink(2)](../man2/unlink.2.html),  [remove(3)](../man3/remove.3.html),  [cpuset(7)](../man7/cpuset.7.html),  [mount_namespaces(7)](../man7/mount_namespaces.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [symlink(7)](../man7/symlink.7.html),  [mount(8)](../man8/mount.8.html)

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
