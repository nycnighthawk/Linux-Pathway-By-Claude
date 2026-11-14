---
{"title": "setxattr(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/lsetxattr.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setxattr(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setxattr(2)                System Calls Manual                setxattr(2)

## [](#NAME)NAME

           setxattr, lsetxattr, fsetxattr - set an extended attribute value

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/xattr.h>

           int setxattr(size_t size;
                         const char *path, const char *name,
                         const void value[size], size_t size, int flags);
           int lsetxattr(size_t size;
                         const char *path, const char *name,
                         const void value[size], size_t size, int flags);
           int fsetxattr(size_t size;
                         int fd, const char *name,
                         const void value[size], size_t size, int flags);

## [](#DESCRIPTION)DESCRIPTION

           Extended attributes are name:value pairs associated with inodes
           (files, directories, symbolic links, etc.).  They are extensions
           to the normal attributes which are associated with all inodes in
           the system (i.e., the stat(2) data).  A complete overview of
           extended attributes concepts can be found in xattr(7).

           setxattr() sets the value of the extended attribute identified by
           name and associated with the given path in the filesystem.  The
           size argument specifies the size (in bytes) of value; a zero-
           length value is permitted.

           lsetxattr() is identical to setxattr(), except in the case of a
           symbolic link, where the extended attribute is set on the link
           itself, not the file that it refers to.

           fsetxattr() is identical to setxattr(), only the extended
           attribute is set on the open file referred to by fd (as returned
           by open(2)) in place of path.

           An extended attribute name is a null-terminated string.  The name
           includes a namespace prefix; there may be several, disjoint
           namespaces associated with an individual inode.  The value of an
           extended attribute is a chunk of arbitrary textual or binary data
           of specified length.

           By default (i.e., flags is zero), the extended attribute will be
           created if it does not exist, or the value will be replaced if the
           attribute already exists.  To modify these semantics, one of the
           following values can be specified in flags:

           XATTR_CREATE
                  Perform a pure create, which fails if the named attribute
                  exists already.

           XATTR_REPLACE
                  Perform a pure replace operation, which fails if the named
                  attribute does not already exist.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On failure, -1 is returned and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EDQUOT Disk quota limits meant that there is insufficient space
                  remaining to store the extended attribute.

           EEXIST XATTR_CREATE was specified, and the attribute exists
                  already.

           ENODATA
                  XATTR_REPLACE was specified, and the attribute does not
                  exist.

           ENOSPC There is insufficient space remaining to store the extended
                  attribute.

           ENOTSUP
                  The namespace prefix of name is not valid.

           ENOTSUP
                  Extended attributes are not supported by the filesystem, or
                  are disabled,

           EPERM  The file is marked immutable or append-only.  (See
                  FS_IOC_SETFLAGS(2const).)

           In addition, the errors documented in stat(2) can also occur.

           ERANGE The size of name or value exceeds a filesystem-specific
                  limit.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4, glibc 2.3.

## [](#SEE_ALSO)SEE ALSO

           getfattr(1), setfattr(1), getxattr(2), listxattr(2), open(2),
           removexattr(2), stat(2), symlink(7), xattr(7)

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

    Linux man-pages 6.19            2026-02-08                    setxattr(2)

------------------------------------------------------------------------

Pages that refer to this page: [getxattr(2)](../man2/getxattr.2.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [listxattr(2)](../man2/listxattr.2.html),  [open(2)](../man2/open.2.html),  [removexattr(2)](../man2/removexattr.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [io_uring_prep_fsetxattr(3)](../man3/io_uring_prep_fsetxattr.3.html),  [io_uring_prep_setxattr(3)](../man3/io_uring_prep_setxattr.3.html),  [capabilities(7)](../man7/capabilities.7.html),  [inotify(7)](../man7/inotify.7.html),  [landlock(7)](../man7/landlock.7.html),  [symlink(7)](../man7/symlink.7.html),  [xattr(7)](../man7/xattr.7.html)

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
