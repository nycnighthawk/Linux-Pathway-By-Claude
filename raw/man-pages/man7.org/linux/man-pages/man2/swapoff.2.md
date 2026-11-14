---
{"title": "swapon(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/swapoff.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# swapon(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    swapon(2)                  System Calls Manual                  swapon(2)

## [](#NAME)NAME

           swapon, swapoff - start/stop swapping to file/device

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/swap.h>

           int swapon(const char *path, int swapflags);
           int swapoff(const char *path);

## [](#DESCRIPTION)DESCRIPTION

           swapon() sets the swap area to the file or block device specified
           by path.  swapoff() stops swapping to the file or block device
           specified by path.

           If the SWAP_FLAG_PREFER flag is specified in the swapon()
           swapflags argument, the new swap area will have a higher priority
           than default.  The priority is encoded within swapflags as:

               (prio << SWAP_FLAG_PRIO_SHIFT) & SWAP_FLAG_PRIO_MASK

           If the SWAP_FLAG_DISCARD flag is specified in the swapon()
           swapflags argument, freed swap pages will be discarded before they
           are reused, if the swap device supports the discard or trim
           operation.  (This may improve performance on some Solid State
           Devices, but often it does not.)  See also NOTES.

           These functions may be used only by a privileged process (one
           having the CAP_SYS_ADMIN capability).

       Priority
           Each swap area has a priority, either high or low.  The default
           priority is low.  Within the low-priority areas, newer areas are
           even lower priority than older areas.

           All priorities set with swapflags are high-priority, higher than
           default.  They may have any nonnegative value chosen by the
           caller.  Higher numbers mean higher priority.

           Swap pages are allocated from areas in priority order, highest
           priority first.  For areas with different priorities, a higher-
           priority area is exhausted before using a lower-priority area.  If
           two or more areas have the same priority, and it is the highest
           priority available, pages are allocated on a round-robin basis
           between them.

           As of Linux 1.3.6, the kernel usually follows these rules, but
           there are exceptions.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EBUSY  (for swapon()) The specified path is already being used as
                  a swap area.

           EINVAL The file path exists, but refers neither to a regular file
                  nor to a block device;

           EINVAL (swapon()) The indicated path does not contain a valid swap
                  signature or resides on an in-memory filesystem such as
                  tmpfs(5).

           EINVAL (since Linux 3.4)
                  (swapon()) An invalid flag value was specified in
                  swapflags.

           EINVAL (swapoff()) path is not currently a swap area.

           ENFILE The system-wide limit on the total number of open files has
                  been reached.

           ENOENT The file path does not exist.

           ENOMEM The system has insufficient memory to start swapping.

           EPERM  The caller does not have the CAP_SYS_ADMIN capability.
                  Alternatively, the maximum number of swap files are already
                  in use; see NOTES below.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           The swapflags argument was introduced in Linux 1.3.2.

## [](#NOTES)NOTES

           The partition or path must be prepared with mkswap(8).

           There is an upper limit on the number of swap files that may be
           used, defined by the kernel constant MAX_SWAPFILES.  Before Linux
           2.4.10, MAX_SWAPFILES has the value 8; since Linux 2.4.10, it has
           the value 32.  Since Linux 2.6.18, the limit is decreased by 2
           (thus 30), since Linux 5.19, the limit is decreased by 3 (thus:
           29) if the kernel is built with the CONFIG_MIGRATION option (which
           reserves two swap table entries for the page migration features of
           mbind(2) and migrate_pages(2)).  Since Linux 2.6.32, the limit is
           further decreased by 1 if the kernel is built with the
           CONFIG_MEMORY_FAILURE option.  Since Linux 5.14, the limit is
           further decreased by 4 if the kernel is built with the
           CONFIG_DEVICE_PRIVATE option.  Since Linux 5.19, the limit is
           further decreased by 1 if the kernel is built with the
           CONFIG_PTE_MARKER option.

           Discard of swap pages was introduced in Linux 2.6.29, then made
           conditional on the SWAP_FLAG_DISCARD flag in Linux 2.6.36, which
           still discards the entire swap area when swapon() is called, even
           if that flag bit is not set.

## [](#SEE_ALSO)SEE ALSO

           mkswap(8), swapoff(8), swapon(8)

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

    Linux man-pages 6.19            2026-02-08                      swapon(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [swapon(8)](../man8/swapon.8.html)

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
