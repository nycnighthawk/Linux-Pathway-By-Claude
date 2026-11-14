---
{"title": "pmnsmerge(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmnsmerge.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmnsmerge(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CAVEATS](#CAVEATS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMNSMERGE(1)             General Commands Manual             PMNSMERGE(1)

## [](#NAME)NAME

           pmnsmerge - merge multiple versions of a Performance Co-Pilot PMNS

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmnsmerge [-adfxv] [-D debug] infile [...]
           outfile

## [](#DESCRIPTION)DESCRIPTION

           pmnsmerge merges multiple instances of a Performance Metrics Name
           Space (PMNS), as used by the components of the Performance Co-
           Pilot (PCP).

           Each infile argument names a file that includes the root of a
           PMNS, of the form

                     root {
                         /* arbitrary stuff */
                     }

           The order in which the infile files are processed is determined by
           the presence or absence of embedded control lines of the form

           #define _DATESTAMP YYYYMMDD

           Files without a control line are processed first and in the order
           they appear on the command line.  The other files are then
           processed in order of ascending _DATESTAMP.

           The -a option suppresses the argument re-ordering and processes
           all files in the order they appear on the command line.

           The merging proceeds by matching names in PMNS, only those new
           names in each PMNS are considered, and these are added after any
           existing metrics with the longest possible matching prefix in
           their names.  For example, merging these two input PMNS

                     root {                    root {
                                                   surprise  1:1:3
                         mine       1:1:1          mine      1:1:1
                         foo                       foo
                                                   yawn
                         yours      1:1:2
                     }                         }
                     foo {                     foo {
                         fumble     1:2:1
                                                   mumble    1:2:3
                         stumble    1:2:2          stumble   1:2:2
                     }                         }
                                               yawn {
                                                   sleepy    1:3:1
                                               }

           Produces the resulting PMNS in out.

                     root {
                         mine      1:1:1
                         foo
                         yours     1:1:2
                         surprise  1:1:3
                         yawn
                     }
                     foo {
                         fumble    1:2:1
                         stumble   1:2:2
                         mumble    1:2:3
                     }
                     yawn {
                         sleepy    1:3:1
                     }

           To avoid accidental over-writing of PMNS files, outfile is
           expected to not exist when pmnsmerge starts.  The -f option allows
           an existing outfile to be unlinked (if possible) and truncated
           before writing starts.

           Normally duplicate names for the same Performance Metric
           Identifier (PMID) in a PMNS are allowed.  The -d option is the
           default option and is included for backwards compatibility.  The
           -x option reverses the default and pmnsmerge will report an error
           and exit with a non-zero status if a duplicate name is found for a
           PMID in any of the input PMNS files or in the merged output PMNS.

           The -v option produces one line of diagnostic output as each
           infile is processed.

           Once all of the merging has been completed, pmnsmerge will attempt
           to load the resultant namespace using pmLoadASCIINameSpace(3) - if
           this fails for any reason, outfile will still be created, but
           pmnsmerge will report the problem and exit with non-zero status.

           Using pmnsmerge with a single input argument allows that PMNS file
           to be checked.  In addition to syntactic checking, specifying -x
           will also enable a check for duplicate names for all PMIDs.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -a   Process files in command line order.

           -d, --dupok
                Allow duplicate metric names per PMID.  This is the default.

           -f, --force
                Overwrite output file if it already exists.

           -v, --verbose
                Verbose input processing.

           -x, --nodups
                Do not allow duplicate metric names per PMID.

           -?, --help
                Display usage message and exit.

## [](#CAVEATS)CAVEATS

           Once the writing of the new outfile file has begun, the signals
           SIGINT, SIGHUP and SIGTERM will be ignored to protect the
           integrity of the new file.

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

           pmnsadd(1), pmnsdel(1), pmLoadASCIINameSpace(3), pcp.conf(5),
           pcp.env(5) and PMNS(5).

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

    Performance Co-Pilot               PCP                       PMNSMERGE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmnsadd(1)](../man1/pmnsadd.1.html),  [pmnscomp(1)](../man1/pmnscomp.1.html),  [pmnsdel(1)](../man1/pmnsdel.1.html)

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
