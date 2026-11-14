---
{"title": "listmount(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/listmount.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# listmount(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    listmount(2)               System Calls Manual               listmount(2)

## [](#NAME)NAME

           listmount - get a list of mount ID's

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/mount.h>  /* Definition of struct mnt_id_req constants */
           #include <unistd.h>

           int syscall(size_t n;
                       SYS_listmount, struct mnt_id_req *req,
                       uint64_t mnt_ids[n], size_t n,
                       unsigned long flags);

           #include <linux/mount.h>

           struct mnt_id_req {
               __u32  size;    /* sizeof(struct mnt_id_req) */
               __u64  mnt_id;  /* The parent mnt_id being searched */
               __u64  param;   /* The next mnt_id we want to find */
           };

           Note: glibc provides no wrapper for listmount(), necessitating the
           use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           To access the mounts in your namespace, you must have
           CAP_SYS_ADMIN in the user namespace.

           This function returns a list of mount IDs under the req.mnt_id.
           This is meant to be used in conjuction with statmount(2) in order
           to provide a way to iterate and discover mounted file systems.

       The mnt_id_req structure
           req.size is used by the kernel to determine which struct
           mnt_id_req is being passed in, it should always be set to
           sizeof(struct mnt_id_req).

           req.mnt_id is the parent mnt_id that we will list from, which can
           either be LSMT_ROOT which means the root mount of the current
           mount namespace, or a mount ID obtained from either statx(2) using
           STATX_MNT_ID_UNIQUE or from listmount(2).

           req.param is used to tell the kernel what mount ID to start the
           list from.  This is useful if multiple calls to listmount(2) are
           required.  This can be set to the last mount ID returned in order
           to resume from a previous spot in the list.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the number of entries filled into mnt_ids is returned;
           0 if there are no more mounts left.  On error, -1 is returned, and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EPERM  The caller does not have CAP_SYS_ADMIN in the user
                  namespace.

           EFAULT req or mnt_ids points to a location outside the process's
                  accessible address space.

           EINVAL Invalid flag specified in flags.

           EINVAL req is of insufficient size to be utilized.

           E2BIG  req is too large, the limit is the architectures page size.

           ENOENT The specified req.mnt_id doesn't exist.

           ENOMEM Out of memory (i.e., kernel memory).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#SEE_ALSO)SEE ALSO

           statmount(2), statx(2)

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

    Linux man-pages 6.19            2025-09-06                   listmount(2)

------------------------------------------------------------------------

Pages that refer to this page: [listmount(2)](../man2/listmount.2.html),  [statmount(2)](../man2/statmount.2.html),  [statx(2)](../man2/statx.2.html),  [findmnt(8)](../man8/findmnt.8.html)

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
