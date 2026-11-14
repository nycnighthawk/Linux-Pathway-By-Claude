---
{"title": "pmtime(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmtime.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmtime(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMTIME(1)                General Commands Manual                PMTIME(1)

## [](#NAME)NAME

           pmtime - time control server for Performance Co-Pilot

## [](#SYNOPSIS)SYNOPSIS

           pmtime [-D debug] [-V?]  [-p port]

## [](#DESCRIPTION)DESCRIPTION

           pmtime is a graphical user interface for performance monitoring
           applications using the PCP infrastructure and requiring
           interactive time control.

           pmtime is not normally invoked directly by users.  Rather, it is
           more typical for it to be started by client applications (e.g.
           pmchart(1), pmstat(1) or pmval(1)).

           There are two modes of interacting with a pmtime process - live
           host mode, and historical archive mode.  In archive mode the
           window presents time controls suitable for manipulating the
           archive position, allowing full VCR control to move forwards and
           backwards in time at configurable rates and intervals.  In live
           mode the pmtime window contains the simpler time controls suitable
           for live monitoring.

           Note that the pmtime window is only made visible when explicitly
           requested.  Multiple client applications can be connected to a
           single pmtime server - when the final client application exits,
           pmtime will also exit.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -p port, --guiport=port
                port is the port number which pmtime will use for
                communication with its clients (monitoring applications).

           -V, --version
                Display version number and exit.

           -?, --help
                Display usage message and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           When a port number is not explicitly requested on the command line
           via the -p option, the environment variable PMTIME_PORT can be set
           to specify the port number from which available-port probing will
           commence when pmtime is searching for a port number to use.

           The default starting port number is 43334.

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmtime are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ enable internal diagnostics that report all pmtime    │
           │        │ events, e.g. setting timezone, state changes,         │
           │        │ interval changes, timescale changes, etc.             │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmchart(1), pmstat(1) and pmval(1).

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

    Performance Co-Pilot                                            PMTIME(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcpcompat(1)](../man1/pcpcompat.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pmchart(1)](../man1/pmchart.1.html),  [pmstat(1)](../man1/pmstat.1.html),  [pmval(1)](../man1/pmval.1.html),  [pmview(1)](../man1/pmview.1.html),  [pcpintro(3)](../man3/pcpintro.3.html),  [pmgetoptions(3)](../man3/pmgetoptions.3.html),  [pmtime(3)](../man3/pmtime.3.html),  [pmview(5)](../man5/pmview.5.html)

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
