---
{"title": "cmp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cmp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cmp(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CMP(1)                        User Commands                        CMP(1)

## [](#NAME)NAME

           cmp - compare two files byte by byte

## [](#SYNOPSIS)SYNOPSIS

           cmp [OPTION]... FILE1 [FILE2 [SKIP1 [SKIP2]]]

## [](#DESCRIPTION)DESCRIPTION

           Compare two files byte by byte. Byte and line numbers start with
           1.

           The optional SKIP1 and SKIP2 specify the number of bytes to skip
           at the beginning of each file (zero by default).

           Mandatory arguments to long options are mandatory for short
           options too.

           -b, --print-bytes
                  print differing bytes

           -i, --ignore-initial=SKIP
                  skip first SKIP bytes of both inputs

           -i, --ignore-initial=SKIP1:SKIP2
                  skip first SKIP1 bytes of FILE1 and first SKIP2 bytes of
                  FILE2

           -l, --verbose
                  output decimal byte numbers and differing byte values in
                  octal

           -n, --bytes=LIMIT
                  compare at most LIMIT bytes

           -s, --quiet, --silent
                  suppress all normal output

           --help display this help and exit

           -v, --version
                  output version information and exit

           SKIP values may be followed by the following multiplicative
           suffixes: kB 1000, K 1024, MB 1,000,000, M 1,048,576, GB
           1,000,000,000, G 1,073,741,824, and so on for T, P, E, Z, Y.

           If a FILE is '-' or missing, read standard input.  Exit status is
           0 if inputs are the same, 1 if different, 2 if trouble.

## [](#AUTHOR)AUTHOR

           Written by Torbjorn Granlund and David MacKenzie.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to: bug-diffutils@gnu.org
           GNU diffutils home page: <https://www.gnu.org/software/diffutils/>
           General help using GNU software: <https://www.gnu.org/gethelp/>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2026 Free Software Foundation, Inc.  License GPLv3+:
           GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
           This is free software: you are free to change and redistribute it.
           There is NO WARRANTY, to the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           diff(1), diff3(1), sdiff(1)

           The full documentation for cmp is maintained as a Texinfo manual.
           If the info and cmp programs are properly installed at your site,
           the command

                  info cmp

           should give you access to the complete manual.

## [](#COLOPHON)COLOPHON

           This page is part of the diffutils (GNU diff utilities) project.
           Information about the project can be found at 
           ⟨http://savannah.gnu.org/projects/diffutils/⟩.  If you have a bug
           report for this manual page, send it to bug-diffutils@gnu.org.
           This page was obtained from the project's upstream Git repository
           ⟨git://git.savannah.gnu.org/diffutils.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-06-20.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    diffutils 3.12.26-bbc1         August 2026                         CMP(1)

------------------------------------------------------------------------

Pages that refer to this page: [diff(1)](../man1/diff.1.html),  [diff3(1)](../man1/diff3.1.html),  [grep(1)](../man1/grep.1.html),  [sdiff(1)](../man1/sdiff.1.html)

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
