---
{"title": "proc_vmstat(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_vmstat.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_vmstat(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_vmstat(5)             File Formats Manual             proc_vmstat(5)

## [](#NAME)NAME

           /proc/vmstat - virtual memory statistics

## [](#DESCRIPTION)DESCRIPTION

           /proc/vmstat (since Linux 2.6.0)
                  This file displays various virtual memory statistics.  Each
                  line of this file contains a single name-value pair,
                  delimited by white space.  Some lines are present only if
                  the kernel was configured with suitable options.  (In some
                  cases, the options required for particular files have
                  changed across kernel versions, so they are not listed
                  here.  Details can be found by consulting the kernel source
                  code.)  The following fields may be present:

                  nr_free_pages (since Linux 2.6.31)

                  nr_alloc_batch (since Linux 3.12)

                  nr_inactive_anon (since Linux 2.6.28)

                  nr_active_anon (since Linux 2.6.28)

                  nr_inactive_file (since Linux 2.6.28)

                  nr_active_file (since Linux 2.6.28)

                  nr_unevictable (since Linux 2.6.28)

                  nr_mlock (since Linux 2.6.28)

                  nr_anon_pages (since Linux 2.6.18)

                  nr_mapped (since Linux 2.6.0)

                  nr_file_pages (since Linux 2.6.18)

                  nr_dirty (since Linux 2.6.0)

                  nr_writeback (since Linux 2.6.0)

                  nr_slab_reclaimable (since Linux 2.6.19)

                  nr_slab_unreclaimable (since Linux 2.6.19)

                  nr_page_table_pages (since Linux 2.6.0)

                  nr_kernel_stack (since Linux 2.6.32)
                         Amount of memory allocated to kernel stacks.

                  nr_unstable (since Linux 2.6.0)

                  nr_bounce (since Linux 2.6.12)

                  nr_vmscan_write (since Linux 2.6.19)

                  nr_vmscan_immediate_reclaim (since Linux 3.2)

                  nr_writeback_temp (since Linux 2.6.26)

                  nr_isolated_anon (since Linux 2.6.32)

                  nr_isolated_file (since Linux 2.6.32)

                  nr_shmem (since Linux 2.6.32)
                         Pages used by shmem and tmpfs(5).

                  nr_dirtied (since Linux 2.6.37)

                  nr_written (since Linux 2.6.37)

                  nr_pages_scanned (since Linux 3.17)

                  numa_hit (since Linux 2.6.18)

                  numa_miss (since Linux 2.6.18)

                  numa_foreign (since Linux 2.6.18)

                  numa_interleave (since Linux 2.6.18)

                  numa_local (since Linux 2.6.18)

                  numa_other (since Linux 2.6.18)

                  workingset_refault (since Linux 3.15)

                  workingset_activate (since Linux 3.15)

                  workingset_nodereclaim (since Linux 3.15)

                  nr_anon_transparent_hugepages (since Linux 2.6.38)

                  nr_free_cma (since Linux 3.7)
                         Number of free CMA (Contiguous Memory Allocator)
                         pages.

                  nr_dirty_threshold (since Linux 2.6.37)

                  nr_dirty_background_threshold (since Linux 2.6.37)

                  pgpgin (since Linux 2.6.0)

                  pgpgout (since Linux 2.6.0)

                  pswpin (since Linux 2.6.0)

                  pswpout (since Linux 2.6.0)

                  pgalloc_dma (since Linux 2.6.5)

                  pgalloc_dma32 (since Linux 2.6.16)

                  pgalloc_normal (since Linux 2.6.5)

                  pgalloc_high (since Linux 2.6.5)

                  pgalloc_movable (since Linux 2.6.23)

                  pgfree (since Linux 2.6.0)

                  pgactivate (since Linux 2.6.0)

                  pgdeactivate (since Linux 2.6.0)

                  pgfault (since Linux 2.6.0)

                  pgmajfault (since Linux 2.6.0)

                  pgrefill_dma (since Linux 2.6.5)

                  pgrefill_dma32 (since Linux 2.6.16)

                  pgrefill_normal (since Linux 2.6.5)

                  pgrefill_high (since Linux 2.6.5)

                  pgrefill_movable (since Linux 2.6.23)

                  pgsteal_kswapd_dma (since Linux 3.4)

                  pgsteal_kswapd_dma32 (since Linux 3.4)

                  pgsteal_kswapd_normal (since Linux 3.4)

                  pgsteal_kswapd_high (since Linux 3.4)

                  pgsteal_kswapd_movable (since Linux 3.4)

                  pgsteal_direct_dma

                  pgsteal_direct_dma32 (since Linux 3.4)

                  pgsteal_direct_normal (since Linux 3.4)

                  pgsteal_direct_high (since Linux 3.4)

                  pgsteal_direct_movable (since Linux 2.6.23)

                  pgscan_kswapd_dma

                  pgscan_kswapd_dma32 (since Linux 2.6.16)

                  pgscan_kswapd_normal (since Linux 2.6.5)

                  pgscan_kswapd_high

                  pgscan_kswapd_movable (since Linux 2.6.23)

                  pgscan_direct_dma

                  pgscan_direct_dma32 (since Linux 2.6.16)

                  pgscan_direct_normal

                  pgscan_direct_high

                  pgscan_direct_movable (since Linux 2.6.23)

                  pgscan_direct_throttle (since Linux 3.6)

                  zone_reclaim_failed (since linux 2.6.31)

                  pginodesteal (since linux 2.6.0)

                  slabs_scanned (since linux 2.6.5)

                  kswapd_inodesteal (since linux 2.6.0)

                  kswapd_low_wmark_hit_quickly (since Linux 2.6.33)

                  kswapd_high_wmark_hit_quickly (since Linux 2.6.33)

                  pageoutrun (since Linux 2.6.0)

                  allocstall (since Linux 2.6.0)

                  pgrotated (since Linux 2.6.0)

                  drop_pagecache (since Linux 3.15)

                  drop_slab (since Linux 3.15)

                  numa_pte_updates (since Linux 3.8)

                  numa_huge_pte_updates (since Linux 3.13)

                  numa_hint_faults (since Linux 3.8)

                  numa_hint_faults_local (since Linux 3.8)

                  numa_pages_migrated (since Linux 3.8)

                  pgmigrate_success (since Linux 3.8)

                  pgmigrate_fail (since Linux 3.8)

                  compact_migrate_scanned (since Linux 3.8)

                  compact_free_scanned (since Linux 3.8)

                  compact_isolated (since Linux 3.8)

                  compact_stall (since Linux 2.6.35)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  compact_fail (since Linux 2.6.35)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  compact_success (since Linux 2.6.35)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  htlb_buddy_alloc_success (since Linux 2.6.26)

                  htlb_buddy_alloc_fail (since Linux 2.6.26)

                  unevictable_pgs_culled (since Linux 2.6.28)

                  unevictable_pgs_scanned (since Linux 2.6.28)

                  unevictable_pgs_rescued (since Linux 2.6.28)

                  unevictable_pgs_mlocked (since Linux 2.6.28)

                  unevictable_pgs_munlocked (since Linux 2.6.28)

                  unevictable_pgs_cleared (since Linux 2.6.28)

                  unevictable_pgs_stranded (since Linux 2.6.28)

                  thp_fault_alloc (since Linux 2.6.39)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  thp_fault_fallback (since Linux 2.6.39)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  thp_collapse_alloc (since Linux 2.6.39)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  thp_collapse_alloc_failed (since Linux 2.6.39)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  thp_split (since Linux 2.6.39)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  thp_zero_page_alloc (since Linux 3.8)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  thp_zero_page_alloc_failed (since Linux 3.8)
                         See the kernel source file
                         Documentation/admin-guide/mm/transhuge.rst.

                  balloon_inflate (since Linux 3.18)

                  balloon_deflate (since Linux 3.18)

                  balloon_migrate (since Linux 3.18)

                  nr_tlb_remote_flush (since Linux 3.12)

                  nr_tlb_remote_flush_received (since Linux 3.12)

                  nr_tlb_local_flush_all (since Linux 3.12)

                  nr_tlb_local_flush_one (since Linux 3.12)

                  vmacache_find_calls (since Linux 3.16)

                  vmacache_find_hits (since Linux 3.16)

                  vmacache_full_flushes (since Linux 3.19)

## [](#SEE_ALSO)SEE ALSO

           proc(5)

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

    Linux man-pages 6.19            2026-02-08                 proc_vmstat(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc(5)](../man5/proc.5.html)

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
