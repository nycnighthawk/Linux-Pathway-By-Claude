---
{"title": "lp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lp(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [CONFORMING TO](#CONFORMING_TO) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lp(1)                          OpenPrinting                         lp(1)

## [](#NAME)NAME

           lp - print files

## [](#SYNOPSIS)SYNOPSIS

           lp [ -h hostname[:port] ] [ -E ] [ -U username ] [ -c ] [ -d
           destination[/instance] ] [ -m ] [ -n num-copies ] [ -o
           option[=value] ] [ -q priority ] [ -s ] [ -t title ] [ -H handling
           ] [ -P page-list ] [ -- ] [ file(s) ]
           lp [ -h hostname[:port] ] [ -E ] [ -U username ] [ -c ] [ -i job-
           id ] [ -n num-copies ] [ -o option[=value] ] [ -q priority ] [ -t
           title ] [ -H handling ] [ -P page-list ]

## [](#DESCRIPTION)DESCRIPTION

           lp submits files for printing or alters a pending job.  Use a
           filename of "-" to force printing from the standard input.

       THE DEFAULT DESTINATION
           CUPS provides many ways to set the default destination. The LPDEST
           and PRINTER environment variables are consulted first.  If neither
           are set, the current default set using the lpoptions(1) command is
           used, followed by the default set using the lpadmin(8) command.

## [](#OPTIONS)OPTIONS

           The following options are recognized by lp:

           --   Marks the end of options; use this to print a file whose name
                begins with a dash (-).

           -E   Forces encryption when connecting to the server.

           -U username
                Specifies the username to use when connecting to the server.

           -c   This option is provided for backwards-compatibility only. On
                systems that support it, this option forces the print file to
                be copied to the spool directory before printing.  In CUPS,
                print files are always sent to the scheduler via IPP which
                has the same effect.

           -d destination
                Prints files to the named printer.

           -h hostname[:port]
                Chooses an alternate server.  Note: This option must occur
                before all others.

           -i job-id
                Specifies an existing job to modify.

           -m   Sends an email when the job is completed.

           -n copies
                Sets the number of copies to print.

           -o "name=value [ ... name=value ]"
                Sets one or more job options.  See "COMMON JOB OPTIONS"
                below.

           -q priority
                Sets the job priority from 1 (lowest) to 100 (highest).  The
                default priority is 50.

           -s   Do not report the resulting job IDs (silent mode.)

           -t "name"
                Sets the job name.

           -H hh:mm

           -H hold

           -H immediate

           -H restart

           -H resume
                Specifies when the job should be printed.  A value of
                immediate will print the file immediately, a value of hold
                will hold the job indefinitely, and a UTC time value (HH:MM)
                will hold the job until the specified UTC (not local) time.
                Use a value of resume with the -i option to resume a held
                job.  Use a value of restart with the -i option to restart a
                completed job.

           -P page-list
                Specifies which pages to print in the document.  The list can
                contain a list of numbers and ranges (#-#) separated by
                commas, e.g., "1,3-5,16".  The page numbers refer to the
                output pages and not the document's original pages - options
                like "number-up" can affect the numbering of the pages.

       COMMON JOB OPTIONS
           Aside from the printer-specific options reported by the
           lpoptions(1) command, the following generic options are available:

           -o job-sheets=name
                Prints a cover page (banner) with the document.  The "name"
                can be "classified", "confidential", "secret", "standard",
                "topsecret", or "unclassified".

           -o media=size
                Sets the page size to size. Most printers support at least
                the size names "a4", "letter", and "legal".

           -o number-up={2|4|6|9|16}
                Prints 2, 4, 6, 9, or 16 document (input) pages on each
                output page.

           -o orientation-requested=4
                Prints the job in landscape (rotated 90 degrees counter-
                clockwise).

           -o orientation-requested=5
                Prints the job in landscape (rotated 90 degrees clockwise).

           -o orientation-requested=6
                Prints the job in reverse portrait (rotated 180 degrees).

           -o print-as-raster
                Prints the job as raster.

           -o print-quality=3

           -o print-quality=4

           -o print-quality=5
                Specifies the output quality - draft (3), normal (4), or best
                (5).

           -o sides=one-sided
                Prints on one side of the paper.

           -o sides=two-sided-long-edge
                Prints on both sides of the paper for portrait output.

           -o sides=two-sided-short-edge
                Prints on both sides of the paper for landscape output.

## [](#ENVIRONMENT)ENVIRONMENT

           The following environment variables override the default
           destination:

           LPDEST
                Specifies the default print queue (System V standard).

           PRINTER
                Specifies the default print queue (Berkeley standard).

## [](#CONFORMING_TO)CONFORMING TO

           Unlike the System V printing system, CUPS allows printer names to
           contain any printable character except SPACE, TAB, "/", or "#".
           Also, printer and class names are not case-sensitive.

           The -q option accepts a different range of values than the Solaris
           lp command, matching the IPP job priority values (1-100, 100 is
           highest priority) instead of the Solaris values (0-39, 0 is
           highest priority).

## [](#EXAMPLES)EXAMPLES

           Print two copies of a document to the default printer:

               lp -n 2 filename

           Print a double-sided legal document to a printer called "foo":

               lp -d foo -o media=legal -o sides=two-sided-long-edge filename

           Print a presentation document 2-up to a printer called "bar":

               lp -d bar -o number-up=2 filename

## [](#SEE_ALSO)SEE ALSO

           cancel(1), lpadmin(8), lpoptions(1), lpq(1), lpr(1), lprm(1),
           lpstat(1), CUPS Online Help (http://localhost:631/help)

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2020-2024 by OpenPrinting.

## [](#COLOPHON)COLOPHON

           This page is part of the CUPS (a standards-based, open source
           printing system) project.  Information about the project can be
           found at ⟨https://github.com/openprinting/cups⟩.  If you have a
           bug report for this manual page, see
           ⟨https://github.com/OpenPrinting/cups/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/openprinting/cups⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    2024-04-02                         CUPS                             lp(1)

------------------------------------------------------------------------

Pages that refer to this page: [cancel(1)](../man1/cancel.1.html),  [cups(1)](../man1/cups.1.html),  [lpoptions(1)](../man1/lpoptions.1.html),  [lpq(1)](../man1/lpq.1.html),  [lpr(1)](../man1/lpr.1.html),  [lprm(1)](../man1/lprm.1.html),  [lpstat(1)](../man1/lpstat.1.html),  [backend(7)](../man7/backend.7.html),  [cupsaccept(8)](../man8/cupsaccept.8.html),  [cupsenable(8)](../man8/cupsenable.8.html),  [lpadmin(8)](../man8/lpadmin.8.html),  [lpc(8)](../man8/lpc.8.html),  [lpmove(8)](../man8/lpmove.8.html)

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
