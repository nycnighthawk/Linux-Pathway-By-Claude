---
{"title": "pmdaoverhead(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdaoverhead.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdaoverhead(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAOVERHEAD(1)          General Commands Manual          PMDAOVERHEAD(1)

## [](#NAME)NAME

           pmdaoverhead - performance metrics domain agent (PMDA) exporting
           resource consumption metrics for groups of processes

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/overhead/pmdaoverhead [-C] [-c config] [-D debug]
           [-d domain] [-l logfile] [-R interval]

## [](#DESCRIPTION)DESCRIPTION

           pmdaoverhead is a configurable Performance Metrics Domain Agent
           (PMDA) for exporting resource consumption for groups of related
           processes.

           The pmdaoverhead command line options are:

           -C  parse the configuration file(s) and exit after reporting any
               errors.

           -c  configuration file(s), config may be either a file or a
               directory; in the latter case all the files within config are
               assumed to be configuration files for pmdaoverhead and they
               will all be processed.

               Each configuration file defines one or more ``groups'' of
               processes of interest, using the syntax described in the
               ``CONFIGURATION'' section below.

               By default all configuration files below the
               $PCP_SYSCONF_DIR/overhead/conf.d/ directory are used.

           -d  It is absolutely crucial that the performance metrics domain
               number specified here is unique and consistent.  That is,
               domain should be different for every PMDA on the one host, and
               the same domain number should be used for the same PMDA on all
               hosts.

           -l  Location of the log file.  By default, a log file named
               overhead.log is written in the current directory of pmcd(1)
               when pmdaoverhead is started, i.e.  $PCP_LOG_DIR/pmcd.  If the
               log file cannot be created or is not writable, output is
               written to the standard error instead.

           -R  The PMDA uses a separate thread to periodically scan all
               processes to determine which processes are deemed
               ``interesting'' in each group, and extracting resource
               consumption for those processes.  The interval (in seconds)
               determines how often this scanning and resource calculation is
               done, the default is 60 (seconds).

## [](#CONFIGURATION)CONFIGURATION

           Each configuration file defines one or more ``groups'' of
           processes.  The file format is simple and follows the following
           rules.

           1.  Lines beginning with a hash ``#'' are treated as comments.
               More generally, except for the pattern: clause described
               below, all text between a hash and the end of line is treated
               as a comment.

           2.  White space (spaces or tabs or newlines) are required to
               separate lexical components.  Spaces and tabs are otherwise
               ignored.  Other than terminating comments and the regex in a
               pattern: clause, newlines are also ignored.

           3.  Each group is introduced by a group clause that has the form
                       group name { parameters }
               where name is a unique name for the group across all groups in
               the pmdaoverhead configuration files.  As name becomes
               embedded in the Performance Metrics Name Space (PMNS) if must
               follow the rules for metric name components as described in
               PMNS(5), namely beginning with an alphabetic character,
               followed by zero or more characters drawn from the
               alphabetics, numerics and the underscore ``_'' character.

           4.  The parameters must include one id: clause and one pattern:
               clause.

           5.  An id: clause has the form
                       id: ident
               where ident is a unique identifier number for the group across
               all groups in the pmdaoverhead configuration files.  Valid
               values for ident are in the range 0 to 4094 (inclusive).

           6.  A pattern: clause has the form
                       pattern: regex
               where regex is an extended regular expression notation in the
               style of egrep(1).  The regex starts at the first non-
               whitespace character after pattern: and extends to the next
               newline.

               The processes that are considered to be members of the group
               are those for which the command name, as reported by
                       $ pminfo -f proc.psinfo.cmd
               is matched by regex plus all the descendents of those
               processes.  So for example the regex ^pmcd$ will match pmcd(1)
               and all the PMDA processes launched by pmcd(1) and any of
               their children, etc.

## [](#INSTALLATION)INSTALLATION

           If you want access to the names, help text and values for the
           overhead performance metrics, do the following as root:

                # cd $PCP_PMDAS_DIR/overhead
                # ./Install

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/overhead
                # ./Remove

           pmdaoverhead is launched by pmcd and should never be executed
           directly.  The Install and Remove scripts notify pmcd when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdaoverhead
           $PCP_PMDAS_DIR/overhead/Install
                  installation script for the pmdaoverhead agent
           $PCP_PMDAS_DIR/overhead/Remove
                  undo installation script for the pmdaoverhead agent
           $PCP_LOG_DIR/pmcd/overhead.log
                  default log file for error messages and other information
                  from pmdaoverhead
           $PCP_SYSCONF_DIR/overhead/conf.d
                  directory containing configuration files for the overhead
                  metrics

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

           Debugging options specific to pmdaoverhead are as follows:
           ┌────────┬────────────────────────────────┐
           │ Option │ Description                    │
           ├────────┼────────────────────────────────┤
           │ appl0  │ configfile parsing             │
           ├────────┼────────────────────────────────┤
           │ appl1  │ refresh() start-end timestamps │
           ├────────┼────────────────────────────────┤
           │ appl2  │ /proc selection in refresh()   │
           └────────┴────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmdaproc(1), pcp.conf(5), pcp.env(5) and
           PMNS(5).

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

    Performance Co-Pilot               PCP                    PMDAOVERHEAD(1)

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
