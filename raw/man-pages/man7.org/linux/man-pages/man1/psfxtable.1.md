---
{"title": "psfxtable(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/psfxtable.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# psfxtable(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PSFXTABLE(1)             General Commands Manual             PSFXTABLE(1)

## [](#NAME)NAME

           psfxtable - handle Unicode character tables for console fonts

## [](#SYNOPSIS)SYNOPSIS

           psfxtable [-i infont] [-o outfont] [-it intable] [-ot outtable]
           [-nt]

## [](#DESCRIPTION)DESCRIPTION

           psfxtable handles the embedded Unicode character table for .psf
           format console fonts. It reads a font and possibly a table and
           writes a font and/or a table.  psfaddtable(1), psfgettable(1) and
           psfstriptable(1) are links to it.

           Each of the filenames infont, outfont, intable, and outtable may
           be replaced by a single dash (-), in which case standard input or
           standard output is used.  If no -i option is given, the font is
           read from standard input.  If no -it or -o or -ot option is given,
           no input table is read or no output font or output table is
           written.

           By default the output font (if any) will have a Unicode table when
           either the input font has one, or an explicit table (which
           overrides an input font table) has been provided.  The option -nt
           causes output of a font without table.  When outfont is requested
           it will get a psf1 header when infont has a psf1 header and
           intable does not have sequences and a psf2 header otherwise.

## [](#SEE_ALSO)SEE ALSO

           setfont(8), psfaddtable(1), psfgettable(1), psfstriptable(1)

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

    kbd                             9 Dec 1999                   PSFXTABLE(1)

------------------------------------------------------------------------

Pages that refer to this page: [psfaddtable(1)](../man1/psfaddtable.1.html),  [psfgettable(1)](../man1/psfgettable.1.html),  [psfstriptable(1)](../man1/psfstriptable.1.html)

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
