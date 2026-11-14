---
{"title": "uniq(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/uniq.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uniq(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UNIQ(1)                       User Commands                       UNIQ(1)

## [](#NAME)NAME

           uniq - report or omit repeated lines

## [](#SYNOPSIS)SYNOPSIS

           uniq [OPTION]... [INPUT [OUTPUT]]

## [](#DESCRIPTION)DESCRIPTION

           Filter adjacent matching lines from INPUT (or standard input),
           writing to OUTPUT (or standard output).

           With no options, matching lines are merged to the first
           occurrence.

           Mandatory arguments to long options are mandatory for short
           options too.

           -c, --count
                  prefix lines by the number of occurrences

           -d, --repeated
                  only print duplicate lines, one for each group

           -D     print all duplicate lines

           --all-repeated[=METHOD]
                  like -D, but allow separating groups with an empty line;
                  METHOD={none(default),prepend,separate}

           -f, --skip-fields=N
                  avoid comparing the first N fields

           --group[=METHOD]
                  show all items, separating groups with an empty line;
                  METHOD={separate(default),prepend,append,both}

           -i, --ignore-case
                  ignore differences in case when comparing

           -s, --skip-chars=N
                  avoid comparing the first N characters

           -u, --unique
                  only print unique lines

           -z, --zero-terminated
                  line delimiter is NUL, not newline

           -w, --check-chars=N
                  compare no more than N characters in lines

           --help display this help and exit

           --version
                  output version information and exit

           A field is a run of blanks (usually spaces and/or TABs), then
           non-blank characters.  Fields are skipped before chars.

           'uniq' does not detect repeated lines unless they are adjacent.
           You may want to sort the input first, or use 'sort -u' without
           'uniq'.

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

           comm(1), join(1), sort(1)

           Full documentation <https://www.gnu.org/software/coreutils/uniq>
           or available locally via: info '(coreutils) uniq invocation'

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

    GNU coreutils 9.11              April 2026                        UNIQ(1)

------------------------------------------------------------------------

Pages that refer to this page: [comm(1)](../man1/comm.1.html),  [join(1)](../man1/join.1.html),  [sort(1)](../man1/sort.1.html)

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
