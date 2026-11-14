---
{"title": "uptime(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/uptime.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uptime(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UPTIME(1)                General Commands Manual                UPTIME(1)

## [](#NAME)NAME

           uptime - Tell how long the system has been running.

## [](#SYNOPSIS)SYNOPSIS

           uptime [option ...]

## [](#DESCRIPTION)DESCRIPTION

           uptime gives a one line display of the following information.  The
           current time, how long the system has been running, how many users
           are currently logged on, and the system load averages for the past
           1, 5, and 15 minutes.

           This is the same information contained in the header line
           displayed by w(1).

           System load averages is the average number of processes that are
           either in a runnable or uninterruptible state.  A process in a
           runnable state is either using the CPU or waiting to use the CPU.
           A process in uninterruptible state is waiting for some I/O access,
           eg waiting for disk.  The averages are taken over the three time
           intervals.  Load averages are not normalized for the number of
           CPUs in a system, so a load average of 1 means a single CPU system
           is loaded all the time while on a 4 CPU system it means it was
           idle 75% of the time.

## [](#OPTIONS)OPTIONS

           -c, --container
                  show the container uptime instead of system uptime.

           -p, --pretty
                  show uptime in pretty format

           -h, --help
                  display this help text

           -r, --raw
                  Display values in a raw format. Current time and uptime are
                  displayed in seconds.

           -s, --since
                  system up since, in yyyy-mm-dd HH:MM:SS format

           -V, --version
                  display version information and exit

## [](#ENVIRONMENT)ENVIRONMENT

           PROCPS_CONTAINER
                  If $PROCPS_CONTAINER is set, then uptime behaves as if the
                  --container option has been given.

## [](#FILES)FILES

           /var/run/utmp
                  information about who is currently logged on

           /proc  process information

## [](#SEE_ALSO)SEE ALSO

           ps(1), top(1), utmp(5), w(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           Please send bug reports to ⟨procps@freelists.org⟩.

## [](#COLOPHON)COLOPHON

           This page is part of the procps-ng (/proc filesystem utilities)
           project.  Information about the project can be found at 
           ⟨https://gitlab.com/procps-ng/procps⟩.  If you have a bug report
           for this manual page, see
           ⟨https://gitlab.com/procps-ng/procps/blob/master/Documentation/bugs.md⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/procps-ng/procps.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    procps-ng                       2024-02-08                      UPTIME(1)

------------------------------------------------------------------------

Pages that refer to this page: [htop(1)](../man1/htop.1.html),  [pcp-uptime(1)](../man1/pcp-uptime.1.html),  [tload(1)](../man1/tload.1.html),  [top(1)](../man1/top.1.html),  [w(1)](../man1/w.1.html),  [getloadavg(3)](../man3/getloadavg.3.html),  [proc(5)](../man5/proc.5.html),  [proc_loadavg(5)](../man5/proc_loadavg.5.html),  [time_namespaces(7)](../man7/time_namespaces.7.html)

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
