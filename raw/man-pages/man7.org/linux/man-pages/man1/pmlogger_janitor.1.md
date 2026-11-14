---
{"title": "pmlogger_janitor(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogger_janitor.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogger_janitor(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERATION](#OPERATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGGER_JANITOR(1)      General Commands Manual      PMLOGGER_JANITOR(1)

## [](#NAME)NAME

           pmlogger_janitor - management helper for Performance Co-Pilot
           archive files

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmlogger_janitor [-NV?]  [-c control] [-l logfile]
           [-X program] [-Y regex]

## [](#DESCRIPTION)DESCRIPTION

           Typically pmlogger_janitor is not used directly, rather it is
           called from pmlogger_check(1) to clean up any residual processes
           and state files associated with moribund instances of pmlogger(1).

           If pmlogger_janitor is run directly, it needs to be run as the
           user $PCP_USER; the only exception is when the -N option is used.

## [](#OPTIONS)OPTIONS

           -c control, --control=control
                Like pmlogger_check(1) and pmlogger_daily(1),
                pmlogger_janitor is controlled by PCP logger control file(s)
                that specify the pmlogger instances to be managed.  The
                default control file is $PCP_PMLOGGERCONTROL_PATH but an
                alternate may be specified using the -c option.  If the
                directory $PCP_PMLOGGERCONTROL_PATH.d (or control.d from the
                -c option) exists, then the contents of any additional
                control files therein will be appended to the main control
                file (which must exist).

           -l file, --logfile=file
                In order to ensure that mail is not unintentionally sent when
                this script is run from cron(8) or systemd(1) diagnostics are
                always sent to log files.  By default, this file is
                $PCP_LOG_DIR/pmlogger/pmlogger_janitor.log but this can be
                changed using the -l option.  If this log file already exists
                when the script starts, it will be renamed with a .prev
                suffix (overwriting any log file saved earlier) before
                diagnostics are generated to the log file.

           -N, --showme
                This option enables a ``show me'' mode, where the actions are
                echoed, but not executed, in the style of ``make -n''.  Using
                -N in conjunction with -V maximizes the diagnostic
                capabilities for debugging.

           -V, --verbose
                The -V option enables verbose tracing.  By default
                pmlogger_janitor generates no output unless some error or
                warning condition is encountered.  A second -V increases the
                verbosity.  Using -N in conjunction with -V maximizes the
                diagnostic capabilities for debugging.

           -X program, --compressor=program
                This option specifies the program to use for compression.
                Refer to pmlogger_daily(1) for details.

           -Y regex, --regex=regex
                This option allows a regular expression to be specified
                causing files in the set of files matched for compression to
                be omitted.  Refer to pmlogger_daily(1) for details.

           -?, --help
                Display usage message and exit.

## [](#OPERATION)OPERATION

           pmlogger_janitor operates in a number of passes looking for things
           to cleanup.

           Pass 1 Scan the pmlogger port map files in the
                  $PCP_TMP_DIR/pmlogger directory.  Use the process id (PID)
                  from the name of the port map file and ps(1) to check and
                  if the process exists and it ``looks like'' an active
                  pmlogger; if so append the PID and the directory where the
                  archive is being written (extracted from the port map file)
                  to a list of interest, otherwise the port map file is
                  assumed to be associated with a pmlogger that has exited
                  and the port map file is removed.

           Pass 2 Use ps(1) to scan all processes and identify any pmlogger
                  instances that were started by pmlogger_check(3) or
                  pmlogger_daily(3), these will have a signature -m option in
                  their arguments.  Append the PIDs and directories where the
                  archive is being written (extracted from the command line
                  arguments) to the list of interest.

           Pass 3 Parse all of the pmlogger.control(5) files from either the
                  standard places, or control if the -c option is used.  For
                  each pmlogger instance, it should be in the list of
                  interest, and if so remove it from that list.

                  If the list of interest is empty at the end of this Pass,
                  we're done.

           Pass 4 Each process remaining in the list of interest is a
                  pmlogger that is running, but should not be; probably as a
                  result of a change to the pmlogger.control(5) files.  Send
                  each process a SIGTERM.

           Pass 5 For each process remaining in the list of interest after
                  Pass 3 compress any archives in the directory pmlogger was
                  writing into.  This is the only step where the -X and -Y
                  options might be used.

           Pass 6 For each pmlogger sent a SIGTERM in Pass 4 check that it
                  has exited and if not send it a SIGKILL.

## [](#FILES)FILES

           $PCP_LOG_DIR/pmlogger/pmlogger_janitor.log
                if the previous execution of pmlogger_janitor produced any
                output it is saved here.  The normal case is no output in
                which case the file does not exist.

           $PCP_ARCHIVE_DIR/SaveLogs
                if this directory exists, then the log file from the -l
                argument for pmlogger_janitor will be saved in this directory
                with the name of the format <date>-pmlogger_janitor.log.<pid>
                This allows the log file to be inspected at a later time,
                even if several pmlogger_janitor executions have been
                launched in the interim.  $PCP_ARCHIVE_DIR/SaveLogs needs to
                be owned by the user $PCP_USER.

           $PCP_TMP_DIR/pmlogger
                pmlogger maintains the files in this directory as the port
                map between the PID of the pmlogger instance, the IPC port
                that may be used to control each pmlogger instance (as used
                by pmlc(1)), the name of the host where pmcd(1) is providing
                the metrics for pmlogger, the remote connection string for
                the remote HTTP server that is receiving the logged data or
                the full path to the archive base name for a local logger and
                any annotation from the -m or -x options; all of this
                information is also available via the pmcd.pmlogger.*
                metrics, e.g. $ pminfo -f pmcd.pmlogger

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmlc(1), pmlogctl(1), pmlogger(1),
           pmlogger_check(1), pmlogger_daily(1), ps(1), systemd(1),
           pmlogger.control(5) and cron(8).

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

    Performance Co-Pilot               PCP                PMLOGGER_JANITOR(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogger_check(1)](../man1/pmlogger_check.1.html)

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
