---
{"title": "verify_blkparse(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/verify_blkparse.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# verify_blkparse(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    VERIFY_BLKPARSE(1)                                     VERIFY_BLKPARSE(1)

## [](#NAME)NAME

           verify_blkparse - verifies an output file produced by blkparse

## [](#SYNOPSIS)SYNOPSIS

           verify_blkparse <filename>

## [](#DESCRIPTION)DESCRIPTION

           Verifies an output file from blkparse. All it does is check if the
           events in the file are correctly time ordered. If an entry is
           found that isn't ordered, it's dumped to stdout.

## [](#AUTHORS)AUTHORS

           blkparse was written by Jens Axboe, Alan D. Brunelle and Nathan
           Scott.  This man page was created from the blktrace documentation
           by Bas Zoetekouw.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to <linux-btrace@vger.kernel.org>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2006 Jens Axboe, Alan D. Brunelle and Nathan Scott.
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

           btrace(8), blktrace(8), blkparse(1), blkrawverify(1), btt(1)

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

    blktrace git-20070306202522   March  6, 2007           VERIFY_BLKPARSE(1)

------------------------------------------------------------------------

Pages that refer to this page: [blkparse(1)](../man1/blkparse.1.html),  [blkrawverify(1)](../man1/blkrawverify.1.html),  [bno_plot(1)](../man1/bno_plot.1.html),  [btt(1)](../man1/btt.1.html),  [blkiomon(8)](../man8/blkiomon.8.html),  [blktrace(8)](../man8/blktrace.8.html),  [btrace(8)](../man8/btrace.8.html)

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
