---
{"title": "perfalloc(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perfalloc.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perfalloc(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERFALLOC(1)             General Commands Manual             PERFALLOC(1)

## [](#NAME)NAME

           perfalloc - notify pmdaperfevent(1) to disable hardware counter
           allocation.

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/perfevent/perfalloc [-D] [-d] [-f lockfile] [-h]
           [-v] [commandline]

## [](#DESCRIPTION)DESCRIPTION

           perfalloc is a command that notifies the pmdaperfevent(1) to
           disable hardware counter event collection.  This allow
           unprivileged processes to use the hardware counters.

           If the reservation request fails, then perfalloc exits immediately
           with exit code EXIT_FAILURE.  If successful, the perfalloc will
           run until a kill signal is received.  The reservation request
           persists while perfalloc is running.

           Note that pmdaperfevent is affected by the value of the
           kernel.perf_event_paranoid setting, which can be adjusted by
           sysctl(8).

           If a commandline is given, this is executed as a subprocess of the
           agent.  When the command dies, so does the agent.

           A brief description of the command line options follows:

           -D   run in the foreground (the default)

           -d   run in the background

           -f FILE
                use FILE as the lock file (default
                $PCP_PMDAS_DIR/perfevent/perflock)

           -h   display a help message and exit

           -v   output version number and exit

## [](#BUGS)BUGS

           There may be a delay of up to 100 milliseconds between perfalloc
           requesting the hardware counter disabling and the perfevent PMDA
           processing the request.

           The perfalloc process does not check the status of the request and
           therefore is not able to provide a positive confirmation that the
           request succeeded and the hardware counters are disabled.

## [](#SEE_ALSO)SEE ALSO

           pmdaperfevent(1), perfevent.conf(3) and sysctl(8).

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

    Performance Co-Pilot               PCP                       PERFALLOC(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdaperfevent(1)](../man1/pmdaperfevent.1.html)

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
