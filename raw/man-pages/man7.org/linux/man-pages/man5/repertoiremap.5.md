---
{"title": "repertoiremap(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/repertoiremap.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# repertoiremap(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    repertoiremap(5)           File Formats Manual           repertoiremap(5)

## [](#NAME)NAME

           repertoiremap - map symbolic character names to Unicode code
           points

## [](#DESCRIPTION)DESCRIPTION

           A repertoire map defines mappings between symbolic character names
           (mnemonics) and Unicode code points when compiling a locale with
           localedef(1).  Using a repertoire map is optional, it is needed
           only when symbolic names are used instead of now preferred Unicode
           code points.

       Syntax
           The repertoiremap file starts with a header that may consist of
           the following keywords:

           comment_char
                  is followed by a character that will be used as the comment
                  character for the rest of the file.  It defaults to the
                  number sign (#).

           escape_char
                  is followed by a character that should be used as the
                  escape character for the rest of the file to mark
                  characters that should be interpreted in a special way.  It
                  defaults to the backslash (\).

           The mapping section starts with the keyword CHARIDS in the first
           column.

           The mapping lines have the following form:

           <symbolic-name> <code-point> comment
                  This defines exactly one mapping, comment being optional.

           The mapping section ends with the string END CHARIDS.

## [](#FILES)FILES

           /usr/share/i18n/repertoiremaps
                  Usual default repertoire map path.

## [](#STANDARDS)STANDARDS

           POSIX.2.

## [](#NOTES)NOTES

           Repertoire maps are deprecated in favor of Unicode code points.

## [](#EXAMPLES)EXAMPLES

           A mnemonic for the Euro sign can be defined as follows:

           <Eu> <U20AC> EURO SIGN

## [](#SEE_ALSO)SEE ALSO

           locale(1), localedef(1), charmap(5), locale(5)

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

    Linux man-pages 6.19            2025-05-17               repertoiremap(5)

------------------------------------------------------------------------

Pages that refer to this page: [localedef(1)](../man1/localedef.1.html)

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
