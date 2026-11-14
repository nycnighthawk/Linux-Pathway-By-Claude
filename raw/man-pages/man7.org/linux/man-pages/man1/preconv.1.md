---
{"title": "preconv(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/preconv.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# preconv(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Synopsis](#Synopsis) \| [Description](#Description) \| [Options](#Options) \| [Exit status](#Exit_status) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    preconv(1)               General Commands Manual               preconv(1)

## [](#Name)Name

           preconv - prepare files for typesetting with groff

## [](#Synopsis)Synopsis

           preconv [-dr] [-D fallback-encoding] [-e encoding] [file ...]

           preconv -h

           preconv --help

           preconv -v

           preconv --version

## [](#Description)Description

           preconv reads each file, converts its encoded characters to a form
           troff(1) can interpret, and sends the result to the standard
           output stream.  Currently, this means that code points in the
           range 0–127 in ISO 646:1991 IRV (US-ASCII), ISO 8859, or Unicode
           remain as-is and the remainder are converted to the groff special
           character form “\[uXXXX]”, where XXXX is a hexadecimal number of
           four to six digits corresponding to a Unicode code point.  By
           default, preconv also inserts a roff .lf request at the beginning
           of each file, identifying it for the benefit of later processing
           (including diagnostic messages); the -r option suppresses this
           behavior.

           In typical usage scenarios, preconv need not be run directly;
           instead it should be invoked with the -k or -K options of groff.
           If no file operands are present, or if file is “-”, preconv reads
           the standard input stream.

           preconv selects an input encoding with the following algorithm,
           stopping at the first success.

           1.  If the input encoding has been explicitly specified with
               option -e, use it.

           2.  If the input starts with a Unicode Byte Order Mark, select
               UTF-8, UTF-16, or UTF-32 accordingly.

           3.  If the input stream is seekable, check the first two input
               lines for a GNU Emacs file-local variable identifying the
               character encoding, here referred to as the “coding tag”.  If
               found, use it.

           4.  If the input stream is seekable, and if the uchardet library
               is available on the system, use it to try to infer the
               encoding of the file.

           5.  If the -D option specifies an encoding, use it.

           6.  Use the encoding specified by the current locale (LC_CTYPE),
               unless the locale is “C”, “POSIX”, or empty, in which case
               assume ISO Latin-1 (8859-1).

           The coding tag and uchardet methods in the above procedure rely
           upon a seekable input stream; when preconv reads from a pipe, the
           stream is not seekable, and these detection methods are skipped.
           If character encoding detection of your input is unreliable,
           arrange for one of the other methods to succeed by using preconv's
           -D or -e options, or by configuring your locale appropriately.
           groff also supports a GROFF_ENCODING environment variable, which
           can be overridden by its -K option.  Valid values for (or
           parameters to) all of these are enumerated in the lists of
           recognized coding tags in the next subsection, and are further
           influenced by iconv library support.

       Coding tags
           Text editors that support more than a single character encoding
           need tags within the input files to mark the file's encoding.
           While it is possible to guess the right input encoding with the
           help of heuristics that produce good results for a preponderance
           of natural language texts, they are not absolutely reliable.
           Heuristics can fail on inputs that are too short or don't
           represent a natural language.

           Consequently, preconv supports the coding tag convention used by
           GNU Emacs (with some restrictions).  This notation appears in
           specially marked regions of an input file designated for “file-
           local variables”.

           preconv interprets the following syntax if it occurs in a roff
           comment in the first or second line of the input.  Both “\"” and
           “\#” comment forms are recognized, but the control (or no-break
           control) character must be the default and must begin the line.
           Similarly, the escape character must be the default.
                  -*- [...;] coding: encoding[; ...] -*-

           The only variable preconv interprets is “coding”, which can take
           the values listed below.

           The following list comprises all MIME “charset” parameter values
           recognized, case-insensitively, by preconv.
                  big5, cp1047, euc-jp, euc-kr, gb2312, iso-8859-1,
                  iso-8859-2, iso-8859-5, iso-8859-7, iso-8859-9,
                  iso-8859-13, iso-8859-15, koi8-r, us-ascii, utf-8, utf-16,
                  utf-16be, utf-16le

           In addition, the following list of other coding tags is
           recognized, each of which is mapped to an appropriate value from
           the list above.
                  ascii, chinese-big5, chinese-euc, chinese-iso-8bit,
                  cn-big5, cn-gb, cn-gb-2312, cp878, csascii, csisolatin1,
                  cyrillic-iso-8bit, cyrillic-koi8, euc-china, euc-cn,
                  euc-japan, euc-japan-1990, euc-korea, greek-iso-8bit,
                  iso-10646/utf8, iso-10646/utf-8, iso-latin-1, iso-latin-2,
                  iso-latin-5, iso-latin-7, iso-latin-9, japanese-euc,
                  japanese-iso-8bit, jis8, koi8, korean-euc, korean-iso-8bit,
                  latin-0, latin1, latin-1, latin-2, latin-5, latin-7,
                  latin-9, mule-utf-8, mule-utf-16, mule-utf-16be,
                  mule-utf-16-be, mule-utf-16be-with-signature,
                  mule-utf-16le, mule-utf-16-le,
                  mule-utf-16le-with-signature, utf8, utf-16-be,
                  utf-16-be-with-signature, utf-16be-with-signature,
                  utf-16-le, utf-16-le-with-signature,
                  utf-16le-with-signature

           Any “-dos”, “-unix”, or “-mac” suffix on a coding tag (which
           indicates the end-of-line convention used in the file) is ignored
           during comparison with the above tags.

       [1miconv[24m support
           While preconv recognizes all of the coding tags listed above, it
           is capable on its own of interpreting only two encodings:
           ISO Latin-1 and and UTF-8.  ISO 646:1991 IRV (US-ASCII) is a
           proper subset of both these encodings.  If iconv(3) support is
           configured at compile time and available at run time, all others
           are passed to iconv library functions, which may recognize many
           additional encoding strings.  The command “preconv -v” discloses
           whether iconv support is configured.

           The use of iconv means that characters in the input that encode
           invalid code points for that encoding may be dropped from the
           output stream or mapped to the Unicode replacement character
           (U+FFFD).  Compare the following examples using the input “café”
           (note the “e” with an acute accent), which due to its short length
           challenges inference of the encoding used.
                  printf 'caf\351\n' | LC_ALL=en_US.UTF-8 preconv
                  printf 'caf\351\n' | preconv -e us-ascii
                  printf 'caf\351\n' | preconv -e latin-1
           The fate of the accented “e” differs in each case.  In the first,
           uchardet fails to detect an encoding (though the library on your
           system may behave differently) and preconv falls back to the
           locale settings, where octal 351 starts an incomplete UTF-8
           sequence and results in the Unicode replacement character.  In the
           second, it is not a representable character in the declared input
           encoding of US-ASCII and is discarded by iconv.  In the last, it
           is correctly detected and mapped.

       Limitations
           preconv cannot perform any transformation on input that it cannot
           see.  Examples include files that are interpolated by
           preprocessors that run subsequently, including soelim(1); files
           included by troff itself through “so” and similar requests; and
           string definitions passed to troff through its -d command-line
           option.

           preconv assumes that its input uses the default escape character,
           a backslash \, and writes special character escape sequences
           accordingly.

## [](#Options)Options

           -h and --help display a usage message, while -v and --version show
           version and configuration information; all exit afterward.

           -d     Emit debugging messages to the standard error stream.

           -D fbenc
                  Select the fallback encoding fbenc if all detection methods
                  fail.

           -e enc Skip detection and select encoding enc; see groff's -K
                  option.

           -r     Write files “raw”; do not add .lf requests.

## [](#Exit_status)Exit status

           preconv exits with status 0 on successful operation, status 2 if
           the program cannot interpret its command-line arguments, and
           status 1 if it encounters an error during operation.

## [](#See_also)See also

           groff(1), iconv(3), locale(7)

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

    groff 1.24.1                    2026-03-14                     preconv(1)

------------------------------------------------------------------------

Pages that refer to this page: [groff(1)](../man1/groff.1.html)

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
