---
{"title": "fincore(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/fincore.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fincore(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FINCORE(1)                    User Commands                    FINCORE(1)

## [](#NAME)NAME

           fincore - count pages of file contents in core

## [](#SYNOPSIS)SYNOPSIS

           fincore [options] file...

## [](#DESCRIPTION)DESCRIPTION

           fincore counts pages of file contents being resident in memory (in
           core), and reports the numbers. If an error occurs during
           counting, then an error message is printed to the stderr and
           fincore continues processing the rest of files listed in a command
           line. fincore uses the cachestat(2) syscall to count resident
           pages. If the cachestat(2) syscall is not available and cachestat
           usage is not forced with the --cachestat option, then fincore uses
           the mincore(2) syscall as a fallback. The cachestat(2) syscall is
           more efficient than mincore because it does not require a page
           table lock to walks page tables, and also reports more information
           than mincore, like the number of cached pages, dirty pages, pages
           marked for writeback, evicted pages, and recently evicted pages.
           Another difference between the two syscalls is that if write
           permissions are not granted to the file, then cachestat(2) returns
           an error, while mincore(2) for security reasons, returns fake data
           as if all pages were resident in memory (c.f.r. kernel commit
           "make mincore() more conservative"
           <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=134fca9063ad4851de767d1768180e5dede9a881>).

           The default output is subject to change. So whenever possible, you
           should avoid using default outputs in your scripts. Always
           explicitly define expected columns by using --output columns-list
           in environments where a stable output is required.

## [](#OPTIONS)OPTIONS

           -n, --noheadings
               Do not print a header line in status output.

           -b, --bytes
               Print sizes in bytes rather than in human-readable form.

               By default, sizes are shown in units that are powers of 1024
               bytes. The formal abbreviations for these units (KiB, MiB,
               GiB, ...) are further shortened to just their first letter: K,
               M, G, ....

           -c, --total
               produce a grand total.

           -C, --cachestat
               force usage of the cachestat(2) syscall instead of mincore(2),
               and fail if it’s not available.

           -o, --output list
               Define output columns. See the --help output to get a list of
               the currently supported columns. The default list of columns
               may be extended if list is specified in the format +list.

           --output-all
               Output all available columns.

           -r, --raw
               Produce output in raw format. All potentially unsafe
               characters are hex-escaped (\x<code>).

           -J, --json
               Use JSON output format.

           -R, --recursive
               Recursively check all files in directories.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

           LIBSMARTCOLS_JSON=compact|lines
               Control JSON output format when using --json. Supported values
               are compact for JSON output with minimal whitespace, and lines
               for JSON Lines format (one JSON object per line). If unset or
               set to any other value, pretty-printed JSON is used.

## [](#AUTHORS)AUTHORS

           Masatake YAMATO <yamato@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           mincore(2), getpagesize(2), getconf(1p) cachestat(2)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The fincore command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     FINCORE(1)

------------------------------------------------------------------------

Pages that refer to this page: [mincore(2)](../man2/mincore.2.html),  [posix_fadvise(2)](../man2/posix_fadvise.2.html)

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
