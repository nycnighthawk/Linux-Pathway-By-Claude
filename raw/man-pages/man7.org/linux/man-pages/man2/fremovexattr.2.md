---
{"title": "removexattr(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/fremovexattr.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# removexattr(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    removexattr(2)             System Calls Manual             removexattr(2)

## [](#NAME)NAME

           removexattr, lremovexattr, fremovexattr - remove an extended
           attribute

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/xattr.h>

           int removexattr(const char *path, const char *name);
           int lremovexattr(const char *path, const char *name);
           int fremovexattr(int fd, const char *name);

## [](#DESCRIPTION)DESCRIPTION

           Extended attributes are name:value pairs associated with inodes
           (files, directories, symbolic links, etc.).  They are extensions
           to the normal attributes which are associated with all inodes in
           the system (i.e., the stat(2) data).  A complete overview of
           extended attributes concepts can be found in xattr(7).

           removexattr() removes the extended attribute identified by name
           and associated with the given path in the filesystem.

           lremovexattr() is identical to removexattr(), except in the case
           of a symbolic link, where the extended attribute is removed from
           the link itself, not the file that it refers to.

           fremovexattr() is identical to removexattr(), only the extended
           attribute is removed from the open file referred to by fd (as
           returned by open(2)) in place of path.

           An extended attribute name is a null-terminated string.  The name
           includes a namespace prefix; there may be several, disjoint
           namespaces associated with an individual inode.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On failure, -1 is returned and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           ENODATA
                  The named attribute does not exist.

           ENOTSUP
                  Extended attributes are not supported by the filesystem, or
                  are disabled.

           In addition, the errors documented in stat(2) can also occur.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4, glibc 2.3.

## [](#SEE_ALSO)SEE ALSO

           getfattr(1), setfattr(1), getxattr(2), listxattr(2), open(2),
           setxattr(2), stat(2), symlink(7), xattr(7)

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

    Linux man-pages 6.19            2026-02-08                 removexattr(2)

------------------------------------------------------------------------

Pages that refer to this page: [getxattr(2)](../man2/getxattr.2.html),  [listxattr(2)](../man2/listxattr.2.html),  [setxattr(2)](../man2/setxattr.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [symlink(7)](../man7/symlink.7.html),  [xattr(7)](../man7/xattr.7.html)

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
