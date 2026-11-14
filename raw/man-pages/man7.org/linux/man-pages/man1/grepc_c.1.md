---
{"title": "grepc_c(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/grepc_c.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# grepc_c(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    grepc_c(1)               General Commands Manual               grepc_c(1)

## [](#NAME)NAME

           grepc_c - print PCRE patterns for searching C code

## [](#SYNOPSIS)SYNOPSIS

           grepc_c [option ...] pattern

## [](#DESCRIPTION)DESCRIPTION

           grepc_c(1) is a driver for grepc(1).  It prints PCRE patterns that
           grepc(1) will use to search for declarations, definitions, and/or
           uses of pattern in C source code.

           pattern is a PCRE pattern.  It normally represents a C identifier,
           and word boundaries are implicitly added to it in most cases.

       Types of code
           This program can produce PCRE pattern for several types of code.
           The following arguments can be passed to the -t option to select
           the types of code that will be searched.

           e      enum constant definitions.

           f      Function prototypes and definitions.  This can be further
                  subdivided into:

                  fp     Function prototypes.

                  fd     Function definitions.

                  fl     Linux kernel system calls.  This can be further
                         subdivided into:

                         flp    Linux kernel system call prototypes.

                         fld    Linux kernel system call definitions.

                  fg     glibc internal names of libc functions.  This can be
                         further subdivided into:

                         fgp    glibc prototypes.

                         fgd    glibc definitions.

           m      Macro definitions.

                  mf     Function-like macro definitions.

                  mo     Other macro definitions.

           t      Type definitions.

           u      Uses.  Searches occurences of pattern within enums,
                  function bodies, macro replacements, and type definitions,
                  and prints the whole enum, function, macro, and/or type
                  definitions.  In this case there are no word boundaries set
                  by default, so if pattern is open, fopen will also be
                  found; that's to allow searching for patterns containing
                  any sequence of characters.

                  This can be further subdivided into:

                  ue     Uses within enum definitions (except as an enum
                         constant).

                  uf     Uses within function definition bodies.

                  um     Uses within macro replacements.

                  ut     Uses within type definitions (except enum; that is:
                         typedef, struct, or union).

## [](#OPTIONS)OPTIONS

           -t type
                  Restrict the search to a specific type of code (see Types
                  of code under DESCRIPTION).  This option can be passed
                  multiple times to search for various types of code.
                  Default: e f m t.

## [](#EXAMPLES)EXAMPLES

           alx@devuan:~$ grepc_c -tm alignof;
           (?s)^[ \t]*#\s*define\s[\s\\]*alignof\(.*?[^\\]$
           (?s)^[ \t]*#\s*define\s[\s\\]*alignof\b(?!\().*?(?<!\\)$
           alx@devuan:~$ cd /usr/lib/gcc/;
           alx@devuan:/usr/lib/gcc$ pcre2grep -rnMf <(grepc_c -tm alignof) .;
           ./x86_64-linux-gnu/15/include/stdalign.h:33:#define alignof _Alignof

## [](#SEE_ALSO)SEE ALSO

           grepc(1), pcre2grep(1), pcre2syntax(3), pcre2pattern(3)

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

    Linux man-pages 6.19            2026-01-06                     grepc_c(1)

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
