---
{"title": "numastat(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/numastat.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# numastat(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNTAX](#SYNTAX) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    numastat(8)                   Administration                  numastat(8)

## [](#NAME)NAME

           numastat - Show per-NUMA-node memory statistics for processes and
           the operating system

## [](#SYNTAX)SYNTAX

           numastat

           numastat [-V]

           numastat [<PID>|<pattern>...]

           numastat [-c] [-m] [-n] [-p <PID>|<pattern>] [-s[<node>]] [-v]
           [-z] [<PID>|<pattern>...]

## [](#DESCRIPTION)DESCRIPTION

           numastat with no command options or arguments at all, displays
           per-node NUMA hit and miss system statistics from the kernel
           memory allocator.  This default numastat behavior is strictly
           compatible with the previous long-standing numastat perl script,
           written by Andi Kleen.  The default numastat statistics shows per-
           node numbers (in units of pages of memory) in these categories:

           numa_hit is memory successfully allocated on this node as
           intended.

           numa_miss is memory allocated on this node despite the process
           preferring some different node. Each numa_miss has a numa_foreign
           on another node.

           numa_foreign is memory intended for this node, but actually
           allocated on some different node.  Each numa_foreign has a
           numa_miss on another node.

           interleave_hit is interleaved memory successfully allocated on
           this node as intended.

           local_node is memory allocated on this node while a process was
           running on it.

           other_node is memory allocated on this node while a process was
           running on some other node.

           Any supplied options or arguments with the numastat command will
           significantly change both the content and the format of the
           display.  Specified options will cause display units to change to
           megabytes of memory, and will change other specific behaviors of
           numastat as described below.

           Memory usage information reflects the resident pages on the
           system.

## [](#OPTIONS)OPTIONS

           -c     Minimize table display width by dynamically shrinking
                  column widths based on data contents.  With this option,
                  amounts of memory will be rounded to the nearest megabyte
                  (rather than the usual display with two decimal places).
                  Column width and inter-column spacing will be somewhat
                  unpredictable with this option, but the more dense display
                  will be very useful on systems with many NUMA nodes.

           -m     Show the meminfo-like system-wide memory usage information.
                  This option produces a per-node breakdown of memory usage
                  information similar to that found in /proc/meminfo.

           -n     Show the original numastat statistics info.  This will show
                  the same information as the default numastat behavior but
                  the units will be megabytes of memory, and there will be
                  other formatting and layout changes versus the original
                  numastat behavior.

           -p <PID> or <pattern>
                  Show per-node memory allocation information for the
                  specified PID or pattern.  If the -p argument is only
                  digits, it is assumed to be a numerical PID.  If the
                  argument characters are not only digits, it is assumed to
                  be a text fragment pattern to search for in process command
                  lines.  For example, numastat -p qemu will attempt to find
                  and show information for processes with "qemu" in the
                  command line.  Any command line arguments remaining after
                  numastat option flag processing is completed, are assumed
                  to be additional <PID> or <pattern> process specifiers.  In
                  this sense, the -p option flag is optional: numastat qemu
                  is equivalent to numastat -p qemu

           -s[<node>]
                  Sort the table data in descending order before displaying
                  it, so the biggest memory consumers are listed first.  With
                  no specified <node>, the table will be sorted by the total
                  column.  If the optional <node> argument is supplied, the
                  data will be sorted by the <node> column.  Note that <node>
                  must follow the -s immediately with no intermediate white
                  space (e.g., numastat -s2). Because -s can allow an
                  optional argument, it must always be the last option
                  character in a compound option character string. For
                  example, instead of numastat -msc (which probably will not
                  work as you expect), use numastat -mcs

           -v     Make some reports more verbose.  In particular, process
                  information for multiple processes will display detailed
                  information for each process.  Normally when per-node
                  information for multiple processes is displayed, only the
                  total lines are shown.

           -V     Display numastat version information and exit.

           -z     Skip display of table rows and columns of only zero
                  valuess.  This can be used to greatly reduce the amount of
                  uninteresting zero data on systems with many NUMA nodes.
                  Note that when rows or columns of zeros are still displayed
                  with this option, that probably means there is at least one
                  value in the row or column that is actually non-zero, but
                  rounded to zero for display.

## [](#NOTES)NOTES

           numastat attempts to fold each table display so it will be
           conveniently readable on the output terminal.  Normally a terminal
           width of 80 characters is assumed.  When the resize command is
           available, numastat attempts to dynamically determine and fine
           tune the output tty width from resize output.  If numastat output
           is not to a tty, very long output lines can be produced, depending
           on how many NUMA nodes are present.  In all cases, output width
           can be explicitly specified via the NUMASTAT_WIDTH environment
           variable.  For example, NUMASTAT_WIDTH=100  numastat.  On systems
           with many NUMA nodes, numastat -c -z .... can be very helpful to
           selectively reduce the amount of displayed information.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           NUMASTAT_WIDTH

## [](#FILES)FILES

           /proc/*/numa_maps
           /sys/devices/system/node/node*/meminfo
           /sys/devices/system/node/node*/numastat

## [](#EXAMPLES)EXAMPLES

           numastat -c -z -m -n
           numastat -czs libvirt kvm qemu
           watch -n1 numastat
           watch -n1 --differences=cumulative numastat

## [](#AUTHORS)AUTHORS

           The original numastat perl script was written circa 2003 by Andi
           Kleen <andi.kleen@intel.com>.  The current numastat program was
           written in 2012 by Bill Gray <bgray@redhat.com> to be compatible
           by default with the original, and to add options to display per-
           node system memory usage and per-node process memory allocation.

## [](#SEE_ALSO)SEE ALSO

           numactl(8), set_mempolicy(2), numa(3)

## [](#COLOPHON)COLOPHON

           This page is part of the numactl (NUMA commands) project.
           Information about the project can be found at 
           ⟨http://oss.sgi.com/projects/libnuma/⟩.  If you have a bug report
           for this manual page, send it to linux-numa@vger.kernel.org.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/numactl/numactl.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Bill Gray                         1.0.0                       numastat(8)

------------------------------------------------------------------------

Pages that refer to this page: [migrate_pages(2)](../man2/migrate_pages.2.html),  [move_pages(2)](../man2/move_pages.2.html)

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
