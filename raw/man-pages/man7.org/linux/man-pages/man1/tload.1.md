---
{"title": "tload(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/tload.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tload(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TLOAD(1)                 General Commands Manual                 TLOAD(1)

## [](#NAME)NAME

           tload - graphic representation of system load average

## [](#SYNOPSIS)SYNOPSIS

           tload [option ...] [tty]

## [](#DESCRIPTION)DESCRIPTION

           tload prints a graph of the current system load average to the
           specified tty (or the tty of the tload process if none is
           specified).

## [](#OPTIONS)OPTIONS

           -s, --scale number
                  The scale option allows a vertical scale to be specified
                  for the display (in characters between graph ticks); thus,
                  a smaller value represents a larger scale, and vice versa.

           -d, --delay seconds
                  The delay sets the delay between graph updates in seconds.

           -h, --help
                  Display this help text.

           -V, --version
                  Display version information and exit.

## [](#FILES)FILES

           /proc/loadavg load average information

## [](#SEE_ALSO)SEE ALSO

           ps(1), top(1), uptime(1), w(1)

## [](#BUGS)BUGS

           The -d delay option sets the time argument for an alarm(2); if -d
           0 is specified, the alarm is set to 0, which will never send the
           SIGALRM and update the display.

## [](#AUTHORS)AUTHORS

           Branko Lankester, David Engel ⟨david@ods.com⟩, and Michael K.
           Johnson ⟨johnsonm@redhat.com⟩.

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

    procps-ng                       2020-06-04                       TLOAD(1)

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
