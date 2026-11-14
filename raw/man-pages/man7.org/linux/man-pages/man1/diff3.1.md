---
{"title": "diff3(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/diff3.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# diff3(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DIFF3(1)                      User Commands                      DIFF3(1)

## [](#NAME)NAME

           diff3 - compare three files line by line

## [](#SYNOPSIS)SYNOPSIS

           diff3 [OPTION]... MYFILE OLDFILE YOURFILE

## [](#DESCRIPTION)DESCRIPTION

           Compare three files line by line.

           Mandatory arguments to long options are mandatory for short
           options too.

           -A, --show-all
                  output all changes, bracketing conflicts

           -e, --ed
                  output ed script incorporating changes from OLDFILE to
                  YOURFILE into MYFILE

           -E, --show-overlap
                  like -e, but bracket conflicts

           -3, --easy-only
                  like -e, but incorporate only nonoverlapping changes

           -x, --overlap-only
                  like -e, but incorporate only overlapping changes

           -X     like -x, but bracket conflicts

           -i     append 'w' and 'q' commands to ed scripts

           -m, --merge
                  output actual merged file, according to -A if no other
                  options are given

           -a, --text
                  treat all files as text

           --strip-trailing-cr
                  strip trailing carriage return on input

           -T, --initial-tab
                  make tabs line up by prepending a tab

           --diff-program=PROGRAM
                  use PROGRAM to compare files

           -L, --label=LABEL
                  use LABEL instead of file name (can be repeated up to three
                  times)

           --help display this help and exit

           -v, --version
                  output version information and exit

           The default output format is a somewhat human-readable
           representation of the changes.

           The -e, -E, -x, -X (and corresponding long) options cause an ed
           script to be output instead of the default.

           Finally, the -m (--merge) option causes diff3 to do the merge
           internally and output the actual merged file.  For unusual input,
           this is more robust than using ed.

           If a FILE is '-', read standard input.  Exit status is 0 if
           successful, 1 if conflicts, 2 if trouble.

## [](#AUTHOR)AUTHOR

           Written by Randy Smith.

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

           cmp(1), diff(1), sdiff(1)

           The full documentation for diff3 is maintained as a Texinfo
           manual.  If the info and diff3 programs are properly installed at
           your site, the command

                  info diff3

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

    diffutils 3.12.26-bbc1         August 2026                       DIFF3(1)

------------------------------------------------------------------------

Pages that refer to this page: [cmp(1)](../man1/cmp.1.html),  [diff(1)](../man1/diff.1.html),  [patch(1)](../man1/patch.1.html),  [sdiff(1)](../man1/sdiff.1.html)

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
