---
{"title": "outb(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/inw.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# outb(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    outb(2)                    System Calls Manual                    outb(2)

## [](#NAME)NAME

           outb, outw, outl, outsb, outsw, outsl, inb, inw, inl, insb, insw,
           insl, outb_p, outw_p, outl_p, inb_p, inw_p, inl_p - port I/O

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/io.h>

           unsigned char inb(unsigned short port);
           unsigned char inb_p(unsigned short port);
           unsigned short inw(unsigned short port);
           unsigned short inw_p(unsigned short port);
           unsigned int inl(unsigned short port);
           unsigned int inl_p(unsigned short port);

           void outb(unsigned char value, unsigned short port);
           void outb_p(unsigned char value, unsigned short port);
           void outw(unsigned short value, unsigned short port);
           void outw_p(unsigned short value, unsigned short port);
           void outl(unsigned int value, unsigned short port);
           void outl_p(unsigned int value, unsigned short port);

           void insb(unsigned long count;
                      unsigned short port, void addr[count],
                      unsigned long count);
           void insw(unsigned long count;
                      unsigned short port, void addr[count],
                      unsigned long count);
           void insl(unsigned long count;
                      unsigned short port, void addr[count],
                      unsigned long count);
           void outsb(unsigned long count;
                      unsigned short port, const void addr[count],
                      unsigned long count);
           void outsw(unsigned long count;
                      unsigned short port, const void addr[count],
                      unsigned long count);
           void outsl(unsigned long count;
                      unsigned short port, const void addr[count],
                      unsigned long count);

## [](#DESCRIPTION)DESCRIPTION

           This family of functions is used to do low-level port input and
           output.  The out* functions do port output, the in* functions do
           port input; the b-suffix functions are byte-width and the w-suffix
           functions word-width; the _p-suffix functions pause until the I/O
           completes.

           They are primarily designed for internal kernel use, but can be
           used from user space.

           You must compile with -O or -O2 or similar.  The functions are
           defined as inline macros, and will not be substituted in without
           optimization enabled, causing unresolved references at link time.

           You use ioperm(2) or alternatively iopl(2) to tell the kernel to
           allow the user space application to access the I/O ports in
           question.  Failure to do this will cause the application to
           receive a segmentation fault.

## [](#VERSIONS)VERSIONS

           outb() and friends are hardware-specific.  The value argument is
           passed first and the port argument is passed second, which is the
           opposite order from most DOS implementations.

## [](#STANDARDS)STANDARDS

           None.

## [](#SEE_ALSO)SEE ALSO

           ioperm(2), iopl(2)

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

    Linux man-pages 6.19            2026-02-08                        outb(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioperm(2)](../man2/ioperm.2.html),  [iopl(2)](../man2/iopl.2.html)

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
