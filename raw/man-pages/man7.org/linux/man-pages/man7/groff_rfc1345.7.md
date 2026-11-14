---
{"title": "groff_rfc1345(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/groff_rfc1345.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groff_rfc1345(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Description](#Description) \| [Bugs](#Bugs) \| [Files](#Files) \| [Authors](#Authors) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    groff_rfc1345(7)     Miscellaneous Information Manual    groff_rfc1345(7)

## [](#Name)Name

           groff_rfc1345 - special character names from RFC 1345 and Vim
           digraphs

## [](#Description)Description

           The file rfc1345.tmac defines special character escape sequences
           for groff(7) based on the glyph mnemonics specified in RFC 1345
           and the digraph table of the text editor Vim.  Each escape
           sequence translates to a Unicode code point, and will render
           correctly if the underlying font is a Unicode font that covers the
           code point.

           For example, “\[Rx]” is the “recipe” or “prescription take”
           symbol, and maps to the code point U+211E.  groff lets you write
           it as “\[u211E]”, but “\[Rx]” is more mnemonic.

           For a list of the glyph names provided, please see the file
           rfc1345.tmac, which contains definitions of the form
                  .char \[Rx] \[u211E]    \" PRESCRIPTION TAKE
           where .char's first argument defines a groff special character
           escape sequence with a mnemonic glyph name, its second argument is
           a special character escape sequence based on the code point, and
           the comment describes the glyph defined.

           The RFC 1345 glyph names cover a wide range of Unicode code
           points, including supplemental Latin, Greek, Cyrillic, Hebrew,
           Arabic, Hiragana, Katakana, and Bopomofo letters, punctuation,
           math notation, currency symbols, industrial and entertainment
           icons, and box-drawing symbols.

           The Vim digraph table is largely a subset of RFC 1345 (being
           limited to two-character mnemonics), but, as a newer
           implementation, adds several mnemonics not specified in the RFC
           (Latin capital and small letters W and Y with grave accent,
           bullet, horizontal ellipsis, quadruple prime, “approaches the
           limit”, and two mappings each for the Euro and rouble signs).
           These have also been added to rfc1345.tmac.

           rfc1345.tmac contains about 1,700 glyph names.  It is not an error
           to load rfc1345.tmac if your font does not have all the glyphs, as
           long as it contains the glyphs that you actually use in your
           document.

           The RFC 1345 mnemonics are not identical in every case to the
           mappings for special character glyph names that are built in to
           groff; for example, “\[<<]” means the “much less than” sign
           (U+226A) when rfc1345.tmac is not loaded and this special
           character is not otherwise defined by a document or macro package.
           rfc1345.tmac redefines “\[<<]” to the “left-pointing double angle
           quotation mark” (U+00AB).  See groff_char(7) for the full list of
           predefined special character escape sequences.

       Usage
           Load the rfc1345.tmac file.  This can be done by either adding
           “.mso rfc1345.tmac” to your document before the first use of any
           of the glyph names the macro file defines, or by using the
           troff(1) option “-m rfc1345” from the shell.

## [](#Bugs)Bugs

           As the groff Texinfo manual notes, “[o]nly the current font is
           checked for ligatures and kerns; neither special fonts nor
           entities defined with the char request (and its siblings) are
           taken into account.”  Many of the characters defined in
           rfc1345.tmac are accented Latin letters, and will be affected by
           this deficiency, producing subpar typography 
           ⟨https://savannah.gnu.org/bugs/?59932⟩.

## [](#Files)Files

           /usr/local/share/groff/1.24.1/tmac/rfc1345.tmac
                  implements the character mappings.

## [](#Authors)Authors

           rfc1345.tmac was contributed by Dorai Sitaram ⟨ds26gte@yahoo.com⟩.

## [](#See_also)See also

           RFC 1345 ⟨https://tools.ietf.org/html/rfc1345⟩, by Keld Simonsen,
           June 1992.

           The Vim digraph table can be listed using the vim(1) command
           “:help digraph-table”.

           groff_char(7)

## [](#COLOPHON)COLOPHON

           This page is part of the groff (GNU troff) project.  Information
           about the project can be found at 
           ⟨http://www.gnu.org/software/groff/⟩.  If you have a bug report for
           this manual page, see ⟨http://www.gnu.org/software/groff/⟩.  This
           page was obtained from the tarball groff-1.24.1.tar.gz fetched
           from ⟨https://ftp.gnu.org/gnu/groff/⟩ on 2026-08-04.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    groff 1.24.1                    2026-03-14               groff_rfc1345(7)

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
