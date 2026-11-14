---
{"title": "pcp-verify(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-verify.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-verify(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-VERIFY(1)            General Commands Manual            PCP-VERIFY(1)

## [](#NAME)NAME

           pcp-verify - verify aspects of a PCP installation

## [](#SYNOPSIS)SYNOPSIS

           pcp verify [-a archive] [-D debug] [-h host] [-csvV?]

## [](#DESCRIPTION)DESCRIPTION

           pcp-verify inspects various aspects of a PCP collector
           installation and reports on whether it is configured correctly for
           certain modes of operation.

           By default, pcp-verify checks that PMCD is running and no agents
           are in a failed state.  These checks can be extended and refined
           using the command line options.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -a archive, --archive=archive
                Use the archive for verification.

           -c, --containers
                Verify the collector installation for monitoring containers.

           -h host, --host=host
                Connect to the PMCD on host for verification.

           -s, --secure
                Verify that the required components for encrypted
                communication are in place.

           -v, --verbose
                Increase the verbosity, and report on each check as it is
                made.  In the absence of any issues found, pcp-verify
                operates silently.

           -V, --version
                Display version number and exit.

           -?, --help
                Display usage message and exit.

## [](#DIAGNOSTICS)DIAGNOSTICS

           pcp-verify will exit with a non-zero status if it finds anything
           worth reporting, otherwise it is silent and returns zero.

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

           PCPIntro(1) and pcp(1).

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

    Performance Co-Pilot               PCP                      PCP-VERIFY(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp(1)](../man1/pcp.1.html)

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
