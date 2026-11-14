---
{"title": "mknod(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/mknod.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mknod(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mknod(2)                   System Calls Manual                   mknod(2)

## [](#NAME)NAME

           mknod, mknodat - create a special or ordinary file

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/stat.h>

           int mknod(const char *path, mode_t mode, dev_t dev);

           #include <fcntl.h>           /* Definition of AT_* constants */
           #include <sys/stat.h>

           int mknodat(int dirfd, const char *path, mode_t mode, dev_t dev);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           mknod():
               _XOPEN_SOURCE >= 500
                   || /* Since glibc 2.19: */ _DEFAULT_SOURCE
                   || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           The system call mknod() creates a filesystem node (file, device
           special file, or named pipe) named path, with attributes specified
           by mode and dev.

           The mode argument specifies both the file mode to use and the type
           of node to be created.  It should be a combination (using bitwise
           OR) of one of the file types listed below and zero or more of the
           file mode bits listed in inode(7).

           The file mode is modified by the process's umask in the usual way:
           in the absence of a default ACL, the permissions of the created
           node are (mode & ~umask).

           The file type must be one of S_IFREG, S_IFCHR, S_IFBLK, S_IFIFO,
           or S_IFSOCK to specify a regular file (which will be created
           empty), character special file, block special file, FIFO (named
           pipe), or UNIX domain socket, respectively.  (Zero file type is
           equivalent to type S_IFREG.)

           If the file type is S_IFCHR or S_IFBLK, then dev specifies the
           major and minor numbers of the newly created device special file
           (makedev(3) may be useful to build the value for dev); otherwise
           it is ignored.

           If path already exists, or is a symbolic link, this call fails
           with an EEXIST error.

           The newly created node will be owned by the effective user ID of
           the process.  If the directory containing the node has the set-
           group-ID bit set, or if the filesystem is mounted with BSD group
           semantics, the new node will inherit the group ownership from its
           parent directory; otherwise it will be owned by the effective
           group ID of the process.

       mknodat()
           The mknodat() system call operates in exactly the same way as
           mknod(), except for the differences described here.

           If path is relative, then it is interpreted relative to the
           directory referred to by the file descriptor dirfd (rather than
           relative to the current working directory of the calling process,
           as is done by mknod() for a relative pathname).

           If path is relative and dirfd is the special value AT_FDCWD, then
           path is interpreted relative to the current working directory of
           the calling process (like mknod()).

           If path is absolute, then dirfd is ignored.

           See openat(2) for an explanation of the need for mknodat().

## [](#RETURN_VALUE)RETURN VALUE

           mknod() and mknodat() return zero on success.  On error, -1 is
           returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES The parent directory does not allow write permission to the
                  process, or one of the directories in the path prefix of
                  path did not allow search permission.  (See also
                  path_resolution(7).)

           EBADF  (mknodat()) path is relative but dirfd is neither AT_FDCWD
                  nor a valid file descriptor.

           EDQUOT The user's quota of disk blocks or inodes on the filesystem
                  has been exhausted.

           EEXIST path already exists.  This includes the case where path is
                  a symbolic link, dangling or not.

           EFAULT path points outside your accessible address space.

           EINVAL mode requested creation of something other than a regular
                  file, device special file, FIFO or socket.

           ELOOP  Too many symbolic links were encountered in resolving path.

           ENAMETOOLONG
                  path was too long.

           ENOENT A directory component in path does not exist or is a
                  dangling symbolic link.

           ENOMEM Insufficient kernel memory was available.

           ENOSPC The device containing path has no room for the new node.

           ENOTDIR
                  A component used as a directory in path is not, in fact, a
                  directory.

           ENOTDIR
                  (mknodat()) path is relative and dirfd is a file descriptor
                  referring to a file other than a directory.

           EPERM  mode requested creation of something other than a regular
                  file, FIFO (named pipe), or UNIX domain socket, and the
                  caller is not privileged (Linux: does not have the
                  CAP_MKNOD capability); also returned if the filesystem
                  containing path does not support the type of node
                  requested.

           EROFS  path refers to a file on a read-only filesystem.

## [](#VERSIONS)VERSIONS

           POSIX.1-2001 says: "The only portable use of mknod() is to create
           a FIFO-special file.  If mode is not S_IFIFO or dev is not 0, the
           behavior of mknod() is unspecified."  However, nowadays one should
           never use mknod() for this purpose; one should use mkfifo(3), a
           function especially defined for this purpose.

           Under Linux, mknod() cannot be used to create directories.  One
           should make directories with mkdir(2).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024 XSI.

## [](#HISTORY)HISTORY

           mknod()
                  SVr4, 4.4BSD, SUSv1, POSIX.1-2001 XSI (but see VERSIONS).

           mknodat()
                  glibc 2.4, Linux 2.6.16, POSIX.1-2008 XSI.

## [](#NOTES)NOTES

           There are many infelicities in the protocol underlying NFS.  Some
           of these affect mknod() and mknodat().

## [](#SEE_ALSO)SEE ALSO

           mknod(1), chmod(2), chown(2), fcntl(2), mkdir(2), mount(2),
           socket(2), stat(2), umask(2), unlink(2), makedev(3), mkfifo(3),
           acl(5), path_resolution(7)

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

    Linux man-pages 6.19            2026-02-11                       mknod(2)

------------------------------------------------------------------------

Pages that refer to this page: [mknod(1)](../man1/mknod.1.html),  [F_NOTIFY(2const)](../man2/F_NOTIFY.2const.html),  [mkdir(2)](../man2/mkdir.2.html),  [open(2)](../man2/open.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unlink(2)](../man2/unlink.2.html),  [dev_t(3type)](../man3/dev_t.3type.html),  [makedev(3)](../man3/makedev.3.html),  [mkfifo(3)](../man3/mkfifo.3.html),  [remove(3)](../man3/remove.3.html),  [intro(4)](../man4/intro.4.html),  [fstab(5)](../man5/fstab.5.html),  [proc_pid_attr(5)](../man5/proc_pid_attr.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [inode(7)](../man7/inode.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [mount(8)](../man8/mount.8.html),  [xfs_db(8)](../man8/xfs_db.8.html)

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
