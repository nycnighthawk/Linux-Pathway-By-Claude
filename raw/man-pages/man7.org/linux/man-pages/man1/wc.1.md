---
{"title": "wc(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/wc.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# wc(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WC(1)                         User Commands                         WC(1)

## [](#NAME)NAME

           wc - print newline, word, and byte counts for each file

## [](#SYNOPSIS)SYNOPSIS

           wc [OPTION]... [FILE]...
           wc [OPTION]... --files0-from=F

## [](#DESCRIPTION)DESCRIPTION

           Print newline, word, and byte counts for each FILE, and a total
           line if more than one FILE is specified.  A word is a nonempty
           sequence of non white space delimited by white space characters or
           by start or end of input.

           With no FILE, or when FILE is -, read standard input.

           The options below may be used to select which counts are printed,
           always in the following order: newline, word, character, byte,
           maximum line length.

           -c, --bytes
                  print the byte counts

           -m, --chars
                  print the character counts

           -l, --lines
                  print the newline counts

           --debug
                  indicate what line count acceleration is used

           --files0-from=F
                  read input from the files specified by NUL-terminated names
                  in file F; If F is -, read names from standard input

           -L, --max-line-length
                  print the maximum display width

           -w, --words
                  print the word counts

           --total=WHEN
                  when to print a line with total counts; WHEN can be: auto,
                  always, only, never

           --help display this help and exit

           --version
                  output version information and exit

## [](#AUTHOR)AUTHOR

           Written by Paul Rubin and David MacKenzie.

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

           Full documentation <https://www.gnu.org/software/coreutils/wc>
           or available locally via: info '(coreutils) wc invocation'

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

    GNU coreutils 9.11              April 2026                          WC(1)

------------------------------------------------------------------------

Pages that refer to this page: [bridge(8)](../man8/bridge.8.html),  [ip(8)](../man8/ip.8.html),  [tc(8)](../man8/tc.8.html)

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
