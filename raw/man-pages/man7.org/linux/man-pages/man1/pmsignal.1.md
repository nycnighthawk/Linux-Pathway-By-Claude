---
{"title": "pmsignal(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmsignal.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmsignal(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMSIGNAL(1)              General Commands Manual              PMSIGNAL(1)

## [](#NAME)NAME

           pmsignal - send a signal to one or more processes

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmsignal [-alnp] [-s signal] [PID ...|name ...]

## [](#DESCRIPTION)DESCRIPTION

           pmsignal provides a cross-platform event signalling mechanism for
           use with tools from the Performance Co-Pilot toolkit.  It can be
           used to send a named signal (only HUP, USR1, TERM, and KILL are
           accepted) to one or more processes.

           The processes are specified directly using PIDs or as program
           names (with either the -a or -p options).  In the all case, the
           set of all running processes is searched for a basename(1) match
           on name.  In the program case, process identifiers are extracted
           from files in the $PCP_RUN_DIR directory where file names are
           matched on name.pid.

           The -n option reports the list of process identifiers that would
           have been signalled, but no signals are actually sent.

           If a signal is not specified, then the TERM signal will be sent.
           The list of supported signals is reported when using the -l
           option.

           On Linux and UNIX platforms, pmsignal is a simple wrapper around
           the kill(1) command.  On Windows, the is no direct equivalent to
           this mechanism, and so an alternate mechanism has been implemented
           - this is only honoured by PCP tools, however, not all Windows
           utilities.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -a, --all
                Send signal to all named processes.

           -l, --list
                List supported signals.

           -n, --dry-run
                List processes that would be affected.

           -p, --program
                Extract programs from PCP runtime PID files.

           -s signal, --signal=signal
                Specify the signal to send, one of: HUP, USR1, TERM, KILL.

           -?, --help
                Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           basename(1), kill(1), killall(1), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                        PMSIGNAL(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmcd(1)](../man1/pmcd.1.html)

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
