---
{"title": "proc_pid_smaps(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_smaps.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_smaps(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_smaps(5)          File Formats Manual          proc_pid_smaps(5)

## [](#NAME)NAME

           /proc/pid/smaps - XXX: What does 's' in "smaps" stand for?

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/smaps (since Linux 2.6.14)
                  This file shows memory consumption for each of the
                  process's mappings.  (The pmap(1) command displays similar
                  information, in a form that may be easier for parsing.)
                  For each mapping there is a series of lines such as the
                  following:

                      00400000-0048a000 r-xp 00000000 fd:03 960637       /bin/bash
                      Size:                552 kB
                      Rss:                 460 kB
                      Pss:                 100 kB
                      Shared_Clean:        452 kB
                      Shared_Dirty:          0 kB
                      Private_Clean:         8 kB
                      Private_Dirty:         0 kB
                      Referenced:          460 kB
                      Anonymous:             0 kB
                      AnonHugePages:         0 kB
                      ShmemHugePages:        0 kB
                      ShmemPmdMapped:        0 kB
                      Swap:                  0 kB
                      KernelPageSize:        4 kB
                      MMUPageSize:           4 kB
                      Locked:                0 kB
                      ProtectionKey:         0
                      VmFlags: rd ex mr mw me dw

                  The first of these lines shows the same information as is
                  displayed for the mapping in /proc/pid/maps.  The following
                  lines show the size of the mapping, the amount of the
                  mapping that is currently resident in RAM ("Rss"), the
                  process's proportional share of this mapping ("Pss"), the
                  number of clean and dirty shared pages in the mapping, and
                  the number of clean and dirty private pages in the mapping.
                  "Referenced" indicates the amount of memory currently
                  marked as referenced or accessed.  "Anonymous" shows the
                  amount of memory that does not belong to any file.  "Swap"
                  shows how much would-be-anonymous memory is also used, but
                  out on swap.

                  The "KernelPageSize" line (available since Linux 2.6.29) is
                  the page size used by the kernel to back the virtual memory
                  area.  This matches the size used by the MMU in the
                  majority of cases.  However, one counter-example occurs on
                  PPC64 kernels whereby a kernel using 64 kB as a base page
                  size may still use 4 kB pages for the MMU on older
                  processors.  To distinguish the two attributes, the
                  "MMUPageSize" line (also available since Linux 2.6.29)
                  reports the page size used by the MMU.

                  The "Locked" indicates whether the mapping is locked in
                  memory or not.

                  The "ProtectionKey" line (available since Linux 4.9, on x86
                  only) contains the memory protection key (see pkeys(7))
                  associated with the virtual memory area.  This entry is
                  present only if the kernel was built with the
                  CONFIG_X86_INTEL_MEMORY_PROTECTION_KEYS configuration
                  option (since Linux 4.6).

                  The "VmFlags" line (available since Linux 3.8) represents
                  the kernel flags associated with the virtual memory area,
                  encoded using the following two-letter codes:

                         rd   readable
                         wr   writable
                         ex   executable
                         sh   shared
                         mr   may read
                         mw   may write
                         me   may execute
                         ms   may share
                         gd   stack segment grows down
                         pf   pure PFN range
                         dw   disabled write to the mapped file
                         lo   pages are locked in memory
                         io   memory mapped I/O area
                         sr   sequential read advise provided
                         rr   random read advise provided
                         dc   do not copy area on fork
                         de   do not expand area on remapping
                         ac   area is accountable
                         nr   swap space is not reserved for the area
                         ht   area uses huge tlb pages
                         sf   perform synchronous page faults (since Linux 4.15)
                         nl   non-linear mapping (removed in Linux 4.0)
                         ar   architecture specific flag
                         wf   wipe on fork (since Linux 4.14)
                         dd   do not include area into core dump
                         sd   soft-dirty flag (since Linux 3.13)
                         mm   mixed map area
                         hg   huge page advise flag
                         nh   no-huge page advise flag
                         mg   mergeable advise flag
                         um   userfaultfd missing pages tracking (since Linux 4.3)
                         uw   userfaultfd wprotect pages tracking (since Linux 4.3)

                  The /proc/pid/smaps file is present only if the
                  CONFIG_PROC_PAGE_MONITOR kernel configuration option is
                  enabled.

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

    Linux man-pages 6.19            2026-02-08              proc_pid_smaps(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc_pid(5)](../man5/proc_pid.5.html)

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
