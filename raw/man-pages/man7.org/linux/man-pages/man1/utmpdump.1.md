---
{"title": "utmpdump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/utmpdump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# utmpdump(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UTMPDUMP(1)                   User Commands                   UTMPDUMP(1)

## [](#NAME)NAME

           utmpdump - dump UTMP and WTMP files in raw format

## [](#SYNOPSIS)SYNOPSIS

           utmpdump [options] filename

## [](#DESCRIPTION)DESCRIPTION

           utmpdump is a simple program to dump UTMP and WTMP files in raw
           format, so they can be examined. utmpdump reads from stdin unless
           a filename is passed.

## [](#OPTIONS)OPTIONS

           -f, --follow
               Output appended data as the file grows.

           -o, --output file
               Write command output to file instead of standard output.

           -r, --reverse
               Undump, write back edited login information into the utmp or
               wtmp files.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#NOTES)NOTES

           utmpdump can be useful in cases of corrupted utmp or wtmp entries.
           It can dump out utmp/wtmp to an ASCII file, which can then be
           edited to remove bogus entries, and reintegrated using:

              utmpdump -r < ascii_file > wtmp

           But be warned, utmpdump was written for debugging purposes only.

       File formats
           Only the binary version of the utmp(5) is standardised. Textual
           dumps may become incompatible in future.

           The version 2.28 was the last one that printed text output using
           ctime(3) timestamp format. Newer dumps use millisecond precision
           ISO-8601 timestamp format in UTC-0 timezone. Conversion from
           former timestamp format can be made to binary, although attempt to
           do so can lead the timestamps to drift amount of timezone offset.

## [](#BUGS)BUGS

           You may not use the -r option, as the format for the utmp/wtmp
           files strongly depends on the input format. This tool was not
           written for normal use, but for debugging only.

## [](#AUTHORS)AUTHORS

           Michael Krapp

## [](#SEE_ALSO)SEE ALSO

           last(1), w(1), who(1), utmp(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The utmpdump command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                    UTMPDUMP(1)

------------------------------------------------------------------------

Pages that refer to this page: [getutmp(3)](../man3/getutmp.3.html),  [utmp(5)](../man5/utmp.5.html)

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
