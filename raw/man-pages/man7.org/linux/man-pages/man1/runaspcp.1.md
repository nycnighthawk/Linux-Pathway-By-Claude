---
{"title": "runaspcp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/runaspcp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# runaspcp(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RUNASPCP(1)              General Commands Manual              RUNASPCP(1)

## [](#NAME)NAME

           runaspcp - execute a shell command as the user ``pcp''

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/runaspcp [-D debug] [-s shell] command

## [](#DESCRIPTION)DESCRIPTION

           runaspcp runs the single argument command as the user $PCP_USER
           and group $PCP_GROUP (both from /etc/pcp.conf).

           The command is run by sh(1) by default, else shell from the -s (or
           --shell) command line argument.

           Normally runaspcp is used from the PCP ``init'' scripts that are
           launched as ``root'' but need to downgrade their privileges when
           running some PCP daemons as the ``pcp'' user.

           The -?, --help option displays a usage message.

## [](#DIAGNOSTICS)DIAGNOSTICS

           The exit status is 1 if runaspcp cannot change user or group, or
           cannot execute the shell, else the exit status of command.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to runaspcp are as follows:
           ┌────────┬─────────────────────┐
           │ Option │ Description         │
           ├────────┼─────────────────────┤
           │ appl0  │ verbose diagnostics │
           └────────┴─────────────────────┘

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

    Performance Co-Pilot               PCP                        RUNASPCP(1)

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
