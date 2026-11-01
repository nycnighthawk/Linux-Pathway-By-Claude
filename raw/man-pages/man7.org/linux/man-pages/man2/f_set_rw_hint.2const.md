---
{"title": "F_GET_RW_HINT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/f_set_rw_hint.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# F_GET_RW_HINT(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    F_GET_RW_HINT(2const)                               F_GET_RW_HINT(2const)

## [](#NAME)NAME

           F_GET_RW_HINT, F_SET_RW_HINT, F_GET_FILE_RW_HINT,
           F_SET_FILE_RW_HINT - get/set file read/write hints

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <fcntl.h>

           int fcntl(int fd, F_GET_RW_HINT, uint64_t *arg);
           int fcntl(int fd, F_SET_RW_HINT, uint64_t *arg);
           int fcntl(int fd, F_GET_FILE_RW_HINT, uint64_t *arg);
           int fcntl(int fd, F_GET_FILE_RW_HINT, uint64_t *arg);

## [](#DESCRIPTION)DESCRIPTION

           Write lifetime hints can be used to inform the kernel about the
           relative expected lifetime of writes on a given inode or via a
           particular open file description.  (See open(2) for an explanation
           of open file descriptions.)  In this context, the term "write
           lifetime" means the expected time the data will live on media,
           before being overwritten or erased.

           An application may use the different hint values specified below
           to separate writes into different write classes, so that multiple
           users or applications running on a single storage back-end can
           aggregate their I/O patterns in a consistent manner.  However,
           there are no functional semantics implied by these flags, and
           different I/O classes can use the write lifetime hints in
           arbitrary ways, so long as the hints are used consistently.

           The following operations can be applied to the file descriptor,
           fd:

           F_GET_RW_HINT
                  Returns the value of the read/write hint associated with
                  the underlying inode referred to by fd.

           F_SET_RW_HINT
                  Sets the read/write hint value associated with the
                  underlying inode referred to by fd.  This hint persists
                  until either it is explicitly modified or the underlying
                  filesystem is unmounted.

           F_GET_FILE_RW_HINT
                  Returns the value of the read/write hint associated with
                  the open file description referred to by fd.

           F_SET_FILE_RW_HINT
                  Sets the read/write hint value associated with the open
                  file description referred to by fd.

           If an open file description has not been assigned a read/write
           hint, then it shall use the value assigned to the inode, if any.

           The following read/write hints are supported:

           RWH_WRITE_LIFE_NOT_SET
                  No specific hint has been set.  This is the default value.

           RWH_WRITE_LIFE_NONE
                  No specific write lifetime is associated with this file or
                  inode.

           RWH_WRITE_LIFE_SHORT
                  Data written to this inode or via this open file
                  description is expected to have a short lifetime.

           RWH_WRITE_LIFE_MEDIUM
                  Data written to this inode or via this open file
                  description is expected to have a lifetime longer than data
                  written with RWH_WRITE_LIFE_SHORT.

           RWH_WRITE_LIFE_LONG
                  Data written to this inode or via this open file
                  description is expected to have a lifetime longer than data
                  written with RWH_WRITE_LIFE_MEDIUM.

           RWH_WRITE_LIFE_EXTREME
                  Data written to this inode or via this open file
                  description is expected to have a lifetime longer than data
                  written with RWH_WRITE_LIFE_LONG.

           All the write-specific hints are relative to each other, and no
           individual absolute meaning should be attributed to them.

## [](#RETURN_VALUE)RETURN VALUE

           Zero.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           See fcntl(2).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.13.

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

    Linux man-pages 6.19            2025-07-20          F_GET_RW_HINT(2const)

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
