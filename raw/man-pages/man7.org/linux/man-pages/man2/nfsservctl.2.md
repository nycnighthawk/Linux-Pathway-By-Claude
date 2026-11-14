---
{"title": "nfsservctl(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/nfsservctl.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nfsservctl(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nfsservctl(2)              System Calls Manual              nfsservctl(2)

## [](#NAME)NAME

           nfsservctl - syscall interface to kernel nfs daemon

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/nfsd/syscall.h>

           long nfsservctl(int cmd, struct nfsctl_arg *argp,
                           union nfsctl_res *resp);

## [](#DESCRIPTION)DESCRIPTION

           Note: Since Linux 3.1, this system call no longer exists.  It has
           been replaced by a set of files in the nfsd filesystem; see
           nfsd(7).

               /*
                * These are the commands understood by nfsctl().
                */
               #define NFSCTL_SVC        0  /* This is a server process.  */
               #define NFSCTL_ADDCLIENT  1  /* Add an NFS client.  */
               #define NFSCTL_DELCLIENT  2  /* Remove an NFS client.  */
               #define NFSCTL_EXPORT     3  /* Export a filesystem.  */
               #define NFSCTL_UNEXPORT   4  /* Unexport a filesystem.  */
               #define NFSCTL_UGIDUPDATE 5  /* Update a client's UID/GID map
                                               (only in Linux 2.4.x and earlier).  */
               #define NFSCTL_GETFH      6  /* Get a file handle (used by mountd(8))
                                               (only in Linux 2.4.x and earlier).  */

               struct nfsctl_arg {
                   int                       ca_version;     /* safeguard */
                   union {
                       struct nfsctl_svc     u_svc;
                       struct nfsctl_client  u_client;
                       struct nfsctl_export  u_export;
                       struct nfsctl_uidmap  u_umap;
                       struct nfsctl_fhparm  u_getfh;
                       unsigned int          u_debug;
                   } u;
               }

               union nfsctl_res {
                       struct knfs_fh          cr_getfh;
                       unsigned int            cr_debug;
               };

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Removed in Linux 3.1.  Removed in glibc 2.28.

## [](#SEE_ALSO)SEE ALSO

           nfsd(7)

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

    Linux man-pages 6.19            2025-09-21                  nfsservctl(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [capabilities(7)](../man7/capabilities.7.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/nfsservctl.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
