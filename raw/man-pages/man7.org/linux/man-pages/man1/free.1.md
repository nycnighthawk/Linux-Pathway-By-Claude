---
{"title": "free(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/free.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# free(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FREE(1)                  General Commands Manual                  FREE(1)

## [](#NAME)NAME

           free - Display amount of free and used memory in the system

## [](#SYNOPSIS)SYNOPSIS

           free [option ...]

## [](#DESCRIPTION)DESCRIPTION

           free displays the total amount of free and used physical and swap
           memory in the system, as well as the buffers and caches used by
           the kernel. The information is gathered by parsing /proc/meminfo.
           The displayed columns are:

           total  Total usable memory (MemTotal and SwapTotal in
                  /proc/meminfo). This includes the physical and swap memory
                  minus a few reserved bits and kernel binary code.

           used   Used or unavailable memory (calculated as total -
                  available)

           free   Unused memory (MemFree and SwapFree in /proc/meminfo)

           shared Memory used (mostly) by tmpfs (Shmem in /proc/meminfo)

           buffers
                  Memory used by kernel buffers (Buffers in /proc/meminfo)

           cache  Memory used by the page cache and slabs (Cached and
                  SReclaimable in /proc/meminfo)

           buff/cache
                  Sum of buffers and cache

           available
                  Estimation of how much memory is available for starting new
                  applications, without swapping. Unlike the data provided by
                  the cache or free fields, this field takes into account
                  page cache and also that not all reclaimable memory slabs
                  will be reclaimed due to items being in use (MemAvailable
                  in /proc/meminfo, available on kernels 3.14, emulated on
                  kernels 2.6.27+, otherwise the same as free)

## [](#OPTIONS)OPTIONS

           -b, --bytes
                  Display the amount of memory in bytes.

           -k, --kibi
                  Display the amount of memory in kibibytes.  This is the
                  default.

           -m, --mebi
                  Display the amount of memory in mebibytes.

           -g, --gibi
                  Display the amount of memory in gibibytes.

           --tebi Display the amount of memory in tebibytes.

           --pebi Display the amount of memory in pebibytes.

           --kilo Display the amount of memory in kilobytes. Implies --si.

           --mega Display the amount of memory in megabytes. Implies --si.

           --giga Display the amount of memory in gigabytes. Implies --si.

           --tera Display the amount of memory in terabytes. Implies --si.

           --peta Display the amount of memory in petabytes. Implies --si.

           -h, --human
                  Show all output fields automatically scaled to shortest
                  three digit unit and display the units of print out.
                  Following units are used.

                    B = bytes
                    Ki = kibibyte
                    Mi = mebibyte
                    Gi = gibibyte
                    Ti = tebibyte
                    Pi = pebibyte

                  If unit is missing, and you have exbibyte of RAM or swap,
                  the number is in tebibytes and columns might not be aligned
                  with header.

           -w, --wide
                  Switch to the wide mode. The wide mode produces lines
                  longer than 80 characters. In this mode buffers and cache
                  are reported in two separate columns.

           -c, --count count
                  Display the result count times.  Requires the -s option.

           -l, --lohi
                  Show detailed low and high memory statistics.

           -L, --line
                  Show output on a single line, often used with the -s option
                  to show memory statistics repeatedly.

           -s, --seconds delay
                  Continuously display the result delay  seconds apart.  You
                  may actually specify any floating point number for delay
                  using either . or , for decimal point.  usleep(3) is used
                  for microsecond resolution delay times.

           --si   Use kilo, mega, giga etc (power of 1000) instead of kibi,
                  mebi, gibi (power of 1024).

           -t, --total
                  Display a line showing the column totals.

           -v, --committed
                  Display a line showing the memory commit limit and amount
                  of committed/uncommitted memory. The total column on this
                  line will display the memory commit limit.   This line is
                  relevant if memory overcommit is disabled.   On systems
                  with memory overcommit enabled, the free value can
                  temporarily appear negative. This is not a bug, but an
                  effect of overcommit, as the system has promised more
                  memory than the total of its virtual address space.  The
                  negative value indicates the magnitude of the system's
                  memory over-allocation.

           --help Print help.

           -V, --version
                  Display version information.

## [](#FILES)FILES

           /proc/meminfo
                  memory information

## [](#BUGS)BUGS

           The value for the shared column is not available from kernels
           before 2.6.32 and is displayed as zero.

           Please send bug reports to ⟨procps@freelists.org⟩.

## [](#SEE_ALSO)SEE ALSO

           ps(1), slabtop(1), top(1), vmstat(8).

## [](#COLOPHON)COLOPHON

           This page is part of the procps-ng (/proc filesystem utilities)
           project.  Information about the project can be found at 
           ⟨https://gitlab.com/procps-ng/procps⟩.  If you have a bug report
           for this manual page, see
           ⟨https://gitlab.com/procps-ng/procps/blob/master/Documentation/bugs.md⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/procps-ng/procps.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    procps-ng                       2023-05-02                        FREE(1)

------------------------------------------------------------------------

Pages that refer to this page: [htop(1)](../man1/htop.1.html),  [pcp-free(1)](../man1/pcp-free.1.html),  [slabtop(1)](../man1/slabtop.1.html),  [top(1)](../man1/top.1.html),  [w(1)](../man1/w.1.html),  [proc(5)](../man5/proc.5.html),  [proc_meminfo(5)](../man5/proc_meminfo.5.html),  [tmpfs(5)](../man5/tmpfs.5.html),  [vmstat(8)](../man8/vmstat.8.html)

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
