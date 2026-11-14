---
{"title": "pmnsdel(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmnsdel.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmnsdel(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CAVEATS](#CAVEATS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMNSDEL(1)               General Commands Manual               PMNSDEL(1)

## [](#NAME)NAME

           pmnsdel - delete a subtree of names from the Performance Co-Pilot
           PMNS

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmnsdel [-?]  [-D debug] [-n namespace] metricpath
           [...]

## [](#DESCRIPTION)DESCRIPTION

           pmnsdel removes subtrees of names from a Performance Metrics Name
           Space (PMNS), as used by the components of the Performance Co-
           Pilot (PCP).

           Normally pmnsdel operates on the default Performance Metrics Name
           Space (PMNS), however if the -n option is specified an alternative
           namespace is used from the file namespace.

           The default PMNS is found in the file $PCP_VAR_DIR/pmns/root
           unless the environment variable PMNS_DEFAULT is set, in which case
           the value is assumed to be the pathname to the file containing the
           default PMNS.

           The metric names to be deleted are all those for which one of the
           metricpath arguments is a prefix in the PMNS, see PMNS(5).

           All of the files defining the PMNS must be located within the
           directory that contains the root of the PMNS, and this would
           typically be $PCP_VAR_DIR/pmns for the default PMNS, and this
           would typically imply running pmnsdel as root.

           Provided some initial integrity checks are satisfied, pmnsdel will
           update the necessary PMNS files.  Should an error be encountered
           the original namespace is restored.  Note that any PMNS files that
           are no longer referenced by the modified namespace will not be
           removed, even though their contents are not part of the new
           namespace.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -n pmnsfile, --namespace=pmnsfile
                Load an alternative Performance Metrics Name Space (PMNS(5))
                from the file pmnsfile.

           -?, --help
                Display usage message and exit.

## [](#CAVEATS)CAVEATS

           Once the writing of the new namespace file has begun, the signals
           SIGINT, SIGHUP and SIGTERM will be ignored to protect the
           integrity of the new files.

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/root
                the default PMNS, when the environment variable PMNS_DEFAULT
                is unset

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

           pmnsadd(1), pmnsmerge(1), pcp.conf(5), pcp.env(5) and PMNS(5).

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

    Performance Co-Pilot               PCP                         PMNSDEL(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmnsadd(1)](../man1/pmnsadd.1.html),  [pmnscomp(1)](../man1/pmnscomp.1.html),  [pmnsmerge(1)](../man1/pmnsmerge.1.html),  [pmda(3)](../man3/pmda.3.html)

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
