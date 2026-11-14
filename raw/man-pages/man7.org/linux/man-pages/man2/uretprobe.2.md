---
{"title": "uretprobe(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/uretprobe.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uretprobe(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    uretprobe(2)               System Calls Manual               uretprobe(2)

## [](#NAME)NAME

           uretprobe - execute pending return uprobes

## [](#SYNOPSIS)SYNOPSIS

           int uretprobe(void);

## [](#DESCRIPTION)DESCRIPTION

           uretprobe() is an alternative to breakpoint instructions for
           triggering return uprobe consumers.

           Calls to uretprobe() are only made from the user-space trampoline
           provided by the kernel.  Calls from any other place result in a
           SIGILL.

## [](#RETURN_VALUE)RETURN VALUE

           The return value is architecture-specific.

## [](#ERRORS)ERRORS

           SIGILL uretprobe() was called by a user-space program.

## [](#VERSIONS)VERSIONS

           The behavior varies across systems.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           Linux 6.11.

           uretprobe() was initially introduced for the x86_64 architecture
           where it was shown to be faster than breakpoint traps.  It might
           be extended to other architectures.

## [](#CAVEATS)CAVEATS

           uretprobe() exists only to allow the invocation of return uprobe
           consumers.  It should never be called directly.

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

    Linux man-pages 6.19            2026-02-08                   uretprobe(2)

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
