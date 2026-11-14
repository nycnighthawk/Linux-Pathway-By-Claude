---
{"title": "head(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/head.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# head(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    HEAD(1)                       User Commands                       HEAD(1)

## [](#NAME)NAME

           head - output the first part of files

## [](#SYNOPSIS)SYNOPSIS

           head [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           Print the first 10 lines of each FILE to standard output.  With
           more than one FILE, precede each with a header giving the file
           name.

           With no FILE, or when FILE is -, read standard input.

           Mandatory arguments to long options are mandatory for short
           options too.

           -c, --bytes=[-]NUM
                  print the first NUM bytes of each file; with the leading
                  '-', print all but the last NUM bytes of each file

           -n, --lines=[-]NUM
                  print the first NUM lines instead of the first 10; with the
                  leading '-', print all but the last NUM lines of each file

           -q, --quiet, --silent
                  never print headers giving file names

           -v, --verbose
                  always print headers giving file names

           -z, --zero-terminated
                  line delimiter is NUL, not newline

           --help display this help and exit

           --version
                  output version information and exit

           NUM may have a multiplier suffix: b 512, kB 1000, K 1024, MB
           1000*1000, M 1024*1024, GB 1000*1000*1000, G 1024*1024*1024, and
           so on for T, P, E, Z, Y, R, Q.  Binary prefixes can be used, too:
           KiB=K, MiB=M, and so on.

## [](#AUTHOR)AUTHOR

           Written by David MacKenzie and Jim Meyering.

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

           tail(1)

           Full documentation <https://www.gnu.org/software/coreutils/head>
           or available locally via: info '(coreutils) head invocation'

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

    GNU coreutils 9.11              April 2026                        HEAD(1)

------------------------------------------------------------------------

Pages that refer to this page: [tail(1)](../man1/tail.1.html)

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
