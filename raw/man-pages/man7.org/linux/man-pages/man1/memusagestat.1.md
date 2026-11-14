---
{"title": "memusagestat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/memusagestat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# memusagestat(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    memusagestat(1)          General Commands Manual          memusagestat(1)

## [](#NAME)NAME

           memusagestat - generate graphic from memory profiling data

## [](#SYNOPSIS)SYNOPSIS

           memusagestat [option ...] datafile [outfile]

## [](#DESCRIPTION)DESCRIPTION

           memusagestat creates a PNG file containing a graphical
           representation of the memory profiling data in the file datafile;
           that file is generated via the -d (or --data) option of
           memusage(1).

           The red line in the graph shows the heap usage (allocated memory)
           and the green line shows the stack usage.  The x-scale is either
           the number of memory-handling function calls or (if the -t option
           is specified) time.

## [](#OPTIONS)OPTIONS

           -o file
           --output=file
                  Name of the output file.

           -s string
           --string=string
                  Use string as the title inside the output graph.

           -t
           --time Use time (rather than number of function calls) as the
                  scale for the X axis.

           -T
           --total
                  Also draw a graph of total memory consumption.

           -x size
           --x-size=size
                  Make the output graph size pixels wide.

           -y size
           --y-size=size
                  Make the output graph size pixels high.

           -?
           --help Print a help message and exit.

           --usage
                  Print a short usage message and exit.

           -V
           --version
                  Print version information and exit.

## [](#BUGS)BUGS

           To report bugs, see ⟨http://www.gnu.org/software/libc/bugs.html⟩

## [](#EXAMPLES)EXAMPLES

           See memusage(1).

## [](#SEE_ALSO)SEE ALSO

           memusage(1), mtrace(1)

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

    Linux man-pages 6.19            2026-02-08                memusagestat(1)

------------------------------------------------------------------------

Pages that refer to this page: [memusage(1)](../man1/memusage.1.html)

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
