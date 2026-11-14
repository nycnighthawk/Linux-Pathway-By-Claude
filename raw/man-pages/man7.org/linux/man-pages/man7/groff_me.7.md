---
{"title": "groff_me(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/groff_me.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groff_me(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Synopsis](#Synopsis) \| [Description](#Description) \| [Files](#Files) \| [Notes](#Notes) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    groff_me(7)          Miscellaneous Information Manual         groff_me(7)

## [](#Name)Name

           groff_me - “me” macro package for formatting roff documents

## [](#Synopsis)Synopsis

           groff -me [option ...] [file ...]

           groff -m me [option ...] [file ...]

## [](#Description)Description

           The GNU implementation of the me macro package is part of the
           groff document formatting system.  The me package of macro
           definitions for the roff language provides a convenient facility
           for preparing technical papers in various formats.  This version
           is based on the me distributed with 4.4BSD and can be used with
           the GNU troff formatter as well as those descended from AT&T
           troff.

           Some formatter requests affect page layout unpredictably when used
           in conjunction with this package; however, the following may be
           used with impunity after the first call to a paragraphing macro
           like lp or pp.  Some arguments are optional; see groff(7) for
           details, particularly of requests whose argument list is
           designated with an ellipsis.  An asterisk * marks groff
           extensions.

           ad c       set text adjustment mode to c
           af r f     assign format f to register r
           am m e     append to macro m until e called
           as s t     append rest of line t to string s
           bp n       begin new page numbered n
           br         break output line
           ce n       center next n productive input lines
           cp n       en-/disable AT&T troff compatibility mode*
           de m e     define macro m until e called
           do t       interpret input t with compatibility mode off*
           ds s t     define rest of line t as string s
           el t       interpret t if corresponding ie's p false
           fc c d     set field delimiter c and padding glyph d
           fi         enable filling
           hc c       set hyphenation character to c
           hy m       set automatic hyphenation mode to m
           ie p t     as if, but enable interpretation of later el
           if p t     if condition p, interpret rest of line t
           in h       set indentation to distance h
           lc c       set leader repetition glyph to c
           ls n       set line spacing to n
           mc c h     set (right) margin glyph to c at distance h
           mk r       mark vertical position in register r
           na         disable adjustment of text
           ne v       need vertical space of distance v
           nf         disable filling
           nh         disable automatic hyphenation
           nr r n i   assign register r value n with auto-increment i
           ns         begin no-space mode
           pl v       set page length to v
           pn n       set next page number to n
           po h       set page offset to h
           rj n       right-align next n productive input lines*
           rm m       remove macro, string, or request m
           rn m n     rename macro, string, or request m to n
           rr r       remove register r
           rs         resume spacing (end no-space mode)
           rt v       return to vertical position set by mk, or v
           so f       source (interpolate) input file f
           sp n       insert n lines of vertical space
           ta ...     set tab stops
           tc c       set tab repetition glyph to c
           ti h       set temporary indentation (next line only) to h
           tl ...     output three-part title
           tr ...     translate characters
           ul n       underline next n productive input lines

           Except on title pages (produced by calling tp), me suppresses the
           output of vertical space at the tops of pages (after the output of
           any page header); the sp request thus does not work there.  You
           can instead call bl or enclose the desired spacing request in a
           diversion, for instance by calling (b and )b.  me also intercepts
           the ll request; see the “me Reference Manual” for details.

       Name space
           Objects in me follow a rigid naming convention.  To avoid
           conflict, any user-defined register, string, or macro names should
           be single numerals or uppercase letters, or any longer sequence of
           letters and numerals with at least one uppercase letter.  (For
           portability between BSD and groff me, limit names to two
           characters, and avoid the name [ (left square bracket).)  The
           names employed by any preprocessors in use should also not be
           repurposed.

       Macros
           $0   post-section heading hook
           $1   pre-section depth 1 hook
           $2   pre-section depth 2 hook
           $3   pre-section depth 3 hook
           $4   pre-section depth 4 hook
           $5   pre-section depth 5 hook
           $6   pre-section depth 6 hook
           $C   post-chapter title hook
           $H   page/column heading hook
           $c   output chapter number and title
           $f   output footer
           $h   output header
           $p   output section heading
           $s   output footnote area separator
           (b   begin block
           (c   begin centered block
           (d   begin delayed text
           (f   begin footnote
           (l   begin list
           (q   begin long quotation
           (x   begin index entry
           (z   begin floating keep
           )b   end block
           )c   end centered block
           )d   end delayed text
           )f   end footnote
           )l   end list
           )q   end long quotation
           )x   end index entry
           )z   end floating keep
           ++   set document segment type
           +c   begin chapter
           1c   end multi-column layout
           2c   begin multi-column layout
           EN   end eqn equation
           EQ   begin eqn equation
           GE   end grn picture with drawing position at bottom
           GF   end grn picture with drawing position at top
           GS   start grn picture
           IE   end ideal picture with drawing position at bottom
           IF   end ideal picture with drawing position at top
           IS   start ideal picture
           PE   end pic picture with drawing position at bottom
           PF   end pic picture with drawing position at top
           PS   start pic picture
           TE   end tbl table
           TH   end heading for multi-page tbl table
           TS   start tbl table
           b    embolden argument
           ba   set base indentation
           bc   begin new column
           bi   embolden and italicize argument
           bx   box argument
           ef   set even-numbered page footer
           eh   set even-numbered page header
           ep   end page
           fo   set footer
           he   set header
           hl   draw horizontal line
           hx   suppress next page's headers/footers
           i    italicize argument
           ip   begin indented paragraph
           ld   reset localization and date registers and strings*
           ll   set line length
           lp   begin fully left-aligned paragraph
           np   begin numbered paragraph
           of   set odd-numbered page footer
           oh   set odd-numbered page header
           pd   output delayed text
           pp   begin first-line indented paragraph
           q    quote argument
           r    set argument in roman
           re   reset tab stops
           sh   begin numbered section
           sm   set argument at smaller type size
           sx   change section depth
           sz   set type size and vertical spacing
           tp   begin title page
           u    underline argument
           uh   begin unnumbered section
           xl   set line length (current environment only)
           xp   output index

           Some macros are provided for “old” roff(1) compatibility.  The “me
           Reference Manual” describes alternatives for modern documents.

           ar   use Arabic numerals for page numbers
           bl   insert space (even at page top; cf. sp)
           ix   set indentation without break
           m1   set page top to header distance
           m2   set header to text distance
           m3   set text to footer distance
           m4   set footer to page bottom distance
           n1   begin output line numbering
           n2   end or alter output line numbering
           pa   begin page
           ro   use Roman numerals for page numbers
           sk   skip next page

       Registers
           $0   section depth
           $1   first section number component
           $2   second section number component
           $3   third section number component
           $4   fourth section number component
           $5   fifth section number component
           $6   sixth section number component
           $c   current column number
           $d   delayed text number
           $f   footnote number
           $i   paragraph base indentation
           $l   column width
           $m   number of available columns
           $p   numbered paragraph number
           $s   column spacing (indentation)
           bi   display (block) indentation
           bm   distance from text area to page bottom
           bs   display (block) pre/post space
           bt   block threshold for keeps
           ch   current chapter number
           df   display font
           dv   vertical spacing of displayed text (as percentage)*
           es   equation pre/post space
           ff   footnote font
           fi   footnote indentation (first line only)
           fm   footer margin
           fp   footnote type size in points
           fs   footnote prespace
           fu   footnote undent (right indentation)
           hm   header margin
           ii   indented paragraph indentation
           no   line numbering offset*
           pf   paragraph font
           pi   paragraph indentation
           po   page offset
           pp   paragraph type size in points
           ps   paragraph prespace
           qi   long quotation left/right indentation
           qp   long quotation type size in points
           qs   long quotation pre/post space
           sf   section title font
           si   section indentation per level of depth
           so   additional section title offset
           sp   section title type size in points
           ss   section prespace
           sx   super/subscript line height increase*
           tf   title font
           tm   distance from page top to text area
           tp   title type size in points
           tv   vertical spacing of text (as percentage)*
           xs   index entry prespace
           xu   index undent (right indentation)
           y2   year of the century*
           y4   year*
           yr   year minus 1900
           zs   floating keep pre/post space

       Strings
           #    delayed text marker
           $n   catenated section number
           *    footnote marker
           -    em dash
           <    begin subscripting
           >    end subscripting
           dw   weekday name
           lq   left double quotation mark
           mo   month name
           rq   right double quotation mark
           td   date
           wa   term for “appendix” used by .$c*
           wc   term for “chapter” used by .$c*
           {    begin superscripting
           }    end superscripting

## [](#Files)Files

           /usr/local/share/groff/1.24.1/tmac/e.tmac
                  implements the package.

           /usr/local/share/groff/1.24.1/tmac/refer-me.tmac
                  implements refer(1) support for me.

           /usr/local/share/groff/1.24.1/tmac/me.tmac
                  is a wrapper enabling the package to be loaded with the
                  option “-m me”.

## [](#Notes)Notes

           Some early roff macro packages limited their names to a single
           letter, which followed the formatter's m option, resulting in
           “names” like -mm, -ms, -mv, and -mn.  me's “e” stands for “Eric P.
           Allman”, the author of the original macro package and the
           technical papers documenting it.

## [](#See_also)See also

           Two manuals are available in source and rendered form.  On your
           system, they may be compressed and/or available in additional
           formats.

           /usr/local/share/doc/groff-1.24.1/meintro.me
           /usr/local/share/doc/groff-1.24.1/meintro.ps
                  is “Writing Papers with Groff Using -me”, by Eric P.
                  Allman, adapted for groff by James Clark.

           /usr/local/share/doc/groff-1.24.1/meref.me
           /usr/local/share/doc/groff-1.24.1/meref.ps
                  is the “me Reference Manual”, by Eric P. Allman, adapted
                  for groff by James Clark and G. Branden Robinson.

           Groff: The GNU Implementation of troff, by Trent A. Fisher and
           Werner Lemberg, is the primary groff manual.  You can browse it
           interactively with “info groff”.

           For preprocessors supported by me, see eqn(1), grn(1), pic(1),
           refer(1), and tbl(1).

           groff(1), troff(1), groff(7)

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

    groff 1.24.1                    2026-03-14                    groff_me(7)

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
