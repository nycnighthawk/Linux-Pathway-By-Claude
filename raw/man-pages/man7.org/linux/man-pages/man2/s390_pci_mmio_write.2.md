---
{"title": "s390_pci_mmio_write(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/s390_pci_mmio_write.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# s390_pci_mmio_write(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    s390_pci_mmio_write(2)     System Calls Manual     s390_pci_mmio_write(2)

## [](#NAME)NAME

           s390_pci_mmio_write, s390_pci_mmio_read - transfer data to/from
           PCI MMIO memory page

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(size_t length;
                       SYS_s390_pci_mmio_write, unsigned long mmio_addr,
                       const void user_buffer[length], size_t length);
           int syscall(size_t length;
                       SYS_s390_pci_mmio_read, unsigned long mmio_addr,
                       void user_buffer[length], size_t length);

           Note: glibc provides no wrappers for these system calls,
           necessitating the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           The s390_pci_mmio_write() system call writes length bytes of data
           from the user-space buffer user_buffer to the PCI MMIO memory
           location specified by mmio_addr.  The s390_pci_mmio_read() system
           call reads length bytes of data from the PCI MMIO memory location
           specified by mmio_addr to the user-space buffer user_buffer.

           These system calls must be used instead of the simple assignment
           or data-transfer operations that are used to access the PCI MMIO
           memory areas mapped to user space on the Linux System z platform.
           The address specified by mmio_addr must belong to a PCI MMIO
           memory page mapping in the caller's address space, and the data
           being written or read must not cross a page boundary.  The length
           value cannot be greater than the system page size.

## [](#RETURN_VALUE)RETURN VALUE

           On success, s390_pci_mmio_write() and s390_pci_mmio_read() return
           0.  On failure, -1 is returned and errno is set to indicate the
           error.

## [](#ERRORS)ERRORS

           EFAULT The address in mmio_addr is invalid.

           EFAULT user_buffer does not point to a valid location in the
                  caller's address space.

           EINVAL Invalid length argument.

           ENODEV PCI support is not enabled.

           ENOMEM Insufficient memory.

## [](#STANDARDS)STANDARDS

           Linux on s390.

## [](#HISTORY)HISTORY

           Linux 3.19.  System z EC12.

## [](#SEE_ALSO)SEE ALSO

           syscall(2)

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

    Linux man-pages 6.19            2026-02-08         s390_pci_mmio_write(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html)

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
