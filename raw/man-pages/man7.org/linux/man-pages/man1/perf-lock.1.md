---
{"title": "perf-lock(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-lock.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-lock(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMON OPTIONS](#COMMON_OPTIONS) \| [REPORT OPTIONS](#REPORT_OPTIONS) \| [INFO OPTIONS](#INFO_OPTIONS) \| [CONTENTION OPTIONS](#CONTENTION_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-LOCK(1)                   perf Manual                   PERF-LOCK(1)

## [](#NAME)NAME

           perf-lock - Analyze lock events

## [](#SYNOPSIS)SYNOPSIS

           perf lock {record|report|script|info|contention}

## [](#DESCRIPTION)DESCRIPTION

           You can analyze various lock behaviours and statistics with this
           perf lock command.

               'perf lock record <command>' records lock events
               between start and end <command>. And this command
               produces the file "perf.data" which contains tracing
               results of lock events.

               'perf lock report' reports statistical data.

               'perf lock script' shows raw lock events.

               'perf lock info' shows metadata like threads or addresses
               of lock instances.

               'perf lock contention' shows contention statistics.

## [](#COMMON_OPTIONS)COMMON OPTIONS

           -i, --input=<file>
               Input file name. (default: perf.data unless stdin is a fifo)

           --output=<file>
               Output file name for perf lock contention and report.

           -v, --verbose
               Be more verbose (show symbol address, etc).

           -q, --quiet
               Do not show any warnings or messages. (Suppress -v)

           -D, --dump-raw-trace
               Dump raw trace in ASCII.

           -f, --force
               Don’t complain, do it.

           --vmlinux=<file>
               vmlinux pathname

           --kallsyms=<file>
               kallsyms pathname

## [](#REPORT_OPTIONS)REPORT OPTIONS

           -k, --key=<value>
               Sorting key. Possible values: acquired (default), contended,
               avg_wait, wait_total, wait_max, wait_min.

           -F, --field=<value>
               Output fields. By default it shows all the fields but users
               can customize that using this. Possible values: acquired,
               contended, avg_wait, wait_total, wait_max, wait_min.

           -c, --combine-locks
               Merge lock instances in the same class (based on name).

           -t, --threads
               The -t option is to show per-thread lock stat like below:

                   $ perf lock report -t -F acquired,contended,avg_wait

                   Name   acquired  contended   avg wait (ns)

                              perf     240569          9            5784
                           swapper     106610         19             543
                            :15789      17370          2           14538
                      ContainerMgr       8981          6             874
                             sleep       5275          1           11281
                   ContainerThread       4416          4             944
                   RootPressureThr       3215          5            1215
                       rcu_preempt       2954          0               0
                      ContainerMgr       2560          0               0
                           unnamed       1873          0               0
                   EventManager_De       1845          1             636
                   futex-default-S       1609          0               0

           -E, --entries=<value>
               Display this many entries.

## [](#INFO_OPTIONS)INFO OPTIONS

           -t, --threads
               dump only the thread list in perf.data

           -m, --map
               dump only the map of lock instances (address:name table)

## [](#CONTENTION_OPTIONS)CONTENTION OPTIONS

           -k, --key=<value>
               Sorting key. Possible values: contended, wait_total (default),
               wait_max, wait_min, avg_wait.

           -F, --field=<value>
               Output fields. By default it shows all but the wait_min fields
               and users can customize that using this. Possible values:
               contended, wait_total, wait_max, wait_min, avg_wait.

           -t, --threads
               Show per-thread lock contention stat

           -b, --use-bpf
               Use BPF program to collect lock contention stats instead of
               using the input data.

           -a, --all-cpus
               System-wide collection from all CPUs.

           -C, --cpu=<value>
               Collect samples only on the list of CPUs provided. Multiple
               CPUs can be provided as a comma-separated list with no space:
               0,1. Ranges of CPUs are specified with -: 0-2. Default is to
               monitor all CPUs.

           -p, --pid=<value>
               Record events on existing process ID (comma separated list).

           --tid=<value>
               Record events on existing thread ID (comma separated list).

           -M, --map-nr-entries=<value>
               Maximum number of BPF map entries (default: 16384). This will
               be aligned to a power of 2.

           --max-stack=<value>
               Maximum stack depth when collecting lock contention (default:
               8).

           --stack-skip=<value>
               Number of stack depth to skip when finding a lock caller
               (default: 3).

           -E, --entries=<value>
               Display this many entries.

           -l, --lock-addr
               Show lock contention stat by address

           -o, --lock-owner
               Show lock contention stat by owners. This option can be
               combined with -t, which shows owner’s per thread lock stats,
               or -v, which shows owner’s stacktrace. Requires --use-bpf.

           -Y, --type-filter=<value>
               Show lock contention only for given lock types (comma
               separated list). Available values are: semaphore, spinlock,
               rwlock, rwlock:R, rwlock:W, rwsem, rwsem:R, rwsem:W, rtmutex,
               rwlock-rt, rwlock-rt:R, rwlock-rt:W, percpu-rwmem, pcpu-sem,
               pcpu-sem:R, pcpu-sem:W, mutex

                   Note that RW-variant of locks have :R and :W suffix.  Names without the
                   suffix are shortcuts for the both variants.  Ex) rwsem = rwsem:R + rwsem:W.

           -L, --lock-filter=<value>
               Show lock contention only for given lock addresses or names
               (comma separated list).

           -S, --callstack-filter=<value>
               Show lock contention only if the callstack contains the given
               string. Note that it matches the substring so rq would match
               both raw_spin_rq_lock and irq_enter_rcu.

           -x, --field-separator=<SEP>
               Show results using a CSV-style output to make it easy to
               import directly into spreadsheets. Columns are separated by
               the string specified in SEP.

           --lock-cgroup
               Show lock contention stat by cgroup. Requires --use-bpf.

           -G, --cgroup-filter=<value>
               Show lock contention only in the given cgroups (comma
               separated list).

           -J, --inject-delay=<time@function[1]>
               Add delays to the given lock. It’s added to the contention-end
               part so that the (new) owner of the lock will be delayed. But
               by slowing down the owner, the waiters will also be delayed as
               well. This is working only with -b/--use-bpf.

                   The 'time' is specified in nsec but it can have a unit suffix.  Available
                   units are "ms", "us" and "ns".  Currently it accepts up to 10ms of delays
                   for safety reasons.

                   Note that it will busy-wait after it gets the lock. Delaying locks can
                   have significant consequences including potential kernel crashes.  Please
                   use it at your own risk.

## [](#SEE_ALSO)SEE ALSO

           perf(1)

## [](#NOTES)NOTES

            1. time@function
               mailto:time@function

## [](#COLOPHON)COLOPHON

           This page is part of the perf (Performance analysis tools for
           Linux (in Linux source tree)) project.  Information about the
           project can be found at 
           ⟨https://perf.wiki.kernel.org/index.php/Main_Page⟩.  If you have a
           bug report for this manual page, send it to
           linux-kernel@vger.kernel.org.  This page was obtained from the
           project's upstream Git repository
           ⟨http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-08-03.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    perf                            2025-05-31                   PERF-LOCK(1)

------------------------------------------------------------------------

Pages that refer to this page: [perf(1)](../man1/perf.1.html)

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
