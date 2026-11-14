---
{"title": "pmlogredact(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogredact.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogredact(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGREDACT(1)           General Commands Manual           PMLOGREDACT(1)

## [](#NAME)NAME

           pmlogredact - remove sensitive information from PCP archives

## [](#SYNOPSIS)SYNOPSIS

           pmlogredact [-vx?]  [-D debug] [-c config] inarch [outarch]

## [](#DESCRIPTION)DESCRIPTION

           Performance Co-Pilot (PCP) archives may contain a wealth of
           information collected from across all components of a system.

           Some of this information may be deemed sensitive outside the
           context of the original collection for analysis of system
           performance.  Examples of sensitive information might include user
           names, paths to user home directories (that may imply user names),
           hostnames, IP addresses, MAC addresses, command line arguments,
           process environment variables, etc.

           pmlogredact may be used to remove sensitive information before
           archives are shipped to another organization, or stored in another
           geography, or to meet regulatory or privacy compliance.  The
           output archive outarch is the redacted version of the input
           archive inarch.

           pmlogredact is a thin wrapper around pmlogrewrite(1), and so the
           configuration files for pmlogredact follow the same syntax as the
           configuration files for pmlogrewrite(1).

           There are a default set of redaction rules in the
           $PCP_VAR_DIR/config/pmlogredact/* files.  These rules remove some
           metrics, rewrite the instance domains of some metrics and rewrite
           the values of some metrics.  The -x (or --exclude-std) option may
           be used to not use the default set of rules.

           Additional (or alternative) configuration files may be specified
           with one or more -c (or --config) options, where each config is
           either a file or a directory (implying all the files within that
           directory).

           The -v (or --verbose) option adds verbosity (and is passed direct‐
           ly to pmlogrewrite(1)).

           The -?  (or --help) option displays a usage message and exits.

## [](#FILES)FILES

           $PCP_VAR_DIR/config/pmlogredact/*
                default redaction rules

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to parameter‐
           ize the file and directory names used by PCP.  On each installa‐
           tion, the file /etc/pcp.conf contains the local values for these
           variables.  The $PCP_CONF variable may be used to specify an al‐
           ternative configuration file, as described in pcp.conf(5).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional diagnos‐
           tics on stderr to help triage problems, although the information
           is sometimes cryptic and primarily intended to provide guidance
           for developers rather end-users.  debug is a comma separated list
           of debugging options; use pmdbg(1) with the -l option to obtain a
           list of the available debugging options and their meaning.

## [](#SEE_ALSO)SEE ALSO

           pmlogrewrite(1), pcp.conf(5) and pcp.env(5).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.  In‐
           formation about the project can be found at ⟨http://www.pcp.io/⟩.
           If you have a bug report for this manual page, send it to
           pcp@groups.io.  This page was obtained from the project's upstream
           Git repository ⟨https://github.com/performancecopilot/pcp.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-08-04.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Performance Co-Pilot               PCP                     PMLOGREDACT(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogrewrite(1)](../man1/pmlogrewrite.1.html)

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
