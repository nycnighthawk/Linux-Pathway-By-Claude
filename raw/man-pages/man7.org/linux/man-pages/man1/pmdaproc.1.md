---
{"title": "pmdaproc(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdaproc.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdaproc(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [HOTPROC OVERVIEW](#HOTPROC_OVERVIEW) \| [HOTPROC CONFIGURATION](#HOTPROC_CONFIGURATION) \| [DYNAMIC CONFIGURATION](#DYNAMIC_CONFIGURATION) \| [ACCESS CONFIGURATION](#ACCESS_CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAPROC(1)              General Commands Manual              PMDAPROC(1)

## [](#NAME)NAME

           pmdaproc - process performance metrics domain agent (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/proc/pmdaproc [-AL] [-D debug] [-d domain] [-l
           logfile] [-r cgroup] [-U username]

## [](#DESCRIPTION)DESCRIPTION

           pmdaproc is a Performance Metrics Domain Agent (PMDA) which
           extracts performance metrics describing the state of the
           individual processes running on a Linux system.

           The proc PMDA exports metrics that measure the memory, processor
           and other resource use of each process, as well as summary
           information collated across all of the running processes.  This
           includes per-process NUMA placement summaries from
           /proc/<pid>/numa_maps via the proc.numa_maps.* metrics.  The PMDA
           uses credentials passed from the PMAPI(3) monitoring tool
           identifying the user requesting the information, to ensure that
           only values the user is allowed to access are returned by the
           PMDA.  This involves the PMDA temporarily changing its effective
           user and group identifiers for the duration of requests for
           instances and values.  In other words, system calls to extract
           information are performed as the user originating the request and
           not as a privileged user.  The mechanisms available for transfer
           of user credentials are described further in the PCPIntro(1) page.

           A brief description of the pmdaproc command line options follows:

           -A   Disables use of the credentials provided by PMAPI client
                tools and simply runs everything under the "root" account.
                Refer to the ACCESS CONFIGURATION section below for finer
                grained control when using pmcd(1) with remote client
                authentication.  Only enable this option if you understand
                the risks involved, and are sure that all remote accesses
                will be from benevolent users.  If enabled, unauthenticated
                remote PMAPI clients will be able to access potentially
                sensitive performance metric values which an unauthenticated
                PMAPI client usually would not be able to.  Refer to
                CVE-2011-2495 and CVE-2012-3419 for additional details.

           -L   Changes the per-process instance domain used by most pmdaproc
                metrics to include threads as well.

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                proc.log is written in the current directory of pmcd(1) when
                pmdaproc is started, i.e.  $PCP_LOG_DIR/pmcd.  If the log
                file cannot be created or is not writable, output is written
                to the standard error instead.

           -r   Restrict the set of processes exported in the per-process
                instance domain to only those processes that are contained by
                the specified cgroup resource container.  This option
                provides an optional finer granularity to the monitoring, and
                can also be used to reduce the resources consumed by pmdaproc
                during requests for instances and values.

           -U   User account under which to run the agent.  The default is
                the privileged "root" account, with seteuid (2) and setegid
                (2) switching for accessing most information.

## [](#HOTPROC_OVERVIEW)HOTPROC OVERVIEW

           The pmdaproc Performance Metrics Domain Agent (PMDA) includes an
           additional set of per-process metrics with an instance domain of
           processes restricted to an "interesting" or "hot" set.  Unlike the
           stock metrics exported by the proc PMDA, which have an instance
           domain equal to the current processes, hot metrics have an
           instance domain which is a subset of this.  This hotproc instance
           domain is determined by a configurable predicate evaluated over
           some refresh interval.

           As well as the equivalent per-process proc metrics, hotproc
           provides a cpuburn metric which specifies the CPU utilization of
           the process over the refresh interval, total metrics which
           indicate how much of the available CPU time the "interesting"
           processes account for, predicate metrics which show the values of
           the reserved variables (see below) that are being used in the
           hotproc predicate, and control metrics for controlling the agent.

## [](#HOTPROC_CONFIGURATION)HOTPROC CONFIGURATION

           The configuration file consists of one predicate used to determine
           if a process should be in the interesting set or not.

           An example configuration file may be found at
           $PCP_PMDAS_DIR/proc/samplehotproc.conf

           This file with any modifications can be copied to
           $PCP_PMDAS_DIR/proc/hotproc.conf in order to configure the hot
           metrics. The pmstore(1) and pmStore(3) interfaces can be used as
           well (described below).

           The predicate is described using the language specified below.
           The symbols are based on those used by the C(1) and awk(1)
           languages.

           Boolean Connectives
                  && (and), || (or), !  (not), () (precedence overriding)

           Number comparators
                  < , <= , > , >= , == , !=

           String comparators
                  == , !=

           String/Pattern comparators
                  ~ (string matches pattern) , !~ (string does not match
                  pattern)

           Reserved variables
                  uid (user id; type integer) uname (user name; type string),
                  gid (group id; type integer) gname (group name; type
                  string), fname (process file name; type string), psargs
                  (process file name with args; type string), cpuburn (cpu
                  utilization; type float), iodemand (I/O demand - Kbytes
                  read/written per second; type float), ctxswitch (number of
                  context switches per second; type float), syscalls (number
                  of system calls per second; type float), virtualsize
                  (virtual size in Kbytes; type float), residentsize
                  (resident size in Kbytes; type float), iowait (blocked and
                  raw io wait in secs/sec; type float), schedwait (time
                  waiting in run queue in secs/sec; type float).

           Literal values
                  1234 (positive integer), 0.35 (positive float), "foobar"
                  (string; delimited by "), /[fF](o)+bar/ (pattern; delimited
                  by /), true (boolean), false (boolean)

           Comments
                  #this is a comment (from # to the end of the line).

           Examples
                    cpuburn > 0.2 # cpu utilization of more than 20%
                    cpuburn > 0.2 && uname == "root"
                    cpuburn > 0.2 && (uname == "root" || uname == "hot")
                    psargs ~ /pmda/ && cpuburn > 0.4

           The hotproc.predicate metrics may be used to see what the values
           of the reserved variables are that were used by the predicate at
           the last refresh.  They do not cover the reserved variables which
           are already exported elsewhere. A hotproc.predicate metric may not
           have a value if it is not referenced in the configuration
           predicate.

## [](#DYNAMIC_CONFIGURATION)DYNAMIC CONFIGURATION

           The hot process metrics can also be configured at runtime through
           the pmstore(1) interface (and, implicitly, the pmStore(3) API)

           Examples
                    pmstore hotproc.control.config 'fname == "mingetty"'
                    pmstore hotproc.control.config 'uid == 0'

           To force the config file to be reloaded:
                    pmstore hotproc.control.reload_config "1"

## [](#ACCESS_CONFIGURATION)ACCESS CONFIGURATION

           Access to per-process metrics is controlled by several factors.

           When using automatically authenticating local connections, such as
           through the "unix:" or "local:" style context, then client tools
           will have full access to these metrics as if sampling the metrics
           directly as the user running the client tool.

           When using pmcd with remote, authenticated clients it is possible
           to specify a set of user names that are allowed access to the
           process metrics.

           A configuration file $PCP_SYSCONF_DIR/proc/access.conf can be used
           to fine-tune this behaviour, and it supports two keywords:

           allowed
                  A comma-separated list of authenticated user names that
                  will be allowed access to per-process metrics.  Sampling is
                  performed as the root user.

           mapped A boolean value, when true indicating that authenticated
                  user names will be mapped to local system user account
                  names (this requires a one-to-one user name mapping between
                  the account and the SASL-based authenticated user name
                  enforced by pmcd(1)).  Sampling is performed as that local
                  user.

## [](#INSTALLATION)INSTALLATION

           The proc PMDA is installed and available by default.  If you want
           to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/proc
                # ./Remove

           If you want to establish access to the names, help text and values
           for the proc performance metrics once more, after removal, do the
           following as root:

                # cd $PCP_PMDAS_DIR/proc
                # ./Install

           pmdaproc is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdaproc
           $PCP_PMDAS_DIR/proc/help
                  default help text file for the proc metrics
           $PCP_PMDAS_DIR/proc/Install
                  installation script for the pmdaproc agent
           $PCP_PMDAS_DIR/proc/Remove
                  undo installation script for the pmdaproc agent
           $PCP_LOG_DIR/pmcd/proc.log
                  default log file for error messages and other information
                  from pmdaproc
           $PCP_PMDAS_DIR/proc/samplehotproc.conf
                  simple sample hotproc configuration
           $PCP_PMDAS_DIR/proc/hotproc.conf
                  default hotproc configuration file
           $PCP_SYSCONF_DIR/proc/access.conf
                  default access control configuration file

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

           Debugging options specific to pmdaproc are as follows:
           ┌────────┬───────────────────────────────────────────────┐
           │ Option │ Description                                   │
           ├────────┼───────────────────────────────────────────────┤
           │ appl0  │ cgroup handling                               │
           ├────────┼───────────────────────────────────────────────┤
           │ appl1  │ refresh processing, including hotproc metrics │
           ├────────┼───────────────────────────────────────────────┤
           │ appl2  │ PMNS operations                               │
           ├────────┼───────────────────────────────────────────────┤
           │ appl3  │ process accounting metrics                    │
           └────────┴───────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmstore(1), seteuid(2), setegid(2),
           PMAPI(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                        PMDAPROC(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-atop(1)](../man1/pcp-atop.1.html),  [pcp-atopsar(1)](../man1/pcp-atopsar.1.html),  [pmdaoverhead(1)](../man1/pmdaoverhead.1.html),  [pmda(3)](../man3/pmda.3.html),  [LOGARCHIVE(5)](../man5/LOGARCHIVE.5.html)

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
