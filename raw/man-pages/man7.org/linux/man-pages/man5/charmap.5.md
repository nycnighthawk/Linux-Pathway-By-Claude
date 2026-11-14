---
{"title": "charmap(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/charmap.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# charmap(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    charmap(5)                 File Formats Manual                 charmap(5)

## [](#NAME)NAME

           charmap - character set description file

## [](#DESCRIPTION)DESCRIPTION

           A character set description (charmap) defines all available
           characters and their encodings in a character set.  localedef(1)
           can use charmaps to create locale variants for different character
           sets.

       Syntax
           The charmap file starts with a header that may consist of the
           following keywords:

           <code_set_name>
                  is followed by the name of the character map.

           <comment_char>
                  is followed by a character that will be used as the comment
                  character for the rest of the file.  It defaults to the
                  number sign (#).

           <escape_char>
                  is followed by a character that should be used as the
                  escape character for the rest of the file to mark
                  characters that should be interpreted in a special way.  It
                  defaults to the backslash (\).

           <mb_cur_max>
                  is followed by the maximum number of bytes for a character.
                  The default value is 1.

           <mb_cur_min>
                  is followed by the minimum number of bytes for a character.
                  This value must be less than or equal than <mb_cur_max>.
                  If not specified, it defaults to <mb_cur_max>.

           The character set definition section starts with the keyword
           CHARMAP in the first column.

           The following lines may have one of the two following forms to
           define the character set:

           <character> byte-sequence comment
                  This form defines exactly one character and its byte
                  sequence, comment being optional.

           <character>..<character> byte-sequence comment
                  This form defines a character range and its byte sequence,
                  comment being optional.

           The character set definition section ends with the string END
           CHARMAP.

           The character set definition section may optionally be followed by
           a section to define widths of characters.

           The WIDTH_DEFAULT keyword can be used to define the default width
           for all characters not explicitly listed.  The default character
           width is 1.

           The width section for individual characters starts with the
           keyword WIDTH in the first column.

           The following lines may have one of the two following forms to
           define the widths of the characters:

           <character> width
                  This form defines the width of exactly one character.

           <character>...<character> width
                  This form defines the width for all the characters in the
                  range.

           The width definition section ends with the string END WIDTH.

## [](#FILES)FILES

           /usr/share/i18n/charmaps
                  Usual default character map path.

## [](#STANDARDS)STANDARDS

           POSIX.2.

## [](#EXAMPLES)EXAMPLES

           The Euro sign is defined as follows in the UTF-8 charmap:

           <U20AC>     /xe2/x82/xac EURO SIGN

## [](#SEE_ALSO)SEE ALSO

           iconv(1), locale(1), localedef(1), locale(5), charsets(7)

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

    Linux man-pages 6.19            2026-02-08                     charmap(5)

------------------------------------------------------------------------

Pages that refer to this page: [locale(1)](../man1/locale.1.html),  [localedef(1)](../man1/localedef.1.html),  [locale(5)](../man5/locale.5.html),  [repertoiremap(5)](../man5/repertoiremap.5.html)

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
