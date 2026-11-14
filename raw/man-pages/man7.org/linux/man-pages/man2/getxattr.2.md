---
{"title": "getxattr(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getxattr.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getxattr(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getxattr(2)                System Calls Manual                getxattr(2)

## [](#NAME)NAME

           getxattr, lgetxattr, fgetxattr - retrieve an extended attribute
           value

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/xattr.h>

           ssize_t getxattr(size_t size;
                            const char *path, const char *name,
                            void value[size], size_t size);
           ssize_t lgetxattr(size_t size;
                            const char *path, const char *name,
                            void value[size], size_t size);
           ssize_t fgetxattr(size_t size;
                            int fd, const char *name,
                            void value[size], size_t size);

## [](#DESCRIPTION)DESCRIPTION

           Extended attributes are name:value pairs associated with inodes
           (files, directories, symbolic links, etc.).  They are extensions
           to the normal attributes which are associated with all inodes in
           the system (i.e., the stat(2) data).  A complete overview of
           extended attributes concepts can be found in xattr(7).

           getxattr() retrieves the value of the extended attribute
           identified by name and associated with the given path in the
           filesystem.  The attribute value is placed in the buffer pointed
           to by value; size specifies the size of that buffer.  The return
           value of the call is the number of bytes placed in value.

           lgetxattr() is identical to getxattr(), except in the case of a
           symbolic link, where the link itself is interrogated, not the file
           that it refers to.

           fgetxattr() is identical to getxattr(), only the open file
           referred to by fd (as returned by open(2)) is interrogated in
           place of path.

           An extended attribute name is a null-terminated string.  The name
           includes a namespace prefix; there may be several, disjoint
           namespaces associated with an individual inode.  The value of an
           extended attribute is a chunk of arbitrary textual or binary data
           that was assigned using setxattr(2).

           If size is specified as zero, these calls return the current size
           of the named extended attribute (and leave value unchanged).  This
           can be used to determine the size of the buffer that should be
           supplied in a subsequent call.  (But, bear in mind that there is a
           possibility that the attribute value may change between the two
           calls, so that it is still necessary to check the return status
           from the second call.)

## [](#RETURN_VALUE)RETURN VALUE

           On success, these calls return a nonnegative value which is the
           size (in bytes) of the extended attribute value.  On failure, -1
           is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           E2BIG  The size of the attribute value is larger than the maximum
                  size allowed; the attribute cannot be retrieved.  This can
                  happen on filesystems that support very large attribute
                  values such as NFSv4, for example.

           ENODATA
                  The named attribute does not exist, or the process has no
                  access to this attribute.

           ENOTSUP
                  Extended attributes are not supported by the filesystem, or
                  are disabled.

           ERANGE The size of the value buffer is too small to hold the
                  result.

           In addition, the errors documented in stat(2) can also occur.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4, glibc 2.3.

## [](#EXAMPLES)EXAMPLES

           See listxattr(2).

## [](#SEE_ALSO)SEE ALSO

           getfattr(1), setfattr(1), listxattr(2), open(2), removexattr(2),
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

    Linux man-pages 6.19            2026-02-08                    getxattr(2)

------------------------------------------------------------------------

Pages that refer to this page: [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [listxattr(2)](../man2/listxattr.2.html),  [open(2)](../man2/open.2.html),  [removexattr(2)](../man2/removexattr.2.html),  [setxattr(2)](../man2/setxattr.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [io_uring_prep_fgetxattr(3)](../man3/io_uring_prep_fgetxattr.3.html),  [io_uring_prep_getxattr(3)](../man3/io_uring_prep_getxattr.3.html),  [capabilities(7)](../man7/capabilities.7.html),  [symlink(7)](../man7/symlink.7.html),  [xattr(7)](../man7/xattr.7.html)

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
