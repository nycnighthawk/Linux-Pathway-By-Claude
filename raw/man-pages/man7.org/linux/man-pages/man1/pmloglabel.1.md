---
{"title": "pmloglabel(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmloglabel.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmloglabel(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [EXIT STATUS](#EXIT_STATUS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGLABEL(1)            General Commands Manual            PMLOGLABEL(1)

## [](#NAME)NAME

           pmloglabel - check and repair a performance metrics archive label

## [](#SYNOPSIS)SYNOPSIS

           pmloglabel [-lLsv?]  [-D debug] [-h hostname] [-p pid] [-V
           version] [-Z timezone] archive

## [](#DESCRIPTION)DESCRIPTION

           pmloglabel verifies, reports on, and can modify all details of the
           labels in each of the files of a Performance Co-Pilot (PCP)
           archive.  The archive has the base name archive and must have been
           previously created using pmlogger(1).

           Each of the files in a PCP archive (metadata, temporal index, and
           one or more data volumes) must contain a valid label at the start,
           else the PCP tools will refuse to open the archive at all.

           Thus, the primary function of pmloglabel is to be able to repair
           any inconsistent or corrupt label fields, such that the entire
           archive is not lost.  It will not check the remainder of the
           archive, but it will give you a fighting chance to recover
           otherwise lost data.  Together, pmloglabel and pmlogextract are
           able to produce a valid PCP archive from many forms of corruption.

           Note that if the temporal index is found to be corrupt, the
           "*.index" file can be safely moved aside and the archive will
           still be accessible, however retrievals may take longer without
           the index.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -h hostname, --host=hostname
                Modify the logged hostname in the archive label, for all
                files in the archive.

           -l, --label
                Dump out the archive label, showing the archive format
                version, the time and date for the start and (current) end of
                the archive, and the host from which the performance metrics
                values were collected.

           -L   Like -l, just a little more verbose, showing also the
                timezone and creator process identifier from the archive
                label.

           -p pid, --pid=pid
                Set the process identifier stored in the archive label to
                pid, for all files in the archive.

           -s   Rewrite the sentinel values which precede and follow the
                archive label, for all files in the archive.

           -v, --verbose
                Verbose mode.  Additional progress information is produced at
                each step.

           -V version, --version=version
                Stamp the version number into the magic number field at the
                start of the archive label, for all files in the archive.

           -Z timezone, --timezone=timezone
                Changes the timezone in the archive labels to timezone in the
                format of the environment variable TZ as described in
                environ(7).

           -?, --help
                Display usage message and exit.

## [](#EXAMPLES)EXAMPLES

           The following demonstrates the use of pmloglabel in finding and
           then correcting a corrupt field (PID) in the label of the temporal
           index of an archive named "20080125".

                     $ pmlogdump -l 20080125
                     pmlogdump: Cannot open archive "20080125": Illegal label record at start of a PCP archive file
                     $ pmloglabel 20080125
                     Mismatched PID (5264/5011) between temporal index and data volume 0
                     $ pmloglabel -p 5264 20080125
                     $ pmlogdump -l 20080125
                     Log Label (Log Format Version 2)
                     Performance metrics from host fw1
                       commencing Fri Jan 25 00:10:09.341 2008
                       ending     Sat Jan 26 00:09:54.344 2008

## [](#EXIT_STATUS)EXIT STATUS

           pmloglabel exits with status 0 if the archive labels are clean.
           If invoked incorrectly, the exit status will be 1.  If corruption
           is detected and still exists at the end, the exit status will be
           2.  If requested to write out the archive labels, and some aspect
           of that write out fails, then the exit status will be 3.

## [](#FILES)FILES

           $PCP_LOG_DIR/pmlogger/<hostname>
                Default directory for PCP archives containing performance
                metric values collected from the host <hostname>.

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

           PCPIntro(1), pmlogcheck(1), pmlogdump(1), pmlogextract(1),
           pmlogger(1), pmlogger_check(1), pmlogger_daily(1),
           pmlogrewrite(1), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                      PMLOGLABEL(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogdump(1)](../man1/pmlogdump.1.html),  [pmlogrewrite(1)](../man1/pmlogrewrite.1.html)

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
