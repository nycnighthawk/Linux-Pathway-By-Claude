---
{"title": "comm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/comm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# comm(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    COMM(1)                       User Commands                       COMM(1)

## [](#NAME)NAME

           comm - compare two sorted files line by line

## [](#SYNOPSIS)SYNOPSIS

           comm [OPTION]... FILE1 FILE2

## [](#DESCRIPTION)DESCRIPTION

           Compare sorted files FILE1 and FILE2 line by line.

           When FILE1 or FILE2 (not both) is -, read standard input.

           With no options, produce three-column output.  Column one contains
           lines unique to FILE1, column two contains lines unique to FILE2,
           and column three contains lines common to both files.

           -1     suppress column 1 (lines unique to FILE1)

           -2     suppress column 2 (lines unique to FILE2)

           -3     suppress column 3 (lines that appear in both files)

           --check-order
                  check that the input is correctly sorted, even if all input
                  lines are pairable

           --nocheck-order
                  do not check that the input is correctly sorted

           --output-delimiter=STR
                  separate columns with STR

           --total
                  output a summary

           -z, --zero-terminated
                  line delimiter is NUL, not newline

           --help display this help and exit

           --version
                  output version information and exit

           Comparisons honor the rules specified by 'LC_COLLATE'.

## [](#EXAMPLES)EXAMPLES

           comm -12 file1 file2
                  Print only lines present in both file1 and file2.

           comm -3 file1 file2
                  Print lines in file1 not in file2, and vice versa.

## [](#AUTHOR)AUTHOR

           Written by Richard M. Stallman and David MacKenzie.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to: bug-coreutils@gnu.org
           GNU coreutils home page: <https://www.gnu.org/software/coreutils/>
           General help using GNU software: <https://www.gnu.org/gethelp/>
           Report any translation bugs to
           <https://translationproject.org/team/>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2026 Free Software Foundation, Inc.  License GPLv3+:
           GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
           This is free software: you are free to change and redistribute it.
           There is NO WARRANTY, to the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           join(1), uniq(1)

           Full documentation <https://www.gnu.org/software/coreutils/comm>
           or available locally via: info '(coreutils) comm invocation'

## [](#COLOPHON)COLOPHON

           This page is part of the coreutils (basic file, shell and text
           manipulation utilities) project.  Information about the project
           can be found at ⟨http://www.gnu.org/software/coreutils/⟩.  If you
           have a bug report for this manual page, see
           ⟨http://www.gnu.org/software/coreutils/⟩.  This page was obtained
           from the tarball coreutils-9.11.tar.xz fetched from
           ⟨http://ftp.gnu.org/gnu/coreutils/⟩ on 2026-08-03.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    GNU coreutils 9.11              April 2026                        COMM(1)

------------------------------------------------------------------------

Pages that refer to this page: [join(1)](../man1/join.1.html),  [uniq(1)](../man1/uniq.1.html)

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
