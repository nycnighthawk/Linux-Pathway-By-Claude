---
{"title": "pmdammv(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdammv.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdammv(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAMMV(1)               General Commands Manual               PMDAMMV(1)

## [](#NAME)NAME

           pmdammv - memory mapped values performance metrics domain agent
           (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/mmv/pmdammv [-D debug] [-d domain] [-l logfile] [-U
           username]

## [](#DESCRIPTION)DESCRIPTION

           pmdammv is a Performance Metrics Domain Agent (PMDA) which exports
           application level performance metrics using memory mapped files.
           It offers an extremely low overhead instrumentation facility that
           is well-suited to long running, mission critical applications
           where it is desirable to have performance metrics and availability
           information permanently enabled.

           The mmv PMDA exports instrumentation that has been added to an
           application using the MMV APIs (refer to mmv_stats_init(3) and
           mmv(5) for further details).  These APIs can be called from
           several languages, including C, C++, Perl, Python, Java (via the
           separate ``Parfait'' class library) and GoLang (via the separate
           ``Speed'' library).

           A brief description of the pmdammv command line options follows:

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                mmv.log is written in the current directory of pmcd(1) when
                pmdammv is started, i.e.  $PCP_LOG_DIR/pmcd.  If the log file
                cannot be created or is not writable, output is written to
                the standard error instead.

           -U   User account under which to run the agent.  The default is
                the unprivileged "pcp" account in current versions of PCP,
                but in older versions the superuser account ("root") was used
                by default.

## [](#INSTALLATION)INSTALLATION

           Firstly, a security model for interprocess communication between
           instrumented applications and pmdammv (running as a shared library
           inside pmcd) must be chosen and established.

           This communication occurs through memory mapped files in a
           location known to both pmdammv and the instrumented applications.
           That location is $PCP_TMP_DIR/mmv, although that is often hidden
           behind application APIs such as ``Parfait'' and mmv_stats_init(3).
           The permissions set on this directory indicate the security model
           in use.

           The more secure method is to use an existing unprivileged group
           which is shared by instrumented applications, pmcd and pmdammv
           such as the "pcp" group.

                # . /etc/pcp.env
                # mkdir -m 775 $PCP_TMP_DIR/mmv
                # chgrp pcp $PCP_TMP_DIR/mmv

           Since this method requires instrumented applications to use this
           non-default group (see newgrp(1) and setgid(2)) a common
           alternative involves the use of a world-writable $PCP_TMP_DIR/mmv
           directory with the sticky-bit set (similar to /tmp and /var/tmp,
           for example).

           This allows any application, running under any user account, to
           communicate with the PMDA (which runs under the "pcp" account by
           default).  This may not be desirable for all environments and one
           should consider the security implications of any directory setup
           like this (similar classes of issues exist as those that affect
           the system temporary file directories).

           pmdammv is enabled by default on all modern PCP installations, and
           thus the names, help text and values for the mmv performance
           metrics are available without the usual PMDA ./Install process.

           If the $PCP_TMP_DIR/mmv directory does not exist, then the
           ./Install script can be used to create a world-writable sticky-
           bit-set directory for communication.  This is for backwards
           compatibility, as well as ease of use - to use this mechanism, do
           the following as root:

                # rmdir $PCP_TMP_DIR/mmv
                # cd $PCP_PMDAS_DIR/mmv
                # ./Install

           This installation process will not overwrite any existing
           $PCP_TMP_DIR/mmv directory.

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/mmv
                # ./Remove

           pmdammv is launched by pmcd and should never be executed directly.
           The Install and Remove scripts notify pmcd when the agent is
           installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdammv
           $PCP_TMP_DIR/mmv
                  directory housing memory mapped value files
           $PCP_PMDAS_DIR/mmv/help
                  default help text file for the mmv metrics
           $PCP_PMDAS_DIR/mmv/Install
                  installation script for the pmdammv agent
           $PCP_PMDAS_DIR/mmv/Remove
                  undo installation script for the pmdammv agent
           $PCP_LOG_DIR/pmcd/mmv.log
                  default log file for error messages and other information
                  from pmdammv

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

           Debugging options specific to pmdammv are as follows:
           ┌────────┬─────────────────────┐
           │ Option │ Description         │
           ├────────┼─────────────────────┤
           │ appl0  │ verbose diagnostics │
           └────────┴─────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), newgrp(1), setgid(2), mmv_stats_init(3),
           mmv(5), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                         PMDAMMV(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogger(1)](../man1/pmlogger.1.html),  [mmv(5)](../man5/mmv.5.html)

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
