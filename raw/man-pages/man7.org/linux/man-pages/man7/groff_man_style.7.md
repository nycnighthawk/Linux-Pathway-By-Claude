---
{"title": "groff_man_style(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/groff_man_style.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groff_man_style(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Synopsis](#Synopsis) \| [Description](#Description) \| [Options](#Options) \| [Files](#Files) \| [Notes](#Notes) \| [Authors](#Authors) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    groff_man_style(7)   Miscellaneous Information Manual  groff_man_style(7)

## [](#Name)Name

           groff_man_style - GNU roff man page tutorial and style guide

## [](#Synopsis)Synopsis

           groff -man [option ...] [file ...]

           groff -m man [option ...] [file ...]

## [](#Description)Description

           The GNU implementation of the man macro package is part of the
           groff document formatting system.  It is used to compose manual
           pages (“man pages”) like the one you are reading.  This document
           presents the macros thematically; for those needing only a quick
           reference, the following table lists them alphabetically, with
           references to appropriate subsections below.  Experienced man
           authors may prefer groff_man(7).

           Macro   Meaning                      Subsection
           ───────────────────────────────────────────────────────────────
           .B      Bold                         Font style macros
           .BI     Bold, italic alternating     Font style macros
           .BR     Bold, roman alternating      Font style macros
           .EE     Example end                  Document structure macros
           .EX     Example begin                Document structure macros
           .HP     Begin hanging paragraph      Paragraphing macros
           .I      Italic                       Font style macros
           .IB     Italic, bold alternating     Font style macros
           .IP     Indented paragraph           Paragraphing macros
           .IR     Italic, roman alternating    Font style macros
           .LP     Begin paragraph              Paragraphing macros
           .ME     Mail-to end                  Hyperlink macros
           .MR     Man page cross reference     Hyperlink macros
           .MT     Mail-to start                Hyperlink macros
           .P      Begin paragraph              Paragraphing macros
           .PP     Begin paragraph              Paragraphing macros
           .RB     Roman, bold alternating      Font style macros
           .RE     Relative inset end           Document structure macros
           .RI     Roman, italic alternating    Font style macros
           .RS     Relative inset start         Document structure macros
           .SH     Section heading              Document structure macros
           .SM     Small                        Font style macros
           .SS     Subsection heading           Document structure macros
           .SY     Synopsis start               Synopsis macros
           .TH     Title heading                Document structure macros
           .TP     Tagged paragraph             Paragraphing macros
           .TQ     Supplemental paragraph tag   Paragraphing macros
           .UE     URI end                      Hyperlink macros
           .UR     URI start                    Hyperlink macros
           .YS     Synopsis end                 Synopsis macros

           We discuss other macros (AT, DT, OP, PD, SB, and UC) in subsection
           “Deprecated features” below.

           Throughout Unix documentation, a manual entry is referred to
           simply as a “man page”, regardless of its length, without gendered
           implication, and irrespective of the macro package selected for
           its composition.

           A man page employs the Unix line-ending convention (U+000A only).
           Some basic Latin characters have special meaning to roff; see
           subsection “Portability” below.

       Fundamental concepts
           groff is a programming system for typesetting: we thus often use
           the verb “to set” in the sense “to typeset”.  The formatter
           troff(1) collects words from the input and fills output lines with
           as many as can fit.  Words are separated by spaces and newlines.
           A transition to a new output line is called a break.  Breaks can
           occur at explicit hyphens, at \% or \: escape sequences (see
           subsection “Portability” below), or at predetermined locations in
           a word if automatic hyphenation is enabled (see the -rHY option in
           section “Options” below).  An output line may be supplemented with
           inter-sentence space, then potentially adjusted with more space to
           a consistent length (see the -dAD option).  roff(7) details these
           processes.  The formatter prepares output for terminals or for
           more capable typesetters that can change the type size and font
           family.

           A roff document can contain control lines, which start with a dot
           (.) or neutral apostrophe (').  All other input lines are text
           lines to be formatted.  A macro collects control and/or text lines
           to ease document composition.  man is a macro package.  To call a
           macro, put its name after a dot on a control line.  Some macros
           interpret arguments, words that follow its name.  A newline,
           unless escaped (see subsection “Portability” below), marks the end
           of the macro call.  A control line with no macro name on it is
           called an empty request; it does nothing.

           We describe below several man macros that plant one-line input
           traps: the next input line that directly produces formatted output
           is treated specially.  For man documents that follow the advice in
           section “Portability” below, this means that control lines using
           the empty request and uncommented input lines ending with an
           escaped newline do not spring the trap; anything else does (but
           see the TP macro description).

       Macro reference preliminaries
           A tagged paragraph describes each macro.  We present coupled pairs
           together, as with EX and EE.  Square brackets surround optional
           macro arguments.  If a macro accepts multiple arguments, those
           containing space characters must be double-quoted to be
           interpreted correctly.  If you require an empty macro argument,
           specify it as a pair of neutral double quotes ("").  See section
           “Notes” below for examples of cases where better alternatives to
           empty arguments in macro calls are available.  Most macro
           arguments are formatted as text in the output; exceptions are
           noted.  We identify some macros as extensions to the set
           originally implemented.  They are not supported everywhere; see
           subsection “Use of extensions” below.

       Document structure macros
           Document structure macros organize a man page's content.  All of
           them break the output line.  TH (title heading) identifies the
           document as a man page and configures the page headers and
           footers.  Section headings (SH), one of which is mandatory and
           many of which are conventionally expected, facilitate location of
           material by the reader and aid the man page writer to discuss all
           essential aspects of the topics presented.  Subsection headings
           (SS) are optional and permit sections that grow long to develop in
           a controlled way.  Many technical discussions benefit from
           examples; lengthy ones, especially those reflecting multiple lines
           of input to or output from the system, are usefully bracketed by
           EX and EE.  When none of the foregoing meets a structural demand,
           use RS/RE to inset a region within a (sub)section.

           .TH identifier section [footer-middle [footer-inside [header-
           middle]]]
                  Break the page, reset the page number to 1 (unless the -rC1
                  option is given), and use the arguments to populate the
                  page header and footer.  roff systems refer to these
                  collectively as “titles”.  Together, identifier and the
                  section of the manual to which it belongs can uniquely
                  identify a man document on the system.  This use of
                  “section” has nothing to do with the section headings
                  otherwise discussed in this page; it arises from the
                  organizational scheme of printed and bound Unix manuals.
                  See man(1) or intro(1) for the manual sectioning applicable
                  to your system.  identifier and section are positioned at
                  the left and right in the header; the latter is set after
                  the former, in parentheses and without space.  footer-
                  middle is centered in the footer.  By default, footer-
                  inside is positioned at the bottom left.  Use of the
                  double-sided layout option -rD1 places footer-inside at the
                  bottom left on recto (odd-numbered) pages, and the bottom
                  right on verso (even-numbered) pages.  By default, the
                  outside footer is the page number.  Use of the continuous-
                  rendering option -rcR=1 replaces it with identifier and
                  section, as in the header.  header-middle is centered in
                  the header.  If section is an integer between 1 and 9
                  (inclusive), there is no need to specify header-middle;
                  an.tmac supplies text for it.  If identifier or footer-
                  inside would overrun the space available in the header
                  and/or footer, this package may abbreviate them with
                  ellipses (...).  groff man suppresses headers and footers
                  in HTML output.

                  A valid man document calls TH only once, early in the file,
                  prior to any other macro calls.  By convention, footer-
                  middle is the date of the most recent modification to the
                  source document, in ISO 8601 format (YYYY-MM-DD), and
                  footer-inside is the name and version or release of the
                  project providing it.

           .SH [heading-text]
                  Set heading-text as a section heading.  Given no argument,
                  SH plants a one-line input trap; text on the next line
                  becomes heading-text.  The heading text is set in bold (or
                  the font specified by the string HF), and, on typesetters,
                  slightly larger than the base type size.  If the heading
                  font \*[HF] is bold, use of an italic style in heading-text
                  is mapped to the bold-italic style if available in the font
                  family.  The inset level is reset to 1; see subsection
                  “Horizontal and vertical spacing” below.  Text lines after
                  the call are set as an ordinary paragraph (P).

                  The content of heading-text and ordering of sections
                  follows a set of common practices, as does much of the
                  layout of material within sections.  For example, a section
                  called “Name” or “NAME” must exist, must be the first
                  section after the TH call, and must contain only text of
                  the form
                         topic[, another-topic]... \- summary-description
                  for tools like makewhatis(8) or mandb(8) to index them.

           .SS [subheading-text]
                  Set subheading-text as a subsection heading indented
                  between a section heading and an ordinary paragraph (P).
                  Given no argument, SS plants a one-line input trap; text on
                  the next line becomes subheading-text.  The subheading text
                  is set in bold (or the font specified by the string HF).
                  If the heading font \*[HF] is bold, use of an italic style
                  in subheading-text is mapped to the bold-italic style if
                  available in the font family.  The inset level is reset to
                  1; see subsection “Horizontal and vertical spacing” below.
                  Text lines after the call are set as an ordinary paragraph
                  (P).

           .EX
           .EE    Begin and end example.  After EX, filling is disabled (and,
                  on typesetters, a monospaced font family is selected).
                  Calling EE enables filling (and restores the previous
                  family).

                  Example regions are useful for formatting code, shell
                  sessions, and text file contents.  An example region is not
                  a “literal mode” of any sort: special character escape
                  sequences must still be used to produce correct glyphs for
                  ', -, \, ^, `, and ~ (see subsection “Portability” below).
                  Sentence endings are still detected and supplemental inter-
                  sentence space applied.  If the amount of supplemental
                  inter-sentence spacing is altered, the rendering of, for
                  instance, regular expressions using . or ? followed by
                  multiple spaces can change.  Use the dummy character escape
                  sequence \& before the spaces.

                  Ninth Edition Unix introduced the EX and EE extensions.
                  Documenter's Workbench (DWB), Heirloom Doctools, and Plan 9
                  troffs, and mandoc (since 1.12.2) support them.  Solaris
                  troff does not.

           .RS [inset-amount]
                  Start new relative inset.  man saves any current inset
                  amount and moves right by: inset-amount, if specified; the
                  indentation amount of the preceding IP, TP, or HP macro
                  call if no (sub-)sectioning or ordinary paragraphing macro
                  has intervened; or the amount of the IN register.  RS calls
                  can nest; each increments by 1 the level used by RE.  The
                  level prior to any RS call is 1.

           .RE [inset-level]
                  End a relative inset, reducing it to that of inset-level
                  (or by 1 if not specified) and restoring the corresponding
                  inset amount.

       Paragraphing macros
           These macros break the output line.  An ordinary paragraph (P)
           like this one indents all output lines by the same amount.  A
           hanging paragraph (HP) is a cosmetic variant of P with a hanging
           indent.  Definition lists frequently occur in man pages; these can
           be set as tagged paragraphs, which have one (TP) or more (TQ)
           leading tags followed by a paragraph that has an additional
           indentation.  The indented paragraph (IP) macro can continue the
           indented content of a narrative started with TP, or present an
           itemized or ordered list.  If a paragraphing macro has been called
           since SH or SS, all except TQ follow the break with vertical space
           (in an amount configured by the deprecated PD macro); see
           subsection “Horizontal and vertical spacing” below.  Except for
           TQ, these macros reset the type size, hyphenation, and adjustment
           to (configured) defaults, and the font style to roman.

           .P
           .LP
           .PP    Begin a new paragraph; these macros are synonymous.  Any
                  indentation from use of IP, TP, or HP is cleared.  The
                  inset amount, as affected by RS and RE, is not.

           .HP [indentation]
                  Set a paragraph with a hanging indentation.  Text on output
                  lines after the first is indented by indentation, if
                  specified, and by the amount of the IN register otherwise.

                  Caution: A hanging indentation cannot be expressed
                  naturally in (pure) HTML, a hanging paragraph is not
                  distinguishable from an ordinary one if it formats on only
                  one output line, and non-roff-based man page interpreters
                  may treat HP as an ordinary paragraph anyway.  Thus,
                  information or distinctions you mean to express with
                  indentation may be lost.

           .TP [indentation]
                  Set an indented paragraph with a leading unindented tag.
                  The macro plants a one-line input trap that honors the \c
                  escape sequence; text on the next line becomes the tag, set
                  without indentation.  Text on subsequent lines is indented
                  by indentation, if specified, and by the amount of the IN
                  register otherwise.  If the tag, plus the “tag spacing”
                  stored in the TS register (see section “Options” below) is
                  wider than the indentation, the package breaks the line
                  after the tag.

                  The line containing the tag can include a macro call, for
                  instance to set the tag in bold with B.  TP was used to
                  write the first paragraph of this description of TP, and IP
                  the subsequent one.

           .TQ    Set an additional tag for a paragraph tagged with TP,
                  planting a one-line input trap as with TP.

                  TQ is a GNU extension supported by Heirloom Doctools troff
                  (since Git snapshot 151218) and mandoc (since 1.14.5) but
                  not by DWB, Plan 9, or Solaris troffs.

                  The description of P, LP, and PP above was written using TP
                  and TQ.

           .IP [mark [indentation]]
                  Set an indented paragraph with an optional mark.
                  Arguments, if present, are handled as with TP, except that
                  the mark argument to IP cannot include a macro call, and
                  the tag separation amount stored in the TS register is not
                  enforced.

                  Two convenient uses for IP are

                      (1)  to start a new paragraph with the same indentation
                           as an immediately preceding IP or TP paragraph, if
                           no indentation argument is given; and

                      (2)  to set a paragraph with a short mark that is not
                           semantically important, such as a bullet
                           (•)—obtained with the \[bu] special character
                           escape sequence—or list enumerator, as seen in
                           this very paragraph.

       Synopsis macros
           Use SY and YS to summarize syntax using familiar Unix conventions.
           Heirloom Doctools troff (since Git snapshot 151218) and mandoc
           (since 1.14.5) support these GNU extensions; DWB, Plan 9, and
           Solaris troffs do not.

           .SY keyword [suffix]
                  Begin synopsis.  Adjustment and automatic hyphenation are
                  disabled.  If SY has already been called without a
                  corresponding YS, a break is performed.  keyword and any
                  suffix are set in bold.  When suffix is present, the
                  package sets the next word after it without intervening
                  space.  If a break is required in subsequent text (up to a
                  paragraphing, sectioning, or YS macro call), lines after
                  the first are indented.  Unless the previous synopsis's
                  indentation is reused (see YS below), output lines after
                  the first indent by the width of the pending output line up
                  to the end of keyword plus a space, if keyword is the only
                  argument, and up to the end of suffix otherwise.

           .YS [reuse-indentation]
                  End synopsis, breaking the line and restoring indentation,
                  adjustment, and hyphenation to their previous states.  If
                  an argument is given, the indentation corresponding to the
                  previous SY call is reused by the next SY call instead of
                  being computed.

           Interleave multiple SY/YS blocks with paragraphing macros to
           distinguish differing modes of operation of a complex command like
           tar(1).  Omit the paragraphing macro to indicate synonymous ways
           of invoking a particular mode of operation.  Paragraphing macros
           can similarly manage grouping of function synopses.

           groff's own command-line interface illustrates most specimens of
           synopsis syntax one may encounter.

                  .SY groff
                  .RB [ \-abcCeEgGijklNpRsStUVXzZ ]
                  .RB [ \-d\~\c
                  .IR ctext ]
                  .RB [ \-d\~\c
                  .IB string =\c
                  .IR text ]
                  .RB [ \-D\~\c
                  .IR fallback-encoding ]
                  (and so on similarly)
                  .RI [ file\~ .\|.\|.]
                  .YS
                  .
                  .
                  .P
                  .SY groff
                  .B \-h
                  .YS
                  .
                  .SY groff
                  .B \-\-help
                  .YS
                  .
                  .
                  .P
                  .SY groff
                  .B \-v
                  .RI [ option\~ .\|.\|.\&]
                  .RI [ file\~ .\|.\|.]
                  .YS
                  .
                  .SY groff
                  .B \-\-version
                  .RI [ option\~ .\|.\|.\&]
                  .RI [ file\~ .\|.\|.]
                  .YS

           Given the foregoing input, groff man produces the following
           output.

                  groff [-abcCeEgGijklNpRsStUVXzZ] [-d ctext]
                        [-d string=text] [-D fallback-encoding] [-f font-
                        family] [-F font-directory] [-I inclusion-directory]
                        [-K input-encoding] [-L spooler-argument] [-m macro-
                        package] [-M macro-directory] [-n page-number]
                        [-o page-list] [-P postprocessor-argument]
                        [-r cnumeric-expression] [-r register=numeric-
                        expression] [-T output-device] [-w warning-category]
                        [-W warning-category] [file ...]

                  groff -h

                  groff --help

                  groff -v [option ...] [file ...]

                  groff --version [option ...] [file ...]

           Several features of the above example are of note.

           •  The empty request (.), which does nothing, vertically spaces
              the input file for readability by the document maintainer; see
              subsection “Portability” below regarding blank lines.

           •  Command and option names are presented in bold to cue the user
              that they should be input literally.

           •  Option dashes are specified with the \- escape sequence; this
              is an important practice to make them clearly visible and to
              facilitate copy-and-paste from the rendered man page to a shell
              prompt or text file.

           •  Option arguments and command operands are presented in italics
              (but see subsection “Font style macros” below regarding
              terminals) to cue the user that they must be replaced with
              appropriate input.

           •  Symbols that are neither to be typed literally nor replaced at
              the user's discretion appear in the roman style; brackets
              surround optional arguments, and an ellipsis indicates that the
              previous syntactic element may be repeated arbitrarily.  Where
              whitespace separates optional arguments, a space precedes the
              ellipsis.

           •  The non-breaking adjustable space escape sequence \~ prevents
              the output line from breaking within the option brackets; see
              subsection “Portability” below.

           •  The output line continuation escape sequence \c is used with
              font style alternation macros to allow all three font styles to
              be set without (breakable) space among them; see subsection
              “Portability” below.

           •  The dummy character escape sequence \& follows the ellipsis
              when further text is to follow after space on the output line,
              keeping its last period from being interpreted as the end of a
              sentence because it is followed by characters that are
              transparent to end-of-sentence detection, and/or a newline,
              which would in turn normally cause the formatter to place
              supplemental inter-sentence space after it.  See subsection
              “Portability” below.

           We might synopsize the standard C library function bsearch(3) as
           follows.

                  .P
                  .B void *\c
                  .SY bsearch (
                  .BI const\~void\~* key ,
                  .BI const\~void\~* base ,
                  .BI size_t\~ nmemb ,
                  .BI int\~(* compar )\c
                  .B (const\~void\~*, const\~void\~*));
                  .YS

           groff man produces the following result.

                  void *

                  bsearch const void *key, const void *base, size_t nmemb,
                          int (*compar)(const void *, const void *));

       Hyperlink macros
           Man page cross references like ls(1) are best presented with MR.
           Mark email addresses with MT/ME and other sorts of URI with UR/UE.
           To hyperlink text, terminals and pager programs must support
           ECMA-48 OSC 8 escape sequences (see grotty(1)).  When device
           support is unavailable or disabled with the U register (see
           section “Options” below), groff man renders these URIs between
           angle brackets (⟨ ⟩) after the linked text.

           MT, ME, UR, and UE are GNU extensions supported by Heirloom
           Doctools troff (since Git snapshot 151218) and mandoc (UR/UE since
           1.12.3; MT/ME since 1.14.2) but not by DWB, Plan 9 (original), or
           Solaris troffs.  Plan 9 from User Space's troff implements MR.

           Prepare arguments to MR, MT, and UR for typesetting; they can
           appear in the output.  Use special character escape sequences to
           encode Unicode basic Latin characters where necessary,
           particularly the hyphen-minus.  (See subsection “Portability”
           below.)  URIs can be lengthy; rendering them can result in jarring
           adjustment or variations in line length, or troff warnings when
           one is longer than an output line.  The application of non-
           printing break point escape sequences \: after each slash (or
           series thereof), and before each dot (or series thereof) is
           recommended as a rule of thumb.  The former practice avoids
           forcing a trailing slash in a URI onto a separate output line, and
           the latter helps the reader to avoid mistakenly interpreting a dot
           at the end of a line as a period (or multiple dots as an
           ellipsis).  Thus,
                  .UR http://\:example\:.com/\:fb8afcfbaebc74e\:.cc
           has several potential break points in the URI shown.  Consider
           adding break points before or after at signs in email addresses,
           and question marks, ampersands, and number signs in HTTP(S) URIs.

           .MR topic [manual-section [trailing-text]]
                  (since groff 1.23) Set a man page cross reference as
                  “topic(manual-section)”.  If manual-section is absent, the
                  package omits the surrounding parentheses.  If trailing-
                  text (typically punctuation) is specified, it follows the
                  closing parenthesis without intervening space.  Hyphenation
                  is disabled while the cross reference is set.  topic is set
                  in the font specified by the MF string.  If manual-section
                  is present, the cross reference hyperlinks to a URI of the
                  form “man:topic(manual-section)”.

                         The output driver
                         .MR grops 1
                         produces PostScript from
                         .I troff
                         output.
                         .
                         The Ghostscript program (\c
                         .MR gs 1 )
                         interprets PostScript and PDF.

           .MT address
           .ME [trailing-text]
                  Identify address as an RFC 6068 addr-spec for a “mailto:”
                  URI with the text between the two macro calls as the link
                  text.  An argument to ME is placed after the link text
                  without intervening space.  address may not be visible in
                  the rendered document if hyperlinks are enabled and
                  supported by the output driver.  If they are not, address
                  is set in angle brackets after the link text and before
                  trailing-text.  If hyperlinking is enabled but there is no
                  link text, address is formatted and hyperlinked without
                  angle brackets, except when address appears as a TP
                  paragraph tag.

                  When rendered by groff to a PostScript device,

                         Contact
                         .MT fred\:.foonly@\:fubar\:.net
                         Fred Foonly
                         .ME
                         for more information.

                  formats as “Contact Fred Foonly ⟨fred.foonly@fubar.net⟩ for
                  more information.”.

           .UR uri
           .UE [trailing-text]
                  Identify uri as an RFC 3986 URI hyperlink with the text
                  between the two macro calls as the link text.  An argument
                  to UE is placed after the link text without intervening
                  space.  uri may not be visible in the rendered document if
                  hyperlinks are enabled and supported by the output driver.
                  If they are not, uri is set in angle brackets after the
                  link text and before trailing-text.  If hyperlinking is
                  enabled but there is no link text, uri is formatted and
                  hyperlinked without angle brackets, except when uri appears
                  as a TP paragraph tag.

                  When rendered by groff to a PostScript device,

                         The GNU Project of the Free Software Foundation
                         hosts the
                         .UR https://\:www\:.gnu\:.org/\:software/\:groff/
                         .I groff
                         home page
                         .UE .

                  formats as “The GNU Project of the Free Software Foundation
                  hosts the groff home page
                  ⟨https://www.gnu.org/software/groff/⟩.”.

           If a UR/UE or MT/ME pair occurs in a TP tag and hyperlinking is
           unavailable, groff man sets the link target at the beginning of
           the indented paragraph, not as part of the tag, unless there is no
           link text.

       Font style macros
           The man macro package is limited in its font styling options,
           offering only bold (B), italic (I), and roman.  Italic text may
           instead render underscored on terminals.  SM sets text at a
           smaller type size, which differs visually from regular-sized text
           only on typesetters.  The macros BI, BR, IB, IR, RB, and RI set
           their odd- and even-numbered arguments as text in the alternating
           styles their names indicate, with no space separating them.

           Because font styles are presentational rather than semantic,
           conflicting traditions have arisen regarding which font styles
           should be used to mark file or path names, environment variables,
           and inlined literals.

           The default type size and family for typesetters is 10-point
           Times, except on the X75-12 and X100-12 devices where the type
           size is 12 points.  The default style is roman.

           .B [text]
                  Set text in bold.  Given no argument, B plants a one-line
                  input trap; text on the next line, which can be further
                  formatted with a macro, is set in bold.

                  Use bold for literal portions of syntax synopses, for
                  command-line options in running text, and for literals that
                  are major topics of the subject under discussion; for
                  example, this page uses bold for macro, string, and
                  register names.  In an EX/EE example of interactive I/O
                  (such as a shell session), set only user input in bold.

           .I [text]
                  Set text in an italic or oblique face.  Given no argument,
                  I plants a one-line input trap; text on the next line,
                  which can be further formatted with a macro, is set in an
                  italic or oblique face.

                  Use italics for file and path names, for environment
                  variables, for C data types, for enumeration or
                  preprocessor constants in C, for variant (user-replaceable)
                  portions of syntax synopses, for the first occurrence
                  (only) of a technical concept being introduced, for names
                  of journals and of literary works longer than an article,
                  and anywhere a parameter requiring replacement by the user
                  is encountered.  An exception involves variant text in a
                  context already typeset in italics, such as file or path
                  names with replaceable components; in such cases, follow
                  the convention of mathematical typography: set the file or
                  path name in italics as usual but use roman for the variant
                  part (see IR and RI below), and italics again in running
                  roman text when referring to the variant material.

           .SM [text]
                  Set text one point smaller than the default type size on
                  typesetters.  Given no argument, SM plants a one-line input
                  trap; text on the next line, which can be further formatted
                  with a macro, is set smaller.

                  Note: terminals render text at normal size instead.  Do not
                  rely upon SM to communicate semantic information distinct
                  from using roman style at normal size; it is hidden from
                  readers using such devices.

           Observe what is not prescribed for setting in bold or italics
           above: elements of “synopsis language” such as ellipses and
           brackets around options; proper names and adjectives; titles of
           anything other than major works of literature; identifiers for
           standards documents or technical reports such as CSTR #54,
           RFC 1918, Unicode 16, or POSIX.1-2024; acronyms; and occurrences
           after the first of a technical term.

           Use italics for emphasis rarely, and bold almost never.  Brief
           specimens of literal text, such as article titles, inline
           examples, mentions of individual characters or short strings, and
           (sub)section headings in man pages, are suitable for quotation;
           see the \[lq], \[rq], \[oq], and \[cq] escape sequences in
           subsection “Portability” below.

           Unlike the above font style macros, the font style alternation
           macros below set no input traps; they must be given arguments to
           have effect.  They apply italic corrections as appropriate.  If a
           space is required within an argument, first consider whether the
           same result could be achieved with as much clarity by using
           single-style macros on separate input lines.  When it cannot,
           double-quote an argument containing embedded space characters.
           Setting all three different styles within a word presents
           challenges; it is possible with the \c and/or \f escape sequences.
           See subsection “Portability” below for approaches.

           .BI bold-text italic-text ...
                  Set each argument in bold and italics, alternately.

                         .BI -r\~ register = numeric-expression

           .BR bold-text roman-text ...
                  Set each argument in bold and roman, alternately.

                         Set an ellipsis on the math axis with the GNU extension macro
                         .BR cdots .

           .IB italic-text bold-text ...
                  Set each argument in italics and bold, alternately.

                         In places where
                         .IB n th
                         is allowed,

           .IR italic-text roman-text ...
                  Set each argument in italics and roman, alternately.

                         Use GNU
                         .IR pic 's
                         .B figname
                         command to change the name of the vbox.

           .RB roman-text bold-text ...
                  Set each argument in roman and bold, alternately.

                         .I file
                         is
                         .RB \[lq] \- \[rq],
                         .I groff
                         reads the standard input stream.

           .RI roman-text italic-text ...
                  Set each argument in roman and italics, alternately.

                         .RI ( tpic
                         was a fork of AT&T
                         .I pic
                         by Tim Morgan of the University of California at Irvine

       Horizontal and vertical spacing
           The package sets all text inboard of the left edge of the output
           medium by the amount of the page offset; see register PO in
           section “Options” below.  Headers, footers (both set with TH), and
           section headings (SH) lie at the page offset.  groff man indents
           subsection headings (SS) by the amount in the SN register.

           Ordinary paragraphs not within an RS/RE inset region are inset by
           the amount stored in the BP register; see section “Options” below.
           The IN register configures the default indentation amount used by
           RS (as the inset-amount), IP, TP, and HP; an overriding argument
           is a number plus an optional scaling unit.  If no scaling unit is
           given, the man package assumes “n”; that is, roughly the width of
           a letter “n” in the font current when the macro is called—see
           section “Measurements” in groff(7).  An indentation specified in a
           call to IP, TP, or HP persists until (1) another of these macros
           is called with an indentation argument, or (2) SH, SS, or P or its
           synonyms is called; these clear the indentation entirely.

           The inset amount and indentation are related but distinct
           parameters with the same defaults.  The former is manipulated by
           RS and RE (and by SH and SS, which reset it to the default).
           Indentation is controlled by the paragraphing macros (though,
           again, SH and SS reset it); it is imposed by the TP, IP, and HP
           macros, and cancelled by P and its synonyms.  An extensive example
           follows.

           This ordinary (P) paragraph is not in a relative inset nor does it
           possess an indentation.

                  Now we have created a relative inset with RS and started
                  another ordinary paragraph with P.  We observe that all of
                  its lines are inset and indented the same; contrast with a
                  first-line indentation.

                  tag    This tagged paragraph, set with TP, is still within
                         the RS region, but lines after the first have a
                         supplementary indentation that the tag lacks.

                         A paragraph like this one, set with IP, appears to
                         the reader as also associated with the tag above,
                         because IP re-uses the previous paragraph's
                         indentation unless given an argument to change it.
                         Both the inset amount (RS) and indentation (IP)
                         affect this paragraph.
                         ┌───────────────────────────────────┐
                         │ This table is affected both by    │
                         │ the inset amount and indentation. │
                         └───────────────────────────────────┘

                  •      This indented paragraph is marked with a bullet,
                         contrasting the inset amount and the indentation;
                         only the former affects the mark, but both affect
                         the text of the paragraph.

                  This ordinary (P) paragraph resets the indentation, but the
                  inset amount is unchanged.
                  ┌─────────────────────────────┐
                  │ This table is affected only │
                  │ by the inset amount.        │
                  └─────────────────────────────┘

           Finally, we have ended the relative inset by using RE, which
           (because we used only one RS/RE pair) has restored the inset
           amount to its initial value.  This is an ordinary P paragraph.

           Resist the temptation to mock up tabular or multi-column output
           with tab characters or the indentation arguments to IP, TP, RS, or
           HP; the result may not be comprehensible on an output device you
           fail to check, or which is developed in the future.  Consider the
           table preprocessor tbl(1) instead.

           Several macros insert vertical space: SH, SS, TP, P (and its
           synonyms), IP, and HP.  They then enable no-space mode; see
           groff(7).  The default inter-section and inter-paragraph spacing
           is 1v for terminals and 0.4v for typesetters.  “v” is a unit of
           vertical distance, where 1v is the distance between adjacent text
           baselines.  (The deprecated macro PD can change this vertical
           spacing, but we discourage its use.)  Between EX and EE calls, the
           inter-paragraph spacing is 1v regardless of output device.

       Registers
           Registers are described in section “Options” below.  They can be
           set not only on the command line but in the site man.local file as
           well; see section “Files” below.

       Strings
           The following strings are defined for use in man pages.  groff man
           supports others for configuration of rendering parameters; see
           section “Options” below.

           \*R    interpolates a special character escape sequence for the
                  “registered sign” glyph, \(rg, if available, and “(Reg.)”
                  otherwise.

           \*S    interpolates an escape sequence setting the type size to
                  the document default.

           \*(lq
           \*(rq  interpolate special character escape sequences for left and
                  right double-quotation marks, \(lq and \(rq, respectively.

           \*(Tm  interpolates a special character escape sequence for the
                  “trade mark sign” glyph, \(tm, if available, and “(TM)”
                  otherwise.

           A contemporary man page needs none of the above.  \*S is
           superfluous; type size changes are invisible on terminals, and
           macros that change it restore its original value afterward.
           Better alternatives exist for the rest; simply use the \[rg],
           \[lq], \[rq], and \[tm] special character escape sequences
           directly.  Unless you are aiming for a pathological level of
           portability—perhaps composing a man page for consumption on
           simulators of 1980s Unix systems (or Solaris troff, though even it
           supports “\(rg”)—avoid using the above strings.

       Use of extensions
           To ensure that your man page formats reliably on a wide variety of
           viewers, write it solely with the macros described in this page
           (except for the ones identified as deprecated, which you should
           avoid).  Macros described as extensions might be unsupported by a
           formatter that is important to your audience.  Nevertheless,
           groff's extensions are present because they perform tasks that are
           otherwise difficult or tedious to achieve portably.  If you
           require an extension but expect your man page to be rendered on a
           system that doesn't support it, write a configuration test to
           measure a property of the system, and use m4(1), sed(1), or a
           similar tool to generate a .man file from a .man.in file, defining
           page-local versions of extension macros only where necessary.  You
           can copy extension macro definitions from groff; see an-ext.tmac
           in section “Files” below.

           For example, we might put a line
                  @DEFINE_MR@
           in our man document at the end of the “Name” section, test a
           system for the availability of the groff man MR macro, remove the
           line if the macro is present, and “inline” a definition otherwise,
           as follows.  (This version is slightly simplified and does not
           attempt to disable hyphenation when setting arguments to MR.)
                  have_MR=$(echo .pm | troff -man 2>&1 | grep 'MR[[:space:]]')
                  if [ -n "$have_MR" ]
                  then
                    sed '/@DEFINE_MR@/d' myprog.man.in > myprog.man
                  else
                    sed 's/@DEFINE_MR@/.de MR\
                  .  ie \\\\n(.$=1 .I \\\\$1\
                  .  el .IR \\\\$1 (\\\\$2)\\\\$3\
                  ../' myprog.man.in > myprog.man
                  fi
           (The profusion of backslashes is due to its status as an escape
           character in both roff and sed.)

           If the foregoing method is too much trouble, you could apply the
           radical technique of reading your man page using every formatter
           of interest, confirming satisfactory output from each.  Test
           documentation for syntactic validity and semantic correctness,
           just as you would test code.

       Portability
           GNU troff expects its input to contain Unicode basic Latin code
           points exclusively.  One can maintain it in a more convenient
           encoding, using preconv(1), as with groff(1)'s -k option, to
           generate a basic Latin version that employs special character
           escape sequences to access other glyphs.

           AT&T troff's man package and those of many of its descendants
           format man pages using a line length of 65 ens (character cells)
           on terminals, whereas groff man uses 80 ens (and mandoc(1) 78).
           Readers with low vision may also benefit from the narrower line
           length.  Inspect your documents with “nroff -t -r LL=65n -man” to
           ensure that their output lines don't overrun.

           In roff systems, elemental functions called requests and escape
           sequences control formatting operations.  A request appears on a
           control line.  An escape sequence starts with a backslash (\) and
           can appear almost anywhere.  However, use of roff requests (apart
           from the empty request “.”) risks poor rendering when a page is
           processed by non-roff formatters that attempt to interpret page
           sources.  (Historically, this was commonly attempted for HTML
           conversion.)  Many of these programs don't interpret the full roff
           language (let alone extensions): they may be incapable of handling
           numeric expressions, control structures, or register, string, and
           macro definitions, causing a document's contents to be presented
           incomprehensibly or omitted entirely.  If your document uses
           formatter requests, or escape sequences not shown below, it
           accepts responsibility for restoring formatter state to what the
           man macro package expects.

           Do not put blank (empty) lines in a man page source document.
           They can produce excessive space in the output, or less than is
           attempted; some man(1) programs “squeeze” multiple blank output
           lines into one.

           The wise man author quotes multi-word section and subsection
           headings; the SH and SS macros of man(7) implementations descended
           from Seventh Edition Unix supported six arguments at most.  This
           restriction also applied to the B, I, SM, and font style
           alternation macros.

           Exercise restraint with escape sequences as with requests.  Some
           escape sequences are however required for correct typesetting even
           in man pages and usually do not cause portability problems.
           Several of these render glyphs corresponding to punctuation code
           points in the Unicode basic Latin range (U+0020–U+007F) that are
           handled specially in roff input; the escape sequences below must
           be used to render them correctly and portably when documenting
           material that uses them as literals—namely, any of the set ' - \ ^
           ` ~ (apostrophe, dash or hyphen-minus, backslash, caret, grave
           accent, tilde).

           \"        Comment.  The formatter ignores everything after the
                     double quote to the end of the input line.  Place whole-
                     line comments on a control line immediately after the
                     empty request (“.”).

           \newline  Join the next input line to the current one.  Except for
                     the update of the input line counter (used for
                     diagnostic messages and related purposes), a series of
                     lines ending in backslash-newline appears to groff as a
                     single input line.  Splitting excessively long input
                     lines can ease document maintenance.

           \%        Control hyphenation.  The location of this escape
                     sequence within a word marks a hyphenation point,
                     supplementing groff's automatic hyphenation patterns.
                     At the beginning of a word, it suppresses any
                     hyphenation breaks within except those specified with
                     \%.

           \:        Insert a non-printing break point.  A word can break at
                     such a point, but a hyphen glyph is not written to the
                     output if it does.  The remainder of the word is subject
                     to hyphenation as normal.  You can use \: and \% in
                     combination to control breaking of a file name or URI or
                     to permit hyphenation only after certain explicit
                     hyphens within a word.  See subsection “Hyperlink
                     macros” above for an example.

                     \: is a GNU extension also supported by Heirloom
                     Doctools troff 050915 (September 2005), mandoc 1.13.1
                     (2014-08-10), and neatroff (commit 399a4936,
                     2014-02-17), but not by DWB, Plan 9, or Solaris troffs.

           \~        Adjustable non-breaking space.  Use this escape sequence
                     to prevent a break inside a short phrase or between a
                     numerical quantity and its corresponding unit(s).

                            Before starting the motor,
                            set the output speed to\~1.
                            There are 1,024\~bytes in 1\~KiB.
                            CSTR\~#8 documents the B\~language.

                     \~ is a GNU extension also supported by Heirloom
                     Doctools troff 050915 (September 2005), mandoc 1.9.14
                     (2009-11-16), neatroff (commit 1c6ab0f6e, 2016-09-13),
                     and Plan 9 from User Space troff (commit 93f8143600,
                     2022-08-12), but not by DWB or Solaris troffs.

           \&        Dummy character.  Prefix an input line with it to
                     prevent a dot or apostrophe from being interpreted as
                     beginning a roff control line.  Append \& to an end-of-
                     sentence punctuation sequence to keep it from being
                     recognized as such.

           \|        Thin space (one-sixth em on typesetters, zero-width on
                     terminals); a non-breaking space.  Used primarily in
                     ellipses (“.\|.\|.”) to space the dots more pleasantly
                     on typesetters.

           \c        End a text line without inserting space or attempting a
                     break.  Nothing on the input line after this escape
                     sequence is formatted.  \c is useful when three font
                     styles are needed in a single word, as in a command
                     synopsis.

                            .RB [ \-\-stylesheet=\c
                            .IR name ]

                     \c also helps when changing font styles in EX/EE
                     examples, since they are not filled.

                            .EX
                            $ \c
                            .B groff \-T utf8 \-Z \c
                            .I file \c
                            .B | grotty \-i
                            .EE

                     Normally, if filling is enabled, the formatter treats
                     the end of a text line like a space.  It checks for the
                     end of a sentence, and may break the output line (if
                     not, it inserts an adjustable space).  If filling is
                     disabled, the formatter will break the output line, as
                     in EX/EE examples.  The formatter interprets the next
                     input line as usual, recognizing control lines,
                     including macro calls (contrast with \newline).

                     The \f font selection escape sequence is an alternative
                     to \c; see below.  Using \c to continue a TP paragraph
                     tag across multiple input lines renders incorrectly with
                     groff 1.22.3, mandoc 1.14.1, older versions of these
                     programs, and perhaps with some other formatters.

           \e        Format the roff escape character on the output; widely
                     used in man pages to render a backslash glyph.  It works
                     reliably as long as the “ec” request is not used, which
                     should never happen in man pages, and it is slightly
                     more portable than the more explicit \[rs] (“reverse
                     solidus”) special character escape sequence.

           \fB, \fI, \fR, \fP
                     Switch to bold, italic, roman, or back to the previous
                     style, respectively.  Either \f or \c is needed when
                     three different font styles are required in a word.

                            .RB [ \-\-reference\-dictionary=\fI\,name\/\fP ]

                            .RB [ \-\-reference\-dictionary=\c
                            .IR name ]

                     Style escape sequences may be more portable than \c.  As
                     shown above, it is up to you to account for italic
                     corrections with “\/” and “\,”, which are themselves GNU
                     extensions, if desired and if supported by your
                     implementation.

                     \fP reliably returns to the style in use immediately
                     preceding the previous \f escape sequence only if no
                     sectioning, paragraph, example, or style macro calls
                     have intervened.

                     As long as at most two styles are needed in a word,
                     style macros like B and BI usually result in more
                     readable roff source than \f escape sequences do.

           Several special characters are also widely portable.  Except for
           \-, \[em], and \[ga], AT&T troff did not consistently define the
           characters listed below, but its descendants, like DWB, Plan 9, or
           Solaris troff, can be made to support them by defining them in
           font description files, making them aliases of existing glyphs if
           necessary; see groff_font(5).  groff's extended notation for
           special characters, \[xx], is also supported by mandoc(1),
           Heirloom Doctools troff, and neatroff, but not DWB, Plan 9, or
           Solaris troffs.

           \-     Minus sign.  \- produces the basic Latin hyphen-minus
                  (U+002D) specifying Unix command-line options and
                  frequently used in file names.  “-” is a hyphen in roff;
                  some output devices format it as U+2010 (hyphen).

           \[aq]  Basic Latin neutral apostrophe.  Some output devices format
                  “'” as a right single quotation mark.

           \[oq]
           \[cq]  Opening (left) and closing (right) single quotation marks.
                  Use these for paired directional single quotes, ‘like
                  this’.

           \[dq]  Basic Latin quotation mark (double quote).  Employ it in
                  macro calls to work around interpretation of ‘"’ as an
                  argument delimiter.

                         .TP
                         .BI "split \[dq]" text \[dq]

           \[lq]
           \[rq]  Left and right double quotation marks.  Use these for
                  paired directional double quotes, “like this”.

           \[em]  Em dash.  Use for an interruption—such as this one—in a
                  sentence.

           \[en]  En dash.  Use to separate the ends of a range, as between
                  numbers; for example, “the digits 1–9”.

           \[ga]  Basic Latin grave accent.  Some output devices format “`”
                  as a left single quotation mark.

           \[ha]  Basic Latin circumflex accent (“hat”).  Some output devices
                  format “^” as U+02C6 (modifier letter circumflex accent).

           \[rs]  Reverse solidus (backslash).  The backslash is the default
                  escape character in the roff language, so it does not
                  represent itself in output.  Also see \e above.

           \[ti]  Basic Latin tilde.  Some output devices format “~” as
                  U+02DC (small tilde).

           For maximum portability, avoid escape sequences (including special
           characters) not listed above.

       Hooks
           Two macros, both GNU extensions, are called internally by the
           groff man package to format page headers and footers and can be
           redefined by the administrator in a site's man.local file (see
           section “Files” below).  The presentation of TH above describes
           the default headers and footers.  Because these macros are hooks
           for groff man internals, man pages have no reason to call them.
           Such hook definitions typically consist of “sp” and “tl” requests.
           PT furthermore has the responsibility of emitting a PDF bookmark
           after writing the first page header in a document.  Consult the
           existing implementations in an.tmac when drafting replacements.

           .BT    Set the page footer text (“bottom trap”).

           .PT    Set the page header text (“page trap”).

           To remove a page header or footer entirely, define the appropriate
           macro as empty rather than deleting it.

       Deprecated features
           Use of the following in man pages for public distribution is
           discouraged.

           .AT [system [release]]
                  Alter the footer for use with legacy AT&T man pages,
                  overriding any definition of the footer-inside argument to
                  TH.  This macro exists only to render man pages from
                  historical systems.

                  The inside footer is populated per the value of system.

                         3      7th edition (default)

                         4      System III

                         5      System V

                  The optional release argument specifies the release number,
                  as in “System V Release 3”.

           .DT    Reset tab stops to the default (every 0.5i [inches]).

                  Use of this presentation-oriented macro is deprecated.  It
                  translates poorly to HTML, under which exact space control
                  and tabulation are not readily available.  Thus,
                  information or distinctions that you use tab stops to
                  express are likely to be lost.  If you feel tempted to
                  change the tab stops such that calling this macro later to
                  restore them is desirable, consider composing a table using
                  tbl(1) instead.

           .OP option-name [option-argument]
                  Indicate an optional command parameter called option-name,
                  which is set in bold.  If the option takes an argument,
                  specify option-argument using a noun, abbreviation, or
                  hyphenated noun phrase.  If present, option-argument is
                  preceded by a space and set in italics.  Square brackets in
                  roman surround both arguments.

                  Use of this quasi-semantic macro, an extension whose name
                  originated in DWB troff, is deprecated; groff's interface
                  differs.  Neither can easily be used to annotate options
                  that take optional arguments or options whose arguments
                  have internal structure (such as a mixture of literal and
                  variable components).  One could work around these
                  limitations with font selection escape sequences, but font
                  style alternation macros are preferable; they are more
                  flexible and perform italic corrections on typesetters.

           .PD [vertical-space]
                  Configure the amount of vertical space between paragraphs
                  or (sub)sections.  The optional argument vertical-space
                  specifies the amount; the default scaling unit is “v”.
                  Without an argument, inter-paragraph spacing resets to its
                  default value; see subsection “Horizontal and vertical
                  spacing” above.

                  Use of this presentation-oriented macro is deprecated.  It
                  translates poorly to HTML, under which exact control of
                  inter-paragraph spacing is not readily available.  Thus,
                  information or distinctions that you use PD to express are
                  likely to be lost.

           .SB [text]
                  Set text in bold and (on typesetters) one point smaller
                  than the default type size.  Given no argument, SB plants a
                  one-line input trap; text on the next line, which can be
                  further formatted with a macro, is set smaller and in bold.
                  Use of this macro, an extension originating in SunOS 4.0
                  troff, is deprecated.  SM without an argument, followed
                  immediately by “B text”, produces the same output more
                  portably.  The macros' order is interchangeable; put text
                  with the latter.

                  Note: terminals render text in bold at the normal size
                  instead.  Do not rely upon SB to communicate semantic
                  information distinct from using bold style at normal size;
                  it is hidden from readers using such devices.

           .UC [version]
                  Alter the footer for use with legacy BSD man pages,
                  overriding any definition of the footer-inside argument to
                  TH.  This macro exists only to render man pages from
                  historical systems.

                  The inside footer is populated per the value of version.

                         3      3rd Berkeley Distribution (default)

                         4      4th Berkeley Distribution

                         5      4.2 Berkeley Distribution

                         6      4.3 Berkeley Distribution

                         7      4.4 Berkeley Distribution

       History
           M. Douglas McIlroy ⟨m.douglas.mcilroy@dartmouth.edu⟩ designed,
           implemented, and documented the AT&T man macros for Unix Version 7
           (1979) and employed them to edit Volume 1 of its Programmer's
           Manual, a compilation of all man pages supplied by the system.
           The package supported the macros listed in this page not described
           as extensions, except P and the deprecated AT and UC.  It
           documented no registers and defined only R and S strings.

           UC appeared in 3BSD (1980).  Unix System III (1980) introduced P
           and exposed the registers IN and LL, which had been internal to
           Seventh Edition Unix man.  PWB/Unix 2.0 (1980) added the Tm
           string.  4BSD (1980) added lq and rq strings.  SunOS 2.0 (1985)
           recognized C, D, P, and X registers.  4.3BSD (1986) added AT and
           P.  Ninth Edition Unix (1986) introduced EX and EE.  SunOS 4.0
           (1988) added SB.  Unix System V (1988) incorporated the lq and rq
           strings.

           Except for EX/EE, James Clark implemented the foregoing features
           in early versions of groff.  Later, groff 1.20 (2009) resurrected
           EX/EE and originated SY/YS, TQ, MT/ME, and UR/UE.  Plan 9 from
           User Space's troff introduced MR in 2020, and incorporated the lq
           and rq strings in 2025.

## [](#Options)Options

           The following groff options set registers (with -r) and strings
           (with -d) recognized and used by the man macro package.  To ensure
           rendering consistent with output device capabilities and reader
           preferences, man pages should never manipulate them.

           -dAD=adjustment-mode
                  Set line adjustment to adjustment-mode, which is typically
                  “b” for adjustment to both margins (the default), or “l”
                  for left alignment (ragged right margin).  Any valid
                  argument to groff's “ad” request may be used.  See groff(7)
                  for less-common choices.

           -rBP=base-paragraph-inset
                  Set the inset amount for ordinary paragraphs not within an
                  RS/RE inset.  The default is 5n.

           -rcR=1 Enable continuous rendering.  Output is not paginated;
                  instead, one (potentially very long) page is produced.
                  This is the default for terminal and HTML devices.  Use
                  -rcR=0 to disable it on terminals; on HTML devices, it
                  cannot be disabled.

           -rC1   Number output pages consecutively, in strictly increasing
                  sequence, rather than resetting the page number to 1 (or
                  the value of register P) with each new man document.

           -rCHECKSTYLE=n
                  Report problems with usage of this macro package exhibited
                  by the input at verbosity level n, where n is an integer in
                  the range 0–3, inclusive; 0 disables the messages and is
                  the default.  This feature is a development and debugging
                  aid for man page maintainers; the problems diagnosed, and
                  range and meanings of the supported levels, are subject to
                  change.

           -rCS=1 Set section headings (the argument(s) to SH) in full
                  capitals.  This transformation is off by default because it
                  discards lettercase distinctions.

           -rCT=1 Set the man page identifier (the first argument to TH) in
                  full capitals in headers and footers.  This transformation
                  is off by default because it discards lettercase
                  distinctions.

           -rD1   Enable double-sided layout, formatting footers for even and
                  odd pages differently; see the description of TH in
                  subsection “Document structure macros” above.

           -rFT=footer-distance
                  Set distance of the footer relative to the bottom of the
                  page to footer-distance; this amount is always negative.
                  At one half-inch above this location, the page text is
                  broken before writing the footer.  Ignored if continuous
                  rendering is enabled.  The default is “-0.5i - 1v”.

           -dHF=heading-font
                  Select the font used for section and subsection headings;
                  the default is “B” (bold style of the default family).  Any
                  valid argument to groff's “ft” request may be used.  See
                  groff(7).

           -rHY=0 Disable automatic hyphenation.  Normally, it is
                  enabled (1).  The hyphenation mode is determined by the
                  groff locale; see section “Localization“ of groff(7).

           -rIN=standard-indentation
                  Set the default indentation amount used by IP, TP, and HP,
                  and the inset amount used by RS.  The default is 7n on
                  terminals and 7.2n on typesetters.  Use only integer
                  multiples of unit “n” on terminals for consistent
                  indentation.

           -rLL=line-length
                  Set line length; the default is 80n on terminals and 6.5i
                  on typesetters.

           -rLT=title-length
                  Set the line length for titles.  (“Titles” is the roff term
                  for headers and footers.)  By default, it is set to the
                  line length (see -rLL above).

           -dMF=man-page-topic-font
                  Select the font used for man page identifiers in TH calls
                  and topics named in MR calls; the default is “I” (italic
                  style of the default family).  Any valid argument to
                  groff's “ft” request may be used.  If the MF string ends in
                  “I”, the package assumes it to be an oblique typeface, and
                  applies italic corrections before and after man page topics
                  and identifiers.

           -rPn   Start enumeration of pages at n.  The default is 1.

           -rPO=page-offset
                  Set page offset; the default is 0 on terminals and 1i on
                  typesetters.

           -rStype-size
                  Use type-size for the document's body text; acceptable
                  values are 10, 11, or 12 points.  See subsection “Font
                  style macros” above for the default.

           -rSN=subsection-indentation
                  Set indentation of subsection headings to subsection-
                  indentation.  The default is 3n.

           -rTS=separation
                  Require the given separation between a TP paragraph's tag
                  and its body.  The default is 2n.

           -rU0   Disable generation of URI hyperlinks in output drivers
                  capable of them, making the arguments to MT and UR calls
                  visible as formatted text.  grohtml(1), gropdf(1), and
                  grotty(1) enable hyperlinks by default (the last only if
                  not in its legacy output mode).

           -rXp   Number successors of page p as pa, pb, pc, and so forth.
                  The register tracking the suffixed page letter uses format
                  “a” (see the “af” request in groff(7)).  For example, the
                  option -rX2 produces the following page numbers: 1, 2, 2a,
                  2b, ..., 2aa, 2ab, and so on.

## [](#Files)Files

           /usr/local/share/groff/1.24.1/tmac/an.tmac
                  Most man macros are defined in this file.  It also loads
                  extensions from an-ext.tmac (see below).

           /usr/local/share/groff/1.24.1/tmac/andoc.tmac
                  This brief groff program detects whether the man or mdoc
                  macro package is used by a document and loads the correct
                  macro definitions, taking advantage of the fact that pages
                  using them must call TH or Dd, respectively, before any
                  other macros.  A man program or a user typing, for example,
                  “groff -mandoc page.1”, need not know which package the
                  file page.1 uses.  Multiple man pages, in either format,
                  can be handled; andoc reloads each macro package as
                  necessary.  Page-local redefinitions of names used by the
                  man or mdoc packages prior to TH or Dd calls are
                  “clobbered” by the reloading process.  If you want to
                  provide your own definition of an extension macro to ensure
                  its availability, the an-ext.tmac entry below offers
                  advice.

           /usr/local/share/groff/1.24.1/tmac/an-ext.tmac
                  Definitions of macros described above as extensions (and
                  not deprecated) are contained in this file; in some cases,
                  they are simpler versions of definitions appearing in
                  an.tmac, and are ignored if the formatter is GNU troff.
                  They are written to be compatible with AT&T troff and
                  permissively licensed—not copylefted.  To reduce the risk
                  of name space collisions, string and register names begin
                  only with “m”.  We encourage man page authors who are
                  concerned about portability to legacy Unix systems to copy
                  these definitions into their pages, and maintainers of
                  troff implementations or work-alike systems that format man
                  pages to re-use them.  To ensure reliable rendering, define
                  them after your page calls TH; see the discussion of andoc
                  .tmac above.  Further, it is wise to define such page-local
                  macros (if at all) after the “Name” section to accommodate
                  timid makewhatis(8) or mandb(8) implementations that easily
                  give up scanning for indexing material.

           /usr/local/share/groff/1.24.1/tmac/man.tmac
                  is a wrapper enabling the package to be loaded with the
                  option “-m man”.

           /usr/local/share/groff/1.24.1/tmac/mandoc.tmac
                  is a wrapper enabling andoc.tmac to be loaded with the
                  option “-m mandoc”.

           /usr/local/share/groff/site-tmac/man.local
                  Put site-local changes and customizations into this file.

                         .\" Put only one space after the end of a sentence.
                         .ss 12 0 \" See groff(7).
                         .\" Keep pages narrow even on wide terminals.
                         .if n .if \n[LL]>80n .nr LL 80n

                  On multi-user systems, it is more considerate to users
                  whose preferences may differ from the administrator's to be
                  less aggressive with such settings, or to permit their
                  override with a user-specific man.local file.  Place the
                  requests below at the end of the site-local file to
                  manifest courtesy.
                         .soquiet \V[XDG_CONFIG_HOME]/man.local
                         .soquiet \V[HOME]/.man.local
                  However, a security-sandboxed man(1) program may lack
                  permission to open such files.

## [](#Notes)Notes

           Some tips on composing and troubleshooting your man pages follow.

           • What's the difference between a man page topic and identifier?

             A single man page may document several related but distinct
             topics.  For example, printf(3) and fprintf(3) are often
             presented together.  Moreover, multiple programming languages
             have functions named “printf”, and may document these in a man
             page.  The identifier is intended to (with the section) uniquely
             identify a page on the system; it may furthermore correspond
             closely to the file name of the document.

             The man(1) librarian makes access to man pages convenient by
             resolving topics to man page identifiers.  Thus, you can type
             “man fprintf”, and other pages can refer to it, without knowing
             whether the installed document uses “printf”, “fprintf”, or even
             “c_printf” as its identifier.

           • Some ASCII characters look funny or copy and paste wrong.

             On devices with large glyph repertoires, like UTF-8-capable
             terminals and PDF, GNU troff, like AT&T troff before it, maps
             several keycaps to code points outside the Unicode basic Latin
             range (historically “ASCII”) because that usually results in
             better typography in the general case.  When documenting
             GNU/Linux command or C language syntax, however, this
             translation is sometimes not desirable.

             To get a “literal”...   ...should be input.
             ────────────────────────────────────────────
                                 '   \[aq]
                                 -   \-
                                 \   \[rs]
                                 ^   \[ha]
                                 `   \[ga]
                                 ~   \[ti]
             ────────────────────────────────────────────

             If a neutral double quote (") is needed in a macro argument, you
             can use \[dq] to get it.  Do not use \[aq] for an ordinary
             apostrophe (as in “can't”) or \- for an ordinary hyphen (as in
             “word-aligned”).

           • Do I ever need to use an empty macro argument ("")?

             Probably not.  When this seems necessary, often a shorter or
             clearer alternative is available.

                    Instead of...               ...should be considered.
             ────────────────────────────────────────────────────────────────
             .TP ""                         .TP
             ────────────────────────────────────────────────────────────────
             .BI "" italic-text bold-text   .IB italic-text bold-text
             ────────────────────────────────────────────────────────────────
             .TH foo 1 "" "foo 1.2.3"       .TH foo 1 yyyy-mm-dd "foo 1.2.3"
             ────────────────────────────────────────────────────────────────
             .IP "" 4n                      .IP
             ────────────────────────────────────────────────────────────────
             .IP "" 4n                      .RS 4n
             paragraph                      .P
             ...                            paragraph
             ...                            .RE
             ────────────────────────────────────────────────────────────────
             .B one two "" three            .B one two three

             In the title heading (TH), the date of the page's last revision
             is more important than packaging information; it should not be
             omitted.  Ideally, a page maintainer keeps both up to date.

             IP is sometimes ill-understood and misused, especially when no
             mark argument is supplied—an indentation argument is not
             required.  By setting an explicit indentation, you may be
             overriding the reader's preference as set with the -rIN option.
             If your page renders adequately without one, use the simpler
             form.  If you need to indent multiple (unmarked) paragraphs,
             consider setting an inset region with RS and RE instead.

             In the last example, the empty argument does have a subtly
             different effect than its suggested replacement: the empty
             argument causes an additional space character to be interpolated
             between the arguments “two” and “three”—but it is a regular
             breaking space, so it can be discarded at the end of an output
             line.  It is better not to be subtle, particularly with space,
             which can be overlooked in source and rendered forms.

           • RS doesn't indent relative to my indented paragraph.

             The RS macro determines the inset amount, the position at which
             an ordinary paragraph (P and its synonyms) is set; the value of
             the IN register determines its default amount.  This register
             also determines the default indentation used by IP, TP, and HP.
             To create an inset relative to an indented paragraph, call RS
             repeatedly until an acceptable indentation is achieved, or give
             RS an indentation argument that is at least as much as the
             paragraph's indentation amount relative to an adjacent ordinary
             (P) paragraph.

             Another approach to tagged paragraphs places an RS call
             immediately after the tag; this also forces a break regardless
             of the tag's width, which some authors prefer.  Follow-up
             paragraphs under the tag can then be set with P instead of IP.
             Remember to use RE to end the indented region before starting
             the next tagged paragraph (at the appropriate nesting level).

           • RE doesn't move the inset back to the expected level.

             RE takes an inset level as an argument, unlike RS's inset
             amount.  “.RE 1” goes to the level before any RS macros were
             called, RE 2 goes to the level of the first RS call you made,
             and so forth.  If you desire symmetry in your macro calls,
             simply issue one RE without an argument for each RS that
             precedes it.

             The SH and SS sectioning macros clear relative insets; RE calls
             have no effect until RS is used again.

           • Do I need to keep typing the indentation in a series of IP
             calls?

             Not if you don't want to change it.  Review subsection
             “Horizontal and vertical spacing” above.

               Instead of...     ...should be considered.
             ─────────────────────────────────────────────
             .IP \[bu] 4n        .IP \[bu] 4n
             paragraph           paragraph
             .IP \[bu] 4n        .IP \[bu]
             another-paragraph   another-paragraph
             ─────────────────────────────────────────────

           • Why doesn't the package provide a string to insert an ellipsis?

             Examples of ellipsis usage are shown above, in subsection
             “Synopsis macros”.  The idiomatic roff ellipsis is three dots
             (periods) with thin space escape sequences \| internally
             separating them.  Since dots both begin control lines and are
             candidate end-of-sentence characters, however, it is sometimes
             necessary to prefix and/or suffix an ellipsis with the dummy
             character escape sequence \&.  That fact stands even if a string
             is defined to contain the sequence; further, if the string ends
             with \&, end-of-sentence detection is defeated when you use the
             string at the end of an actual sentence.  (Ending a sentence
             with an ellipsis is often poor style, but not always.)  A
             hypothetical string EL that contained an ellipsis, but not the
             trailing dummy character \&, would then need to be suffixed with
             the latter when not ending a sentence.

                 Instead of...              ...do this.
             ──────────────────────────────────────────────────
             .ds EL \&.\|.\|.         Arguments are
             Arguments are            .IR src-file\~ .\|.\|.\&
             .IR src-file\~ \*(EL\&   .IR dest-dir .
             .IR dest-dir .
             ──────────────────────────────────────────────────

             The first column practices a false economy; the savings in
             typing is offset by the cost of obscuring even the suggestion of
             an ellipsis to a casual reader of the source document, and
             reduced portability to non-roff man page formatters that cannot
             handle string definitions.

             Unicode defines an ellipsis code point, and some fonts have an
             ellipsis glyph, which some man pages have accessed non-portably
             with the font-dependent \N escape sequence.  We discourage their
             use; on terminals, they may crowd the dots into a half-width
             character cell, and do not render at all if the output device
             lacks the glyph.  In synopses, missing ellipses can mislead the
             reader.  Dots and space are universally supported.

           • When and how should I use quotation marks?

             As noted above in subsection “Font style macros”, apply
             quotation marks to “brief specimens of literal text, such as
             article titles, inline examples, mentions of individual
             characters or short strings, and (sub)section headings in man
             pages”.  Multi-word literals, such as Unix commands with
             arguments, when set inline (as opposed to displayed between EX
             and EE), should be quoted to ensure that the boundaries of the
             literal are clear even when the material is stripped of font
             styling by, for example, copy-and-paste operations.  groff,
             Heirloom Doctools troff, neatroff, and mandoc support all of the
             special characters \[oq], \[cq], \[lq], \[rq], \[aq], and \[dq]
             described in subsection “Portability” above.  DWB, Plan 9, and
             Solaris troffs do not.  Interpolating the strings \*(lq and
             \*(rq portably yields directional double quotation marks, if
             available, in all these formatters (though neatroff does not
             supply a man macro package), but they cannot reliably be used in
             macro arguments.

             Obtaining directional single quotation marks is more of a
             challenge.  Historically, man pages used ` and ', which troff
             rendered on typesetters as ‘ and ’, exclusively for them.
             However, in recent years, some distributors of groff have chosen
             to override the meanings of these characters in man pages,
             remapping them to their Unicode Basic Latin code points.
             Unfortunately, ` and ' are the only reliable means of obtaining
             directional single quotation marks in AT&T troff; in that
             implementation, often no special character escape sequences
             exist to obtain them.  Further, AT&T troff's special character
             identifiers, like its font names, were device-specific.  To
             achieve quotation portably in man pages rendered both by AT&T
             and more modern troffs, consider adding a preamble to your page
             after the TH call as follows.

                    .ie \n(.g \{\
                    .  ds oq \[oq]\"
                    .  ds cq \[cq]\"
                    .\}
                    .el \{\
                    .  ds oq `\"
                    .  ds cq '\"
                    .\}

             You must then use the \* escape sequence to interpolate the
             quotation mark strings.

                    The command
                    .RB \*(oq "while !\& git pull; do sleep 10; done" \*(cq
                    retries an update from the repository until it succeeds.

             If this procedure seems complex, petition your distributor to
             revert their remapping of the ` and ' characters.

           • Escape sequences of the form \[xx] don't format correctly.

             The \[xx] special character escape sequence is a GNU troff
             extension also supported by mandoc, Heirloom Doctools troff, and
             neatroff.  DWB, Plan 9, and Solaris troffs don't implement it.
             If your man page requires portability to these formatters, spell
             such escape sequences as “\(xx”; no closing parenthesis is used.
             xx must be exactly two characters; groff_char(7) lists portable
             special character identifiers.

## [](#Authors)Authors

           James Clark wrote the initial GNU implementation of the man macro
           package.  Later, Werner Lemberg ⟨wl@gnu.org⟩ supplied the S, LT,
           and cR registers, the last a 4.3BSD-Reno mdoc(7) feature.  Larry
           Kollar ⟨kollar@alltel.net⟩ added the FT, HY, and SN registers; the
           HF string; and the PT and BT macros in groff 1.19 (2003).  Lemberg
           and Eric S. Raymond ⟨esr@thyrsus.com⟩ contributed EX/EE, MT/ME,
           UR/UE, TQ, and an early version of the SY/YS macros to groff 1.20
           (2009).  G. Branden Robinson ⟨g.branden.robinson@gmail.com⟩
           implemented the AD and MF strings; CS, CT, and U registers; and
           the MR macro for groff 1.23 (2023), and the BP, PO, and TS
           registers and a revised implementation of the SY/YS macros for
           groff 1.24 (2026).

           Susan G. Kleinmann ⟨sgk@debian.org⟩ wrote the initial version of
           this document for the Debian GNU/Linux system.  Lemberg imported
           it to groff.  He and Robinson revised and updated it.  Raymond and
           Robinson documented the extension macros.  Raymond also originated
           the portability section, to which Ingo Schwarze ⟨schwarze@usta.de⟩
           contributed most of the material on escape sequences.

## [](#See_also)See also

           tbl(1), eqn(1), and refer(1) are preprocessors used with man
           pages.  man(1) describes the man page librarian on your system.
           groff_mdoc(7) details the groff version of BSD's alternative macro
           package for man pages.

           groff_man(7), groff(7), groff_char(7)

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

    groff 1.24.1                    2026-03-14             groff_man_style(7)

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
