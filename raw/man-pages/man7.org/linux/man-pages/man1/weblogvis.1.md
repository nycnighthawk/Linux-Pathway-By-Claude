---
{"title": "weblogvis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/weblogvis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# weblogvis(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMAND LINE OPTIONS](#COMMAND_LINE_OPTIONS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WEBLOGVIS(1)             General Commands Manual             WEBLOGVIS(1)

## [](#NAME)NAME

           weblogvis - visualize activity and performance from Web server
           logs

## [](#SYNOPSIS)SYNOPSIS

           weblogvis [-bCfiVz] [-A align] [-a archive] [-h host] [-I time]
           [-m max] [-n pmnsfile] [-O time] [-p port] [-S time] [-t interval]
           [-T time] [-x version] [-Z timezone] [server ...]

## [](#DESCRIPTION)DESCRIPTION

           weblogvis displays Web server activity as extracted from the Web
           server access logs by the Performance Co-Pilot (PCP) agent
           pmdaweblog(1).  The display is modulated by the values of the
           performance metrics retrieved from the target host which is
           running pmcd(1) and the pmdaweblog(1) Performance Metrics Domain
           Agent (PMDA(3)), or from the PCP archive log identified by
           archive.  The display is updated every interval seconds (default 2
           seconds).

           The default display mode shows the request rate classified by
           request response size, for all Web server logs being monitored by
           pmdaweblog(1).  The top of the display includes the idle time and
           the total request rate of each Web server.  The list of servers
           can be restricted by specifying server names.  The possible
           servers are listed in the pmdaweblog(1) configuration file.

           weblogvis uses pmview(1), and so the user interface follows that
           described for pmview(1), which in turn displays the scene within
           an Inventor examiner viewer.

           weblogvis passes most command line options to pmview(1).
           Therefore, the command line options -A, -a, -C, -h, -n, -O, -p,
           -S, -t, -T, -x, -Z and -z, and the user interface are described in
           the pmview(1) man page.

## [](#COMMAND_LINE_OPTIONS)COMMAND LINE OPTIONS

           The weblogvis specific options are:

           -b     Change the display mode to report bytes per second, rather
                  than requests per second.

           -f     Change the classification of activity to use HTTP functions
                  (Get, Post, Head and Other), rather than the default
                  classification by request result size.  With this
                  classification, the error rates from the logs for each Web
                  server are also displayed.

           -i     Label each column with the name of the Web server.

           -I time
                  Change the dafult expected idle time for the Web servers
                  from 3600 seconds (1 hour) to time.

           -m max Change the default normalization maximum to max
                  bytes/second or requests/second, depending on the display
                  mode.  The defaults are 500000 bytes per second or 100
                  requests per second.

           -V     Verbose mode - output the generated pmview(1) configuration
                  file.

## [](#FILES)FILES

           $PCP_VAR_DIR/config/pmlogger/config.web
                  pmlogger(1) configuration file that can be used to create a
                  PCP archive suitable for display with weblogvis
           $PCP_VAR_DIR/config/pmchart/Web.Alarms
                  pmchart(1) configuration file for monitoring Web server
                  alarm conditions
           $PCP_VAR_DIR/config/pmchart/Web.Requests
                  pmchart(1) configuration file for monitoring Web server
                  requests
           $PCP_VAR_DIR/config/pmchart/Web.Volume
                  pmchart(1) configuration file for monitoring the volume of
                  Web server transactions
           $PCP_PMDAS_DIR/weblog
                  installation directory of pmdaweblog(1)

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(4).

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), pmchart(1), pmdaweblog(1), pmlogger(1), pmview(1),
           webpingvis(1), webvis(1), pcp.conf(4) and pcp.env(4).

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

    Performance Co-Pilot                                         WEBLOGVIS(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdaweblog(1)](../man1/pmdaweblog.1.html),  [webpingvis(1)](../man1/webpingvis.1.html),  [webvis(1)](../man1/webvis.1.html)

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
