---
{"title": "btrecord(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/btrecord.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# btrecord(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BTRECORD(8)                                                   BTRECORD(8)

## [](#NAME)NAME

           btrecord - recreate IO loads recorded by blktrace

## [](#SYNOPSIS)SYNOPSIS

           Usage:

           btrecord [ options ] <dev...>

## [](#DESCRIPTION)DESCRIPTION

           The btrecord and btreplay tools provide the ability to record and
           replay IOs captured by the blktrace utility. Attempts are made to
           maintain ordering, CPU mappings and time-separation of IOs.

           The blktrace utility provides the ability to collect detailed
           traces from the kernel for each IO processed by the block IO
           layer. The traces provide a complete timeline for each IO
           processed, including detailed information concerning when an IO
           was first received by the block IO layer — indicating the device,
           CPU number, time stamp, IO direction, sector number and IO size
           (number of sectors). Using this information, one is able to replay
           the IO again on the same machine or another set up entirely.

           The basic operating work-flow to replay IOs would be something
           like:

           -
               Run blktrace to collect traces. Here you specify the
               device or devices that you wish to trace and later replay IOs
             upon. Note:
               the only traces you are interested in are QUEUE requests —
               thus, to save system resources (including storage for traces),
             one could
               specify the -a queue command line option to blktrace.

           -
               While blktrace is running, you run the workload that you
               are interested in.

           -
               When the work load has completed, you stop the blktrace
               utility (thus saving all traces over the complete workload).

           -
               You extract the pertinent IO information from the traces saved
             by
               blktrace using the btrecord utility. This will parse
               each trace file created by blktrace, and crafty IO
             descriptions
               to be used in the next phase of the workload processing.

           -
               Once btrecord has successfully created a series of data
               files to be processed, you can run the btreplay utility which
               attempts to generate the same IOs seen during the sample
             workload phase.

## [](#OPTIONS)OPTIONS

           -d <dir>
           --input-directory=<dir>
                  Set input directory.  This option requires a single
                  parameter providing the directory name for where input
                  files are to be found. The default directory is the current
                  directory (.).

           -D <dir>
           --output-directory=<dir>
                  Set output directory.  This option requires a single
                  parameter providing the directory name for where output
                  files are to be found. The default directory is the current
                  directory (.).

           -F
           --find-traces
                  Find trace files automatically This option instructs
                  btreplay to go find all the trace files in the directory
                  specified (either via the -d option, or in the default
                  directory (.).

           -h
           --help
                  Show help and exit.

           -V
           --version
                  Show version number and exit.

           -m <nanoseconds>
           --max-bunch-time=<nanoseconds>
                  The -m option requires a single parameter which specifies
                  an amount of time (in nanoseconds) to include in any one
                  bunch of IOs that are to be processed. The smaller the
                  value, the smaller the number of IOs processed at one time
                  — perhaps yielding in more realistic replay.  However,
                  after a certain point the amount of overhead per bunch may
                  result in additional real replay time, thus yielding less
                  accurate replay times.

                  The default value is 10,000,000 nanoseconds (10
                  milliseconds).

           -M <num>
           --max-pkts=<num>
                  Set maximum number of packets per bunch.  The -M option
                  requires a single parameter which specifies the maximum
                  number of IOs to store in a single bunch. As with the -m
                  option, smaller values may or may not yield more accurate
                  replay times.

                  The default value is 8, with a maximum value of up to 512
                  being supported.

           -o <basename>
           --output-base=<basename>
                  Set base name for output files.  Each output file has 3
                  fields:

                  1.
                      Device identifier (taken directly from the device name
                     of the
                      blktrace output file).

                  2.
                      btrecord base name — by default ``replay''.

                  3.
                      The CPU number (again, taken directly from the
                      blktrace output file name).

                  This option requires a single parameter that will override
                  the default name (replay), and replace it with the
                  specified value.

           -v
           --verbose
                  Enable verbose output.  This option will output some simple
                  statistics at the end of a successful run.  Example output
                  is:

                  sdab:0: 580661 pkts (tot), 126030 pkts (replay), 89809 bunches, 1.4 pkts/bunch
                  sdab:1: 2559775 pkts (tot), 430172 pkts (replay), 293029 bunches, 1.5 pkts/bunch
                  sdab:2: 653559 pkts (tot), 136522 pkts (replay), 102288 bunches, 1.3 pkts/bunch
                  sdab:3: 474773 pkts (tot), 117849 pkts (replay), 69572 bunches, 1.7 pkts/bunch

                  The meaning of the columns is:

                  1.
                       The first field contains the device name and CPU
                     identifier. Thus:
                       sdab:0: means the device sdab and traces on CPU 0.

                  2.
                       The second field contains the total number of packets
                     processed for each
                       device file.

                  3.
                       The next field shows the number of packets eligible
                     for replay.

                  4.
                       The fourth field contains the total number of IO
                     bunches.

                  5.
                       The last field shows the average number of IOs per
                     bunch recorded.

## [](#AUTHORS)AUTHORS

           btrecord was written by Alan D. Brunelle.  This man page was
           created from the btreplay documentation by Bas Zoetekouw.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to <linux-btrace@vger.kernel.org>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2007 Alan D. Brunelle, Alan D. Brunelle and Nathan
           Scott.
           This is free software.  You may redistribute copies of it under
           the terms of the GNU General Public License
           <http://www.gnu.org/licenses/gpl.html>.  There is NO WARRANTY, to
           the extent permitted by law.
           This manual page was created for Debian by Bas Zoetekouw.  It was
           derived from the documentation provided by the authors and it may
           be used, distributed and modified under the terms of the GNU
           General Public License, version 2.
           On Debian systems, the text of the GNU General Public License can
           be found in /usr/share/common-licenses/GPL-2.

## [](#SEE_ALSO)SEE ALSO

           The full documentation for btreplay can be found in
           /usr/share/doc/blktrace on Debian systems.
           blktrace(8), blkparse(1), btreplay(8)

## [](#COLOPHON)COLOPHON

           This page is part of the blktrace (Linux block layer I/O tracer)
           project.  Information about the project can be found at [unknown
           -- if you know, please contact man-pages@man7.org] It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/linux/kernel/git/axboe/blktrace.git⟩
           on 2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2025-12-10.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    blktrace git-20071207142532 December  8, 2007                 BTRECORD(8)

------------------------------------------------------------------------

Pages that refer to this page: [btreplay(8)](../man8/btreplay.8.html)

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
