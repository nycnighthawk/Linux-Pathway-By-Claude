---
{"title": "newhelp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/newhelp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# newhelp(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                     |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NEWHELP(1)               General Commands Manual               NEWHELP(1)

## [](#NAME)NAME

           newhelp - generate a performance metrics help database

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/newhelp [-vV?]  [-D debug] [-n pmnsfile] [-o
           outputfile] [file ...]

## [](#DESCRIPTION)DESCRIPTION

           newhelp generates the Performance Co-Pilot help text files used by
           Performance Metric Domain Agents (PMDAs).

           Normally newhelp operates on the default Performance Metrics Name
           Space (PMNS), however if the -n option is specified an alternative
           namespace is loaded from the file pmnsfile.

           When there is only one input file, the base name of the new
           database is derived from the name of the input file, otherwise the
           -o flag must be given to explicitly name the database.  If no
           input files are supplied, newhelp reads from the standard input
           stream, in which case the -o flag must be given.

           If the output file name is determined to be foo, newhelp will
           create foo.dir and foo.pag.

           The -V flag causes verbose messages to be printed while newhelp is
           parsing its input.

           The first line of each entry in a help source file consists of an
           ``@'' character beginning the line followed by a space and then
           the performance metric name and a one line description of the
           metric.  Following lines (up to the next line beginning with ``@''
           or end of file) may contain a verbose help description.  E.g.

                #
                # This is an example of newhelp's input syntax
                #
                @ kernel.all.cpu.idle CPU idle time
                A cumulative count of the number of milliseconds
                of CPU idle time, summed over all processors.

           Three-part numeric metric identifiers (PMIDs) may be used in place
           of metric names, e.g. 60.0.23 rather than kernel.all.cpu.idle in
           the example above.  Other than for dynamic metrics (where the
           existence of a metric is known to a PMDA, but not visible in the
           PMNS and hence has no name that could be known to newhelp) use of
           this syntactic variant is not encouraged.

           Lines beginning with ``#'' are ignored, as are blank lines in the
           file before the first ``@''.  The verbose help text is optional.

           As a special case, a ``metric'' name of the form NNN.MM (for
           numeric NNN and MM) is interpreted as an instance domain
           identification, and the text describes the instance domain.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -o output, --output=outout
                Specify base name for output files.

           -n pmnsfile, --namespace=pmnsfile
                Load an alternative Performance Metrics Name Space (PMNS(5))
                from the file pmnsfile.

           -v version, --version=version
                Set output version.  This options is deprecated, the only
                supported value is 2.

           -V, --verbose
                Print verbose output.

           -?, --help
                Display usage message and exit.

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/*
                default PMNS specification files

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           chkhelp(1), PMAPI(3), pmLookupInDomText(3), pmLookupText(3),
           pcp.conf(5), pcp.env(5) and PMNS(5).

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

    Performance Co-Pilot               PCP                         NEWHELP(1)

------------------------------------------------------------------------

Pages that refer to this page: [chkhelp(1)](../man1/chkhelp.1.html),  [pmda(3)](../man3/pmda.3.html),  [pmdahelp(3)](../man3/pmdahelp.3.html),  [pmdainit(3)](../man3/pmdainit.3.html),  [pmdatext(3)](../man3/pmdatext.3.html),  [pmlookupindomtext(3)](../man3/pmlookupindomtext.3.html),  [pmlookuptext(3)](../man3/pmlookuptext.3.html)

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
