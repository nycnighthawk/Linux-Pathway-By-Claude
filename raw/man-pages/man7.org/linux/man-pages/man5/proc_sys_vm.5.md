---
{"title": "proc_sys_vm(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_sys_vm.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_sys_vm(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_sys_vm(5)             File Formats Manual             proc_sys_vm(5)

## [](#NAME)NAME

           /proc/sys/vm/ - virtual memory subsystem

## [](#DESCRIPTION)DESCRIPTION

           /proc/sys/vm/
                  This directory contains files for memory management tuning,
                  buffer, and cache management.

           /proc/sys/vm/admin_reserve_kbytes (since Linux 3.10)
                  This file defines the amount of free memory (in KiB) on the
                  system that should be reserved for users with the
                  capability CAP_SYS_ADMIN.

                  The default value in this file is the minimum of [3% of
                  free pages, 8MiB] expressed as KiB.  The default is
                  intended to provide enough for the superuser to log in and
                  kill a process, if necessary, under the default overcommit
                  'guess' mode (i.e., 0 in /proc/sys/vm/overcommit_memory).

                  Systems running in "overcommit never" mode (i.e., 2 in
                  /proc/sys/vm/overcommit_memory) should increase the value
                  in this file to account for the full virtual memory size of
                  the programs used to recover (e.g., login(1) ssh(1), and
                  top(1)) Otherwise, the superuser may not be able to log in
                  to recover the system.  For example, on x86-64 a suitable
                  value is 131072 (128MiB reserved).

                  Changing the value in this file takes effect whenever an
                  application requests memory.

           /proc/sys/vm/compact_memory (since Linux 2.6.35)
                  When 1 is written to this file, all zones are compacted
                  such that free memory is available in contiguous blocks
                  where possible.  The effect of this action can be seen by
                  examining /proc/buddyinfo.

                  Present only if the kernel was configured with
                  CONFIG_COMPACTION.

           /proc/sys/vm/drop_caches (since Linux 2.6.16)
                  Writing to this file causes the kernel to drop clean
                  caches, dentries, and inodes from memory, causing that
                  memory to become free.  This can be useful for memory
                  management testing and performing reproducible filesystem
                  benchmarks.  Because writing to this file causes the
                  benefits of caching to be lost, it can degrade overall
                  system performance.

                  To free pagecache, use:

                      echo 1 > /proc/sys/vm/drop_caches

                  To free dentries and inodes, use:

                      echo 2 > /proc/sys/vm/drop_caches

                  To free pagecache, dentries, and inodes, use:

                      echo 3 > /proc/sys/vm/drop_caches

                  Because writing to this file is a nondestructive operation
                  and dirty objects are not freeable, the user should run
                  sync(1) first.

           /proc/sys/vm/hugetlb_shm_group (since Linux 2.6.7)
                  This writable file contains a group ID that is allowed to
                  allocate memory using huge pages.  If a process has a
                  filesystem group ID or any supplementary group ID that
                  matches this group ID, then it can make huge-page
                  allocations without holding the CAP_IPC_LOCK capability;
                  see memfd_create(2), mmap(2), and shmget(2).

           /proc/sys/vm/legacy_va_layout (since Linux 2.6.9)
                  If nonzero, this disables the new 32-bit memory-mapping
                  layout; the kernel will use the legacy (2.4) layout for all
                  processes.

           /proc/sys/vm/memory_failure_early_kill (since Linux 2.6.32)
                  Control how to kill processes when an uncorrected memory
                  error (typically a 2-bit error in a memory module) that
                  cannot be handled by the kernel is detected in the
                  background by hardware.  In some cases (like the page still
                  having a valid copy on disk), the kernel will handle the
                  failure transparently without affecting any applications.
                  But if there is no other up-to-date copy of the data, it
                  will kill processes to prevent any data corruptions from
                  propagating.

                  The file has one of the following values:

                  1      Kill all processes that have the corrupted-and-not-
                         reloadable page mapped as soon as the corruption is
                         detected.  Note that this is not supported for a few
                         types of pages, such as kernel internally allocated
                         data or the swap cache, but works for the majority
                         of user pages.

                  0      Unmap the corrupted page from all processes and kill
                         a process only if it tries to access the page.

                  The kill is performed using a SIGBUS signal with si_code
                  set to BUS_MCEERR_AO.  Processes can handle this if they
                  want to; see sigaction(2) for more details.

                  This feature is active only on architectures/platforms with
                  advanced machine check handling and depends on the hardware
                  capabilities.

                  Applications can override the memory_failure_early_kill
                  setting individually with the prctl(2) PR_MCE_KILL
                  operation.

                  Present only if the kernel was configured with
                  CONFIG_MEMORY_FAILURE.

           /proc/sys/vm/memory_failure_recovery (since Linux 2.6.32)
                  Enable memory failure recovery (when supported by the
                  platform).

                  1      Attempt recovery.

                  0      Always panic on a memory failure.

                  Present only if the kernel was configured with
                  CONFIG_MEMORY_FAILURE.

           /proc/sys/vm/oom_dump_tasks (since Linux 2.6.25)
                  Enables a system-wide task dump (excluding kernel threads)
                  to be produced when the kernel performs an OOM-killing.
                  The dump includes the following information for each task
                  (thread, process): thread ID, real user ID, thread group ID
                  (process ID), virtual memory size, resident set size, the
                  CPU that the task is scheduled on, oom_adj score (see the
                  description of /proc/pid/oom_adj), and command name.  This
                  is helpful to determine why the OOM-killer was invoked and
                  to identify the rogue task that caused it.

                  If this contains the value zero, this information is
                  suppressed.  On very large systems with thousands of tasks,
                  it may not be feasible to dump the memory state information
                  for each one.  Such systems should not be forced to incur a
                  performance penalty in OOM situations when the information
                  may not be desired.

                  If this is set to nonzero, this information is shown
                  whenever the OOM-killer actually kills a memory-hogging
                  task.

                  The default value is 0.

           /proc/sys/vm/oom_kill_allocating_task (since Linux 2.6.24)
                  This enables or disables killing the OOM-triggering task in
                  out-of-memory situations.

                  If this is set to zero, the OOM-killer will scan through
                  the entire tasklist and select a task based on heuristics
                  to kill.  This normally selects a rogue memory-hogging task
                  that frees up a large amount of memory when killed.

                  If this is set to nonzero, the OOM-killer simply kills the
                  task that triggered the out-of-memory condition.  This
                  avoids a possibly expensive tasklist scan.

                  If /proc/sys/vm/panic_on_oom is nonzero, it takes
                  precedence over whatever value is used in
                  /proc/sys/vm/oom_kill_allocating_task.

                  The default value is 0.

           /proc/sys/vm/overcommit_kbytes (since Linux 3.14)
                  This writable file provides an alternative to
                  /proc/sys/vm/overcommit_ratio for controlling the
                  CommitLimit when /proc/sys/vm/overcommit_memory has the
                  value 2.  It allows the amount of memory overcommitting to
                  be specified as an absolute value (in kB), rather than as a
                  percentage, as is done with overcommit_ratio.  This allows
                  for finer-grained control of CommitLimit on systems with
                  extremely large memory sizes.

                  Only one of overcommit_kbytes or overcommit_ratio can have
                  an effect: if overcommit_kbytes has a nonzero value, then
                  it is used to calculate CommitLimit, otherwise
                  overcommit_ratio is used.  Writing a value to either of
                  these files causes the value in the other file to be set to
                  zero.

           /proc/sys/vm/overcommit_memory
                  This file contains the kernel virtual memory accounting
                  mode.  Values are:

                         0: heuristic overcommit (this is the default)
                         1: always overcommit, never check
                         2: always check, never overcommit

                  In mode 0, calls of mmap(2) with MAP_NORESERVE are not
                  checked, and the default check is very weak, leading to the
                  risk of getting a process "OOM-killed".

                  In mode 1, the kernel pretends there is always enough
                  memory, until memory actually runs out.  One use case for
                  this mode is scientific computing applications that employ
                  large sparse arrays.  Before Linux 2.6.0, any nonzero value
                  implies mode 1.

                  In mode 2 (available since Linux 2.6), the total virtual
                  address space that can be allocated (CommitLimit in
                  /proc/meminfo) is calculated as

                      CommitLimit = (total_RAM - total_huge_TLB) *
                                 overcommit_ratio / 100 + total_swap

                  where:

                  •  total_RAM is the total amount of RAM on the system;

                  •  total_huge_TLB is the amount of memory set aside for
                     huge pages;

                  •  overcommit_ratio is the value in
                     /proc/sys/vm/overcommit_ratio; and

                  •  total_swap is the amount of swap space.

                  For example, on a system with 16 GB of physical RAM, 16 GB
                  of swap, no space dedicated to huge pages, and an
                  overcommit_ratio of 50, this formula yields a CommitLimit
                  of 24 GB.

                  Since Linux 3.14, if the value in
                  /proc/sys/vm/overcommit_kbytes is nonzero, then CommitLimit
                  is instead calculated as:

                      CommitLimit = overcommit_kbytes + total_swap

                  See also the description of
                  /proc/sys/vm/admin_reserve_kbytes and
                  /proc/sys/vm/user_reserve_kbytes.

           /proc/sys/vm/overcommit_ratio (since Linux 2.6.0)
                  This writable file defines a percentage by which memory can
                  be overcommitted.  The default value in the file is 50.
                  See the description of /proc/sys/vm/overcommit_memory.

           /proc/sys/vm/panic_on_oom (since Linux 2.6.18)
                  This enables or disables a kernel panic in an out-of-memory
                  situation.

                  If this file is set to the value 0, the kernel's OOM-killer
                  will kill some rogue process.  Usually, the OOM-killer is
                  able to kill a rogue process and the system will survive.

                  If this file is set to the value 1, then the kernel
                  normally panics when out-of-memory happens.  However, if a
                  process limits allocations to certain nodes using memory
                  policies (mbind(2) MPOL_BIND) or cpusets (cpuset(7)) and
                  those nodes reach memory exhaustion status, one process may
                  be killed by the OOM-killer.  No panic occurs in this case:
                  because other nodes' memory may be free, this means the
                  system as a whole may not have reached an out-of-memory
                  situation yet.

                  If this file is set to the value 2, the kernel always
                  panics when an out-of-memory condition occurs.

                  The default value is 0.  1 and 2 are for failover of
                  clustering.  Select either according to your policy of
                  failover.

           /proc/sys/vm/swappiness
                  The value in this file controls how aggressively the kernel
                  will swap memory pages.  Higher values increase
                  aggressiveness, lower values decrease aggressiveness.  The
                  default value is 60.

           /proc/sys/vm/user_reserve_kbytes (since Linux 3.10)
                  Specifies an amount of memory (in KiB) to reserve for user
                  processes.  This is intended to prevent a user from
                  starting a single memory hogging process, such that they
                  cannot recover (kill the hog).  The value in this file has
                  an effect only when /proc/sys/vm/overcommit_memory is set
                  to 2 ("overcommit never" mode).  In this case, the system
                  reserves an amount of memory that is the minimum of [3% of
                  current process size, user_reserve_kbytes].

                  The default value in this file is the minimum of [3% of
                  free pages, 128MiB] expressed as KiB.

                  If the value in this file is set to zero, then a user will
                  be allowed to allocate all free memory with a single
                  process (minus the amount reserved by
                  /proc/sys/vm/admin_reserve_kbytes).  Any subsequent
                  attempts to execute a command will result in "fork: Cannot
                  allocate memory".

                  Changing the value in this file takes effect whenever an
                  application requests memory.

           /proc/sys/vm/unprivileged_userfaultfd (since Linux 5.2)
                  This (writable) file exposes a flag that controls whether
                  unprivileged processes are allowed to employ
                  userfaultfd(2).  If this file has the value 1, then
                  unprivileged processes may use userfaultfd(2).  If this
                  file has the value 0, then only processes that have the
                  CAP_SYS_PTRACE capability may employ userfaultfd(2).  The
                  default value in this file is 1.

## [](#SEE_ALSO)SEE ALSO

           proc(5), proc_sys(5)

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

    Linux man-pages 6.19            2026-02-08                 proc_sys_vm(5)

------------------------------------------------------------------------

Pages that refer to this page: [memfd_create(2)](../man2/memfd_create.2.html),  [mmap(2)](../man2/mmap.2.html),  [PR_MCE_KILL_CLEAR(2const)](../man2/PR_MCE_KILL_CLEAR.2const.html),  [shmget(2)](../man2/shmget.2.html),  [proc_sys(5)](../man5/proc_sys.5.html)

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
