---
{"title": "pciconfig_read(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pciconfig_iobase.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pciconfig_read(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    pciconfig_read(2)          System Calls Manual          pciconfig_read(2)

## [](#NAME)NAME

           pciconfig_read, pciconfig_write, pciconfig_iobase - pci device
           information handling

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <pci.h>

           int pciconfig_read(unsigned long bus, unsigned long dfn,
                              unsigned long off, unsigned long size,
                              unsigned char *buf);
           int pciconfig_write(unsigned long bus, unsigned long dfn,
                              unsigned long off, unsigned long size,
                              unsigned char *buf);
           int pciconfig_iobase(int which, unsigned long bus,
                              unsigned long devfn);

## [](#DESCRIPTION)DESCRIPTION

           Most of the interaction with PCI devices is already handled by the
           kernel PCI layer, and thus these calls should not normally need to
           be accessed from user space.

           pciconfig_read()
                  Reads to buf from device dev at offset off value.

           pciconfig_write()
                  Writes from buf to device dev at offset off value.

           pciconfig_iobase()
                  You pass it a bus/devfn pair and get a physical address for
                  either the memory offset (for things like prep, this is
                  0xc0000000), the IO base for PIO cycles, or the ISA holes
                  if any.

## [](#RETURN_VALUE)RETURN VALUE

           pciconfig_read()
                  On success, zero is returned.  On error, -1 is returned and
                  errno is set to indicate the error.

           pciconfig_write()
                  On success, zero is returned.  On error, -1 is returned and
                  errno is set to indicate the error.

           pciconfig_iobase()
                  Returns information on locations of various I/O regions in
                  physical memory according to the which value.  Values for
                  which are: IOBASE_BRIDGE_NUMBER, IOBASE_MEMORY, IOBASE_IO,
                  IOBASE_ISA_IO, IOBASE_ISA_MEM.

## [](#ERRORS)ERRORS

           EINVAL size value is invalid.  This does not apply to
                  pciconfig_iobase().

           EIO    I/O error.

           ENODEV For pciconfig_iobase(), "hose" value is NULL.  For the
                  other calls, could not find a slot.

           ENOSYS The system has not implemented these calls (CONFIG_PCI not
                  defined).

           EOPNOTSUPP
                  This return value is valid only for pciconfig_iobase().  It
                  is returned if the value for which is invalid.

           EPERM  User does not have the CAP_SYS_ADMIN capability.  This does
                  not apply to pciconfig_iobase().

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.0.26/2.1.11.

## [](#SEE_ALSO)SEE ALSO

           capabilities(7)

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

    Linux man-pages 6.19            2026-02-08              pciconfig_read(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/pciconfig_read.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
