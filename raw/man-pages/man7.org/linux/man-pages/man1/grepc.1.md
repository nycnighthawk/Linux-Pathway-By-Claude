---
{"title": "grepc(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/grepc.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# grepc(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CAVEATS](#CAVEATS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    grepc(1)                 General Commands Manual                 grepc(1)

## [](#NAME)NAME

           grepc - find declarations, definitions, and uses in source code

## [](#SYNOPSIS)SYNOPSIS

           grepc [option ...] pattern [file ...]

## [](#DESCRIPTION)DESCRIPTION

           grepc(1) searches for declarations, definitions, and/or uses of
           pattern in each source file.

           pattern is a PCRE pattern.  It normally represents an identifier,
           and word boundaries are implicitly added to it in most cases.

           If no file is given, this program reads standard input.
           Otherwise, it reads all files specified, and searches under any
           specified directories, recursively, without following symbolic
           links.

## [](#OPTIONS)OPTIONS

           -A n   Print n lines of trailing context after a match.

           -B n   Print n lines of leading context before a match.

           -C n   Print n lines of context surrounding a match.

           -c     Do not print matches, and instead print a count of them.

           -h     Suppress the prefixing of file names on output.

           -i     Ignore case distinctions in pattern.

           -l     Suppress normal output; instead print the name of each
                  input file from which output would normally have been
                  printed.  Each file is only printed once.

           -m n   Stop processing after finding n matches.

           -n     Prefix each line of output with the 1-based line number
                  within its input file.

           -t type
                  Restrict the search to a specific type of code.  This
                  option can be passed multiple times to search for various
                  types of code.  The acceptable values depend on the driver
                  used for the language.  See grepc_c(1), which is the
                  default driver.

## [](#CAVEATS)CAVEATS

       Crashes
           In some cases, internal calls to pcre2grep(1) may fail after
           consuming too much resources.  To solve that, use -t to restrict
           the types of code of your search.

       Seekable files
           Files specified in the command line must be seekable and able to
           be opened twice.  If you need to read a non-seekable file,
           redirect it to the standard input.

## [](#EXAMPLES)EXAMPLES

           alx@devuan:/usr/lib/gcc$ grepc -n alignof .;
           ./x86_64-linux-gnu/15/include/stdalign.h:33:#define alignof _Alignof

## [](#SEE_ALSO)SEE ALSO

           grepc_c(1), pcre2grep(1), pcre2syntax(3), pcre2pattern(3)

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

    Linux man-pages 6.19            2025-11-09                       grepc(1)

------------------------------------------------------------------------

Pages that refer to this page: [grepc(1)](../man1/grepc.1.html),  [grepc_c(1)](../man1/grepc_c.1.html)

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
