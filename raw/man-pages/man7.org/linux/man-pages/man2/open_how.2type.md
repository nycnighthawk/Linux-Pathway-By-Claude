---
{"title": "open_how(2type) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/open_how.2type.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# open_how(2type) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    open_how(2type)                                           open_how(2type)

## [](#NAME)NAME

           open_how - how to open a pathname

## [](#LIBRARY)LIBRARY

           Linux kernel headers

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/openat2.h>

           struct open_how {
               u64  flags;    /* O_* flags */
               u64  mode;     /* Mode for O_{CREAT,TMPFILE} */
               u64  resolve;  /* RESOLVE_* flags */
               /* ... */
           };

## [](#DESCRIPTION)DESCRIPTION

           Specifies how a pathname should be opened.

           The fields are as follows:

           flags  This field specifies the file creation and file status
                  flags to use when opening the file.

           mode   This field specifies the mode for the new file.

           resolve
                  This is a bit mask of flags that modify the way in which
                  all components of a pathname will be resolved (see
                  path_resolution(7) for background information).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Extra fields may be appended to the structure, with a zero value
           in a new field resulting in the kernel behaving as though that
           extension field was not present.  Therefore, a user must zero-fill
           this structure on initialization.

## [](#SEE_ALSO)SEE ALSO

           openat2(2)

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

    Linux man-pages 6.19            2025-09-21                open_how(2type)

------------------------------------------------------------------------

Pages that refer to this page: [openat2(2)](../man2/openat2.2.html)

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
