---
{"title": "numa(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/numa.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# numa(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    numa(7)              Miscellaneous Information Manual             numa(7)

## [](#NAME)NAME

           numa - overview of Non-Uniform Memory Architecture

## [](#DESCRIPTION)DESCRIPTION

           Non-Uniform Memory Access (NUMA) refers to multiprocessor systems
           whose memory is divided into multiple memory nodes.  The access
           time of a memory node depends on the relative locations of the
           accessing CPU and the accessed node.  (This contrasts with a
           symmetric multiprocessor system, where the access time for all of
           the memory is the same for all CPUs.)  Normally, each CPU on a
           NUMA system has a local memory node whose contents can be accessed
           faster than the memory in the node local to another CPU or the
           memory on a bus shared by all CPUs.

       NUMA system calls
           The Linux kernel implements the following NUMA-related system
           calls: get_mempolicy(2), mbind(2), migrate_pages(2),
           move_pages(2), and set_mempolicy(2).  However, applications should
           normally use the interface provided by libnuma; see "Library
           Support" below.

       [1m/proc/[24mpid/numa_maps (since Linux 2.6.14)
           This file displays information about a process's NUMA memory
           policy and allocation.

           Each line contains information about a memory range used by the
           process, displaying—among other information—the effective memory
           policy for that memory range and on which nodes the pages have
           been allocated.

           numa_maps is a read-only file.  When /proc/pid/numa_maps is read,
           the kernel will scan the virtual address space of the process and
           report how memory is used.  One line is displayed for each unique
           memory range of the process.

           The first field of each line shows the starting address of the
           memory range.  This field allows a correlation with the contents
           of the /proc/pid/maps file, which contains the end address of the
           range and other information, such as the access permissions and
           sharing.

           The second field shows the memory policy currently in effect for
           the memory range.  Note that the effective policy is not
           necessarily the policy installed by the process for that memory
           range.  Specifically, if the process installed a "default" policy
           for that range, the effective policy for that range will be the
           process policy, which may or may not be "default".

           The rest of the line contains information about the pages
           allocated in the memory range, as follows:

           N<node>=<nr_pages>
                  The number of pages allocated on <node>.  <nr_pages>
                  includes only pages currently mapped by the process.  Page
                  migration and memory reclaim may have temporarily unmapped
                  pages associated with this memory range.  These pages may
                  show up again only after the process has attempted to
                  reference them.  If the memory range represents a shared
                  memory area or file mapping, other processes may currently
                  have additional pages mapped in a corresponding memory
                  range.

           file=<filename>
                  The file backing the memory range.  If the file is mapped
                  as private, write accesses may have generated COW (Copy-On-
                  Write) pages in this memory range.  These pages are
                  displayed as anonymous pages.

           heap   Memory range is used for the heap.

           stack  Memory range is used for the stack.

           huge   Huge memory range.  The page counts shown are huge pages
                  and not regular sized pages.

           anon=<pages>
                  The number of anonymous page in the range.

           dirty=<pages>
                  Number of dirty pages.

           mapped=<pages>
                  Total number of mapped pages, if different from dirty and
                  anon pages.

           mapmax=<count>
                  Maximum mapcount (number of processes mapping a single
                  page) encountered during the scan.  This may be used as an
                  indicator of the degree of sharing occurring in a given
                  memory range.

           swapcache=<count>
                  Number of pages that have an associated entry on a swap
                  device.

           active=<pages>
                  The number of pages on the active list.  This field is
                  shown only if different from the number of pages in this
                  range.  This means that some inactive pages exist in the
                  memory range that may be removed from memory by the swapper
                  soon.

           writeback=<pages>
                  Number of pages that are currently being written out to
                  disk.

## [](#STANDARDS)STANDARDS

           None.

## [](#NOTES)NOTES

           The Linux NUMA system calls and /proc interface are available only
           if the kernel was configured and built with the CONFIG_NUMA
           option.

       Library support
           Link with -lnuma to get the system call definitions.  libnuma and
           the required <numaif.h> header are available in the numactl
           package.

           However, applications should not use these system calls directly.
           Instead, the higher level interface provided by the numa(3)
           functions in the numactl package is recommended.  The numactl
           package is available at
           ⟨ftp://oss.sgi.com/www/projects/libnuma/download/⟩.  The package
           is also included in some Linux distributions.  Some distributions
           include the development library and header in the separate
           numactl-devel package.

## [](#SEE_ALSO)SEE ALSO

           get_mempolicy(2), mbind(2), move_pages(2), set_mempolicy(2),
           numa(3), cpuset(7), numactl(8)

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

    Linux man-pages 6.19            2026-02-08                        numa(7)

------------------------------------------------------------------------

Pages that refer to this page: [get_mempolicy(2)](../man2/get_mempolicy.2.html),  [mbind(2)](../man2/mbind.2.html),  [migrate_pages(2)](../man2/migrate_pages.2.html),  [move_pages(2)](../man2/move_pages.2.html),  [set_mempolicy(2)](../man2/set_mempolicy.2.html),  [proc_pid_numa_maps(5)](../man5/proc_pid_numa_maps.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [cpuset(7)](../man7/cpuset.7.html)

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
