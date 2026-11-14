---
{"title": "pmlogger_check(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogger_check.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogger_check(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGGER_CHECK(1)        General Commands Manual        PMLOGGER_CHECK(1)

## [](#NAME)NAME

           pmlogger_check - administration of Performance Co-Pilot archive
           files

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmlogger_check [-CNnPpqsTV?]  [-c control] [-l
           logfile]

## [](#DESCRIPTION)DESCRIPTION

           pmlogger_check and the related pmlogger_daily(1) tools along with
           associated control files (see pmlogger.control(5)) may be used to
           create a customized regime of administration and management for
           historical archives of performance data within the Performance Co-
           Pilot (see PCPIntro(1)) infrastructure.

           pmlogger_check may be run at any time of the day and is intended
           to check that a desired set of pmlogger(1) processes are running.
           If not, it (re-)starts any missing logger processes.  By default,
           pmlogger_check also calls pmlogger_daily(1) with a -K option to
           execute any required archive compression tasks.

## [](#OPTIONS)OPTIONS

           -C   This option causes pmlogger_check to query the system service
                runlevel information for pmlogger, and use that to determine
                whether to start processes or not.

           -c control, --control=control
                Both pmlogger_check and pmlogger_daily(1) are controlled by
                PCP logger control file(s) that specifies the pmlogger
                instances to be managed.  The default control file is
                $PCP_PMLOGGERCONTROL_PATH but an alternate may be specified
                using the -c option.  If the directory
                $PCP_PMLOGGERCONTROL_PATH.d (or control.d from the -c option)
                exists, then the contents of any additional control files
                therein will be appended to the main control file (which must
                exist).

           -l file, --logfile=file
                In order to ensure that mail is not unintentionally sent when
                these scripts are run from cron(8) or systemd(1) diagnostics
                are always sent to log files.  By default, this file is
                $PCP_LOG_DIR/pmlogger/pmlogger_check.log but this can be
                changed using the -l option.  If this log file already exists
                when the script starts, it will be renamed with a .prev
                suffix (overwriting any log file saved earlier) before
                diagnostics are generated to the log file.  The -l and -t
                options cannot be used together.

           -N, --showme
                This option enables a ``show me'' mode, where the actions are
                echoed, but not executed, in the style of ``make -n''.  Using
                -N in conjunction with -V maximizes the diagnostic
                capabilities for debugging.

           -n, --noerror
                Force the exit status to be 0 other than for catastrophic
                errors.  Useful when called from a systemd(1) service or
                timer unit so that the associated unit is not marked as
                failed in a way that would prevent subsequent execution from
                systemd(1).

           -P, --only-primary
                If this option is specified for pmlogger_check then only the
                primary logger entry in the control files will be processed.
                This is the logical opposite of the -p option described above
                and is intended for use by RC scripts that start only the
                primary logger, such as the pmlogger.service unit.  The -p
                and -P options are mutually exclusive.

           -p, --skip-primary
                If this option is specified for pmlogger_check then any line
                from the control files for the primary pmlogger will be
                ignored.  This option is intended for environments where some
                system daemon, like systemd(1), is responsible for
                controlling (starting, stopping, restarting, etc.) the
                primary pmlogger.

           -q, --quick
                If this option is specified for pmlogger_check then the
                script will ``quickstart'' avoiding any optional processing
                like calling pmlogger_daily(1) to perform archive compression
                tasks.

           -s, --stop
                Use of this option provides the reverse pmlogger_check
                functionality, allowing the set of pmlogger processes to be
                cleanly shutdown.

           -T, --terse
                This option to pmlogger_check produces less verbose output
                than the default.  This is most suitable for a pmlogger
                ``farm'' where many instances of pmlogger are expected to be
                running.

           -V, --verbose
                The -V option enables verbose tracing.  By default
                pmlogger_check generates no output unless some error or
                warning condition is encountered.  A second -V increases the
                verbosity.  Using -N in conjunction with -V maximizes the
                diagnostic capabilities for debugging.

           -?, --help
                Display usage message and exit.

## [](#CONFIGURATION)CONFIGURATION

           Refer to pmlogger.control(5) for a description of the control
           file(s) that are used to control which pmlogger instances and
           which archives are managed by pmlogger_check and
           pmlogger_daily(1).

           The pmlogctl(1) utility may invoke pmlogger_check using the
           sudo(1) command to run it under the $PCP_USER ``pcp'' account.  If
           sudo is configured with the non-default requiretty option (see
           below), pmlogger_check may fail to run due to not having a tty
           configured.  This issue can be resolved by adding a second line
           (expand $PCP_BINADM_DIR according to your platform) to the
           /etc/sudoers configuration file as follows:

                Defaults requiretty
                Defaults!$PCP_BINADM_DIR/pmlogger_check !requiretty

           Note that the unprivileged PCP account under which these commands
           run uses /sbin/nologin as the shell, so the requiretty option is
           ineffective here and safe to disable in this way.

## [](#FILES)FILES

           $PCP_VAR_DIR/config/pmlogger/config.default
                default pmlogger configuration file location for the local
                primary logger, typically generated automatically by
                pmlogconf(1).

           $PCP_ARCHIVE_DIR/<hostname>
                default location for archives of performance information
                collected from the host hostname

           $PCP_ARCHIVE_DIR/<hostname>/lock
                transient lock file to guarantee mutual exclusion during
                pmlogger administration for the host hostname - if present,
                can be safely removed if neither pmlogger_daily(1) nor
                pmlogger_check are running

           $PCP_ARCHIVE_DIR/<hostname>/Latest
                PCP archive folio created by mkaf(1) for the most recently
                launched archive containing performance metrics from the host
                hostname

           $PCP_LOG_DIR/NOTICES
                PCP ``notices'' file used by pmie(1) and friends

           $PCP_LOG_DIR/pmlogger/pmlogger_check.log
                if the previous execution of pmlogger_check produced any
                output it is saved here.  The normal case is no output in
                which case the file does not exist.

           $PCP_ARCHIVE_DIR/SaveLogs
                if this directory exists, then the log file from the -l
                argument for pmlogger_check will be saved in this directory
                with the name of the format <date>-pmlogger_check.log.<pid>
                This allows the log file to be inspected at a later time,
                even if several pmlogger_check executions have been launched
                in the interim.  Because the PCP archive management tools run
                under the $PCP_USER account ``pcp'',
                $PCP_ARCHIVE_DIR/SaveLogs typically needs to be owned by the
                user ``pcp''.

           $PCP_ARCHIVE_DIR/<hostname>/SaveLogs
                 if this directory exists, then the log file from the -l
                 argument of a newly launched pmlogger(1) for hostname will
                 be saved in this directory with the name archive.log where
                 archive is the basename of the associated pmlogger(1) PCP
                 archive files.  This allows the log file to be inspected at
                 a later time, even if several pmlogger(1) instances for
                 hostname have been launched in the interim.  Because the PCP
                 archive management tools run under the $PCP_USER account
                 ``pcp'', $PCP_ARCHIVE_DIR/<hostname>/SaveLogs typically
                 needs to be owned by the user ``pcp''.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           The default behaviour, when pmlogger(1) configuration comes from
           pmlogconf(1), is to regenerate the configuration file and check
           for changes whenever pmlogger(1) is started from pmlogger_check.
           If the PMDA configuration is stable, this is not necessary, and
           setting $PMLOGGER_CHECK_SKIP_LOGCONF to yes disables the
           regeneration and checking.

## [](#SEE_ALSO)SEE ALSO

           mkaf(1), PCPIntro(1), pmie(1), pmlc(1), pmlogconf(1), pmlogctl(1),
           pmlogger(1), pmlogger_daily(1), pmlogger_daily_report(1),
           pmlogger_janitor(1), sudo(1), systemd(1), pmlogger.control(5) and
           cron(8).

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

    Performance Co-Pilot               PCP                  PMLOGGER_CHECK(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcpintro(1)](../man1/pcpintro.1.html),  [pmfind_check(1)](../man1/pmfind_check.1.html),  [pmlogcompress(1)](../man1/pmlogcompress.1.html),  [pmlogctl(1)](../man1/pmlogctl.1.html),  [pmlogdump(1)](../man1/pmlogdump.1.html),  [pmlogextract(1)](../man1/pmlogextract.1.html),  [pmlogger(1)](../man1/pmlogger.1.html),  [pmlogger_daily(1)](../man1/pmlogger_daily.1.html),  [pmlogger_janitor(1)](../man1/pmlogger_janitor.1.html),  [pmloglabel(1)](../man1/pmloglabel.1.html),  [pmsnap(1)](../man1/pmsnap.1.html),  [LOGARCHIVE(5)](../man5/LOGARCHIVE.5.html),  [pmlogger.control(5)](../man5/pmlogger.control.5.html)

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
