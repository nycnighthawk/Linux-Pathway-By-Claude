---
{"title": "get_mempolicy(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/get_mempolicy.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# get_mempolicy(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    get_mempolicy(2)           System Calls Manual           get_mempolicy(2)

## [](#NAME)NAME

           get_mempolicy - retrieve NUMA memory policy for a thread

## [](#LIBRARY)LIBRARY

           NUMA (Non-Uniform Memory Access) policy library (libnuma, -lnuma)

## [](#SYNOPSIS)SYNOPSIS

           #include <numaif.h>

           long get_mempolicy(unsigned long maxnode;
                              int *mode,
                              unsigned long nodemask[(maxnode + ULONG_WIDTH - 1)
                                                     / ULONG_WIDTH],
                              unsigned long maxnode, void *addr,
                              unsigned long flags);

## [](#DESCRIPTION)DESCRIPTION

           get_mempolicy() retrieves the NUMA policy of the calling thread or
           of a memory address, depending on the setting of flags.

           A NUMA machine has different memory controllers with different
           distances to specific CPUs.  The memory policy defines from which
           node memory is allocated for the thread.

           If flags is specified as 0, then information about the calling
           thread's default policy (as set by set_mempolicy(2)) is returned,
           in the buffers pointed to by mode and nodemask.  The value
           returned in these arguments may be used to restore the thread's
           policy to its state at the time of the call to get_mempolicy()
           using set_mempolicy(2).  When flags is 0, addr must be specified
           as NULL.

           If flags specifies MPOL_F_MEMS_ALLOWED (available since Linux
           2.6.24), the mode argument is ignored and the set of nodes
           (memories) that the thread is allowed to specify in subsequent
           calls to mbind(2) or set_mempolicy(2) (in the absence of any mode
           flags) is returned in nodemask.  It is not permitted to combine
           MPOL_F_MEMS_ALLOWED with either MPOL_F_ADDR or MPOL_F_NODE.

           If flags specifies MPOL_F_ADDR, then information is returned about
           the policy governing the memory address given in addr.  This
           policy may be different from the thread's default policy if
           mbind(2) or one of the helper functions described in numa(3) has
           been used to establish a policy for the memory range containing
           addr.

           If the mode argument is not NULL, then get_mempolicy() will store
           the policy mode and any optional mode flags of the requested NUMA
           policy in the location pointed to by this argument.  If nodemask
           is not NULL, then the nodemask associated with the policy will be
           stored in the location pointed to by this argument.  maxnode
           specifies the number of node IDs that can be stored into nodemask—
           that is, the maximum node ID plus one.  The value specified by
           maxnode is always rounded to a multiple of
           sizeof(unsigned long)*8.

           If flags specifies both MPOL_F_NODE and MPOL_F_ADDR,
           get_mempolicy() will return the node ID of the node on which the
           address addr is allocated into the location pointed to by mode.
           If no page has yet been allocated for the specified address,
           get_mempolicy() will allocate a page as if the thread had
           performed a read (load) access to that address, and return the ID
           of the node where that page was allocated.

           If flags specifies MPOL_F_NODE, but not MPOL_F_ADDR, and the
           thread's current policy is MPOL_INTERLEAVE or
           MPOL_WEIGHTED_INTERLEAVE, then get_mempolicy() will return in the
           location pointed to by a non-NULL mode argument, the node ID of
           the next node that will be used for interleaving of internal
           kernel pages allocated on behalf of the thread.  These allocations
           include pages for memory-mapped files in process memory ranges
           mapped using the mmap(2) call with the MAP_PRIVATE flag for read
           accesses, and in memory ranges mapped with the MAP_SHARED flag for
           all accesses.

           Other flag values are reserved.

           For an overview of the possible policies see set_mempolicy(2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, get_mempolicy() returns 0; on error, -1 is returned
           and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Part of all of the memory range specified by nodemask and
                  maxnode points outside your accessible address space.

           EINVAL The value specified by maxnode is less than the number of
                  node IDs supported by the system.  Or flags specified
                  values other than MPOL_F_NODE or MPOL_F_ADDR; or flags
                  specified MPOL_F_ADDR and addr is NULL, or flags did not
                  specify MPOL_F_ADDR and addr is not NULL.  Or, flags
                  specified MPOL_F_NODE but not MPOL_F_ADDR and the current
                  thread policy is neither MPOL_INTERLEAVE nor
                  MPOL_WEIGHTED_INTERLEAVE.  Or, flags specified
                  MPOL_F_MEMS_ALLOWED with either MPOL_F_ADDR or MPOL_F_NODE.
                  (And there are other EINVAL cases.)

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.7.

## [](#NOTES)NOTES

           For information on library support, see numa(7).

## [](#SEE_ALSO)SEE ALSO

           getcpu(2), mbind(2), mmap(2), set_mempolicy(2), numa(3), numa(7),
           numactl(8)

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

    Linux man-pages 6.19            2026-02-08               get_mempolicy(2)

------------------------------------------------------------------------

Pages that refer to this page: [mbind(2)](../man2/mbind.2.html),  [migrate_pages(2)](../man2/migrate_pages.2.html),  [move_pages(2)](../man2/move_pages.2.html),  [set_mempolicy(2)](../man2/set_mempolicy.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [numa(3)](../man3/numa.3.html),  [cpuset(7)](../man7/cpuset.7.html),  [numa(7)](../man7/numa.7.html),  [migratepages(8)](../man8/migratepages.8.html),  [numactl(8)](../man8/numactl.8.html)

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
