---
{"title": "pmlogger.control(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/pmlogger.control.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogger.control(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SCHEDULED EXECUTION](#SCHEDULED_EXECUTION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGGER.CONTROL(5)        File Formats Manual        PMLOGGER.CONTROL(5)

## [](#NAME)NAME

           pmlogger.control - control files for Performance Co-Pilot
           archiving

## [](#DESCRIPTION)DESCRIPTION

           Historical archiving of performance data for Performance Co-Pilot
           (see PCPIntro(1)) uses pmlogger(1) and one or more instances of
           pmlogger may be managed by pmlogger_check(1) and
           pmlogger_daily(1).

           pmlogger_check(1) may be run at any time of the day and is
           intended to check that the desired set of pmlogger processes are
           running.  If not, it (re-)starts any missing logger processes.  By
           default, pmlogger_check(1) also calls pmlogger_daily(1) with a -K
           option to execute any required archive compression tasks.

           pmlogger_daily(1) is intended to be run once per day, preferably
           in the early morning, as soon after midnight as practicable.  Its
           task is to aggregate, rotate and perform general housekeeping for
           one or more sets of PCP archives.

           Both pmlogger_check(1) and pmlogger_daily(1) operate on a family
           of shared control files, namely the $PCP_PMLOGGERCONTROL_PATH file
           and files within the $PCP_PMLOGGERCONTROL_PATH.d directory.  These
           files must not be writable by any user other than root.

           The control file(s) should be customized according to the
           following rules that define for the current version (1.1) of the
           control file format.

           1.  Lines beginning with a ``#'' are comments.  A special case is
               lines beginning ``#!#''; these are control lines for a
               pmlogger that has been stopped using pmlogctl(1).
           2.  Lines beginning with a ``$'' are assumed to be assignments to
               environment variables in the style of sh(1), and all text
               following the ``$'' will be eval'ed by the script reading the
               control file, and the corresponding variable exported into the
               environment.  This is particularly useful to set and export
               variables into the environment of the administrative scripts,
               e.g.
                   $ PMCD_CONNECT_TIMEOUT=20
               If the value to the right of the ``='' contains any white
               space, then the value should be enclosed in double (") or
               single (') quotes.
               As the lines in each control file are processed in order, it
               is important that any environment variables should be set
               before a control line that specifies a pmlogger instance that
               might expect to use those environment variables, e.g. to
               control compression or culling of archives by
               pmlogger_daily(1).
           3.  There should be a version line in the control file of the
               form:
                   $version=1.1
               But since the only version currently supported is 1.1, this
               declaration provides no additional value beyond documentation.

           4.  Fields within a line of the control file(s) are usually
               separated by one or more spaces or tabs (although refer to the
               description of the directory field below for some important
               exceptions).

           5.  There should be one line in the control file(s) for each
               pmlogger instance with at least 4 fields of the form:
                   host primary socks directory args ...

           6.  The host field is the name of the host that is the source of
               the performance metrics for this pmlogger instance.  The
               reserved word LOCALHOSTNAME will be replaced by local: (so
               connection to pmcd(1) on the local host).

           7.  The primary field indicates if this is a primary pmlogger
               instance (y) or not (n).  Since the primary logger must run on
               the local host, and there may be at most one primary logger
               for a particular host, this field can be y for at most one
               pmlogger instance, in which case the host name must be the
               name of the local host (or LOCALHOSTNAME).

           8.  The socks field indicates if this pmlogger instance needs to
               be started under the control of pmsocks(1) to connect to a
               pmcd(1) through a firewall (y or n).

           9.  The directory field is a directory name.  All archive files
               associated with this pmlogger instance will be created in this
               directory, and this will be the current directory for the
               execution of any programs required to maintain those archives.
               A useful convention is that primary logger archives for the
               local host with hostname myhost are maintained in the
               directory $PCP_ARCHIVE_DIR/myhost (this is where the default
               pmlogger start-up script in $PCP_RC_DIR/pmlogger will create
               the archives), while archives for the remote host mumble are
               maintained in $PCP_ARCHIVE_DIR/mumble.

           10. The directory field may contain embedded shell syntax that
               will be evaluated by sh(1) to produce the real directory name
               to be used.  The allowed constructs are:
               • Any text (including white space) enclosed with $( and ) will
                 be interpreted as a shell command.
               • Any text (including white space) enclosed with ` and ` (back
                 quotes) will be interpreted as a shell command.
               • Within a single line only one style of embedded shell
                 command is allowed, so either $(...)  or `...`, but not
                 both.
               • An initial double quote (") followed by arbitrary text
                 (including white space, but excluding an embedded double
                 quote) and a final double quote.
               • An initial single quote (') followed by arbitrary text
                 (including white space, but excluding an embedded single
                 quote) and a final single quote.
               • Any word containing a $ (assumed to introduce an environment
                 variable name).
           11. In the directory field, the reserved word LOCALHOSTNAME will
               be replaced by the name of the local host.  Similarly the
               reserved words PCP_ARCHIVE_DIR and PCP_LOG_DIR appearing
               anywhere in the directory field will be replaced by the values
               of the corresponding environment variables.
           12. If the directory field (after any shell substitution) begins
               with ``+'' then this indicates that pmlogger(1) will be
               executed with a -R option in args to ``push'' the archive to a
               remote pmproxy(1) server.  In this case, no archive files are
               stored locally, but directory (after the leading ``+'' is
               stripped) is used as the directory in which the log file from
               the local pmlogger(1) will be stored and possibly the location
               for the pmlogger(1) configuration file (see the example
               below).
           13. The optional args field and any remaining fields are
               interpreted as arguments to be passed to pmlogger(1).  Most
               typically this would be at least the -c option to specify the
               metrics to be logged and the logging frequencies, and/or -R in
               the case of a ``push'' archive.

           The following sample control lines specify a primary logger on the
           local host (bozo), non-primary loggers to collect and log
           performance metrics from the hosts wobbly, boing and the local
           host (i.e. bozo) and a logger pushing archives to the remote
           pmproxy(1) on the host grunt.

           $version=1.1
           bozo          y  n  $PCP_ARCHIVE_DIR/bozo   -c config.default
           wobbly        n  n  "/store/wobbly/$(date +%Y)"  -c ./wobbly.config
           boing         n  n  $PCP_ARCHIVE_DIR/boing   -c ./pmlogger.config
           LOCALHOSTNAME n  n  /cluster/LOCALHOSTNAME   -c ./precious.config
           LOCALHOSTNAME n  n  +PCP_ARCHIVE_DIR/remote -R http://grunt:44322 \
                               -c ./remote.config

## [](#SCHEDULED_EXECUTION)SCHEDULED EXECUTION

           The periodic execution of pmlogger_check(1) and pmlogger_daily(1)
           is controlled by either systemd(1) or cron(8).

           Typical crontab(5) entries are provided in
           $PCP_SYSCONF_DIR/pmlogger/crontab (unless installed by default in
           /etc/cron.d already) and shown below.

           # daily processing of archives
           14      0       *       *       *       $PCP_BINADM_DIR/pmlogger_daily
           # every 30 minutes, check pmlogger instances are running
           25,55   *       *       *       *       $PCP_BINADM_DIR/pmlogger_check

           When using systemd(1) on Linux, no crontab entries are needed as
           the timer mechanism provided by systemd is used instead to achieve
           the same period execution as the crontab example above.

## [](#FILES)FILES

           $PCP_PMLOGGERCONTROL_PATH
                the PCP logger control file.  For a new installation this
                file contains no pmlogger(1) control lines (the real control
                files are all in the $PCP_PMLOGGERCONTROL_PATH.d directory),
                but this file is still processed to support any legacy
                configurations therein from earlier PCP releases.
                Warning: this file must not be writable by any user other
                than root.

           $PCP_PMLOGGERCONTROL_PATH.d
                optional directory containing additional PCP logger control
                files, with one or more per pmlogger specification per file.
                Warning: the files herein must not be writable by any user
                other than root.

           $PCP_SYSCONF_DIR/pmlogger/crontab
                sample crontab for automated script execution by $PCP_USER
                (or root).  Exists only if the platform does not support the
                /etc/cron.d mechanism.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmlogctl(1), pmlogger(1), pmlogger_check(1),
           pmlogger_daily(1), pmlogger_daily_report(1), pmproxy(1),
           pmsocks(1), systemd(1) and cron(8).

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

    Performance Co-Pilot               PCP                PMLOGGER.CONTROL(5)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogger_check(1)](../man1/pmlogger_check.1.html),  [pmlogger_daily(1)](../man1/pmlogger_daily.1.html),  [pmlogger_janitor(1)](../man1/pmlogger_janitor.1.html)

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
