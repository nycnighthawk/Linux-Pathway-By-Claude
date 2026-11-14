---
{"title": "subpage_prot(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/subpage_prot.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# subpage_prot(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    subpage_prot(2)            System Calls Manual            subpage_prot(2)

## [](#NAME)NAME

           subpage_prot - define a subpage protection for an address range

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_subpage_prot, unsigned long addr, unsigned long size,
                       uint32_t *map);

           Note: glibc provides no wrapper for subpage_prot(), necessitating
           the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           The PowerPC-specific subpage_prot() system call provides the
           facility to control the access permissions on individual 4 kB
           subpages on systems configured with a page size of 64 kB.

           The protection map is applied to the memory pages in the region
           starting at addr and continuing for size bytes.  Both of these
           arguments must be aligned to a 64-kB boundary.

           The protection map is specified in the buffer pointed to by map.
           The map has 2 bits per 4 kB subpage; thus each 32-bit word
           specifies the protections of 16 4 kB subpages inside a 64 kB page
           (so, the number of 32-bit words pointed to by map should equate to
           the number of 64-kB pages specified by size).  Each 2-bit field in
           the protection map is either 0 to allow any access, 1 to prevent
           writes, or 2 or 3 to prevent all accesses.

## [](#RETURN_VALUE)RETURN VALUE

           On success, subpage_prot() returns 0.  Otherwise, one of the error
           codes specified below is returned.

## [](#ERRORS)ERRORS

           EFAULT The buffer referred to by map is not accessible.

           EINVAL The addr or size arguments are incorrect.  Both of these
                  arguments must be aligned to a multiple of the system page
                  size, and they must not refer to a region outside of the
                  address space of the process or to a region that consists
                  of huge pages.

           ENOMEM Out of memory.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.25 (PowerPC).

           The system call is provided only if the kernel is configured with
           CONFIG_PPC_64K_PAGES.

## [](#NOTES)NOTES

           Normal page protections (at the 64-kB page level) also apply; the
           subpage protection mechanism is an additional constraint, so
           putting 0 in a 2-bit field won't allow writes to a page that is
           otherwise write-protected.

       Rationale
           This system call is provided to assist writing emulators that
           operate using 64-kB pages on PowerPC systems.  When emulating
           systems such as x86, which uses a smaller page size, the emulator
           can no longer use the memory-management unit (MMU) and normal
           system calls for controlling page protections.  (The emulator
           could emulate the MMU by checking and possibly remapping the
           address for each memory access in software, but that is slow.)
           The idea is that the emulator supplies an array of protection
           masks to apply to a specified range of virtual addresses.  These
           masks are applied at the level where hardware page-table entries
           (PTEs) are inserted into the hardware page table based on the
           Linux PTEs, so the Linux PTEs are not affected.  Implicit in this
           is that the regions of the address space that are protected are
           switched to use 4-kB hardware pages rather than 64-kB hardware
           pages (on machines with hardware 64-kB page support).

## [](#SEE_ALSO)SEE ALSO

           mprotect(2), syscall(2)

           Documentation/admin-guide/mm/hugetlbpage.rst in the Linux kernel
           source tree

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

    Linux man-pages 6.19            2026-02-08                subpage_prot(2)

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
