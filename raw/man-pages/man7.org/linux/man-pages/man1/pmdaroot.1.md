---
{"title": "pmdaroot(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdaroot.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdaroot(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAROOT(1)              General Commands Manual              PMDAROOT(1)

## [](#NAME)NAME

           pmdaroot - a privileged PMCD helper performance metrics domain
           agent

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/root/pmdaroot [-D debug] [-d domain] [-l logfile]
           [-s sockname]

## [](#DESCRIPTION)DESCRIPTION

           pmdaroot is a special Performance Metrics Domain Agent (PMDA)
           which cooperates closely with pmcd(1) and other PMDAs to provide
           limited privileged services to these unprivileged processes.

           In this role it is used to discover operating system containers
           running on the local host.  It also enables access to performance
           data from within those containers by other PMDAs running on the
           bare-metal host, using the pmdaRootConnect(3) and the associated
           namespace interfaces.

           Like all other PMDAs, it also exports performance metrics from the
           domain it controls.  Currently, this is limited to information
           about the containers on the local system; currently Docker and LXC
           containers can be detected.

           If a non-default Docker parent-cgroup name is being used, this
           value can be indicated to pmdaroot through addition of a
           $PCP_SYSTEMD_CGROUP variable in /etc/pcp.conf.

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                root.log is written in the current directory of pmcd(1) when
                pmdaroot is started, i.e.  $PCP_LOG_DIR/pmcd.  If the log
                file cannot be created or is not writable, output is written
                to the standard error instead.

           -s   Location of the unix(7) domain socket for communication with
                clients seeking privileged operations.  By default, a socket
                file named $PCP_TMP_DIR/pmcd/root.socket is used.

## [](#INSTALLATION)INSTALLATION

           Access to the names, help text and values for the kernel
           performance metrics is available by default - unlike most other
           agents, no action is required to enable them and they should not
           be removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/root/help
                  default help text file for metrics exported by the root
                  PMDA.
           $PCP_LOG_DIR/pmcd/root.log
                  default log file for error messages and other information
                  from the root PMDA.
           $PCP_VAR_DIR/pmcd/root.socket
                  default socket file for communication with root PMDA
                  clients.

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

           Debugging options specific to pmdaroot are as follows:
           ┌────────┬───────────────────────────┐
           │ Option │ Description               │
           ├────────┼───────────────────────────┤
           │ appl0  │ interactions with pmcd(1) │
           ├────────┼───────────────────────────┤
           │ appl1  │ PMDA startup processing   │
           └────────┴───────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), PMDA(3), pmdaRootConnect(3), pcp.conf(5) and
           unix(7).

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

    Performance Co-Pilot               PCP                        PMDAROOT(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdarootconnect(3)](../man3/pmdarootconnect.3.html)

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
