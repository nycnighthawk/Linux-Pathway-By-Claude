---
{"title": "who(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/who.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# who(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WHO(1)                        User Commands                        WHO(1)

## [](#NAME)NAME

           who - show who is logged on

## [](#SYNOPSIS)SYNOPSIS

           who [OPTION]... [ FILE | ARG1 ARG2 ]

## [](#DESCRIPTION)DESCRIPTION

           Print information about users who are currently logged in.

           -a, --all
                  same as -b -d --login -p -r -t -T -u

           -b, --boot
                  time of last system boot

           -d, --dead
                  print dead processes

           -H, --heading
                  print line of column headings

           -l, --login
                  print system login processes

           --lookup
                  attempt to canonicalize hostnames via DNS

           -m     only hostname and user associated with standard input

           -p, --process
                  print active processes spawned by init

           -q, --count
                  all login names and number of users logged on

           -r, --runlevel
                  print current runlevel

           -s, --short
                  print only name, line, and time (default)

           -t, --time
                  print last system clock change

           -T, -w, --mesg
                  add user's message status as +, - or ?

           -u, --users
                  list users logged in, including idle time

           --message
                  same as -T

           --writable
                  same as -T

           --help display this help and exit

           --version
                  output version information and exit

           If FILE is not specified, use /var/run/utmp.  /var/log/wtmp as
           FILE is common.  If ARG1 ARG2 given, -m presumed: 'am i' or 'mom
           likes' are usual.

## [](#AUTHOR)AUTHOR

           Written by Joseph Arceneaux, David MacKenzie, and Michael Stone.

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

           Full documentation <https://www.gnu.org/software/coreutils/who>
           or available locally via: info '(coreutils) who invocation'

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

    GNU coreutils 9.11              April 2026                         WHO(1)

------------------------------------------------------------------------

Pages that refer to this page: [last(1)](../man1/last.1.html),  [users(1)](../man1/users.1.html),  [utmpdump(1)](../man1/utmpdump.1.html),  [w(1)](../man1/w.1.html),  [utmp(5)](../man5/utmp.5.html)

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
