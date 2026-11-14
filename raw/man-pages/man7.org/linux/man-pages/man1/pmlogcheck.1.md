---
{"title": "pmlogcheck(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogcheck.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogcheck(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERATION](#OPERATION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGCHECK(1)            General Commands Manual            PMLOGCHECK(1)

## [](#NAME)NAME

           pmlogcheck - checks for invalid data in a PCP archive

## [](#SYNOPSIS)SYNOPSIS

           pmlogcheck [-flmRrvwz?]  [-D debug] [-n pmnsfile] [-S start] [-T
           finish] [-Z timezone] archive ...

## [](#DESCRIPTION)DESCRIPTION

           pmlogcheck prints information about the nature of any invalid data
           which it detects in the files of PCP archives.  For some limited
           cases it also provides a ``repair'' facility.

           Each archive has the base name archive and must have been
           previously created using pmlogger(1).  Alternatively, archive can
           be the name of a physical file that forms part of a PCP archive.

           When multiple archive options are present, all of the
           corresponding PCP archives will be checked, however if the archive
           options are file names, then each associated PCP archive will be
           checked at most once.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -f, --full
                Under normal operation, most errors in Pass 0 (see below) are
                sufficiently serious that pmlogcheck will exit this happens.
                The -f option forces pmlogcheck to keep going, even if
                serious errors are found.

           -l, --label
                Print the archive label, showing the archive format version,
                the time and date for the start and (current) end of the
                archive, and the host from which the performance metrics
                values were collected.

           -m, --metadataonly
                Skip Pass 3 (see below) and only check the archive meta data.
                This can run substantially faster in cases where the volume
                data doesn't need to be checked, especially on archives with
                compressed data volume(s).

           -n pmnsfile, --namespace=pmnsfile
                Load an alternative Performance Metrics Name Space (PMNS(5))
                from the file pmnsfile.

           -R, --auto-repair
                Try to repair any structural damage and in particular when
                files are incomplete (usually as a result of a system crash
                or filesystem out of space conditions), truncate them to
                preserve as much complete information as possible.
                Truncation will only work for uncompressed files, so any
                archive with compressed file components will need to be
                uncompressed first with pmlogdecompress(1).

                Any repair option implies -f.

                Some problems detected by pmlogcheck are not best resolved by
                file truncation (e.g. pmlogrewrite(1) may be a better
                option), so it is recommended that pmlogcheck is first run
                without -R to determine the scope of any issues, or repair
                interactively with -r.

           -r, --repair
                Same repair functions as -R but the -r option requires
                pmlogcheck to be run interactively and it will prompt the
                user and demand a positive response before any file is
                truncated.

           -S starttime, --start=starttime
                Specify the starttime of time window over which metrics
                should be checked in Pass 3 (see below).  Refer to
                PCPIntro(1) for a complete description of the syntax for
                starttime.

           -T endtime, --finish=endtime
                Specify the endtime of time window over which metrics should
                be checked in Pass 3 (see below).  Refer to PCPIntro(1) for a
                complete description of the syntax for endtime.

           -v, --verbose
                Enable verbose mode.

           -w, --nowrap
                Suppress reporting of counter wraps.

           -z, --hostzone
                Use the local timezone of the host that is the source of the
                performance metrics archive.  The default is to use the
                timezone of the local host.

           -Z timezone, --timezone=timezone
                Use timezone for the date and time.  Timezone is in the
                format of the environment variable TZ as described in
                environ(7).  The default is to use the timezone of the local
                host.

           -?, --help
                Display usage message and exit.

## [](#OPERATION)OPERATION

           The checking proceeds in a number of passes, each designed to
           validate progressively more complex semantic relationships between
           the information in a PCP archive.

       Pass 0
           Each physical file of the PCP archive is processed to ensure the
           label records are valid and consistent, and that each file
           contains an integral number of physical records with correct
           header and trailer fields.

           Any errors at this stage are usually fatal.  The PCP archive is
           probably damaged beyond repair, and no more passes of pmlogcheck
           are attempted.

       Pass 1
           Validates the integrity of the temporal index, usually
           archive.index.

           As the temporal index is (strictly speaking) optional, errors at
           this stage are handled by marking the index as bad and ignoring it
           for the remainder of the pmlogcheck passes.

           Permanent repair can be achieved by removing the temporal index
           file and then making a copy of the PCP archive using
           pmlogrewrite(1) or pmlogextract(1).  This will create a new
           temporal index for the copied archive as a side-effect.

       Pass 2
           Validates the integrity of the metadata file, usually
           archive.meta.

       Pass 3
           Validates the integrity of each of the volumes of the PCP archive,
           usually archive.0, archive.1, etc.

           There is some basic integrity checks to ensure the encoding of
           values for each metric remains consistent and the values are well
           formed across all the observations in the archive.

           Also the timestamps for the observations are expected to be
           monotonically increasing as the archive is traversed.

           Additional attention is given to counter metrics (type from
           pmLookupDesc(3) is PM_SEM_COUNTER) which are expected to have
           monotonically increasing values.  If the values are not monotonic
           increasing this may suggest a counter wrap has happened or there
           has been some interruption or reset to the underlying source of
           the performance data that is no captured in the archive.

           For each counter metric which has been detected as having wrapped
           at some point in the archive, pmlogcheck produces output
           describing the metric name (with instance identifiers where
           appropriate), the internal storage type for the metric, the value
           of the metric before the counter wrap (with its associated
           timestamp), and the value of the metric after the wrap (also with
           a timestamp).

           The -w option may be used to suppress reporting of counter wraps.

           pmlogcheck produces two different timestamp formats, depending on
           the interval over which it is run.  For an interval greater than
           24 hours, the date is displayed in addition to the time at which
           the counter wrap occurred.  If the extent of the data being
           checked is less than 24 hours, a more precise format is used (time
           is displayed with millisecond precision, but without the date).

## [](#EXAMPLES)EXAMPLES

           The following are all equivalent:

                $ pmlogcheck myarchive
                $ pmlogcheck myarchive.0
                $ pmlogcheck myarchive.meta
                $ pmlogcheck myarchive.0 myarchive.meta

           If the current directory contains multiple PCP archives, then the
           command

                $ pmlogcheck *.meta*

           will check them all, as there is one .meta file for each PCP
           archive, but this file may have been compressed (hence the
           trailing *).

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/*
                default PMNS specification files

           $PCP_LOG_DIR/pmlogger/<hostname>
                default directory for PCP archives containing performance
                data collected from the host hostname.

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

           Debugging options specific to pmlogcheck are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ dump each pmResult processed                          │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl1  │ report each time a new metric-instance pair is seen   │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl2  │ report counter values as part of wrap detection       │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl3  │ report elapsed and cpu time for each pass             │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmlogdecompress(1), pmlogdump(1), pmlogextract(1),
           pmlogger(1), pmlogrewrite(1), pmlogsummary(1), PMAPI(3),
           pmLookupDesc(3), PMNS(5), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                      PMLOGCHECK(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogdump(1)](../man1/pmlogdump.1.html),  [pmloglabel(1)](../man1/pmloglabel.1.html),  [pmlogsize(1)](../man1/pmlogsize.1.html),  [pmisetvolumesize(3)](../man3/pmisetvolumesize.3.html)

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
