---
{"title": "vmstat(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/vmstat.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# vmstat(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FIELD DESCRIPTION FOR VM MODE](#FIELD_DESCRIPTION_FOR_VM_MODE) \| [FIELD DESCRIPTION FOR DISK MODE](#FIELD_DESCRIPTION_FOR_DISK_MODE) \| [FIELD DESCRIPTION FOR DISK PARTITION MODE](#FIELD_DESCRIPTION_FOR_DISK_PARTITION_MODE) \| [FIELD DESCRIPTION FOR SLAB MODE](#FIELD_DESCRIPTION_FOR_SLAB_MODE) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    VMSTAT(8)                System Manager's Manual                VMSTAT(8)

## [](#NAME)NAME

           vmstat - Report virtual memory statistics

## [](#SYNOPSIS)SYNOPSIS

           vmstat [option ...] [delay [count]]

## [](#DESCRIPTION)DESCRIPTION

           vmstat reports information about processes, memory, paging, block
           IO, traps, disks and cpu activity.

           The first report produced gives averages since the last reboot.
           Additional reports give information on a sampling period of length
           delay.  The process and memory reports are instantaneous in either
           case.

## [](#OPTIONS)OPTIONS

           delay  The delay between updates in seconds.  If no delay is
                  specified, only one report is printed with the average
                  values since boot.

           count  Number of updates.  In absence of count, when delay is
                  defined, default is infinite.

           -a, --active
                  Display active and  inactive memory, given a 2.5.41 kernel
                  or better.

           -f, --forks
                  The -f switch displays the number of forks since boot.
                  This includes the fork, vfork, and clone system calls, and
                  is equivalent to the total number of tasks created.  Each
                  process is represented by one or more tasks, depending on
                  thread usage.  This display does not repeat.

           -m, --slabs
                  Displays slabinfo.

           -n, --one-header
                  Display the header only once rather than periodically.

           -s, --stats
                  Displays a table of various event counters and memory
                  statistics.  This display does not repeat.

           -d, --disk
                  Report disk statistics (2.5.70 or above required).

           -D, --disk-sum
                  Report some summary statistics about disk activity.

           -p, --partition device
                  Detailed statistics about partition (2.5.70 or above
                  required).

           -S, --unit character
                  Switches outputs between 1000 (k), 1024 (K), 1000000 (m),
                  or 1048576 (M) bytes.  Note this does not change the block
                  (bi/bo) fields.

           -t, --timestamp
                  Append timestamp to each line

           -w, --wide
                  Wide output mode (useful for systems with higher amount of
                  memory, where the default output mode suffers from unwanted
                  column breakage).  The output is wider than 80 characters
                  per line.

           -y, --no-first
                  Omits first report with statistics since system boot.

           -V, --version
                  Display version information and exit.

           -h, --help
                  Display help and exit.

## [](#FIELD_DESCRIPTION_FOR_VM_MODE)FIELD DESCRIPTION FOR VM MODE

       Procs
           r: The number of runnable processes (running or waiting for run time).
           b: The number of processes blocked waiting for I/O to complete.

       Memory
           These are affected by the --unit option.
           swpd: the amount of swap memory used.
           free: the amount of idle memory.
           buff: the amount of memory used as buffers.
           cache: the amount of memory used as cache.
           inact: the amount of inactive memory.  (-a option)
           active: the amount of active memory.  (-a option)

       Swap
           These are affected by the --unit option.
           si: Amount of memory swapped in from disk (/s).
           so: Amount of memory swapped to disk (/s).

       IO
           bi: Kibibyte received from a block device (KiB/s).
           bo: Kibibyte sent to a block device (KiB/s).

       System
           in: The number of interrupts per second, including the clock.
           cs: The number of context switches per second.

       CPU
           These are percentages of total CPU time.
           us: Time spent running non-kernel code.  (user time, including nice time)
           sy: Time spent running kernel code.  (system time)
           id: Time spent idle.  Prior to Linux 2.5.41, this includes IO-wait time.
           wa: Time spent waiting for IO.  Prior to Linux 2.5.41, included in idle.
           st: Time stolen from a virtual machine.  Prior to Linux 2.6.11, unknown.
           gu: Time spent running KVM guest code (guest time, including guest nice).

## [](#FIELD_DESCRIPTION_FOR_DISK_MODE)FIELD DESCRIPTION FOR DISK MODE

       Reads
           total: Total reads completed successfully
           merged: grouped reads (resulting in one I/O)
           sectors: Sectors read successfully
           ms: milliseconds spent reading

       Writes
           total: Total writes completed successfully
           merged: grouped writes (resulting in one I/O)
           sectors: Sectors written successfully
           ms: milliseconds spent writing

       IO
           cur: I/O in progress
           s: seconds spent for I/O

## [](#FIELD_DESCRIPTION_FOR_DISK_PARTITION_MODE)FIELD DESCRIPTION FOR DISK PARTITION MODE

           reads: Total number of reads issued to this partition
           read sectors: Total read sectors for partition
           writes : Total number of writes issued to this partition
           requested writes: Total number of write requests made for partition

## [](#FIELD_DESCRIPTION_FOR_SLAB_MODE)FIELD DESCRIPTION FOR SLAB MODE

           Slab mode shows statistics per slab, for more information about
           this information see slabinfo(5)

           cache: Cache name
           num: Number of currently active objects
           total: Total number of available objects
           size: Size of each object
           pages: Number of pages with at least one active object

## [](#NOTES)NOTES

           vmstat requires read access to files under /proc. The -m requires
           read access to /proc/slabinfo which may not be available to
           standard users.  Mount options for /proc such as subset=pid may
           also impact what is visible.

## [](#SEE_ALSO)SEE ALSO

           free(1), iostat(1), mpstat(1), ps(1), sar(1), top(1), slabinfo(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           Please send bug reports to ⟨procps@freelists.org⟩.

## [](#COLOPHON)COLOPHON

           This page is part of the procps-ng (/proc filesystem utilities)
           project.  Information about the project can be found at 
           ⟨https://gitlab.com/procps-ng/procps⟩.  If you have a bug report
           for this manual page, see
           ⟨https://gitlab.com/procps-ng/procps/blob/master/Documentation/bugs.md⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/procps-ng/procps.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    procps-ng                       2024-07-19                      VMSTAT(8)

------------------------------------------------------------------------

Pages that refer to this page: [cifsiostat(1)](../man1/cifsiostat.1.html),  [free(1)](../man1/free.1.html),  [iostat(1)](../man1/iostat.1.html),  [mpstat(1)](../man1/mpstat.1.html),  [pidstat(1)](../man1/pidstat.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [sar(1)](../man1/sar.1.html),  [slabtop(1)](../man1/slabtop.1.html),  [top(1)](../man1/top.1.html)

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
