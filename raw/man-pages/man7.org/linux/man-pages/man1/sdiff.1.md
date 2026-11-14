---
{"title": "sdiff(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/sdiff.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sdiff(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SDIFF(1)                      User Commands                      SDIFF(1)

## [](#NAME)NAME

           sdiff - side-by-side merge of file differences

## [](#SYNOPSIS)SYNOPSIS

           sdiff [OPTION]... FILE1 FILE2

## [](#DESCRIPTION)DESCRIPTION

           Side-by-side merge of differences between FILE1 and FILE2.

           Mandatory arguments to long options are mandatory for short
           options too.

           -o, --output=FILE
                  operate interactively, sending output to FILE

           -i, --ignore-case
                  consider upper- and lower-case to be the same

           -E, --ignore-tab-expansion
                  ignore changes due to tab expansion

           -Z, --ignore-trailing-space
                  ignore white space at line end

           -b, --ignore-space-change
                  ignore changes in the amount of white space

           -W, --ignore-all-space
                  ignore all white space

           -B, --ignore-blank-lines
                  ignore changes whose lines are all blank

           -I, --ignore-matching-lines=RE
                  ignore changes all whose lines match RE

           --strip-trailing-cr
                  strip trailing carriage return on input

           -a, --text
                  treat all files as text

           -w, --width=NUM
                  output at most NUM (default 130) print columns

           -l, --left-column
                  output only the left column of common lines

           -s, --suppress-common-lines
                  do not output common lines

           -t, --expand-tabs
                  expand tabs to spaces in output

           --tabsize=NUM
                  tab stops at every NUM (default 8) print columns

           -d, --minimal
                  try hard to find a smaller set of changes

           -H, --speed-large-files
                  assume large files, many scattered small changes

           --diff-program=PROGRAM
                  use PROGRAM to compare files

           --help display this help and exit

           -v, --version
                  output version information and exit

           If a FILE is '-', read standard input.  Exit status is 0 if inputs
           are the same, 1 if different, 2 if trouble.

## [](#AUTHOR)AUTHOR

           Written by Thomas Lord.

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

           cmp(1), diff(1), diff3(1)

           The full documentation for sdiff is maintained as a Texinfo
           manual.  If the info and sdiff programs are properly installed at
           your site, the command

                  info sdiff

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

    diffutils 3.12.26-bbc1         August 2026                       SDIFF(1)

------------------------------------------------------------------------

Pages that refer to this page: [cmp(1)](../man1/cmp.1.html),  [diff(1)](../man1/diff.1.html),  [diff3(1)](../man1/diff3.1.html)

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
