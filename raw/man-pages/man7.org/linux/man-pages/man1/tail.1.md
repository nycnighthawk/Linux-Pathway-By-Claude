---
{"title": "tail(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/tail.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tail(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TAIL(1)                       User Commands                       TAIL(1)

## [](#NAME)NAME

           tail - output the last part of files

## [](#SYNOPSIS)SYNOPSIS

           tail [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           Print the last 10 lines of each FILE to standard output.  With
           more than one FILE, precede each with a header giving the file
           name.

           With no FILE, or when FILE is -, read standard input.

           Mandatory arguments to long options are mandatory for short
           options too.

           -c, --bytes=[+]NUM
                  output the last NUM bytes; or use -c +NUM to output
                  starting with byte NUM of each file

           --debug
                  indicate which --follow implementation is used

           -f, --follow[={name|descriptor}]
                  output appended data as the file grows; an absent option
                  argument means 'descriptor'

           -F     same as --follow=name --retry

           -n, --lines=[+]NUM
                  output the last NUM lines, instead of the last 10; or use
                  -n +NUM to skip NUM-1 lines at the start

           --max-unchanged-stats=N
                  with --follow=name, reopen a FILE which has not changed
                  size after N (default 5) iterations to see if it has been
                  unlinked or renamed (this is the usual case of rotated log
                  files); with inotify, this option is rarely useful

           --pid=PID
                  with -f, exit after PID no longer exists; can be repeated
                  to watch multiple processes

           -q, --quiet, --silent
                  never output headers giving file names

           --retry
                  keep trying to open a file if it is inaccessible

           -s, --sleep-interval=N
                  with -f, sleep for approximately N seconds (default 1.0)
                  between iterations; with inotify and --pid=P, check process
                  P at least once every N seconds

           -v, --verbose
                  always output headers giving file names

           -z, --zero-terminated
                  line delimiter is NUL, not newline

           --help display this help and exit

           --version
                  output version information and exit

           NUM may have a multiplier suffix: b 512, kB 1000, K 1024, MB
           1000*1000, M 1024*1024, GB 1000*1000*1000, G 1024*1024*1024, and
           so on for T, P, E, Z, Y, R, Q.  Binary prefixes can be used, too:
           KiB=K, MiB=M, and so on.

           With --follow (-f), tail defaults to following the file
           descriptor, which means that even if a tail'ed file is renamed,
           tail will continue to track its end.  This default behavior is not
           desirable when you really want to track the actual name of the
           file, not the file descriptor (e.g., log rotation).  Use
           --follow=name in that case.  That causes tail to track the named
           file in a way that accommodates renaming, removal and creation.

## [](#AUTHOR)AUTHOR

           Written by Paul Rubin, David MacKenzie, Ian Lance Taylor, and Jim
           Meyering.

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

           head(1)

           Full documentation <https://www.gnu.org/software/coreutils/tail>
           or available locally via: info '(coreutils) tail invocation'

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

    GNU coreutils 9.11              April 2026                        TAIL(1)

------------------------------------------------------------------------

Pages that refer to this page: [head(1)](../man1/head.1.html),  [pmcd(1)](../man1/pmcd.1.html),  [pmdalogger(1)](../man1/pmdalogger.1.html),  [pmdasystemd(1)](../man1/pmdasystemd.1.html),  [pmdaweblog(1)](../man1/pmdaweblog.1.html),  [pon(1)](../man1/pon.1.html)

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
