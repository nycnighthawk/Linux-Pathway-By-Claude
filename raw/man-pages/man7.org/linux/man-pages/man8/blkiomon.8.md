---
{"title": "blkiomon(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/blkiomon.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# blkiomon(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BLKIOMON(8)                                                   BLKIOMON(8)

## [](#NAME)NAME

           blkiomon - monitor block device I/O based o blktrace data

## [](#SYNOPSIS)SYNOPSIS

           blkiomon -I interval [ -h file ] [ -b file ] [ -d file ] [ -D file
           ] [ -Q path_name -q msg_queue_id -m msg_id ] [ -V ]

## [](#DESCRIPTION)DESCRIPTION

           blkiomon is a block device I/O monitor. It periodically generates
           per-device request size and request latency statistics from
           blktrace data. It provides histograms as well as data that can be
           used to calculate min, max, average and variance. For this
           purpose, it consumes D and C traces read from stdin.  Note, that
           this doesn't work for logical volumes, as high-level drivers don't
           see the completion of the events (C).

           There are options for binary output and human-readable output to
           files and stdout. Output to a message queue is supported as well.

           There is no need to use blkparse with blkiomon. blkiomon is
           capable of consuming binary output written to stdout by blktrace.

## [](#OPTIONS)OPTIONS

           -I interval
           --interval=interval
                  Set sample interval

           -h file
           --human-readable=file
                  Human-readable output file. Use '-' for stdout.

           -b file
           --binary=file
                  Binary output file. Use '-' for stdout.

           -d file
           --dump-lldd=file
                  Output file for data emitted by low level device driver.

           -D file
           --debug=file
                  Output file for debugging data. Use '-' for stdout.

           -Q path_name
           --msg-queue=path_name
                  Sets path_name as path name for existing message queue to
                  be used for binary output.

           -q msg_queue_id
           --msg-queue-id=msg_queue_id
                  Sets msg_queue_id as ID for an existing message queue to be
                  used for binary output.

           -m msg_id
           --msg-id=msg_id
                  Sets msg_id as message identifier to be used for binary
                  output messages written to an existing message queue.

           -V
           --version
                  Print program version.

## [](#EXAMPLES)EXAMPLES

           To get I/O statistics for /dev/sdw every 10 seconds for a period
           of one hour, use the following command:

               % blktrace /dev/sdw -a issue -a complete -w 3600 -o - |
           blkiomon -I 10 -h -

## [](#AUTHORS)AUTHORS

           blkiomon and this man page were written by Martin Peschke.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to <linux-btrace@vger.kernel.org>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2008 IBM Corp.
           This is free software.  You may redistribute copies of it under
           the terms of the GNU General Public License
           <http://www.gnu.org/licenses/gpl.html>.  There is NO WARRANTY, to
           the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           btrace(8), blktrace(8), blkparse(1), verify_blkparse(1),
           blkrawverify(1), btt(1)

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

                                  July 17, 2008                   BLKIOMON(8)

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
