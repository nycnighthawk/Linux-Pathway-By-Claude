---
{"title": "last(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/last.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# last(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LAST(1)                  General Commands Manual                  LAST(1)

## [](#NAME)NAME

           last - list logins on the system

## [](#SYNOPSIS)SYNOPSIS

           last   [ -num | -n num | --lines num ]
                  [ -f filename | --file filename ]
                  [ people ...  ] [ ttys ...  ]
                  [ --complain ] [ --no-truncate-ftp-entries ]
                  [ -x | --more-records ] [ -a | --all-records ]
                  [ --tw-leniency num ] [ --tw-suspicious num ]
                  [ -i | --ip-address ] [ --debug ] [ -w | --wide ]
                  [ -s | --print-seconds ] [ -y | --print-year ]
                  [ -V | --version ] [ -h | --help ]

## [](#DESCRIPTION)DESCRIPTION

           last  looks  through  the  file wtmp (which records all logins/lo‐
           gouts) and  prints  information  about  connect  times  of  users.
           Records are printed from most recent to least recent.  Records can
           be specified by tty and username.  tty names can be abbreviated:
                                         last 0
           is equivalent to
                                       last tty0.

           Multiple arguments can be specified:
                                   last root console
           will  print  all  of the entries for the user root and all entries
           logged in on the console tty.

           The special users reboot and shutdown log in when the  system  re‐
           boots or (surprise) shuts down.
                                      last reboot
           will produce a record of reboot times.

           If last is interrupted by a quit signal, it prints out how far its
           search in the wtmp file had reached and then quits.

## [](#OPTIONS)OPTIONS

           -n num, --lines num
                  Limit the number of lines that last outputs.  This is dif‐
                  ferent from u*x last, which lets you specify the number
                  right after a dash.
           -f filename, --file filename
                  Read from the file filename instead of the system's wtmp
                  file.
           --complain
                  When the wtmp file has a problem (a time-warp, missing
                  record, or whatever), print out an appropriate error.
           --tw-leniency num
                  Set the time warp leniency to num seconds.  Records in wtmp
                  files might be slightly out of order (most notably when two
                  logins occur within a one-second period - the second one
                  gets written first).  By default, this value is set to 60.
                  If the program notices this problem, time is not assigned
                  to users unless the --timewarps flag is used.
           --tw-suspicious num
                  Set the time warp suspicious value to num seconds.  If two
                  records in the wtmp file are farther than this number of
                  seconds apart, there is a problem with the wtmp file (or
                  your machine hasn't been used in a year).  If the program
                  notices this problem, time is not assigned to users unless
                  the --timewarps flag is used.
           --no-truncate-ftp-entries
                  When printing out the information, don't chop the number
                  part off of `ftp'XXXX entries.
           -x, --more-records
                  Print out run level changes, shutdowns, and time changes in
                  addition to the normal records.
           -a, --all-records
                  Print out all records in the wtmp file.
           -i, --ip-address
                  Some machines store the IP address of a connection in a
                  utmp record.  Enabling this option makes last print the IP
                  address instead of the hostname.
           -w, --wide
                  By default, last tries to print each entry within in 80
                  columns.  Use this option to instruct last to print out the
                  fields in the wtmp file with full field widths.
           --debug
                  Print verbose internal information.
           -s, --print-seconds
                  Print seconds when displaying dates.
           -y, --print-year
                  Print year when displaying dates.
           -V, --version
                  Print last's version number.
           -h, --help
                  Prints the usage string and default locations of system
                  files to standard output and exits.

## [](#FILES)FILES

           wtmp
                  The system wide login record file. See wtmp(5) for further
                  details.

## [](#AUTHOR)AUTHOR

           The GNU accounting utilities were written by Noel Cragg
           <noel@gnu.ai.mit.edu>. The man page was added by Dirk Eddelbuettel
           <edd@qed.econ.queensu.ca>.

## [](#SEE_ALSO)SEE ALSO

           who(1), wtmp(5)

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

                                  1997 August 19                      LAST(1)

------------------------------------------------------------------------

Pages that refer to this page: [lastcomm(1)](../man1/lastcomm.1.html),  [utmpdump(1)](../man1/utmpdump.1.html),  [utmp(5)](../man5/utmp.5.html)

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
