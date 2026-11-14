---
{"title": "semind(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/semind.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semind(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SUBCOMMANDS](#SUBCOMMANDS) \| [COMMON OPTIONS](#COMMON_OPTIONS) \| [ADD OPTIONS](#ADD_OPTIONS) \| [SEARCH OPTIONS](#SEARCH_OPTIONS) \| [FORMAT](#FORMAT) \| [KIND](#KIND) \| [MODE](#MODE) \| [SEE ALSO](#SEE_ALSO) \| [HOMEPAGE](#HOMEPAGE) \| [MAILING LIST](#MAILING_LIST) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    semind(1)                General Commands Manual                semind(1)

## [](#NAME)NAME

           semind - Semantic Indexer for C

## [](#SYNOPSIS)SYNOPSIS

           semind [options]
           semind [options] add [command options] [--] [compiler options]
           [files...]
           semind [options] rm [command options] pattern
           semind [options] search [command options] [pattern]
           semind [options] search [command options] (-e|-l)
           filename:linenr:column

## [](#DESCRIPTION)DESCRIPTION

           semind is the simple to use cscope-like tool based on
           sparse/dissect.  Unlike cscope it runs after pre-processor and
           thus it can't index the code filtered out by ifdef's, but otoh it
           understands how the symbol is used and it can track the usage of
           struct members.

## [](#SUBCOMMANDS)SUBCOMMANDS

           add    generates or updates semantic index file.

           rm     removes files from the index by pattern. The pattern is a
                  glob(7) wildcard pattern.

           search queries information about symbol by pattern. The pattern is
                  a glob(7) wildcard pattern.

## [](#COMMON_OPTIONS)COMMON OPTIONS

           -D, --database=FILE
                  specify database file (default: ./semind.sqlite).

           -v, --verbose
                  show information about what is being done.

           -h, --help
                  show this text and exit.

## [](#ADD_OPTIONS)ADD OPTIONS

           --include-local-syms
                  include into the index local symbols.

## [](#SEARCH_OPTIONS)SEARCH OPTIONS

           -f, --format=STRING
                  specify an output format. Default: '(%m)
                  %f\t%l\t%c\t%C\t%s' (see FORMAT below).

           -p, --path=PATTERN
                  search symbols only in specified directories.

           -m, --mode=MODE
                  search only the specified type of access (see MODE below).

           -k, --kind=KIND
                  specify a kind of symbol (see KIND below).

           -e, --explain
                  Show what happens in the specified file position;

           -l, --location
                  Show usage of symbols from a specific file position;

           -v, --verbose
                  show information about what is being done;

           -h, --help
                  show this text and exit.

## [](#FORMAT)FORMAT

           %m     access mode in human readable form (see MODE below).

           %f     file name.

           %l     line number.

           %c     column number.

           %C     the name of the function in which the symbol occurs.

           %n     symbol name.

           %s     source code line. Indexer does not save source code lines.
                  They are read from the file during the search.

## [](#KIND)KIND

           f      function

           s      strict

           m      struct member

## [](#MODE)MODE

           The MODE is dumped as a 3-letter string. The first letter denotes
           address of part, 2-nd - access by value, 3-rd - access by pointer.
           A special value 'def' means a symbol definition.

           r      read

           w      write

           m      read and write

## [](#SEE_ALSO)SEE ALSO

           sparse(1)

## [](#HOMEPAGE)HOMEPAGE

           https://sparse.docs.kernel.org

## [](#MAILING_LIST)MAILING LIST

           linux-sparse@vger.kernel.org

## [](#COLOPHON)COLOPHON

           This page is part of the sparse (a Semantic Parser for C) project.
           Information about the project can be found at 
           ⟨https://sparse.wiki.kernel.org/⟩.  If you have a bug report for
           this manual page, send it to linux-sparse@vger.kernel.org.  This
           page was obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/devel/sparse/sparse.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2025-12-18.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                                                    semind(1)

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
