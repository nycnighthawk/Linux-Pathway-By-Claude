---
{"title": "telnet-probe(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/telnet-probe.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# telnet-probe(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TELNET-PROBE(1)          General Commands Manual          TELNET-PROBE(1)

## [](#NAME)NAME

           telnet-probe - lightweight telnet-like port probe

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/telnet-probe [-cv?]  host port

## [](#DESCRIPTION)DESCRIPTION

           telnet-probe allows the pmdashping(1) daemons to establish
           connections to arbitrary local and remote service-providing
           daemons so that response time and service availability information
           can be obtained.

           The required host and port number arguments have the same meaning
           as their telnet(1) equivalents.

           The -c option causes telnet-probe to perform a connect(2) only.
           This skips the read(2) and write(2) exercise that would otherwise
           be done after connecting (see below).

           Once the telnet connection has been established, telnet-probe
           reads from stdin until end-of-file, and writes all the input data
           to the telnet connection.  Next, telnet-probe will read from the
           telnet connection until end-of-file, discarding whatever data it
           receives.  Then telnet-probe exits.

           To operate successfully, the input passed via telnet-probe to the
           remote service must be sufficient to cause the remote service to
           close the connection when the last line of input has been
           processed, e.g. ending with ``quit'' when probing SMTP on port 25.

           By default telnet-probe will not produce any output, unless there
           is an error in which case a diagnostic message can be displayed
           (in verbose mode only) and the exit status will be non-zero
           indicating a failure.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -c   Connect only, do not read or write.

           -v   Enable verbose mode.

           -?   Display usage message and exit.

## [](#DIAGNOSTICS)DIAGNOSTICS

           If telnet-probe succeeds, then 0 will be returned.  If the attempt
           to establish a connection fails or is terminated, then a non-zero
           exit status is returned.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmdashping(1), pmie(1), telnet(1), connect(2),
           read(2) and write(2).

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

    Performance Co-Pilot               PCP                    TELNET-PROBE(1)

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
