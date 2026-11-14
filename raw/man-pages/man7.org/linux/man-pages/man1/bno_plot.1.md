---
{"title": "bno_plot(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/bno_plot.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# bno_plot(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BNO_PLOT(1)                                                   BNO_PLOT(1)

## [](#NAME)NAME

           bno_plot - generate interactive 3D plot of IO blocks and sizes

## [](#SYNOPSIS)SYNOPSIS

           bno_plot [ -h | --help ]
                    [ -v | --verbose ]
                    [ -K | --keys-below ]
                    [ <file...> ]

## [](#DESCRIPTION)DESCRIPTION

           bno_plot is a visualization tool for the block layer IO tracing
           tool called blktrace(8).  As noted in its documentation, blktrace
           is a block layer IO tracing mechanism which provides detailed
           information about request queue operations up to user space.

           bno_plot utilizes gnuplot to generate a 3D plot of the block
           number output from btt.  If no <files> are specified, it will
           utilize all files generated after btt was run with -B blknos
           (meaning: all files of the form blknos*[rw].dat).

           The -K option forces bno_plot to put the keys below the graph.  If
           it is not specified, all keys for input files are put in the upper
           right corner of the graph. If the number of devices exceed 10,
           then bno_plot will automatically push the keys under the graph.

           To use this utility, the gnuplot package needs to be installed.

           To exit the plotter, enter 'quit' or ^D at the 'gnuplot> ' prompt.

## [](#AUTHORS)AUTHORS

           bno_plot was written by Alan D. Brunelle.  This man page was
           created from the blktrace documentation by Bas Zoetekouw.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to <linux-btrace@vger.kernel.org>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2008 Hewlett-Packard Development Company, L.P.
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

           btt(1), gnuplot(1), blktrace(8), blkparse(1), verify_blkparse(1),
           blkrawverify(1)

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

    blktrace git-20080213182518 February 22, 2007                 BNO_PLOT(1)

------------------------------------------------------------------------

Pages that refer to this page: [btt(1)](../man1/btt.1.html)

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
