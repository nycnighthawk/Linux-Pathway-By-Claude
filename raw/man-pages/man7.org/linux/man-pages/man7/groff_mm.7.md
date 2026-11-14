---
{"title": "groff_mm(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/groff_mm.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groff_mm(7) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Synopsis](#Synopsis) \| [Description](#Description) \| [Macros](#Macros) \| [Strings](#Strings) \| [Registers](#Registers) \| [Files](#Files) \| [Authors](#Authors) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    groff_mm(7)          Miscellaneous Information Manual         groff_mm(7)

## [](#Name)Name

           groff_mm - memorandum macros for GNU roff

## [](#Synopsis)Synopsis

           groff -mm [option ...] [file ...]

           groff -m mm [option ...] [file ...]

## [](#Description)Description

           The mm macro package distributed with the groff document
           formatting system is suitable for the composition of letters,
           memoranda, reports, and books.

           Call an mm macro at the beginning of a document to initialize the
           package.  A simple mm document might use only P for paragraphing.
           Set numbered and unnumbered section headings with H and HU,
           respectively.  Change the style of the typeface with B, I, and R;
           you can alternate styles within a word with BI, BR, IB, IR, RB,
           and RI.  Several nestable list types are available via AL, BL,
           BVL, DL, ML, RL, and VL; each of these begins a list, to which LI
           adds an item and LE ends the (nested) list.  LB begins a list with
           customizable layout parameters.  DS and DF start static and
           floating displays, respectively; DE terminates either.

           groff mm is intended to be compatible with the mm implementation
           found in the AT&T Documenter's Workbench 3.3 (“DWB”), with the
           following limitations and changes.

           •  Omitted features include the logo and company name strings, }Z
              and ]S, respectively; the encoded company site location
              addresses recognized as the third argument to the AU macro; the
              Pv (“private” heading) register; and the OK (other keywords)
              and PM (proprietary markings) macros.

           •  groff mm implements the CS (output cover page or “sheet”) macro
              only for memorandum type 4.

           •  The grap preprocessor is not explicitly supported; groff mm
              defines no G1 or G2 macros.

           •  Registers A, C, T, and U, set from the troff or nroff command
              lines with DWB, are not recognized.

           •  When setting the registers L or W from the command line, use an
              explicit scaling unit to avoid surprises.

           •  The Le register defaults to 1, consistently with Lf, Lt, and Lx
              in DWB; equations captioned with EC appear in tables of
              contents produced by TC.

           •  The Li register configures the text indentation of RL list
              items; DWB used a hard-coded value of 6 ens.

           •  groff mm uses the same adjustment and font style defaults in
              nroff and troff modes.

           •  Cut marks are not supported.

           DWB supported only seven heading levels.  As a compatible
           extension, groff mm supports fourteen, introducing new registers
           H8 through H14, and affecting the interpretation of the HF and HP
           strings.

           groff mm features a citation (or “bookmark”) system, permitting
           the document to make (customizable) internal references like “See
           chapter 5, page 128.”.  Forward references require two-pass
           formatting.  See the INITR macro description below and mmroff(1).

           Macro, register, and string descriptions in this page frequently
           mention each other; most references are to macros.  Where a
           register or string is referenced, its type is explicitly
           identified.  mm's macro names are usually in full capitals;
           registers and strings tend to have mixed-case names.

           Except where noted, mm assumes that horizontal measurements are
           reckoned in ens (scaling unit n) and vertical ones in vees
           (scaling unit v).  groff mm permits use of non-integral
           typographical points (scaling unit z).  Use explicit scaling units
           for clarity and predictable behavior.

       Document styles
           groff mm offers three frameworks for document organization.
           COVER/COVEND is a flexible means of preparing any document
           requiring a cover page.  LT/LO aids preparation of typical
           Anglophone correspondence (business letters, for example).  The MT
           memorandum type mechanism implements a group of formal styles
           historically used by AT&T Bell Laboratories.  Your document can
           select at most one of these approaches; when used, each disables
           the others.

       Localization
           groff mm is designed to be easily localized.  For languages other
           than English, strings that can appear in output are collected in
           the file /usr/local/share/groff/1.24.1/tmac/xx.tmac, where xx is
           an ISO 639 two-letter language identifier.  Localization packages
           should be loaded after mm; for example, you might format a Swedish
           mm document with the command “groff -mm -msv”.

           This package can also be localized by site or territory; for
           example, /usr/local/share/groff/1.24.1/tmac/mse.tmac illustrates
           how to adapt the output to a national standard using its ISO 3166
           territory code.  Such a package can define a string that causes a
           macro file /usr/local/share/groff/1.24.1/tmac/mm/territory_locale
           to be loaded at package initialization.  If this mechanism is not
           used, /usr/local/share/groff/1.24.1/tmac/mm/locale is loaded
           instead.  No diagnostic is produced if these files do not exist.

       Registers and strings
           Much mm behavior can be configured by registers and strings.  The
           nr request assigns a value to a register.

                  .nr ident [±]n [i]

           ident is the name of the register, and n is the value to be
           assigned.  Prefixing n with a plus or minus sign increments or
           decrements (respectively) its existing value.  If assignment of a
           (possibly) negative n is required, further prefix it with a zero
           or enclose it in parentheses.  If i is specified, the register's
           value automatically changes by i prior to interpolation if a plus
           or minus sign is included in the escape sequence as follows.

                  \n[±][ident]

           i can be negative; it combines algebraically with the sign in the
           interpolation escape sequence.  The brackets around ident are
           literal.

           Many of the registers mm provides are as Boolean-valued, meaning
           that they are considered “true” (on, enabled) when they have a
           positive value, and “false” (off, disabled) otherwise.

           Define strings with the ds request.

                  .ds ident contents

           contents consumes everything up to the end of the line, including
           trailing spaces.  It is a good practice to end contents with a
           comment escape sequence (\") so that extraneous spaces do not
           intrude during document maintenance.  To include leading spaces in
           contents, prefix it with a double quote.  Interpolate strings with
           the \* escape sequence.

                  \*[ident]

           Register and string name spaces are distinct, but strings and
           macros share a name space.  Defining a string with the same name
           as an mm macro is not supported and may cause incorrect rendering,
           the emission of diagnostic messages, and an error exit status from
           troff.

       Register format
           A register is interpolated using Arabic numerals if no other
           format has been assigned to it.  Assign a format to a register
           with the af request.

                  .af R c

           R is the name of the register, and c is the format.  If c is a
           sequence of Arabic numerals, their quantity defines a zero-padded
           minimum width for the interpolated register value.

                  Form   Sequence
                  1      0, 1, 2, 3, ..., 10, ...
                  001    000, 001, 002, 003, ..., 1000, ...
                  i      0, i, ii, iii, iv, ...
                  I      0, I, II, III, IV, ...
                  a      0, a, b, c, ..., z, aa, ab, ...
                  A      0, A, B, C, ..., Z, AA, AB, ...

       Fonts
           mm assumes that the font styles R (roman), I (italic), and
           B (bold) are mounted at font positions 1, 2, and 3, respectively.
           Use the fp request to mount substitute fonts at these positions as
           desired.  The default font family is “T” (Times).  To select a
           different one, invoke groff's fam request or use its -f command-
           line option.

## [](#Macros)Macros

           Double-quote macro arguments that contain space characters.  An
           explicitly empty argument may be specified with an empty pair of
           double quotes; for example, the following macro call has three
           arguments.

                  .XX "foo bar" "" baz

           Some macros are documented as causing a page break; this does not
           occur if such a macro is called when the drawing position is
           already at the top of a page (after a page heading, if any).

           Hook macros are undefined by default; mm calls them to enable
           customization of its behavior.  (DWB termed these “exits”.)

           Macro names longer than two characters are extensions; some
           shorter names were not part of DWB's published interface but are
           documented aspects of groff mm.

           1C [1] Format page text in one column (the default layout).  The
                  page is broken.  A 1 argument suppresses this break; its
                  use may cause body text and a pending footnote to
                  overprint.  See 2C, MC, and NCOL.

           2C     Begin two-column formatting.  This is a special case of MC.
                  See 1C and NCOL.

           AE     Abstract end; stop collecting abstract text.  See AS.

           AF [org-name]
                  Specify a memorandum's organizational affiliation.  At most
                  one can be declared; org-name is used by MT memoranda and
                  available to cover pages.  See COVER.

           AFX    Define this hook macro to assume responsibility for
                  formatting the affiliated firm name defined by AF in
                  memorandum types 0 and 4 and documents using the ms cover
                  page style.  If not defined (the default), internally
                  defined macros handle this task; see subsection “Internals”
                  and section “Files” below.  Applications include setting
                  the firm name in a different font family or at a larger
                  type size, drawing a rule across the page, and including a
                  logo image using groff's PDFPIC or PSPIC macros.  See MT,
                  COVER, and groff_tmac(5).

           AL [number-format [text-indent [1]]]
                  Begin an auto-incrementing numbered list, where item
                  numbers start at one and are followed by a dot.  number-
                  format assigns the register format (see above) mm uses for
                  the list item enumerators.  The default is 0.  A text-
                  indent argument overrides register Li.  A third argument
                  suppresses the vertical space that normally precedes each
                  list item; see register Lsp.  Vertical space in the amount
                  of Lsp precedes the list itself, but does not accumulate
                  with pre-item space when this list is nested in another.
                  AL calls LB; use LI to declare list items, and LE to end
                  the list.

           APP [sequence-number [title]]
                  Begin an appendix.  If sequence-number is omitted, it
                  increments (or is initialized to 1, if necessary).  The
                  register format used for sequence-number is “A”.  The page
                  is broken.  The register Aph determines whether an appendix
                  heading is then formatted.  This heading uses the string
                  App followed by sequence-number.  Appendices appear in any
                  table of contents (see TC).  The string Apptxt is set to
                  title if the latter is present, and made empty otherwise.

           APPSK sequence-number n [title]
                  As APP, but increment the page number by n.  Use this macro
                  to “skip pages” when diagrams or other materials not
                  formatted by troff are included in appendices.

           AS [placement [indentation]]
                  Abstract start; begin collecting abstract.  Input up to the
                  next AE call is included in the abstract.  placement
                  influences the location of the abstract on the cover page
                  of a memorandum (see MT).  COVER, by contrast, ignores
                  placement by default, but can be customized to interpret
                  it.

                  [1mplacement[24m   Effect
                  0           The abstract appears on page 1 and cover page
                              if the document is a “released paper”
                              memorandum (“.MT 4”); otherwise, it appears on
                              page 1 without a cover page.
                  1           The abstract appears only on the cover page
                              (“.MT 4” only).

                  An abstract does not appear at all in external letters
                  (“.MT 5”).  A placement of 2 was supported by DWB, but is
                  not by groff mm.

                  A second argument increases the indentation by indentation
                  and reduces the line length by twice this amount.  The
                  default is 0.

           AT title ...
                  Specify author's title(s).  If present, AT must appear just
                  after the corresponding author's AU.  Each title occupies
                  an output line beneath the author's name in the signature
                  block used by LT letters (see SG) and in MT memoranda.  The
                  ms cover page style also formats these data.

           AU [name [initials [loc [dept [ext [room [arg1 [arg2 [arg3]]]]]]]]]
                  Specify author.  AU terminates a document title started
                  with TL, and can be called without arguments for that
                  purpose.  Author information is used by cover pages, MT
                  memoranda, and SG.  Further arguments comprise initials,
                  location, department, telephone extension, room number or
                  name, and up to three additional items.  Repeat AU to
                  identify multiple authors.

                  Use WA/WE instead to identify the author for documents
                  employing LT.

           AV [name [1]]
                  Format approval lines for a handwritten signature and date.
                  Two horizontal rules are drawn, with the specified name and
                  the text of the string Letdate, respectively, beneath them.
                  Above these rules, mm formats the text in the string
                  Letapp; a second argument replaces this text with one vee
                  of vertical space.  See LT.

           AVL [name]
                  As AV, but omitting the approval notation (the Letapp
                  string), the date rule, and the label below the date rule
                  (the Letdate string).

           B [bold-text [previous-font-text]] ...
                  Join bold-text in boldface with previous-font-text in the
                  previous font, without space between the arguments.  If no
                  arguments, switch font to bold style.

           B1     Begin boxed static display.  The text is indented by 1n,
                  and the line length reduced by 2n.  See DS.  This is a
                  groff mm extension.

           B2     End boxed static display.  See B1.  This is a groff mm
                  extension.

           BE     End bottom block; see BS.

           BI [bold-text [italic-text]] ...
                  Join bold-text in boldface with italic-text in italics,
                  without space between the arguments.

           BL [text-indent [1]]
                  Begin bulleted list.  mm marks each item with the string
                  BU.  A text-indent argument overrides register Pi.  A
                  second argument suppresses the vertical space that normally
                  precedes each list item; see register Lsp.  Vertical space
                  in the amount of Lsp precedes the list itself, but does not
                  accumulate with pre-item space when this list is nested in
                  another.  BL calls LB; use LI to declare list items, and LE
                  to end the list.

           BR [bold-text [roman-text]] ...
                  Join bold-text in boldface with roman-text in roman style,
                  without space between the arguments.

           BS     Begin bottom block.  mm collects input into the bottom
                  block until the document calls BE, and outputs it between
                  the footnote area and footer of each page.

           BVL [text-indent [mark-indent [1]]]
                  Begin broken variable-item (or “tagged”) list.  Each item
                  should supply its own mark.  The line is always broken
                  after the mark; contrast VL.  A text-indent argument
                  overrides register Pi; mark-indent sets the distance from
                  the indentation of the current list to the mark.  A third
                  argument suppresses the vertical space that normally
                  precedes each list item; see register Lsp.  Vertical space
                  in the amount of Lsp precedes the list itself, but does not
                  accumulate with pre-item space when this list is nested in
                  another.  BVL calls LB; use LI to declare list items, and
                  LE to end the list.

           COVER [style]
                  Begin a cover page description.  COVER must appear before
                  the body text (or main matter) of a document.  The argument
                  style is used to construct the file name /usr/local/share/
                  groff/1.24.1/tmac/mm/style.cov and load it with the mso
                  request.  The default style is “ms”; the ms.cov file
                  prepares a cover page resembling that of the ms package.  A
                  .cov file must define a COVEND macro, which a document must
                  call at the end of the cover description.  Use cover
                  description macros in the following order; only TL and AU
                  are required.

                  .COVER
                  .AF
                  .TL
                  .AU
                  .AT
                  .\" Add additional AU and AT calls as needed.
                  .AS
                  .AE
                  .COVEND

           COVEND End the cover description.

           DE     End static or floating display begun with DS or DF.

           DF [format [fill [right-indentation]]]
                  Begin floating display.  A floating display is saved in a
                  queue and output in the order entered.  Arguments are
                  handled as in DS.  Floating displays cannot be nested.
                  Placement of floating displays is controlled by the
                  registers De and Df.

           DL [text-indent [1]]
                  Begin dashed list.  mm marks each item with the string EM.
                  A text-indent argument overrides register Pi.  A second
                  argument suppresses the vertical space that normally
                  precedes each list item; see register Lsp.  Vertical space
                  in the amount of Lsp precedes the list itself, but does not
                  accumulate with pre-item space when this list is nested in
                  another.  DL calls LB; use LI to declare list items, and LE
                  to end the list.

           DS [format [fill [right-indentation]]]
                  Begin static display.  mm collects input into a display
                  until the document calls DE.  The display is output on a
                  single page unless it is taller than the height of the
                  page.  DS can be nested (contrast with DF).

                  [1mformat[24m   Effect
                  none     Do not indent the display.
                  L        Do not indent the display.
                  I        Indent text by \n[Si].
                  C        Center each line.
                  CB       Center the whole display as a block.
                  R        Right-align each line.
                  RB       Right-align the whole display as a block.

                  The values “L”, “I”, “C”, and “CB” can also be specified as
                  “0”, “1”, “2”, and “3”, respectively, for compatibility
                  with DWB.

                  [1mfill[24m   Effect
                  none   Disable filling.
                  N      Disable filling.
                  F      Enable filling.

                  “N” and “F” can also be specified as “0” and “1”,
                  respectively, for compatibility with DWB.

                  A third argument reduces the line length by right-
                  indentation.

                  mm normally places vertical space before and after the
                  display.  Set register Ds to “0” to suppress it.

           EC [title [override [flag [ref-name]]]]
                  Caption an equation.  A caption comprises the string Capec
                  followed by an automatically incrementing counter stored in
                  the register Ec, punctuation configured by the register Of,
                  then title (if any).  Use the af request to configure Ec's
                  number format.  override and flag alter the equation number
                  as follows.  Omitting flag and specifying 0 in its place
                  are equivalent.

                  [1mflag[24m   Effect
                  0      Prefix number with override.
                  1      Suffix number with override.
                  2      Replace number with override.

                  mm centers equation captions irrespective of the alignment
                  of any enclosing display.

                  Specifying ref-name stores the equation number as if by
                  “.SETR ref-name \n[Ec]”.  Recognition of this argument is a
                  groff mm extension.

                  The package lists captioned equations in a table of
                  contents (see TC) if the Boolean register Le is true.  The
                  string Le captions this list.

           EF ["'left'center'right'"]
                  Define the even-page footer, which is formatted just above
                  the normal page footer on even-numbered pages.  See PF.  EF
                  defines the string EOPef.

           EH ["'left'center'right'"]
                  Define the even-page header, which is formatted just below
                  the normal page header on even-numbered pages.  See PH.  EH
                  defines the string TPeh.

           EN     End mathematical expression input preprocessed by eqn(1);
                  see EQ.

           EOP    groff mm calls this hook macro in lieu of normal page
                  footer layout.  The package uses a separate environment to
                  format headers and footers.  See TP.

                  Strings available to EOP
                  ─────────────────────────
                  EOPf     argument to PF
                  EOPef    argument to EF
                  EOPof    argument to OF

           EPIC [-L] width height [name]
                  Draw a box with the given width and height.  The text name
                  (or default text) is formatted inside the box; no attempt
                  is made to size the box to fit the text.  An application of
                  this macro is to indicate the placement of an image to be
                  determined later, or externally composited in
                  postprocessing.  -L as the first argument left-aligns the
                  box; the default is to center it.  See PIC.

           EQ [label]
                  Start mathematical expression input preprocessed by eqn(1).
                  EQ and EN macro calls bracket an equation region.  Such
                  regions must be contained in displays (DS/DE), except when
                  the region is used only to configure eqn and not to produce
                  output.  If present, label appears aligned to the right and
                  centered vertically within the display; see register Eq.
                  If multiple eqn regions occur within a display, only the
                  last label (if any) is used.

           EX [title [override [flag [ref-name]]]]
                  Caption an exhibit.  Arguments are handled analogously to
                  EC.  The register Ex is the exhibit counter.  The string
                  Capex precedes the exhibit number and any title.  mm
                  centers exhibit captions irrespective of the alignment of
                  any enclosing display.

                  The package lists captioned exhibits in a table of contents
                  (see TC) if the Boolean register Lx is true.  The string Lx
                  captions this list.

           FC [closing-text]
                  Output the string Letfc, or the specified closing-text, as
                  the formal closing of a letter or memorandum.  See LT and
                  MT.

           FD [arg [1]]
                  Configure display of footnotes.  The first argument encodes
                  enablement of automatic hyphenation, adjustment to both
                  margins, indentation of footnote text, and left- vs. right-
                  alignment of the footnote label within the space allocated
                  for it.

                  [1marg[24m   Hyphenate?   Adjust?   Indent?   Label alignment
                  0     no           yes       yes       left
                  1     yes          yes       yes       left
                  2     no           no        yes       left
                  3     yes          no        yes       left
                  4     no           yes       no        left
                  5     yes          yes       no        left
                  6     no           no        no        left
                  7     yes          no        no        left
                  8     no           yes       yes       right
                  9     yes          yes       yes       right
                  10    no           no        yes       right
                  11    yes          no        yes       right

                  An arg greater than 11 is treated as 0.  mm's default is 0.

                  A second argument resets footnote numbering when a first-
                  level heading is encountered.  See FS.

           FE     End footnote; see FS.

           FG [title [override [flag [ref-name]]]]
                  Caption a figure.  Arguments are handled analogously to EC.
                  The register Fg is the figure counter.  The string Capfg
                  precedes the figure number and any title.  mm centers
                  figure captions irrespective of the alignment of any
                  enclosing display.

                  The package lists captioned figures in a table of contents
                  (see TC) if the Boolean register Lf is true.  The string Lf
                  captions this list.

           FS [mark]
                  Start footnote.  mm collects input into a footnote until
                  the document calls FE, outputting it when the vertical
                  drawing position nears the page bottom.  By default, mm
                  automatically numbers footnotes starting at 1; the number
                  is available in register Ftnum and, with a trailing period,
                  in string F.  If desired, interpolate this string in the
                  body text to format the footnote mark.  mm interpolates
                  string F prior to the footnote text.  Footnotes are
                  vertically separated by the product of registers Fs and
                  Lsp.  In groff mm, footnotes may be used in displays.

                  A mark argument, which need not be numeric, replaces the
                  default footnote mark, leaving the string F unchanged.  In
                  that event, you must explicitly write any footnote mark to
                  appear in the footnote itself.

           GETHN ref-name [string]
                  Interpolate ref-name's heading mark, or, if string is
                  specified, store it there.  In neither case does GETHN
                  suffix the interpolation with space.  See INITR.

           GETPN ref-name [string]
                  Interpolate ref-name's page number, or, if string is
                  specified, store it there.  In neither case does GETPN
                  suffix the interpolation with space.  See INITR.

           GETR ref-name
                  Retrieve location data for reference ref-name, call GETHN
                  and GETPN to populate strings Qrfh and Qrfn, respectively,
                  and interpolate string Qrf as an internal reference to it.
                  See INITR.

           GETST ref-name [string]
                  Interpolate ref-name's auxiliary reference datum, or, if
                  string is specified, store it there.  In neither case does
                  GETST suffix the interpolation with space.  See INITR.

           H level [title [suffix]]
                  Set a numbered section heading at level.  mm calls LC to
                  clear any lists, then produces numbered heading marks of
                  the form a.b.c..., with up to fourteen levels of nesting.
                  Each level's number increments automatically with each H
                  call and is reset to zero when a more significant level is
                  specified.  “1” is the most significant or coarsest
                  division of the document.  Text after an H call is
                  formatted as a paragraph; calling P is unnecessary.

                  The optional title must be double-quoted if it contains
                  spaces.  mm appends suffix to title in the body of the
                  document, but omits it from any table of contents (see TC).
                  This facility can be used to annotate the heading title
                  with a footnote.  suffix should not interpolate the F
                  string; specify a footnote mark explicitly.  See FS.

                  Heading behavior is configurable.  Several registers set
                  thresholds, where heading levels at or below a threshold
                  value are handled in one way, and those above it another.
                  For example, mm populates a table of contents (see TC) with
                  the title of a heading if its level is within the Cl
                  register threshold.

                  Heading layout.  Register Ej sets a threshold for page
                  breaking (ejection) prior to a heading.  If not preceded by
                  a page break, a heading level within the threshold in
                  register Hps is preceded by the amount of vertical space in
                  register Hps1, and by the amount in Hps2 otherwise.  The Hb
                  register sets a threshold at which a break occurs after the
                  heading, and register Hs sets a threshold within which
                  vertical space follows it.  If the heading level is above
                  both of these, and the paragraph is not numbered, mm
                  produces a run-in heading; paragraph text follows on the
                  same output line.  Otherwise, register Hi configures the
                  indentation of text after headings.  Threshold register Hc
                  permits centering; mm centers a heading with a level within
                  both of the Hb and Hc thresholds.

                  Heading typeface and size.  The HF string configures the
                  fonts used for heading marks and titles at each level.  The
                  string HP likewise assigns a type size to each heading
                  level.  The hook macros HX and/or HZ can control the
                  vertical spacing used by headings.

                  Heading number format.  Registers named H1 through H14
                  store counters for each heading level.  Their values are
                  printed using Arabic numerals by default; see HM.  The
                  heading levels are catenated with dots for formatting; to
                  typeset only the deepest, set the Ht register.  Heading
                  numbers are not suffixed with a trailing dot except when
                  only the first level is output; to omit a dot in this case
                  as well, clear the H1dot register.

                  Customizing heading behavior.  H calls HX, HY, and HZ hook
                  macros to further customize headings.  These can change the
                  heading's mark (the numbered portion before any heading
                  title), its vertical spacing, and its vertical space
                  requirements (for instance, to require a minimum quantity
                  of subsequent output lines on the page, breaking the page
                  otherwise).  Define hook macros in expectation of the
                  following parameters.  The argument declared-level is the
                  level argument to H, or 0 for unnumbered headings (see HU).
                  actual-level is the same as declared-level for numbered
                  headings, and the value of register Hu for unnumbered
                  headings.  title-suffix is the catenation of the
                  corresponding arguments to H or HU.

                  HX declared-level actual-level title-suffix
                         mm calls HX before setting the heading.  Your
                         definition may alter }0, }2, and ;3.

                         }0 (string)
                                contains the heading mark plus two spaces if
                                declared-level is non-zero, and otherwise is
                                empty.

                         ;0 (register)
                                encodes a position for the text after the
                                heading.  0 means that the heading is to be
                                run in, 1 means that a break is to occur
                                before the text, and 2 means that vertical
                                space is to separate heading and text.

                         }2 (string)
                                is the suffix that separates a run-in heading
                                from the text.  It contains two spaces if
                                register ;0 is 0, and otherwise is empty.

                         ;3 (register)
                                contains the vertical space required for the
                                heading to be typeset.  If that amount is not
                                available, the page is broken prior to the
                                heading.  The default is 2v.

                  HY declared-level actual-level title-suffix
                         mm calls HY after determining the heading typeface
                         and size.  It could be used to change indentation.

                  HZ declared-level actual-level title-suffix
                         mm calls HZ after formatting the heading, just
                         before H or HU returns.  It could be used to change
                         the page header to include a section heading.

           HC [hyphenation-character]
                  Set hyphenation character, selecting the default, “\%”, if
                  called without argument.

           HM [arg1 [arg2 [... [arg14]]]]
                  Set the heading mark style.  Each argument assigns the
                  specified register format (see above) to the corresponding
                  heading level.  The default is 1 for all levels.  An
                  explicitly empty argument also indicates the default.

           HU title [suffix]
                  Set an unnumbered section heading with title and, as a
                  groff mm extension, an optional suffix.  The heading is
                  treated as a numbered heading of the level stored in
                  register Hu, but no heading mark is output; see H.

           I [italic-text [previous-font-text]] ...
                  Join italic-text in italics with previous-font-text in the
                  previous font, without space between the arguments.  If no
                  arguments, switch font to italic style.

           IA [recipient-name [title]]
                  Specify the inside address in a letter.  The arguments give
                  each recipient a name and title.  mm collects input into
                  the inside address until the document calls IE, then
                  outputs it.  You can specify multiple recipients with empty
                  IA/IE pairs; mm uses only the last address.  See LT.

           IB [italic-text [bold-text]] ...
                  Join italic-text in italics with bold-text in boldface,
                  without space between the arguments.

           IE     End the inside address begun with IA.

           IND argument ...
                  If the Boolean register Ref is true, write an index entry
                  as a specially prepared roff comment to the standard error
                  stream, with each argument separated from its predecessor
                  by a tab character.  The entry's location information is
                  arranged as configured by the most recent INITI call.

           INDP   Output the index set up by INITI and populated by IND
                  calls.  By default, INDP calls SK and writes a centered
                  caption interpolating the string Index.  It then disables
                  filling and calls 2C; afterward, it restores filling and
                  calls 1C.

                  Define macros to customize this behavior.  INDP calls TXIND
                  before the caption, TYIND instead of writing the caption,
                  and TZIND after formatting the index.

           INITI location-type file-name [macro]
                  Initialize groff mm's indexing system.  Argument location-
                  type selects how the location of each index entry is
                  reported.  file-name populates an internal string used
                  later by INDP.

                  [1mlocation-type[24m   Entry format
                  N               page number
                  H               heading mark
                  B               page number, tab character, heading mark

                  If macro is specified, groff mm calls it for each index
                  entry with the arguments given to IND.

           INITR file-name-prefix
                  Initialize the internal reference macros.  Internal
                  references are written to the standard error stream, which
                  should be redirected into a file named file-name-
                  prefix.qrf.  mmroff(1) handles this and the two formatting
                  passes it requires.  The first pass identifies internal
                  references; the second includes them.  See SETR, GETHN,
                  GETPN, and GETST.

           IR [italic-text [roman-text]] ...
                  Join italic-text in italics with roman-text in roman style,
                  without space between the arguments.

           LB text-indent mark-indent pad type [mark-or-format [pre-item-
           space [pre-list-space]]]
                  Begin list.  The macros AL, BL, BVL, DL, ML, RL, and VL
                  call LB in various ways; they are simpler to use and may be
                  preferred if they suit the desired purpose.

                  mm tracks the nesting level of lists; the outermost is 0.
                  It indents each list item (text formatted after an LI call)
                  by text-indent.  The mark is left-aligned at mark-indent,
                  and padded on the left with pad ens of space.  type
                  determines the mark's format.

                  [1mtype[24m   Output for a mark “x”
                  0      x
                  1      x.
                  2      x)
                  3      (x)
                  4      [x]
                  5      <x>
                  6      {x}

                  If type is 0, mark-or-format specifies each item's mark
                  (which can be overridden by an argument to LI).  If mark-
                  or-format is empty (or the dummy character “\&”) mm sets
                  items at mark-indent with a hanging indent at text-indent.

                  If type is greater than zero, mm supplies an automatically
                  incrementing numeric mark, and interprets mark-or-format as
                  a register format.

                  A type of -1 causes groff mm to break the line after the
                  mark even if it fits within text-indent; this is a groff mm
                  extension.

                  The last two arguments manage vertical space.  Unless a
                  list's nesting level is greater than the value of register
                  Ls, its items are preceded by pre-item-space multiplied by
                  the register Lsp; the default is 1.  LB precedes the list
                  by pre-list-space multiplied by the register Lsp; the
                  default is 0.

           LC [list-level]
                  Clear list state.  Active lists are terminated as if with
                  LE, either all (the default) or only those from the current
                  level down to list-level if specified.

           LE [1] End list.  The current list is terminated.  An argument
                  of 1 causes vertical space in the amount of register Lsp to
                  follow the list.

           LI [mark [pad-prefix]]
                  Begin a list item.  mm collects input into a list item
                  until the document terminates the current list or calls LI
                  again.  By default, the item's text is preceded by any mark
                  configured by the current list.  If mark is the only
                  argument, it replaces the mark configured in the
                  corresponding LB call.  If the width of the mark plus any
                  pad specified in the LB call exceeds the text indentation,
                  groff mm warns and uses one en of padding between the mark
                  and the text.  The presence of a second argument prefixes
                  mark to the LB-configured mark and, as a groff mm
                  extension, conditionally puts an unbreakable space between
                  the prefix and mark per the argument's Boolean value.

           LO option [value]
                  Specify letter options; see LT.  By default, mm recognizes
                  the following option values.  See IA regarding the inside
                  address and string DT regarding the date.

                  [1moption[24m   Meaning and Effect
                  AT       Attention; put contents of string LetAT and value
                           left-aligned after the inside address.
                  CN       Confidential; put value, or contents of string
                           LetCN, left-aligned after the date.
                  RN       Reference; put contents of string LetRN and value
                           after the confidential notation (if any) and the
                           date, aligned with the latter.
                  SA       Salutation; put value, or contents of string
                           LetSA, left-aligned after the inside address and
                           the confidential notation (if any).
                  SJ       Subject; put contents of string LetSJ and value
                           left-aligned after the inside address and the
                           attention and salutation notations (if any).  In
                           letter type “SP”, LetSJ is ignored and value is
                           set in full capitals.

           LT [style]
                  Format a letter in the designated style, defaulting to BL
                  (see below).  A letter begins with the writer's address
                  (WA/WE), followed by the date (ND), the inside address
                  (IA/IE), the body of the letter (P and other general-
                  purpose mm macros), the formal closing (FC), the signature
                  (SG), and notations (NS/NE).  Any of these except the body
                  text may be omitted.  Letter options specified with LO add
                  further annotations, which are extensible; see subsection
                  “Internals” below.

                  [1mstyle[24m   Description
                  BL      Blocked: the writer's address, date, formal
                          closing, and signature are indented to the center
                          of the line.  Everything else is left-aligned.
                  SB      Semi-blocked: as BL, but the first line of each
                          paragraph is indented by \n[Pi] ens.
                  FB      Fully blocked: everything is left-aligned.
                  SP      Simplified: as FB, but a formal closing is omitted,
                          and the signature is set in full capitals.

           MC column-width [gutter-width]
                  Begin multi-column layout.  groff mm creates as many
                  columns of column-width as the line length will permit.
                  gutter-width is the interior spacing between columns.  It
                  defaults to column-width/15.  NCOL moves to the next
                  column, and 1C returns to single-column layout.  MC is a
                  groff mm extension, generalizing 2C.  See MULB for an
                  alternative.

           ML mark [text-indent [1]]
                  Start a marked list; the mark argument precedes each item.
                  text-indent overrides the default indentation of the list
                  items, which is the width of mark plus one en.  A third
                  argument suppresses the vertical space that normally
                  precedes each list item; see register Lsp.  Vertical space
                  in the amount of Lsp precedes the list itself, but does not
                  accumulate with pre-item space when this list is nested in
                  another.  ML calls LB; use LI to declare list items, and LE
                  to end the list.

           MT [type [addressee]]
                  Select memorandum type.  These correspond to formats used
                  by AT&T Bell Laboratories, where the mm package was
                  initially developed, affecting the document layout.  Some
                  of these included a cover page with a caption categorizing
                  the document.  groff mm uses type to construct the file
                  name /usr/local/share/groff/1.24.1/tmac/mm/type.MT and load
                  it with the mso request.  Memorandum types 0 to 5 are
                  supported; any other value of type is mapped to type 6.
                  Omitting type implies 1.  addressee sets a string analogous
                  to one used by AT&T cover page macros not implemented in
                  groff mm.

                  [1mtype[24m     Description
                  0        normal memorandum; no caption
                  1        captioned “TECHNICAL MEMORANDUM”
                  2        captioned “INTERNAL MEMORANDUM”
                  3        captioned “ADMINISTRATIVE MEMORANDUM”
                  4        released paper
                  5        external letter
                  string   captioned string

                  See COVER for a more flexible cover page mechanism.

           MOVE y-pos [x-pos [line-length]]
                  Move to a position, setting page offset to x-pos.  If line-
                  length is not given, the difference between current and new
                  page offset is used.  Use PGFORM without arguments to
                  return to normal.

           MULB cw1 sp1 [cw2 sp2] ... cwn
                  Begin alternative multi-column mode.  All column widths cwi
                  must be specified, as must the amount of space spi between
                  each column pair.  MULB uses a diversion and operates in a
                  separate environment.

           MULE   End alternative multi-column mode and emit the columns.

           MULN   Start next column in alternative column mode.

           NCOL   Start next column (only when using 2C or MC).  Contrast
                  with MULN.

           ND [arg]
                  Set the document's date.  mm does not interpret arg; it can
                  be a revision identifier (or empty).  mm calls ND itself
                  when initializing.

           NE     End notation begun with NS; filling is enabled.

           nP [type]
                  As P, but set a paragraph number in the form x.yy, where x
                  is the number of the second heading level, and yy
                  increments with each nP call; its value is not reset when
                  the second-level heading number changes.  mm uses a
                  register format of “00” for yy.

           NS [code [1]]
                  Declare notations, typically for letters or memoranda, of
                  the type specified by code.  The text corresponding to code
                  is output, and filling is disabled until the document calls
                  NE.  Typically, a list of names or attachments lies within
                  NS/NE.  If code is absent or does not match one of the
                  values listed under the Letns string description below,
                  each line of notations is formatted as “Copy (line) to”.
                  If a second argument, conventionally 1, is given, code
                  becomes the entire notation and NE is not necessary.  In
                  groff mm, you can set up further notations to be recognized
                  by NS; see the strings Letns and Letnsdef below.

           OF ["'left'center'right'"]
                  Define the odd-page footer, which is formatted just above
                  the normal page footer on odd-numbered pages.  See PF.  OF
                  defines the string EOPof.

           OH ["'left'center'right'"]
                  Define the odd-page header, which is formatted just below
                  the normal page header on odd-numbered pages.  See PH.  OH
                  defines the string TPoh.

           OP     Ensure that subsequent text is formatted at the top of an
                  odd-numbered page; no page break is performed if the
                  drawing position is already there.

           P [type]
                  Begin new paragraph.  If type is missing or 0, P sets the
                  paragraph fully left-aligned.  A type of 1 indents the
                  first line by \[Pi] ens.  Set the register Pt to select a
                  default paragraph indentation style.  The register Ps
                  determines the amount of vertical space between paragraphs.

                  To set a paragraph with a hanging indent, use VL with the
                  desired indentation as the argument, LI (with no argument),
                  and LE.

           PE     End picture input preprocessed by pic(1); see PS.

           PF ["'left'center'right'"]
                  Define the page footer.  The footer is formatted at the
                  bottom of each page; the argument is otherwise as described
                  in PH.  PF defines the string EOPf.  See EF, OF, and EOP.

           PGFORM [line-length [page-length [page-offset [1]]]]
                  Set line length, page length, and/or page offset.  This
                  macro can be used for letterheads and similar.  It is
                  normally the first macro call in a file, though it is not
                  necessary.  PGFORM can be used without arguments to reset
                  everything after a MOVE call.  A line break is done unless
                  the fourth argument is given.  This can be used to avoid
                  the page number on the first page while setting new width
                  and length.  (It seems as if this macro sometimes doesn't
                  work too well.  Use the command-line arguments to change
                  line length, page length, and page offset instead.)

           PGNH   Suppress header on the next page.  To suppress a header on
                  the first page, call this macro prior to formatting any
                  text in the document.  Also see register N.

           PH ["'left'center'right'"]
                  Define the page header, formatted at the top of each page,
                  as the argument, where left, center, and right are aligned
                  to the respective locations on the line.  A “%” character
                  in arg is replaced by the page number.  If the argument is
                  absent, no page header is set.  The default page header is
                         "''- % -''"
                  which centers the page number between hyphens and formats
                  nothing at the upper left and right.  Header macros call PX
                  (if defined) after formatting the header.  PH defines the
                  string TPh.  See EH, OH, and TP.

           PIC [-B] [-C|-I n|-L|-R] file [width [height]]
                  Include PostScript document file.  The optional -B argument
                  draws a box around the picture.  The optional -L, -C, -R,
                  and -I n arguments align the picture or indent it by n.  By
                  default, the picture is left-aligned.  Optional width and
                  height arguments resize the picture.  Use of this macro
                  requires two-pass processing; see INITR and mmroff(1).

           PS     Start picture input preprocessed by pic(1).

           PY     As PE, but with “flyback”, returning the drawing position
                  to where it was prior to the picture.  This is a groff mm
                  extension.

           R [roman-text [previous-font-text]] ...
                  Join roman-text in roman style with previous-font-text in
                  the previous font, without space between the arguments.  If
                  no arguments, switch font to roman style.

           RB [roman-text [bold-text]] ...
                  Join roman-text in roman style with bold-text in boldface,
                  without space between the arguments.

           RD [prompt [div [str]]]
                  Write prompt (if specified, a tab and colon “:” to the
                  standard error stream and read response from standard input
                  stream, optionally into a diversion div and/or string str.
                  Interpolate the saved text by calling its name like a
                  macro.  If string is present, the input is also stored in a
                  string of that name.

           RF     End a bibliographic reference citiation started with RS.
                  See RP.

           RI [roman-text [italic-text]] ...
                  Join roman-text in roman style with italic-text in italics,
                  without space between the arguments.

           RL [text-indent [1]]
                  Begin an auto-incrementing numbered list, where item
                  numbers start at one and set between square brackets.  A
                  text-indent argument overrides register Li.  A second
                  argument suppresses the vertical space that normally
                  precedes each list item; see register Lsp.  Vertical space
                  in the amount of Lsp precedes the list itself, but does not
                  accumulate with pre-item space when this list is nested in
                  another.  RL calls LB; use LI to declare list items, and LE
                  to end the list.  “RL” is a mnemonic for “reference list”,
                  but this macro has no relationship with mm's bibliographic
                  reference list facilities.

           RP [suppress-counter-reset [page-ejection-policy]]
                  Format a reference list, listing items accumulated within
                  RS/RF pairs.  The reference counter is reset unless the
                  first argument is 1.  Normally, page breaks occur before
                  and after the references are output; the register Rpej
                  configures this behavior, and a second argument overrides
                  its value.  TC calls RP automatically if references have
                  accumulated.

                  groff mm calls LB to format the reference list; the Rpfmt
                  string configures the list's appearance.  Setting register
                  Ls to 0 suppresses spacing after the list.  The string Rp
                  contains the reference list caption.

           RPX    This hook macro assumes responsibility for formatting the
                  heading of the reference page that RP produces.  If not
                  defined (the default), mm sets the reference list caption
                  in the string Rp after two vees of space, centered in
                  italics, followed by another vee of space.

           RS [reference-string]
                  Begin citation of an automatically numbered bibliographic
                  reference entry.  mm collects input into a reference entry
                  until the document calls RF.  A subsequent RP call emits
                  the accumulated entries.  References are numbered starting
                  at 1; the register :R stores the most recently assigned
                  number.  Interpolate the string Rf where the reference mark
                  should be, then place the entry between RS and RF calls on
                  text lines after the reference mark.  The Rfstyle register
                  determines whether the mark is bracketed, superscripted, or
                  both.  If reference-string is specified, mm also stores the
                  reference mark in a string of that name.

           S [type-size [vertical-spacing]]
                  Set type size and vertical spacing.  Each argument is a
                  groff measurement, using an appropriate scaling unit and an
                  optional + or - prefix to increment or decrement the
                  current value.  An argument of P restores the previous
                  value, C retains the current value, and D requests the
                  default.  mm treats an empty or omitted argument as P.

           SA [mode]
                  Set or restore the default enablement of adjustment.
                  Specify 0 or 1 as mode to set a document's default
                  explicitly; groff mm assumes 1.  Invoke the na request as
                  desired to temporarily suspend adjustment.  H and HU, and
                  SA when called without a mode argument, restore the default
                  adjustment.

           SETR ref-name [string]
                  Create reference ref-name, storing its heading and page
                  numbers.  If string is present, groff mm saves it as an
                  auxiliary datum for retrieval by GETST.  See INITR.

           SG [arg [1]]
                  Output author signature block(s) in LT letters and MT
                  memoranda.  The format of a signature block depends on the
                  letter or memorandum type.  See subsection “Internals”
                  below.

                  LT letters emit a signature for one author at most (see
                  WA).  The author's title, if any, is set on the next line,
                  indented to align with the name, except in letter type
                  “SP”, where it is set in full capitals (like the name)
                  after a comma and space.

                  Memorandum type 4 uses no signature block.  In other
                  memoranda, each of an author's titles is set on a
                  subsequent line, indented to align with the name.  They
                  furthermore encode a secretarial annotation including the
                  location, department, and initials specified in each
                  author's AU call, followed by any arg, writing it at the
                  left margin preceding the last author's name, or preceding
                  the first if a second SG argument is present.

           SK [n] Skip n pages.  If n is 0 or omitted, mm breaks the page if
                  necessary.  Otherwise, mm prints n pages, blank except for
                  any headers and footers.

           SM text [post]
           SM pre text post
                  Format text at a smaller type size, joined with any
                  specified pre and post at normal size, without space
                  between the arguments.

           SP [distance]
                  Space downward by distance.  Multiple SP calls in sequence
                  produce only the largest of the specified distances.  SP
                  accepts boundary-relative motions specified with a prefixed
                  | operator, but not negative ones.

                  SP has no effect when the drawing position is at the top of
                  the page.  Put the dummy character escape sequence \&
                  (followed by \c if desired to prevent a break) on a text
                  line prior to an SP call to overcome this restriction.

           TAB    Reset tab stops to every 5 ens.  The ta request customizes
                  them.

           TB [title [override [flag [ref-name]]]]
                  Caption a table.  Arguments are handled analogously to EC.
                  The register Tb is the table counter.  The string Captb
                  precedes the table number and any title.  mm centers table
                  captions irrespective of the alignment of any enclosing
                  display.

                  The package lists captioned tables in a table of contents
                  (see TC) if the Boolean register Lt is true.  The string Lt
                  captions this list.

           TC [slevel [spacing [tlevel [tab [h1 [h2 [h3 [h4 [h5]]]]]]]]]
                  Output table of contents.  This macro is normally the last
                  called in the document.  It flushes any pending displays
                  and, if any references are pending (see RS), calls RP.  It
                  then begins a new page with the contents caption, stored in
                  the string Captc, centered at the top.  The entries follow
                  after three vees of space.  Each entry is a saved section
                  (number and) heading title (see the Cl register), along
                  with its associated page number.  By default, mm indents an
                  entry by an amount corresponding to its heading level and
                  the maximum heading length encountered at that heading
                  level; if defined, the string Ci overrides these
                  indentations.  Entries at heading levels up to and
                  including slevel are preceded by spacing vees of space.
                  Entries at heading levels up to and including tlevel are
                  followed by a leader and a right-aligned page number.  If
                  the Boolean-valued tab argument is true, the leader is
                  replaced with horizontal motion in the same amount.  For
                  entries above heading level tlevel, the page number follows
                  the heading text after a word space.  Each argument h1...h5
                  appears in order on its own line, centered, above the
                  contents caption.  Page numbering restarts at 1, in
                  register format “i”.  If the Oc register is true, numbering
                  of these pages is suppressed.

                  If the document calls TC with at most four arguments, mm
                  calls the hook macro TX prior to formatting the contents
                  caption, and TY (if defined) instead of formatting the
                  contents caption.

                  mm then presents lists of figures, tables, equations, and
                  exhibits, in that order.  A list appears only if at least
                  one such captioned item is present, and if its
                  corresponding register (Le, Lf, Lt, or Lx) is set.  TXxx
                  and TYxx macros, where xx is “FG”, “TB”, “EC”, or “EX”, and
                  strings Capfg, Captb, Capec, and Capex analogously
                  configure the output of each captioned list.

           TE     End tbl(1) table.  See TS.

           TH     Mark the end of a TS/TE table heading.  When a table spans
                  multiple pages, the heading repeats at the top of each
                  page.  groff mm does not implement the N argument supported
                  by DWB.

           TL [charging-case-number [filing-case-number]]
                  Begin document title.  mm collects input into the title
                  until a subsequent AU call and formats it as directed by
                  the MT memorandum type or cover page macros.  mm saves
                  charging-case-number and filing-case-number for use in all
                  memorandum types except 4.

           TM number ...
                  Declare technical memorandum number(s) used with MT
                  memoranda.

           TP     mm calls this hook macro in lieu of normal page header
                  layout.  The package uses a separate environment to format
                  headers and footers.  See EOP.

                  Strings available to TP
                  ────────────────────────
                  TPh     argument to PH
                  TPeh    argument to EH
                  TPoh    argument to OH

           TS [H] Start tbl(1) table.  Argument “H” tells mm that the table's
                  heading should repeat after page breaks.  See TE, TH, and
                  tbl(1).

           VERBON [format [type-size [font]]]
                  Begin display of verbatim content.  format controls several
                  parameters.  Add up the values of desired features; the
                  default is 0.  Further arguments configure the type-size in
                  typographical points (on typesetting devices), and the face
                  (font).  On typesetting devices, the default face is CR
                  (Courier roman), a monospaced font: all glyphs are equally
                  wide.

                  Value   Effect
                  1       Disable the formatter's escape character (\).
                  2       Vertically space before the display.
                  4       Vertically space after the display.
                  8       Number output lines; call formatter's nm request
                          with arguments in string Verbnm.
                  16      Indent by the amount stored in register Verbin.

           VERBOFF
                  End verbatim display.

           VL [text-indent [mark-indent [1]]]
                  Begin variable-item (or “tagged”) list.  Each item should
                  supply its own mark, or tag.  A text-indent argument
                  overrides register Pi; mark-indent sets the distance from
                  the indentation of the current list to the mark.  A third
                  argument suppresses the vertical space that normally
                  precedes each list item; see register Lsp.  Vertical space
                  in the amount of Lsp precedes the list itself, but does not
                  accumulate with pre-item space when this list is nested in
                  another.  RL calls LB; use LI to declare list items, and LE
                  to end the list.

           VM [-T] [top [bottom]]
                  Configure vertical margins.

                  Without a -T argument, increment the top and bottom margins
                  by top and bottom, respectively.  If absent, set the
                  corresponding margin to zero.

                  With the -T argument, set the top and bottom margins to top
                  and bottom, respectively.  If absent, set the respective
                  margin to the default (top: 7v, bottom: 6v).

                  We recommend defining the hook macros TP and/or EOP if
                  using -T and setting top and/or bottom margin to values
                  less than the default.  groff mm exposes this undocumented
                  DWB macro to enable greater user control of page layout.

           WA [writer's-name [title]]
                  Specify the writer(s) of an LT letter.  mm collects input
                  into the writer's address until the document calls WE, then
                  outputs it.  You can specify multiple writers with empty
                  WA/WE pairs; only the last address is used.  The arguments
                  give each writer a name and title.

           WC [format ...]
                  Control width of footnotes and displays.

                  [1mformat[24m   Effect
                  N        equivalent to “-WF -FF -WD” (default)
                  WF       set footnotes at full line length, even in two-
                           column mode
                  -WF      set footnotes using column line length
                  FF       apply width of first footnote to encountered to
                           subsequent ones
                  -FF      footnote width determined by WF and -WF
                  WD       set displays at full line length, even in two-
                           column mode
                  -WD      set displays using column line length

           WE     End the writer's address begun with WA.

## [](#Strings)Strings

           Many mm strings interpolate predefined, localizable text.  We
           present their contents in quotation marks.

           Abstract
                  “ABSTRACT”

           App    “APPENDIX”

           Apptxt stores the title argument to the most recent APP call.

           Aumt   lists space-separated indices of positional arguments to
                  the AU macro that should be suppressed from appearance in
                  the document heading on the first page of MT memorandum
                  types 0–3 and 6.  By default, it is undefined; all
                  arguments are formatted except the second (author
                  initials).

           BU     interpolates a bullet mark, \[bu].

           Capec  “Equation”

           Capex  “Exhibit”

           Capfg  “Figure”

           Captb  “Table”

           Captc  “CONTENTS”

           Ci     assigns indentation amounts used by each heading level
                  listed in a table of contents, in one-to-one
                  correspondence, overriding those computed by TC.  Each word
                  must be a horizontal measurement (like “1i”).

           DT     stores the date or other identifier set by ND, if called,
                  and otherwise one constructed using the formatter's date
                  registers; see groff(1).  The groff locale determines its
                  format, but register Isodate may override it.

           EM     interpolates an em dash, \[em].

           F      interpolates an automatically numbered footnote mark; the
                  number is used by the next FS call without an argument.  In
                  troff mode, the mark is superscripted; in nroff mode, it is
                  surrounded by square brackets.

           H1txt  stores the text of the current first-level heading; H and
                  HU update it, as does TC when processing table of contents
                  entries and captions of displayed figures, tables,
                  equations, and exhibits.

           HF     assigns font identifiers, separated by spaces, to heading
                  levels in one-to-one correspondence.  Each identifier may
                  be a font mounting position, font name, or style name.
                  Omitted values are assumed to be 1.  The default is “2 2 2
                  2 2 2 2 2 2 2 2 2 2 2”, which places all headings in
                  italics.  DWB's default was “3 3 2 2 2 2 2”.

           HP     assigns type sizes, separated by spaces, to heading levels
                  in one-to-one correspondence.  groff mm interprets each
                  size in typographical points, translating zero values to
                  10.  Omitted values are assumed to be 0 (and are translated
                  accordingly).  The default is “0 0 0 0 0 0 0 0 0 0 0 0 0
                  0”.

           Index  “INDEX”

           Le     “LIST OF EQUATIONS”

           Letfc  “Yours very truly,” (see FC)

           Letapp “APPROVED:” (see AV)

           LetAT  “ATTENTION:” (see LO)

           LetCN  “CONFIDENTIAL” (see LO)

           Letdate
                  “Date” (see AV)

           Letns  is a group of strings structuring the notations produced by
                  NS.  If the code argument to NS has no corresponding
                  string, the notation is included between parentheses,
                  prefixed with Letns!copy, and suffixed with Letns!to.
                  Observe the spaces after “Copy” and before “to”.

                  NS code   String       Contents
                  0         Letns!0      Copy to
                  1         Letns!1      Copy (with att.) to
                  2         Letns!2      Copy (without att.) to
                  3         Letns!3      Att.
                  4         Letns!4      Atts.
                  5         Letns!5      Enc.
                  6         Letns!6      Encs.
                  7         Letns!7      Under separate cover
                  8         Letns!8      Letter to
                  9         Letns!9      Memorandum to
                  10        Letns!10     Copy (with atts.) to
                  11        Letns!11     Copy (without atts.) to
                  12        Letns!12     Abstract Only to
                  13        Letns!13     Complete Memorandum to
                  14        Letns!14     CC
                  —         Letns!copy   Copy (with trailing space)
                  —         Letns!to      to (note leading space)

           Letnsdef
                  selects the notation format when NS is given no argument.
                  The default is 0.

           LetRN  “In reference to:” (see LO)

           LetSA  “To Whom It May Concern:” (see LO)

           LetSJ  “SUBJECT:” (see LO)

           Lf     “LIST OF FIGURES”

           Lt     “LIST OF TABLES”

           Lx     “LIST OF EXHIBITS”

           MO1
           ...
           MO12   “January” through “December”

           Qrf    “See chapter \E*[Qrfh], page \En[Qrfp].”  If your document
                  uses multiple heading levels, you might redefine this
                  string to use the word “section” instead of “chapter”.

           Qrfh   stores the heading mark corresponding to the most recent
                  GETR call.

           Qrfp   stores the page number corresponding to the most recent
                  GETR call.

           Rf     interpolates an automatically numbered reference mark; the
                  number is used by the next RS call.

           Rp     “REFERENCES”

           Rpfmt  specifies the LB arguments that groff mm uses to format the
                  items in an RP reference list.  The default is “\\n[Li] 0 1
                  0 \& 0”.

           Rg     interpolates the registered (trade) mark sign.

           Sm     interpolates the service mark sign.

           Tcstatus
                  interpolates an indicator of the TC macro's processing
                  status.  If TC is not operating, it is empty.  User-defined
                  TP or EOP macros might condition page headers or footers on
                  its contents.

                  Value   Meaning
                  co      Table of contents
                  fg      List of figures
                  tb      List of tables
                  ec      List of equations
                  ex      List of exhibits
                  ap      Appendix

           Tm     interpolates ™, the trade mark sign.

           Verbnm supplies argument(s) to the nm request employed by the
                  VERBON macro.  The default is 1.

## [](#Registers)Registers

           Default register values, where meaningful, are shown in
           parentheses.

           .mgm   indicates that groff mm is in use (Boolean-valued; 1).

           Aph    formats an appendix heading (and title, if supplied); see
                  APP (Boolean-valued; 1).

           Au     includes supplemental author information (the third and
                  subsequent arguments to AU) in memorandum “from”
                  information; see COVER and MT, and the Aumt string
                  (Boolean-valued; 1).

           Cl     sets the threshold for inclusion of headings in a table of
                  contents.  Headings at levels above this value are
                  excluded; see H and TC.  The Cl register controls whether a
                  heading is saved for output in the table of contents at the
                  time H or HU is called; if you change Cl's value
                  immediately prior to calling TC, you are unlikely to get
                  the result you want (2).

           Cp     suppresses page breaks before lists of captioned equations,
                  exhibits, figures, and tables, and before an index; see EC,
                  EX, FG, TB, and INDP (Boolean-valued; 0).

           D      produces debugging information for the mm package on the
                  standard error stream.  A value of 0 outputs nothing;
                  1 reports formatting progress.  Higher values communicate
                  internal state information of increasing verbosity (0).

           De     causes a page break after a floating display is output; see
                  DF (Boolean-valued; 0).

           Df     configures the behavior of DF.  The following values are
                  recognized; 4 and 5 do not override the De register (5).

                  Value   Effect
                  0       Flush pending displays at the end of each section
                          when section-page numbering is active, otherwise at
                          the end of the document.
                  1       Flush a pending display on the current page or
                          column if there is enough space, otherwise at the
                          end of the document.
                  2       Flush one pending display at the top of each page
                          or column.
                  3       Flush a pending display on the current page or
                          column if there is enough space, otherwise at the
                          top of the next.
                  4       Flush as many pending displays as possible in a new
                          page or column.
                  5       Fill columns or pages with flushed displays until
                          none remain.

           Ds     puts vertical space in the amount of register Dsp (if
                  defined) or Lsp before and after each static display; see
                  DS (Boolean-valued; 1).

           Dsp    configures the amount of vertical space placed before and
                  after static displays; see DS and register Ds (undefined).

           Ec     is an auto-incrementing equation counter; see EC.

           E      determines the font style used by MT memoranda, LT letters,
                  and the ms.cov cover page style to set the date and certain
                  other document data; 0 selects roman, and 1 bold (Boolean-
                  valued; 1).

           Ej     sets the threshold for page breaks (ejection) prior to the
                  format of headings.  Headings at levels above this value
                  are set on the same page and column as any preceding text
                  if possible; see H (0).

           Eq     aligns an equation label to the left of a display instead
                  of the right (Boolean-valued; 0).

           Ex     is an auto-incrementing exhibit counter; see EX.

           Fg     is an auto-incrementing figure counter; see FG.

           Fs     is multiplied by register Lsp to vertically separate
                  footnotes; see FS (1).

           Ftnum  is an auto-incrementing footnote counter; see FS.  groff mm
                  recognizes :p as an alias of Ftnum for DWB compatibility.

           H1
           ...
           H14    are auto-incrementing counters corresponding to each
                  heading level; see H.

           H1dot  appends a period to the number of a level one heading; see
                  H (Boolean-valued; 1).

           H1h    is a copy of register H1, but it is incremented just before
                  a page break.  This can be useful in hook macros; see H and
                  HX.

           Hb     sets the threshold for breaking the line after formatting a
                  heading.  Text after headings at levels above this value is
                  set on the same output line if possible.  Paragraphs
                  numbered via nP or the Np register cause a break
                  regardless; see H (2).

           Hc     sets the threshold for centering a heading.  Headings at
                  levels above this value use the prevailing alignment (that
                  is, they are not centered); see H (0).

           Hi     selects an indentation policy for text formatted after
                  headings.  It does not affect “run-in” headings.  The
                  following values are recognized; see H and P (1).

                  Value   Effect
                  0       no indentation
                  1       indent per the paragraph type
                  2       indent to align with heading title

           Hps    sets the heading level threshold for application of
                  preceding vertical space; see H.  Headings at levels above
                  the value in register Hps use the amount of space in
                  register Hps1; otherwise that in Hps2.  The value of Hps
                  should be strictly greater than that of Ej (1).

           Hps1   configures the amount of vertical space preceding a heading
                  above the Hps threshold; see H (troff devices: 0.5v; nroff
                  devices: 1v).

           Hps2   configures the amount of vertical space preceding a heading
                  within the Hps threshold; see H (troff devices: 1v; nroff
                  devices: 2v).

           Hs     sets the heading level threshold for application of
                  succeeding vertical space.  If the heading level is greater
                  than Hs, the heading is followed by vertical space in the
                  amount of register Hss; see H (2).

           Hss    is multiplied by register Lsp to produce vertical space
                  after headings above the threshold in register Hs; see H
                  (1).

           Ht     suppresses output of heading level counters above the
                  deepest when a heading mark is formatted; see H (Boolean-
                  valued; 0).

           Hu     sets the heading level used by unnumbered headings; see HU
                  (2).

           Hy     enables automatic hyphenation of words (Boolean-valued; 0).

           Isodate
                  configures the use of ISO 8601 date format; that is, YYYY-
                  MM-DD instead of the format specified by the localization
                  file.  Call ND without arguments after updating its value
                  (Boolean-valued; 0).

           L      defines the page length for the document, and must be set
                  from the command line.  A scaling unit should be appended.
                  The default is that of the selected groff output device.

           Le
           Lf
           Lt
           Lx     configure the report of lists of equation, figure, table,
                  and exhibit captions, respectively, after a table of
                  contents; see TC (all: Boolean-valued; 1).

           Letwam sets the maximum number of input lines permitted in a
                  writer's address; see WA and WE (14).

           Li     configures the text indentation (in ens) applied to
                  enumerated list types; that is, to items in AL and RL
                  lists, and in LB lists whose type argument is greater than
                  zero (5).

           Ls     sets a threshold for placement of vertical space before
                  list items.  If the list nesting level is greater than this
                  value, no such spacing occurs; see LI (\n[.R]).

           Lsp    configures the base amount of vertical space used for
                  separation in the document.  mm applies this spacing to
                  many contexts, sometimes with multipliers; see DS, FS, H,
                  LI, and P (troff devices: 0.5v; nroff devices: 1v).

           N      configures the header and footer placements used by PH.
                  The default footer is empty.  If “section-page” numbering
                  is selected, the default header becomes empty and the
                  default footer becomes “x-y”, where x is is the section
                  number (the number of the current first-level heading)
                  and y the page number within the section.  The following
                  values are recognized; for finer control, see PH, PF, EH,
                  EF, OH, and OF, and registers Sectf and Sectp.  Value 5 is
                  a groff mm extension (0).

                  Value   Effect
                  0       Set header on all pages.
                  1       Move header to footer on page 1.
                  2       Omit header on page 1.
                  3       Use “section-page” numbering style on all pages.
                  4       Omit header on all pages.
                  5       Use “section-page” and “section-figure” numbering
                          style on all pages.

           Np     numbers paragraphs with a leading mark in the format s.p,
                  where s is is first-level heading number and p is the
                  paragraph number, starting at 1; see H and P (Boolean-
                  valued; 0).

           O      defines the page offset of the document, and must be set
                  from the command line.  A scaling unit should be appended.
                  The default is .75i on terminal devices.  On typesetters,
                  it is .963i or set to 1i by the papersize.tmac package; see
                  groff_tmac(5).

           Oc     suppresses the appearance of page numbers in the table of
                  contents; see TC (Boolean-valued; 0).

           Of     selects a separator format within equation, exhibit,
                  figure, and table captions; see EC, EX, FG, and TB.  The
                  punctuation in the separator is either a dot or the EM
                  string.  The following values are recognized; the spaces
                  shown are unpaddable (0).

                  Value   Effect
                  0       ".  "
                  1       " — "

           P      interpolates the current page number; it is the same as
                  register % except when “section-page” numbering is enabled.

           Pi     configures the indentation (in ens) applied to the first
                  line of an unnumbered paragraph that has such (see P); and
                  the text indentation of non-enumerated list items; that is,
                  to items in BL, BVL, DL, and VL lists (but not ML), and in
                  LB lists whose type argument is zero or less (5).

           Pgps   causes the type size and vertical spacing set by S to apply
                  to headers and footers, overriding the HP string.  If not
                  set, S calls affect headers and footers only when followed
                  by PH, PF, OH, EH, OF, or EF calls (Boolean-valued; 1).

           Ps     is multiplied by register Lsp to vertically separate
                  paragraphs; see P (1).

           Pt     determines when a first-line indentation is applied to a
                  paragraph; see P (0).

                  Value   Effect
                  0       never
                  1       always
                  2       always, except immediately after H, HU, DE, or LE

           Ref    is used internally to control mmroff(1)'s two-pass approach
                  to index and reference management; see IND, INDP, INITI,
                  INITR, and PIC (Boolean-valued; 0).

           Rfnum  is an auto-incrementing reference counter; see RS.  groff
                  mm recognizes :R as an alias of Rfnum for DWB
                  compatibility.

           Rfstyle
                  determines the format of the reference number in the Rf
                  string.  groff mm maps 0 to 1 in nroff mode and 2 in troff
                  mode (0).

                  Value   Meaning
                  0       automatic
                  1       bracketed
                  2       superscripted
                  3       bracketed and superscripted

                  Changes to Rfstyle's value may not take effect until the
                  next heading or paragraphing macro call.

           Rpej   configures the default page ejection policy for reference
                  pages; see RP (0).

                  Value   Effect
                  0       Break the page before and after the reference list.
                  1       Suppress page break after the list.
                  2       Suppress page break before the list.
                  3       Suppress page breaks before and after the list.

           S      defines the type size for the document, and must be set
                  from the command line.  A scaling unit should be appended;
                  p is typical (10p).

           Sectf  selects the “section-figure” numbering style.  Its default
                  is 0 unless register N is set to 5 at the command line
                  (Boolean-valued).

           Sectp  selects the “section-page” numbering style.  Its default
                  is 0 unless register N is set to 3 or 5 at the command line
                  (Boolean-valued).

           Si     configures the amount of display indentation in ens; see DS
                  (5).

           Tb     is an auto-incrementing table counter; see TB.

           V      defines the vertical spacing for the document, and must be
                  set from the command line.  A scaling unit should be
                  appended; p is typical.  The default vertical spacing is
                  120% of the type size.  This register is a groff mm
                  extension.

           Verbin configures the amount of indentation for verbatim displays
                  when indentation is selected; see VERBON (5n).

           W      defines the “width” of the document (that is, the length of
                  an output line with no indentation); it must be set from
                  the command line.  A scaling unit should be appended.  The
                  default is 6i or assigned by the papersize.tmac package;
                  see groff_tmac(5).

       Internals
           The argument (if any) to a COVER or MT call determines the file
           that groff mm loads to configure the document's layout; see
           section “Files” below.

           LT's behavior depends on the style argument given to it; it calls
           macros with names suffixed accordingly.  It is therefore possible
           to define additional letter types, either in the territory-
           specific macro file, or as local additions.  LT sets the registers
           Pt and Pi to 0 and 5, respectively.  (DWB used a value of 3 for
           Pi.)  It then calls an initialization macro corresponding to the
           type.  Define the following macros to support a new letter type.

           let@init_type
                  initializes any registers and other data needed by the
                  letter type.

           let@head_type
                  formats the letterhead; it is called instead of the usual
                  page header macro.  Its definition should remove the alias
                  let@header unless the letterhead is desired on subsequent
                  pages.

           let@sg_type name title n is-final [SG-arg ...]
                  is called by SG only for LT letters; MT memoranda implement
                  their own signature processing.  name and title are
                  specified through WA/WE.  n is the index of the nth writer,
                  and is-final is true for the last writer to be listed.
                  Further SG arguments are appended to the signature line.

           let@fc_type closing
                  is called by FC, and takes the formal closing as its
                  argument.

           LO implements letter options.  It requires that a string named
           Lettype be defined, where type is the letter type.  LO then
           assigns its second argument (value) to the string let*lo-type.

## [](#Files)Files

           /usr/local/share/groff/1.24.1/tmac/m.tmac
                  is the groff implementation of the memorandum macros.

           /usr/local/share/groff/1.24.1/tmac/mm.tmac
                  is a wrapper enabling the package to be loaded with the
                  option “-m mm”.

           /usr/local/share/groff/1.24.1/tmac/refer-mm.tmac
                  implements refer(1) support for mm.

           /usr/local/share/groff/1.24.1/tmac/mm/ms.cov
                  implements an ms-like cover page.

           /usr/local/share/groff/1.24.1/tmac/mm/0.MT
                  implements memorandum types 0–3 and 6.

           /usr/local/share/groff/1.24.1/tmac/mm/4.MT
                  implements memorandum type 4.

           /usr/local/share/groff/1.24.1/tmac/mm/5.MT
                  implements memorandum type 5.

           /usr/local/share/groff/1.24.1/tmac/mm/locale
                  performs any (further) desired localization if present.

           /usr/local/share/doc/groff-1.24.1/examples/letter.mm
                  illustrates features of the LT letter formats.

           /usr/local/share/doc/groff-1.24.1/examples/memorandum.mm
                  illustrates features of the MT memorandum formats.

           /usr/local/share/doc/groff-1.24.1/examples/story.mm
                  illustrates use of mm for literary purposes.

## [](#Authors)Authors

           Jörgen Hägg ⟨jh@axis.se⟩ of Lund, Sweden, wrote the version of the
           mm macro package distributed with groff based on an early version
           of groff ms by James Clark ⟨jjc@jclark.com⟩.  Werner Lemberg ⟨wl@
           gnu.org⟩ and G. Branden Robinson ⟨g.branden.robinson@gmail.com⟩
           revised and updated it.

## [](#See_also)See also

           MM - A Macro Package for Generating Documents 
           ⟨https://tkurtbond.github.io/troff/mm-all.pdf⟩, the DWB 3.3 mm
           manual, introduces the package but does not document groff mm
           extensions.

           Groff: The GNU Implementation of troff, by Trent A. Fisher and
           Werner Lemberg, is the primary groff manual.  You can browse it
           interactively with “info groff”.

           groff(1), troff(1), tbl(1), pic(1), eqn(1), refer(1),
           groff_mmse(7)

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

    groff 1.24.1                    2026-03-14                    groff_mm(7)

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
