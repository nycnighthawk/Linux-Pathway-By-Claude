---
{"title": "pmdadocker(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdadocker.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdadocker(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDADOCKER(1)            General Commands Manual            PMDADOCKER(1)

## [](#NAME)NAME

           pmdadocker - docker performance metrics domain agent (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/docker/pmdadocker [-D debug] [-d domain] [-l
           logfile]

## [](#DESCRIPTION)DESCRIPTION

           pmdadocker is a docker Performance Metrics Domain Agent (PMDA)
           which exposes performance metrics as reported from the Docker
           Remote API.

           A brief description of the pmdadocker command line options
           follows:

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                docker.log is written in the current directory of pmcd(1)
                when pmdadocker is started, i.e.  $PCP_LOG_DIR/pmcd.  If the
                log file cannot be created or is not writable, output is
                written to the standard error instead.

           Remote API metric requests are activated automatically and are
           fetched on a timer.  This timer is represented as a by pmdadocker
           via the docker.control.timing.  By default, pmdadocker will be set
           to fetch on a 1 second interval.

           pmdadocker will iterate over three different docker remote API
           calls:

           /containers/$ID/json
                  Container metrics regarding the current state of the
                  container. Such as PID, name or if the container is
                  running.

           /version
                  Basic version metrics about the current docker daemon in
                  use.

           /containers/$ID/stats?stream=0
                  More in depth memory and cpu metrics of the container.

## [](#INSTALLATION)INSTALLATION

           If you want access to the names, help text and values for the
           docker performance metrics, do the following as root:

                # cd $PCP_PMDAS_DIR/docker
                # ./Install

           If you want to undo the installation (and remove both PMDAs), do
           the following as root:

                # cd $PCP_PMDAS_DIR/docker
                # ./Remove

           pmdadocker is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdadocker
           $PCP_PMDAS_DIR/docker/help
                  default help text file for the docker metrics
           $PCP_PMDAS_DIR/docker/Install
                  installation script for the pmdadocker agent
           $PCP_PMDAS_DIR/docker/Remove
                  undo installation script for the pmdadocker agent
           $PCP_LOG_DIR/pmcd/docker.log
                  default log file for error messages and other information
                  from pmdadocker

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

           Debugging options specific to pmdadocker are as follows:
           ┌────────┬────────────────────────────────────────┐
           │ Option │ Description                            │
           ├────────┼────────────────────────────────────────┤
           │ appl1  │ report failure to fetch stats via http │
           └────────┴────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pcp.conf(5), pcp.env(5) and docker(1).

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

    Performance Co-Pilot               PCP                      PMDADOCKER(1)

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
