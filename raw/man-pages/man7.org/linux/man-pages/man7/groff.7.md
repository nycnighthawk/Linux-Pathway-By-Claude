---
{"title": "groff(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/groff.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groff(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Description](#Description) \| [Input format](#Input_format) \| [Syntax characters](#Syntax_characters) \| [Sentences](#Sentences) \| [Tabs and leaders](#Tabs_and_leaders) \| [Line continuation](#Line_continuation) \| [Colors](#Colors) \| [Measurements](#Measurements) \| [Numeric expressions](#Numeric_expressions) \| [Identifiers](#Identifiers) \| [Control characters](#Control_characters) \| [Invoking requests](#Invoking_requests) \| [Calling macros](#Calling_macros) \| [Using escape sequences](#Using_escape_sequences) \| [Delimiters](#Delimiters) \| [Dummy characters](#Dummy_characters) \| [Page control](#Page_control) \| [Control structures](#Control_structures) \| [Syntax reference conventions](#Syntax_reference_conventions) \| [Request short reference](#Request_short_reference) \| [Escape sequence short reference](#Escape_sequence_short_reference) \| [Strings](#Strings) \| [Registers](#Registers) \| [Using fonts](#Using_fonts) \| [Hyphenation](#Hyphenation) \| [Localization](#Localization) \| [Writing macros](#Writing_macros) \| [Traps](#Traps) \| [Diversions](#Diversions) \| [Punning names](#Punning_names) \| [Environments](#Environments) \| [Postprocessor access](#Postprocessor_access) \| [Underlining](#Underlining) \| [Compatibility mode](#Compatibility_mode) \| [Debugging](#Debugging) \| [Authors](#Authors) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    groff(7)             Miscellaneous Information Manual            groff(7)

## [](#Name)Name

           groff - GNU roff language reference

## [](#Description)Description

           groff is short for GNU roff, a free reimplementation of the AT&T
           device-independent troff typesetting system.  See roff(7) for a
           survey of and background on roff systems.

           This document is intended as a reference.  The primary groff
           manual, Groff: The GNU Implementation of troff, by Trent A. Fisher
           and Werner Lemberg, is a better resource for learners, containing
           many examples and much discussion.  It is written in Texinfo; you
           can browse it interactively with “info groff”.  Additional
           formats, including plain text, HTML, TeX DVI, and PDF, may be
           available in /usr/local/share/doc/groff-1.24.1.

           We apply the term “groff” to the language documented here, the GNU
           implementation of the overall system, the project that develops
           that system, and the command of that name.  In the first sense,
           groff is an extended dialect of the roff language, for which many
           similar implementations exist.

           GNU troff, installed on this system as troff(1), is the formatter:
           a program that reads device and font descriptions (groff_font(5)),
           interprets the groff language expressed in input text, and
           translates it into a device-independent page description language
           (groff_out(5)) that is usually then post-processed by an output
           driver to produce PostScript, PDF, HTML, DVI, or terminal output.
           We speak of “the formatter” when describing behavior that is
           generally true of troff and nroff programs.

## [](#Input_format)Input format

           Organize input to GNU troff into lines separated by the Unix
           newline character (U+000A), using the character encoding it
           recognizes: ISO Latin-1 (8859-1).  We recommend use of
           ISO 646:1991 IRV (US-ASCII) or (equivalently) the Basic Latin
           subset of ISO 10646 (Unicode); see groff_char(7).

           Some control characters (from the sets “C0 Controls” and “C1
           Controls” as Unicode describes them) are invalid as input
           characters.  GNU troff discards them upon reading.  (It also emits
           a warning in category “input”; see section “Warnings” of
           troff(1).)  It processes a character sequence “foo”, followed by
           an invalid character and then “bar”, as “foobar”.

           Invalid input characters comprise 0x00, 0x0B, 0x0D–0x1F, and
           0x80–0x9F.  (Historically, control characters like ASCII STX, ETX,
           and BEL (Control+B, Control+C, and Control+G) respectively) have
           been observed in roff documents, particularly in macro packages
           employing them as delimiters with the output comparison operator
           to try to avoid collisions with the content of arbitrary user-
           supplied parameters (see subsection “Conditional expressions”
           below).  We discourage this expedient; in GNU troff it is
           unnecessary (outside of compatibility mode) because the program
           parses delimited arguments at a different input level than their
           surrounding context.  See section “Miscellaneous” of
           groff_diff(7).)  GNU troff uses some of these code points for
           internal purposes, making non-trivial the extension of the program
           to accept UTF-8 or other encodings that use characters from these
           ranges.

## [](#Syntax_characters)Syntax characters

           Several input characters are syntactically significant to groff.
           The most important of these distinguish control lines, which
           instruct the formatter, from text lines that are formatted as
           output.

           .   A dot at the beginning of an input line marks it as a control
               line.  It can also follow the el and nop requests, and the
               condition in “if”, ie, and “while” requests.  The control
               character invokes requests and calls macros by the name that
               follows it.  The cc request can change the control character.

           '   The neutral apostrophe is the no-break control character,
               recognized where the control character is.  It suppresses the
               (first) break implied by the bp, ce, cf, fi, fl, “in”, nf, rj,
               sp, ti, and trf requests.  The requested operation takes
               effect at the next break.  It makes br and brp nilpotent.  The
               no-break control character can be changed with the c2 request.
               When formatted, “'” may be typeset as a typographical
               quotation mark; use the \[aq] special character escape
               sequence to format a neutral apostrophe glyph.

           "   The neutral double quote can be used to enclose arguments to
               macros and strings, and is required if those arguments contain
               space or tab characters.  The requests “as”, as1, cf, char,
               ds, ds1, fchar, fschar, mso, msoquiet, nx, “open”, opena, pi,
               schar, “so”, soquiet, sy, and trf strip a leading neutral
               double quote from their final arguments to allow embedding of
               leading spaces.  All such arguments are “strings” in a general
               sense, representing character sequences, file names, operating
               system commands, or parameters to an output device extension
               command.  To include a double quote inside a quoted argument,
               use the \[dq] special character escape sequence (which also
               serves to typeset the glyph in text).

           \   A backslash introduces an escape sequence.  The escape
               character can be changed with the ec request; eo disables
               escape sequence recognition.  Use the \[rs] special character
               escape sequence to format a backslash glyph, and \e to typeset
               the glyph of the current escape character.

           (   An opening parenthesis is special only in certain escape
               sequences; when recognized, it introduces an argument of
               exactly two characters.  groff offers the more flexible square
               bracket syntax.

           [   An opening bracket is special only in certain escape
               sequences; when recognized, it introduces an argument (list)
               of any length, not including a closing bracket.

           ]   A closing bracket is special only when an escape sequence
               using an opening bracket as an argument delimiter is being
               interpreted.  It ends the argument (list).

           Additionally, the Control+A character (U+0001) in text is
           interpreted as a leader (see below).

           Horizontal whitespace characters are significant to groff, but
           trailing spaces on text lines are ignored.

           space  On control lines and within bracketed escape sequences,
                  spaces separate arguments.  On text lines, they separate
                  words.  Multiple adjacent space characters in text cause
                  groff to attempt end-of-sentence detection on the preceding
                  word (and trailing punctuation).  The amount of space
                  between words and sentences is controlled by the ss
                  request.  When filling is enabled (the default), a line may
                  be broken at a space.  When adjustment is enabled (the
                  default), inter-word spaces are expanded until the output
                  line reaches the configured length.  An adjustable but non-
                  breaking space is available with \~.  To get a space of
                  fixed width, use one of the escape sequences ‘\ ’ (the
                  escape character followed by a space), \0, \|, \^, or \h;
                  see section “Escape sequences” below.

           newline
                  On text lines, a newline formats an inter-word space and,
                  if filling is enabled, triggers end-of-sentence recognition
                  on the preceding text.  See section “Line continuation”
                  below.

           tab    A tab character on a text line causes the drawing position
                  to advance to the next defined tab stop.

## [](#Sentences)Sentences

           Configure the sets of characters that potentially end sentences or
           are transparent to sentence endings with the cflags request.  Use
           the ss request to change—or eliminate—supplemental inter-sentence
           space.

## [](#Tabs_and_leaders)Tabs and leaders

           The formatter interprets input horizontal tab characters (“tabs”)
           and Control+A characters (“leaders”) into movements to the next
           tab stop.  Tabs simply move to the next tab stop; leaders place
           enough periods to fill the space.  Tab stops are by default
           located every half inch measured from the drawing position
           corresponding to the beginning of the input line; see section
           “Page geometry” of roff(7).  Tabs and leaders do not cause breaks
           and therefore do not interrupt filling.  Tab stops can be
           configured with the ta request, and tab and leader glyphs with the
           tc and lc requests, respectively.

## [](#Line_continuation)Line continuation

           When filling is enabled, input and output line breaks generally do
           not correspond.  The roff language therefore distinguishes input
           and output line continuation.

           A backslash \ immediately followed by a newline, sometimes
           discussed as \newline, suppresses the effects of that newline on
           the input.  The next input line thus retains the classification of
           its predecessor as a control or text line.  \newline is useful for
           managing line lengths in the input during document maintenance;
           you can break an input line at a space, or in the middle of a
           word, request invocation, macro call, or escape sequence.  Input
           line continuation is invisible to the formatter, with two
           exceptions: the | operator recognizes the new input line, and the
           input line counter register .c increments.

           The \c escape sequence continues an output line.  Nothing on the
           input line after it is formatted.  In contrast to \newline, a line
           after \c is treated as a new input line, so a control character is
           recognized at its beginning.  The visual results depend on whether
           filling is enabled.  An intervening control line that causes a
           break overrides \c, flushing out the pending output line in the
           usual way.  The register .int interpolates a positive value only
           if the pending output line has been continued with \c; this datum
           is associated with the environment.

## [](#Colors)Colors

           groff supports color output with a variety of color spaces and up
           to 16 bits per channel.  Some devices, particularly terminals, may
           be more limited.  When color support is enabled, two colors are
           current at any given time: the stroke color, with which glyphs,
           rules (lines), and geometric objects like circles and polygons are
           drawn, and the fill color, which can be used to paint the interior
           of a closed geometric figure.  The color, defcolor, gcolor, and
           fcolor requests; \m and \M escape sequences; and .color, .m, and
           .M registers exercise color support.

           Each output device has a color named “default”, which cannot be
           redefined.  A device's default stroke and fill colors are not
           necessarily the same.  For the dvi, html, pdf, ps, and xhtml
           output devices, troff automatically loads a macro file defining
           many color names at startup.  By the same mechanism, the devices
           supported by grotty(1) recognize the eight standard
           ISO 6429/ECMA-48 color names.  (These are known vulgarly as “ANSI”
           colors, after its X3.64 standard, now withdrawn.)

## [](#Measurements)Measurements

           Express numeric parameters that specify measurements as integers
           or decimal fractions with an optional scaling unit suffixed.  A
           scaling unit is a letter that immediately follows the magnitude of
           a measurement.  Digits after the decimal point are optional.

           The formatter scales measurements by the specified scaling unit,
           storing them internally (with any fractional part discarded) in
           basic units.  The device resolution can therefore be obtained by
           storing a value of “1i” to a register, then reading the register.

           u      Basic unit; it is at least as small as any other unit.
           i      Inch; defined as 2.54 centimeters.
           c      Centimeter.
           p      Point; a typesetter's unit used for measuring type size.
                  There are 72 points to an inch.
           P      Pica; another typesetter's unit.  There are 6 picas to an
                  inch and 12 points to a pica.
           z      Typographical point; like p, but used only with type sizes,
                  to overcome a limitation of AT&T troff.
           s      Scaled point.
           f      Multiplication by 65,536; scales decimal fractions in the
                  interval [0, 1] to 16-bit unsigned integers.

           The magnitudes of other scaling units depend on the text
           formatting parameters in effect.

           m      Em; an em is equal to the current type size in points.
           n      En; on typesetters, an en is one-half em, but on terminals
                  an en equals an em.
           v      Vee; distance between text baselines.
           M      Hundredth of an em.

       Motion quanta
           The basic unit u is not necessarily an output device's smallest
           addressable length; u can be smaller to avoid integer rounding
           errors.  The minimum distances that a device can work with in the
           horizontal and vertical directions are termed its motion quanta,
           stored in the .H and .V registers, respectively.  The formatter
           rounds measurements to applicable motion quanta.  Half-quantum
           fractions round toward zero.

       Default units
           A general-purpose register (one created or updated with the nr
           request; see section “Registers” below) is implicitly
           dimensionless, or reckoned in basic units if interpreted in a
           measurement context.  But it is convenient for many requests and
           escape sequences to infer a scaling unit for an argument if none
           is specified.  An explicit scaling unit (not after a closing
           parenthesis) can override an undesirable default.  Effectively,
           the default unit is suffixed to the expression if a scaling unit
           is not already present.  GNU troff's use of integer arithmetic in
           numeric expressions should also be kept in mind.

## [](#Numeric_expressions)Numeric expressions

           When evaluated, a numeric expression interpolates an integer.  GNU
           troff recognizes the following operators.

                 +   addition
                 -   subtraction
                 *   multiplication
                 /   truncating division
                 %   modulus
           ────────────────────────────────────────────
           unary +   assertion, motion, incrementation
           unary -   negation, motion, decrementation
           ────────────────────────────────────────────
                 ;   scaling
                >?   maximum
                <?   minimum
           ────────────────────────────────────────────
                 <   less than
                 >   greater than
                <=   less than or equal
                >=   greater than or equal
                 =   equal
                ==   equal
           ────────────────────────────────────────────
                 &   logical conjunction (“and”)
                 :   logical disjunction (“or”)
                 !   logical complementation (“not”)
           ────────────────────────────────────────────
               ( )   precedence
           ────────────────────────────────────────────
                 |   boundary-relative measurement

           troff provides a set of mathematical and logical operators
           familiar to programmers—as well as some unusual ones—but supports
           only integer arithmetic.  (Provision is made for interpreting and
           reporting decimal fractions in certain cases.)  The internal data
           type used for computing results depends on the host machine but is
           at least a 32-bit signed integer, which suffices to represent
           magnitudes within a range of ±2 billion.  (If that's not enough,
           see groff_tmac(5) for the 62bit.tmac macro package.)  Arithmetic
           saturates.  (If overflow would occur, GNU troff emits a warning in
           category “range”.  See section “Warnings” of troff(1).)

           Arithmetic infix operators perform a function on the numeric
           expressions to their left and right; they are + (addition), -
           (subtraction), * (multiplication), / (truncating division), and %
           (modulus).  Truncating division rounds to the integer nearer to
           zero, no matter how large the fractional portion.  Division and
           modulus by zero are errors and abort evaluation of a numeric
           expression.

           Arithmetic unary operators operate on the numeric expression to
           their right; they are - (negation) and + (assertion—for
           completeness; it does nothing).  The unary minus must often be
           used with parentheses to avoid confusion with the decrementation
           operator, discussed below.

           The sign of the modulus of operands of mixed signs is determined
           by the sign of the first.  Division and modulus operators satisfy
           the following property: given a dividend a and a divisor b, a
           quotient q formed by “(a / b)” and a remainder r by “(a % b)”,
           then qb + r = a.

           GNU troff's scaling operator, used with parentheses as (c;e),
           evaluates a numeric expression e using c as the default scaling
           unit.  If c is omitted, scaling units are ignored in the
           evaluation of e.  GNU troff also provides a pair of operators to
           compute the extremum of two operands: >? (maximum) and <?
           (minimum).

           Comparison operators comprise < (less than), > (greater than), <=
           (less than or equal), >= (greater than or equal), and = (equal,
           with a synonym ==).  When evaluating a comparison, the formatter
           replaces it with “0” if it is false and “1” if true.  In the roff
           language, positive values are true, others false.

           Operate on truth values with the logical operators & (logical
           conjunction or “and”) and : (logical disjunction or “or”).  They
           evaluate as comparison operators do.  A logical complementation
           (“not”) operator, !, works only within “if”, “ie”, and “while”
           requests.  Furthermore, the formatter recognizes ! only at the
           beginning of a numeric expression not contained by another numeric
           expression.  In other words, ! must be the “outermost” operator.
           Its presence elsewhere causes the expression to evaluate false.
           (GNU troff emits a warning in category “number”.  See section
           “Warnings” of troff(1).)  This unfortunate limitation maintains
           compatibility with AT&T troff.  Test a numeric expression for
           falsity within a complex expression by comparing it to a false
           value.

           The roff language has no operator precedence: expressions are
           evaluated strictly from left to right, in contrast to schoolhouse
           arithmetic.  Use parentheses ( ) to impose a desired precedence
           upon subexpressions.

           For many requests and escape sequences that cause motion on the
           page, the unary operators + and - work differently when leading a
           numeric expression.  They then indicate a motion relative to the
           drawing position: positive is down in vertical contexts, right in
           horizontal ones.

           + and - are also treated differently by the following requests and
           escape sequences: bp, in, ll, pl, pn, po, ps, pvs, rt, ti, \H, \R,
           and \s.  Here, leading plus and minus signs serve as
           incrementation and decrementation operators, respectively.  To
           negate an expression in these contexts, subtract it from zero or
           include the unary minus in parentheses with its argument.

           A leading | operator indicates a motion relative not to the
           drawing position but to a boundary.  For horizontal motions, the
           measurement specifies a distance relative to a drawing position
           corresponding to the beginning of the input line.  By default, tab
           stops reckon movements in this way.  Most escape sequences do not;
           | tells them to do so.  For vertical motions, the | operator
           specifies a distance from the first text baseline on the page or
           in the current diversion, using the current vertical spacing.

           The delimited escape sequence \B tests its argument for validity
           as a numeric expression.

           A register interpolated as an operand in a numeric expression must
           have an Arabic format; luckily, this is the default.

           Because spaces separate arguments to requests, spaces are not
           allowed in numeric expressions unless parentheses surround the
           (sub)expression containing them.

## [](#Identifiers)Identifiers

           An identifier labels a GNU troff datum such as a register, name
           (macro, string, or diversion), typeface, color, special character
           or character class, hyphenation language code, environment, or
           stream.  Valid identifiers consist of one or more ordinary
           characters.  An ordinary character is any Unicode Basic Latin
           character that is not a space and not the escape character; recall
           section “Input format” above.

           An identifier with a closing bracket (“]”) in its name can't be
           accessed with bracket-form escape sequences that expect an
           identifier as a parameter.  Similarly, the identifier “(” can't be
           interpolated except with bracket forms.

           Beginning a macro, string, or diversion name with the character
           “[” or “]” forecloses use of the refer(1) preprocessor, which
           recognizes input lines starting with “.[” and “.]”  as
           bibliographic reference delimiters.

           The delimited escape sequence \A tests its argument for validity
           as an identifier.

           The formatter's handling of undefined identifiers is context-
           dependent.  There is no way to invoke an undefined request; such
           syntax is interpreted as a macro call instead.  If the identifier
           is interpreted as a string, macro, or diversion name, the
           formatter defines it as empty and interpolates nothing.  (GNU
           troff emits a warning in category “mac”.  See section “Warnings”
           of troff(1).)  Similarly, if the identifier is interpreted as a
           register name, the formatter initializes it to zero and
           interpolates that value.  GNU troff emits a warning in category
           “reg”; see section “Warnings” in troff(1), and subsection
           “Interpolating registers” and section “Strings” below.  Attempting
           to use an undefined typeface, special character or character
           class, color, environment, hyphenation language code, or stream
           generally provokes an error diagnostic.

           Identifiers for requests, macros, strings, and diversions share
           one name space; special characters and character classes another.
           No other object types do.

## [](#Control_characters)Control characters

           The formatter recognizes a control character only at the beginning
           of an input line, or at the beginning of a branch of a control
           structure request; see section “Control structures” below.

           A few requests cause a break implicitly; invoke them with the no-
           break control character to prevent the break.  Break suppression
           is its sole behavioral distinction.  Employing the no-break
           control character to invoke requests that don't cause breaks is
           harmless but poor style.

           The control character “.” and the no-break control character “'”
           can be changed with the cc and c2 requests, respectively.  Within
           a macro definition, register .br indicates the control character
           used to call it.

## [](#Invoking_requests)Invoking requests

           A control character is optionally followed by tabs and/or spaces
           and then an identifier naming a request or macro.  The invocation
           of an unrecognized request is interpreted as a macro call.
           Defining a macro with the same name as a request replaces the
           request.  Deleting a request name with the rm request makes it
           unavailable.  The als request can alias requests, permitting them
           to be wrapped or non-destructively replaced.  See section
           “Strings” below.

           There is no inherent limit on argument length or quantity.  Most
           requests take one or more arguments, and ignore any they do not
           expect.  A request may be separated from its arguments by tabs or
           spaces, but only spaces can separate an argument from its
           successor.  Only one between arguments is necessary; any excess is
           ignored.  GNU troff does not allow tabs for argument separation.
           (Plan 9 troff does.)

           Generally, a space within a request argument is not relevant, not
           meaningful, or is supported by bespoke provisions, as with the tl
           request's delimiters.  Some requests, like ds, interpret the
           remainder of the control line as a single argument.  See section
           “Strings” below.

           Spaces and tabs immediately after a control character are ignored.
           Commonly, authors use them to indent the source of documents or
           macro files.

## [](#Calling_macros)Calling macros

           If a macro of the desired name does not exist when called, the
           formatter creates it and assigns it an empty definition.  (GNU
           troff emits a warning in category “mac”.  See section “Warnings”
           in troff(1).)  Calling an undefined macro does end a macro
           definition naming it as its end macro (see section “Writing
           macros” below).

           To embed spaces within a macro argument, enclose the argument in
           neutral double quotes ‘"’.  Horizontal motion escape sequences are
           sometimes a better choice for arguments to be formatted as text.

           The foregoing raises the question of how to embed neutral double
           quotes or backslashes in macro arguments when those characters are
           desired as literals.  In GNU troff, the special character escape
           sequence \[rs] produces a backslash and \[dq] a neutral double
           quote.

           In GNU troff's AT&T compatibility mode, these characters remain
           available as \(rs and \(dq, respectively.  AT&T troff did not
           consistently define these special characters, but its descendants
           can be made to support them.  See groff_font(5).  If even that is
           not feasible, see the “Calling Macros” section of the groff
           Texinfo manual for the complex macro argument quoting rules of
           AT&T troff.

## [](#Using_escape_sequences)Using escape sequences

           Whereas requests must occur on control lines, escape sequences can
           occur intermixed with text and may appear in arguments to
           requests, macros, and other escape sequences.  An escape sequence
           is introduced by the escape character, a backslash \.  The next
           character selects the escape's function.

           Escape sequences vary in length.  Some take an argument, and of
           those, some have different syntactical forms for a one-character,
           two-character, or arbitrary-length argument.  Others accept only
           an arbitrary-length argument.  In the former scheme, a one-
           character argument follows the function character immediately, an
           opening parenthesis “(” introduces a two-character argument (no
           closing parenthesis is used), and an argument of arbitrary length
           is enclosed in brackets “[]”.  In the latter scheme, the user
           selects a delimiter character.  A few escape sequences are
           idiosyncratic, and support both of the foregoing conventions (\s),
           designate their own termination sequence (\?), consume input until
           the next newline (\!, \", \#), or support an additional modifier
           character (\s again, and \n).  In no case can an escape sequence
           parameter contain an unescaped newline.

           If the character that follows the escape character does not
           identify a defined operation, the formatter ignores the escape
           character.  (GNU troff emits a warning in category “escape”.  See
           section “Warnings” in troff(1).)

           Escape sequence interpolation is of higher precedence than escape
           sequence argument interpretation.  This rule affords flexibility
           in using escape sequences to construct parameters to other escape
           sequences.

           The escape character can be interpolated (\e).  Requests permit
           the escape mechanism to be deactivated (eo) and restored, or the
           escape character changed (ec), and to save and restore it (ecs and
           ecr).

## [](#Delimiters)Delimiters

           Some escape sequences that require parameters use delimiters.  The
           neutral apostrophe ' is a popular choice and shown in this
           document.  The neutral double quote " is also commonly seen.
           Punctuation characters are the best choice (and most portable to
           other troffs, except for those meaningful in numeric expressions;
           see below.

           The following escape sequences are not themselves delimited, and
           thus are allowed as delimiters: \space, \%, \|, \^, \{, \}, \',
           \`, \-, \_, \!, \?, \), \/, \,, \&, \:, \~, \0, \a, \c, \d, \e,
           \E, \p, \r, \t, and \u.  However, we discourage using them this
           way; they can make the input confusing to read.  (The eqn(1) and
           tbl(1) preprocessors use parameterized but non-delimited special
           character escape sequences \( and \[ to bracket portions of their
           output.)  An invalid escape sequence is valid as a delimiter if
           the character after the escape character would be valid.

           The escape sequences \D, \h, \H, \l, \L, \N, \R, \s, \S, \v, and
           \x prohibit delimiters that are meaningful in numeric expressions,
           because they accept numeric expressions as (or within) their
           arguments.  For consistency, GNU troff prohibits the same
           delimiters in the argument to the tl request.  The “if”, ie, and
           “while” requests each interpret their first argument as a
           conditional expression; only characters that are not meaningful as
           operators in that context can be used as output comparison
           delimiters.  The following inputs are therefore invalid as
           delimiters in GNU troff.

                  •  the numerals 0–9 and the decimal point “.”

                  •  the (single-character) operators +-/*%<>=&:()|

                  •  any escape sequences other than \%, \:, \{, \}, \', \`,
                     \-, \_, \!, \/, \c, \e, and \p

           Delimiter syntax is flexible (and laborious to describe) primarily
           for historical reasons; the foregoing restrictions need be kept in
           mind mainly when using GNU troff in AT&T compatibility mode.
           Normally, GNU troff keeps track of the nesting depth of escape
           sequence interpolations, so the only characters you need to avoid
           using as delimiters are those that appear in the arguments you
           input, not those that result from interpolation.  Typically, '
           works fine.  See section “Implementation differences” in
           groff_diff(7).

## [](#Dummy_characters)Dummy characters

           As discussed in roff(7), the first character on an input line is
           treated specially.  Further, formatting a glyph has many
           consequences on formatter state (see section “Environments”
           below).  Occasionally, we want to escape this context or embrace
           some of those consequences without actually rendering a glyph to
           the output.  \& interpolates a dummy character, which is
           constitutive of output but invisible.  Its presence alters the
           interpretation context of a subsequent input character, and enjoys
           several applications: preventing the insertion of extra space
           after an end-of-sentence character, preventing interpretation of a
           control character at the beginning of an input line, preventing
           kerning between two glyphs, and permitting the tr request to remap
           a character to “nothing”.  \) works as \& does, except that it
           does not cancel a pending end-of-sentence state.

## [](#Page_control)Page control

           Discretionary page breaks can prevent the unwanted separation of
           content.  A new page number takes effect during page ejection; see
           subsection “The implicit page trap” below.  The bp request breaks
           the page, incrementing the page number by one (or setting it per
           the supplied argument).  The ne request forces a page break if
           insufficient vertical space is available (it asserts “needed”
           space).  sv requires vertical space as ne does, but also saves it
           for later output by the os request.

           The nl register interpolates the vertical drawing position as of
           the most recently typeset output line.  It does not necessarily
           (and often does not) represent that of the pending output line,
           because the formatter does not determine the position of its
           baseline until it is output.  Assigning a value to nl sets the
           vertical drawing position in advance of further modifications to
           baseline positioning arising from alterations to type size,
           changes to vertical spacing, or application of extra pre- or post-
           vertical spacing.

           When the formatter starts, the transition to the first page has
           not yet happened—nl is negative.  If you plant a page location
           trap at vertical position “0” (idiomatically to format a header),
           you can assign a negative value to nl to spring that trap even if
           the page has already started (see subsection “Page location traps”
           below).

## [](#Control_structures)Control structures

           groff has “if” and “while” control structures like other
           languages.  However, the syntax for grouping multiple input lines
           in the branches or bodies of these structures is unusual.

           They have a common form: the request name is (except for el
           “else”) followed by a conditional expression cond-expr; the
           remainder of the line, input, is interpreted as if it were an
           input line.  Any quantity of spaces between arguments to requests
           serves only to separate them; leading spaces in input are
           therefore not seen.  input effectively cannot be omitted; if cond-
           expr is true and input is empty, the newline at the end of the
           control line is interpreted as a blank line (and therefore a blank
           text line).

           It is frequently desirable for a control structure to govern more
           than one request, macro call, or text line, or combination of the
           foregoing.  The opening and closing brace escape sequences \{ and
           \} perform such grouping.  Brace escape sequences outside of
           control structures have no meaning and produce no output.

           \{ should appear (after optional spaces and tabs) immediately
           subsequent to the request's conditional expression.  \} should
           appear on a line with other occurrences of itself as necessary to
           match \{ sequences.  It can be preceded by a control character,
           spaces, and tabs.  Input after any quantity of \} sequences on the
           same line is processed only if all the preceding conditions to
           which they correspond are true.  Furthermore, a \} closing the
           body of a “while” request must be the last such escape sequence on
           an input line.

           GNU troff treats the body of a “while” request similarly to that
           of a de request (albeit one not read in copy mode), but stores it
           under an internal name and deletes it when the loop finishes.  The
           operation of a macro containing a “while” request can slow
           significantly if its body is large.  Each time GNU troff
           interpolates the macro, it parses and stores the “while” body
           again.  An often better solution—and one that is more portable,
           since AT&T troff lacked the “while” request—is to instead write a
           recursive macro, which is parsed only once (unless you redefine
           it).  To prevent infinite loops, GNU troff limits the default
           number of available recursion levels to 1,000 or somewhat less
           (because things other than macro calls can be on the input stack).
           You can disable this protective measure, or alter the limit, by
           setting the slimit register.  See section “Debugging” below.

       Conditional expressions
           The “if”, ie, and “while” requests test the truth values of
           numeric expressions.  They also support several additional Boolean
           operators; the members of this expanded class are termed
           conditional expressions; their truth values are as shown below.

           [1mcond-expr[24m...   ...is true if...
           ───────────────────────────────────────────────────────────────────
                's1's2'   s1 produces the same formatted output as s2.
                    c g   a character g is defined.
                    d m   a string, macro, diversion, or request m is
                          defined.
                      e   the current page number is even.
                    F f   a font named f is available.
                    m c   a color named c is defined.
                      n   the formatter is in nroff mode.
                      o   the current page number is odd.
                    r n   a register named n is defined.
                    S s   a font style named s is available.
                      t   the formatter is in troff mode.
                      v   n/a (historical artifact; always false).

           If the first argument to an “if”, ie, or “while” request begins
           with a non-alphanumeric character apart from “!” (see below) and
           is not a numeric expression, the formatter performs an output
           comparison test.  Shown first in the table above, the output
           comparison operator interpolates a true value if formatting its
           comparands s1 and s2 produces the same output commands.  Other
           delimiters can be used in place of the neutral apostrophes; see
           section “Delimiters” above.  troff formats s1 and s2 in separate
           scratch buffers; after comparison, it discards the resulting data.
           The resulting glyph properties, including font family, style,
           size, and slant, must match, but not necessarily the requests
           and/or escape sequences used to obtain them.  Motions must match
           in orientation and magnitude to within the applicable horizontal
           or vertical motion quantum of the device, after rounding.

           Surround the comparands with \? to avoid formatting them; this
           causes them to be compared character by character, as with string
           comparisons in other programming languages.  Since GNU troff reads
           comparands protected with \? in copy mode, they need not be
           syntactically valid.  The escape character is still lexically
           recognized, however, and consumes the next character.

           The above operators can't be combined with most others, but a
           leading “!”, not followed immediately by spaces or tabs,
           complements an expression.  Spaces and tabs are optional
           immediately after the “c”, “d”, “F”, “m”, “r”, and “S” operators,
           but right after “!”, they end the predicate and the conditional
           evaluates true.  (This bizarre behavior maintains compatibility
           with AT&T troff.)

           Conditional operators do not create roff language objects as
           interpolations with \n and \* escape sequences do.

## [](#Syntax_reference_conventions)Syntax reference conventions

           In the following request and escape sequence specifications, most
           argument names were chosen to be descriptive.  GNU troff reads
           arguments named character-sequence, command, contents, file, and
           message in copy mode (see section “Copy Mode” below) until the end
           of the input line.  A character-sequence comprises one or more
           ordinary, special, or indexed characters; spaces; or escape
           sequences that interpolate only these.  We name the remaining
           arguments for clarity; they are also character-sequences.  A
           neutral double quote ‘"’ can optionally prefix a character-
           sequence; the formatter discards one if present, permitting
           initial embedded spaces in the argument.  input refers to
           arbitrary character sequences (up to a newline or delimiter) that
           GNU troff fully interprets, in contrast to copy mode.

           A few denotations are more specific.

                  b          is a numerical expression evaluated as a
                             Boolean; positive values are true, others false.
                  c          denotes a single character—ordinary, special, or
                             indexed.
                  command    is an instance of contents (see below) to be
                             passed to the system as a command (potentially
                             with arguments).  GNU troff strips a leading
                             neutral double quote, allowing embedded leading
                             spaces.
                  contents   is arbitrary input, excluding an unescaped
                             newline, read in copy mode.  GNU troff strips a
                             leading neutral double quote, allowing embedded
                             leading spaces.
                  div        is a diversion identifier.
                  env        is an environment identifier.
                  file       is an instance of contents naming a file on the
                             system.  GNU troff strips a leading neutral
                             double quote, allowing embedded leading spaces.
                             GNU troff does not accept newlines (line feeds)
                             in file names supplied as arguments to requests.
                  font       is a typeface specified as a font identifier, an
                             abstract style, or a mounting position.
                  ident      is a valid groff identifier; its use often
                             indicates that the operation creates an object
                             of a type subsequently referred to as mac, reg,
                             str, and so forth.
                  mac        is a macro identifier.
                  message    is an instance of contents to emit on the
                             standard error stream.  GNU troff strips a
                             leading neutral double quote, allowing embedded
                             leading spaces.
                  n          is a numeric expression that evaluates to a non-
                             negative integer.
                  ±N         is a numeric expression with a meaning dependent
                             on its sign; see below.
                  name       is a macro, string, or diversion identifier, or
                             the name of a request.
                  npl        is a numeric expression constituting a count of
                             subsequent productive input lines; that is,
                             those that directly produce formatted output.
                             Text lines produce output, as do control lines
                             containing requests like “.tl //Page %//” or
                             escape sequences like “\l'1i'”.  Macro calls are
                             not themselves productive, but their
                             interpolations can be.
                  reg        is a register identifier.
                  str        is a string identifier.
                  stream     is an output stream identifier.

           If a numeric expression presented as ±N starts with a ‘+’ sign, an
           increment in the amount of of N is applied to the value applicable
           to the request or escape sequence.  If it starts with a ‘-’ sign,
           a decrement of magnitude N is applied instead.  Without a sign, N
           replaces any existing value.  A roff formatter always interprets a
           leading minus sign in N as a decrementation operator, not an
           algebraic sign.  To assign a register a negative value or the
           negated value of another interpolation, you must force the
           formatter to interpret “-” as a negation or minus, rather than
           decrementation, operator: enclose the “-” with its operand in
           parentheses or subtract the expression of interest from zero.  If
           a prior value does not exist—the register was undefined—an
           increment or decrement applies as if to 0.

## [](#Request_short_reference)Request short reference

           Not all details of request behavior are outlined here.  See the
           groff Texinfo manual or, for features new to GNU troff,
           groff_diff(7).

           .ab        Abort the formatter; exit with failure status.
           .ab terminal-message
                      Abort the formatter; write terminal-message to the
                      standard error stream and exit with failure status.
           .ad        Enable output line alignment and adjustment using the
                      mode stored in \n[.j].
           .ad c      Enable output line alignment and adjustment in mode c
                      (c=b,c,l,n,r).  Sets \n[.j].
           .af reg c  Assign format c to register reg, where c is “i”, “I”,
                      “a”, “A”, or a sequence of decimal digits whose
                      quantity denotes the minimum width in digits to be used
                      when the register is interpolated.  “i” and “a”
                      indicate Roman numerals and basic Latin alphabetics,
                      respectively, in the lettercase specified.  The default
                      is 0.
           .aln new-register existing-register
                      Create alias (additional name) new-register of
                      existing-register, causing the names to refer to the
                      same stored object.  If existing-register is undefined,
                      the formatter ignores the request.  GNU troff emits a
                      warning in category “reg”.
           .als new-name existing-name
                      Create alias (additional name) new-name of request,
                      string, macro, or diversion existing-name, causing the
                      names to refer to the same stored object.  If existing-
                      name is undefined, the formatter ignores the request.
                      GNU troff emits a warning in category “mac”.  If new-
                      name already exists, its definition is lost unless
                      already aliased.
           .am mac    Append to macro mac until encountering “..” at the
                      start of a control line in the current conditional
                      block.
           .am mac end-mac
                      Append to macro mac until end-mac is called at the
                      start of a control line in the current conditional
                      block.  end-mac can be a request.
           .am1 mac   As ”am”, with compatibility mode disabled when the
                      appendment to macro mac is interpreted.
           .am1 mac end-mac
                      As “.am mac”, with compatibility mode disabled when the
                      appendment to macro mac is interpreted.
           .ami str   Append to a macro indirectly—its name is in string str—
                      until encountering “..”.
           .ami str end-mac-str
                      Append to a macro indirectly.  As ”am”, but str and
                      end-mac-str contain the names of the macro to be
                      appended to, and that whose call ends the appendment,
                      respectively.
           .ami1 str  As ami, with compatibility mode disabled when the
                      appendment is interpreted.
           .ami1 str end-mac-str
                      As ami, with compatibility mode disabled when the
                      appendment is interpreted.
           .as ident  Create string ident with empty contents; no operation
                      if ident already exists.
           .as str contents
                      Append contents to string str.
           .as1 ident As “.as ident”.
           .as1 str contents
                      As ”as”, with compatibility mode disabled when the
                      appendment to string str is interpreted.
           .asciify div
                      Unformat ordinary characters, spaces, and some escape
                      sequences in diversion div.  When transforming a glyph
                      node back into an input sequence that demands
                      expression as a special character escape sequence, GNU
                      troff uses the default escape character.
           .backtrace Write the state of the input stack to the standard
                      error stream.  See the -b option of groff(1).
           .bd font   Stop emboldening font font.
           .bd font n Embolden font by overstriking its glyphs offset by n-1
                      units.  See register .b.
           .bd special-font font
                      Stop emboldening special-font when font is selected.
                      special-font must be a font name, not a mounting
                      position.
           .bd special-font font n
                      Embolden special-font, overstriking its glyphs offset
                      by n-1 units when font is selected.  See register .b.
           .blm       Unset blank line macro (trap).  Restore default
                      handling of blank lines.
           .blm mac   Set blank line macro (trap) to mac.
           .box       Stop directing output to current diversion; any pending
                      output line is discarded.
           .box ident Direct output to diversion ident, omitting a partially
                      collected line.
           .boxa      Stop appending output to current diversion; any pending
                      output line is discarded.
           .boxa div  Append output to diversion div, omitting a partially
                      collected line.
           .bp        Break page and start a new one.
           .bp ±N     Break page, starting a new one numbered ±N.
           .br        Break output line.
           .brp       Break and force adjustment of the output line per the
                      current adjustment mode.
           .break     Break out of a ”while” loop.
           .c2        Reset no-break control character to “'”.
           .c2 o      Recognize ordinary character o as no-break control
                      character.
           .cc        Reset control character to ‘.’.
           .cc o      Recognize ordinary character o as the control
                      character.
           .ce        Break, center the output of the next productive input
                      line without filling, and break again.
           .ce npl    Break, center the output of the next npl productive
                      input lines without filling, then break again.  If npl
                      ≤ 0, stop centering.
           .cf file   Break and copy contents of file as “throughput” to GNU
                      troff output (see groff_out(5)).  Each line of file is
                      output as if preceded by \!, but is not interpreted by
                      the formatter.  Unsafe request; disabled by default.
           .cflags n c...
                      Assign properties encoded by non-negative integer n to
                      each character or class c.  Spaces need not separate c
                      arguments.
           .ch mac    Unplant page location trap mac.
           .ch mac vertical-position
                      Change page location trap mac planted by wh by moving
                      its location to vertical-position (default scaling
                      unit v).
           .char c    Define an ordinary, special, or indexed character c as
                      empty.
           .char c contents
                      Define an ordinary, special, or indexed character c as
                      contents.
           .chop name Remove the last character from the macro, string, or
                      diversion name.
           .class ident c ...
                      Define a (character) class ident comprising the
                      characters or range expressions c, where each c is an
                      ordinary, special, or indexed character; or a range
                      expression.  A class thus defined can then be referred
                      to in a cflags request in lieu of listing all the
                      characters within it.
           .close stream
                      Close stream, making it unavailable for ”write”
                      requests.
           .color     Enable output of color-related device-independent
                      output commands.  It is enabled by default.
           .color b   Enable or disable output of color-related device-
                      independent output commands per Boolean expression b.
           .composite c
                      Remove composite character mapping for character c.
           .composite c1 c2
                      Map character c1 to c2 when c1 is a combining component
                      in a composite character.
           .continue  Skip the remainder of a “while” loop's body,
                      immediately retesting its conditional expression.
           .cp        Enable AT&T troff compatibility mode.  It is disabled
                      by default.
           .cp b      Enable or disable AT&T troff compatibility mode per
                      Boolean expression b.
           .cs f      Disable constant-width glyph spacing mode for font f.
           .cs f n    Enable constant-width glyph spacing mode for font f at
                      n/36 ems.
           .cs f n p  Enable constant-width glyph spacing mode for font at
                      n/36 ems, as if one em equals p scaled points.
           .cu        Continuously underline the output of the next
                      productive input line.
           .cu npl    Continuously underline the output of the next npl
                      productive input lines.  If npl=0, stop continuously
                      underlining.
           .da        Stop appending output to current diversion.
           .da div    Append output to diversion div.
           .de ident  Define macro ident until “..” occurs at the start of a
                      control line in the current conditional block.
           .de ident end-mac
                      Define macro ident until end-mac is called at the start
                      of a control line in the current conditional block.
                      end-mac can be a request.
           .de1 ident As de, with compatibility mode disabled when mac is
                      interpreted.
           .de1 ident end-mac
                      As “.de ident end-mac”, with compatibility mode
                      disabled when mac is interpreted.
           .defcolor ident scheme color-component ...
                      Define a color named ident.  scheme identifies a color
                      space and determines the number of required color-
                      components; it must be one of “rgb” (three components),
                      “cmy” (three), “cmyk” (four), or “gray” (one).  “grey”
                      is accepted as a synonym of “gray”.  The color
                      components can be encoded as a single hexadecimal value
                      starting with # or ##.  The former indicates that each
                      component is in the range 0–255 (0–FF), the latter the
                      range 0–65,535 (0–FFFF).  Alternatively, each color
                      component can be specified as a decimal fraction in the
                      range 0–1, interpreted using a default scaling unit
                      of “f”, which multiplies its value by 65,536 (but
                      clamps it at 65,535).
           .dei str   Define macro indirectly.  As de, but interpolate string
                      str to obtain the macro's name.
           .dei str end-mac-str
                      Define macro indirectly.  As de, but str and end-mac-
                      str contain the names of the macro to be defined, and
                      that whose call ends the definition, respectively.
           .dei1 str  As dei, with compatibility mode disabled when the macro
                      is interpreted.
           .dei1 str end-mac-str
                      As dei, with compatibility mode disabled when the macro
                      is interpreted.
           .device character-sequence
                      Embed character-sequence into GNU troff output as
                      parameters to an “xX” device extension command; see
                      groff_out(5).  The output driver or other postprocessor
                      interprets character-sequence as it sees fit.
           .devicem name
                      Write contents of macro or string name to troff output
                      as the argument to a device extension command.
           .di        Stop directing output to current diversion.
           .di ident  Direct output to diversion ident.
           .do name argument ...
                      Interpret the string, request, diversion, or macro name
                      (along with any further arguments) with compatibility
                      mode disabled.  Compatibility mode is restored (only if
                      it was active) when the interpolation of name is
                      interpreted.
           .ds ident  Create empty string named ident.
           .ds ident contents
                      Create a string named ident containing contents.
           .ds1 ident
           .ds1 ident contents
                      As ds, with compatibility mode disabled when the string
                      is interpreted.
           .dt        Clear diversion trap.
           .dt vertical-position mac
                      Set the diversion trap to macro mac at vertical-
                      position (default scaling unit v).
           .ec        Recognize \ as the escape character.
           .ec o      Recognize ordinary character o as the escape character.
           .ecr       Restore escape character saved with ecs.
           .ecs       Save the escape character.
           .el        Interpolate a newline if the conditional expression of
                      the corresponding ie request was false.
           .el input  Interpret input as if it were an input line if the
                      conditional expression of the corresponding ie request
                      was false.
           .em        Unset end-of-input macro.
           .em mac    Call macro mac after the end of input.
           .eo        Disable the escape mechanism in interpretation mode.
           .ev        Pop environment stack, returning to previous one.
           .ev env    Push current environment onto stack and switch to env,
                      creating it if necessary.
           .evc env   Copy environment env to the current one.
           .ex        Exit the formatter.
           .fam       Set default font family to previous value.
           .fam name  Set default font family to name.
           .fc        Disable field mechanism.
           .fc c      Set field delimiter to c and pad glyph to space.
           .fc c1 c2  Set field delimiter to c1 and pad glyph to c2.
           .fchar c   Define fallback character c as empty.
           .fchar c contents
                      Define fallback character c as contents.  As char, but
                      while that request hides a glyph with the same name in
                      the selected font, fchar definitions are used only if
                      the font lacks a glyph for c.  GNU troff performs this
                      test before searching special fonts.
           .fcolor    Restore previous fill color, or the default if there is
                      none.
           .fcolor col
                      Select col as the fill color.
           .fi        Enable filling of output lines; a pending output line
                      is broken.  Sets \n[.u].
           .fl        Flush any pending output line.
           .fp pos id Mount font with font description file name id at non-
                      negative position pos.
           .fp pos id font-description-file-name
                      Mount font with font-description-file-name as name id
                      at non-negative position pos.
           .fschar f c
                      Define fallback character c specific to font f as
                      empty.
           .fschar f c contents
                      Define fallback character c specific to font f as
                      contents.  As char, but GNU troff locates a character
                      defined by fschar after any fonts named as arguments to
                      the fspecial are searched and before those named as
                      arguments to the “special” request.
           .fspecial f
                      Empty the list of fonts treated as special when f is
                      selected.
           .fspecial f s ...
                      Declare each font s as special only when font f is
                      selected.  GNU troff searches fonts specified as
                      arguments to the “special” request after those given as
                      arguments to the fspecial request.
           .ft
           .ft P      Select the typeface font.  If font is an integer, the
                      formatter interprets it as a mounting position; the
                      font mounted there is selected.  If that position
                      refers to an abstract style, GNU troff combines it with
                      the default family (see fam above and \F below) to make
                      a resolved font name.  If font is “DESC”, if the
                      mounting position is not an abstract style and no font
                      is mounted there, or the mounting position is negative,
                      GNU troff ignores the request.  (It also emits a
                      warning in category “font”, or “range”, as appropriate.
                      See section “Warnings” in troff(1).)  Also see \f .
           .ftr f     Remove translation of font named f.
           .ftr f1 f2 Translate font name f1 to f2.
           .fzoom font 0
                      Stop magnifying font.
           .fzoom font zoom
                      Set magnification of mounted font to zoom, a multiplier
                      of the current type size in thousandths (default:
                      1000).
           .gcolor    Restore previous stroke color, or the default if there
                      is none.
           .gcolor col
                      Select col as the stroke color.
           .hc        Reset the hyphenation character to \% (the default).
           .hc c      Change the hyphenation character to c.
           .hcode dst1 src1 [dst2 src2] ...
                      Set the hyphenation code of character dst1 to that of
                      src1, and so on.
           .hla       Clear the environment's hyphenation language (disabling
                      automatic hyphenation).
           .hla ident Set the environment's hyphenation language to ident.
           .hlm       Set the consecutive automatically hyphenated line limit
                      to -1 (the default), meaning “no limit”.
           .hlm n     Set the consecutive automatically hyphenated line limit
                      to to n.  A negative value means “no limit”.
           .hpf file  Read hyphenation patterns from file.
           .hpfa file Append hyphenation patterns from file.
           .hpfcode a b [c d] ...
                      Caution: This request will be withdrawn in a future
                      groff release.  Use hcode instead.
                      Define mappings for character codes in hyphenation
                      pattern files.
           .hw word ...
                      Define each argument word (comprising ordinary,
                      special, or indexed characters) as a hyphenation
                      exception word such that each occurrence of a hyphen-
                      minus “-” in word indicates a hyphenation point.
           .hy        Set automatic hyphenation mode to the value of the
                      .hydefault register.
           .hy 0      Disable automatic hyphenation; same as .nh.
           .hy mode   Set automatic hyphenation mode to mode; see section
                      “Hyphenation” below.
           .hydefault mode
                      Set hyphenation mode default to mode; see section
                      “Hyphenation” below.
           .hym       Set the (right) hyphenation margin to 0 (the default).
           .hym length
                      Set the (right) hyphenation margin to length (default
                      scaling unit m).
           .hys       Set the hyphenation space to 0 (the default).
           .hys hyphenation-space
                      Suppress automatic hyphenation in adjustment modes “b”
                      or “n” if that adjustment can be achieved by adding no
                      more than hyphenation-space to each inter-word space
                      (default scaling unit m).
           .ie cond-expr
                      Interpolate a newline if cond-expr is true, otherwise
                      skip to a corresponding el request.
           .ie cond-expr input
                      If cond-expr is true, interpret input as if it were an
                      input line, otherwise skip to a corresponding el
                      request.
           .if cond-expr
                      Interpolate a newline if cond-expr is true.
           .if cond-expr input
                      If cond-expr is true, then interpret input as if it
                      were an input line.
           .ig        Ignore input (except for side effects of \R on auto-
                      incrementing registers) until “..” occurs at the start
                      of a control line in the current conditional block.
           .ig end-mac
                      Ignore input (except for side effects of \R on auto-
                      incrementing registers) until end-mac is called at the
                      start of a control line in the current conditional
                      block.  end-mac can be a request.
           .in        Set indentation amount to previous value.
           .in ±N     Set indentation to ±N (default scaling unit m).
           .it        Cancel any pending input line trap.
           .it npl mac
                      Set (or replace) an input line trap in the environment,
                      calling mac after the next npl productive input lines
                      have been read.  Lines interrupted with the \c escape
                      sequence are counted separately.
           .itc       Cancel any pending input line trap.
           .itc npl mac
                      As ”it”, but lines interrupted with the \c escape
                      sequence do not apply to the line count.
           .kern      Enable pairwise kerning.
           .kern b    Enable or disable pairwise kerning per Boolean
                      expression b.
           .lc        Unset leader repetition character.
           .lc c      Set leader repetition character to c (default: “.”).
           .length reg contents
                      Compute the number of characters in contents and store
                      the count in the register reg.
           .linetabs  Activate line-tabs in the environment.  It is disabled
                      by default.
           .linetabs b
                      Activate or deactivate line-tabs in the environment per
                      Boolean expression b.
           .lf input-line-number
                      Set the input line number the formatter uses when
                      reporting diagnostics.  The argument becomes the input
                      line number of the next line the formatter reads.
           .lf input-line-number character-sequence
                      As lf with one argument, but also update the reported
                      file name to character-sequence.
           .lg        Enable ligature mode 1.
           .lg m      Set ligature mode to m (0 = disable, 1 = enable, 2 =
                      enable for two-letter ligatures only).
           .ll        Set line length to previous value.  Does not affect a
                      pending output line.
           .ll ±N     Set line length to ±N (default length 6.5i, default
                      scaling unit m).  Does not affect a pending output
                      line.
           .lsm       Unset the leading space macro (trap).  Restore default
                      handling of lines with leading spaces.
           .lsm mac   Set the leading space macro (trap) to mac.
           .ls        Change to the previous value of additional intra-line
                      skip.
           .ls n      Set additional intra-line skip value to n, i.e., n-1
                      blank lines are inserted after each text output line.
           .lt        Set length of title lines to previous value.
           .lt ±N     Set length of title lines (default length 6.5i, default
                      scaling unit m).
           .mc        Cease writing margin character.
           .mc c      Begin writing margin character c to the right of each
                      output line at a distance of 10p.
           .mc c d    Begin writing margin character c on each output line at
                      distance d to the right of the right margin (default
                      distance 10p, default scaling unit m).
           .mk        Mark vertical drawing position in an internal register;
                      see .rt.
           .mk reg    Mark vertical drawing position in register reg.
           .mso file  As ”so”, except that GNU troff searches for the
                      specified file in the same directories as macro files;
                      see GROFF_TMAC_PATH in section “Environment” of
                      groff(1) and -m in section “Options” of the same page.
           .msoquiet file
                      As mso, but no warning is emitted if file does not
                      exist.
           .na        Disable output line adjustment.
           .ne        Break page if distance to next page location trap is
                      less than one vee.
           .ne d      Break page if distance to next page location trap is
                      less than distance d (default scaling unit v).
           .nf        Disable filling of output lines; a pending output line
                      is broken.  Clears \n[.u].
           .nh        Disable automatic hyphenation; same as “.hy 0”.
           .nm        Deactivate output line numbering.
           .nm ±N
           .nm ±N m
           .nm ±N m s
           .nm ±N m s i
                      Activate output line numbering: number the next output
                      line ±N, writing numbers every m lines (default 1),
                      with s numeral widths (\0) between the line number and
                      the output (default 1), and indenting the line number
                      by i numeral widths (default 0).
           .nn        Suppress numbering of the next output line counted by
                      nm.
           .nn n      Suppress numbering of the next n output lines counted
                      by nm.  If n=0, cancel suppression.
           .nop       Interpolate a newline.
           .nop input Interpret input as if it were an input line.
           .nr reg ±N Define or update register reg with value N.
           .nr reg ±N I
                      Define or update register reg with value N and auto-
                      increment I, which may be any integer.
           .nroff     Make the conditional expressions n true and t false.
           .ns        Enable no-space mode, ignoring .sp requests until a
                      glyph or \D primitive is output.  See .rs.
           .nx        Stop processing the input file and read the next, if
                      any.
           .nx file   Stop processing the input file and read file.
           .open ident file
                      Open file for writing and associate a stream named
                      ident with it, making it available for ”write”
                      requests.  Unsafe request; disabled by default.
           .opena ident file
                      As “open”, but if file already exists, appends to it
                      instead of overwriting it.  Unsafe request; disabled by
                      default.
           .os        Output vertical space that was saved by the sv request.
           .output character-sequence
                      Emit character-sequence “transparently” (directly) to
                      troff's output.
           .pc        Reset page number character to ‘%’.
           .pc c      Change the page number character used in titles to c.
           .pchar c ...
                      Report, to the standard error stream, information about
                      each character (be it ordinary, special, or indexed) or
                      character class c.  A character defined by a request
                      (char, fchar, fschar, or schar) reports its contents as
                      a JSON-encoded string, but the output is not otherwise
                      in JSON format.
           .pcolor    Report, to the standard error stream, each defined
                      color name, its color space identifier, and channel
                      value assignments.  A device's default stroke and/or
                      fill colors, “default”, are not listed since they are
                      immutable and their details unknown to the formatter.
           .pcolor col ...
                      Report, to the standard error stream, the name, color
                      space identifier, and channel value assignments of each
                      color col.
           .pcomposite
                      Report, to the standard error stream, the list of
                      configured composite character mappings.  See the
                      “composite” request.  The “from” code point is listed
                      first, followed by its “to” mapping.
           .pev       Report the state of the current environment followed by
                      that of all other environments to the standard error
                      stream.
           .pfp       Report, to the standard error stream, the list of
                      occupied font mounting positions.  Occupied mounting
                      positions are listed, one per line, in increasing
                      order, followed by the typeface name; if the name
                      corresponds to an abstract style, the entry ends there.
                      Otherwise, the name of the font description file and
                      the font's “internal name” datum, the meaning of which
                      varies by output device, follow.
           .pftr      Report, to the standard error stream, the list of font
                      translations.
           .phw       Report, to the standard error stream, the list of
                      hyphenation exception words associated with the
                      hyphenation language selected by the hla request.  A
                      “-” marks each hyphenation point.  A word prefixed with
                      “-” is not hyphenated at all.  The report suffixes
                      words to which automatic hyphenation applies (meaning
                      those defined in a hyphenation pattern file rather than
                      with the hw request) with a tab and asterisk “*”.
           .pi command
                      Pipe GNU troff output through command (which is read in
                      copy mode) by passing it to popen(3).  Multiple pi
                      requests construct a multi-stage pipeline in the same
                      order as the formatter encounters the requests.  Unsafe
                      request; disabled by default.
           .pl        Set page length to default 11i.  The current page
                      length is stored in register .p.
           .pl ±N     Change page length to ±N (default scaling unit v).
           .pline     Report, in JSON syntax to the standard error stream,
                      the list of output nodes corresponding to the pending
                      output line.  In JSON, a pair of empty brackets “[ ]”
                      represents an empty list.  A pending output line has
                      not yet undergone adjustment, and lacks a line number
                      and margin character (all as applicable).
           .pm        Report, to the standard error stream, the names of all
                      defined macros, strings, and diversions and their
                      lengths in characters or nodes.
           .pm name ...
                      Report, to the standard error stream, the JSON-encoded
                      name and contents of each macro, string, or diversion
                      name.
           .pn ±N     Set next page number.
           .pnr       Report the names, values, and (as applicable)
                      autoincrement amounts and assigned formats of all
                      defined registers to the standard error stream.
           .pnr reg ...
                      Report the name and value and, if its type is numeric,
                      the autoincrement amount and assigned format, of each
                      register reg to the standard error stream.
           .po        Change to previous page offset.  The current page
                      offset is available in register .o.
           .po ±N     Alter page offset (default scaling unit m).
           .ps        Restore previous type size.
           .ps ±N     Set/increase/decrease the type size to/by N scaled
                      points (a non-positive resulting type size is set to
                      1 u); also see \s[±N].
           .psbb postscript-file
                      Retrieve the bounding box of the PostScript image found
                      in postscript-file, which must conform to Adobe's
                      Document Structuring Conventions (DSC).  See registers
                      llx, lly, urx, ury.
           .pso command
                      As “so”, except that input comes from the standard
                      output stream of command, which is passed to popen(3).
                      Unsafe request; disabled by default.
           .pstream   Report, in JSON syntax to the standard error stream,
                      the list of open streams, including the name of each
                      open stream, the name of the file backing it, and its
                      mode (writing or appending).
           .pwh       Report names and positions of all page location traps
                      to the standard error stream.
           .pvs       Change to previous post-vertical line spacing.
           .pvs ±N    Change post-vertical line spacing according to ±N
                      (default scaling unit p).
           .rchar c...
                      Remove definition of each ordinary, special, or indexed
                      character c, undoing the effect of a char, fchar, or
                      schar request.  Spaces need not separate c arguments.
                      The character definition removed (if any) is the first
                      encountered in the resolution process documented in
                      section “Using Symbols” of Groff: The GNU
                      Implementation of troff.  Glyphs, which are defined by
                      font description files, cannot be removed.
           .rd        Read insertion from standard input stream, ringing
                      terminal bell as prompt.
           .rd terminal-message
                      Read insertion from standard input stream, writing
                      terminal-message to standard error stream as prompt.
           .return    Stop interpreting an interpolated macro, skipping the
                      remainder of its definition.
           .return input
                      As return, but perform the skip twice—once within the
                      macro being interpreted and once in an enclosing macro.
           .rfschar f c...
                      Remove each fallback special character c for font f.
                      Spaces need not separate c arguments.  See fschar.
           .rj        Break, right-align the output of the next productive
                      input line without filling, then break again.
           .rj npl    Break, right-align the output of the next npl
                      productive input lines without filling, then break
                      again.  If npl ≤ 0, stop right-aligning.
           .rm name ...
                      Remove each request, macro, diversion, or string name.
           .rn old new
                      Rename request, macro, diversion, or string old to new.
           .rnn reg1 reg2
                      Rename register reg1 to reg2.
           .rr reg ...
                      Remove each register reg.
           .rs        Restore spacing; disable no-space mode.  See .ns.
           .rt        Return (upward only) to vertical position marked by .mk
                      on the current page.
           .rt N      Return (upward only) to vertical position N (default
                      scaling unit v).
           .schar c   Define global fallback character c as empty.
           .schar c contents
                      Define global fallback character c as contents.  As
                      char, but GNU troff locates a character defined with
                      schar after any fonts named as arguments to the
                      “special” request and before any mounted special fonts.
           .shc       Reset the soft hyphen character to \[hy].
           .shc c     Set the soft hyphen character to c.
           .shift     Shift macro or string parameters one place n places:
                      argument i becomes argument i-1; argument 1 becomes
                      unavailable.
           .shift n   Shift macro or string parameters n places: argument i
                      becomes argument i-n; arguments 1 to n become
                      unavailable.
           .sizes s1 s2 ... sn [0]
                      Set available type sizes to the list of values or
                      ranges; each si is interpreted in units of scaled
                      points (s).  GNU troff strips a leading neutral double
                      quote from s1; it reads each si in copy mode.
           .so file   Replace the request's control line with the contents of
                      file, “sourcing” it.  GNU troff searches for file in
                      any directories specified by -I command-line options,
                      followed by the current working directory.  If file
                      does not exist, the formatter ignores the request.
                      (GNU troff emits a warning in category “file”.)
           .soquiet file
                      As ”so”, but no warning is emitted if file does not
                      exist.
           .sp        Break and move the next text baseline down by one vee,
                      or until springing a page location trap.  If invoked
                      with the no-break control character, sp moves the text
                      baseline applicable to the entire pending output line.
           .sp vertical-distance
                      As sp, but move by vertical-distance instead of 1v.
                      Inside a diversion, the formatter ignores any argument.
                      A negative vertical-distance cannot reduce the position
                      of the text baseline below zero.  Applying the
                      boundary-relative measurement operator | operator to
                      vertical-distance, as in “|N”, moves to a position
                      relative to the page top for positive N, and the bottom
                      if N is negative.
           .special   Empty the list of special fonts designated by this
                      request when given arguments.
           .special s ...
                      Declare each font s as special, irrespective of its
                      description file, populating a list that GNU troff
                      searches, in order, to find the glyph demanded.  GNU
                      troff searches fonts specified as arguments to the
                      “special” request after those given as arguments to the
                      fspecial request.
           .spreadwarn
                      Toggle the spread warning on and off (the default)
                      without changing its value.
           .spreadwarn N
                      Emit a break warning if the additional space inserted
                      for each space between words in an adjusted output line
                      is greater than or equal to N.  A negative N is treated
                      as 0.  The default scaling unit is m.  At startup,
                      spreadwarn is inactive and N is 3 m.
           .ss n      Set minimum inter-word space and supplemental inter-
                      sentence space sizes to n 12ths of the selected font's
                      spacewidth parameter (default: 12).
           .ss n m    As “.ss n”, but set supplemental inter-sentence space
                      size to m 12ths of the selected font's spacewidth
                      parameter.
           .stringdown str
                      Replace each byte in the string named str with its
                      lowercase version.
           .stringup str
                      Replace each byte in the string named str with its
                      uppercase version.
           .sty pos style
                      Associate abstract style with non-negative font
                      position pos.
           .substring str start [end]
                      Replace the string named str with its substring bounded
                      by the indices start and end, inclusive.  Negative
                      indices count backward from the end of the string.
           .sv        As ne, but save 1 v for output with os request.
           .sv d      As ne, but save distance d for later output with os
                      request (default scaling unit v).
           .sy command
                      Execute command (which is read in copy mode) in the
                      operating environment by passing it to system(3).  See
                      register systat.  Unsafe request; disabled by default.
           .ta        Clear tab stops.
           .ta n1 n2 ... nn T r1 r2 ... rn
                      Set tabs at positions n1, n2, ..., nn, then set tabs at
                      nn+m×rn+r1 through nn+m×rn+rn, where m increments from
                      0, 1, 2, ... to the output line length.  Each
                      n argument can be prefixed with a “+” to place the tab
                      stop ni at a distance relative to the previous, n(i-1).
                      Each argument ni or ri can be suffixed with a letter to
                      align text within the tab column bounded by tab stops
                      i and i+1; “L” for left-aligned (the default), “C” for
                      centered, and “R” for right-aligned.
           .tag       Reserved for internal use.
           .taga      Reserved for internal use.
           .tc        Unset tab repetition character.
           .tc c      Set tab repetition character to c (default: none).
           .ti ±N     Temporarily indent next output line (default scaling
                      unit m).
           .tkf font s1 n1 s2 n2
                      Enable track kerning for font.
           .tl 'left'center'right'
                      Format three-part title.
           .tm        Write a newline to the standard error stream.
           .tm terminal-message
                      Send terminal-message, followed by a newline, to the
                      standard error stream.  The formatter reads the
                      argument to the end of the input line in copy mode, but
                      does not remove a leading double quote; contrast .tm1.
           .tm1       As tm.
           .tm1 message
                      As tm, but removes a leading neutral double quote ‘"’
                      from message, permitting initial embedded spaces in it,
                      and reads it to the end of the input line in copy mode.
           .tmc       No operation.
           .tmc message
                      As tm1, but does not append a newline.
           .tr abcd...
                      Translate ordinary or special characters a to b, c to
                      d, and so on prior to output.
           .trf file  Break and copy contents of file as “throughput” to GNU
                      troff output (see groff_out(5)).  Unlike cf, characters
                      invalid as input to GNU troff are discarded.  If file's
                      contents do not end with a newline, trf appends one.
           .trin abcd...
                      As tr, except that asciify ignores the translation when
                      a diversion is interpolated.
           .trnt abcd...
                      As tr, except that translations are suppressed in the
                      argument to \!.
           .troff     Make the conditional expressions t true and n false.
           .uf font   Set underline font used by ul to font.
           .ul        Underline (italicize in troff mode) the output of the
                      next productive input line.
           .ul npl    Underline (italicize in troff mode) the output of the
                      next npl productive input line.  If npl=0, stop
                      underlining.
           .unformat div
                      Unformat space characters and tabs in diversion div,
                      preserving font information.
           .vpt       Enable vertical position traps.  They are enabled by
                      default.
           .vpt b     Enable or disable vertical position traps per Boolean
                      expression b.
           .vs        Change to previous vertical spacing.
           .vs ±N     Set vertical spacing to ±N (default scaling unit p).
           .warn      Enable all warning categories.
           .warn 0    Disable all warning categories.
           .warn n    Enable warnings in categories whose codes sum to n; see
                      troff(1).
           .warnscale scaling-unit
                      Select scaling unit used in certain warnings (one of u,
                      i, c, p, or P; default: i).  Ignored on nroff-mode
                      output devices, for which these diagnostics report the
                      vertical page location in lines, and the horizontal
                      page location in ens.
           .wh vertical-position
                      Remove visible page location trap at vertical-position
                      (default scaling unit v).
           .wh vertical-position mac
                      Plant macro mac as page location trap at vertical-
                      position (default scaling unit v), removing any visible
                      trap already there.
           .while cond-expr
                      Interpolate newlines unless and until cond-expr
                      evaluates false.
           .while cond-expr input
                      Repeatedly execute input unless and until cond-expr
                      evaluates false.
           .write stream character-sequence
                      Write character-sequence, a sequence of ordinary
                      characters, spaces, or tabs, to stream, which must
                      previously have been the subject of an “open” (or
                      opena) request, followed by a newline.  GNU troff
                      flushes the stream after writing to it.
           .writec stream character-sequence
                      As ”write”, but does not write a newline to the output.
           .writem stream name
                      Write the contents of the macro or string name to
                      stream, which must previously have been the subject of
                      an “open” (or opena) request.  GNU troff reads the
                      contents of name in copy mode.

## [](#Escape_sequence_short_reference)Escape sequence short reference

           The escape sequences \", \#, \$, \*, \?, \a, \e, \n, \t, \g, \V,
           and \newline are interpreted even in copy mode.

           The escape sequences \f, \F, \H, \m, \M, \R, \s, and \S are not
           tokenized when GNU troff reads its input.  \R updates only the
           formatter's register dictionary, and does not contribute
           (directly) to output.  The others alter the environment (see
           section “Environments” below).  See the “GNU troff Internals”
           section of the groff Texinfo manual.

           \"     Comment; read everything up to the next newline in copy
                  mode and discard it.
           \#     Whole-line comment; read everything up to and including the
                  next newline in copy mode and discard it.
           \*s    Interpolate string with one-character name s.
           \*(st  Interpolate string with two-character name st.
           \*[string]
                  Interpolate string with name string (of arbitrary length).
           \*[string arg ...]
                  Interpolate string with name string (of arbitrary length),
                  taking arg ... as arguments.
           \$0    Interpolate name by which currently executing macro was
                  invoked.
           \$n    Interpolate macro or string parameter numbered n (1≤n≤9).
           \$(nn  Interpolate macro or string parameter numbered nn
                  (01≤nn≤99).
           \$[nnn]
                  Interpolate macro or string parameter numbered nnn (nnn≥1).
           \$*    Interpolate catenation of all macro or string parameters,
                  separated by spaces.
           \$@    Interpolate catenation of all macro or string parameters,
                  with each surrounded by double quotes and separated by
                  spaces.
           \$^    Interpolate catenation of all macro or string parameters as
                  if they were arguments to the ds request.
           \'     is a synonym for \[aa], the acute accent special character.
           \`     is a synonym for \[ga], the grave accent special character.
           \-     is a synonym for \[-], the minus sign special character.
           \_     is a synonym for \[ul], the underrule special character.
           \%     Mark a hyphenation point within a word.  At the beginning
                  of a word, prevent it from being otherwise hyphenated.
           \!character-sequence
                  Transparently embed character-sequence, up to and including
                  the end of the line, into the current diversion, requests,
                  macro calls, and escape sequences when reading them into a
                  diversion.  Doing so prevents them from taking effect until
                  the diverted text is actually output.
           \?character-sequence\?
                  Transparently embed character-sequence, up to its own next
                  occurrence on the input line, into a diversion, or
                  unformatted as an output comparand in a conditional
                  expression.  Ignored in the top-level diversion.
           \space Move right one inter-word space.
           \~     Insert an unbreakable, adjustable space.
           \0     Move right by the width of a numeral in the current font.
           \|     Move one-sixth em to the right on typesetters.
           \^     Move one-twelfth em to the right on typesetters.
           \&     Interpolate a dummy character.
           \)     Interpolate a dummy character that is transparent to end-
                  of-sentence recognition.
           \/     Apply italic correction.  Use between an immediately
                  adjacent oblique glyph on the left and an upright glyph on
                  the right.
           \,     Apply left italic correction.  Use between an immediately
                  adjacent upright glyph on the left and an oblique glyph on
                  the right.
           \:     Non-printing break point (similar to \%, but never produces
                  a hyphen glyph).
           \newline
                  Continue current input line on the next.
           \{     Begin conditional input.
           \}     End conditional input.
           \(sc   Interpolate glyph of special character with two-character
                  identifier sc.
           \[spchar]
                  Interpolate glyph of special character with identifier
                  spchar (of arbitrary length).
           \[base-char comp ...]
                  Interpolate composite glyph constructed from base-char and
                  each component comp.
           \[charnnn]
                  Interpolate glyph of eight-bit encoded character nnn, where
                  0≤nnn≤255.
           \[unnnn[n[n]]]
                  Interpolate glyph of Unicode character with code point
                  nnnn[n[n]] in uppercase hexadecimal.
           \[ubase-char[_combining-component]...]
                  Interpolate composite glyph from Unicode character base-
                  char and combining-components.
           \a     Interpolate a leader in copy mode.
           \A'input'
                  Interpolate 1 if input is a valid identifier, and 0
                  otherwise.  Because GNU troff ignores any input character
                  with an invalid code when reading it, invalid identifiers
                  are empty or contain spaces, tabs, newlines, or escape
                  sequences that interpolate something other than a sequence
                  of ordinary characters.
           \b'string'
                  Build bracket: pile a sequence of glyphs corresponding to
                  each character in string vertically, and center it
                  vertically on the output line.
           \B'input'
                  Interpolate 1 if input is a valid numeric expression, and 0
                  otherwise.
           \c     Continue output line at next input line.
           \C'glyph'
                  As \[glyph], but compatible with other troff
                  implementations.
           \d     Move downward ½ em on typesetters.
           \D'drawing-command'
                  See subsection “Drawing commands” below.
           \e     Interpolate the escape character.
           \E     As \e, but not interpreted in copy mode.
           \fP    Select previous font mounting position (abstract style or
                  font); same as “.ft” or “.ft P”.
           \fF    Select font mounting position, abstract style, or font with
                  one-character name or one-digit position F.  F cannot be P.
           \f(ft  Select font mounting position, abstract style, or font with
                  two-character name or two-digit position ft.
           \f[font]
                  Select font mounting position, abstract style, or font with
                  arbitrarily long name or position font.  font cannot be P.
           \f[]   Select previous font mounting position (abstract style or
                  font).
           \Ff    Set default font family to that with one-character name f.
           \F(fm  Set default font family to that with two-character name fm.
           \F[fam]
                  Set default font family to that with arbitrarily long name
                  fam.
           \F[]   Set default font family to previous value.
           \gr    Interpolate format of register with one-character name r.
           \g(rg  Interpolate format of register with two-character name rg.
           \g[reg]
                  Interpolate format of register with arbitrarily long name
                  reg.
           \h'N'  Horizontally move the drawing position by N ems (or
                  specified units); | may be used.  Positive motion is
                  rightward.
           \H'N'  Set (increment, decrement) the height of the current font,
                  but not its width.  If N is zero, the formatter uses the
                  font's inherent height for its type size default scaling
                  unit z).
           \kr    Store the horizontal drawing position, relative to that
                  corresponding to the start of the input line (ignoring page
                  offset and indentation), in register name r.
           \k(rg  Store the horizontal drawing position, relative to that
                  corresponding to the start of the input line (ignoring page
                  offset and indentation), in register name rg.
           \k[reg]
                  Store the horizontal drawing position, relative to that
                  corresponding to the start of the input line (ignoring page
                  offset and indentation), in register name reg.
           \l'N[c]'
                  Draw horizontal line of length N with character c (default:
                  \[ru]; default scaling unit m).
           \L'N[c]'
                  Draw vertical line of length N with character c (default:
                  \[br]; default scaling unit v).
           \mc    Select stroke color with one-character name c.
           \m(cl  Select stroke color with two-character name cl.
           \m[color]
                  Select stroke color with arbitrarily long name color.
           \m[]   Restore previous stroke color.
           \Mc    Select fill color with one-character name c.
           \M(cl  Select fill color with two-character name cl.
           \M[color]
                  Select fill color with arbitrarily long name color.
           \M[]   Restore previous fill color.
           \nr    Interpolate value of register with one-character name r.
           \n(rg  Interpolate value of register with two-character name rg.
           \n[reg]
                  Interpolate value of register with arbitrarily long
                  name reg.
           \N'n'  Format indexed character numbered n in the current font.
           \o'abc...'
                  Overstrike centered glyphs of characters a, b, c, and so
                  on.
           \O0    At the outermost suppression level, disable emission of
                  glyphs and geometric objects to the output driver.
           \O1    At the outermost suppression level, enable emission of
                  glyphs and geometric objects to the output driver.
           \O2    At the outermost suppression level, enable glyph and
                  geometric primitive emission to the output driver and write
                  to the standard error stream the page number, four bounding
                  box registers enclosing glyphs written since the previous
                  \O escape sequence, the page offset, line length, image
                  file name (if any), horizontal and vertical device motion
                  quanta, and input file name.
           \O3    Begin a nested suppression level.
           \O4    End a nested suppression level.
           \O[5Pfile]
                  At the outermost suppression level, write the name file to
                  the standard error stream at position P, which must be one
                  of l, r, c, or i.
           \p     Break output line at next word boundary; adjust if
                  applicable.
           \r     Move “in reverse” (upward) 1 em.
           \R'name ±N'
                  Set, increment, or decrement register name by N.
           \s±N   Set/increase/decrease the type size to/by N scaled points.
                  N must be a single digit.  If n is an unsigned “0”, restore
                  the previous size.  (In compatibility mode only, a non-zero
                  N must be in the range 4–39.)  Otherwise, as ps request.
           \s(±N
           \s±(N  Set/increase/decrease the type size to/by N scaled points;
                  N is a two-digit number ≥1.  If n is an unsigned “00”,
                  restore the previous size.  Otherwise, as ps request.
           \s[±N]
           \s±[N]
           \s'±N'
           \s±'N' Set/increase/decrease the type size to/by N scaled points.
                  If n is an unsigned “0” (with any number of leading
                  zeroes), restore the previous size.  Otherwise, as ps
                  request.
           \S'N'  Slant the glyphs of the currently selected font by @var{N}
                  degrees.  Positive values slant in the direction of text
                  flow.  Only integer values are possible.
           \t     Interpolate a tab in copy mode.
           \u     Move upward ½ em on typesetters.
           \v'N'  Vertically move the drawing position by N vees (or
                  specified units); | may be used.  Positive motion is
                  downward.
           \Ve    Interpolate value of system environment variable with one-
                  character name e as returned by getenv(3).
           \V(ev  Interpolate value of system environment variable with two-
                  character name ev as returned by getenv(3).
           \V[env]
                  Interpolate value of system environment variable with
                  arbitrarily long name env as returned by getenv(3).
           \w'input'
                  Interpolate the width of input, as interpreted, in basic
                  units.  This escape sequence allows several properties of
                  formatted output to be measured without writing it out.
                  The formatter processes input in a dummy environment: this
                  means that font and type size changes, for example, may
                  occur within it without affecting subsequent output.
           \x'N'  Increase vertical spacing of pending output line by N vees
                  (or specified units; negative before, positive after).
           \X'character-sequence'
                  Write character-sequence to troff output as a device
                  extension command.  The groff special character repertoire
                  is unknown to output drivers outside of glyphs named in a
                  device's fonts, and even then they may not possess complete
                  coverage of the names documented in groff_char(7).
                  Further, escape sequences that produce horizontal or
                  vertical motions, hyphenation breaks, or that are dummy
                  characters may appear in strings or be converted to nodes,
                  particularly in diversions.  These are not representable
                  when interpolated directly into device-independent output,
                  as might be done when writing out tag names for PDF
                  bookmarks, which can appear in a viewer's navigation pane.

                  So that documents or macro packages do not have to
                  laboriously “sanitize” strings destined for interpolation
                  in device extension commands, this escape sequence performs
                  certain transformations on its argument.  For these
                  transformations, character translations and definitions are
                  ignored.

                  GNU troff converts several ordinary characters that typeset
                  as non-basic Latin code points to code points outside that
                  range so that they are used consistently whether they are
                  formatted as glyphs or used in a device control command
                  argument.  These ordinary characters are “'”, “-”, “^”,
                  “`”, and “~”; others are written as-is.

                  Special characters that typeset as Unicode basic Latin
                  characters are translated to basic Latin characters
                  accordingly.  So that any Unicode code point can be
                  represented in device extension commands, for example in an
                  author's name in document metadata or as a usefully named
                  bookmark or hyperlink anchor, GNU troff maps other special
                  characters to Unicode special character notation.  Special
                  characters without a Unicode representation, and escape
                  sequences that do not interpolate a sequence of ordinary
                  and/or special characters, produce warnings in category
                  “char”.
           \Yn    Write contents of macro or string n to troff output as a
                  device extension command.
           \Y(nm  Write contents of macro or string nm to troff output as a
                  device extension command.
           \Y[name]
                  Write contents of macro or string name to troff output as a
                  device extension command.
           \zc    Format character c with zero width—without advancing the
                  drawing position.
           \Z'input'
                  Save the drawing position, format input, then restore it.
                  GNU troff ignores tabs and leaders in input with an error
                  diagnostic.

       Drawing commands
           Drawing commands direct the output device to render geometrical
           objects rather than glyphs.  Specific devices may support only a
           subset, or may feature additional ones; consult the man page for
           the output driver in use.  Terminals in particular implement
           almost none.

           Rendering starts at the drawing position; when finished, the
           drawing position is left at the rightmost point of the object,
           even for closed figures, except where noted.  GNU troff draws
           stroked (outlined) objects with the stroke color, and shades
           filled ones with the fill color.  See section “Colors” above.
           Coordinates h and v are horizontal and vertical motions relative
           to the drawing position or previous point in the command.  The
           default scaling unit for horizontal measurements (and diameters of
           circles) is m; for vertical ones, v.

           Circles, ellipses, and polygons can be drawn stroked or filled.
           These are independent properties; if you want a filled, stroked
           figure, you must draw the same figure twice using each drawing
           command.  A filled figure is always smaller than an outlined one
           because the former is drawn only within its defined area, whereas
           strokes have a line thickness (set with \D't').

           \D'~ h1 v1 ... hn vn'
                  Draw B-spline to each point in sequence, leaving drawing
                  position at (hn, vn).
           \D'a hc vc h v'
                  Draw circular arc centered at (hc, vc) counterclockwise
                  from the drawing position to a point (h, v) relative to the
                  center.  (hc, vc) is adjusted to the point nearest the
                  perpendicular bisector of the arc's chord.
           \D'c d'
                  Draw circle of diameter d with its leftmost point at the
                  drawing position.
           \D'C d'
                  As \D'C', but the circle is filled.
           \D'e h v'
                  Draw ellipse of width h and height v with its leftmost
                  point at the drawing position.
           \D'E h v'
                  As \D'e', but the ellipse is filled.
           \D'l h v'
                  Draw line from the drawing position to (h, v).
           \D'p h1 v1 ... hn vn'
                  Draw polygon with vertices at the drawing position and each
                  point in sequence.  GNU troff closes the polygon by drawing
                  a line from (hn, vn) back to the initial drawing position.
                  Afterward, the drawing position is left at (hn, vn).
           \D'P h1 v1 ... hn vn'
                  As \D'p', but the polygon is filled.
           \D't n'
                  Set stroke thickness of geometric objects to to n basic
                  units.  A zero n selects the minimum supported thickness.
                  A negative n selects a thickness proportional to the type
                  size; this is the default.

## [](#Strings)Strings

           groff supports strings primarily for user convenience.
           Conventionally, if one would define a macro only to interpolate a
           small amount of text, without invoking requests or calling any
           other macros, one defines a string instead.  Only one string is
           predefined by the language.

           \*[.T]     Contains the name of the output device (for example,
                      “utf8” or “pdf”).

           The ds request creates a string with a specified name and
           contents.  If the identifier named by ds already exists as an
           alias, the target of the alias is redefined.  If ds is invoked
           with only one argument, the named string becomes empty.  The
           formatter removes a leading neutral double quote ‘"’ from contents
           to permit the embedding of leading spaces.  It interprets any
           other ‘"’ literally, but the wise author uses the special
           character escape sequence \[dq] instead if the string might be
           interpolated as part of a macro argument; see section “Calling
           macros” above.

           The \* escape sequence dereferences a string's name, interpolating
           its contents.  If the name does not exist, the formatter defines
           it as empty, interpolates nothing, and emits a warning in category
           “mac”.  See section “Warnings” in troff(1).  The bracketed
           interpolation form accepts arguments that are handled as macro
           arguments are; see section “Calling macros” above.  In contrast to
           macro calls, an argument containing a closing bracket ] must be
           enclosed in double quotes.  When defining strings, argument
           interpolations must be escaped if they are to reference parameters
           from the calling context; see section “Parameters” below.  Any
           non-initial neutral double quote " is interpreted literally, but
           it is wise to use the special character escape sequence \[dq]
           instead if the string might be interpolated as part of a macro
           argument; see section “Calling macros” above.  Strings are not
           limited to a single input line of text.  \newline works just as it
           does elsewhere.  The resulting string is stored without the
           newlines.  When filling is disabled, care is required to avoid
           overrunning the line length when interpolating strings.
           Conversely, when filling is enabled, it is not necessary to append
           \c to a string interpolation to prevent a break afterward, as
           might be required in a macro argument.  Nor does a string require
           use of the GNU troff chop request to excise a trailing newline as
           is often done with diversions.  It is not possible to embed a
           newline in a string that will be interpreted as such when the
           string is interpolated.  To achieve that effect, use \* to
           interpolate a macro instead; see section “Punning names” below.

           The “as” request is similar to ds but appends to a string instead
           of redefining it.  If “as” is invoked with only one argument, no
           operation is performed (beyond dereferencing the string).

           Because strings are similar to macros, they too can be defined to
           suppress AT&T troff compatibility mode enablement when
           interpolated; see section “Compatibility mode” below.  The ds1
           request defines a string that suspends compatibility mode when the
           string is later interpolated.  as1 is likewise similar to “as”,
           with compatibility mode suspended when the appended portion of the
           string is later interpolated.

           Caution: These requests treat the remainder of the input line as
           their second argument, including any spaces, up to a newline or
           comment escape sequence.  Ending string definitions (and
           appendments) with a comment, even an empty one, prevents unwanted
           space from creeping into them during source document maintenance.
           This rule and suggestion also applies to the second argument of
           the “length” request, to requests that define characters (char,
           fchar, fschar, and schar), and to the file name or command
           arguments of the cf, hpf, hpfa, mso, msoquiet, nx, “open”, opena,
           pi, pso, “so”, soquiet, and trf requests.

           Several requests exist to perform rudimentary string operations.
           Strings can be queried (length) and modified (chop, substring,
           stringup, stringdown), and their names can be manipulated through
           renaming, removal, and aliasing (rn, rm, als).

           Redefinitions and appendments “write through” request, macro,
           string, and diversion names.  To replace an aliased object with a
           separately defined one, you must use the rm request on its name
           first.

## [](#Registers)Registers

           In the roff language, numbers and measurements can be stored in
           registers.  Many built-in registers exist, supplying anything from
           components of the date to details of formatting parameters; some
           of these are read-only.  You can also define your own.  See
           section “Identifiers” above regarding the construction of valid
           names for registers.

           Each register (except read-only ones) can be assigned a format,
           causing its value to interpolate with leading zeroes, in Roman
           numerals, or alphabetically.  Some read-only registers are string-
           valued, meaning that they interpolate text and lack a format.

           Define registers and update their values with the nr request or
           the \R escape sequence.

           User-defined registers can also be incremented or decremented by a
           configured amount at the time they are interpolated.  The value of
           the increment is specified with a third argument to the nr
           request, and a special interpolation syntax, \n±, alters and then
           retrieves the register's value.  Together, these features are
           called auto-increment.  (A negative auto-increment can be
           considered an “auto-decrement”.)

           Many predefined registers are available.  The following
           presentation uses register interpolation syntax \n[name] to refer
           to a register name to clearly distinguish it from a string or
           request name; the symbols \n[] are not part of the register name.
           The register name space is separate from that used for requests,
           macros, strings, and diversions.

       Read-only registers
           Predefined registers whose identifiers start with a dot are read-
           only.  Many are Boolean-valued.

           Caution: Built-in registers are subject to removal like others;
           once removed, they can be recreated only as normal writable
           registers and will not otherwise reflect the configuration of the
           formatter.

           A register name is often associated with a request of the same
           name (without the dot); exceptions are noted.

           \n[.$] Count of arguments passed to currently interpolated macro
                  or string.
           \n[.a] Amount of extra post-vertical line space; see \x.
           \n[.A] Approximate output is being formatted (Boolean-valued); see
                  troff -a option.
           \n[.b] Font emboldening offset; see bd.
           \n[.br]
                  The normal control character was used to call the macro
                  being interpreted (Boolean-valued).
           \n[.c] Input line number; see lf and register “c.”.
           \n[.C] AT&T troff compatibility mode is enabled (Boolean-valued);
                  see cp.  Always false when processing ”do”; see register
                  .cp.
           \n[.cdp]
                  Depth of last glyph formatted in the environment; positive
                  if glyph extends below the baseline.
           \n[.ce]
                  Count of input lines remaining to be centered in the
                  environment.
           \n[.cht]
                  Height of last glyph formatted in the environment; positive
                  if glyph extends above the baseline.
           \n[.color]
                  Color output is enabled (Boolean-valued).
           \n[.cp]
                  Within ”do”, the saved value of compatibility mode; see
                  register .C.
           \n[.csk]
                  Skew of the last glyph formatted in the environment; see
                  register skw.
           \n[.d] Vertical drawing position in diversion.
           \n[.ev]
                  Name of environment (string-valued).
           \n[.f] Mounting position of selected font; see ft and \f.
           \n[.F] Name of input file (string-valued); see lf.
           \n[.fam]
                  Name of the environment's default font family (string-
                  valued).
           \n[.fn]
                  Resolved name of font selected in the environment (string-
                  valued); see ft and \f.
           \n[.fp]
                  Next non-zero free font mounting position index.
           \n[.g] Always true in GNU troff (Boolean-valued).
           \n[.h] Text baseline high-water mark on page or in diversion.
           \n[.H] Horizontal motion quantum of output device in basic units.
           \n[.height]
                  Height of the environment's selected font; see \H.
           \n[.hla]
                  Hyphenation language in environment (string-valued).
           \n[.hlc]
                  Count of immediately preceding consecutive hyphenated lines
                  in environment.
           \n[.hlm]
                  Maximum quantity of consecutive hyphenated lines allowed in
                  environment.
           \n[.hy]
                  Automatic hyphenation mode in environment.
           \n[.hydefault]
                  Hyphenation mode default in environment.
           \n[.hym]
                  Hyphenation margin in environment.
           \n[.hys]
                  Hyphenation space adjustment threshold in environment.
           \n[.i] Environment's indentation amount; see ”in”.
           \n[.in]
                  Indentation amount applicable to the output line pending in
                  the environment; see ti.
           \n[.int]
                  The text most recently formatted in the environment was
                  “interrupted” or continued with \c (Boolean-valued).
           \n[.it]
                  Count of input lines remaining in the environment's pending
                  input trap.
           \n[.itc]
                  The environment's pending input trap honors output line
                  continuation with \c (Boolean-valued).
           \n[.itm]
                  Name of the macro associated with the pending input trap
                  (string-valued).
           \n[.j] The environment's adjustment mode encoded as an integer;
                  see ad and na.  Do not interpret or perform arithmetic on
                  its value.
           \n[.k] The environment's horizontal drawing position relative to
                  indentation.
           \n[.kern]
                  Pairwise kerning is enabled (Boolean-valued).
           \n[.l] Line length; see ll.
           \n[.L] Line spacing; see ls.
           \n[.lg]
                  Ligature mode.
           \n[.linetabs]
                  Line-tabs mode is enabled in the environment (Boolean-
                  valued).
           \n[.ll]
                  Line length applicable to the environment's pending output
                  line.
           \n[.lt]
                  Environment's title line length.
           \n[.m] Stroke color (string-valued); see gcolor and \m.  The
                  default stroke color is named “default”.
           \n[.M] Fill color (string-valued); see fcolor and \M.  The default
                  fill color is named “default”.
           \n[.n] Length of formatted output on previous output line.
           \n[.ne]
                  Amount of vertical space required by last ne that caused a
                  trap to be sprung; also see register .trunc.
           \n[.nm]
                  Output line numbering is enabled in the environment
                  (Boolean-valued).
           \n[.nn]
                  Count of lines remaining in the environment for which
                  numbering is suppressed while output line numbering is
                  enabled.
           \n[.ns]
                  No-space mode is enabled (Boolean-valued).
           \n[.o] Page offset; see po.
           \n[.O] Output suppression nesting level; see \O.
           \n[.p] Page length; see pl.
           \n[.P] The page is selected for output (Boolean-valued); see troff
                  -o option.
           \n[.pe]
                  Page ejection is in progress (Boolean-valued).
           \n[.pn]
                  Number of the next page.
           \n[.ps]
                  The environment's type size in scaled points.
           \n[.psr]
                  The environment's most recently requested type size in
                  scaled points; see ps and \s.
           \n[.pvs]
                  The environment's post-vertical line spacing.
           \n[.R] Maximum representable integer in GNU troff.
           \n[.rj]
                  Count of input lines remaining to be right-aligned in the
                  environment.
           \n[.s] The environment's type size in points as a decimal fraction
                  (string-valued); see ps and \s.
           \n[.S] Reserved.  Plan 9 troff uses this name for roughly the same
                  purpose as GNU troff's \n[.tabs]
           \n[.slant]
                  Slant in degrees of the environment's selected font; see
                  \S.
           \n[.sr]
                  The environment's most recently requested type size in
                  points as a decimal fraction (string-valued); see ps and
                  \s.
           \n[.ss]
                  Size of the environment's minimum inter-word space in
                  twelfths of the space width of the selected font.
           \n[.sss]
                  Size of the environment's supplemental inter-sentence space
                  in twelfths of the space width of the selected font.
           \n[.sty]
                  The environment's selected abstract style (string-valued);
                  see ft and \f.
           \n[.t] Distance to next vertical position trap; see wh and ch.  If
                  no such traps exist between the drawing position and the
                  bottom of the page, troff interpolates the distance to the
                  page bottom.  Within a diversion, in the absence of a
                  diversion trap, this distance is the maximum possible
                  vertical position supported by the output device.
           \n[.T] An output device was explicitly selected (Boolean-valued);
                  see troff -T option.
           \n[.tabs]
                  The environment's tab stop settings (if any) suitable for
                  use as argument to ta (string-valued).
           \n[.trap]
                  Name of the next vertical position trap after the vertical
                  drawing position.  (string-valued); see wh, ch, and dt.
           \n[.trunc]
                  Amount of vertical space truncated by the most recently
                  sprung vertical position trap, or, if the trap was sprung
                  by an ne, minus the amount of vertical motion produced by
                  ne; also see register .ne.
           \n[.u] Filling is enabled in the environment (Boolean-valued); see
                  fi and nf.
           \n[.U] Unsafe mode is enabled (Boolean-valued); see troff -U
                  option.
           \n[.v] The environment's vertical line spacing; see vs.
           \n[.V] Vertical motion quantum of the output device in basic
                  units.
           \n[.vpt]
                  Vertical position traps are enabled (Boolean-valued).
           \n[.w] Width of last glyph formatted in the environment.
           \n[.warn]
                  Sum of the numeric codes of enabled warning categories.
           \n[.x] Major version number of the running troff formatter.
           \n[.y] Minor version number of the running troff formatter.
           \n[.Y] Revision number of the running troff formatter.
           \n[.z] Name of diversion (string-valued).  Empty if output is
                  directed to the top-level diversion.
           \n[.zoom]
                  Magnification of the environment's selected font (in
                  thousandths; zero if no magnification); see fzoom.

       Writable predefined registers
           Several registers are predefined but also modifiable; some are
           updated upon interpretation of certain requests or escape
           sequences.  Date- and time-related registers are set to the local
           time as determined by localtime(3) when the formatter launches.
           This initialization can be overridden by SOURCE_DATE_EPOCH and TZ;
           see section “Environment” of groff(1).

           \n[$$] Process ID of troff.
           \n[%]  Page number.
           \n[c.] Input line number.
           \n[ct] Union of character types of each glyph rendered into dummy
                  environment by \w.
           \n[dl] Width of last closed diversion.
           \n[dn] Height of last closed diversion.
           \n[dw] Day of the week (1–7; 1 is Sunday).
           \n[dy] Day of the month (1–31).
           \n[hours]
                  Count of hours elapsed since midnight (0–23).
           \n[hp] Horizontal drawing position relative to that at the start
                  of the input line.
           \n[llx]
                  Lower-left x coordinate (in PostScript units) of PostScript
                  image; see psbb.
           \n[lly]
                  Lower-left y coordinate (in PostScript units) of PostScript
                  image; see psbb.
           \n[ln] Output line number; see nm.
           \n[lsn]
                  Count of leading spaces on input line.
           \n[lss]
                  Amount of horizontal space corresponding to leading spaces
                  on input line.
           \n[minutes]
                  Count of minutes elapsed in the hour (0–59).
           \n[mo] Month of the year (1–12).
           \n[nl] Vertical drawing position.
           \n[opmaxx]
           \n[opmaxy]
           \n[opminx]
           \n[opminy]
                  These four registers mark the top left- and bottom right-
                  hand corners of a rectangle encompassing all formatted
                  output on the page.  They are reset to -1 by \O0 or \O1.
           \n[rsb]
                  As register sb, adding maximum glyph height to measurement.
           \n[rst]
                  As register st, adding maximum glyph depth to measurement.
           \n[sb] Maximum displacement of text baseline below its original
                  position after rendering into dummy environment by \w.
           \n[seconds]
                  Count of seconds elapsed in the minute (0–60).
           \n[skw]
                  Skew of last glyph rendered into dummy environment by \w.
           \n[slimit]
                  The maximum depth of troff's internal input stack.  If ≤0,
                  there is no limit: recursion can continue until available
                  memory is exhausted.  The default is 1,000.
           \n[ssc]
                  Subscript correction of last glyph rendered into dummy
                  environment by \w.
           \n[st] Maximum displacement of text baseline above its original
                  position after rendering into dummy environment by \w.
           \n[systat]
                  Return value of system(3); see sy.
           \n[urx]
                  Upper-right x coordinate (in PostScript units) of
                  PostScript image; see psbb.
           \n[ury]
                  Upper-right y coordinate (in PostScript units) of
                  PostScript image; see psbb.
           \n[year]
                  Gregorian year.
           \n[yr] Gregorian year minus 1900.

## [](#Using_fonts)Using fonts

           In digital typography, a font is a collection of characters in a
           specific typeface that a device can render as glyphs at a desired
           size.  (Terminals and some typesetters have fonts that render at
           only one or two sizes.  As examples, take the groff lj4 device's
           Lineprinter, and lbp's Courier and Elite faces.)  A roff formatter
           can change typefaces at any point in the text.  The basic faces
           are a set of styles combining upright and slanted shapes with
           normal and heavy stroke weights: “R”, “I”, “B”, and “BI”—these
           stand for roman, bold, italic, and bold-italic.  For linguistic
           text, GNU troff groups typefaces into families containing each of
           these styles.  (Font designers prepare families such that the
           styles share esthetic properties.)  A text font is thus often a
           family combined with a style, but it need not be: consider the ps
           and pdf devices' ZCMI (Zapf Chancery Medium italic)—often, no
           other style of Zapf Chancery Medium is provided.  On typesetters,
           at least one special font is available, comprising unstyled glyphs
           for mathematical operators and other purposes.

           Like the AT&T troff formatter, GNU troff does not itself load or
           manipulate a digital font file; instead it works with a font
           description file that characterizes it, including its glyph
           repertoire and the metrics (dimensions) of each glyph.  This
           information permits the formatter to accurately place glyphs with
           respect to each other.  Before using a font description, the
           formatter associates it with a mounting position, a place in an
           ordered list of available typefaces.  So that a document need not
           be strongly coupled to a specific font family, in GNU troff an
           output device can associate a style in the abstract sense with a
           mounting position.  Thus the default family can be combined with a
           style dynamically, producing a resolved font name.  A user-
           specified font name that combines family and style, or refers to a
           font that is not a member of a family, is already “resolved”.

           Fonts often have trademarked names, and even Free Software fonts
           can require renaming upon modification.  groff maintains a
           convention that a device's serif font family is given the name T
           (“Times”), its sans-serif family H (“Helvetica”), and its
           monospaced family C (“Courier”).  Historical inertia has driven
           groff's font identifiers to short uppercase abbreviations of font
           names, as with TR, TB, TI, TBI, and a special font S.

           The default family used with abstract styles can be changed at any
           time; initially, it is T.  Typically, abstract styles are arranged
           in the first four mounting positions in the order shown above.
           The default mounting position, and therefore style, is always 1
           (R).  By issuing appropriate formatter instructions, you can
           override these defaults before your document writes its first
           glyph.

           Terminals cannot change font families and lack special fonts.
           They support style changes by overstriking, or by altering
           ISO 6429/ECMA-48 graphic renditions (character cell attributes).

           The ft request and \f escape sequence select a typeface by name,
           abstract style, or mounting position.  The fam request and \F
           escape sequence set the default font family.  The ftr request
           translates one font name to another; fzoom magnifies or reduces
           the typeface corresponding to a resolved one.  sty and fp
           associate abstract styles and font names with mounting positions.

       Characters and glyphs
           A glyph is a graphical representation of a character.  Whereas a
           character is an abstraction of semantic information, a glyph is an
           intelligible mark visible on screen or paper.  A character has
           many possible representation forms; for example, the character “A”
           can be written in an upright or slanted typeface, producing
           distinct glyphs.  Sometimes, a sequence of characters map to a
           single glyph:@: this is a ligature—the most common is `fi'.

           Space characters never become glyphs in GNU troff.  If not
           discarded (as when trailing text lines), horizontal motions
           represent them in the output.

           The formatter supports three kinds of character.  An ordinary
           character (see section “Identifiers” above) is the most commonly
           used, has no special syntax, and typically represents itself.
           (Depending on the breadth of the output device's glyph repertoire,
           the characters ', -, ^, `, and ~ can be exceptions to this rule.
           " and \ are not exceptions, but because they are syntactically
           meaningful to the formatter, access to their glyphs may require
           use of special characters (or changing or disabling the escape
           character).  See groff_char(7).  Interpolate a special character
           with the “\[xxx] or “\C'xxx'” escape sequence syntax, where xxx is
           an identifier.  An indexed character bypasses most character-to-
           glyph resolution logic, uses the “\N'i'syntax, and selects a glyph
           from the currently selected font by its integer-valued position i
           in the output device's representation of that font.  (A device's
           fonts do not necessarily arrange their glyphs according to a
           standard character encoding.)

           User-defined characters are similar to string definitions (see
           section “Strings” above) and permit extension of or substitution
           within the character repertoire.  Any ordinary, special, or
           indexed character can be user-defined.  The char, fchar, schar,
           and fschar requests create user-defined characters employed at
           various stages of the character-to-glyph resolution process.

           In a troff system, a font description file lists all of the glyphs
           a particular font provides.  If the user requests a glyph not
           available in the currently selected font, the formatter looks it
           up an ordered list of special fonts.  By default, the “ps”
           (PostScript) and “pdf” output devices support the two special
           fonts “SS” (slanted symbol) and “S” (symbol); and these devices'
           DESC files arrange them such that the formatter searches the
           former before the latter.  Other output devices use different
           names for special fonts.  Fonts mounted with the fonts keyword in
           the DESC file are globally available.  GNU troff's special and
           fspecial requests alter the list of fonts treated as special on a
           general basis, or only when a certain font is currently selected,
           respectively.

           GNU troff employs the following procedure to resolve an input
           character into a glyph.  User-defined characters make this
           resolution process recursive.  The first step that succeeds ends
           the resolution procedure for the character being formatted, which
           may not be the last in the sequence interpolated by a user-defined
           character.

           •      Interpolate the definition of any character defined by the
                  char request and apply this procedure to each character in
                  its definition.

           •      Check the current font for a glyph corresponding to the
                  character.

           •      Interpolate the definition of any user-defined character
                  matching defined by the fchar request and apply this
                  procedure to each character in its definition.

           •      Check whether the current font has a font-specific list of
                  special fonts; if so, check the each font therein, in the
                  order determined by the last applicable fspecial request,
                  for a glyph corresponding to the character.

           •      Interpolate the definition of any character defined by the
                  fschar request for the currently selected font, and apply
                  this procedure to each character in its definition.

           •      Check each font in the list configured by the most recently
                  issued special request for a glyph corresponding to the
                  character.

           •      Interpolate the definition of any character defined by the
                  sschar request and apply this procedure to each character
                  in its definition.

           •      Finally, iterate through the list of mounted fonts by
                  position.  For each mounted font, if that font bears the
                  special directive (see groff_font(5)), check it for a glyph
                  corresponding to the character.  This stage of the
                  resolution process can sometimes lead to surprising results
                  since the fonts directive in the DESC file often contains
                  empty positions that are filled by a macro file or document
                  employing the fp request after the formatter initializes.

       Special fonts
           Special fonts are those that the formatter searches, in mounting
           position order, when it cannot find a requested glyph in the
           selected font.  Typically, they are declared as such in their
           description files (see groff_font(5)), and contain unstyled
           glyphs.  The “Symbol” and “Zapf Dingbats” fonts of the PostScript
           and PDF standards are examples.  Ordinarily, only typesetters have
           special fonts.

           GNU troff's special and fspecial requests permit a document to
           supplement the set of fonts the device configures for glyph search
           without having to use the fp request to manipulate the list of
           mounting positions, which can be tedious—by default, GNU troff
           mounts 40 fonts at startup when using the ps device.

## [](#Hyphenation)Hyphenation

           When filling, groff hyphenates words as needed at user-specified
           and automatically determined hyphenation points.  Explicitly
           hyphenated words such as “mother-in-law” are always eligible for
           breaking after each of their hyphens.  The hyphenation
           character \% and non-printing break point \: escape sequences may
           be used to control the hyphenation and breaking of individual
           words.  The hw request sets user-defined hyphenation points for
           specified words at any subsequent occurrence.  Otherwise, groff
           determines hyphenation points automatically by default.

           Several requests influence automatic hyphenation.  Because
           conventions vary, a variety of hyphenation modes is available to
           the hy request; these determine whether hyphenation will apply to
           a word prior to breaking a line at the end of a page (more or
           less; see below for details), and at which positions within that
           word automatically determined hyphenation points are permissible.
           The localization macro files loaded by troffrc configure a default
           hyphenation mode appropriate to the language.

           0      disables hyphenation.

           1      enables hyphenation except after the first and before the
                  last character of a word.

           The remaining values “imply” 1; that is, they enable hyphenation
           under the same conditions as “.hy 1”, and then apply or lift
           restrictions relative to that basis.

           2      disables hyphenation of the last word on a page or column,
                  even for explicitly hyphenated words.  (Hyphenation is
                  prevented if the next page location trap is closer to the
                  vertical drawing position than the next text baseline would
                  be.  See section “Traps” below.)

           4      disables hyphenation before the last two characters of a
                  word.

           8      disables hyphenation after the first two characters of a
                  word.

           16     enables hyphenation before the last character of a word.

           32     enables hyphenation after the first character of a word.

           Apart from value 2, restrictions imposed by the hyphenation mode
           are not respected for words whose hyphenations have been specified
           with the hyphenation character (“\%” by default) or the .hw
           request.

           Nonzero values are additive.  For example, mode 12 causes groff to
           hyphenate neither the last two nor the first two characters of a
           word.  Some values cannot be used together because they
           contradict; for instance, values 4 and 16, and values 8 and 32.
           As noted, it is superfluous to add 1 to any non-zero even mode.

           The places within a word that are eligible for hyphenation are
           determined by language-specific data (hla, hpf, and hpfa) and
           lettercase relationships (hcode and hpfcode).  Furthermore,
           hyphenation of a word might be suppressed due to a limit on
           consecutive hyphenated lines (hlm), a minimum line length
           threshold (hym), or because the line can instead be adjusted with
           additional inter-word space (hys).

## [](#Localization)Localization

           GNU troff ties the set of hyphenation patterns to the hyphenation
           language code selected by the hla request.  The hpf request is
           usually invoked by a localization file loaded by the troffrc file.
           groff provides localization files for several languages; See
           subsection “Localization packages” of groff_tmac(5).  For Western
           languages, the localization file sets the default hyphenation mode
           and loads hyphenation patterns and exceptions.  By default,
           troffrc loads the localization file for English.

## [](#Writing_macros)Writing macros

           The .de request defines a macro named for its argument.  If that
           name already exists as an alias, the target of the alias is
           redefined; see section “Strings” above.  troff enters “copy mode”
           (see below), storing subsequent input lines as the definition.  If
           the optional second argument is not specified, the definition ends
           with the control line “..” (two dots).  Tabs and spaces are
           permitted between the dots.  Alternatively, a second argument to
           .de names a macro whose call (or request whose invocation) syntax
           ends the definition; this end macro is then interpreted normally.
           Spaces or tabs are permitted after the first control character in
           the line containing this ending token, but a tab immediately after
           the token prevents its recognition as the end of a macro
           definition.  Macro definitions can be nested if they use distinct
           end macros or if their ending tokens are sufficiently escaped.  An
           end macro need not be defined until it is called.  This fact
           enables a nested macro definition to begin inside one macro and
           end inside another.

           Variants of .de disable compatibility mode and/or indirect the
           names of the macros specified for definition or termination: these
           are .de1, .dei, and .dei1.  Append to macro definitions with .am,
           .am1, .ami, and .ami1.  The .als, .rm, and .rn requests create an
           alias of, remove, and rename a macro, respectively.  .return stops
           the execution of a macro immediately, returning to the enclosing
           context.

       Parameters
           Macro call and string interpolation parameters can be accessed
           using escape sequences starting with “\$”.  The \n[.$] read-only
           register stores the count of parameters available to a macro or
           string; change its value with the .shift request, which dequeues
           parameters from the current list.  The \$0 escape sequence
           interpolates the name by which a macro was called.  Applying
           string interpolation to a macro does not change this name.

       Copy mode
           GNU troff processes certain requests in copy mode: it copies
           ordinary, special, and indexed characters as-is; interpolates the
           escape sequences \n, \g, \$, \*, \V, and \? normally; discards
           comments \" and \#; interpolates \a, \e, and \t, as the current
           leader, escape, or tab character with respectively; represents
           \newline, \&, \_, \|, \^, \{, \}, \`, \', \-, \!, \c, \%, \space,
           \E, \), \~, and \: in an encoded form, and copies other escape
           sequences as-is.  The term “copy mode” reflects its most visible
           application in requests that populate macros and strings, but
           other requests also use it when interpreting arguments that can't
           meaningfully represent typesetting operations.  For example, a
           font selection escape sequence has no meaning in a hyphenation
           pattern file name (hpf) or a diagnostic message written to the
           terminal (tm).  The complement of copy mode—a roff formatter's
           behavior when not defining or appending to a macro, string, or
           diversion—where all macros are interpolated, requests invoked, and
           valid escape sequences processed immediately upon recognition, can
           be termed interpretation mode.

           The escape character (\ by default) when used before itself quotes
           an escape character for later interpretation in an enclosing
           context.  Escape character quotation enables you to control
           whether the formatter interprets a given \n, \g, \$, \*, \V, or \?
           escape sequence at the time the macro containing it is defined, or
           later when the macro is called.

           You can think of \\ as a “delayed” backslash; it is the escape
           character followed by a backslash from which the escape character
           has removed its special meaning.  Consequently, \\ is not best
           considered an escape sequence, but a quoted escape character.  In
           any escape sequence \X that troff does not recognize, the
           formatter discards the escape character and outputs X.  An
           unrecognized escape sequence causes a warning in category
           “escape”, with two exceptions, \\ being one.  The other is \.,
           which quotes the control character.  It is used to permit nested
           macro definitions to end without a named macro call to conclude
           them.  Without a syntax for quoting the control character, this
           would not be possible.  Outside of copy mode, roff documents
           should not use the \\ or \. character sequences; they serve only
           to obfuscate the input.  Use \e to represent the escape character,
           \[rs] to obtain a backslash glyph, and \& before . and ' where
           troff expects them as control characters if you mean to use them
           literally.

           Macro definitions can be nested to arbitrary depth.  Given the
           input character sequence “\\” in a macro or string definition, the
           formatter interprets each escape character in multiple contexts;
           once, when populating the macro or string, where the first “\”
           serves its quotation function—thus only one “\” is stored in the
           definition.  (Verify this fact with the pm request.)  The
           formatter interprets the second “\” as an escape character
           (assuming the escape character hasn't been changed in the
           meantime) each time it interpolates the macro or string
           definition.  This fact leads to exponential growth in the quantity
           of escape characters required to quote and thereby delay
           interpolation of \n, \g, \$, \*, \V, and \? at each nesting level.
           An alternative is to use \E, which represents an escape character
           that is not interpreted in copy mode.  Because \. is not a true
           escape sequence, we can't use \E to keep “..” from ending a macro
           definition prematurely.  If the multiplicity of backslashes
           complicates maintenance, use end macros.

## [](#Traps)Traps

           Traps are locations in the output, or conditions on the input
           that, when reached or fulfilled, call a specified macro.  A
           vertical position trap calls a macro when the formatter's vertical
           drawing position reaches or passes, in the downward direction, a
           certain location on the output page or in a diversion.  Its
           applications include setting page headers and footers, body text
           in multiple columns, and footnotes.  These traps can occur at a
           given location either on the page (wh, ch) or in the current
           diversion (dt)—together, these are known as vertical position
           traps, which can be disabled and reënabled (vpt).

           A diversion is not formatted in the context of a page, so it lacks
           page location traps; instead it can have a diversion trap.  There
           can exist at most one such vertical position trap per diversion.

           Other kinds of trap can be planted at a blank line (blm); at a
           line with leading space characters (lsm); after a certain number
           of productive input lines (it, itc); or at the end of input (em).

           Setting a trap is also called planting one.  It is said that a
           trap is sprung if its condition is fulfilled.

           The formatter passes no arguments to macros called by traps.

           Registers associated with trap management include vertical
           position trap enablement status (\n[.vpt]), distance to the next
           trap (\n[.t]), and the name of that trap (\n[.trap]); the count of
           lines remaining in the pending input trap (\n[.it]), the name of
           the macro associated with it (\n[.itm]), and whether that input
           trap honors the \c output line continuation escape sequence
           (\n[.itc]); amount of needed (.ne-requested) space that caused the
           most recent vertical position trap to be sprung (\n[.ne]), amount
           of needed space truncated from the amount requested (\n[.trunc]);
           page ejection status (\n[.pe]); and leading space count (\n[lsn])
           with its corresponding amount of motion (\n[lss]).

       Page location traps
           A page location trap is a vertical position trap that applies to
           the page; that is, to the top-level diversion.  Many can be
           present; manage them with the wh and ch requests.  Non-negative
           page locations given to these requests set the trap relative to
           the top of the page; negative values set the trap relative to the
           bottom of the page.  It is not possible to plant a trap less than
           one basic unit from the page bottom: a location of “-0” is
           interpreted as “0”, the top of the page.  An existing visible trap
           (see below) at the same location is removed; this is wh's sole
           function if its second argument is missing.

           A trap is sprung only if it is visible, meaning that its location
           is reachable on the page and it is not hidden by another trap at
           the same location already planted there.  (A trap planted at “20i”
           or “-30i” will not be sprung on a page of length “11i”.)

           A trap above the top or at or below the bottom of the page can be
           made visible by either moving it into the page area or increasing
           the page length so that the trap is on the page.  A negative trap
           value always uses the current page length; the formatter does not
           convert it to an absolute vertical position.  We can use the pwh
           request to dump page location traps to the standard error stream;
           see section “Debugging” below.  GNU troff reports their positions
           in basic units, and includes empty slots in the list, where a trap
           had been planted but subsequently (re)moved, because they can
           affect the visibility of subsequently planted traps.

       The implicit page trap
           An implicit page trap always exists in the top-level diversion
           (see below); its purpose is to eject the current page and start
           the next one.  It works like a trap in some ways but not others.
           It has no name, so it cannot be moved or deleted with wh or ch
           requests.  You cannot hide it by placing another trap at its
           location, and can move it only by redefining the page length with
           pl.  Its operation is suppressed when vertical page traps are
           disabled with GNU troff's vpt request.

## [](#Diversions)Diversions

           In roff systems it is possible to format text as if for output,
           but instead of writing it immediately, one can divert the
           formatted text into a named storage area.  It is retrieved later
           by specifying its name after a control character.  The formatter
           uses the same name space for such diversions as for strings and
           macros; see section “Identifiers” above.  Such text is sometimes
           said to be “stored in a macro”, but this coinage obscures the
           important distinction between macros and strings on one hand and
           diversions on the other; the former store unformatted input text,
           and the latter capture formatted output.  Diversions also do not
           interpret arguments.  Applications of diversions include
           footnotes, tables of contents, indices, and “keeps” (preventing a
           page break from occurring at an inconvenient place by forcing a
           set of output lines to be set as a group).  For orthogonality it
           is said that GNU troff populates the top-level diversion if no
           diversion is active (that is, formatted output is being “diverted”
           directly to the output device).  The top-level diversion has no
           name.

           Dereferencing an undefined diversion creates an empty one of that
           name.  (GNU troff also emits a warning in category “mac”; see
           section “Warnings” of troff(1).)  A diversion does not exist for
           the purpose of testing with the d conditional expression operator
           until its initial definition ends; see subsection “Conditional
           expressions” above.

           The di request creates a diversion, including any partially
           collected line.  da appends to a diversion, creating one if it
           does not already exist.  If the diversion's name already exists as
           an alias, the target of the alias is replaced or appended to; see
           section “Strings” above.  The pending output line is diverted as
           well.  Switching to another environment (with the ev request)
           before invoking di or da avoids including any pending output line
           in the diversion.  (See section “Environments[” below.)

           Invoking di or da without an argument stops diverting output to
           the diversion named by the most recent corresponding request.
           Invoking di or da without an argument when no diversion is being
           populated does nothing.  (GNU troff emits a warning in category
           “di”; see section “Warnings” of troff(1).)

           box and boxa work similarly, but ignore partially collected lines.
           Call any of these macros again without an argument to end the
           diversion.

           Diversion requests can be nested.  The registers .d and .z report
           information about the current diversion, and dn and dl about the
           most recently closed one.  .h is meaningful in diversions,
           including the top-level one.

           After output to a (named) diversion stops, the formatter stores
           its vertical and horizontal sizes, to the writable registers dn
           and dl, respectively.  Only the lines just processed are counted:
           for the computation of dn and dl, the requests da and boxa are
           handled as if di and box had been used, respectively—lines that
           have been already stored in the diversion (box) are not taken into
           account.

           The \! and \? escape sequences and output request escape from a
           diversion, the first two to the enclosing level and the last to
           the top level.  This facility is termed transparent embedding.

           The asciify and “unformat” requests reprocess diversions.

## [](#Punning_names)Punning names

           Macros, strings, and diversions share a name space; see section
           “Identifiers” above.  Internally, the same mechanism is used to
           store them.  You can thus call a macro with string interpolation
           syntax and vice versa.  Interpolating a string does not hide
           existing macro arguments.  Place the sequence \\ at the end of a
           line in a macro definition or, within a macro definition,
           immediately after the interpolation of a macro as a string, to
           suppress the effect of a newline.

## [](#Environments)Environments

           Environments store most of the parameters that control text
           processing.  A default environment named “0” (zero) exists when
           exists when the formatter starts up; formatting-related requests
           and escape sequences modify its properties.

           You can create new environments and switch among them.  Only one
           is current at any given time.  Active environments are managed
           using a stack, a data structure supporting “push” and “pop”
           operations.  The current environment is at the top of the stack.
           The same environment name can be pushed onto the stack multiple
           times, possibly interleaved with others.  Popping the environment
           stack does not destroy the current environment; it remains
           accessible by name and can be made current again by pushing it at
           any time.  Environments cannot be renamed or deleted, and can only
           be modified when current.  To inspect the environment stack, use
           the pev request; see section “Debugging” below.

           Environments store the following information.

           •  a partially collected line, if any

           •  data about the most recently output glyph and line (registers
              .cdp, .cht, .csk, .n, .w)

           •  typeface parameters (size, family, style, height and slant,
              inter-word and inter-sentence space sizes)

           •  page parameters (line length, title length, vertical spacing,
              line spacing, indentation, line numbering, centering, right-
              alignment, underlining, hyphenation parameters)

           •  filling enablement; adjustment enablement and mode

           •  tab stops; tab, leader, escape, control, no-break control,
              hyphenation, and margin characters

           •  input line traps

           •  stroke and fill colors

           The ev request (with an argument) pushes to and (without) pops
           from the environment stack, while evc copies a named environment's
           parameters to the current one.

## [](#Postprocessor_access)Postprocessor access

           Beyond the cf and trf requests, two escape sequences and two
           requests enable documents to pass information directly to a
           postprocessor.  These are useful for exercising device-specific
           capabilities that the groff language does not abstract or
           generalize; examples include the embedding of hyperlinks and image
           files.  Device-specific functions are documented in each output
           driver's man page, such as gropdf(1), grops(1), or grotty(1).

           The “device” request and \X escape sequence embed their arguments
           into GNU troff output as parameters to an “x X” device extension
           command (see groff_out(5)).  The interpretation of such parameters
           is determined by the output driver or other postprocessor.

           GNU troff also permits the interpolation of macro or string
           contents as a device extension command.  The devicem request and
           \Y escape sequence correspond to “.device \*[name]” and
           “\X'\*[name]”, respectively.  They differ from their counterparts
           in that GNU troff does not interpret the contents of the string or
           macro name; further, name may be a macro and thus contain
           newlines.  (There is no way to embed a newline in the arguments to
           “device” or \X.)  The inclusion of newlines requires an extension
           to the AT&T troff device-independent page description language,
           and their presence confuses drivers that do not know about it (see
           subsection “Device control commands” of groff_out(5)).

           Use of device extension commands early in a document (before the
           first text is formatted) can interfere with processing of page
           location traps.  If you experience problems when placing them
           early, precede the first with a dummy character escape sequence
           “\&”; recall section “Dummy Characters” above.

           The tag and taga requests are reserved for internal use.

## [](#Underlining)Underlining

           In RUNOFF (see roff(7)), underlining, even of lengthy passages,
           was straightforward because only fixed-pitch printing devices were
           targeted.  Typesetter output posed a greater challenge.  There
           exists a groff request .ul (see above) that underlines subsequent
           source lines on terminals, but on typesetters, it selects an
           italic font style instead.  The ms macro package (see groff_ms(7))
           offers a macro .UL, but it too produces the desired effect only on
           typesetters, and has other limitations.

           One could adapt ms's approach to the construction of a macro as
           follows.
                  .de UNDERLINE
                  . ie n \\$1\f[I]\\$2\f[P]\\$3
                  . el \\$1\Z'\\$2'\v'.25m'\D'l \w'\\$2'u 0'\v'-.25m'\\$3
                  ..
           If doclifter(1) makes trouble, change the macro name UNDERLINE
           into some 2-letter word, like Ul.  Moreover, change the form of
           the font selection escape sequence from \f[P] to \fP.

       Underlining without macro definitions
           If one does not want to use macro definitions, e.g., when
           doclifter gets lost, use the following.
                  .ds u1 before
                  .ds u2 in
                  .ds u3 after
                  .ie n \*[u1]\f[I]\*[u2]\f[P]\*[u3]
                  .el \*[u1]\Z'\*[u2]'\v'.25m'\D'l \w'\*[u2]'u 0'\v'-.25m'\*[u3]
           When using doclifter, it might be necessary to change syntax forms
           such as \[xy] and \*[xy] to those supported by AT&T troff: \*(xy
           and \(xy, and so on.

           Then these lines could look like
                  .ds u1 before
                  .ds u2 in
                  .ds u3 after
                  .ie n \*[u1]\fI\*(u2\fP\*(u3
                  .el \*(u1\Z'\*(u2'\v'.25m'\D'l \w'\*(u2'u 0'\v'-.25m'\*(u3

           The result looks like
                  before _i_n after

       Underlining by overstriking with \(ul
           The \z escape sequence writes a glyph without advancing the
           drawing position, enabling overstriking.  Thus, \zc\(ul formats c
           with an underrule glyph on top of it.  Video terminals implement
           the underrule by setting a character cell's underline attribute,
           so this technique works in both nroff and troff modes.

           Long words may then look intimidating in the input; a clarifying
           approach might be to use the input line continuation escape
           sequence \newline to place each underlined character on its own
           input line.  Thus,
                  .nf
                  \&\fB: ${\fIvar\fR\c
                  \zo\(ul\
                  \zp\(ul\c
                  \&\fIvalue\fB}
                  .fi
           produces
                  : ${varo_p_value}
           as output.

## [](#Compatibility_mode)Compatibility mode

           groff_diff(7) documents differences between the roff language
           recognized by GNU troff and that of AT&T troff, as well as the
           device, font, and device-independent page description formats
           described by CSTR #54.  GNU troff provides an AT&T troff
           compatibility mode.  The cp request and registers .C and .cp set
           and test the enablement of this mode.

## [](#Debugging)Debugging

           Preprocessors use the lf request to preserve the identities of
           line numbers and names of input files.  groff emits a variety of
           error diagnostics and supports several categories of warning; the
           output of these can be selectively suppressed with “warn” (and see
           the -E, -w, and -W options of troff(1)).  A trace of the
           formatter's input processing stack can be emitted when errors or
           warnings occur by means of troff(1)'s -b option, or produced on
           demand with the backtrace request.  tm, tmc, and tm1 can be used
           to emit customized diagnostic messages or for instrumentation
           while troubleshooting.  ex and ab cause early termination with
           successful and error exit codes respectively, to halt further
           processing when continuing would be fruitless.  Examine the state
           of the formatter with requests that write lists of defined names—
           macros, strings, and diversions—(pm); characters (pchar;
           experimental); colors (pcolor); composite character mappings
           (pcomposite); environments (pev); occupied font mounting positions
           (pfp); font translations (pftr); automatic hyphenation codes
           (pchar) and exceptions (phw); registers (pnr); open streams
           (pstream); and page location traps (pwh).  Requests can also
           disclose to the standard error stream the internal properties and
           representations of characters and classes (pchar), macros (and
           strings and diversions) (pm), and the list of output nodes
           corresponding to the pending input line (pline).

## [](#Authors)Authors

           This document was written by Trent A. Fisher, Werner Lemberg ⟨wl@
           gnu.org⟩, and G. Branden Robinson ⟨g.branden.robinson@gmail.com⟩.
           Section “Underlining” was primarily written by Bernd Warken
           ⟨groff-bernd.warken-72@web.de⟩.

## [](#See_also)See also

           Groff: The GNU Implementation of troff, by Trent A. Fisher and
           Werner Lemberg, is the primary groff manual.  You can browse it
           interactively with “info groff”.

           “Troff User's Manual” by Joseph F. Ossanna, 1976 (revised by Brian
           W. Kernighan, 1992), AT&T Bell Laboratories Computing Science
           Technical Report No. 54, widely called simply “CSTR #54”,
           documents the language, device and font description file formats,
           and device-independent page description language referred to
           collectively in groff documentation as “AT&T troff”.

           “A Typesetter-independent TROFF” by Brian W. Kernighan, 1982, AT&T
           Bell Laboratories Computing Science Technical Report No. 97
           (CSTR #97), provides additional insights into the device and font
           description file formats and device-independent page description
           language.

           groff(1)
                  is the preferred interface to the groff system; it manages
                  the pipeline that carries a source document through
                  preprocessors, the troff formatter, and an output driver to
                  viewable or printable form.  It also exhaustively lists the
                  man pages provided with the GNU roff system.

           groff_char(7)
                  discusses character encoding issues and escape sequences
                  that produce glyphs.

           groff_diff(7)
                  covers differences between the GNU troff formatter, its
                  device and font description file formats, its device-
                  independent page description language, and those of AT&T
                  troff.

           groff_font(5)
                  describes the formats of the files that describe devices
                  (DESC) and fonts.

           groff_tmac(5)
                  surveys macro packages provided with groff, describes how
                  documents can take advantage of them, offers guidance on
                  writing macro packages and using diversions, and includes
                  historical information.

           roff(7)
                  presents a detailed history of roff systems and summarizes
                  concepts common to them.

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

    groff 1.24.1                    2026-03-14                       groff(7)

------------------------------------------------------------------------

Pages that refer to this page: [man(1)](../man1/man.1.html),  [man-pages(7)](../man7/man-pages.7.html)

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
