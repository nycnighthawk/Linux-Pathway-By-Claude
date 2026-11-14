---
{"title": "perf-iostat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-iostat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-iostat(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-IOSTAT(1)                 perf Manual                 PERF-IOSTAT(1)

## [](#NAME)NAME

           perf-iostat - Show I/O performance metrics

## [](#SYNOPSIS)SYNOPSIS

           perf iostat list
           perf iostat <ports> -- <command> [<options>]

## [](#DESCRIPTION)DESCRIPTION

           Mode is intended to provide four I/O performance metrics per each
           PCIe root port:

           •   Inbound Read - I/O devices below root port read from the host
               memory, in MB

           •   Inbound Write - I/O devices below root port write to the host
               memory, in MB

           •   Outbound Read - CPU reads from I/O devices below root port, in
               MB

           •   Outbound Write - CPU writes to I/O devices below root port, in
               MB

## [](#OPTIONS)OPTIONS

           <command>...
               Any command you can specify in a shell.

           list
               List all PCIe root ports.

           <ports>
               Select the root ports for monitoring. Comma-separated list is
               supported.

## [](#EXAMPLES)EXAMPLES

            1. List all PCIe root ports (example for 2-S platform):

                   $ perf iostat list
                   S0-uncore_iio_0<0000:00>
                   S1-uncore_iio_0<0000:80>
                   S0-uncore_iio_1<0000:17>
                   S1-uncore_iio_1<0000:85>
                   S0-uncore_iio_2<0000:3a>
                   S1-uncore_iio_2<0000:ae>
                   S0-uncore_iio_3<0000:5d>
                   S1-uncore_iio_3<0000:d7>

            2. Collect metrics for all PCIe root ports:

                   $ perf iostat -- dd if=/dev/zero of=/dev/nvme0n1 bs=1M oflag=direct
                   357708+0 records in
                   357707+0 records out
                   375083606016 bytes (375 GB, 349 GiB) copied, 215.974 s, 1.7 GB/s

                   Performance counter stats for 'system wide':

                      port             Inbound Read(MB)    Inbound Write(MB)    Outbound Read(MB)   Outbound Write(MB)
                   0000:00                    1                    0                    2                    3
                   0000:80                    0                    0                    0                    0
                   0000:17               352552                   43                    0                   21
                   0000:85                    0                    0                    0                    0
                   0000:3a                    3                    0                    0                    0
                   0000:ae                    0                    0                    0                    0
                   0000:5d                    0                    0                    0                    0
                   0000:d7                    0                    0                    0                    0

            3. Collect metrics for comma-separated list of PCIe root ports:

                   $ perf iostat 0000:17,0:3a -- dd if=/dev/zero of=/dev/nvme0n1 bs=1M oflag=direct
                   357708+0 records in
                   357707+0 records out
                   375083606016 bytes (375 GB, 349 GiB) copied, 197.08 s, 1.9 GB/s

                   Performance counter stats for 'system wide':

                      port             Inbound Read(MB)    Inbound Write(MB)    Outbound Read(MB)   Outbound Write(MB)
                   0000:17               358559                   44                    0                   22
                   0000:3a                    3                    2                    0                    0

                   197.081983474 seconds time elapsed

## [](#SEE_ALSO)SEE ALSO

           perf-stat(1)

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

    perf                            2021-08-10                 PERF-IOSTAT(1)

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
