---
{"title": "pmpost(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmpost.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmpost(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [UNIX SEE ALSO](#UNIX_SEE_ALSO) \| [WINDOWS SEE ALSO](#WINDOWS_SEE_ALSO) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMPOST(1)                General Commands Manual                PMPOST(1)

## [](#NAME)NAME

           pmpost - append messages to the Performance Co-Pilot notice board

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmpost [-D debug] message

## [](#DESCRIPTION)DESCRIPTION

           pmpost will append the text message to the end of the Performance
           Co-Pilot (PCP) notice board file ($PCP_LOG_DIR/NOTICES) in an
           atomic manner that guards against corruption of the notice board
           file by concurrent invocations of pmpost.

           The PCP notice board is intended to be a persistent store and
           clearing house for important messages relating to the operation of
           the PCP and the notification of performance alerts from pmie(1)
           when other notification options are either unavailable or
           unsuitable.

           Before being written, messages are prefixed by the current time,
           and when the current day is different to the last time the notice
           board file was written, pmpost will prepend the message with the
           full date.

           If the notice board file does not exist, pmpost will create it.
           pmpost would usually run from long-running PCP daemons executing
           under the (typically unprivileged) $PCP_USER and $PCP_GROUP
           accounts.  The file should be owned and writable by the $PCP_USER
           user, and readable by others.

## [](#FILES)FILES

           $PCP_LOG_DIR/NOTICES
                the PCP notice board file

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           The file /etc/pcp.conf contains the local values for PCP_
           variables.

## [](#UNIX_SEE_ALSO)UNIX SEE ALSO

           logger(1).

## [](#WINDOWS_SEE_ALSO)WINDOWS SEE ALSO

           pcp-eventlog(1).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           pmie(1), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                          PMPOST(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcpintro(1)](../man1/pcpintro.1.html)

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
