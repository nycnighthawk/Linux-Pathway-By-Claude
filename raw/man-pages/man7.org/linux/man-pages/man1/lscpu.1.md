---
{"title": "lscpu(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lscpu.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lscpu(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [COLUMNS](#COLUMNS) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LSCPU(1)                      User Commands                      LSCPU(1)

## [](#NAME)NAME

           lscpu - display information about the CPU architecture

## [](#SYNOPSIS)SYNOPSIS

           lscpu [options]

## [](#DESCRIPTION)DESCRIPTION

           lscpu gathers CPU architecture information from sysfs,
           /proc/cpuinfo and any applicable architecture-specific libraries
           (e.g. librtas on Powerpc). The command output can be optimized for
           parsing or for easy readability by humans. The information
           includes, for example, the number of CPUs, threads, cores,
           sockets, and Non-Uniform Memory Access (NUMA) nodes. There is also
           information about the CPU caches and cache sharing, family, model,
           bogoMIPS, byte order, stepping and microcode version.

           The default output formatting on a terminal is subject to change
           and may be optimized for better readability. The output for
           non-terminals (e.g., pipes) is never affected by this optimization
           and it is always in "Field: data\n" format. Use for example "lscpu
           | less" to see the default output without optimizations.

           In virtualized environments, the CPU architecture information
           displayed reflects the configuration of the guest operating system
           which is typically different from the physical (host) system. On
           architectures that support retrieving physical topology
           information, lscpu also displays the number of physical sockets,
           chips, cores in the host system.

           Options that produce an output table accept an optional list
           argument. This list is a comma-separated series of column labels
           to limit the table to only the specified columns, arranged in the
           specified order. Use --help to see a list of valid column labels.
           The labels are case insensitive. Not all columns are supported on
           all architectures. If an unsupported column is specified, lscpu
           prints the column but does not provide any data for it.

           The cache sizes are reported as summary from all CPUs. The
           versions before v2.34 reported per-core sizes, but this output was
           confusing due to complicated CPUs topology and the way how caches
           are shared between CPUs. For more details about caches see
           --cache. Since version v2.37 lscpu follows cache IDs as provided
           by Linux kernel and it does not always start from zero.

## [](#OPTIONS)OPTIONS

           -a, --all
               Include lines for online and offline CPUs in the output
               (default for -e). This option may only be specified together
               with option -e or -p.

           -B, --bytes
               Print sizes in bytes rather than in human-readable form.

               By default, sizes are shown in units that are powers of 1024
               bytes. The formal abbreviations for these units (KiB, MiB,
               GiB, ...) are further shortened to just their first letter: K,
               M, G, ....

           -b, --online
               Limit the output to online CPUs (default for -p). This option
               may only be specified together with option -e or -p.

           -C, --caches[=list]
               Display details about CPU caches. For details about available
               information see --list-columns output.

               If the list argument is omitted, all columns for which data is
               available are included in the command output.

               When specifying the list argument, the option string plus the
               equal sign (=) plus the list may not contain any whitespace.
               Examples: -C=NAME,ONE-SIZE or --caches=NAME,ONE-SIZE.

               The default list of columns may be extended if list is
               specified in the format +list (e.g., lscpu -C=+ALLOC-POLICY).

           -c, --offline
               Limit the output to offline CPUs. This option may only be
               specified together with option -e or -p.

           -e, --extended[=list]
               Display the CPU information in human-readable format.

               If the list argument is omitted, the default columns are
               included in the command output. The default output is subject
               to change.

               When specifying the list argument, the option string plus the
               equal sign (=) plus the list may not contain any whitespace.
               Examples: -e=cpu,node or --extended=cpu,node.

               The default list of columns may be extended if list is
               specified in the format +list (e.g., lscpu -e=+MHZ).

           -H, --list-columns
               List the columns that can be specified with the --extended,
               --parse and --caches options. Can be used with --json or --raw
               to get the list in a machine-readable format.

           --hierarchic[=when]
               Use subsections in summary output. For backward compatibility,
               the default is to use subsections only when output on a
               terminal, and to use flattened output on a non-terminal. The
               optional argument when can be never, always, or auto. If the
               when argument is omitted, it defaults to always.

           -J, --json
               Use JSON output format for the default summary or extended
               output (see --extended). For backward compatibility, JSON
               output follows the default summary behavior for non-terminals
               (e.g., pipes) where subsections are missing. See also
               --hierarchic.

           --output-all
               Output all available columns. This option must be combined
               with either --extended, --parse, or --caches.

           -p, --parse[=list]
               Optimize the command output for easy parsing.

               If the list argument is omitted, the command output is
               compatible with earlier versions of lscpu. In this compatible
               format, two commas are used to separate CPU cache columns. If
               no CPU caches are identified the cache column is omitted. If
               the list argument is used, cache columns are separated with a
               colon (:).

               When specifying the list argument, the option string plus the
               equal sign (=) plus the list may not contain any whitespace.
               Examples: -p=cpu,online,mhz or --parse=cpu,online,mhz.

               The default list of columns may be extended if list is
               specified in the format +list (e.g., lscpu -p=+MHZ).

           -r, --raw
               Produce output in its raw format. This option is only
               applicable for the --extended, --parse, and --caches outputs.

           -s, --sysroot directory
               Gather CPU data for a Linux instance other than the instance
               from which the lscpu command is issued. The specified
               directory is the system root of the Linux instance to be
               inspected.

           -x, --hex
               Use hexadecimal masks for CPU sets (for example "ff"). The
               default is to print the sets in list format (for example 0,1).
               Note that before version 2.30 the mask has been printed with
               0x prefix.

           -y, --physical
               Display physical IDs for all columns with topology elements
               (core, socket, etc.). Other than logical IDs, which are
               assigned by lscpu, physical IDs are platform-specific values
               that are provided by the kernel. Physical IDs are not
               necessarily unique and they might not be arranged
               sequentially. If the kernel could not retrieve a physical ID
               for an element lscpu prints the dash (-) character.

               The CPU logical numbers are not affected by this option.

           --arm-id[=list]
               Print a list of the known ARM core implementers and their
               human readable names.

               If an argument is given, print a list of the individual core
               IDs and their names, for the given implementer.

           --arm-model id
               Print the name for this specific core model. This requires
               passing --arm-id=id to indicate the implementer id as well.

           --annotate[=when]
               Adds an annotation to each column header name. Such an
               annotation can be shown as a tooltip by terminals that support
               this feature. The optional when argument can be always, never,
               or auto. If the argument is omitted, it defaults to auto,
               which means that annotations will only be used when the output
               goes to a terminal.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           LSCPU_CACHES_COLUMNS=
               Specify a comma-separated list of output columns to print. All
               columns for the option -C can be used.

           LSCPU_COLUMNS=
               Specify a comma-separated list of output columns to print. All
               columns listed by --list-columns for the options -e and -p can
               be used.

           LSCPU_DEBUG=all
               Enable lscpu debug output.

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

           LIBSMARTCOLS_JSON=compact|lines
               Control JSON output format when using --json. Supported values
               are compact for JSON output with minimal whitespace, and lines
               for JSON Lines format (one JSON object per line). If unset or
               set to any other value, pretty-printed JSON is used.

           ULPATH_DEBUG=all
               Enable path debug output.

## [](#COLUMNS)COLUMNS

           A list of valid column labels can be viewed with the
           --list-columns option.

## [](#NOTES)NOTES

           The default output is subject to change. So whenever possible, you
           should avoid using default output in your scripts.

## [](#BUGS)BUGS

           The basic overview of CPU models is based on heuristics, taking
           into account differences such as CPU model names and implementer
           IDs. In some (unusual) cases, CPUs may differentiate in flags or
           BogoMIPS, but these differences are ignored in the lscpu overview.

           Sometimes in Xen Dom0 the kernel reports wrong data.

           On virtual hardware the number of cores per socket, etc. can be
           wrong.

## [](#AUTHORS)AUTHORS

           Cai Qian <qcai@redhat.com>, Karel Zak <kzak@redhat.com>, Heiko
           Carstens <heiko.carstens@de.ibm.com>, Christian Goeschel Ndjomouo
           <cgoesc2@wgu.edu>

## [](#SEE_ALSO)SEE ALSO

           chcpu(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The lscpu command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                       LSCPU(1)

------------------------------------------------------------------------

Pages that refer to this page: [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [proc_cpuinfo(5)](../man5/proc_cpuinfo.5.html),  [sched(7)](../man7/sched.7.html),  [chcpu(8)](../man8/chcpu.8.html)

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
