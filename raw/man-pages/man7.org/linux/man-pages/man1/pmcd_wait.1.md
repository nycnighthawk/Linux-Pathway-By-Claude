---
{"title": "pmcd_wait(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmcd_wait.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmcd_wait(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMCD_WAIT(1)             General Commands Manual             PMCD_WAIT(1)

## [](#NAME)NAME

           pmcd_wait - wait for PMCD to accept client connections

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmcd_wait [-v?]  [-D debug] [-h host] [-t timeout]

## [](#DESCRIPTION)DESCRIPTION

           pmcd_wait waits for the Performance Metrics Collector Daemon
           (PMCD) to be running and accepting client connections.

           Unless directed to another host by the -h option, pmcd_wait will
           try to contact pmcd(1) on the local host.

           pmcd_wait will timeout and abandon the attempt to connect to pmcd
           after 60 seconds.  This default timeout interval may be changed
           using the -t option, where the interval argument follows the
           syntax described in PCPIntro(1) and in the simplest form may be an
           unsigned integer (the implied units in this case are seconds).

           On successful connection to pmcd an exit status of zero is
           returned.

           If an error or timeout occurs, then a non-zero exit status is
           returned as described below.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -h host, --host=host
                Connect pmcd(1) on host, rather than the one on the default
                localhost.

           -t timeout, --interval=timeout
                Timeout after timeout seconds if not connected.  The default
                timeout value is 60 seconds.

           -v, --verbose
                This option turns the verbose mode on.  With the verbose mode
                off (which is the default), no output will be generated.
                With verbose mode on, error messages will be output on
                stderr.

           -?, --help
                Display usage message and exit.

## [](#DIAGNOSTICS)DIAGNOSTICS

           Error messages will be output to stderr only if the verbose mode
           is on.

           The following exit status codes are returned:

           0      pmcd_wait was able to successfully connect to pmcd within
                  the timeout period.

           1      A usage error occurred, use -v for more details.

           2      No connection was made in the timeout interval.  This will
                  happen if pmcd is running but takes too long to complete
                  the client connection, or if pmcd is not running and all
                  connection attempts in the timeout interval failed with the
                  error ECONNREFUSED.

           3      A UNIX error occurred, use -v for more details.

           4      A PCP error occurred, use -v for more details.

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

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                       PMCD_WAIT(1)

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
