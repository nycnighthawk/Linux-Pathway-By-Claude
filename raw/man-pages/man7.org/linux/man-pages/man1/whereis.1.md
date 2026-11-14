---
{"title": "whereis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/whereis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# whereis(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILE SEARCH PATHS](#FILE_SEARCH_PATHS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXAMPLES](#EXAMPLES) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WHEREIS(1)                    User Commands                    WHEREIS(1)

## [](#NAME)NAME

           whereis - locate the binary, source, and manual page files for a
           command

## [](#SYNOPSIS)SYNOPSIS

           whereis [options] [-BMS directory... -f] name...

## [](#DESCRIPTION)DESCRIPTION

           whereis locates the binary, source and manual files for the
           specified command names. The supplied names are first stripped of
           leading pathname components. Prefixes of s. resulting from use of
           source code control are also dealt with. whereis then attempts to
           locate the desired program in the standard Linux places, and in
           the places specified by $PATH and $MANPATH.

           The search restrictions (options -b, -m and -s) are cumulative and
           apply to the subsequent name patterns on the command line. Any new
           search restriction resets the search mask. For example,

              whereis -bm ls tr -m gcc

           searches for "ls" and "tr" binaries and man pages, and for "gcc"
           man pages only.

           The options -B, -M and -S reset search paths for the subsequent
           name patterns. For example,

              whereis -m ls -M /usr/share/man/man1 -f cal

           searches for "ls" man pages in all default paths, but for "cal" in
           the /usr/share/man/man1 directory only.

## [](#OPTIONS)OPTIONS

           -b
               Search for binaries.

           -m
               Search for manuals.

           -s
               Search for sources.

           -u
               Only show the command names that have unusual entries. A
               command is said to be unusual if it does not have just one
               entry of each explicitly requested type. Thus 'whereis -m -u
               *' asks for those files in the current directory which have no
               documentation file, or more than one.

           -B list
               Limit the places where whereis searches for binaries, by a
               whitespace-separated list of directories.

           -M list
               Limit the places where whereis searches for manuals and
               documentation in Info format, by a whitespace-separated list
               of directories.

           -S list
               Limit the places where whereis searches for sources, by a
               whitespace-separated list of directories.

           -f
               Terminates the directory list and signals the start of
               filenames. It must be used when any of the -B, -M, or -S
               options is used.

           -l
               Output the list of effective lookup paths that whereis is
               using. When none of -B, -M, or -S is specified, the option
               will output the hard-coded paths that the command was able to
               find on the system.

           -g
               Interpret the next names as a glob(7) patterns. whereis always
               compares only filenames (aka basename) and never complete
               path. Using directory names in the pattern has no effect.
               Don’t forget that the shell interprets the pattern when
               specified on the command line without quotes. It’s necessary
               to use quotes for the name, for example:

                  whereis -g 'find*'

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#FILE_SEARCH_PATHS)FILE SEARCH PATHS

           By default whereis tries to find files from hard-coded paths,
           which are defined with glob patterns. The command attempts to use
           the contents of $PATH and $MANPATH environment variables as
           default search path. The easiest way to know what paths are in use
           is to add the -l listing option. Effects of the -B, -M, and -S are
           displayed with -l.

## [](#ENVIRONMENT)ENVIRONMENT

           WHEREIS_DEBUG=all
               Enable debug output.

## [](#EXAMPLES)EXAMPLES

           To find all files in /usr/bin which are not documented in
           /usr/man/man1 or have no source in /usr/src:

              cd /usr/bin
              whereis -u -ms -M /usr/man/man1 -S /usr/src -f *

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The whereis command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     WHEREIS(1)

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
