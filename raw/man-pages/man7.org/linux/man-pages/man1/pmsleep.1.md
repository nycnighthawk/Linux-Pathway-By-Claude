---
{"title": "pmsleep(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmsleep.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmsleep(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMSLEEP(1)               General Commands Manual               PMSLEEP(1)

## [](#NAME)NAME

           pmpause, pmsleep - portable subsecond-capable sleep

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmpause [-w where]
           $PCP_BINADM_DIR/pmsleep [-w where] interval

## [](#DESCRIPTION)DESCRIPTION

           pmpause sleeps indefinitely, until interrupted by SIGKILL.

           pmsleep sleeps for the specified interval.  The interval argument
           follows the syntax described in PCPIntro(1) for -t, and in the
           simplest form may be an unsigned integer or floating point
           constant (the implied units in this case are seconds).

           The -w option is provided to allow annotation of scripts with
           multiple uses of pmpause and/or pmsleep to identify a particular
           use in the process's arguments, e.g. as visible to ps(1).

## [](#DIAGNOSTICS)DIAGNOSTICS

           The exit status is 0 for success, or 1 for a malformed command
           line.  If the underlying nanosleep(2) system call fails, an errno
           is returned.

## [](#SEE_ALSO)SEE ALSO

           sleep(1), pause(2) and nanosleep(2).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.
           Information about the project can be found at 
           ⟨http://www.pcp.io/⟩.  If you have a bug report for this manual
           page, send it to pcp@groups.io.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot               PCP                         PMSLEEP(1)

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
