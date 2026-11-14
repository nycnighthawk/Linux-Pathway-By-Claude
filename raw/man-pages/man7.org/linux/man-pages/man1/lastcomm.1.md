---
{"title": "lastcomm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lastcomm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lastcomm(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LASTCOMM(1)              General Commands Manual              LASTCOMM(1)

## [](#NAME)NAME

           lastcomm -  print out information about previously executed
           commands.

## [](#SYNOPSIS)SYNOPSIS

           lastcomm
                  [ command-name ...  ]
                  [ user-name ...  ]
                  [ terminal-name ...  ]
                  [ OPTION ... ]

## [](#DESCRIPTION)DESCRIPTION

           lastcomm  prints  out  information  about previously executed com‐
           mands.  If no arguments are specified, lastcomm  will  print  info
           about  all  of  the commands in acct (the record file).  If called
           with one or more of command-name, user-name, or terminal-name, on‐
           ly records containing those items will be displayed.  For example,
           to find out which users used command `a.out' and which users  were
           logged into `tty0', type:
                                  lastcomm a.out tty0

           This  will  print any entry for which `a.out' or `tty0' matches in
           any of the record's fields (command, name, or terminal).   If  you
           want  to  find only items that match *all* of the arguments on the
           command line, you must use the '-strict-match' option.  For  exam‐
           ple,  to  list all of the executions of command a.out by user root
           on terminal tty0, type:
             lastcomm --strict-match --command a.out --user root --tty tty0

           The order of the arguments is not important.

           For each entry the following information is printed:
              + command name of the process
              + flags, as recorded by the system accounting routines:
                   S -- command executed by super-user
                   F -- command executed after a fork but without a following
           exec
                   C -- command run in PDP-11 compatibility mode (VAX only)
                   D -- command terminated with the generation of a core file
                   X -- command was terminated with the signal SIGTERM
              + the name of the user who ran the process
              + time the process started

## [](#OPTIONS)OPTIONS

           --strict-match
                  Print only entries that match *all* of the arguments on the
                  command line.
           --print-controls
                  Print control characters.
           --user name
                  List records for user with name.  This is useful if you're
                  trying to match a username that happens to be the same as a
                  command (e.g., ed ).
           --command name
                  List records for command name.
           --tty name
                  List records for tty name.
           --forwards
                  Read file forwards instead of backwards. This avoids trying
                  to seek on the file and can be used to read from a pipe.
                  This must be specified prior to any -f arguments.
           -f filename, --file filename
                  Read from the file filename instead of acct.  A filename of
                  "-" will result in reading from stdin. This must either be
                  the first -f option, or --forwards must precede all -f op‐
                  tions.
           --ahz hz
                  Use this flag to tell the program what AHZ should be (in
                  hertz).  This option is useful if you are trying to view an
                  acct file created on another machine which has the same
                  byte order and file format as your current machine, but has
                  a different value for AHZ.
           -p, --show-paging
                  Print paging statistics.
           --pid  Show PID and PPID of the process if acct version 3 format
                  is supported by kernel.
           --pid  Add pid of the process and pid of the process parent to the
                  output (pid is the last but one and parent pid the last
                  column).  These values are shown only when they are gener‐
                  ated by acct function (depends on the version of kernel)
           --debug
                  Print verbose internal information.
           -V, --version
                  Print the version number of lastcomm.
           -h, --help
                  Prints the usage string and default locations of system
                  files to standard output and exits.

## [](#FILES)FILES

           acct
                  The system wide process accounting file. See acct(5) (or
                  pacct(5)) for further details.  /var/log/account
                         This directory contains pacct files which contain
                         the binary process accounting data as written by the
                         kernel.

## [](#AUTHOR)AUTHOR

           The GNU accounting utilities were written by Noel Cragg
           <noel@gnu.ai.mit.edu>. The man page was adapted from the account‐
           ing texinfo page by Susan Kleinmann <sgk@sgk.tiac.net>.

## [](#SEE_ALSO)SEE ALSO

           last(1), acct(5)

## [](#COLOPHON)COLOPHON

           This page is part of the psacct (process accounting utilities)
           project.  Information about the project can be found at 
           ⟨http://www.gnu.org/software/acct/⟩.  If you have a bug report for
           this manual page, see ⟨http://www.gnu.org/software/acct/⟩.  This
           page was obtained from the tarball acct-6.6.4.tar.gz fetched from
           ⟨http://ftp.gnu.org/gnu/acct/⟩ on 2026-08-04.  If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                 1995 October 31                  LASTCOMM(1)

------------------------------------------------------------------------

Pages that refer to this page: [acct(5)](../man5/acct.5.html),  [dump-acct(8)](../man8/dump-acct.8.html),  [dump-utmp(8)](../man8/dump-utmp.8.html)

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
