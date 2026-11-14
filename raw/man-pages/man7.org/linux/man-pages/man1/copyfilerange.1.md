---
{"title": "copyfilerange(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/copyfilerange.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# copyfilerange(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    COPYFILERANGE(1)              User Commands              COPYFILERANGE(1)

## [](#NAME)NAME

           copyfilerange - copy range(s) from source to destination file

## [](#SYNOPSIS)SYNOPSIS

           copyfilerange [options] source destination range...

## [](#DESCRIPTION)DESCRIPTION

           The copyfilerange command copies byte ranges from source to
           destination file. It is a wrapper around the copy_file_range(2)
           system call.

           The command can be used to create files with unallocated gaps
           (sparse files) and/or with shared blocks between multiple files
           (reflinks).

           Each range is of the form source_offset:destination_offset:length,
           with all values in bytes. If length is 0, then as much data as is
           available is copied. Multiple ranges may be supplied.

           When one or both of the offsets are omitted, the operation uses
           the last-used file location, starting with 0.

## [](#OPTIONS)OPTIONS

           -r, --ranges file
               Read range(s) separated by newlines from this file.

           -v, --verbose
               Verbose output of the copied ranges.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           0
               success

           1
               unspecified failure

## [](#NOTES)NOTES

           The copy_file_range(2) system call has some serious caveats: the
           source and destination files must use the same filesystem type,
           and some virtual filesystems (like procfs) won’t work.
           copy_file_range(2) will use reflinks when the filesystem supports
           this. To use reflinks, the file range most often needs to align
           with the filesystem block size on both the source and destination
           file.

## [](#AUTHORS)AUTHORS

           Dick Marinus <dick@mrns.nl>

## [](#EXAMPLES)EXAMPLES

               copyfilerange original-file reflink ::

               copyfilerange original-file first-block ::4096

               copyfilerange original-file even-blocks -r <(seq 0 8192 40960|awk '{print $1"::4096"}')

               copyfilerange original-file sparse-file 0:1M:1

               copyfilerange original-file split-first-mb ::1M

               copyfilerange original-file split-remainder 1M::

               copyfilerange split-first-mb join ::

               copyfilerange split-remainder join :1M:

## [](#SEE_ALSO)SEE ALSO

           copy_file_range(2)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The copyfilerange command is part of the util-linux package which
           can be downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24               COPYFILERANGE(1)

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
