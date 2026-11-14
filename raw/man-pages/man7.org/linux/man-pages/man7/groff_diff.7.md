---
{"title": "groff_diff(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/groff_diff.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groff_diff(7) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Description](#Description) \| [Language](#Language) \| [Formatter output](#Formatter_output) \| [Debugging](#Debugging) \| [Compatibility mode](#Compatibility_mode) \| [Other differences](#Other_differences) \| [Authors](#Authors) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    groff_diff(7)        Miscellaneous Information Manual       groff_diff(7)

## [](#Name)Name

           groff_diff - differences between GNU roff and AT&T troff

## [](#Description)Description

           The GNU roff text processing system, groff, is a reimplementation
           and extension of AT&T troff, the typesetting system originating in
           Unix systems of the 1970s.  groff removes many arbitrary
           limitations and adds features, both to the input language and to
           the page description language output by the troff formatter.  We
           also note here differences arising from groff's implementation of
           AT&T troff features.  The following discussion assumes familiarity
           with those features; see roff(7) for background.  GNU troff can
           operate in a manner that increases support for documents written
           for AT&T troff; see section “Compatibility mode” below.

## [](#Language)Language

           GNU troff features identifiers of arbitrary length; supports color
           output, non-integral type sizes, user-defined characters, and
           automatic hyphenation in languages other than English; adds more
           conditional expression operators; recognizes additional scaling
           units and arithmetic operators; enables general file I/O (in
           “unsafe mode” only); and exposes more formatter state.

       Long names
           GNU troff introduces many new requests; with three exceptions (cp,
           do, rj), they have names longer than two characters.  The names of
           registers, fonts, strings/macros/diversions, environments, special
           characters, character classes, streams, hyphenation language
           codes, and colors can be of any length.  Anywhere AT&T troff
           supports a parameterized escape sequence that uses an opening
           parenthesis “(” to introduce a two-character argument, groff
           supports a square-bracketed form “[]” where the argument within
           can be of arbitrary length.

       Font families, abstract styles, and translation
           GNU troff can group text typefaces into families.  For example,
           groff ships with support for families containing each of the
           styles “R”, “I”, “B”, and “BI” (roman [upright], bold, italic
           [slanted], and bold-italic).  So that a document need not be
           coupled to a specific font family, an output device can associate
           a style in the abstract sense with a mounting position.  Thus the
           default family can combine with a style dynamically, producing a
           resolved font name.  A document can translate, or remap, font
           names with the ftr request.

           Applying the requests cs, bd, tkf, uf, or fspecial to an abstract
           style affects the member of the default family corresponding to
           that style.  The default family can be set with the fam request or
           -f command-line option.  The styles directive in the output
           device's DESC file controls which mounting positions (if any) are
           initially associated with abstract styles rather than fonts, and
           the sty request can update this association.

       Colors
           groff supports color output with a variety of color spaces and up
           to 16 bits per channel.  Some devices, particularly terminals, may
           be more limited.  When color support is enabled, two colors are
           current at any given time: the stroke color, with which glyphs,
           rules (lines), and geometric figures are drawn, and the fill
           color, which paints the interior of filled geometric figures.  The
           color, defcolor, gcolor, and fcolor requests; \m and \M escape
           sequences; and .color, .m, and .M registers exercise color
           support.

       Hyphenation
           GNU troff uses a hyphenation algorithm and language-specific
           pattern files (based on TeX's) to decide which words can be
           hyphenated and where.  AT&T troff's hyphenation system (“suftab”)
           was specific to English.

           New requests permit finer control over hyphenation breaking;
           hyphenation of a word might be suppressed due to a limit on
           consecutive hyphenated lines (hlm), a minimum line length
           threshold (hym), or because the line can instead be adjusted with
           additional inter-word space (hys).  The hla request selects a
           hyphenation language, whereas hpf and hpfa respectively load and
           append to the language's hyphenation patterns.  If no hyphenation
           language is set or no patterns are loaded, GNU troff does not
           perform automatic hyphenation.

           For automatic hyphenation to work, the formatter must know which
           letters are equivalent.  For example, the letter “E” behaves like
           “e”; only the latter typically appears in hyphenation pattern
           files.  GNU troff expects characters that participate in automatic
           hyphenation to be assigned hyphenation codes that define these
           equivalence classes.  At startup, GNU troff assigns hyphenation
           codes to the letters “a”–“z”, applies the same codes to “A”–“Z” in
           one-to-one correspondence, and assigns a code of zero to all other
           characters.

           The hcode request enables application of hyphenation codes to
           characters outside the Unicode basic Latin set; without doing so,
           words containing such letters won't hyphenate properly even if the
           corresponding hyphenation patterns contain them.  Localization
           files for the input character set and language configure
           hyphenation codes; see groff_tmac(5).

           GNU troff's \: escape sequence works like \% but produces no
           hyphen if the word breaks at that location.

       Fractional type sizes and new scaling units
           When configuring the type size, AT&T troff ignored scaling units
           and interpreted all measurements in points.  Combined with integer
           arithmetic, this design choice made it impossible to support, for
           instance, ten-and-a-half-point type.  In GNU troff an output
           device can select a scaling factor that subdivides a point into
           “scaled points”.  A type size expressed in scaled points can thus
           represent a non-integral size in points.

           A scaled point, scaling unit s, is equal to 1/sizescale points,
           where the device description file, DESC, specifies sizescale and
           otherwise defaults to 1; see groff_font(5).  GNU troff also
           defines the typographical point, scaling unit z, which explicitly
           specifies a type size of potentially non-integral measure.  The
           program multiplies typographical points by sizescale and converts
           the value to an integer.  Arguments GNU troff interprets in z
           units by default comprise those to the escape sequences \H and \s,
           to the request ps, the third argument to the cs request, and the
           second and fourth arguments to the tkf request.  In GNU troff, the
           register \n[.s] interpolates the type size in typographical points
           (z), whereas the register \n[.ps] interpolates it in scaled points
           (s).  “\n[.ps]s”, “\n[.s]z”, and “1m” are co-equal by definition.

           For example, if sizescale is 1000, then a scaled point is one
           thousandth of a point.  Consequently, “.ps 10.5” is synonymous
           with “.ps 10.5z”; both set the type size to 10,500 scaled points
           or 10.5 typographical points.

           It makes no sense to use the “z” scaling unit in a numeric
           expression whose default scaling unit is neither “u” nor “z”, so
           GNU troff disallows this.  Similarly, it is nonsensical to use
           scaling units other than “p”, “s”, “z”, or “u”, in a numeric
           expression whose default scaling unit is “z”, and so GNU troff
           disallows those as well.

           Output devices may be limited in the type sizes they can employ.
           The .s and .ps registers represent the type size selected by the
           formatter as it understands a device's capability.  the read-only
           registers .psr and (string-valued) .sr interpolate the last
           requested in scaled points and in points as a decimal fraction,
           respectively.  Like the actual current and previous type size, the
           requested ones are properties of an environment.

           For example, if a document requests a type size of 10.95 points,
           and the nearest size permitted by a sizes request (or by the sizes
           or sizescale directives in the device's DESC file) is 11 points,
           groff uses the latter value.

           A further two new measurement units available in groff are “M”,
           which indicates hundredths of an em, and “f”, which multiplies by
           65,536.  The latter provides convenient fractions for color
           definitions with the defcolor request.  For example, 0.5f equals
           32768u.

       Special fonts
           GNU troff's “special” and fspecial requests permit a document to
           supplement the set of fonts the device configures for glyph search
           without having to use the fp request to manipulate the list of
           mounting positions, which can be tedious—by default, GNU troff
           mounts 40 fonts at startup when using the ps device.

       Numeric expressions
           GNU troff permits spaces in a numeric expression within
           parentheses, and offers three new operators.

           e1>?e2 Interpolate the greater of expressions e1 and e2.

           e1<?e2 Interpolate the lesser of expressions e1 and e2.

           (c;e)  Interpolate expression e using c as the default scaling
                  unit, ignoring scaling units in e if c is empty.

           Arithmetic in GNU troff saturates instead of wrapping.

       Conditional expressions
           More conditions can be tested with the “if” and ie requests, as
           well as the new “while” request.

           c chr  True if a character chr is available; chr is an ordinary,
                  special, or indexed character, whether defined by a font
                  description file or a request.

           d nam  True if a string, macro, diversion, or request nam is
                  defined.

           F fnt  True if a font fnt is available; fnt can be an abstract
                  style or a font name.  fnt is handled as if it were an
                  argument to the ft request (that is, the default family is
                  combined with an abstract style and font translation is
                  applied), but fnt cannot be a mounting position, and no
                  font is mounted.

           m col  True if a color col is defined.

           r reg  True if a register reg is defined.

           S sty  True if an abstract style sty is registered.  Font
                  translations apply.

           v      Always false.  This condition exists for compatibility with
                  certain other troff implementations.  (We refer to vtroff,
                  a translator that converted the C/A/T command stream
                  produced by early-vintage AT&T troff to a form suitable for
                  Versatec and Benson-Varian plotters.)

       Drawing commands
           GNU troff extends the \D escape sequence with drawing commands to
           create filled circles and ellipses, and polygons.  Stroked
           (outlined) objects are drawn with the stroke color and filled
           (solid) ones shaded with the fill color.  These are independent
           properties; if you want a filled, stroked figure, you must draw
           the same figure twice using each command.  A filled figure is
           smaller than a stroked one using the same parameters because the
           former is drawn only within its defined area, whereas strokes have
           a line thickness, set with another new drawing command.

       Notational conventions
           In the request and escape sequence descriptions below, GNU troff
           reads arguments named character-sequence, command, contents, file,
           and message in copy mode until the end of the input line.  A
           character-sequence comprises one or more ordinary, special, or
           indexed characters; spaces; or escape sequences that interpolate
           only these.  We name the remaining arguments for clarity; they are
           also character-sequences.  A neutral double quote ‘"’ can
           optionally prefix a character-sequence; the formatter discards one
           if present, permitting initial embedded spaces in the argument.

           input refers to arbitrary character sequences (up to a newline or
           delimiter) that GNU troff fully interprets, in contrast to copy
           mode.

       Escape sequences
           groff introduces several new escape sequences, extends the syntax
           of the AT&T troff escape sequences \D, \f, \k, \n, \s, \$, and \*,
           and alters the behavior of \X.  The following list collates escape
           sequences alphabetically at first, and then by symbol roughly in
           Unicode code point order.  Neutral apostrophes ' illustrate escape
           sequences with a user-selectable delimiter.  Many others are
           available; see subsection “Miscellaneous” and section
           “Compatibility Mode” below.

           \A'input'
                  Interpolate 1 if input is a valid identifier, and 0
                  otherwise.  Because GNU troff ignores any input character
                  with an invalid code when reading it, invalid identifiers
                  are empty or contain spaces, tabs, newlines, or escape
                  sequences that interpolate something other than a sequence
                  of ordinary characters.  You can employ \A to validate a
                  macro argument before using it to construct another escape
                  sequence or identifier.

           \B'input'
                  Interpolate 1 if input is a valid numeric expression, and 0
                  otherwise.  You might use \B along with the “if” request to
                  filter out invalid macro arguments.

           \D'C d'
                  Draw filled circle of diameter d with its leftmost point at
                  the drawing position.

           \D'E h v'
                  Draw filled ellipse of axis lengths h and v, with its
                  leftmost point at the drawing position.

           \D'p h1 v1 ... hn vn'
                  Draw polygon with vertices at the drawing position and each
                  point in sequence.  GNU troff closes the polygon by drawing
                  a line from (hn, vn) back to the initial drawing position;
                  DWB and Heirloom troffs do not.  Afterward, the drawing
                  position is left at (hn, vn).

           \D'P h1 v1 ... hn vn'
                  As \D'p', but the polygon is filled.  groff does not
                  specify how the output device must fill concave or self-
                  intersecting polygons.

           \D't n'
                  Set line thickness of geometric objects to n basic units.
                  A zero n selects the minimum supported thickness.  A
                  negative n (the default) selects a thickness proportional
                  to the type size.

           \E     Embed an escape character that is not interpreted in copy
                  mode (compare with \a and \t).  You can use it to ease the
                  writing of nested macro definitions.  It is also convenient
                  to define strings containing escape sequences that need to
                  work when used in copy mode (for example, as macro
                  arguments), or that will be interpolated at varying macro
                  nesting depths.

           \f[fnt]
                  Select typeface fnt, which may be a mounting position,
                  abstract style, or font name.  \f[], \f[P], and \fP are
                  synonyms; we recommend the first.

           \Ff
           \F(fm
           \F[fml]
                  Select default font family.  \F[] makes the previous font
                  family the default.  \FP is unlike \fP; it selects font
                  family “P” as the default.  See the fam request below.

           \k(rg
           \k[reg]
                  Store the horizontal drawing position, relative to that
                  corresponding to the start of the input line (ignoring page
                  offset and indentation), in two-character register name rg
                  or arbitrary register name reg.

           \mc
           \m(cl
           \m[col]
                  Set stroke color to col.  \m[] restores the previous stroke
                  color, or the default if there is none.

           \Mc
           \M(cl
           \M[col]
                  Set fill color to col.  \M[] restores the previous fill
                  color, or the default if there is none.

           \n[reg]
                  Interpolate register reg.

           \On
           \O[n]  Suppress troff output of glyphs and geometric objects.  The
                  sequences \O2, \O3, \O4, and \O5 are intended for internal
                  use by grohtml(1).

                  \O0
                  \O1    Disable and enable, respectively, the emission of
                         glyphs and geometric objects to the output driver,
                         provided that this sequence occurs at the outermost
                         suppression level (see \O3 and \O4).  Horizontal
                         motions corresponding to non-overstruck glyph widths
                         still occur.  These sequences also reset the
                         registers opminx, opminy, opmaxx, and opmaxy to -1.
                         These four registers mark the top left and bottom
                         right hand corners of a box encompassing all written
                         or drawn output.

                  \O2    At the outermost suppression level, enable emission
                         of glyphs and geometric objects, and write to the
                         standard error stream the page number and values of
                         the four aforementioned registers encompassing
                         glyphs written since the last interpolation of a \O
                         sequence, as well as the page offset, line length,
                         image file name (if any), horizontal and vertical
                         device motion quanta, and input file name.  Numeric
                         values are in basic units.

                  \O3
                  \O4    Begin and end a nested suppression level,
                         respectively.  grohtml uses this mechanism to create
                         images of output preprocessed with pic, eqn, and
                         tbl.  At startup, troff is at the outermost
                         suppression level.  pre-grohtml generates these
                         sequences when processing the document, using troff
                         with the ps output device, Ghostscript, and the PNM
                         tools to produce images in PNG format.  These
                         sequences start a new page if the device is not html
                         or xhtml, to reduce the number of images crossing a
                         page boundary.

                  \O5[Pfile]
                         At the outermost suppression level, write the name
                         file to the standard error stream at position P,
                         which must be one of l, r, c, or i, corresponding to
                         left, right, centered, and inline alignments within
                         the document, respectively.  file is a name
                         associated with the production of the next image.

           \R'name ±n'
                  Synonymous with “.nr name ±n”.

           \s[0]
           \s'0'  Restore the previous type size; no operation if there is
                  none.

           \s[±n]
           \s±[n]
           \s'±n'
           \s±'n' Set the type size to, or increment or decrement it by,
                  n typographical points.

           \Ve
           \V(ev
           \V[env]
                  Interpolate contents of the system environment variable env
                  (one-character name e, two-character name ev) as returned
                  by getenv(3).  \V is interpreted even in copy mode.

           \X'character-sequence'
                  Unlike AT&T troff, GNU troff performs some limited
                  processing of the sequence of ordinary characters, special
                  characters, and spaces in character-sequence.

                  The formatter's special character repertoire is unknown to
                  output drivers outside of glyphs named in a device's fonts,
                  and even then they may not possess complete coverage of the
                  names documented in groff_char(7).  Further, escape
                  sequences that produce horizontal or vertical motions,
                  hyphenation breaks, or that are dummy characters may appear
                  in strings or be converted to nodes, particularly in
                  diversions.  When they occur in a device extension command,
                  they produce warnings in category “char”.  These are not
                  representable when interpolated directly into device-
                  independent output, as might be done when writing out tag
                  names for PDF bookmarks, which can appear in a viewer's
                  navigation pane.  This is also the case for a small number
                  of special characters, such as \[ru], the baseline rule,
                  that lack a Unicode definition.

                  So that any Unicode code point can be represented in device
                  extension commands, for example in an author's name in
                  document metadata or as a usefully named bookmark or
                  hyperlink anchor, GNU troff transforms its argument to
                  represent characters outside the Unicode Basic Latin range
                  as Unicode code points expressed in groff's notation for
                  these, “\[uXXXX]”; see groff_char(7).  For these
                  transformations, the formatter ignores character
                  translations and definitions.

                  GNU troff converts several ordinary characters that typeset
                  as non-basic Latin code points to code points outside that
                  range so that they are used consistently whether they are
                  formatted as glyphs or used in a device extension command
                  argument.  These ordinary characters are “'”, “-”, “^”,
                  “`”, and “~”; others are written as-is.  Thus, “'”
                  transforms to “\[u2019]”.

                  Contrariwise, GNU troff translates special characters that
                  typeset as Unicode basic Latin characters to basic Latin
                  characters accordingly.  Thus, “\[ga]” transforms to “`”,
                  “\[Do]” to “$”, and so on.

           \Ym
           \Y(ma
           \Y[mac]
                  Interpolate a macro or string as a device extension
                  command.  As \X'\*[mac]', except that GNU troff does not
                  interpret the contents of mac; further, mac can be a macro
                  and thus contain newlines, unlike the argument to \X .
                  This inclusion of newlines requires an extension to the
                  AT&T troff device-independent page description language,
                  and their presence confuses drivers that do not know about
                  it (see subsection “Device control commands” of
                  groff_out(5)).

           \Z'input'
                  Save the drawing position, format input, then restore it.
                  GNU troff ignores tabs and leaders in input with an error
                  diagnostic.

           \#     Read everything up to and including the next newline in
                  copy mode and discard it.  \# is like \", except that \"
                  does not ignore a newline; the latter therefore cannot be
                  used by itself for a whole-line comment—it leaves a blank
                  line on the input stream.

           \$0    Interpolate the name by which the macro being interpreted
                  was called.  In GNU troff this name can vary; see the als
                  request.

           \$(nn
           \$[nnn]
                  In a macro or string definition, interpolate the nnth or
                  nnnth argument.  In GNU troff, macros and strings can have
                  an unlimited number of arguments.

           \$*    In a macro or string definition, interpolate the catenation
                  of all arguments, separated by spaces.

           \$@    In a macro or string definition, interpolate the catenation
                  of all arguments, with each surrounded by double quotes and
                  separated by spaces.

           \$^    In a macro or string definition, interpolate the catenation
                  of all arguments constructed in a form suitable for passage
                  to the ds request.

           \)     Interpolate a transparent dummy character—one that is
                  ignored by end-of-sentence detection.  It behaves as \&,
                  except that \& is treated as letters and numerals normally
                  are after “.”, “?”, and “!”; \& cancels end-of-sentence
                  detection, and \) does not.

           \*[string [arg ...]]
                  Interpolate string, passing it arg ... as arguments.

           \/     Apply an italic correction: modify the spacing of the
                  preceding glyph so that the distance between it and the
                  following glyph is correct if the latter is of upright
                  shape.  For example, if an italic “f” is followed
                  immediately by a roman right parenthesis, then in many
                  fonts the top right portion of the “f” overlaps the top of
                  the right parenthesis, which is ugly.  Inserting \/ between
                  them avoids this problem.  Consider using \/ whenever a
                  slanted glyph is immediately followed by an upright glyph
                  without any intervening space.

           \,     Apply a left italic correction: modify the spacing of the
                  following glyph so that the distance between it and the
                  preceding glyph is correct if the latter is of upright
                  shape.  For example, if a roman left parenthesis is
                  immediately followed by an italic “f”, then in many fonts
                  the bottom left portion of the “f” overlaps the bottom of
                  the left parenthesis, which is ugly.  Inserting \, between
                  them avoids this problem.  Consider using \, whenever an
                  upright glyph is followed immediately by a slanted glyph
                  without any intervening space.

           \:     Insert a non-printing break point.  That is, a word can
                  break there, but the soft hyphen character does not mark
                  the break point if it does (in contrast to “\%”).  The
                  remainder of the word is subject to hyphenation as normal.

           \?character-sequence\?
                  Suppress formatting of character-sequence.  This feature
                  has two applications.

                  Surround operands to the output comparison operator with \?
                  to compare them by character rather than as formatted
                  output.  Since GNU troff reads comparands protected with \?
                  in copy mode, they need not even be valid groff syntax.
                  The escape character is still lexically recognized,
                  however, and consumes the next character.

                  When used in a diversion, \? transparently embeds input,
                  read in copy mode, until its own next occurrence on the
                  input line.  Use \! if you want to embed newlines in a
                  diversion.  Unlike \!, \? is interpreted even in copy mode,
                  and a character-sequence in the top-level diversion is not
                  sent to device-independent output.

           \[char]
                  Typeset the special character char.  See groff_char(7).

           \[base-char combining-component ...]
                  Typeset a composite glyph consisting of base-char overlaid
                  with one or more combining-components.  For example,
                  “\[A ho]” is a capital letter “A” with a “hook accent”
                  (ogonek).  See the composite request below; Groff: The GNU
                  Implementation of troff, the groff Texinfo manual, for
                  details of composite glyph name construction; and
                  groff_char(7) for a list of components used in composite
                  glyph names.

           \~     Insert an adjustable, unbreakable space.  As with ordinary
                  spaces, GNU troff discards any sequence of these at the end
                  of an output line if a break occurs.

       Restricted requests
           To mitigate risks from untrusted input documents, GNU troff
           disables the cf, pi, and sy requests by default.  Its -U option
           enables “unsafe mode”, restoring their function (and enabling
           additional groff extension requests, “open”, opena, and pso).

       Altered requests
           .bd special-font font
                  Stop emboldening special-font when font is selected.
                  special-font must be a font name, not a mounting position.

           .cf ["]file
                  Break and copy the contents of file as “throughput” to GNU
                  troff's output.  If a diversion is in use, GNU troff
                  performs the copy only when the diversion is emitted.  In
                  AT&T troff, the contents of file are immediately copied to
                  the output regardless of whether a diversion is being
                  written to; this behavior is so anomalous that it must be
                  considered a bug.

                  GNU troff removes a leading neutral double quote ‘"’ from
                  the argument, permitting initial embedded spaces in it, and
                  reads it to the end of the input line in copy mode.  If
                  file does not exist or is not readable, a warning in
                  category “file” is emitted and the request has no other
                  effect.

           .de name [end-name]
           .am name [end-name]
           .ds name [["]contents]
           .as name [["]contents]
                  In compatibility mode, these requests behave as de1, am1,
                  ds1, and as1, respectively: GNU troff inserts a
                  compatibility save token at the beginning of the macro,
                  string, or appendment thereto as applicable and a
                  compatibility restore token at its end, enabling
                  compatibility mode during its interpolation.  Thus they
                  work as expected even if the interpolation context disables
                  compatibility mode.

           .hy n  New values 16 and 32 are available; the former enables
                  hyphenation before the last character in a word, and the
                  latter enables hyphenation after the first character in a
                  word.  If invoked without an argument, the mode configured
                  by the hydefault request is selected.

           .lf input-line-number [["]file-identifier]
                  In GNU troff the first argument becomes the input line
                  number of the next line the formatter reads.  It also
                  removes a leading neutral double quote ‘"’ from file-
                  identifier, permitting initial embedded spaces in it, and
                  reads it to the end of the input line in copy mode.

           .nx [["]file]
                  GNU troff removes a leading neutral double quote ‘"’ from
                  file, permitting initial embedded spaces in it, and reads
                  it to the end of the input line in copy mode.

           .pi ["]command
                  GNU troff strips a leading neutral double quote from the
                  argument, permitting initial embedded spaces in it.

           .pm name ...
                  GNU troff reports, to the standard error stream, the JSON-
                  encoded name and contents of each macro, string, or
                  diversion name.

           .so ["]file
                  GNU troff removes a leading neutral double quote ‘"’ from
                  file, permitting initial embedded spaces in it, and reads
                  it to the end of the input line in copy mode.  GNU troff
                  searches for file in any directories specified by -I
                  command-line options, followed by the current working
                  directory.  If file does not exist or is not readable, GNU
                  troff emits a warning in category “file”.

           .ss word-space-size [additional-sentence-space-size]
                  A second argument sets the amount of additional space
                  separating sentences on the same output line.  If omitted,
                  this amount is set to word-space-size.  Both arguments are
                  in twelfths of current font's space width (typically one-
                  fourth to one-third em for Western scripts; see
                  groff_font(5)).  The default for both parameters is 12.
                  Negative values are erroneous.

           .sy ["]command
                  GNU troff strips a leading neutral double quote from the
                  argument, permitting initial embedded spaces in it.

           .ta [[n1 n2 ... nn ]T r1 r2 ... rn]
                  GNU troff supports an extended syntax to specify repeating
                  tab stops after the “T” mark.  These values are always
                  taken as relative distances from the previous tab stop.
                  This is the idiomatic way to specify tab stops at equal
                  intervals in groff.  GNU troff's startup value is “T 0.5i”.

                  The syntax summary above instructs groff to set tabs at
                  positions n1, n2, ..., nn, then at nn+r1, nn+r2, ...,
                  nn+rn, then at nn+rn+r1, nn+rn+r2, ..., nn+rn+rn, and so
                  on.

       New requests
           Several GNU troff requests work like AT&T troff's “as” and ds
           requests, accepting an optional leading neutral double quote,
           notated ‘["]’, in an argument that the formatter reads in copy
           mode to the end of the input line, permitting inclusion of leading
           spaces.

           .aln new-register existing-register
                  Create alias (additional name) new-register of existing-
                  register, causing the names to refer to the same stored
                  object.  If existing-register is undefined, the formatter
                  ignores the request.  GNU troff produces a warning in
                  category “reg”.  See section “Warnings” of troff(1)
                  regarding the enablement and suppression of warnings.  To
                  remove a register alias, invoke rr on its name.  A
                  register's contents do not become inaccessible until it has
                  no more names.

           .als new-name existing-name
                  Create alias (additional name) new-name of request, string,
                  macro, or diversion existing-name, causing the names to
                  refer to the same stored object.  If existing-name is
                  undefined, the formatter ignores the request.  GNU troff
                  produces a warning in category “mac”.  If new-name already
                  exists, its contents are lost unless already aliased.  See
                  section “Warnings” of troff(1) regarding the enablement and
                  suppression of warnings.  To remove an alias, invoke rm on
                  its name.  The object itself is not destroyed until it has
                  no more names.

                  When a request, macro, string, or diversion is aliased,
                  redefinitions and appendments “write through” alias names.
                  To replace an alias with a separately defined object,
                  remove its name first.

           .am1 name [end-name]
                  As “am”, but GNU troff disables compatibility mode while
                  interpreting the appendment to name: it inserts a
                  compatibility save token at the beginning of the
                  appendment, and a compatibility restore token at its end.
                  The requests “am”, am1, de, and de1 can thus be intermixed
                  freely since the compatibility save/restore tokens affect
                  only the parts of the macro populated by am1 and de1.

           .ami name [end-name]
                  Append to macro indirectly.  See dei below.

           .ami1 name [end-name]
                  As ami, but GNU troff disables compatibility mode while
                  interpreting the appendment to the macro named by the
                  contents of string name; see am1 above.

           .as1 name [["]contents]
                  As “as”, but GNU troff disables compatibility mode while
                  interpreting the appendment to the string name: it inserts
                  a compatibility save token at the beginning of the
                  appendment, and a compatibility restore token at its end.
                  The requests “as”, as1, ds, and ds1 can thus be intermixed
                  freely since the compatibility save/restore tokens affect
                  only the portions of the string populated by as1 and ds1.

           .asciify div
                  Unformat the diversion div in a way such that Unicode basic
                  Latin (US-ASCII) characters, characters translated with the
                  trin request, space characters, and some escape sequences
                  that were formatted in the diversion div are treated like
                  ordinary input characters when div is interpolated.  Doing
                  so can be useful in conjunction with the writem request.

                  When transforming a glyph node back into an input sequence
                  that demands expression as a special character escape
                  sequence, GNU troff uses the default escape character.

                  asciify cannot return all nodes in a diversion to their
                  source equivalents: those produced by indexed characters
                  (\N), for example, remain nodes, so the result cannot be
                  guaranteed to be a character sequence as a macro or string
                  is.  Give the diversion name as an argument to the pm
                  request to inspect its contents and node list.  Glyph
                  parameters such as the type face and size are not
                  preserved; use “unformat” to achieve that.

           .backtrace
                  Write backtrace of input stack to the standard error
                  stream.  See the -b option of troff(1).

           .blm [name]
                  Set a blank line macro (trap).  If a blank line macro is
                  thus defined, groff executes name when a blank line is
                  encountered in the input, instead of the usual behavior.  A
                  line consisting only of spaces is also treated as blank and
                  subject to this trap.  If no argument is supplied, the
                  default blank line behavior is (re-)established.

           .box [name]
           .boxa [name]
                  Divert (or append) output to name, similarly to the di and
                  da requests, respectively.  Any pending output line is not
                  included in the diversion.  Without an argument, stop
                  diverting output; any pending output line inside the
                  diversion is discarded.

           .break Exit a “while” loop.  Do not confuse this request with a
                  typographical break or the br request.  See “continue”.

           .brp   Break and force adjustment of the output line per the
                  current adjustment mode.  Like br, it does nothing if
                  invoked with the no-break control character.

           .cflags n c...
                  Assign properties encoded by non-negative integer n to each
                  character or class c.  Spaces need not separate c
                  arguments.

                  n is the sum of any of the following.  Some combinations
                  are nonsensical, such as “33” (1 + 32).

                  1      Recognize the character as ending a sentence if
                         followed by a newline or two spaces.  Initially,
                         characters “.?!” have this property.

                  2      Enable breaks before the character.  A line is not
                         broken at a character with this property unless the
                         characters on each side both have non-zero
                         hyphenation codes.  This exception can be overridden
                         by adding 64.  Initially, no characters have this
                         property.

                  4      Enable breaks after the character.  A line is not
                         broken at a character with this property unless the
                         characters on each side both have non-zero
                         hyphenation codes.  This exception can be overridden
                         by adding 64.  Initially, characters “-\[hy]\[em]”
                         have this property.

                  8      Mark the glyph associated with this character as
                         overlapping other instances of itself horizontally.
                         Initially, characters
                         “\[ul]\[rn]\[ru]\[radicalex]\[sqrtex]” have this
                         property.

                  16     Mark the glyph associated with this character as
                         overlapping other instances of itself vertically.
                         Initially, the character “\[br]” has this property.

                  32     Mark the character as transparent for the purpose of
                         end-of-sentence recognition.  In other words, an
                         end-of-sentence character followed by any number of
                         characters with this property is treated as the end
                         of a sentence if followed by a newline or two
                         spaces.  This is the same as having a zero space
                         factor in TeX.  Initially, characters
                         “'")]*\[dg]\[dd]\[rq]\[cq]” have this property.

                  64     Ignore hyphenation codes of the surrounding
                         characters.  Use this value in combination with
                         values 2 and 4.  Initially, no characters have this
                         property.

                  The remaining values were implemented for East Asian
                  language support; those who use alphabetic scripts
                  exclusively can disregard them.

                  128    Prohibit a break before the character, but allow a
                         break after the character.  This works only in
                         combination with values 256 and 512 and has no
                         effect otherwise.  Initially, no characters have
                         this property.

                  256    Prohibit a break after the character, but allow a
                         break before the character.  This works only in
                         combination with values 128 and 512 and has no
                         effect otherwise.  Initially, no characters have
                         this property.

                  512    Allow a break before or after the character.  This
                         works only in combination with values 128 and 256
                         and has no effect otherwise.  Initially, no
                         characters have this property.

                  In contrast to values 2 and 4, the values 128, 256, and 512
                  work pairwise.  If, for example, the left character has
                  value 512, and the right character 128, no break will be
                  automatically inserted between them.  If we use value 6
                  instead for the left character, a break after the character
                  can't be suppressed since the neighboring character on the
                  right doesn't get examined.

           .char c [["]contents]
                  Define an ordinary, special, or indexed character c as
                  contents.  Omitting contents gives c an empty definition.

                  Defining (or redefining) a character c creates a formatter
                  object that GNU troff recognizes like any other ordinary,
                  special, or indexed character on input, and produces
                  contents on output.  When formatting c, GNU troff processes
                  contents in a temporary environment and encapsulates the
                  result in a node (see section “GNU troff Internals” in
                  Groff: The GNU Implementation of troff, the groff Texinfo
                  manual); disabling compatibility mode and setting the
                  escape character to to \ while interpreting contents.  Any
                  emboldening, constant spacing, or track kerning applies to
                  this object rather than to individual glyphs resulting from
                  the formatting of contents.

                  A character defined by char can be used just like a glyph
                  provided by the output device.  In particular, other
                  characters can be translated to it with the tr request; it
                  can be made the tab or leader fill character with the tc
                  and lc requests; sequences of it can be drawn with the \l
                  and \L escape sequences; and, if the hcode request is used
                  on c, it is subject to automatic hyphenation.

                  However, a user-defined character c does not participate at
                  its boundaries in kerning adjustments or italic
                  corrections.

                  The formatter prevents infinite recursion by treating an
                  occurrence of a character in its own definition as if it
                  were undefined; when interpolating such a character, GNU
                  troff emits a warning in category “char”.  (Mutually
                  recursive character definitions are handled similarly.)

                  The tr and trin requests take precedence if char also
                  applies to c.  The rchar request removes character
                  definitions.

           .chop name
                  Remove the last character from the macro, string, or
                  diversion name.  This is useful for removing the newline
                  from the end of a diversion that is to be interpolated as a
                  string.  This request can be used repeatedly on the same
                  name; see section “GNU troff Internals” in Groff: The GNU
                  Implementation of troff, the groff Texinfo manual, for
                  discussion of nodes inserted by groff.

           .class ident c ...
                  Define a character class (or simply “class”) ident
                  comprising the members c..., where each c is an ordinary,
                  special, or indexed character; or a range expression.  A
                  class thus defined can then be referred to in a cflags
                  request in lieu of listing all the characters within it.

                  Since class and special character names share the same name
                  space, we recommend starting and ending the class name with
                  “[” and “]”, respectively, to avoid collisions with
                  existing special character names defined by GNU troff or
                  the user (with char and related requests).  This practice
                  applies the presence of “]” in the class name to prevent
                  the usage of the special character escape form “\[...]”,
                  you must therefore access a class thus named via the \C
                  escape sequence.

                  An argument c can alternatively be a range expression
                  consisting of a start character followed by “-” and then an
                  end character.  Internally, GNU troff converts these two
                  character names to Unicode code points (according to the
                  groff glyph list [GGL]), which determine the start and end
                  values of the range.  If that conversion fails, GNU troff
                  skips the range expression and any remaining arguments.

           .close stream
                  Close the named stream, invalidating it as an argument to
                  the “write” request.  See “open”.

           .composite c1 c2
                  Map ordinary or special character c1 to c2 when c1 is a
                  combining component in a composite character.  Typically,
                  composite is used to map a spacing character to a combining
                  one.  See groff_char(7).

           .continue
                  Skip the remainder of a “while” loop's body, immediately
                  retesting its conditional expression.  See “break” above.

           .color [b]
                  Enable or disable output of color-related device-
                  independent output commands per Boolean expression b.  It
                  is enabled by default, and if b is omitted.

           .cp [b]
                  Enable or disable AT&T troff compatibility mode per Boolean
                  expression b.  It is disabled by default, and enabled if b
                  is omitted.  In compatibility mode, long names are not
                  recognized, and the incompatibilities they cause do not
                  arise.

           .defcolor ident scheme color-component ...
                  Define a color named ident.  scheme identifies a color
                  space and determines the number of required color-
                  components; it must be one of “rgb” (three components),
                  “cmy” (three components), “cmyk” (four components), or
                  “gray” (one component).  “grey” is accepted as a synonym of
                  “gray”.  Each color component can be encoded as a
                  hexadecimal value starting with # or ##.  The former
                  indicates that each component is in the range 0–255 (0–FF),
                  the latter the range 0–65535 (0–FFFF).  Alternatively, a
                  component can be specified as a decimal fraction in the
                  range 0–1, interpreted using a default scaling unit of “f”,
                  which multiplies its value by 65,536 (but clamps it at
                  65,535).

                  Each output device has a color named “default”, which
                  cannot be redefined.  A device's default stroke and fill
                  colors are not necessarily the same.

           .de1 ident [end-name]
                  As “de”, but GNU troff disables compatibility mode while
                  interpreting name: it inserts a compatibility save token at
                  the beginning of the macro definition, and a compatibility
                  restore token at its end.  See .am1 above.

           .dei name [end-name]
                  Define macro indirectly, with the name of the macro to be
                  defined in string name and the name of the end macro
                  terminating its definition in string end-name.

           .dei1 name [end-name]
                  As dei, but GNU troff disables compatibility mode while
                  interpreting the macro named by the contents of string
                  name.  See am1 and de1 above.

           .device [["]character-sequence]
                  Embed character-sequence into GNU troff output as
                  parameters to an “xX” device extension command; see
                  groff_out(5).  The output driver or other postprocessor
                  interprets character-sequence as it sees fit.

           .devicem name
                  Write contents of macro or string name to troff output as
                  the argument to a device extension command.

           .do name [argument ...]
                  Interpret the string, request, diversion, or macro name
                  (along with any further arguments) with compatibility mode
                  disabled.  Compatibility mode is restored (only if it was
                  active) when the interpolation of name is interpreted; that
                  is, the restored compatibility state applies to the request
                  or contents of the macro, string, or diversion name, its
                  arguments, and data read from files or pipes if name is the
                  “so”, soquiet, mso, msoquiet, or pso request.

           .ds1 name [["]contents]
                  As ds, but GNU troff disables AT&T compatibility mode while
                  interpreting name: it inserts a “compatibility save” token
                  at the beginning of contents, and a “compatibility restore”
                  token after it.

           .ecr   Restore the escape character saved with ecs, or set escape
                  character to “\” if none has been saved.

           .ecs   Save the current escape character.

           .evc env
                  Copy the properties of environment env to the current
                  environment, except for:

                  •  a partially collected line, if present;

                  •  the interruption status of the previous input line (due
                     to use of the \c escape sequence);

                  •  the count of remaining lines to center, to right-align,
                     or to underline (with or without underlined
                     spaces)—these are set to zero;

                  •  the activation status of temporary indentation;

                  •  input traps and their associated data;

                  •  the activation status of line numbering (which can be
                     reactivated with “.nm +0”); and

                  •  the count of consecutive hyphenated lines (set to zero).

                  Copying an environment to itself discards the foregoing
                  data.

           .fam [fml]
                  Set default font family to fml.  With no argument, the
                  previous font family is selected, and if none, the
                  formatter's default family.  This default is “T” (Times),
                  but can be overridden by the output device—see
                  groff_font(5).  The default font family is associated with
                  the environment.  See \F.

           .fchar c [["]contents]
                  Define fallback character c as contents.  As char, but
                  while that request hides a glyph with the same name in the
                  selected font, fchar definitions are used only if the font
                  lacks a glyph for c.  GNU troff performs this test before
                  searching special fonts.

           .fcolor [col]
                  Select col as the environment's fill color, or, without an
                  argument, restore the previous fill color, or the default
                  if there is none.

           .fschar f c [["]contents]
                  Define fallback special character c for font f as contents.
                  As char, but GNU troff locates a character defined by
                  fschar after any fonts named as arguments to the fspecial
                  are searched and before those named as arguments to the
                  “special” request.

           .fspecial f [s ...]
                  Declare each font s as special only when font f is
                  selected.  Initially, a font f's list of associated special
                  fonts is empty for all f.  GNU troff searches fonts
                  specified as arguments to the “special” request after those
                  given as arguments to the fspecial request.  See “special”.

           .ftr f [g]
                  Translate font f to g.  Whenever a font named f is referred
                  to in an \f escape sequence, in the F and S conditional
                  expression operators, or in the ft, ul, bd, cs, tkf,
                  “special”, fspecial, fp, or sty requests, font g is used.
                  If g is missing or identical to f, then font f is not
                  translated.

           .fzoom f [zoom]
                  Set zoom factor zoom for font f.  zoom must be a non-
                  negative integer; it scales the magnification by
                  thousandths with 1000 as a basis.  If zoom is missing or
                  equal to zero or 1000, font f is not magnified.  f must be
                  a resolved font name, not an abstract style or mounting
                  position.

           .gcolor [col]
                  Select col as the environment's stroke color, or, without
                  an argument, restore the previous stroke color, or the
                  default if there is none.

           .hcode dst1 src1 [dst2 src2] ...
                  Set the hyphenation code of character dst1 to that of src1,
                  and so on.  dst1 must be an ordinary character (other than
                  a numeral) or a special character, and src1 must be an
                  ordinary character (other than a numeral) or a special
                  character to which a hyphenation code has already been
                  applied.  Assigning the code of an ordinary character to
                  itself effectively creates a unique hyphenation code (which
                  can then be copied to others).  hcode ignores spaces
                  between arguments.  If any argument is invalid, hcode
                  reports an error and stops reading them.

           .hla [lang]
                  Set the hyphenation language to lang, or clear it if there
                  is no argument.  Hyphenation exceptions specified with the
                  hw request and hyphenation patterns and exceptions
                  specified with the hpf and hpfa requests are associated
                  with the hyphenation language.  The hla request is usually
                  invoked by a localization file, which is in turn loaded by
                  the troffrc or troffrc-end file; see the hpf request below.

           .hlm [n]
                  Set the consecutive automatically hyphenated line limit to
                  n.  A negative value means “no limit”.  Omitting n implies
                  a limit of -1.  This value is associated with the
                  environment.  Only lines output from a given environment
                  count toward the maximum associated with that environment.
                  Hyphens resulting from \% are counted; explicit hyphens are
                  not.

           .hpf ["]pattern-file
                  Read hyphenation patterns from pattern-file.  This file is
                  sought in the same way that macro files are with the mso
                  request.

                  The pattern-file should have the same format as (simple)
                  TeX pattern files.  The following scanning rules are
                  implemented.

                  •  A percent sign starts a comment (up to the end of the
                     line) even if preceded by a backslash.

                  •  “Digraphs” like \$ are not supported.

                  •  “^^xx” (where each x is 0–9 or a–f) and ^^c (character c
                     in the code point range 0–127 decimal) are recognized;
                     other uses of ^ cause an error.

                  •  No macro expansion is performed.

                  •  hpf checks for the expression \patterns{...} (possibly
                     with whitespace before or after the braces).  Everything
                     between the braces is taken as hyphenation patterns.
                     Consequently, “{” and “}” are not allowed in patterns.

                  •  Similarly, \hyphenation{...} gives a list of hyphenation
                     exceptions.

                  •  \endinput is recognized also.

                  •  For backward compatibility, if \patterns is missing, the
                     whole file is treated as a list of hyphenation patterns
                     (but the “%” character is still recognized as the start
                     of a comment).

                  Use the hcode request (see above) to map the encoding used
                  in hyphenation pattern files to groff's input encoding.

                  GNU troff ties the set of hyphenation patterns to the
                  hyphenation language code selected by the hla request.  The
                  hpf request is usually invoked by a localization file
                  loaded by the troffrc file.  groff provides localization
                  files for several languages; See subsection “Localization
                  packages” of groff_tmac(5).  For Western languages, the
                  localization file sets the default hyphenation mode and
                  loads hyphenation patterns and exceptions.  By default,
                  troffrc loads the localization file for English.

                  A second call to hpf (for the same language) replaces the
                  old patterns with the new ones.

                  Invoking hpf causes an error if there is no hyphenation
                  language.

                  If no hpf request is specified (either in the document, in
                  a file loaded at startup, or in a macro package), GNU troff
                  won't automatically hyphenate at all.

           .hpfa ["]pattern-file
                  As hpf, except that the hyphenation patterns and exceptions
                  from pattern-file are appended to the patterns already
                  applied to the hyphenation language of the environment.

           .hpfcode a b [c d] ...
                  Caution: This request will be withdrawn in a future groff
                  release.  Use hcode instead.

                  Define mapping values for character codes in pattern files.
                  hpf or hpfa apply the mapping after reading or appending to
                  the active list of patterns.  Its arguments are pairs of
                  character codes—integers from 0 to 255.  The request maps
                  character code a to code b, code c to code d, and so on.
                  Character codes that would otherwise be invalid in GNU
                  troff can be used.  By default, every code maps to itself
                  except those for letters “A” to “Z”, which map to those for
                  “a” to “z”.

           .hydefault mode
                  Set hyphenation mode default to mode.  When the hy request
                  is invoked without an argument, this mode is selected.  The
                  hyphenation mode default is associated with the
                  environment.  The formatter's default is 1 for AT&T troff
                  compatibility.  groff locale files generally set a more
                  appropriate one; see groff_tmac(5).

           .hym [length]
                  Set the (right) hyphenation margin to length.  If the
                  adjustment mode is not “b” or “n”, the line is not
                  hyphenated if it is shorter than length.  Without an
                  argument, the default hyphenation margin is reset to its
                  default value, 0.  The default scaling unit is “m”.  The
                  hyphenation margin is associated with the environment.  A
                  negative argument resets the hyphenation margin to zero,
                  emitting a warning in category “range”.

           .hys [hyphenation-space]
                  Suppress hyphenation of the line in adjustment modes “b” or
                  “n”, if that adjustment can be achieved by adding no more
                  than hyphenation-space extra space to each inter-word
                  space.  Without an argument, the hyphenation space
                  adjustment threshold is set to its default value, 0.  The
                  default scaling unit is “m”.  The hyphenation space
                  adjustment threshold is associated with the environment.  A
                  negative argument resets the hyphenation space adjustment
                  threshold to zero, emitting a warning in category “range”.

           .itc n [mac]
                  As “it”, but lines interrupted with the \c escape sequence
                  do not apply to the line count.

           .kern [b]
                  Enable or disable pairwise kerning of glyphs in the
                  environment per Boolean expression b.  It is enabled by
                  default, and if b is omitted.

           .length reg [["]contents]
                  Compute the number of characters in contents and store the
                  count in the register reg.  If reg doesn't exist, GNU troff
                  creates it.

                  Caution: If you interpolate a macro or diversion in
                  contents (see section “Punning Names” in groff(7)), the
                  length request counts characters (or nodes) only up to the
                  first newline, and leaves the rest on the input stream.  In
                  conventional circumstances, that means the remainder is
                  interpreted, and may be formatted.  To discover the length
                  of any string, macro, or diversion, use the pm request.
                  See section “Debugging” below.

           .linetabs [b]
                  Activate or deactivate line-tabs in the environment per
                  Boolean expression b.  They are inactive by default, and
                  activated if b is omitted.  When line-tabs are active, tab
                  stops are computed relative to the start of the pending
                  output line instead of the drawing position corresponding
                  to the start of the input line.

           .lsm [name]
                  Set a leading space trap, calling the macro name when GNU
                  troff encounters leading spaces on a text line; the
                  implicit line break that normally happens in this case is
                  suppressed.  The formatter stores the count of leading
                  spaces on the text line in register lsn, and the amount of
                  corresponding horizontal motion in register lss,
                  irrespective of whether a leading space trap is set.  When
                  it is, GNU troff removes the leading spaces from the input
                  line and produces no motion before calling name.

                  If no argument is supplied, GNU troff reëstablishes the
                  default handling of leading spaces on text lines (breaking
                  the line when filling, and formatting a horizontal motion
                  of \n[lsn] word spaces).

           .mso ["]file
                  As “so”, except that GNU troff searches for the specified
                  file in the same directories as macro files; see
                  GROFF_TMAC_PATH in section “Environment” of groff(1) and -m
                  in section “Options” of the same page.  If file does not
                  exist or is not readable, a warning in category “file” is
                  emitted and the request has no other effect.

           .msoquiet ["]file
                  As mso, but no warning is emitted if file does not exist.

           .nop [input]
                  Interpret input as if it were an input line.  nop resembles
                  “.if 1”; it puts a break on the output if input is empty.
                  Unlike “if”, it cannot govern conditional blocks.  Its
                  application is to maintain consistent indentation within
                  macro definitions even when formatting output.

           .nroff Make the n conditional expression evaluate true and t
                  false.  See troff.

           .open ident ["]file
                  Open file for writing and associate a stream named ident
                  with it, making it available for “write” requests.  Unsafe
                  request; disabled by default.  Also see writec and “close”.

           .opena ident ["]file
                  As “open”, but appends to file if it already exists instead
                  of overwriting it.

           .output ["]character-sequence
                  Emit character-sequence, transparently to GNU troff output;
                  this usage is similar to that of \! when it occurs in the
                  top-level diversion.

           .pchar c ...
                  Report, to the standard error stream, information about
                  each character (be it ordinary, special, or indexed) or
                  character class c.  A character defined by a request (char,
                  fchar, fschar, or schar) reports its contents as a JSON-
                  encoded string, but the output is not otherwise in JSON
                  format.

           .pcolor [col ...]
                  Report, to the standard error stream, each defined color
                  named col, its color space identifier, and channel value
                  assignments, or, without arguments, those of all defined
                  colors.  A device's default stroke and/or fill colors,
                  “default”, are not listed since they are immutable and
                  their details unknown to the formatter.

           .pcomposite
                  Report, to the standard error stream, the list of
                  configured composite character mappings.  See “composite”
                  above.  The “from” code point is listed first, followed by
                  its “to” mapping.

           .pev   Report the state of the current environment followed by
                  that of all other environments to the standard error
                  stream.

           .pfp   Report, to the standard error stream, the list of occupied
                  font mounting positions.  Occupied mounting positions are
                  listed, one per line, in increasing order, followed by the
                  typeface name; if the name corresponds to an abstract
                  style, the entry ends there.  Otherwise, the name of the
                  font description file and the font's “internal name” datum,
                  the meaning of which varies by output device, follow.

           .pftr  Report, to the standard error stream, the list of font
                  translations.  See pftr above.  The “from” font identifier
                  is listed first, followed by its “to” translation.

           .phw   Report, to the standard error stream, the list of
                  hyphenation exception words associated with the hyphenation
                  language selected by the hla request.  A “-” marks each
                  hyphenation point.  A word prefixed with “-” is not
                  hyphenated at all.  The report suffixes words to which
                  automatic hyphenation applies (meaning those defined in a
                  hyphenation pattern file rather than with the hw request)
                  with a tab and asterisk “*”.

           .pline Report, in JSON syntax to the standard error stream, the
                  list of output nodes corresponding to the pending output
                  line.  In JSON, a pair of empty brackets “[ ]” represents
                  an empty list.  A pending output line has not yet undergone
                  adjustment, and lacks a line number and margin character
                  (all as applicable).

           .pnr [reg ...]
                  Report the name and value and, if its type is numeric, the
                  autoincrement amount and assigned format of each register
                  reg, or, without arguments, those of all defined registers,
                  to the standard error stream.

           .psbb file
                  Get the bounding box of a PostScript image file.  This file
                  must conform to Adobe's Document Structuring Conventions;
                  the request attempts to extract the bounding box values
                  from a %%BoundingBox comment.  After invocation, the x and
                  y coordinates (in PostScript units) of the lower left and
                  upper right corners can be found in the registers \n[llx],
                  \n[lly], \n[urx], and \n[ury], respectively.  If an error
                  occurs, these four registers are set to zero.

           .pso ["]command
                  As “so”, except that input comes from the standard output
                  stream of command, which is passed to popen(3).

           .pstream
                  Report, in JSON syntax to the standard error stream, the
                  list of open streams, including the name of each open
                  stream, the name of the file backing it, and its mode
                  (writing or appending).

           .pwh   Report the names and vertical positions, in basic units, of
                  all page location traps to the standard error stream.  GNU
                  troff reports empty slots in the list, where a trap had
                  been planted but subsequently (re)moved, because they can
                  affect the visibility of subsequently planted traps.

           .pvs ±n
                  Set the post-vertical line spacing to n; default scaling
                  unit is “p”.  With no argument, the post-vertical line
                  space is set to its previous value.

                  In GNU troff, the distance between text baselines consists
                  of the extra pre-vertical line spacing set by the most
                  negative \x argument on the pending output line, the
                  vertical spacing (vs), the extra post-vertical line spacing
                  set by the most positive \x argument on the pending output
                  line, and the post-vertical line spacing set by this
                  request.

           .rchar c...
                  Remove definition of each ordinary, special, or indexed
                  character c, undoing the effect of a char, fchar, or schar
                  request.  Spaces need not separate c arguments.  The
                  character definition removed (if any) is the first
                  encountered in the resolution process documented in section
                  “Using Symbols” of Groff: The GNU Implementation of troff.
                  Glyphs, which are defined by font description files, cannot
                  be removed.

           .return [input]
                  Stop interpreting an interpolated macro, skipping to the
                  end of its definition.  Do not confuse “return” with rt.
                  If called with an argument input, GNU troff performs the
                  skip twice—once within the macro being interpreted and once
                  in an enclosing macro, permitting a macro to wrap the
                  request (as trace.tmac does).

           .rfschar f c ...
                  Remove each fallback special character c for font f.
                  Spaces need not separate c arguments.  See fschar.

           .rj [n]
                  Break, right-align the next n (default: 1) input lines,
                  then break again.  rj implies “.ce 0”, and ce implies “.rj
                  0”.  Invoking the request with the no-break control
                  character suppresses the first break.

           .rnn r1 r2
                  Rename register r1 to r2.  If r1 doesn't exist, the request
                  is ignored.

           .schar c [["]contents]
                  Define global fallback character c as contents.  As char,
                  but GNU troff locates a character defined with schar after
                  any fonts named as arguments to the “special” request and
                  before any mounted special fonts.

           .shc [c]
                  Set the soft hyphen character, inserted when a word is
                  hyphenated automatically or at a hyphenation character,
                  to c.  If c is omitted, the soft hyphen character is set to
                  the default, \[hy].  If the selected glyph does not exist
                  in the font in use at a potential hyphenation point, then
                  the line is not broken at that point.  Neither character
                  definitions (char and similar) nor translations (tr and
                  similar) are considered when assigning the soft hyphen
                  character.

           .shift [n]
                  Shift macro or string parameters n places (by 1 if n
                  omitted): argument i becomes argument i-n; arguments 1 to n
                  become unavailable.  Shifting by a non-positive amount, or
                  outside of a macro or string definition, performs no
                  operation.  The register .$ adjusts its value accordingly.

           .sizes s1 s2 ... sn [0]
                  Set the available type sizes to s1, s2, ... sn scaled
                  points.  The list of sizes can be terminated by an
                  optional “0”.  Each si can also be a range m–n.  In
                  contrast to the device description file directive of the
                  same name (see groff_font(5)), the argument list can't
                  extend over more than one line.

           .soquiet ["]file
                  As “so”, but no warning is emitted if file does not exist.

           .special [s ...]
                  Declare each font s as special, irrespective of its
                  description file, populating a list that GNU troff
                  searches, in order, to find the glyph demanded.  GNU troff
                  mounts each font s.  Invoking special without arguments
                  empties the list.  A font is not automatically unmounted if
                  a subsequent special request removes it from the list.
                  Initially, the list is empty.  GNU troff searches fonts
                  specified as arguments to the “special” request after those
                  given as arguments to the fspecial request.

           .spreadwarn [limit]
                  Emit a “break” warning if the additional space inserted for
                  each space between words in an output line adjusted to both
                  margins with “.ad b” is larger than or equal to limit.  A
                  negative value is treated as zero; an absent argument
                  toggles the warning on and off without changing limit.  The
                  default scaling unit is m.  At startup, spreadwarn is
                  inactive and limit is 3 m.

                  For example, “.spreadwarn 0.2m” warns if troff must add
                  0.2 m or more to each inter-word space in a line.

           .stringdown str
           .stringup str
                  Alter the string named str by replacing each of its bytes
                  with its lowercase (down) or uppercase (up) version (if one
                  exists).  Special characters (see groff_char(7)) will often
                  transform in the expected way due to the regular naming
                  convention for accented characters.  When they do not, use
                  substrings and/or catenation.

           .sty pos style
                  Associate abstract style with non-negative font mounting
                  position pos.

           .substring str start [end]
                  Replace the string named str with its substring bounded by
                  the indices start and end, inclusively.  The first
                  character in the string has index 0.  Negative indices
                  count backward from the end of the string: the last
                  character has index -1, the character before the last has
                  index -2, and so on.  If end is omitted, -1 is implied.

           .tkf f s1 n1 s2 n2
                  Enable track kerning for font f.  When the current font
                  is f, the width of every glyph is increased by an amount
                  between n1 and n2; when the current type size is less than
                  or equal to s1, the width is increased by n1; when it is
                  greater than or equal to s2, the width is increased by n2;
                  when the type size is greater than or equal to s1 and less
                  than or equal to s2, the increase in width is a linear
                  function of the type size.

           .tm1 [["]message]
                  As tm, but removes a leading neutral double quote ‘"’ from
                  message, permitting initial embedded spaces in it.

           .tmc [["]message]
                  As tm1, but does not append a newline.

           .trf file
                  Break and copy file as “throughput” to GNU troff output,
                  discarding characters that are invalid as input; contrast
                  with cf.  Each line of file is output as if preceded by \!,
                  but is not interpreted by the formatter.  If file does not
                  end with a newline, trf appends one.  Invoking the request
                  with the no-break control character suppresses the break.

           .trin abcd
                  As the tr request, but the asciify request uses the
                  character code (if any) before the character translation.

           .trnt abcd
                  As the tr request, but the translations do not apply to
                  text that is transparently throughput into a diversion with
                  \!.

           .troff Make the t conditional expression evaluate true and n
                  false.  See nroff.

           .unformat div
                  Unformat the diversion div.  Unlike asciify, “unformat”
                  handles only tabs and spaces between words, the latter
                  usually arising from spaces or newlines in the input.  Tabs
                  are treated as input tokens, and spaces become adjustable
                  again.  The vertical sizes of lines are not preserved, but
                  glyph information (font, type size, space width, and so on)
                  is retained.

           .vpt [b]
                  Enable or disable vertical position traps per Boolean
                  expression b.  They are enabled by default, and if b is
                  omitted.  Vertical position traps are those set by the ch,
                  wh, and dt requests.  Vertical position trap enablement is
                  global.

           .warn [n]
                  Select categories of warnings to be reported.  n is the sum
                  of the numeric codes associated with each warning category
                  that is to be enabled; all other categories are disabled.
                  The categories and their associated codes are listed in
                  section “Warnings” of troff(1).  For example, “.warn 0”
                  disables all warnings, and “.warn 1” disables all warnings
                  except those about missing glyphs.  If no argument is
                  given, all warning categories are enabled.

           .warnscale scaling-unit
                  Select scaling unit used in certain warnings (one of u, i,
                  c, p, or P; default: i).  Ignored on nroff-mode output
                  devices, for which these diagnostics report the vertical
                  page location in lines, and the horizontal page location in
                  ens.

           .while cond-expr input
                  Evaluate the conditional expression cond-expr, and
                  repeatedly execute input unless and until cond-expr
                  evaluates false.  input, which is often a conditional
                  block, is referred to as the “while” request's body.

                  GNU troff treats the body of a “while” request similarly to
                  that of a de request (albeit one not read in copy mode),
                  but stores it under an internal name and deletes it when
                  the loop finishes.  The operation of a macro containing a
                  “while” request can slow significantly if its body is
                  large.  Each time GNU troff interpolates the macro, it
                  parses and stores the “while” body again.  An often better
                  solution—and one that is more portable, since AT&T troff
                  lacked the “while” request—is to instead write a recursive
                  macro, which is parsed only once (unless you redefine it).
                  To prevent infinite loops, GNU troff limits the default
                  number of available recursion levels to 1,000 or somewhat
                  less (because things other than macro calls can be on the
                  input stack).  You can disable this protective measure, or
                  alter the limit, by setting the slimit register.  See
                  section “Debugging” below.

                  If a “while” body begins with a conditional block, its
                  closing brace must end an input line.

                  The “break” and “continue” requests alter a “while” loop's
                  flow of control.

           .write stream [["]character-sequence]
                  Write character-sequence, a sequence of ordinary
                  characters, spaces, or tabs read in copy mode, to stream,
                  which must previously have been the subject of an “open”
                  (or opena) request, followed by a newline.  GNU troff
                  flushes the stream after writing to it.

           .writec stream [["]character-sequence]
                  As “write”, but does not append a newline to contents.

           .writem stream name
                  Write the contents of the macro or string name to stream,
                  which must previously have been the subject of an “open”
                  (or opena) request.  GNU troff reads the contents of name
                  in copy mode.

       Altered registers
           GNU troff alters the semantics of two AT&T troff registers and
           imparts semantics to two others that CSTR #54 documented as
           “reserved”.

           \n[.R] Because GNU troff dynamically manages register storage, it
                  repurposes the .R register to interpolate the maximum
                  integer representable in the formatter.  Favor its use over
                  numeric literals with many zeroes or nines to indicate an
                  arbitrary large quantity.

           \n[.s] In GNU troff, the .s register is string-valued; it
                  interpolates the type size in typographical points, which
                  can be represented as a decimal fraction.

           \n[.x] Interpolate major version number of the running troff
                  formatter.  For example, if the version number is 1.23.0,
                  then \n[.x] contains 1.

           \n[.y] Interpolate minor version number of the running troff
                  formatter.  For example, if the version number is 1.23.0,
                  then \n[.y] contains 23.  Also see \n[.Y] below.

       New registers
           GNU troff exposes more formatter state via many new read-only
           registers.  Their names often correspond to the requests that
           affect them.

           \n[.br]
                  Within a macro definition, interpolate 1 if the macro is
                  called with the “normal” control character (“.” by
                  default), and 0 otherwise.  This facility allows requests
                  to be reliably wrapped by a macro.  Interpolating the .br
                  register outside of a macro definition makes no sense.

           \n[.C] Interpolate 1 if AT&T troff compatibility mode is in
                  effect, 0 otherwise.  See cp.

           \n[.cdp]
                  Interpolate depth of last glyph added to the environment.
                  It is positive if the glyph extends below the baseline.

           \n[.ce]
                  Interpolate count of input lines remaining to be centered
                  in the environment.

           \n[.cht]
                  Interpolate height of last glyph added to the environment.
                  It is positive if the glyph extends above the baseline.

           \n[.color]
                  Interpolate 1 if color output is enabled, 0 otherwise.

           \n[.cp]
                  Within a “do” request, interpolate the saved value of
                  compatibility mode (see \n[.C] above).

           \n[.csk]
                  Interpolate skew of last glyph added to the environment.
                  The skew of a glyph is how far to the right of the center
                  of a glyph the center of an accent over that glyph is to be
                  placed.

           \n[.ev]
                  Interpolate name of current environment.  This is a string-
                  valued register.

           \n[.fam]
                  Interpolate name of the environment's default font family.
                  This is a string-valued register.

           \n[.fn]
                  Interpolate resolved name of the font selected in the
                  environment.  This is a string-valued register.

           \n[.fp]
                  Interpolate next free non-zero font mounting position.

           \n[.g] Interpolate 1.  Test with “if” or ie to check whether GNU
                  troff is the formatter.

           \n[.height]
                  Interpolate the rescaled height of the environment's
                  selected font, in scaled points.  It is zero if the font
                  height is not rescaled.  See \H.

           \n[.hla]
                  Interpolate hyphenation language of the environment.  This
                  is a string-valued register.

           \n[.hlc]
                  Interpolate count of immediately preceding consecutive
                  hyphenated lines in the environment.

           \n[.hlm]
                  Interpolate maximum number of consecutive hyphenated lines
                  allowed in the environment.

           \n[.hy]
                  Interpolate automatic hyphenation mode of the environment.

           \n[.hydefault]
                  Interpolate hyphenation mode default of the environment.

           \n[.hym]
                  Inteprolate hyphenation margin of the environment.

           \n[.hys]
                  Interpolate hyphenation space adjustment threshold of the
                  environment.

           \n[.in]
                  Interpolate indentation amount applicable to the output
                  line pending in the environment.

           \n[.int]
                  Interpolate 1 if the text most recently formatted in the
                  environment was “interrupted” or continued with \c,
                  0 otherwise.

           \n[.it]
                  Interpolate count of input lines remaining in the
                  environment's pending input trap.

           \n[.itc]
                  Interpolate 1 if the environment's pending input trap
                  honors the output line continuation escape sequence (\c),
                  0 otherwise.

           \n[.itm]
                  Interpolate the name of the macro associated with the
                  environment's pending input trap.  This is a string-valued
                  register.

           \n[.kern]
                  Interpolate 1 if pairwise kerning is enabled, 0 otherwise.

           \n[.lg]
                  Interpolate ligature mode.

           \n[.linetabs]
                  Interpolate 1 if line-tabs mode is enabled in the
                  environment, 0 otherwise.

           \n[.ll]
                  Interpolate line length applicable to the environment's
                  pending output line.

           \n[.lt]
                  Interpolate the environment's title line length.

           \n[.m] Interpolate name of the environment's selected stroke
                  color.  This is a string-valued register.

           \n[.M] Interpolate name of the environment's selected fill color.
                  This is a string-valued register.

           \n[.ne]
                  Interpolate amount of space demanded by the most recent ne
                  request that sprang a page location trap.  See \n[.trunc].

           \n[.nm]
                  Interpolate 1 if output line numbering is enabled in the
                  environment (even if temporarily suppressed), 0 otherwise.

           \n[.nn]
                  Interpolate count of lines remaining in the environment for
                  which numbering is suppressed while output line numbering
                  is enabled.

           \n[.ns]
                  Interpolate 1 if no-space mode is enabled, 0 otherwise.

           \n[.O] Interpolate output suppression level.  See \O.

           \n[.P] Interpolate 1 if the current page is selected for output,
                  0 otherwise.  See -o command-line option to troff(1).

           \n[.pe]
                  Interpolate 1 during page ejection, 0 otherwise.

           \n[.pn]
                  Interpolate next page number (either that set by pn, or
                  that of the current page plus 1).

           \n[.ps]
                  Interpolate the environment's type size in scaled points.

           \n[.psr]
                  Interpolate the environment's most recently requested type
                  size in scaled points.

           \n[.pvs]
                  Interpolate the environment's post-vertical line spacing
                  amount.

           \n[.rj]
                  Interpolate count of input lines remaining to be right-
                  aligned in the environment.

           \n[.slant]
                  Interpolate slant in degrees of the environment's selected
                  font.  See \S.

           \n[.sr]
                  Interpolate the environment's most recently requested type
                  size in typographical points.  This is a string-valued
                  register.

           \n[.ss]
           \n[.sss]
                  Interpolate values of the environment's minimum inter-word
                  space and supplemental inter-sentence space, respectively,
                  in twelfths of the space width of the selected font.

           \n[.sty]
                  Interpolate the environment's selected abstract font style,
                  if any.  This is a string-valued register.

           \n[.tabs]
                  Interpolate the environment's tab stop settings (if any) in
                  a form suitable for passage to the ta request.  This is a
                  string-valued register.

           \n[.trap]
                  Interpolate the name of the next vertical position trap
                  after the vertical drawing position.  This is a string-
                  valued register.

           \n[.trunc]
                  Interpolate amount of vertical space truncated by the most
                  recently sprung page location trap, or, if the trap was
                  sprung by an ne request, minus the amount of vertical
                  motion produced by the ne request.  In other words, at the
                  point a trap is sprung, \n[.trunc] represents the
                  difference of what the vertical position would have been
                  but for the trap, and what the vertical position actually
                  is.  See \n[.ne].

           \n[.U] Interpolate 1 if in unsafe mode, 0 otherwise.  See -U
                  command-line option to troff(1).

           \n[.vpt]
                  Interpolate 1 if vertical position traps are enabled,
                  0 otherwise.

           \n[.warn]
                  Interpolate warning mask.  See section “Warnings” of
                  troff(1).

           \n[.Y] Interpolate revision number of the running troff formatter.
                  For example, if the version number is 1.23.0, then \n[.Y]
                  contains 0.  Also see \n[.x] and \n[.y] above.

           \n[.zoom]
                  Interpolate magnification of the environment's selected
                  font, in thousandths, or 0 if magnification unused.  See
                  fzoom.

           The following (writable) registers are set by the psbb request.

           \n[llx]
           \n[lly]
           \n[urx]
           \n[ury]
                  Interpolate the (upper, lower, left, right) bounding box
                  values (in PostScript units) of the most recently processed
                  PostScript image.

           The following (writable) registers are set by the \w escape
           sequence.

           \n[rst]
           \n[rsb]
                  Like \n[st] and \n[sb], but taking account of the heights
                  and depths of glyphs.  In other words, these registers
                  store the highest and lowest vertical positions attained by
                  the argument formatted by the \w escape sequence, doing
                  what AT&T troff documented \n[st] and \n[sb] as doing.

           \n[ssc]
                  The amount of (possibly negative) horizontal space to add
                  to the last glyph before a subscript.

           \n[skw]
                  How far to right of the center of the last glyph in the \w
                  argument, to place the center of an accent from a roman
                  font over that glyph.

           Other writable registers are as follows.  Those relating to date
           and time are initialized using localtime(3) at formatter startup.

           \n[c.] Interpolate input line number.  \n[.c] is a read-only alias
                  of this register.

           \n[hours]
                  Interpolate number of hours elapsed since midnight.

           \n[hp] Interpolate horizontal position relative to that at the
                  start of the input line.

           \n[lsn]
           \n[lss]
                  Interpolate count of leading spaces on input line and
                  amount of corresponding horizontal motion, respectively.

           \n[minutes]
                  Interpolate number of minutes elapsed in the hour.

           \n[seconds]
                  Interpolate number of seconds elapsed in the minute.

           \n[systat]
                  Interpolate return value of system(3) function executed by
                  most recent sy request.

           \n[slimit]
                  Interpolates maximum quantity of objects on troff's
                  internal input stack (default: 1000).  If non-positive,
                  there is no limit: recursion can continue until program
                  memory is exhausted.

           \n[year]
                  Interpolate Gregorian year.  AT&T troff's \n[yr]
                  interpolates the Gregorian year minus 1900.

       Delimiters
           AT&T troff recognized slightly varying sets of delimiters when
           expecting numerical expressions (as with the \h escape sequence),
           string expressions (as with the \w escape sequence and tl
           request), and output comparisons (as in “.if #foo#bar# .tm
           match”).  GNU troff, when not in compatibility mode, recognizes a
           single consistent set of delimiters.  Compatibility mode emulates
           AT&T troff only up to a point.  GNU troff accepts leaders and tabs
           as delimiters, as well as Control+D (EOT or EOF), Control+H (BS or
           backspace), and Control+L (FF or form feed), all of which, when
           used as delimiters, cause AT&T troff to behave in ways difficult
           to predict.

       Miscellaneous
           A font not listed in the output device's DESC file's fonts
           directive is automatically mounted at the next available font
           position when it is selected.  If you mount a font explicitly with
           the fp request, you should do so on the first unused position,
           which can be found in the .fp register.

           Unparameterized string interpolation does not conceal the
           arguments to a macro being interpreted.  Thus, in a macro
           definition, the call of another macro with the existing argument
           list,
                  .xx \\$@
           is more efficiently done with
                  \\*[xx]\\
           (that is, with string interpolation).  The trailing backslashes
           prevent the final newline in the macro definition from being
           interpolated, potentially putting an unwanted blank line on the
           output.  See section “Punning Names” in groff(7).

           If a font description file contains pairwise kerning information,
           glyphs from that font are kerned.  Kerning between two glyphs can
           be inhibited by placing a dummy character \& between them.

           GNU troff keeps track of the nesting depth of escape sequence
           interpolations and other uses of delimiters, as in the tl request
           and the output comparison operator (that is, input like 'foo'bar'
           as a conditional expression), so the only characters you need to
           avoid using as delimiters are those that appear in the arguments
           you input, not any that result from interpolation.  Typically, '
           works fine.  Use visible characters as delimiters in GNU troff,
           not US-ASCII controls like BEL (Control+G).  The implementation of
           \$@ ensures that the double quotes surrounding an argument appear
           at an interpolation depth different from that of the arguments
           themselves.  Similarly, in bracket-form escape sequences like
           \f[ZCMI], a right bracket ] does not end the sequence unless it
           occurs at the same interpolation depth as the opening [.  In
           compatibility mode, no attention is paid to the interpolation
           depth.

           In GNU troff, the tr request can map characters to the unbreakable
           space escape sequence \~ as a special case (tr normally operates
           only on characters).  This feature replaces the odd-parity tr
           mapping trick used in AT&T troff documents, where a character,
           often ~, was “sacrificed” by mapping it to “nothing”, drafting it
           into use as an unadjustable, unbreakable space.  (This feature was
           gratuitous even in early AT&T troff, which supported the \space
           escape sequence by 1976.)  Often, it makes more sense to use GNU
           troff's \~ escape sequence instead, which has been adopted by
           every other active troff implementation except that of Illumos, as
           well as by the non-troff mandoc.  Translation of a character to \~
           is generally unnecessary, but might be employed to obtain an
           unbreakable space when the escape character will subsequently be
           disabled.

           GNU troff permits tabs and spaces after the first dot on a control
           line that ends a macro definition.

## [](#Formatter_output)Formatter output

           The page description language output by GNU troff is modeled after
           that used by AT&T troff once the latter adopted a device-
           independent approach in the early 1980s.  Only the differences are
           documented here.  For a fuller discussion, see groff_out(5).

           Glyph and font names can be of arbitrary length; postprocessors
           should not assume that they are at most two characters.  A glyph
           to be formatted is always drawn from the current font; in contrast
           to AT&T device-independent troff, drivers need not search special
           fonts to find a glyph.

       Units
           The argument to the s command is in scaled points (units of
           points/n, where n is the argument to the sizescale command in the
           DESC file).  The argument to the “x H” command is also in scaled
           points.

       Simple commands
           If the tcommand directive is present in the output device's DESC
           file, GNU troff employs the following two commands.

           t xyz...
                  Typeset word xyz; that is, set a sequence of ordinary
                  glyphs named x, y, z, ..., terminated by a space or
                  newline; an optional second integer argument is ignored
                  (this allows the formatter to generate an even number of
                  arguments).  Each glyph is set at the current drawing
                  position, and the position is then advanced horizontally by
                  the glyph's width.  A glyph's width is read from its
                  metrics in the font description file, scaled to the current
                  type size, and rounded to a multiple of the horizontal
                  motion quantum.  Use the C command to emplace glyphs of
                  special characters.

           u n xyz...
                  Typeset word xyz with track kerning.  As t, but after
                  placing each glyph, the drawing position is further
                  advanced horizontally by n basic units.

           New commands implement color support.

           mc cyan magenta yellow
           md
           mg gray
           mk cyan magenta yellow black
           mr red green blue
                  Set the components of the stroke color with respect to
                  various color spaces.  md resets the stroke color to the
                  default value.  The arguments are integers in the range 0
                  to 65535.

           A new device control subcommand is available.

           x u n  If n is 1, start underlining of spaces.  If n is 0, stop
                  underlining of spaces.  This facility is needed for the cu
                  request in nroff mode and is ignored otherwise.

       Extended drawing commands
           GNU pic does not produce troff escape sequences employing these
           extensions if its -n option is given.

           Df n   Set the shade of gray used to fill geometric objects to n,
                  which must be an integer.  0 corresponds to white and 1000
                  to black.  A grayscale ramp spans the two.  A value outside
                  this range uses the stroke color as the fill color.  The
                  fill color is opaque.  Normally the default is black, but
                  some drivers may provide a way of changing this.  Df is
                  obsolete since 2002, superseded by DFg below.

                  The corresponding \D'f' escape sequence should not be used:
                  its argument is rounded to an integer multiple of the
                  horizontal motion quantum, which can limit the precision
                  of n.

           DC d   Draw a filled circle of diameter d with its leftmost point
                  at the drawing position.

           DE h v Draw a filled ellipse, of horizontal axis h and vertical
                  axis v, with its leftmost point at the drawing position.

           Dp dx1dy1...dxndyn
                  Draw a polygon with, for i=1,...,n+1, its ith vertex at the
                  drawing position +ij−=Σ11(dxj,dyj).  groff output drivers
                  automatically close polygons, drawing a line from (dxn,dyn)
                  back to (dx1,dy1).  The drawing position is left at the
                  last specified vertex, but this may change in a future
                  version of GNU troff.  Heirloom Doctools troff, like DWB
                  troff, by default does not close the polygon.  In its groff
                  compatibility mode, Heirloom closes the polygon but leaves
                  the drawing position unchanged—that is, at the polygon's
                  initial drawing position.

           DP dx1dy1...dxndyn
                  As Dp, but draw a filled rather than a stroked polygon.

           Dt n   Set the line thickness to n basic units.  AT&T troff output
                  drivers use a thickness proportional to the type size; this
                  is the GNU troff default.  A negative n requests this
                  explicitly.  An n of zero selects the smallest available
                  line thickness.

           A difficulty arises in how the drawing position should be changed
           after the execution of these commands.  This has little importance
           to most users, since the output of GNU grn and pic does not depend
           on it.  Given a drawing command of the form Dz x1y1...xnyn, where
           z is not c or e, AT&T troff treats each xi as a horizontal motion,
           each yi as a vertical one, and therefore assumes that the width of
           the drawn object is in=Σ1xi, and its height is in=Σ1yi.  (Verify its
           assumption about height by examining the st and sb registers after
           using such a drawing command in a \w escape sequence).  Thus after
           executing a D command of the form Dz x1y1...xnyn, the drawing
           position increases by (in=Σ1xi,in=Σ1yi).  For the sake of
           compatibility, GNU troff follows this rule, even though it
           frustrates extensions to the D command that set drawing parameters
           rather than rendering objects, producing ugly results in the case
           of Dt and Df, or otherwise don't parameterize objects as a series
           of vertices, as with GNU troff's filled ellipse, DE.  In a future
           release, GNU troff and its output drivers may abandon the
           application of this assumption to drawing commands not explicitly
           specified in the AT&T “Troff User's Manual”.  You can ensure
           predictable output by enclosing drawing commands in the zero-
           motion escape sequence \Z.

           GNU troff implements fill color selection with another set of
           extensions.

           DFc cyan magenta yellow
           DFd
           DFg gray
           DFk cyan magenta yellow black
           DFr red green blue
                  Set the components of the fill color as described under the
                  \M escape sequence above.  DFd restores the device's
                  default fill color.  The drawing position is not updated,
                  in contrast to Df.

       Device control syntax extension
           GNU troff introduces a line continuation convention, permitting
           the argument to the x X command to contain newlines.  A newline in
           the input is transformed to the sequence “newline+”.  When
           interpreting an x X command, a postprocessor should therefore be
           prepared for a plus sign after a newline; if it occurs, preserve
           the newline, discard the plus sign, and continue to collect the
           input into the argument of the x X command.  A newline not
           followed by a plus sign terminates the x X command.  An
           application of this feature is the embedding of PostScript or PDF
           language command streams into troff output.

           GNU troff guarantees that the first three output commands it emits
           are as follows.

                  x T device
                  x res n h v
                  x init

## [](#Debugging)Debugging

           In addition to AT&T troff's debugging features, GNU troff emits
           more error diagnostics when syntactical or semantic nonsense is
           encountered and supports several warning categories; the output of
           these can be selected with “warn”.  Also see the -E, -w, and -W
           options of troff(1).

           A trace of the formatter's input processing stack can be emitted
           when errors or warnings occur by means of GNU troff -b option, or
           produced on demand with the backtrace request.

           groff also adds more flexible diagnostic output requests (tmc and
           tm1).  Examine the state of the formatter with requests that write
           lists of defined colors (pcolor), composite character mappings
           (pcomposite), environments (pev), font translations (pftr),
           automatic hyphenation codes (pchar) and exceptions (phw),
           registers (pnr), open streams (pstream), and page location traps
           (pwh).  Requests can also disclose to the standard error stream
           the internal properties and representations of characters and
           classes (pchar), macros (and strings and diversions) (pm), and the
           list of output nodes corresponding to the pending input line
           (pline).

## [](#Compatibility_mode)Compatibility mode

           Some syntactical and behavioral differences between AT&T and GNU
           troffs are thought too important to neglect; GNU troff therefore
           makes available a compatibility mode in an effort to keep
           documents prepared for AT&T troff rendering well.

           Identifiers of arbitrary length may be GNU troff's most obvious
           innovation.  AT&T troff interprets “.dsabcd” as defining a string
           “ab” with contents “cd”.  Normally, GNU troff interprets this
           input as calling a macro named “dsabcd”.  AT&T troff also
           interprets \*[ and \n[ as interpolating a string or register,
           respectively, named “[”.  GNU troff, however, normally interprets
           “[” as bracketing a long name (with “]” at the distal end).  In
           compatibility mode, GNU troff interprets names in the traditional
           way, they thus can be two characters long at most.  See the -C
           option in troff(1) and, above, the .C and .cp registers, and cp
           and “do” requests, for more on compatibility mode.

           The register \n[.cp] is specialized and may require a statement of
           rationale.  When writing macro packages or documents that use GNU
           troff features and which may be mixed with other packages or
           documents that do not—common scenarios include serial processing
           of man pages or use of the “so” or mso requests—you may desire
           correct operation regardless of compatibility mode enablement in
           the surrounding context.  It may occur to you to save the existing
           value of \n(.C into a register, say, _C, at the beginning of your
           file, turn compatibility mode off with “.cp 0”, then restore it
           from that register at the end with “.cp \n(_C”.  At the same time,
           a modular design of a document or macro package may lead you to
           multiple layers of inclusion.  You cannot use the same register
           name everywhere lest you “clobber” the value from a preceding or
           enclosing context.  The two-character register name space of AT&T
           troff is confining, but employing GNU troff's more capacious one,
           as with “.nr _my_saved_C \n(.C” does not work in compatibility
           mode; the register name is too long.  Employing the “do” request
           is no help: “.do nr _my_saved_C \n(.C” always saves zero to the
           register, because “do” turns compatibility mode off while it
           interprets its argument list.

           GNU troff normally tracks the interpolation depth of escape
           sequence parameters and other delimited structures, but not in
           compatibility mode.  See section “Miscellaneous” above.

           The escape sequences \f, \H, \m, \M, \R, \s, and \S are
           transparent to control character recognition at the beginning of
           an input line, or after the conditional expression of an “if” or
           ie request, only in compatibility mode.  That is, upon
           interpreting them, GNU troff normally no longer recognizes a
           control character on the input line; but in compatibility mode, it
           does, just like AT&T troff.

           Normally, the syntax form \sn accepts only a single character (a
           digit) for n, consistently with other forms that originated in
           AT&T troff, like \*, \$, \f, \g, \k, \n, and \z.  In compatibility
           mode only, a non-zero n must be in the range 4–39.  Legacy
           documents relying upon this quirk of parsing should migrate to
           another \s form.  [Background: The Graphic Systems C/A/T
           phototypesetter (the original device target for AT&T troff)
           supported only a few discrete type sizes in the range 6–36 points,
           so Ossanna contrived a special case in the parser to do what the
           user must have meant.  Kernighan warned of this in the 1992
           revision of CSTR #54 (§2.3), and more recently, McIlroy referred
           to it as a “living fossil”.]

## [](#Other_differences)Other differences

           GNU troff does not emit output if it has nothing to format.  For
           example, it treats an input document consisting solely of nr and
           tm requests as empty, and produces nothing on its standard output
           stream.  AT&T troff does, creating a blank page.

           Use of C0 control characters in identifiers is not portable;
           Solaris, Plan 9, and Heirloom Doctools troffs accept Control+B,
           Control+C, Control+E, Control+F, and Control+G (only); DWB 3.3
           troff does not.  GNU troff rejects C0 controls in identifiers with
           an error diagnostic.

           Formatters that don't implement GNU troff extension request names
           tend to ignore them, and if they don't support a GNU troff
           extension escape sequence, they are liable to format its function
           selector character as text.  For example, the adjustable, non-
           breaking space escape sequence \~ is also supported by Heirloom
           Doctools troff 050915 (September 2005), mandoc 1.9.5 (2009-09-21),
           neatroff (commit 1c6ab0f6e, 2016-09-13), and Plan 9 from User
           Space troff (commit 93f8143600, 2022-08-12), but not by Solaris or
           Documenter's Workbench troffs, which both render it as “~”.  The
           \A escape sequence (see subsection “Escape sequences” above) may
           be helpful in avoiding their use.

           AT&T troff discards trailing spaces from input lines, like GNU
           troff, but when it does so, AT&T troff also cancels end-of-
           sentence detection.  Use of the dummy character escape sequence \&
           is more portable.

           When adjusting output lines to both margins, AT&T troff at first
           adjusts spaces starting from the right; GNU troff begins from the
           left.  Both implementations adjust spaces from opposite ends on
           alternating output lines in this adjustment mode to prevent
           “rivers” in the text.

           GNU troff does not always hyphenate words as AT&T troff does.  The
           AT&T implementation uses a set of hard-coded rules specific to
           U.S. English, while GNU troff uses language-specific hyphenation
           pattern files derived from TeX.  Some versions of troff reserved
           meager storage for hyphenation exception words (arguments to the
           hw request); GNU troff has no such restriction.  When the hy
           request is invoked without an argument, GNU troff sets the
           automatic hyphenation mode to the value of the .hydefault
           register; the AT&T implementation sets it to “1”, which is not
           suitable in GNU troff for some languages, including English.

           Unlike GNU troff, AT&T troff does not recognize an occurrence of
           \% at the beginning of a word as suppressing its hyphenation;
           instead, it (uselessly) marks the start of the word as a potential
           hyphenation point, permitting output lines to end with hyphens
           that are not interior to a word.

           GNU troff handles the dummy character \& differently from AT&T
           troff when it is followed by the hyphenation control escape
           sequence \% at the beginning of a word.  GNU troff does not regard
           the dummy character as “starting” the word; AT&T troff does.
           Further, Heirloom Doctools troff does not honor an explicit
           hyphenation point marked with \% after a word-initial one.

           GNU troff interprets request arguments representing file names and
           system commands in the same way it does the contents argument to
           the ds and “as” requests: it removes a leading neutral double
           quote ‘"’ from the argument to the cf, nx, pi, “so”, and sy
           requests, and the second argument (if present) to the lf request,
           permitting initial embedded spaces in it, and reads it to the end
           of the input line in copy mode.  This difference permits the
           formatter to handle files with spaces in their names, but requires
           more care with trailing comments, and doubling of an initial
           neutral double quote “"” if the file name has one.

           The existence of the .T string is a common feature of device-
           independent troffs—DWB 3.3, Solaris, Heirloom Doctools, and Plan 9
           troff all support it—but valid values are specific to each
           implementation.

           The (read-only) register .T interpolates 1 if GNU troff is run
           with the -T option, and 0 otherwise.  In contrast, AT&T troff
           interpolated 1 only if nroff was the formatter and was run with
           -T.

           AT&T troff ignored attempts to remove read-only registers; GNU
           troff honors such requests.

           The lf request sets the number of the current input line in AT&T
           troff, and the next in GNU troff.

           AT&T troff had only environments named “0”, “1”, and “2”.  In GNU
           troff, any number of environments may exist, using any valid
           identifiers for their names.

           As noted above in “Fractional type sizes and new scaling units”,
           AT&T troff's ps request ignores scaling units and thus “.ps 10u”
           sets the type size to 10 points, whereas in GNU troff it sets the
           type size to 10 scaled points, possibly a much smaller
           measurement.  AT&T's behavior also means that “.ps 10p” and
           “.ps 10z” are portable.

           The ab request differs from AT&T troff: GNU troff writes no
           message to the standard error stream if no arguments are given,
           and it exits with a failure status instead of a successful one.

           The bp request differs from AT&T troff: GNU troff does not accept
           a scaling unit on the argument, a page number; the former does
           (uselessly).

           In AT&T troff the pm request reports macro, string, and diversion
           sizes in units of 128-byte blocks, and an argument reduces the
           report to a sum of the above in the same units.  GNU troff reports
           their lengths in characters or nodes if given no arguments, and
           otherwise dumps the JSON-encoded name, contents, and other
           properties of each named argument.

           AT&T troff ignores the ss request if the output is a terminal
           device; GNU troff rounds down the values of minimum inter-word and
           additional inter-sentence space each to the nearest multiple
           of 12.

           GNU troff distinguishes characters from glyphs.  Characters can be
           ordinary, special, or indexed, and populate strings and macros.
           Characters per se have not (yet) been formatted.  Glyphs represent
           graphemes (supplied by the output device) and populate diversions.
           Formatting converts characters into (sequences of) glyphs.  GNU
           troff stores properties of the environment that affect how a glyph
           is rendered with the glyph node's data.  Thus, subsequent
           formatting operations do not affect it, including bd, cs, tkf, tr,
           and fp requests.  Normally, a macro or string contains only a list
           of characters and a diversion contains only a list of nodes.
           However, applying the asciify or unformat requests to a diversion
           converts some of its nodes back into characters.  Where the
           formatter cannot recover the character representation of a node,
           it stores a null character in the character list corresponding to
           a single node in the node list.  Consequently, a glyph node does
           not behave as a character does in macro interpolation: it does not
           inherit special properties that the character from which it was
           constructed might have had.

           One way to format a backslash in most documents is with the \e
           escape sequence; this formats the glyph of the current escape
           character, regardless of whether it is used in a diversion; it
           also works in both GNU troff and AT&T troff.  (Naturally, if
           you've changed the escape character, you need to prefix the “e”
           with whatever it is—and you'll likely get something other than a
           backslash in the output.)

           The other correct way, appropriate in contexts independent of the
           backslash's common use as a roff escape character—perhaps in
           discussion of character sets or other programming languages—is the
           special character escape sequence \(rs or \[rs], for “reverse
           solidus”, from its name in the ECMA-6 and ISO 10646 standards.
           [AT&T troff 's font description files did not define the rs
           special character, but those of its descendant Heirloom Doctools
           troff do, as of its 060716 release (July 2006).]

           To store an escape sequence in a diversion that is interpreted
           when the diversion is interpolated, either use the traditional \!
           transparent output facility, or, if this is unsuitable, the new \?
           escape sequence.  See subsection “Escape sequences” above and
           sections “Diversions” and “GNU troff Internals” in Groff: The GNU
           Implementation of troff, the groff Texinfo manual.

           Like AT&T troff, GNU troff maintains a buffer of device-
           independent output commands, populating the buffer as formatted
           output accumulates.  GNU troff always flushes this buffer when
           processing a break; AT&T troff does so according to no obvious
           schedule (perhaps, if the buffer is of fixed size, the formatter
           performs the flush when the buffer runs out of room).

           In the somewhat pathological case where a diversion exists
           containing a partially collected line and a partially collected
           line at the top-level diversion has never existed, AT&T troff
           outputs a partially collected but otherwise empty line (as if “\c”
           were in the top-level diversion) at the end of input; GNU troff
           does not.

       Formatter output incompatibilities
           Its extensions notwithstanding, GNU troff's page description
           language has some incompatibilities with that of AT&T troff, but
           better compatibility is sought; problem reports and patches are
           welcome.  The following incompatibilities are known.

           •  The drawing position after rendering polygons is inconsistent
              with AT&T troff practice.  Other implementations have diverged
              on this point as well.

           •  The output cannot be easily rescaled to other devices as AT&T
              troff's could.

## [](#Authors)Authors

           This document was written by James Clark ⟨jjc@jclark.com⟩, Werner
           Lemberg ⟨wl@gnu.org⟩, Bernd Warken ⟨groff-bernd.warken-72@web.de⟩,
           and G. Branden Robinson ⟨g.branden.robinson@gmail.com⟩.

## [](#See_also)See also

           Groff: The GNU Implementation of troff, by Trent A. Fisher and
           Werner Lemberg, is the primary groff manual.  You can browse it
           interactively with “info groff”.

           “Troff User's Manual” by Joseph F. Ossanna, 1976 (revised by Brian
           W. Kernighan, 1992), AT&T Bell Laboratories Computing Science
           Technical Report No. 54, widely called simply “CSTR #54”,
           documents the language, device and font description file formats,
           and page description language referred to collectively in groff
           documentation as AT&T troff.

           “A Typesetter-independent TROFF” by Brian W. Kernighan, 1982, AT&T
           Bell Laboratories Computing Science Technical Report No. 97,
           provides additional insights into the device and font description
           file formats and page description language.

           groff(1), groff(7), roff(7)

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

    groff 1.24.1                    2026-03-14                  groff_diff(7)

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
