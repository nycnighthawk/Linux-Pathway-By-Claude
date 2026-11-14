---
{"title": "pmlogpush(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogpush.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogpush(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                     |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGPUSH(1)             General Commands Manual             PMLOGPUSH(1)

## [](#NAME)NAME

           pmlogpush - push an archive to a remote pmproxy server

## [](#SYNOPSIS)SYNOPSIS

           pmlogpush [-vV?]  [-D debug] [-h host] [-p port] [-s unix] [-Z
           timezone] archive

## [](#DESCRIPTION)DESCRIPTION

           pmlogpush sends the contents of a Performance Co-Pilot (PCP)
           archive to a HTTP server (typically to a remote pmproxy(1) daemon)
           using the logger API subset within the PMWEBAPI(5).  The archive
           must have been previously created using pmlogger(1).

           This archive should be complete and finished (not actively being
           written to).  Comparable functionality is available directly from
           pmlogger via the HTTP-prefixed archive name syntax, which pushes
           archives remotely while they are actively being written.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -h hostname, --host=hostname
                The hostname for the remote pmproxy server to receive the
                given PCP archive.

           -p port, --port=port
                Internet socket port number where the remote pmproxy server
                is listening, waiting to receive the given PCP archive.  The
                default port is 44322.

           -s path, --unix=path
                Unix domain socket path where a local pmproxy server is
                listening (locally), waiting to receive the given PCP
                archive.

           -v, --verbose
                Increase the diagnostic information reported as pmlogpush
                runs.

           -?, --help
                Display usage message and exit.

           -V, --version
                Display version number and exit.

## [](#FILES)FILES

           $PCP_LOG_DIR/pmproxy/<hostname>
                Default directory for pushed PCP archives created (remotely)
                by the receving pmproxy server.  The hostname is extracted
                from the given archive, as is the recording start time -
                together these properties are used to name the pushed archive
                on the receiving end (i.e. by the pmproxy server).

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
           their meaning.  The http debugging option is of particular
           interest for this utility.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmlogger(1), pmproxy(1), PMWEBAPI(3), pcp.conf(5) and
           pcp.env(5).

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

    Performance Co-Pilot               PCP                       PMLOGPUSH(1)

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
