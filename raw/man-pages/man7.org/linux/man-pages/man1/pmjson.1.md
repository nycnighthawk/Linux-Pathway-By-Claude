---
{"title": "pmjson(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmjson.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmjson(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMJSON(1)                General Commands Manual                PMJSON(1)

## [](#NAME)NAME

           pmjson - Performance Co-Pilot JSON dumping utility

## [](#SYNOPSIS)SYNOPSIS

           pmjson [-mnpqyV?]  [-D debug] [-i infile] [-o outfile]

## [](#DESCRIPTION)DESCRIPTION

           pmjson is used to manipulate JSON (JavaScript Object Notation)
           formatted text used in the Performance Co-Pilot (PCP toolkit).  It
           can produce minimal and human readable output formats when it is
           supplied with valid JSON input.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -i infile, --in=infile
                JSON formatted input infile - path to a file from which input
                should be read.  If this option is omitted, then pmjson will
                read from the standard input stream.

           -m, --minimal
                Produce JSON output with all superfluous whitespace removed
                from the resulting JSON string.

           -o outfile, --out=outfile
                Formatted output is written to the named outfile.  If this
                option is omitted, then pmjson will write to the standard
                output stream.

           -n, --not-pretty
                Produce JSON output in raw, monochromatic format (default if
                output is being sent to a file).

           -p, --pretty
                Produce JSON output in a human-friendly format (default if
                output is on a terminal).

           -q, --quiet
                Verify the input as valid JSON only, no output is produced.

           -V, --version
                Display version number and exit.

           -y, --yaml
                Produce YAML-like output, a human-readable format with less
                syntactic sugar than JSON.

           -?, --help
                Display usage message and exit.

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

           PMWEBAPI(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                          PMJSON(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmwebapi(3)](../man3/pmwebapi.3.html)

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
