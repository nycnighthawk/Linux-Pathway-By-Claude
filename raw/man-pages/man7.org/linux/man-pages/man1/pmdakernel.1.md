---
{"title": "pmdakernel(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdakernel.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdakernel(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SYNOPSIS](#SYNOPSIS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KERNEL_PMDAS(1)          General Commands Manual          KERNEL_PMDAS(1)

## [](#NAME)NAME

           pmdaaix, pmdadarwin, pmdafreebsd, pmdalinux, pmdanetbsd,
           pmdaopenbsd, pmdasolaris, pmdawindows - operating system kernel
           performance metrics domain agents

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/aix/pmdaaix [-D debug] [-d domain] [-l logfile] [-U
           username]
           $PCP_PMDAS_DIR/darwin/pmdadarwin [-D debug] [-d domain] [-l
           logfile] [-U username]
           $PCP_PMDAS_DIR/freebsd/pmdafreebsd [-D debug] [-d domain] [-l
           logfile] [-U username]
           $PCP_PMDAS_DIR/linux/pmdalinux [-A] [-D debug] [-d domain] [-l
           logfile] [-U username]
           $PCP_PMDAS_DIR/netbsd/pmdanetbsd [-D debug] [-d domain] [-l
           logfile] [-U username]
           $PCP_PMDAS_DIR/netbsd/pmdaopenbsd [-D debug] [-d domain] [-l
           logfile] [-U username]
           $PCP_PMDAS_DIR/solaris/pmdasolaris [-D debug] [-d domain] [-l
           logfile] [-U username]
           $PCP_PMDAS_DIR/windows/pmdawindows [-D debug] [-d domain] [-l
           logfile] [-U username]

## [](#DESCRIPTION)DESCRIPTION

           Each supported platform has a kernel Performance Metrics Domain
           Agent (PMDA) which extracts performance metrics from the kernel of
           that platfrom.  A variety of platform-specific metrics are
           available, with an equally varied set of access mechanisms -
           typically this involves special system calls, or reading from
           files in kernel virtual filesystems such as the Linux sysfs and
           procfs filesystems.

           The platform kernel PMDA is one of the most critical components of
           the PCP installation, and must be as efficient and reliable as
           possible.  In all installations the default kernel PMDA will be
           installed as a shared library and thus executes directly within
           the pmcd(1) process.  This slightly reduces overheads associated
           with querying the metadata and values associated with these
           metrics (no message passing is required).

           Unlike many other PMDAs, the kernel PMDA exports a number of
           metric namespace subtrees, such as kernel, network, swap, mem,
           ipc, filesys, nfs, disk and hinv (hardware inventory).

           Despite usually running as shared libraries, most installations
           also include a stand-alone executable for the kernel PMDA.  This
           is to aid profiling and debugging activities, with dbpmda(1) for
           example.  In this case (but not for shared libraries), the
           following command line options are available:

           -A   Disables use of the credentials provided by PMAPI client
                tools, and simply runs everything under the "root" account.
                Only enable this option if you understand the risks involved,
                and are sure that all remote accesses will be from benevolent
                users.  If enabled, unauthenticated remote PMAPI clients will
                be able to access potentially sensitive performance metric
                values which an unauthenticated PMAPI client usually would
                not be able to.  Refer to CVE-2012-3419 for additional
                details.

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                [platform].log is written in the current directory of pmcd(1)
                when pmda[platform] is started, i.e.  $PCP_LOG_DIR/pmcd.  If
                the log file cannot be created or is not writable, output is
                written to the standard error instead.

           -U   User account under which to run the agent.  The default is
                either the privileged "root" account on some platforms
                (Linux, for example) or the unprivileged "pcp" account
                (wherever possible).

## [](#INSTALLATION)INSTALLATION

           Access to the names, help text and values for the kernel
           performance metrics is available by default - unlike most other
           agents, no action is required to enable them and they should not
           be removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/[platform]/help
                  default help text file for the the kernel metrics
           $PCP_LOG_DIR/pmcd/[platform].log
                  default log file for error messages and other information
                  from the kernel PMDA.

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

           Debugging options specific to pmdaaix, pmdafreebsd, pmdanetbsd,
           pmdaopenbsd and pmdasolaris are as follows:
           ┌────────┬─────────────────────┐
           │ Option │ Description         │
           ├────────┼─────────────────────┤
           │ appl0  │ verbose diagnostics │
           └────────┴─────────────────────┘

           Debugging options specific to pmdalinux are as follows:
           ┌────────┬──────────────────────┐
           │ Option │ Description          │
           ├────────┼──────────────────────┤
           │ appl1  │ disk-related metrics │
           ├────────┼──────────────────────┤
           │ appl8  │ filesys metrics      │
           └────────┴──────────────────────┘

## [](#SYNOPSIS)SYNOPSIS

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), dbpmda(1), pmcd(1), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                    KERNEL_PMDAS(1)

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
