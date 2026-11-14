---
{"title": "trace-cmd-convert(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-convert.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-convert(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-CONVERT(1)        libtracefs Manual        TRACE-CMD-CONVERT(1)

## [](#NAME)NAME

           trace-cmd-convert - convert trace files

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd convert [OPTIONS] [output-file]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) convert command converts trace file. It reads the
           input file and copies the data into an output file. The output
           file may be in different format, depending on the command line
           arguments. The default output is in version 7 and compressed (if
           compiled with compression support).

## [](#OPTIONS)OPTIONS

           -i input-file
               By default, trace-cmd convert will read the file trace.dat.
               But the -i option open up the given input-file instead.

           -o out-file
               The name of the output file, this parameter is mandatory.
               Note, the output file may also be specified as the last item
               on the command line.

           --file-version
               Desired version of the output file. Supported versions are 6
               or 7.

           --compression
               Compression of the trace output file, one of these strings can
               be passed:

                   'any'  - auto select the best available compression algorithm

                   'none' - do not compress the trace file

                   'name' - the name of the desired compression algorithms. Available algorithms can be listed with
                   trace-cmd list -c

           --help
               Print usage information.

## [](#EXAMPLES)EXAMPLES

           # trace-cmd convert --compression any trace_compress.dat

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd.dat(1)

## [](#AUTHOR)AUTHOR

           Steven Rostedt <rostedt@goodmis.org[1]>, author of trace-cmd.
           Tzvetomir Stoyanov <tz.stoyanov@gmail.com[2]>, author of this man
           page.

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#COPYING)COPYING

           Copyright (C) 2021 VMware. Free use of this software is granted
           under the terms of the GNU Public License (GPL).

## [](#NOTES)NOTES

            1. rostedt@goodmis.org
               mailto:rostedt@goodmis.org

            2. tz.stoyanov@gmail.com
               mailto:tz.stoyanov@gmail.com

## [](#COLOPHON)COLOPHON

           This page is part of the trace-cmd (a front-end for Ftrace)
           project.  Information about the project can be found at 
           ⟨https://www.trace-cmd.org/⟩.  If you have a bug report for this
           manual page, see ⟨https://www.trace-cmd.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-05-29.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    libtracefs                      09/24/2023           TRACE-CMD-CONVERT(1)

------------------------------------------------------------------------

Pages that refer to this page: [trace-cmd(1)](../man1/trace-cmd.1.html)

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
