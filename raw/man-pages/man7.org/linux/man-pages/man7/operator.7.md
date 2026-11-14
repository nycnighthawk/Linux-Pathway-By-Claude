---
{"title": "operator(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/operator.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# operator(7) --- Linux manual page

+-----------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------+-----------------------------------+
|                                                                       |                                   |
+-----------------------------------------------------------------------+-----------------------------------+

    operator(7)          Miscellaneous Information Manual         operator(7)

## [](#NAME)NAME

           operator - C operator precedence and order of evaluation

## [](#DESCRIPTION)DESCRIPTION

           This manual page lists C operators and their precedence in
           evaluation.

           Operator                            Associativity   Notes
           () _Generic()                       -               [1]
           [] () . -> ++ -- (type){}           left to right   [2] [3]
           ++ -- & * + - ~ ! _Countof sizeof   right to left   [4]
           alignof _Maxof _Minof
           (type)                              right to left
           * / %                               left to right
           + -                                 left to right
           << >>                               left to right
           < > <= >=                           left to right
           == !=                               left to right
           &                                   left to right
           ^                                   left to right
           |                                   left to right
           &&                                  left to right
           ||                                  left to right
           ?:                                  right to left
           = *= /= %= += -= <<= >>= &= ^= |=   right to left
           ,                                   left to right

           The following notes provide further information to the above
           table:

           [1]  The () at this precedence is the parenthesized expression.
           [2]  The () at this precedence is the function call operator.
           [3]  The ++ and -- operators at this precedence level are the
                postfix flavors of the operators.
           [4]  The ++ and -- operators at this precedence level are the
                prefix flavors of the operators.

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

    Linux man-pages 6.19            2025-12-01                    operator(7)

------------------------------------------------------------------------

Pages that refer to this page: [countof(3)](../man3/countof.3.html),  [\_Maxof(3)](../man3/_Maxof.3.html)

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
