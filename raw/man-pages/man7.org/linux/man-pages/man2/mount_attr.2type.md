---
{"title": "mount_attr(2type) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/mount_attr.2type.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mount_attr(2type) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mount_attr(2type)                                       mount_attr(2type)

## [](#NAME)NAME

           mount_attr - what mount properties to set and clear

## [](#LIBRARY)LIBRARY

           Linux kernel headers

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/mount.h>

           struct mount_attr {
               u64 attr_set;     /* Mount properties to set */
               u64 attr_clr;     /* Mount properties to clear */
               u64 propagation;  /* Mount propagation type */
               u64 userns_fd;    /* User namespace file descriptor */
               /* ... */
           };

## [](#DESCRIPTION)DESCRIPTION

           Specifies which mount properties should be changed with
           mount_setattr(2).

           The fields are as follows:

           .attr_set
                  This field specifies which MOUNT_ATTR_* attribute flags to
                  set.

           .attr_clr
                  This field specifies which MOUNT_ATTR_* attribute flags to
                  clear.

           .propagation
                  This field specifies what mount propagation will be
                  applied.  The valid values of this field are the same
                  propagation types described in mount_namespaces(7).

           .userns_fd
                  This field specifies a file descriptor that indicates which
                  user namespace to use as a reference for ID-mapped mounts
                  with MOUNT_ATTR_IDMAP.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 5.12.  glibc 2.36.

           Extra fields may be appended to the structure, with a zero value
           in a new field resulting in the kernel behaving as though that
           extension field was not present.  Therefore, a user must zero-fill
           this structure on initialization.

## [](#SEE_ALSO)SEE ALSO

           mount_setattr(2)

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

    Linux man-pages 6.19            2025-09-21              mount_attr(2type)

------------------------------------------------------------------------

Pages that refer to this page: [fsmount(2)](../man2/fsmount.2.html),  [mount_setattr(2)](../man2/mount_setattr.2.html),  [open_tree(2)](../man2/open_tree.2.html)

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
