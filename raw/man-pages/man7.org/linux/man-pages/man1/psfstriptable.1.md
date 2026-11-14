---
{"title": "psfstriptable(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/psfstriptable.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# psfstriptable(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PSFSTRIPTABLE(1)         General Commands Manual         PSFSTRIPTABLE(1)

## [](#NAME)NAME

           psfstriptable - remove the embedded Unicode character table from a
           console font

## [](#SYNOPSIS)SYNOPSIS

           psfstriptable fontfile outfile

## [](#DESCRIPTION)DESCRIPTION

           psfstriptable reads a .psf format console font from fontfile,
           removes the embedded Unicode font table if there is one, and
           writes the result to outfile.  An input file name of "-" denotes
           standard input, and an output file name of "-" denotes standard
           output.

## [](#SEE_ALSO)SEE ALSO

           setfont(8), psfaddtable(1), psfgettable(1), psfxtable(1)

## [](#COLOPHON)COLOPHON

           This page is part of the kbd (Linux keyboard tools) project.
           Information about the project can be found at 
           ⟨http://www.kbd-project.org/⟩.  If you have a bug report for this
           manual page, send it to kbd@lists.altlinux.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/legionus/kbd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-26.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    kbd                            25 Oct 1994               PSFSTRIPTABLE(1)

------------------------------------------------------------------------

Pages that refer to this page: [psfaddtable(1)](../man1/psfaddtable.1.html),  [psfgettable(1)](../man1/psfgettable.1.html),  [psfxtable(1)](../man1/psfxtable.1.html)

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
