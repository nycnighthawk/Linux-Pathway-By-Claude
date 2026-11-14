---
{"title": "webpingvis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/webpingvis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# webpingvis(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CAVEATS](#CAVEATS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WEBPINGVIS(1)            General Commands Manual            WEBPINGVIS(1)

## [](#NAME)NAME

           webpingvis - visualize Web server response time

## [](#SYNOPSIS)SYNOPSIS

           webpingvis [-CiVz] [-A align] [-a archive] [-h host] [-m max] [-n
           pmnsfile] [-O time] [-p port] [-S time] [-T time] [-t interval]
           [-x version] [-Z timezone]

## [](#DESCRIPTION)DESCRIPTION

           webpingvis displays a summary of Web server response-time
           statistics collected from the Performance Co-Pilot (PCP)
           infrastructure.  The display is modulated by the values of
           performance metrics retrieved from the target host (which is
           running pmcd(1) and the pmdawebping(1) Performance Metrics Domain
           Agent) or from the PCP archive log identified by archive.  The
           display is updated every interval seconds (default 2 seconds).

           As in all pmview(1) scenes, when the mouse is moved over one of
           the bars, the current value and metric information for that bar
           will be shown in the text box near the top of the display.  The
           height of the bars is proportional to the performance metric
           values relative to the maximum, as controlled by size of the URLs
           being fetched by pmdawebping(1), and the -m option (see below).

           The bars in the webpingvis scene represent the following
           information:

           Size
               The green bars indicate the relative sizes of the results
               returned for each URL in the pmdawebping workload.

           Response
               For each URL in the pmdawebping workload, the components of
               the Web server response-time (connect, head and body) and the
               total response-time is displayed.

               To the right, the component and total times are summed over
               all URLs in the pmdawebping workload.

           Errors
               The four red error bars indicate the number of socket, HTTP,
               HTML or other errors that occurred in the last iteration of
               the pmdawebping workload.  Any of these errors will terminate
               the request for a URL.

           webpingvis uses pmview(1), and so the user interface follows that
           described for pmview(1), which in turn displays the scene within
           an Inventor examiner viewer.  For generic control of the viewer,
           see ivview(1).

           webpingvis passes most command line options to pmview(1).
           Therefore, the command line options -A, -a, -C, -h, -n, -O, -p,
           -S, -t, -T, -x, -Z and -z, and the user interface are described in
           the pmview(1) man page.

           Options specific to webpingvis are:

           -i     The URL names are not included as labels in the scene by
                  default.  The -i option forces them to be included.

           -m max Change the normalization factor for the response-time bars.
                  The value for max is in units of milliseconds, and should
                  be the expected maximum value for the total response-time
                  aggregated over all URLs in the pmdawebping workload.  The
                  default value is 1000 milliseconds.

           -V     The derived configuration file for pmview(1) is written on
                  standard output.  This may be saved and used directly with
                  pmview(1) if the user wishes to customize the display, or
                  modify some of the normalization parameters.

## [](#CAVEATS)CAVEATS

           As webpingvis sorts the configured URLs by size, running
           webpingvis shortly after starting pmdawebping(1) may result in the
           URLs being sorted incorrectly as they may not have been fetched.

           The ~ character may not be parsed correctly by pmview(1).
           Therefore, if pmdawebping(1) is fetching any URLs containing ~
           then webpingvis will not launch.

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/*
                  default PMNS specification files
           $PCP_VAR_DIR/config/pmlogger/config.webpingvis
                  pmlogger(1) configuration file that can be used to create a
                  PCP archive suitable for display with webpingvis
           $PCP_VAR_DIR/config/pmchart/Web.Response
                  A pmchart(1) configuration file for monitoring Web server
                  response time

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(4).

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), pmchart(1), pmdawebping(1), pmdumplog(1), pminfo(1),
           pmlogger(1), pmval(1), pmview(1), weblogvis(1) and webvis(1).

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

    Performance Co-Pilot                                        WEBPINGVIS(1)

------------------------------------------------------------------------

Pages that refer to this page: [weblogvis(1)](../man1/weblogvis.1.html),  [webvis(1)](../man1/webvis.1.html)

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
