---
{"title": "pmdaamdgpu(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdaamdgpu.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdaamdgpu(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAAMDGPU(1)            General Commands Manual            PMDAAMDGPU(1)

## [](#NAME)NAME

           pmdaamdgpu - AMD GPU metrics domain agent (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/amdgpu/pmdaamdgpu [-D debug] [-d domain] [-l
           logfile] [-t interval]

## [](#DESCRIPTION)DESCRIPTION

           pmdaamdgpu is a Performance Metrics Domain Agent (PMDA) which
           extracts performance metrics describing the metrics available on
           AMD GPU cards via the DRM library.

           The amdgpu PMDA exports metrics that measure GPU activity, memory
           utilization, temperature, etc on GCN 1.2+ AMD GPUs.

           A brief description of the pmdaamdgpu command line options
           follows:

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                amdgpu.log is written in the current directory of pmcd(1)
                when pmdaamdgpu is started, i.e.  $PCP_LOG_DIR/pmcd.  If the
                log file cannot be created or is not writable, output is
                written to the standard error instead.

           -t   Enables and sets a sampling interval for automatic refreshing
                of metric values.  The functionality is disabled by default,
                however this option allows a time interval to be specified on
                which all values are sampled - this has the effect of
                constantly updating the accumulating metrics, with the goal
                of assisting client tools such as pcp-atop(1) and pmlogger(1)
                to observe sub-sample time changes in GPU and process state.
                Typically these tools have longer sampling intervals, and can
                thus 'miss' activity happening during their sampling
                interval.

## [](#INSTALLATION)INSTALLATION

           The amdgpu PMDA is not installed and available by default.  If you
           want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/amdgpu
                # ./Remove

           If you want to establish access to the names, help text and values
           for the AMD GPU performance metrics once more, after removal, do
           the following as root:

                # cd $PCP_PMDAS_DIR/amdgpu
                # ./Install

           pmdaamdgpu is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdaamdgpu
           $PCP_PMDAS_DIR/amdgpu/help
                  default help text file for the amdgpu metrics
           $PCP_PMDAS_DIR/amdgpu/Install
                  installation script for the pmdaamdgpu agent
           $PCP_PMDAS_DIR/amdgpu/Remove
                  undo installation script for the pmdaamdgpu agent
           $PCP_LOG_DIR/pmcd/amdgpu.log
                  default log file for error messages and other information
                  from pmdaamdgpu

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to configure
           the file and directory names used by PCP.  On each installation,
           the file /etc/pcp.conf contains the local values for these
           variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmdaamdgpu are as follows:
           ┌────────┬──────────────────────────┐
           │ Option │ Description              │
           ├────────┼──────────────────────────┤
           │ appl0  │ interaction with pmcd(1) │
           ├────────┼──────────────────────────┤
           │ appl2  │ trace select(2) calls    │
           └────────┴──────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp-atop(1), pmcd(1), pmlogger(1), pcp.conf(5) and
           pcp.env(5).

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

    Performance Co-Pilot               PCP                      PMDAAMDGPU(1)

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
