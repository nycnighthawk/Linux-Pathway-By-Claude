---
{"title": "pmlogger_daily(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogger_daily.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogger_daily(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CALLBACKS](#CALLBACKS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [COMPATIBILITY ISSUES](#COMPATIBILITY_ISSUES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGGER_DAILY(1)        General Commands Manual        PMLOGGER_DAILY(1)

## [](#NAME)NAME

           pmlogger_daily - administration of Performance Co-Pilot archive
           files

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmlogger_daily [-DEfKMNnoPpQrRVzZ?]  [-c control]
           [-d fssize] [-k time] [-l logfile] [-m addresses] [-s size] [-t
           want] [-x time] [-X program] [-Y regex]

## [](#DESCRIPTION)DESCRIPTION

           pmlogger_daily and the related pmlogger_check(1) tools along with
           associated control files (see pmlogger.control(5)) may be used to
           create a customized regime of administration and management for
           historical archives of performance data within the Performance Co-
           Pilot (see PCPIntro(1)) infrastructure.

           pmlogger_daily is intended to be run once per day, preferably in
           the early morning, as soon after midnight as practicable.  Its
           task is to aggregate, rotate and perform general housekeeping one
           or more sets of PCP archives.

           To accommodate the evolution of PMDAs and changes in production
           logging environments, pmlogger_daily is integrated with
           pmlogrewrite(1) to allow optional and automatic rewriting of
           archives before merging.  If there are global rewriting rules to
           be applied across all archives mentioned in the control file(s),
           then create the directory $PCP_SYSCONF_DIR/pmlogrewrite and place
           any pmlogrewrite(1) rewriting rules in this directory.  For
           rewriting rules that are specific to only one family of archives,
           use the directory name from the control file(s) - i.e. the fourth
           field - and create a file, or a directory, or a symbolic link
           named pmlogrewrite within this directory and place the required
           rewriting rule(s) in the pmlogrewrite file or in files within the
           pmlogrewrite subdirectory.  pmlogger_daily will choose rewriting
           rules from the archive directory if they exist, else rewriting
           rules from $PCP_SYSCONF_DIR/pmlogrewrite if that directory exists,
           else no rewriting is attempted.

           As an alternate mechanism, if the file
           $PCP_LOG_DIR/pmlogger/.NeedRewrite exists when pmlogger_daily
           starts then this is treated the same as specifying -R on the
           command line and $PCP_LOG_DIR/pmlogger/.NeedRewrite will be
           removed once all the rewriting has been done.

## [](#OPTIONS)OPTIONS

           -c control, --control=control
                Both pmlogger_daily and pmlogger_check(1) are controlled by
                PCP logger control file(s) that specifies the pmlogger(1)
                instances to be managed.  The default control file is
                $PCP_PMLOGGERCONTROL_PATH, but an alternate may be specified
                using the -c option.  If the directory
                $PCP_PMLOGGERCONTROL_PATH.d (or control.d from the -c option)
                exists, then the contents of any additional control files
                therein will be appended to the main control file (which must
                exist).

           -D, --noreport
                Do not perform the conditional pmlogger_daily_report(1)
                processing as described below.

           -d fssize, --disk=fssize
                This option enforces a maximum total file system space usage
                per host directory for PCP archive files stored under each
                $PCP_ARCHIVE_DIR/<hostname> and
                $PCP_REMOTE_ARCHIVE_DIR/<hostname> location. The fssize must
                be specified as an integer with a suffix K or k for
                kilobytes, M or m for megabytes, G or g for gigabytes (e.g.
                500m or 10G).  As a special case, fssize may be the keyword
                unlimited to prevent any file system space limit enforcement
                (this is the default behaviour).

                Alternatively, the file system space limit may be set by
                exporting the $PCP_SPACELIMIT environment variable, which is
                handled analogously to $PCP_CULLAFTER.  If both
                $PCP_SPACELIMIT and -d are provided and specify different
                values then the value from the environment variable is used
                and a warning is issued.

                After normal daily log processing (compression, merging,
                culling by age, etc.)  completes, if the total file system
                space consumed by any pmlogger(1) instance exceeds fssize,
                then additional archive files will be purged (i.e. removed),
                oldest first, until the file system usage is reduced to be
                not more than fssize.  This purging operation never deletes
                archive files with today's date, and so always preserves the
                most recent archives required by active pmlogger(1)
                processes.

                Enforcement is only performed when pmlogger_daily runs
                (typically once a day), not continuously.  As a result, the
                total file system usage for any pmlogger(1) instance may
                exceed a specified maximum between pmlogger_daily executions
                (for example, as new archives are created or when archives
                are uncompressed for merging or prior to asynchronous archive
                compression).

           -E, --expunge
                This option causes pmlogger_daily to pass the -E flag to
                pmlogger_merge(1) in order to expunge metrics with metadata
                inconsistencies and continue rather than fail.  This is
                intended for automated daily archive rotation where it is
                highly desirable for unattended daily archive merging,
                rewriting and compression to succeed.  For further details,
                see pmlogger_merge(1) and description for the -x flag in
                pmlogextract(1).

           -f, --force
                This option forces pmlogger_daily to attempt compression
                actions.  Using this option in production is not recommended.

           -k time, --discard=time
                After some period, old PCP archives are discarded.  time is a
                time specification in the syntax of find-filter(1), so
                DD[:HH[:MM]].  The optional HH (hours) and MM (minutes) parts
                are 0 if not specified.  By default the time is 14:0:0 or 14
                days, but may be changed using this option.

                Some special values are recognized for the time, namely 0 to
                keep no archives beyond the the ones being currently written
                by pmlogger(1), and forever or never to prevent any archives
                being discarded.

                The time can also be set using the $PCP_CULLAFTER variable,
                set in either the environment or in a control file.  If both
                $PCP_CULLAFTER and -k specify different values for time then
                the environment variable value is used and a warning is
                issued, i.e. if $PCP_CULLAFTER is set in the control file, it
                overrides -k given on the command line.

                Note that the semantics of time are that it is measured from
                the time of last modification of each archive, and not from
                the original archive creation date.  This has subtle
                implications for compression (see below) - the compression
                process results in the creation of new archive files which
                have new modification times.  In this case, the time period
                (re)starts from the time of compression.

           -K   When this option is specified for pmlogger_daily then only
                the compression tasks are attempted, so no pmlogger rotation,
                no culling, no rewriting, etc.  When -K is used and a period
                of 0 is in effect (from -x on the command line or
                $PCP_COMPRESSAFTER in the environment or via the control
                file) this is intended for environments where compression of
                archives is desired before the scheduled daily processing
                happens.  To achieve this, once pmlogger_check(1) has
                completed regular processing, it calls pmlogger_daily with
                just the -K option.  Provided $PCP_COMPRESSAFTER is set to 0
                along with any other required compression options to match
                the scheduled invocation of pmlogger_daily, then this will
                compress all volumes except the ones being currently written
                by pmlogger(1).  If $PCP_COMPRESSAFTER is set to a value
                greater than zero, then manually running pmlogger_daily with
                the -x option may be used to compress volumes that are
                younger than the $PCP_COMPRESSAFTER time.  This may be used
                to reclaim filesystem space by compressing volumes earlier
                than they would have otherwise been compressed.  Note that
                since the default value of $PCP_COMPRESSAFTER is 0 days, the
                -x option has no effect unless the control file has been
                edited and $PCP_COMPRESSAFTER has been set to a value greater
                than 0.

                The default value of $PCP_COMPRESSAFTER is 0 if zstd(1) is
                installed, or if xz(1) is installed and the lzma library is
                available (as reported for the transparent_decompress option
                by pmconfig(1)).  Otherwise the default value of
                $PCP_COMPRESSAFTER is never.

           -l file, --logfile=file
                In order to ensure that mail is not unintentionally sent when
                these scripts are run from cron(8) or systemd(1) diagnostics
                are always sent to log files.  By default, this file is
                $PCP_LOG_DIR/pmlogger/pmlogger_daily.log but this can be
                changed using the -l option.  If this log file already exists
                when the script starts, it will be renamed with a .prev
                suffix (overwriting any log file saved earlier) before
                diagnostics are generated to the log file.  The -l and -t
                options cannot be used together.

           -m addresses, --mail=addresses
                Use of this option causes pmlogger_daily to construct a
                summary of the ``notices'' file entries which were generated
                in the last 24 hours, and e-mail that summary to the set of
                space-separated addresses.  This daily summary is stored in
                the file $PCP_LOG_DIR/NOTICES.daily, which will be empty when
                no new ``notices'' entries were made in the previous 24 hour
                period.

           -M   This option may be used to disable archive merging (or
                renaming) and rewriting (-M implies -r).  This is most useful
                in cases where the archives are being incrementally copied to
                a remote repository, e.g. using rsync(1).  Merging, renaming
                and rewriting all risk an increase in the synchronization
                load, especially immediately after pmlogger_daily has run, so
                -M may be useful in these cases.

           -N, --showme
                This option enables a ``show me'' mode, where the programs
                actions are echoed, but not executed, in the style of ``make
                -n''.  Using -N in conjunction with -V maximizes the
                diagnostic capabilities for debugging.

           -n, --noerror
                Force the exit status to be 0 other than for catastrophic
                errors.  Useful when called from a systemd(1) service or
                timer unit so that the associated unit is not marked as
                failed in a way that would prevent subsequent execution from
                systemd(1).

           -o   By default all possible archives will be merged.  This option
                reinstates the old behaviour in which only yesterday's
                archives will be considered as merge candidates.  In the
                special case where only a single input archive needs to be
                merged, pmlogmv(1) is used to rename the archive, otherwise
                pmlogger_merge(1) is used to merge all of the archives for a
                single host and a single day into a new PCP archive and the
                individual archives are removed.

           -P, --noproxy
                By default, in addition to the archives created by local
                pmlogger(1) instances below the $PCP_ARCHIVE_DIR/<hostname>
                directories pmlogger_daily will also process the archives
                that have been ``pushed'' from a remote pmlogger(1) via the
                local pmproxy(1) and stored below the
                $PCP_LOG_DIR/pmproxy/<hostname> directories.  The -P option
                prevents the processing of the archives from pmproxy(1).

           -p   If this option is specified for pmlogger_daily then the
                status of the daily processing is polled and if the daily
                pmlogger(1) rotation, culling, rewriting, compressing, etc.
                has not been done in the last 24 hours then it is done now.
                The intent is to have pmlogger_daily called regularly with
                the -p option (at 30 mins past the hour, every hour in the
                default cron(8) set up) to ensure daily processing happens as
                soon as possible if it was missed at the regularly scheduled
                time (which is 00:10 by default), e.g. if the system was down
                or suspended at that time.  With this option pmlogger_daily
                simply exits if the previous day's processing has already
                been done.  Note that this option is not used on platforms
                supporting systemd(1) because the pmlogger_daily.timer
                service unit specifies a timer setting with Persistent=true.
                The -K and -p options to pmlogger_daily are mutually
                exclusive.

           -Q, --proxyonly
                The inverse of -P described above, namely only process the
                archives that have been ``pushed'' from a remote pmlogger(1)
                via the local pmproxy(1) and ignore all archives created by
                local pmlogger(1) instances below the
                $PCP_ARCHIVE_DIR/<hostname> directories.

           -r, --norewrite
                This command line option acts as an override and prevents all
                archive rewriting with pmlogrewrite(1) independent of the
                presence of any rewriting rule files or directories.

           -R, --rewriteall
                Sometimes PMDA changes require all archives to be rewritten,
                not just the ones involved in any current merging.  This is
                required for example after a PCP upgrade where a new version
                of an existing PMDA has revised metadata.  The -R command
                line forces this universal-style of rewriting.  The -R option
                to pmlogger_daily is mutually exclusive with both the -r and
                -M options.

           -s size, --rotate=size
                If the PCP ``notices'' file ($PCP_LOG_DIR/NOTICES) is larger
                than 20480 bytes, pmlogger_daily will rename the file with a
                ``.old'' suffix, and start a new ``notices'' file.  The
                rotate threshold may be changed from 20480 to size bytes
                using the -s option.

           -t period
                To assist with debugging or diagnosing intermittent failures
                the -t option may be used.  This will turn on very verbose
                tracing (-VV) and capture the trace output in a file named
                $PCP_LOG_DIR/pmlogger/daily.datestamp.trace, where datestamp
                is the time pmlogger_daily was run in the format
                YYYYMMDD.HH.MM.  In addition, the period argument will ensure
                that trace files created with -t will be kept for period days
                and then discarded.

           -V, --verbose
                The output from the cron(8) execution of the scripts may be
                extended using the -V option to the scripts which will enable
                verbose tracing of their activity.  By default the scripts
                generate no output unless some error or warning condition is
                encountered.  A second -V increases the verbosity.  Using -N
                in conjunction with -V maximizes the diagnostic capabilities
                for debugging.

           -x time, --compress-after=time
                Archive data files can optionally be compressed after some
                period to conserve file system space.  This is particularly
                useful for large numbers of pmlogger(1) processes under the
                control of pmlogger_daily.

                time is a time specification in the syntax of find-filter(1),
                so DD[:HH[:MM]].  The optional HH (hours) and MM (minutes)
                parts are 0 if not specified.

                Some special values are recognized for the time, namely 0 to
                apply compression as soon as possible, and forever or never
                to prevent any compression being done.

                If transparent_decompress is enabled when libpcp was built
                (can be checked with the pmconfig(1) -L option), then the
                default behaviour is compression ``as soon as possible''.
                Otherwise the default behaviour is to not compress files
                (which matches the historical default behaviour in earlier
                PCP releases).

                The time can also be set using the $PCP_COMPRESSAFTER
                variable, set in either the environment or in a control file.
                If both $PCP_COMPRESSAFTER and -x specify different values
                for time then the environment variable value is used and a
                warning is issued.  For important other detailed notes
                concerning volume compression, see the -K and -k options
                (above).

           -X program, --compressor=program
                This option specifies the program to use for compression - by
                default this is pmlogcompress(1).  The environment variable
                $PCP_COMPRESS may be used as an alternative mechanism to
                define program.  If both $PCP_COMPRESS and -X specify
                different compression programs then the environment variable
                value is used and a warning is issued.

           -Y regex, --regex=regex
                This option allows a regular expression to be specified
                causing files in the set of files matched for compression to
                be omitted - this allows only the data file to be compressed,
                and also prevents the program from attempting to compress it
                more than once.  The default regex is
                "\.(index|Z|gz|bz2|zip|xz|lzma|lzo|lz4|zst)$"
                - such files are filtered using the -v option to egrep(1).
                The environment variable $PCP_COMPRESSREGEX may be used as an
                alternative mechanism to define regex.  If both
                $PCP_COMPRESSREGEX and -Y specify different values for regex
                then the environment variable value is used and a warning is
                issued.

           -z   This option causes pmlogger_daily to not ``re-exec'', see
                pmlogger(1), when it would otherwise choose to do so and is
                intended only for QA testing.

           -Z   This option causes pmlogger_daily to ``re-exec'', see
                pmlogger(1), whenever that is possible and is intended only
                for QA testing.

           -?, --help
                Display usage message and exit.

## [](#CALLBACKS)CALLBACKS

           Additionally pmlogger_daily supports the following ``hooks'' to
           allow auxiliary operations to be performed at key points in the
           daily processing of the archives.  These callbacks are controlled
           via variables that may be set in the environment or via the
           control file.

           Note that merge callbacks and autosaving described below are not
           enabled when only compression tasks are being attempted, i.e. when
           -K command line option is used.

           All of the callback script execution and the autosave file moving
           will be executed as the non-privileged user ``pcp'' and group
           ``pcp'', so appropriate permissions may need to have been set up
           in advance.

           $PCP_MERGE_CALLBACK
                As each day's archive is created by merging and before any
                compression takes place, if $PCP_MERGE_CALLBACK is defined,
                then it is assumed to be a script that will be called with
                one argument being the name of the archive (stripped of any
                suffixes), so something of the form
                /some/directory/path/YYYYMMDD.  The script needs to be either
                a full pathname, or something that will be found on the
                shell's $PATH .  The callback script will be run in the
                foreground, so pmlogger_daily will wait for it to complete.

                If the control file contains more than one
                $PCP_MERGE_CALLBACK specification then these will be run
                serially in the order they appear in the control file.  If
                $PCP_MERGE_CALLBACK is defined in the environment when
                pmlogger_daily is run, this is treated as though this option
                was the first in the control file, i.e. it will be run before
                any merge callbacks mentioned in the control file.

                If the pcp-zeroconf packages is installed, then a special
                merge callback is added to call pmlogger_daily_report(1)
                first, before any other merge callback options, but only for
                the primary pmlogger(1) instance.  Refer to
                pmlogger_daily_report(1) for an explanation of the pcp-
                zeroconf requirements.

                If pmlogger_daily is in ``catch up'' mode (more than one
                day's worth of archives need to be combined) then each call
                back is executed once for each day's archive that is
                generated.

                A typical use might be to produce daily reports from the PCP
                archive which needs to wait until the archive has been
                created, but is more efficient if it is done before any
                potential compression of the archive.

           $PCP_COMPRESS_CALLBACK
                If pmlogger_daily is run with -x 0 or $PCP_COMPRESSAFTER=0,
                then compression is done immediately after merging.  As each
                day's archive is compressed, if $PCP_COMPRESS_CALLBACK is
                defined, then it is assumed to be a script that will be
                called with one argument being the name of the archive
                (stripped of any suffixes), so something of the form
                /some/directory/path/YYYYMMDD.  The script needs to be either
                a full pathname, or something that will be found on the
                shell's $PATH .  The callback script will be run in the
                foreground, so pmlogger_daily will wait for it to complete.

                If the control file contains more than one
                $PCP_COMPRESS_CALLBACK specification then these will be run
                serially in the order they appear in the control file.  If
                $PCP_COMPRESS_CALLBACK is defined in the environment when
                pmlogger_daily is run, this is treated as though this option
                was the first in the control file, i.e. it will be run first.

                If pmlogger_daily is in ``catch up'' mode (more than one
                day's worth of archives need to be compressed) then each call
                back is executed once for each day's archive that is
                compressed.

                A typical use might be to keep recent archives in
                uncompressed form for efficient querying, but move the older
                archives to some other storage location once the compression
                has been done.

           $PCP_AUTOSAVE_DIR
                Once the merging and possible compression has been done by
                pmlogger_daily, if $PCP_AUTOSAVE_DIR is defined then all of
                the physical files that make up one day's archive will be
                moved (autosaved) to the directory specified by
                $PCP_AUTOSAVE_DIR.

                The basename of the archive is used to set the reserved words
                DATEYYYY (year), DATEMM (month) and DATEDD (day) and these
                (along with LOCALHOSTNAME) may appear literally in
                $PCP_AUTOSAVE_DIR, and will be substituted at execution time
                to generate the destination directory name.  For example:
                  $PCP_AUTOSAVE_DIR=/gpfs/LOCALHOSTNAME/DATEYYYY/DATEMM-
                  DATEDD

                Note that these ``date'' reserved words correspond to the
                date on which the archive data was collected, not the date
                that pmlogger_daily was run.

                If $PCP_AUTOSAVE_DIR (after LOCALHOSTNAME and ``date''
                substitution) does not exist then pmlogger_daily will attempt
                to create it (along with any parent directories that do not
                exist).  Just be aware that this directory creation runs
                under the uid of the user ``pcp'', so directories along the
                path to $PCP_AUTOSAVE_DIR may need to be writeable by this
                non-root user.

                By ``move'' the archives we mean a paranoid checksum-copy-
                checksum-remove (using the -c option for pmlogmv(1)) that
                will bail if the copy fails or the checksums do not match
                (the archives are important so we cannot risk something like
                a full filesystem or a permissions issue messing with the
                copy process).

                If pmlogger_daily is in ``catch up'' mode (more than one
                day's worth of archives need to be combined) then the
                archives for more than one day could be copied in this step.

                A typical use might be to create PCP archives on a local
                filesystem initially, then once all the data for a single day
                has been collected and merged, migrate that day's archive to
                a shared filesystem or a remote filesystem.  This may allow
                automatic backup to off-site storage and/or reduce the number
                of I/O operations and filesystem metadata operations on the
                (potentially slower) non-local filesystem.

## [](#CONFIGURATION)CONFIGURATION

           Refer to pmlogger.control(5) for a description of the contol
           file(s) that are used to control which pmlogger(1) instances and
           which archives are managed by pmlogger_check(1) and
           pmlogger_daily.

           Additionally, when pmproxy(1) archives are being processed,
           environment variables like $PCP_CULLAFTER or $PCP_COMPRESSAFTER
           can be set either for all remote hosts via the file
           $PCP_LOG_DIR/pmproxy/control and/or per-host via files named
           $PCP_LOG_DIR/pmproxy/<hostname>/control.

## [](#FILES)FILES

           $PCP_VAR_DIR/config/pmlogger/config.default
                default pmlogger(1) configuration file location for the local
                primary logger, typically generated automatically by
                pmlogconf(1).

           $PCP_ARCHIVE_DIR/<hostname>
                default location for archives of performance information
                collected from the host hostname

           $PCP_ARCHIVE_DIR/<hostname>/lock
                transient lock file to guarantee mutual exclusion during
                pmlogger(1) administration for the host hostname - if
                present, can be safely removed if neither pmlogger_daily nor
                pmlogger_check(1) are running

           $PCP_ARCHIVE_DIR/<hostname>/Latest
                PCP archive folio created by mkaf(1) for the most recently
                launched archive containing performance metrics from the host
                hostname

           $PCP_LOG_DIR/NOTICES
                PCP ``notices'' file used by pmie(1) and friends

           $PCP_LOG_DIR/pmlogger/pmlogger_daily.log
                if the previous execution of pmlogger_daily produced any
                output it is saved here.  The normal case is no output in
                which case the file does not exist.

           $PCP_ARCHIVE_DIR/SaveLogs
                 if this directory exists, then the log file from the -l
                 argument for pmlogger_daily will be saved in this directory
                 with the name of the format <date>-pmlogger_daily.log.<pid>
                 or <date>-pmlogger_daily-K.log.<pid> This allows the log
                 file to be inspected at a later time, even if several
                 pmlogger_daily executions have been launched in the interim.
                 Because the PCP archive management tools run under the
                 $PCP_USER account ``pcp'', $PCP_ARCHIVE_DIR/SaveLogs
                 typically needs to be owned by the user ``pcp''.

           $PCP_ARCHIVE_DIR/<hostname>/SaveLogs
                  if this directory exists, then the log file from the -l
                  argument of a newly launched pmlogger(1) for hostname will
                  be saved in this directory with the name archive.log where
                  archive is the basename of the associated pmlogger(1) PCP
                  archive files.  This allows the log file to be inspected at
                  a later time, even if several pmlogger(1) instances for
                  hostname have been launched in the interim.  Because the
                  PCP archive management tools run under the uid of the user
                  ``pcp'', $PCP_ARCHIVE_DIR/<hostname>/SaveLogs typically
                  needs to be owned by the user ``pcp''.

           $PCP_LOG_DIR/pmlogger/.NeedRewrite
                   if this file exists, then this is treated as equivalent to
                   using -R on the command line and the file will be removed
                   once all rewriting has been done.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           $PCP_SPACELIMIT
                If set, specifies a maximum allowed total file system space
                (in kilobytes, or with optional K/M/G suffix as for the -d
                option) for each per-host archive directory under
                $PCP_ARCHIVE_DIR or $PCP_REMOTE_ARCHIVE_DIR .  This value is
                used by pmlogger_daily when enforcing archive retention
                limits for file system space, unless the -d option is
                provided in which case the command line flag overrides the
                environment variable and a warning is issued. Enforcement
                occurs after each run of pmlogger_daily and only applies at
                that time—not continuously.

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#COMPATIBILITY_ISSUES)COMPATIBILITY ISSUES

           Earlier versions of pmlogger_daily used find(1) to locate files
           for compressing or culling and the -k and -x options took only
           integer values to mean ``days''.  The semantics of this was quite
           loose given that find(1) offers different precision and semantics
           across platforms.

           The current implementation of pmlogger_daily uses find-filter(1)
           which provides high precision intervals and semantics that are
           relative to the time of execution and are consistent across
           platforms.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), egrep(1), find-filter(1), pmconfig(1), pmlc(1),
           pmlogcompress(1), pmlogconf(1), pmlogctl(1), pmlogextract(1),
           pmlogger(1), pmlogger_check(1), pmlogger_daily_report(1),
           pmlogger_merge(1), pmlogmv(1), pmlogrewrite(1), pmproxy(1),
           systemd(1), xz(1), zstd(1), pmlogger.control(5) and cron(8).

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

    Performance Co-Pilot               PCP                  PMLOGGER_DAILY(1)

------------------------------------------------------------------------

Pages that refer to this page: [find-filter(1)](../man1/find-filter.1.html),  [pcp-atop(1)](../man1/pcp-atop.1.html),  [pcp-atopsar(1)](../man1/pcp-atopsar.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pmlc(1)](../man1/pmlc.1.html),  [pmlogcompress(1)](../man1/pmlogcompress.1.html),  [pmlogctl(1)](../man1/pmlogctl.1.html),  [pmlogdump(1)](../man1/pmlogdump.1.html),  [pmlogextract(1)](../man1/pmlogextract.1.html),  [pmlogger(1)](../man1/pmlogger.1.html),  [pmlogger_check(1)](../man1/pmlogger_check.1.html),  [pmlogger_daily_report(1)](../man1/pmlogger_daily_report.1.html),  [pmlogger_janitor(1)](../man1/pmlogger_janitor.1.html),  [pmlogger_merge(1)](../man1/pmlogger_merge.1.html),  [pmlogger_rewrite(1)](../man1/pmlogger_rewrite.1.html),  [pmloglabel(1)](../man1/pmloglabel.1.html),  [pmsearch(1)](../man1/pmsearch.1.html),  [pmsnap(1)](../man1/pmsnap.1.html),  [pmdiscoversetup(3)](../man3/pmdiscoversetup.3.html),  [LOGARCHIVE(5)](../man5/LOGARCHIVE.5.html),  [pmlogger.control(5)](../man5/pmlogger.control.5.html)

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
