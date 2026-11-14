---
{"title": "iostat2pcp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/iostat2pcp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iostat2pcp(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CAVEATS](#CAVEATS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOSTAT2PCP(1)            General Commands Manual            IOSTAT2PCP(1)

## [](#NAME)NAME

           iostat2pcp - import iostat data and create a PCP archive

## [](#SYNOPSIS)SYNOPSIS

           iostat2pcp [-v] [-S start] [-t interval] [-V version] [-Z
           timezone] infile outfile

## [](#DESCRIPTION)DESCRIPTION

           iostat2pcp reads a text file created with iostat(1) (infile) and
           translates this into a Performance Co-Pilot (PCP) archive with the
           basename outfile.  If infile is ``-'' then iostat2pcp reads from
           standard input, allowing easy preprocessing of the iostat(1)
           output with sed(1) or similar.

           The resultant PCP archive may be used with all the PCP client
           tools to graph subsets of the data using pmchart(1), perform data
           reduction and reporting, filter with the PCP inference engine
           pmie(1), etc.

           A series of physical files will be created with the prefix
           outfile.  These are outfile.0 (the performance data), outfile.meta
           (the metadata that describes the performance data) and
           outfile.index (a temporal index to improve efficiency of replay
           operations for the archive).  If any of these files exists
           already, then iostat2pcp will not overwrite them and will exit
           with an error message.

           The first output sample from iostat(1) contains a statistical
           summary since boot time and is ignored by iostat2pcp, so the first
           real data set is the second one in the iostat(1) output.

           The best results are obtained when iostat(1) was run with its own
           -t flag, so each output sample is prefixed with a timestamp.  Even
           better is -t with $S_TIME_FORMAT=ISO set in environment when
           iostat(1) is run, in which case the timestamp includes the
           timezone.

           Note that if $S_TIME_FORMAT=ISO is not used with the -t option
           then iostat(1) may produce a timestamp controlled by LC_TIME from
           the locale that is in a format iostat2pcp cannot parse.  The
           formats for the timestamp that iostat2pcp accepts are illustrated
           by these examples:

           2013-07-06T21:34:39+1000
               (for the $S_TIME_FORMAT=ISO).

           2013-07-06 21:34:39
               (for some of the European formats, e.g. de_AT, de_BE, de_LU
               and en_DK.utf8).

           06/07/13 21:34:39
               (for all of the $LC_TIME settings for English locales outside
               North America, e.g. en_AU, en_GB, en_IE, en_NZ, en_SG and
               en_ZA, and all the Spanish locales, e.g. es_ES, es_MX and
               es_AR).

           In particular, note that some common North American $LC_TIME
           settings will not work with iostat2pcp (namely, en_US, POSIX and
           C) because they use the MM/DD format which may be incorrectly
           converted with the assumed DD/MM format.  This is another reason
           to recommend setting $S_TIME_FORMAT=ISO.

           If there are no timestamps in the input stream, iostat2pcp will
           try and deduce the sample interval if basic Disk data (-d option
           for iostat(1)) is found.  If this fails, then the -t option may be
           used to specify the sample interval in seconds.  This option is
           ignored if timestamps are found in the input stream.

           The -S option may be used to specify as start time for the first
           real sample in infile, where start must have the format HH:MM:SS.
           This option is ignored if timestamps are found in the input
           stream.

           The -V option specifies the version for the output PCP archive.
           By default the archive version $PCP_ARCHIVE_VERSION (set to 3 in
           current PCP releases) is used, and the only values currently
           supported for version are 2 or 3.

           The -Z option may be used to specify a timezone.  It must have the
           format +HHMM (for hours and minutes East of UTC) or -HHMM (for
           hours and minutes West of UTC).  Note in particular that neither
           the zoneinfo (aka Olson) format, e.g. Europe/Paris, nor the Posix
           TZ format, e.g.  EST+5 is allowed for the -Z option.  This option
           is ignored if ISO timestamps are found in the input stream.  If
           the timezone is not specified and cannot be deduced, it defaults
           to ``UTC''.

           Some additional diagnostic output is generated with the -v option.

           iostat2pcp is a Perl script that uses the PCP::LogImport Perl
           wrapper around the PCP libpcp_import library, and as such could be
           used as an example to develop new tools to import other types of
           performance data and create PCP archives.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -S start
                Specify the start time for the first sample.

           -t interval
                Specify the sample interval in seconds.

           -v   Print verbose output.

           -Z timezone
                Specify the timezone to use, see above.

## [](#CAVEATS)CAVEATS

           iostat2pcp requires infile to have been created by the version of
           iostat(1) from http://freshmeat.net/projects/sysstat .

           iostat2pcp handles the -c (CPU), -d (Disk), -x (eXtended Disk) and
           -p (Partition) report formats (including their -k, -m, -z and ALL
           variants), but does not accommodate the -n (Network Filesystem)
           report format from iostat(1); this is a demand-driven limitation
           rather than a technical limitation.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           iostat(1), pmchart(1), pmie(1), pmlogger(1), sed(1),
           Date::Format(3pm), Date::Parse(3pm), PCP::LogImport(3pm) and
           LOGIMPORT(3).

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

    Performance Co-Pilot               PCP                      IOSTAT2PCP(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcpcompat(1)](../man1/pcpcompat.1.html),  [pcp-iostat(1)](../man1/pcp-iostat.1.html)

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
