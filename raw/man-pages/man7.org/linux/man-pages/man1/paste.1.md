---
{"title": "paste(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/paste.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# paste(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PASTE(1)                      User Commands                      PASTE(1)

## [](#NAME)NAME

           paste - merge lines of files

## [](#SYNOPSIS)SYNOPSIS

           paste [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           Write lines consisting of the sequentially corresponding lines
           from each FILE, separated by TABs, to standard output.  The
           newline of every line except the line from the last file is
           replaced with a TAB.

           With no FILE, or when FILE is -, read standard input.

           Mandatory arguments to long options are mandatory for short
           options too.

           -d, --delimiters=LIST
                  reuse characters from LIST instead of TABs; backslash
                  escapes are supported

           -s, --serial
                  paste one file at a time instead of in parallel; the
                  newline of every line except the last line in each file is
                  replaced with a TAB

           -z, --zero-terminated
                  line delimiter is NUL, not newline

           --help display this help and exit

           --version
                  output version information and exit

## [](#AUTHOR)AUTHOR

           Written by David M. Ihnat and David MacKenzie.

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

           Full documentation <https://www.gnu.org/software/coreutils/paste>
           or available locally via: info '(coreutils) paste invocation'

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

    GNU coreutils 9.11              April 2026                       PASTE(1)

------------------------------------------------------------------------

Pages that refer to this page: [colrm(1)](../man1/colrm.1.html),  [column(1)](../man1/column.1.html)

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
