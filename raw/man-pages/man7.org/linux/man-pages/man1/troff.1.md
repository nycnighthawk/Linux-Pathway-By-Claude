---
{"title": "troff(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/troff.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# troff(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Synopsis](#Synopsis) \| [Description](#Description) \| [Options](#Options) \| [Warnings](#Warnings) \| [Exit status](#Exit_status) \| [Environment](#Environment) \| [Files](#Files) \| [Authors](#Authors) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    troff(1)                 General Commands Manual                 troff(1)

## [](#Name)Name

           troff - GNU roff typesetter and document formatter

## [](#Synopsis)Synopsis

           troff [-abcCEiRSUz] [-d ctext] [-d string=text] [-f font-family]
                 [-F font-directory] [-I inclusion-directory] [-m macro-
                 package] [-M macro-directory] [-n page-number] [-o page-
                 list] [-r cnumeric-expression] [-r register=numeric-
                 expression] [-T output-device] [-w warning-category]
                 [-W warning-category] [file ...]

           troff --help

           troff -v

           troff --version

## [](#Description)Description

           GNU troff transforms groff(7) language input into the device-
           independent page description language detailed in groff_out(5);
           troff is thus the heart of the GNU roff document formatting
           system.  If no file operands are present, or if file is “-”, troff
           reads the standard input stream.

           GNU troff is functionally compatible with the AT&T troff
           typesetter and features numerous extensions.  Many people prefer
           to use the groff(1) command, a front end which also runs
           preprocessors and output drivers in the appropriate order and with
           appropriate options.

## [](#Options)Options

           -h and --help display a usage message, while -v and --version show
           version information; all exit afterward.

           -a     Generate a plain text approximation of the typeset output.
                  The read-only register .A is set to 1.  This option
                  produces a sort of abstract preview of the formatted
                  output.

                  •  Page breaks are marked by a phrase in angle brackets;
                     for example, “<beginning of page>”.

                  •  Lines are broken where they would be in formatted
                     output.

                  •  Vertical motion, apart from that implied by a break, is
                     not represented.

                  •  A horizontal motion of any size is represented as one
                     space.  Adjacent horizontal motions are not combined.
                     Supplemental inter-sentence space (configured by the
                     second argument to the .ss request) is not represented.

                  •  A special character is rendered as its identifier
                     between angle brackets; for example, a hyphen appears as
                     “<hy>”.

                  The above description should not be considered a
                  specification; the details of -a output are subject to
                  change.

           -b     Write a backtrace reporting the state of troff's input
                  parser to the standard error stream with each diagnostic
                  message.  The line numbers given in the backtrace might not
                  always be correct, because troff's idea of line numbers can
                  be confused by requests that append to macros.

           -c     Disable multi-color output and “color” request's ability to
                  enable it.

           -C     Enable AT&T troff compatibility mode; implies -c.  See
                  groff_diff(7).

           -d ctext
           -d string=text
                  Define roff string c or string as text.  c must be a one-
                  character identifier; string can be of arbitrary length.
                  Such assignments happen before any macro file is loaded,
                  including the startup file.  Due to getopt_long(3)
                  limitations, c cannot be, and string cannot contain, an
                  equals sign, even though that is a valid character in a
                  roff identifier.

           -E     Inhibit troff error messages; implies -Ww.  This option
                  does not suppress messages sent to the standard error
                  stream by documents or macro packages using tm or related
                  requests.

           -f fam Use fam as the default font family.

           -F dir Search in directory dir for the selected output device's
                  directory of device and font description files.  See the
                  description of GROFF_FONT_PATH in section “Environment”
                  below for the default search locations and ordering.

           -i     Read the standard input stream after all named input files
                  have been processed.

           -I dir Search the directory dir for files (those named on the
                  command line; in psbb, so, and soquiet requests; and in
                  “\X'ps: import'”, “\X'ps: file'”, and “\X'pdf: pdfpic'”
                  device extension escape sequences).  -I may be specified
                  more than once; each dir is searched in the given order.
                  To search the current working directory before others, add
                  “-I .” at the desired place; it is otherwise searched last.
                  -I works similarly to, and is named for, the “include”
                  option of Unix C compilers.

           -m mac Search for the macro package mac.tmac and read it prior to
                  any input.  If not found, tmac.mac is attempted.  See the
                  description of GROFF_TMAC_PATH in section “Environment”
                  below for the default search locations and ordering.

           -M dir Search directory dir for macro files.  See the description
                  of GROFF_TMAC_PATH in section “Environment” below for the
                  default search locations and ordering.

           -n num Begin numbering pages at num.  The default is 1.

           -o list
                  Output only pages in list, which is a comma-separated list
                  of inclusive page ranges; n means page n, m-n means every
                  page between m and n, -n means every page up to n, and n-
                  means every page from n on.  troff stops processing and
                  exits after formatting the last page enumerated in list.

           -r cnumeric-expression
           -r register=numeric-expression
                  Define roff register c or register as numeric-expression.
                  c must be a one-character identifier; register can be of
                  arbitrary length.  Such assignments happen before any macro
                  file is loaded, including the startup file.  Due to
                  getopt_long(3) limitations, c cannot be, and register
                  cannot contain, an equals sign, even though that is a valid
                  character in a roff identifier.

           -R     Prevent loading of troffrc and troffrc-end; this option can
                  be useful for troubleshooting.

           -S     Enable safer mode and ignore any subsequent -U option.

           -T dev Prepare output for device dev.  The default is ps; see
                  groff(1).

           -U     Operate in unsafe mode, enabling the cf, open, opena, pi,
                  pso, and sy requests, which are disabled by default because
                  they allow an untrusted input document to run arbitrary
                  commands, put arbitrary content into troff output, or write
                  to arbitrary file names.  (GNU troff does not, however,
                  accept newlines (line feeds) in file names supplied as
                  arguments to requests.)  This option also adds the current
                  directory to the macro package search path; see the -m and
                  -M options above.

           -w cat
           -W cat Enable and inhibit, respectively, warnings in category cat.
                  See section “Warnings” below.

           -z     Suppress formatted output.

## [](#Warnings)Warnings

           GNU troff divides its warning diagnostics into named, numbered
           categories.  The -w and -W options use the associated names.  A
           power of two characterizes each category; the warn request and the
           .warn register respectively set and report the sum of enabled
           category codes.  Warnings of each category are produced under the
           following circumstances.

                 ┌───────────────────────┬──────────────────────────┐
                 │ Bit   Code   Category │ Bit    Code     Category │
                 ├───────────────────────┼──────────────────────────┤
                 │   0      1   char     │  10      1024   reg      │
                 │   1      2   unused   │  11      2048   tab      │
                 │   2      4   break    │  12      4096   unused   │
                 │   3      8   delim    │  13      8192   missing  │
                 │   4     16   unused   │  14     16384   input    │
                 │   5     32   scale    │  15     32768   escape   │
                 │   6     64   range    │  16     65536   space    │
                 │   7    128   syntax   │  17    131072   font     │
                 │   8    256   di       │  18    262144   ig       │
                 │   9    512   mac      │  19    524288   color    │
                 │                       │  20   1048576   file     │
                 └───────────────────────┴──────────────────────────┘

           break           4   A filled output line could not be broken such
                               that its length was less than or equal to, or
                               adjusted such that its length was exactly
                               equal to, the output line length “\n[.l]”.
                               GNU troff reports the amount of overset or
                               underset in the scaling unit configured by the
                               warnscale request in troff mode, and in ens
                               (‘n’; character cells) in nroff mode.  This
                               category is enabled by default.

           char            1   No user-defined character of the requested
                               name or index exists and no mounted font
                               defines a glyph for it, or input could not be
                               encoded for device-independent output.  This
                               category is enabled by default.

           color      524288   An undefined color name was selected, an
                               attempt was made to define a color using an
                               unrecognized color space, an invalid channel
                               value in a color definition was encountered,
                               or an attempt was made to redefine a default
                               color.

           delim           8   The selected delimiter character was ambiguous
                               because it is also meaningful when beginning a
                               numeric expression, or the closing delimiter
                               in an escape sequence was missing or
                               mismatched.

                               A future groff release may reject ambiguous
                               delimiters.  In compatibility mode, ambiguous
                               delimiters are accepted without warning.

           di            256   A di, da, box, or boxa request was invoked
                               without an argument when there was no current
                               diversion.

           escape      32768   An unsupported escape sequence was
                               encountered.

           file      1048576   An attempt was made to read a file that does
                               not exist.  or a stream remained open at
                               formatter exit.  This category is enabled by
                               default.

           font       131072   A non-existent font was selected.  This
                               category is enabled by default.

           ig         262144   An invalid escape sequence occurred in input
                               ignored using the ig request.  This warning
                               category diagnoses a condition that is an
                               error when it occurs in non-ignored input.

           input       16384   An invalid character occurred on the input
                               stream.

           mac           512   An undefined string, macro, or diversion was
                               used.  When such an object is dereferenced, an
                               empty one of that name is automatically
                               created.  So, unless it is later deleted,
                               troff issues at most one warning for each.

                               troff also uses this category to warn of an
                               attempt to move an unplanted trap macro.  In
                               such cases, the unplanted macro is not
                               dereferenced, so it is not created if it does
                               not exist.

           missing      8192   A request was invoked with a mandatory
                               argument absent.

           range          64   A numeric expression was out of range for its
                               context.

           reg          1024   An undefined register was used.  When an
                               undefined register is dereferenced, the
                               formatter automatically defines it with a
                               value of 0.  So, unless it is later deleted,
                               GNU troff issues at most one warning for each.

           scale          32   A scaling unit inappropriate to its context
                               was used in a numeric expression.

           space       65536   A space was missing between a request or macro
                               and its argument.  This warning is produced
                               when an undefined name longer than two
                               characters is encountered and the first two
                               characters of the name constitute a defined
                               name.  No request is invoked, no macro called,
                               and an empty macro is not defined.  This
                               category is enabled by default.  It never
                               occurs in compatibility mode.

           syntax        128   A self-contradictory hyphenation mode or
                               character flags were requested; an empty or
                               incomplete numeric expression was encountered;
                               an operand to a numeric operator was missing;
                               an attempt was made to format characters or
                               spaces on an input line after an output line
                               continuation escape sequence; a recognized but
                               inapposite escape sequence or unprintable
                               character code was used in a device extension
                               command; an attempt was made to define a
                               recursive, empty, or nonsensical character
                               class; or a groff extension escape sequence or
                               conditional expression operator was used while
                               in compatibility mode.

           tab          2048   A tab character appeared in a parameterized
                               escape sequence, in an unquoted macro
                               argument, or where a request expected a
                               numeric expression argument.

           Two warning names group other warning categories for convenience.

           all    All warning categories except di, mac, and reg.  This
                  shorthand is intended to produce all warnings that are
                  useful with macro packages and documents written for AT&T
                  troff and its descendants, which have less fastidious
                  diagnostics than GNU troff.

           w      All warning categories.  Authors of documents and macro
                  packages targeting groff are encouraged to use this
                  setting.

## [](#Exit_status)Exit status

           troff exits with status 0 on successful operation, status 2 if the
           program cannot interpret its command-line arguments, and status 1
           if it encounters a fatal error during operation, or is directed to
           abort by the input.

## [](#Environment)Environment

           GROFF_FONT_PATH and GROFF_TMAC_PATH each accept a search path of
           directories; that is, a list of directory names separated by the
           system's path component separator character.  On Unix systems,
           this character is a colon (:); on Windows systems, it is a
           semicolon (;).

           GROFF_FONT_PATH
                  A list of directories in which to seek the selected output
                  device's directory of device and font description files.
                  troff will scan directories given as arguments to any
                  specified -F options before these, then in a site-specific
                  directory (/usr/local/share/groff/site-font), a standard
                  location (/usr/local/share/groff/1.24.1/font), and a
                  compatibility directory (/usr/lib/font) after them.

           GROFF_TMAC_PATH
                  A list of directories in which to search for macro files.
                  troff will scan directories given as arguments to any
                  specified -M options before these, then the current
                  directory (only if in unsafe mode), the user's home
                  directory, a site-specific directory (/usr/local/share/
                  groff/site-tmac), and a standard location (/usr/local/
                  share/groff/1.24.1/tmac) after them.

           GROFF_TYPESETTER
                  Set the default output device.  If empty or not set, ps is
                  used.  The -T option overrides GROFF_TYPESETTER.

           SOURCE_DATE_EPOCH
                  A timestamp (expressed as seconds since the Unix epoch) to
                  use as the output creation timestamp in place of the
                  current time.  The time is converted to human-readable form
                  using gmtime(3) and asctime(3) when the formatter starts up
                  and stored in registers usable by documents and macro
                  packages.

           TZ     The time zone to use when converting the current time to
                  human-readable form; see tzset(3).  If SOURCE_DATE_EPOCH is
                  used, it is always converted to human-readable form using
                  UTC.

## [](#Files)Files

           /usr/local/share/groff/1.24.1/tmac/troffrc
                  is an initialization macro file loaded before any macro
                  packages specified with -m options.

           /usr/local/share/groff/1.24.1/tmac/troffrc-end
                  is an initialization macro file loaded after all macro
                  packages specified with -m options.

           /usr/local/share/groff/1.24.1/tmac/name.tmac
                  are macro files distributed with groff.

           /usr/local/share/groff/1.24.1/font/devname/DESC
                  describes the output device name.

           /usr/local/share/groff/1.24.1/font/devname/F
                  describes the font F of device name.

           troffrc and troffrc-end are sought neither in the current nor the
           home directory by default for security reasons, even if the -U
           option is specified.  Use the -M command-line option or the
           GROFF_TMAC_PATH environment variable to add these directories to
           the search path if necessary.

## [](#Authors)Authors

           The GNU version of troff was originally written by James Clark; he
           also wrote the original version of this document, which was
           updated by Werner Lemberg ⟨wl@gnu.org⟩, Bernd Warken ⟨groff-bernd
           .warken-72@web.de⟩, and G. Branden Robinson ⟨g.branden.robinson@
           gmail.com⟩.

## [](#See_also)See also

           Groff: The GNU Implementation of troff, by Trent A. Fisher and
           Werner Lemberg, is the primary groff manual.  You can browse it
           interactively with “info groff”.

           groff(1)
                  offers an overview of the GNU roff system and describes its
                  front end executable.

           groff(7)
                  details the groff language, including a short but complete
                  reference of all predefined requests, registers, and escape
                  sequences.

           groff_char(7)
                  explains the syntax of groff special character escape
                  sequences, and lists all special characters predefined by
                  the language.

           groff_diff(7)
                  enumerates the differences between AT&T device-independent
                  troff and groff.

           groff_font(5)
                  covers the format of groff device and font description
                  files.

           groff_out(5)
                  describes the format of troff's output.

           groff_tmac(5)
                  includes information about macro files that ship with
                  groff.

           roff(7)
                  supplies background on roff systems in general, including
                  pointers to further related documentation.

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

    groff 1.24.1                    2026-03-14                       troff(1)

------------------------------------------------------------------------

Pages that refer to this page: [colcrt(1)](../man1/colcrt.1.html),  [man(1)](../man1/man.1.html),  [zsoelim(1)](../man1/zsoelim.1.html)

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
