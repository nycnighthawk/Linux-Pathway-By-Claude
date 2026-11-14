---
{"title": "gropdf(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/gropdf.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gropdf(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Synopsis](#Synopsis) \| [Description](#Description) \| [Options](#Options) \| [Usage](#Usage) \| [Font installation](#Font_installation) \| [Exit status](#Exit_status) \| [Environment](#Environment) \| [Files](#Files) \| [Authors](#Authors) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    gropdf(1)                General Commands Manual                gropdf(1)

## [](#Name)Name

           gropdf - groff output driver for Portable Document Format

## [](#Synopsis)Synopsis

           gropdf [-delsW] [{-f|--format-options} bit-vector] [-F font-
                  directory] [-I inclusion-directory] [-p paper-format]
                  [--pdfver {1.4|1.7}] [-u [cmap-file]] [-y foundry]
                  [file ...]

           gropdf --help

           gropdf -v

           gropdf --version

## [](#Description)Description

           The GNU roff PDF output driver translates the output of troff(1)
           into Portable Document Format.  Normally, gropdf is invoked by
           groff(1) when the latter is given the “-T pdf” option.  (In this
           installation, ps is the default output device.)  Use groff's -P
           option to pass any options shown above to gropdf.  If no file
           arguments are given, or if file is “-”, gropdf reads the standard
           input stream.  It writes to the standard output stream.

           See section “Font installation” below for a guide to installing
           fonts for gropdf.

## [](#Options)Options

           --help displays a usage message, while -v and --version show
           version information; all exit afterward.

           -d     Include debug information as comments within the PDF.  Also
                  produces an uncompressed PDF.

           -e     Forces gropdf to embed all fonts (even the 14 base PDF
                  fonts).

           --format-options bit-vector
           -f bit-vector
                  Specify advanced options for gropdf.  Familiarity with the
                  ISO 32000 PDF standard ⟨https://www.pdfa-inc.org/product/
                  iso-32000-2-pdf-2-0-bundle-sponsored-access/⟩ is helpful.
                  The bit-vector argument is an integer that configures
                  characteristics of the generated PDF.  Add the following
                  values to combine them.

                         Value   Meaning
                         ─────────────────────────────────────────────────────
                         1       Subset included Type 1 fonts.
                         2       Use more compact format for text by
                                 including space as a character.  Fonts that
                                 do not include space as a glyph may conflict
                                 with this feature.
                         4       Compress all data streams.
                         8       Don't embed font files.  (A font required by
                                 the document is not embedded; usually not
                                 useful.)

                  The default feature combination is 7.  To mimic what gropdf
                  from groff 1.23 produced, specify “6” to turn off
                  subsetting.

           -F dir Prepend directory dir/devname to the search path for font,
                  and device description files; name is the name of the
                  device, usually pdf.

           -I dir Search the directory dir for files named in \X'pdf: pdfpic'
                  device extension commands.  -I may be specified more than
                  once; each dir is searched in the given order.  To search
                  the current working directory before others, add “-I .” at
                  the desired place; it is otherwise searched last.

           -l     Orient the document in landscape format.

           -p paper-format
                  Set the physical dimensions of the output medium.  This
                  overrides the papersize, paperlength, and paperwidth
                  directives in the DESC file; it accepts the same arguments
                  as the papersize directive.  See groff_font(5) for details.

           --pdfver {1.4|1.7}
                  PDF version 1.7 introduced a more compact object format;
                  this is now the default.  If you require the original
                  format (as produced by gropdf 1.23) set the version to 1.4.

           -s     Append a comment line to end of PDF showing statistics,
                  i.e. number of pages in document.  Ghostscript's ps2pdf
                  complains about this line if it is included, but works
                  anyway.

           -u [cmap-file]
                  gropdf normally includes a ToUnicode CMap with any font
                  created using text.enc as the encoding file, this makes it
                  easier to search for words which contain ligatures.  You
                  can include your own CMap by specifying a cmap-file or have
                  no CMap at all by omitting the argument.

           -W     Exit with failure status if any warnings are issued.

           -y foundry
                  Set the foundry to use for selecting fonts of the same
                  name.

## [](#Usage)Usage

           gropdf's input must be in the format produced by troff(1) and
           described in groff_out(5).  Further, its device and font
           description files must meet certain requirements.  The device
           resolution must be an integer multiple of 72 times sizescale.  By
           default, gropdf uses a resolution of 72000 and a sizescale of
           1000.  A valid paper format is mandatory; see groff_font(5).
           While the PDF standard allows several font file formats (like
           TrueType), at present gropdf accepts only the same Type 1 Adobe
           PostScript format as grops(1).  Fewer Type 1 fonts are supported
           natively in PDF documents than the standard 35 fonts supported by
           grops and PostScript printers, but all are available since gropdf
           automatically embeds any that aren't specified by the PDF
           standard.

           gropdf supports foundries that permit multiple providers to supply
           the same groff font names.  groff's compilation process attempts
           to locate Type 1 fonts on the system, populates a Foundry file
           with their locations, and generates font description files
           corresponding to them.  Font description files can also be added
           after installation.  Each such file must contain a directive
                  internalname psname
           that maps the groff font name (such as “TR”) to a PostScript name
           (such as “Times-Roman”).  Lines starting with # and blank lines
           are ignored.  The code for each character given in the font file
           must correspond to the code in the default encoding for the font.
           This code can be used with the \N escape sequence in troff to
           select the character even if it lacks a special character name.
           Every character in the font description must exist in the font
           file, and the widths given in the description must match those
           used in the font file.  See groff_font(5).

           gropdf can automatically embed any downloadable fonts necessary to
           print the document.  Any fonts thus required must be listed in the
           file /usr/local/share/groff/1.24.1/font/devpdf/download, which
           should comprise lines of the form
                  foundry font file-name
           where foundry is the foundry name, or blank for the default
           foundry; font is the PostScript name of the font, and file-name is
           the name of the PFA or PFB font file, and can be a pathname (can
           contain slashes).  Any lines beginning with # and blank lines are
           ignored; fields must be separated by tabs (spaces are not
           allowed); if file-name is not a pathname, it is sought using the
           same mechanism as that used for font metric files.  The download
           file itself is also sought using this mechanism.  Foundry names
           are usually a single character (such as ‘U’ for the URW foundry)
           or empty for the default foundry.  This default uses the same
           fonts as Ghostscript uses when it embeds fonts in a PDF file.

           The default stroke and fill colors are black.

       Typefaces
           Styles called R, I, B, and BI mounted at font positions 1 to 4.
           Text fonts are grouped into families A, BM, C, H, HN, N, P, and T,
           each having members in each of these styles.

                  AR     AvantGarde-Book
                  AI     AvantGarde-BookOblique
                  AB     AvantGarde-Demi
                  ABI    AvantGarde-DemiOblique
                  BMR    Bookman-Light
                  BMI    Bookman-LightItalic
                  BMB    Bookman-Demi
                  BMBI   Bookman-DemiItalic
                  CR     Courier
                  CI     Courier-Oblique
                  CB     Courier-Bold
                  CBI    Courier-BoldOblique
                  HR     Helvetica
                  HI     Helvetica-Oblique
                  HB     Helvetica-Bold
                  HBI    Helvetica-BoldOblique
                  HNR    Helvetica-Narrow
                  HNI    Helvetica-Narrow-Oblique
                  HNB    Helvetica-Narrow-Bold
                  HNBI   Helvetica-Narrow-BoldOblique
                  NR     NewCenturySchlbk-Roman
                  NI     NewCenturySchlbk-Italic
                  NB     NewCenturySchlbk-Bold
                  NBI    NewCenturySchlbk-BoldItalic
                  PR     Palatino-Roman
                  PI     Palatino-Italic
                  PB     Palatino-Bold
                  PBI    Palatino-BoldItalic
                  TR     Times-Roman
                  TI     Times-Italic
                  TB     Times-Bold
                  TBI    Times-BoldItalic

           Another text font is not a member of a family.

                  ZCMI   ZapfChancery-MediumItalic

           Special fonts include S, the PostScript Symbol font; SS, a subset
           of S with slanted lowercase Greek letters; EURO, which offers a
           Euro glyph in several styles for use with old devices lacking it;
           and ZD, Zapf Dingbats.  In contrast to grops, gropdf does not
           require a reversed variant of it (ZDR); the “hand pointing left”
           glyph (\[lh]) is available nevertheless, since pdf.tmac defines it
           using the \X'pdf: xrev' device extension command (see below).
           Some glyphs in these fonts are unnamed and must be accessed as
           indexed characters, using the \N escape sequence.

           The fonts corresponding to EURO and SS are unknown to the PDF
           standard; groff therefore provides their AFM files (font metrics)
           and PFA or PFB files so that they can be used with other software
           and embedded in PDF output.

       Feature service levels and URW font support
           The traditional PostScript Type 1 fonts are limited in their glyph
           repertoire, and the original versions from the Adobe foundry are
           not free software.  Historically, because their presence was
           mandated by the PostScript standard, one could expect to find
           support for them in any conforming device or software PostScript
           renderer.  PostScript (“Level 1”) initially standardized 14
           typefaces: Times, Helvetica, and Courier each in four styles
           (which groff groups into “families”); a symbol font; and a
           dingbats font.  PostScript Level 2 increased the number to 35,
           adding the families Avant Garde, Bookman, Helvetica Narrow, New
           Century Schoolbook, and Palatino; and a text font in one style,
           Zapf Chancery medium italic.  A document could be small because it
           did not need to embed font resources unless it had unusual (for
           the time) glyph or typeface requirements.  This situation carried
           over into the early years of PostScript's successor page
           description language, PDF.  Nowadays, it is common to embed fonts
           in PDFs, and authorities widely recommend this practice, which
           increases the reliability of document rendering, and many free
           software fonts are available with much greater glyph coverage than
           Adobe's Type 1 fonts for PostScript.

           gropdf attempts to work in variety of scenarios, and delivers
           better results when configured with supporting digital font files
           (for embedding) and font metrics files describing those fonts to
           the formatter.

           •  Full service is available when gropdf can locate all 35 fonts
              of the PostScript Level 2 standard on the file system along
              with their corresponding font metrics (AFM) files.  The Adobe-
              compatible unnamed (default) foundry supports up to 256 glyphs
              in each typeface.  Fonts from the URW foundry (“U”) are
              compatible extensions of the Adobe fonts with extended glyph
              coverage, including support for Cyrillic script.  groff's build
              process uses afmtodit(1) to generate font description files
              from the URW foundry's AFM files; see section “Files” below.

           •  Intermediate service is available when gropdf can locate all 35
              fonts of the PostScript Level 2 standard but not their
              corresponding font metrics (AFM) files.  groff's build process
              copies the font description files from those for the grops(1)
              driver, reusing them for gropdf; this reduces glyph coverage to
              256 glyphs maximum from each face, and the “U” foundry is
              unavailable.

           •  Basic service results when gropdf cannot locate all 35 fonts of
              the PostScript Level 2 standard.  Only the base 14 fonts of the
              PDF standard are available, and only in the sense that the
              formatter can use their metrics (copied from grops() font
              descriptions as described above).  Use of the -e option to
              embed fonts in the generated PDF results in an error.

       Device extension commands
           gropdf supports many device extensions, accessed with the groff
           request device or roff \X escape sequence.  First, it understands
           many of the device extensions supported by grops(1).

           \X'ps: invis'
                  Suppress output.

           \X'ps: endinvis'
                  Stop suppressing output.

           \X'ps: exec gsave currentpoint 2 copy translate n rotate neg exch
           neg exch translate'
                  where n is the angle of rotation.  This is to support the
                  align command in pic(1).

           \X'ps: exec grestore'
                  Used by pic(1) to restore state after rotation.

           \X'ps: exec n setlinejoin'
                  where n can be one of the following values.

                  0 = Miter join
                  1 = Round join
                  2 = Bevel join

           \X'ps: exec n setlinecap'
                  where n can be one of the following values.

                  0 = Butt cap
                  1 = Round cap, and
                  2 = Projecting square cap

           gropdf also supports a subset of the commands introduced in
           gpresent's present.tmac.

                  PAUSE
                  BLOCKS
                  BLOCKE

           These allow you to create presentation PDFs.  Many of the other
           commands are already available in other macro packages.

           These commands are implemented with groff X commands:-

           \X'ps: exec %%%%PAUSE'
                  The section before this is treated as a block and is
                  introduced using the current BLOCK transition setting (see
                  “\X'pdf: transition'” below).  Equivalently, .pdfpause is
                  available as a macro.

           \X'ps: exec %%%%BEGINONCE'
                  Any text following this command (up to %%%%ENDONCE) is
                  shown only once, the next %%%%PAUSE will remove it.  If
                  producing a non-presentation PDF, i.e. ignoring the pauses,
                  see GROPDF_NOSLIDE below, this text is ignored.

           \X'ps: exec %%%%ENDONCE'
                  This terminates the block defined by %%%%BEGINONCE.  This
                  pair of commands is what implements the .BLOCKS
                  Once/.BLOCKE commands in present.tmac.

           The mom macro package already integrates these extensions, so you
           can build slides with mom.

           If you use present.tmac with gropdf there is no need to run the
           program presentps(1) since the output will already be a
           presentation PDF.

           All other ps: tags are silently ignored.

           gropdf also recognizes a device extension used by the DVI driver.

           \X'papersize=width,length'
                  Set the page dimensions in centimeters to width by length.
                  If the -l option was specified, these dimensions are
                  swapped.  Changes to the paper dimensions should occur
                  prior to the first page, or during page ejection before
                  starting a subsequent one.

                  Caution: the ordering of dimensions differs from that used
                  by papersize.tmac and troff(1)'s “-d paper” option.

           \X'pdf: markstart /ANN-definition'
           \X'pdf: markend'
                  Macros that support PDF features use these extension
                  commands internally to bracket hotspot text (a hyperlink).
                  User documents should call the .pdfhref macro instead.
                  Their application is found in other macro packages (like
                  groff_man(7) or groff_mdoc(7)) that call .pdfhref with a -S
                  argument, then indicate the end of hotspot text with
                  \X'pdf: markend'\m[\*[pdf:curcol]].

           \X'pdf: xrev'
                  Toggle the reversal of glyph direction.  This feature works
                  by reversing all following text.  Each separate letter is
                  also mirrored.  One application is the reversal of glyphs
                  in the Zapf Dingbats font.  To restore the normal glyph
                  orientation, repeat the command.

           gropdf supports several more device extensions using the pdf: tag.
           The following have counterpart convenience macros that take the
           same arguments and behave equivalently.

           .pdfbackground cmd left top right bottom weight
           .pdfbackground off
           .pdfbackground footnote bottom
           \X'pdf: background cmd left top right bottom weight'
           \X'pdf: background off'
           \X'pdf: background footnote bottom'
                  Produce a background rectangle on the page.

                  cmd    is the command, which can be any of “page|fill|box”
                         in combination.  Thus, “pagefill” would draw a
                         rectangle which covers the whole current page size
                         (in which case the rest of the parameters can be
                         omitted because the box dimensions are taken from
                         the current media size).  “boxfill”, on the other
                         hand, requires the given dimensions to place the
                         box.  Including “fill” in the command paints the
                         rectangle with the current fill colour (as with
                         \M[]) and including “box” gives the rectangle a
                         border in the current stroke colour (as with \m[]).

                         cmd may also be “off” on its own, which terminates
                         drawing the current box.  If you have specified a
                         page colour with “pagefill”, it is always the first
                         box in the stack, and if you specify it again, it
                         replaces the first entry.  Be aware that the
                         “pagefill” box renders the page opaque, so tools
                         that “watermark” PDF pages are unlikely to be
                         successful.  To return the background to
                         transparent, issue an “off” command with no other
                         boxes open.

                         Finally, cmd may be “footnote” followed by a new
                         value for bottom, which is used for all open boxes
                         on the current page.  This is to allow room for
                         footnote areas that grow while a page is processed
                         (to accommodate multiple footnotes, for instance).
                         (If the value is negative, it is used as an offset
                         from the bottom of the page.)

                  left
                  top
                  right
                  bottom are the coordinates of the box.  The top and bottom
                         coordinates are the minimum and maximum for the box,
                         since the actual start of the box is groff's drawing
                         position when you issue the command, and the bottom
                         of the box is the point where you turn the box
                         “off”.  The top and bottom coordinates are used only
                         if the box drawing extends onto the next page;
                         ordinarily, they would be set to the header and
                         footer margins.

                  weight provides the line width for the border if “box” is
                         included in the command.

                  An sboxes macro file is also available; see groff_tmac(5).

           .pdfmarksuspend
           .pdfmarkrestart
           \X'pdf: marksuspend'
           \X'pdf: markrestart'
                  If you use a page location trap to produce a header or
                  footer, or otherwise interrupt a document's text, you need
                  to use these commands if a PDF hotspot crosses a trap
                  boundary; otherwise any text output by the trap will be
                  marked as part of the hotspot.  To prevent this error,
                  place these device extension escape sequences or their
                  corresponding convenience macros .pdfmarksuspend and
                  .pdfmarkrestart at the start and end of the trap macro,
                  respectively.

           .pdfpagename name
           \X'pdf: pagename name'
                  Assign the current page a name.  All documents bear two
                  default names, ‘top’ and ‘bottom’.

           .pdfpagenumbering type prefix start
           \X'pdf: pagenumbering type prefix start'
                  Control the page numbering shown in a PDF reader's outline
                  (which also contains bookmarks).  Normally, the page number
                  associated with each bookmark is its sequence number in the
                  file, but this might not match the desired numbering
                  scheme.  A document may bear a cover sheet (which has no
                  page number); front matter (possibly including a table of
                  contents) that uses lowercase roman numerals; the main
                  matter, which uses arabic numerals; and back matter, which
                  may include appendices that are each prefixed with a letter
                  and independently numbered.  Place this command prior to
                  breaking the page to which the new numbering scheme is to
                  apply.  It then persists until changed again.

                  type   specifies the numbering system to use. It should be
                         one of “Decimal”, “Roman”, “roman”, “Alpha”, or
                         “alpha”.  This parameter may be abbreviated to the
                         first letter, whose lettercase determines that used
                         for the numbers where applicable.  The ordering used
                         by the alphabetic numbering systems is A-Z ... AA-AZ
                         ... ZA-ZZ.  type can also be “.”, which selects no
                         numbering system; you may still provide a prefix.

                  prefix specifies text to precede the page number.  For
                         example, to number the pages of an appendix “A-1”,
                         “A-2”, and so forth, use a prefix of “A-” and a type
                         of “Decimal”.

                  start  determines the page number.  It defaults to 1.

           .pdfpic file alignment width height line-length
           \X'pdf: pdfpic file alignment width height line-length'
                  Place an image from file file of desired width and height
                  (if height is missing or zero then it is scaled
                  proportionally).  If alignment is -L the drawing is left-
                  aligned.  If it is -C or -R a line-length greater than the
                  width of the drawing is required as well.  If width is
                  specified as zero then the width is scaled in proportion to
                  the height.  If both width and height are non-zero the
                  image is scaled to ‘best fit’.

                  The availability of other software on the system, such as
                  PerlMagick, influences the types of image files gropdf can
                  embed in its output.

                 ┌───────┬──────┬─────────┬─────────────┬────────────────────┐
                 │       │ none │ file(1) │ identify(1) │ Image::Magick(3pm) │
                 ├───────┼──────┼─────────┼─────────────┼────────────────────┤
                 │ .pdf  │  ✓   │    ✓    │      ✓      │         ✓          │
                 ├───────┼──────┼─────────┼─────────────┼────────────────────┤
                 │ .jpg  │  ✗   │    ✓    │      ✓      │         ✓          │
                 ├───────┼──────┼─────────┼─────────────┼────────────────────┤
                 │ .jp2  │  ✗   │    ✗    │      ✓      │         ✓          │
                 ├───────┼──────┼─────────┼─────────────┼────────────────────┤
                 │ other │  ✗   │    ✗    │      ✗      │         ✓          │
                 └───────┴──────┴─────────┴─────────────┴────────────────────┘

                  See groff_tmac(5) for a description of the PDFPIC macro,
                  which provides a convenient high-level interface for
                  inclusion of various graphic file formats.

           .pdfswitchtopage when name
           \X'pdf: switchtopage when name'
                  Normally each new page is appended to the end of the
                  document, this command allows following pages to be
                  inserted at a ‘named’ position within the document (see
                  pagename command above).  ‘when’ can be either ‘after’ or
                  ‘before’.  If it is omitted it defaults to ‘before’.  It
                  should be used at the end of the page before you want the
                  switch to happen.  This allows pages such as a TOC to be
                  moved to elsewhere in the document, but more esoteric uses
                  are possible.

           .pdftransition scope mode duration dimension motion direction
           scale bool
           \X'pdf: transition scope mode duration dimension motion direction
           scale bool'
                  Configure the style of page transitions, as used in
                  “slides” (or “foils”).  scope can be either SLIDE or BLOCK.
                  SLIDE applies the transition when a new slide is introduced
                  to the screen; BLOCK applies it to the individual blocks
                  making up the slide.

                  mode is the transition type between slides:-

                         Split - Two lines sweep across the screen, revealing
                         the new page.  The lines may be either horizontal or
                         vertical and may move inward from the edges of the
                         page or outward from the center, as specified by the
                         dimension and motion entries, respectively.
                         Blinds - Multiple lines, evenly spaced across the
                         screen, synchronously sweep in the same direction to
                         reveal the new page.  The lines may be either
                         horizontal or vertical, as specified by the
                         dimension entry.  Horizontal lines move downward;
                         vertical lines move to the right.
                         Box - A rectangular box sweeps inward from the edges
                         of the page or outward from the center, as specified
                         by the motion entry, revealing the new page.
                         Wipe - A single line sweeps across the screen from
                         one edge to the other in the direction specified by
                         the direction entry, revealing the new page.
                         Dissolve - The old page dissolves gradually to
                         reveal the new one.
                         Glitter - As Dissolve, except that the effect sweeps
                         across the page in a wide band moving from one side
                         of the screen to the other in the direction
                         specified by the direction entry.
                         R - The new page simply replaces the old one with no
                         special transition effect; the direction entry shall
                         be ignored.
                         Fly - (PDF 1.5) Changes are flown out or in (as
                         specified by motion), in the direction specified by
                         direction, to or from a location that is offscreen
                         except when direction is None.
                         Push - (PDF 1.5) The old page slides off the screen
                         while the new page slides in, pushing the old page
                         out in the direction specified by direction.
                         Cover - (PDF 1.5) The new page slides on to the
                         screen in the direction specified by direction,
                         covering the old page.
                         Uncover - (PDF 1.5) The old page slides off the
                         screen in the direction specified by direction,
                         uncovering the new page in the direction specified
                         by direction.
                         Fade - (PDF 1.5) The new page gradually becomes
                         visible through the old one.

                  duration is the length of the transition in seconds
                  (default 1).

                  dimension (Optional; Split and Blinds transition styles
                  only) The dimension in which the specified transition
                  effect shall occur: H Horizontal, or V Vertical.

                  motion (Optional; Split, Box and Fly transition styles
                  only) The direction of motion for the specified transition
                  effect: I Inward from the edges of the page, or O Outward
                  from the center of the page.

                  direction (Optional; Wipe, Glitter, Fly, Cover, Uncover and
                  Push transition styles only) The direction in which the
                  specified transition effect shall moves, expressed in
                  degrees counterclockwise starting from a left-to-right
                  direction.  If the value is a number, it shall be one of: 0
                  = Left to right, 90 = Bottom to top (Wipe only), 180 =
                  Right to left (Wipe only), 270 = Top to bottom, 315 = Top-
                  left to bottom-right (Glitter only) The value can be None,
                  which is relevant only for the Fly transition when the
                  value of scale is not 1.0.

                  scale (Optional; PDF 1.5; Fly transition style only) The
                  starting or ending scale at which the changes shall be
                  drawn.  If motion specifies an inward transition, the scale
                  of the changes drawn shall progress from scale to 1.0 over
                  the course of the transition.  If motion specifies an
                  outward transition, the scale of the changes drawn shall
                  progress from 1.0 to scale over the course of the
                  transition

                  bool (Optional; PDF 1.5; Fly transition style only) If
                  true, the area that shall be flown in is rectangular and
                  opaque.

                  Any of the parameters may be replaced with a "." which
                  signifies the parameter retains its previous value, also
                  any trailing missing parameters are ignored.

                  Note: not all PDF Readers support any or all these
                  transitions.

       Macros
           gropdf's support macros in pdf.tmac define the convenience macros
           described above.  Some features have no direct device extension
           escape sequence counterpart.

           .pdfbookmark [-T tag-name] level text
                  Mark the nearest page location as a bookmark, and
                  optionally a named destination as well.  Bookmarks populate
                  the outline pane of the reader.  They are organized into a
                  hierarchical tree; each level of the tree is numbered,
                  starting at 1, and named as text in the outline.  Named
                  destinations permit hyperlink-style navigation within the
                  document.  Specifying -T followed by tag-name creates a
                  named destination making the page location eligible as a
                  target named by “.pdfhref L ...”.

           .pdfhref L -D dest [-S] [-P prefix-text] [-A suffix-text] [link-
           text]
                  Create a hotspot link to dest, (the tag-name) which a
                  “.pdfbookmark ...” or “.pdfhref M ...” call elsewhere in
                  the document should define.  (If the document employs
                  forward references, it must be processed twice; see
                  pdfmom(1).)  If link-text is omitted the text associated
                  with dest, when it was created, is formatted as the link
                  text.  The -P and -A arguments format their successors as
                  text before and after the link text, respectively, without
                  intervening space.  Specifying -S prevents pdfhref from
                  “closing” the hotspot, requiring the document (or macro
                  package wrapping pdfhref) to do so itself with “\X'pdf:
                  markend'\m[\*[pdf:curcol]]”.

           .pdfhref M [-E] [-N tag-name] dest
                  Mark the nearest page location as a destination named (the
                  first word of) dest, which should be unique within a
                  document.  Specifying -T followed by tag-name overrides
                  this default.  Specifying -E formats dest as text in the
                  document as well.

           .pdfhref W -D uri [-S] [-P prefix-text] [-A suffix-text] link-text
                  Create a hotspot link to uri, a World Wide Web Universal
                  Resource Identifier (URI).  The -P and -A arguments format
                  their successors as text before and after the link text,
                  respectively, without intervening space.  Specifying -S
                  prevents pdfhref from “closing” the hotspot, requiring the
                  document (or macro package wrapping pdfhref) to do so
                  itself with “\X'pdf: markend'\m[\*[pdf:curcol]]”.

           .pdfinfo /field content ...
                  Define PDF metadata.  field may be one of Title, Author,
                  Subject, Keywords, or another datum supported by the PDF
                  standard or your reader.  field must be prefixed with a
                  slash.

           .pdfnote [-T title] text
                  Create an annotation in the document.  Reader support for
                  this feature varies.  Some place an icon at the current
                  position on the page; hovering over the icon reveals any
                  title, while clicking on the icon pops up a window
                  containing text.

       Parameters
           The following parameters, shown as roff control lines, affect the
           operation of gropdf.

           ┌────────────────────────────────────────────────────────────────┐
           │        Parameter                Purpose            Default     │
           ├────────────────────────────────────────────────────────────────┤
           │ .nr PDFNOTE.WIDTH          Set width of         1c             │
           │                            annotation icon.                    │
           │ .nr PDFNOTE.HEIGHT         Set height of        1c             │
           │                            annotation icon.                    │
           │ .ds PDFNOTE.COLOR          Set RGB color of     1.00 1.00 0.00 │
           │                            annotation icon                     │
           │                            (RGB)                               │
           │ .ds PDFNOTE.OPACITY        Set opacity of       0.6            │
           │                            annotation icon                     │
           │                            (decimal value in                   │
           │                            [0, 1]).                            │
           │ .nr PDFOUTLINE.FOLDLEVEL   Set depth of         10000          │
           │                            visible bookmark                    │
           │                            hierarchy.                          │
           │ .nr PDFHREF.VIEW.LEADING   Set position         5p             │
           │                            adjustment when                     │
           │                            clicking bookmark                   │
           │                            or internal                         │
           │                            hotspot.                            │
           │ .nr PDFHREF.LEADING        Configure size of    2.0p           │
           │                            increased                           │
           │                            clickable area                      │
           │                            around a hotspot.                   │
           │ .ds PDFHREF.BORDER         Configure the        0 0 0          │
           │                            border width                        │
           │                            around a hotspot                    │
           │                            by specifying two                   │
           │                            zeroes followed by                  │
           │                            the desired width                   │
           │                            in points.  Do not                  │
           │                            use a scaling                       │
           │                            unit.                               │
           │ .ds PDFHREF.COLOR          Set RGB color of     0.00 0.35 0.60 │
           │                            link text.                          │
           └────────────────────────────────────────────────────────────────┘

           In the foregoing, you can also spell “COLOR” in string names as
           “COLOUR”.

       Importing PDF graphics
           If you are importing an image as a PDF file, it must be a single
           page and the drawing must just fit inside the media size of the
           PDF file.  In inkscape(1) or gimp(1), for example, make sure the
           canvas size just fits the image.

           The PDF parser gropdf implements has not been rigorously tested
           with all applications that produce PDF.  If you find a single-page
           PDF which fails to import properly, try processing it with the
           pdftk(1) program.
                  pdftk existing-file output new-file
           You may find that new-file imports successfully.

       TrueType and other font formats
           gropdf does not yet support any font formats besides Adobe Type 1
           (PFA or PFB).

## [](#Font_installation)Font installation

           For your convenience, groff offers install-font.bash, a shell
           script that interactively assists the configuration of fonts for
           use with the GNU troff formatter and the gropdf output driver.
           See section “Files” below.

           The following is a step-by-step font installation guide for
           gropdf.

           •  Convert your font to something groff understands.  This is a
              PostScript Type 1 font in PFA or PFB format, together with an
              AFM file.  A PFA file begins as follows.
                     %!PS-AdobeFont-1.0:
              A PFB file contains this string as well, preceded by some non-
              printing bytes.  In the following steps, we will consider the
              use of CTAN's BrushScriptX-Italic 
              ⟨https://ctan.org/tex-archive/fonts/brushscr⟩ font in PFA
              format.

           •  Convert the AFM file to a groff font description file with the
              afmtodit(1) program.  For instance,
                     $ afmtodit BrushScriptX-Italic.afm text.map BSI
              converts the Adobe Font Metric file BrushScriptX-Italic.afm to
              the groff font description file BSI.

              If you have a font family which provides regular upright
              (roman), bold, italic, and bold-italic styles, (where “italic”
              may be “oblique” or “slanted”), we recommend using R, B, I, and
              BI, respectively, as suffixes to the groff font family name to
              enable groff's font family and style selection features.  An
              example is groff's built-in support for Times: the font family
              name is abbreviated as T, and the groff font names are
              therefore TR, TB, TI, and TBI.  In our example, however, the
              BrushScriptX font is available in a single style only, italic.

           •  Install the groff font description file(s) in a devpdf
              subdirectory in the search path that groff uses for device and
              font file descriptions.  See the GROFF_FONT_PATH entry in
              section “Environment” of troff(1) for the current value of the
              font search path.  While groff doesn't directly use AFM files,
              it is a good idea to store them alongside its font description
              files.

           •  Register fonts in the devpdf/download file so they can be
              located for embedding in PDF files gropdf generates.  Only the
              first download file encountered in the font search path is
              read.  If in doubt, copy the default download file (see section
              “Files” below) to the first directory in the font search path
              and add your fonts there.  The PostScript font name used by
              gropdf is stored in the internalname field in the groff font
              description file.  (This name does not necessarily resemble the
              font's file name.)  If the font in our example had originated
              from a foundry named Z, we would add the following line to
              download.
                     Z→BrushScriptX-Italic→BrushScriptX-Italic.pfa
              A tab character, depicted as →, separates the fields.  The
              default foundry has no name: its field is empty and entries
              corresponding to it start with a tab character, as will the one
              in our example.

           •  Test the selection and embedding of the new font.
                     printf "\\f[BSI]Hello, world!\n" | groff -T pdf -P -e >hello.pdf
                     see hello.pdf

## [](#Exit_status)Exit status

           0      gropdf successfully produced a PDF document.

           1      gropdf experienced a critical error, or warnings were
                  emitted and the -W option was specified.

           2      gropdf could not interpret its command-line arguments.

## [](#Environment)Environment

           GROFF_FONT_PATH
                  A list of directories in which to seek the selected output
                  device's directory of device and font description files.
                  If, in the download file, the font file has been specified
                  with a full path, no directories are searched.  See
                  troff(1) and groff_font(5).

           GROPDF_NOSLIDE
                  If set and evaluates to a true value (to Perl), gropdf
                  ignores commands specific to presentation PDFs, producing a
                  normal PDF instead.

           GROPDF_OPTIONS
                  gropdf interprets the contents of this environment variable
                  as a space-separated list of command-line options.
                  Explicit command-line options override any settings from
                  this environment variable.

           SOURCE_DATE_EPOCH
                  A timestamp (expressed as seconds since the Unix epoch) to
                  use as the output creation timestamp in place of the
                  current time.  The time is converted to human-readable form
                  using Perl's gmtime() function and recorded in a PDF
                  comment.

           TZ     The time zone to use when converting the current time to
                  human-readable form; see tzset(3).  If SOURCE_DATE_EPOCH is
                  used, it is always converted to human-readable form using
                  UTC.

## [](#Files)Files

           /usr/local/share/groff/1.24.1/font/devpdf/DESC
                  describes the pdf output device.

           /usr/local/share/groff/1.24.1/font/devpdf/F
                  describes the font known as F on device pdf.

           /usr/local/share/groff/1.24.1/font/devpdf/U-F
                  describes the font from the URW foundry (versus the Adobe
                  default) known as F on device pdf.

           /usr/local/share/groff/1.24.1/font/devpdf/download
                  lists fonts available for embedding within the PDF document
                  (by analogy to the ps device's downloadable font support).

           /usr/local/share/groff/1.24.1/font/devpdf/Foundry
                  is a data file used by the groff build system to locate
                  PostScript Type 1 fonts.

           /usr/local/share/groff/1.24.1/font/devpdf/symbolsl.afm
                  provides metrics for the slanted symbol font known to groff
                  as SS.  These data facilitate use of the font with non-
                  groff software.

           /usr/local/share/groff/1.24.1/font/devpdf/symbolsl.pfb
                  supplies the slanted symbol font known to groff as SS.

           /usr/local/share/groff/1.24.1/font/devpdf/enc/text.enc
                  describes the encoding scheme used by most PostScript
                  Type 1 fonts; the encoding directive of font description
                  files for the pdf device refers to it.

           /usr/local/share/groff/1.24.1/font/devpdf/generate/symbolsl.sfd
                  is the source form of the symbolsl.pfb font, in spline font
                  database (SFD) format.

           /usr/local/share/groff/1.24.1/tmac/pdf.tmac
                  defines macros for use with the pdf output device.  It is
                  automatically loaded by troffrc when the pdf output device
                  is selected.

           /usr/local/share/groff/1.24.1/tmac/pdfpic.tmac
                  defines the PDFPIC macro for embedding images in a
                  document; see groff_tmac(5).  It is automatically loaded by
                  troffrc.

           /usr/local/share/doc/groff-1.24.1/examples/install-font.bash
                  This script, contributed by mom macro package author Peter
                  Schaffter and long available at his web site, assists with
                  making TrueType (.ttf), OpenType (.otf), and PostScript
                  Type 1 (.pfa, .pfb) fonts available to groff.

                  Change to its directory and run “bash install-font.bash -H”
                  for a man page-like description of its features and
                  operation.

## [](#Authors)Authors

           gropdf was written and is maintained by Deri James ⟨deri@
           chuzzlewit.myzen.co.uk⟩.

## [](#See_also)See also

           /usr/local/share/doc/groff-1.24.1/sboxes/msboxes.ms
           /usr/local/share/doc/groff-1.24.1/sboxes/msboxes.pdf
                  “Using PDF boxes with groff and the ms macros”, by Deri
                  James.

           present.tmac
                  is part of gpresent 
                  ⟨https://bob.diertens.org/corner/useful/gpresent/⟩, a
                  software package by Bob Diertens that works with groff to
                  produce presentations (“foils”, or “slide decks”).

           afmtodit(1), groff(1), troff(1), groff_font(5), groff_out(5)

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

    groff 1.24.1                    2026-03-14                      gropdf(1)

------------------------------------------------------------------------

Pages that refer to this page: [pdfman(1)](../man1/pdfman.1.html)

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
