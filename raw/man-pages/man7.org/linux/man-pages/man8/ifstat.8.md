---
{"title": "ifstat(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ifstat.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ifstat(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IFSTAT(8)                         Linux                         IFSTAT(8)

## [](#NAME)NAME

           ifstat - handy utility to read network interface statistics

## [](#SYNOPSIS)SYNOPSIS

           ifstat [ OPTIONS ] [ INTERFACE_LIST ]

           INTERFACE_LIST := INTERFACE_LIST | interface

## [](#DESCRIPTION)DESCRIPTION

           ifstat neatly prints out network interface statistics.  The
           utility keeps records of the previous data displayed in history
           files and by default only shows difference between the last and
           the current call.  Location of the history files defaults to
           /tmp/.ifstat.u$UID but may be overridden with the IFSTAT_HISTORY
           environment variable. Similarly, the default location for xstat
           (extended stats) is /tmp/.<xstat name>_ifstat.u$UID.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Show summary of options.

           -V, --version
                  Show version of program.

           -a, --ignore
                  Ignore the history file.

           -d, --scan=SECS
                  Sample statistics every SECS seconds.

           -e, --errors
                  Show errors.

           -n, --nooutput
                  Don't display any output.  Update the history file only.

           -r, --reset
                  Reset history.

           -s, --noupdate
                  Don't update the history file.

           -t, --interval=SECS
                  Report average over the last SECS seconds.

           -z, --zeros
                  Show entries with zero activity.

           -j, --json
                  Display results in JSON format

           -p, --pretty
                  If combined with --json, pretty print the output.

           -x, --extended=TYPE
                  Show extended stats of TYPE. Supported types are:

                          cpu_hits - Counts only packets that went via the
                          CPU.

## [](#ENVIRONMENT)ENVIRONMENT

           IFSTAT_HISTORY
                  If set, its value is interpreted as alternate history file
                  path.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           ifstat was written by Alexey Kuznetsov <kuznet@ms2.inr.ac.ru>.

           This manual page was written by Petr Sabata <contyk@redhat.com>.

## [](#COLOPHON)COLOPHON

           This page is part of the iproute2 (utilities for controlling
           TCP/IP networking and traffic) project.  Information about the
           project can be found at 
           ⟨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2⟩.
           If you have a bug report for this manual page, send it to
           netdev@vger.kernel.org, shemminger@osdl.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/network/iproute2/iproute2.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iproute2                       28 Oct 2015                      IFSTAT(8)

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
