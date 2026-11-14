---
{"title": "set_mempolicy(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/set_mempolicy.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# set_mempolicy(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    set_mempolicy(2)           System Calls Manual           set_mempolicy(2)

## [](#NAME)NAME

           set_mempolicy - set default NUMA memory policy for a thread and
           its children

## [](#LIBRARY)LIBRARY

           NUMA (Non-Uniform Memory Access) policy library (libnuma, -lnuma)

## [](#SYNOPSIS)SYNOPSIS

           #include <numaif.h>

           long set_mempolicy(int mode, const unsigned long *nodemask,
                              unsigned long maxnode);

## [](#DESCRIPTION)DESCRIPTION

           set_mempolicy() sets the NUMA memory policy of the calling thread,
           which consists of a policy mode and zero or more nodes, to the
           values specified by the mode, nodemask, and maxnode arguments.

           A NUMA machine has different memory controllers with different
           distances to specific CPUs.  The memory policy defines from which
           node memory is allocated for the thread.

           This system call defines the default policy for the thread.  The
           thread policy governs allocation of pages in the process's address
           space outside of memory ranges controlled by a more specific
           policy set by mbind(2).  The thread default policy also controls
           allocation of any pages for memory-mapped files mapped using the
           mmap(2) call with the MAP_PRIVATE flag and that are only read
           (loaded) from by the thread and of memory-mapped files mapped
           using the mmap(2) call with the MAP_SHARED flag, regardless of the
           access type.  The policy is applied only when a new page is
           allocated for the thread.  For anonymous memory this is when the
           page is first touched by the thread.

           The mode argument must specify one of MPOL_DEFAULT, MPOL_BIND,
           MPOL_INTERLEAVE, MPOL_WEIGHTED_INTERLEAVE, MPOL_PREFERRED,
           MPOL_PREFERRED_MANY, or MPOL_LOCAL (which are described in detail
           below).  All modes except MPOL_DEFAULT require the caller to
           specify the node or nodes to which the mode applies, via the
           nodemask argument.

           The mode argument may also include an optional mode flag.  The
           supported mode flags are:

           MPOL_F_NUMA_BALANCING (since Linux 5.12)
                  When mode is MPOL_BIND, enable the kernel NUMA balancing
                  for the task if it is supported by the kernel.  If the flag
                  isn't supported by the kernel, or is used with mode other
                  than MPOL_BIND, -1 is returned and errno is set to EINVAL.

           MPOL_F_RELATIVE_NODES (since Linux 2.6.26)
                  A nonempty nodemask specifies node IDs that are relative to
                  the set of node IDs allowed by the process's current
                  cpuset.

           MPOL_F_STATIC_NODES (since Linux 2.6.26)
                  A nonempty nodemask specifies physical node IDs.  Linux
                  will not remap the nodemask when the process moves to a
                  different cpuset context, nor when the set of nodes allowed
                  by the process's current cpuset context changes.

           nodemask points to a bit mask of node IDs that contains up to
           maxnode bits.  The bit mask size is rounded to the next multiple
           of sizeof(unsigned long), but the kernel will use bits only up to
           maxnode.  A NULL value of nodemask or a maxnode value of zero
           specifies the empty set of nodes.  If the value of maxnode is
           zero, the nodemask argument is ignored.

           Where a nodemask is required, it must contain at least one node
           that is on-line, allowed by the process's current cpuset context,
           (unless the MPOL_F_STATIC_NODES mode flag is specified), and
           contains memory.  If the MPOL_F_STATIC_NODES is set in mode and a
           required nodemask contains no nodes that are allowed by the
           process's current cpuset context, the memory policy reverts to
           local allocation.  This effectively overrides the specified policy
           until the process's cpuset context includes one or more of the
           nodes specified by nodemask.

           The mode argument must include one of the following values:

           MPOL_DEFAULT
                  This mode specifies that any nondefault thread memory
                  policy be removed, so that the memory policy "falls back"
                  to the system default policy.  The system default policy is
                  "local allocation"—that is, allocate memory on the node of
                  the CPU that triggered the allocation.  nodemask must be
                  specified as NULL.  If the "local node" contains no free
                  memory, the system will attempt to allocate memory from a
                  "near by" node.

           MPOL_BIND
                  This mode defines a strict policy that restricts memory
                  allocation to the nodes specified in nodemask.  If nodemask
                  specifies more than one node, page allocations will come
                  from the node with the lowest numeric node ID first, until
                  that node contains no free memory.  Allocations will then
                  come from the node with the next highest node ID specified
                  in nodemask and so forth, until none of the specified nodes
                  contain free memory.  Pages will not be allocated from any
                  node not specified in the nodemask.

           MPOL_INTERLEAVE
                  This mode interleaves page allocations across the nodes
                  specified in nodemask in numeric node ID order.  This
                  optimizes for bandwidth instead of latency by spreading out
                  pages and memory accesses to those pages across multiple
                  nodes.  However, accesses to a single page will still be
                  limited to the memory bandwidth of a single node.

           MPOL_WEIGHTED_INTERLEAVE (since Linux 6.9)
                  This mode interleaves page allocations across the nodes
                  specified in nodemask according to the weights in
                  /sys/kernel/mm/mempolicy/weighted_interleave.  For example,
                  if bits 0, 2, and 5 are set in nodemask, and the contents
                  of /sys/kernel/mm/mempolicy/weighted_interleave/node0,
                  /sys/.../node2, and /sys/.../node5 are 4, 7, and 9,
                  respectively, then pages in this region will be allocated
                  on nodes 0, 2, and 5 in a 4:7:9 ratio.

           MPOL_PREFERRED
                  This mode sets the preferred node for allocation.  The
                  kernel will try to allocate pages from this node first and
                  fall back to "near by" nodes if the preferred node is low
                  on free memory.  If nodemask specifies more than one node
                  ID, the first node in the mask will be selected as the
                  preferred node.  If the nodemask and maxnode arguments
                  specify the empty set, then the policy specifies "local
                  allocation" (like the system default policy discussed
                  above).

           MPOL_PREFERRED_MANY (since Linux 5.15)
                  This mode specifies a preference for nodes from which the
                  kernel will try to allocate from.  This differs from
                  MPOL_PREFERRED in that it accepts a set of nodes versus a
                  single node.  This policy is intended to benefit page
                  allocations where specific memory types (i.e., non-
                  volatile, high-bandwidth, or accelerator memory) are of
                  greater importance than node location.

           MPOL_LOCAL (since Linux 3.8)
                  This mode specifies "local allocation"; the memory is
                  allocated on the node of the CPU that triggered the
                  allocation (the "local node").  The nodemask and maxnode
                  arguments must specify the empty set.  If the "local node"
                  is low on free memory, the kernel will try to allocate
                  memory from other nodes.  The kernel will allocate memory
                  from the "local node" whenever memory for this node is
                  available.  If the "local node" is not allowed by the
                  process's current cpuset context, the kernel will try to
                  allocate memory from other nodes.  The kernel will allocate
                  memory from the "local node" whenever it becomes allowed by
                  the process's current cpuset context.

           The thread memory policy is preserved across an execve(2), and is
           inherited by child threads created using fork(2) or clone(2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, set_mempolicy() returns 0; on error, -1 is returned
           and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Part of all of the memory range specified by nodemask and
                  maxnode points outside your accessible address space.

           EINVAL mode is invalid.  Or, mode is MPOL_DEFAULT and nodemask is
                  nonempty, or mode is MPOL_BIND or MPOL_INTERLEAVE and
                  nodemask is empty.  Or, maxnode specifies more than a page
                  worth of bits.  Or, nodemask specifies one or more node IDs
                  that are greater than the maximum supported node ID.  Or,
                  none of the node IDs specified by nodemask are on-line and
                  allowed by the process's current cpuset context, or none of
                  the specified nodes contain memory.  Or, the mode argument
                  specified both MPOL_F_STATIC_NODES and
                  MPOL_F_RELATIVE_NODES.  Or, the MPOL_F_NUMA_BALANCING isn't
                  supported by the kernel, or is used with mode other than
                  MPOL_BIND.

           ENOMEM Insufficient kernel memory was available.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.7.

## [](#NOTES)NOTES

           Memory policy is not remembered if the page is swapped out.  When
           such a page is paged back in, it will use the policy of the thread
           or memory range that is in effect at the time the page is
           allocated.

           For information on library support, see numa(7).

## [](#SEE_ALSO)SEE ALSO

           get_mempolicy(2), getcpu(2), mbind(2), mmap(2), numa(3),
           cpuset(7), numa(7), numactl(8)

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

    Linux man-pages 6.19            2026-02-08               set_mempolicy(2)

------------------------------------------------------------------------

Pages that refer to this page: [getcpu(2)](../man2/getcpu.2.html),  [get_mempolicy(2)](../man2/get_mempolicy.2.html),  [mbind(2)](../man2/mbind.2.html),  [migrate_pages(2)](../man2/migrate_pages.2.html),  [move_pages(2)](../man2/move_pages.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [numa(3)](../man3/numa.3.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [tmpfs(5)](../man5/tmpfs.5.html),  [cpuset(7)](../man7/cpuset.7.html),  [numa(7)](../man7/numa.7.html),  [migratepages(8)](../man8/migratepages.8.html),  [numactl(8)](../man8/numactl.8.html)

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
