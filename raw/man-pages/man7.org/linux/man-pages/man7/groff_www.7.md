---
{"title": "groff_www(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/groff_www.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groff_www(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Synopsis](#Synopsis) \| [Description](#Description) \| [Macros](#Macros) \| [Section heading links](#Section_heading_links) \| [Limitations of *grohtml*](#Limitations_of_%3Ci%3Egrohtml%3C/i%3E) \| [Files](#Files) \| [Authors](#Authors) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    groff_www(7)         Miscellaneous Information Manual        groff_www(7)

## [](#Name)Name

           groff_www - GNU roff macros for authoring web pages

## [](#Synopsis)Synopsis

           groff -m www [option ...] [file ...]

## [](#Description)Description

           This manual page describes the GNU www macro package, which is
           part of the groff(7) document formatting system.  This macro file
           is automatically loaded by the default troffrc file when the
           formatter (usually groff(1)) is called with either of the options
           “-T html” or “-T xhtml”.  The HTML output driver grohtml(1) is in
           a beta state; groff distributes these macros to encourage its
           testing.

           Macro       Meaning
           ────────────────────────────────────────────────────────────
           JOBNAME     split output into multiple files
           HX          automatic heading level cut-off
           BCL         specify colours on a web page
           BGIMG       specify background image
           URL         create a URL using two parameters
           MTO         create an HTML email address
           TAG         generate an HTML name
           IMG         include an image file
           PIMG        include PNG image
           MPIMG       place PNG on the margin and wrap text around it
           HnS         begin heading
           HnE         end heading
           LK          emit automatically collected links
           HR          produce a horizontal rule
           NHR         suppress automatic generation of rules
           HTL         record document title as HTML metadata only
           HEAD        add data to <head> block
           ULS         unordered list begin
           ULE         unordered list end
           OLS         ordered list begin
           OLE         ordered list end
           DLS         definition list begin
           DLE         definition list end
           LI          insert a list item
           DC          generate a drop capital
           HTML        transmit raw HTML to output driver
           CDS         code example begin
           CDE         code example end
           ALN         place links on left of main text
           LNS         start two-column table with links on the left
           LNE         end two-column table started with .LNS
           LINKSTYLE   initialize default URL attributes

## [](#Macros)Macros

           JOBNAME file-name-stem
                  Split output into multiple HTML files.  In ms documents, a
                  file is split whenever an .SH or “.NH 1” call is
                  encountered.  Its argument is the file name stem used for
                  output files.  This option is equivalent to grohtml's -j
                  option.

           HX n   Set section heading level above which grohtml is not to
                  automatically generate links to n.  For example, when used
                  with the groff_ms(7) package, “.HX 2” causes grohtml to
                  generate a list of links for ms macro calls “.NH 1” and
                  “.NH 2” but not for “.NH 3”, whereas “.HX 0” generates no
                  hyperlinks to section headings.  Giving groff the option
                  “-P -l” disables automatic heading linkage.

           BCL foreground background active not-visited visited
                  Configure colours used for page foreground, page
                  background, active hypertext link, hypertext links not yet
                  visited, and visited hypertext links.

           BGIMG file
                  Set the background image to file.

           URL url [link-text [post]]
                  Generate a hyperlink to url with optional link-text
                  followed immediately by non-linked text post.

                  If link-text is absent, url is formatted as the link text.
                  Hyphenation is disabled while formatting a URL; insert
                  explicit break points with the \: escape sequence.

           MTO address [link-text [post]]
                  Generate an email hyperlink to address with optional link-
                  text followed immediately by non-linked text post.

                  If link-text is absent, address is formatted as the link
                  text.  Hyphenation is disabled while formatting a URL;
                  insert explicit break points with the \: escape sequence.

           TAG name
                  Generate an anchor name marking its location in the
                  document as a target for hyperlinks.

           IMG file-name [-C|-L|-R] [width [height]]
                  Insert graphical image file-name.  The optional second
                  argument aligns the image to the center (-C; default), left
                  (-L), or right (-R).  The optional width defaults to 100
                  units (in the context of the HTML renderer) and the
                  optional height to the same measurement as width .

           PIMG [-C|-L|-R] file-name [width [height]]
                  Insert graphical image file-name, assumed to be in PNG
                  format.  Compared to IMG, this macro has the advantage of
                  working with both PostScript and HTML devices since it
                  converts file-name into EPS format using pngtopnm(1),
                  pnmcrop(1), and pnmtops(1).  height and width may be given
                  as percentages (of the line length \n[.l] and page length
                  \n[.p], respectively).

                  If the document isn't processed with “-T html” or
                  “-T xhtml”, you must use groff(1)'s -U option.

           MPIMG [-L|-R] [-G gap] file-name [width [height]]
                  As PIMG, but place the image at a margin and wrap text
                  around it.  The image is aligned the to the left (-L,
                  default) or right (-R) margin.  -G gap imposes horizontal
                  space of gap pixels between the picture and the text that
                  wraps around it.  The default gap is zero.

           HnS n  Begin heading at level n.

           HnE    End heading text.

           LK     Direct grohtml to emit the list of automatically generated
                  hyperlinks at this location.

           HR     Generate a full-width horizontal rule when used with
                  “-T html” or “-T xhtml”.

           NHR    Suppress the horizontal rules at the document's top and
                  bottom that grohtml emits by default.

           HTL    Generate an HTML title only.  This differs from
                  groff_ms(7)'s TL macro, which generates both an HTML title
                  and an <H1> heading.  Use it to provide an HTML title as
                  document metadata but not as formatted text.  The title
                  ends when vertical space (.sp) or a break (.br) is seen.

           HEAD   Add arbitrary data to the HTML <head> element.  Ignored if
                  not processed with “-T html” or “-T xhtml”.

           HTML   All text after this macro is treated as raw HTML.  Ignored
                  if not processed with “-T html” or “-T xhtml”.

           DC L text [color]
                  Format a “drop cap”—a large character L (usually a capital
                  letter) at a larger size and with a lower text baseline
                  than the following text, such that the cap-heights of L and
                  text align, in the specified color (default: black).

           CDS    Begin code display; a monospaced font is selected and
                  filling is disabled.

           CDE    End code display.

           ALN [color [width-percentage]]
                  Enable a “navigation pane” containing links to section
                  headings, aligned to the left of running text, and
                  configure its rendering parameters.  Columnation is
                  achieved with an HTML table.  color indicates an HTML
                  background color to be used in the navigation column; the
                  default is #eeeeee.  width-percentage allocates the given
                  percentage of the navigation pane's table column; the
                  default is 30.  Call this macro at most once, at the
                  beginning of the document.

           LNS    Begin text indexed by the navigation pane configured by
                  ALN.

           LNE    End text indexed by navigation pane started by LNS.

           LINKSTYLE color [font-style [open-glyph close-glyph]]
                  Configure rendering of formatted hyperlink targets for
                  devices other than html and xhtml; render targets in color
                  (default: blue) using the typeface font-style (default: CR)
                  bracketed with open-glyph and close-glyph (defaults: \[la]
                  and \[ra], respectively).

## [](#Section_heading_links)Section heading links

           By default grohtml generates links to all section headings and
           places these at the top of the HTML document.  Configure this
           behavior with HX and/or LK.

## [](#Limitations_of_%3Ci%3Egrohtml%3C/i%3E)Limitations of *grohtml*

           tbl(1) tables are rendered as PNG images.

           All URLs currently are treated as consuming no textual space in
           groff.  This could be considered as a bug since it causes some
           problems.  To circumvent this, www.tmac inserts a zero-width
           character which expands to a harmless space (only if run with
           -Thtml or -Txhtml).

           Some of the macros, like ALN, LNS, and LNE, are integrated only
           with the groff_ms(7) package.

## [](#Files)Files

           /usr/local/share/groff/1.24.1/tmac/www.tmac

## [](#Authors)Authors

           The www macro package was written by Gaius Mulley ⟨gaius@glam.ac
           .uk⟩, with additions by Werner Lemberg ⟨wl@gnu.org⟩ and Bernd
           Warken ⟨groff-bernd.warken-72@web.de⟩.

## [](#See_also)See also

           groff(1), troff(1), grohtml(1), netpbm(1)

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

    groff 1.24.1                    2026-03-14                   groff_www(7)

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
