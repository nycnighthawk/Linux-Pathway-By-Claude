---
{"title": "sln(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sln.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sln(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sln(8)                   System Manager's Manual                   sln(8)

## [](#NAME)NAME

           sln - create symbolic links

## [](#SYNOPSIS)SYNOPSIS

           sln source dest
           sln filelist

## [](#DESCRIPTION)DESCRIPTION

           The sln program creates symbolic links.  Unlike the ln(1) program,
           it is statically linked.  This means that if for some reason the
           dynamic linker is not working, sln can be used to make symbolic
           links to dynamic libraries.

           The command line has two forms.  In the first form, it creates
           dest as a new symbolic link to source.

           In the second form, filelist is a list of space-separated pathname
           pairs, and the effect is as if sln was executed once for each line
           of the file, with the two pathnames as the arguments.

           The sln program supports no command-line options.

## [](#SEE_ALSO)SEE ALSO

           ln(1), ld.so(8), ldconfig(8)

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

    Linux man-pages 6.19            2026-02-08                         sln(8)

------------------------------------------------------------------------

Pages that refer to this page: [ld.so(8)](../man8/ld.so.8.html)

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
