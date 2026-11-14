---
{"title": "pmdajbd2(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdajbd2.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdajbd2(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAJBD2(1)              General Commands Manual              PMDAJBD2(1)

## [](#NAME)NAME

           pmdajbd2 - journal block device (JBD) performance metrics domain
           agent (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/jbd2/pmdajbd2 [-D debug] [-d domain] [-l logfile]
           [-j path] [-U username]

## [](#DESCRIPTION)DESCRIPTION

           pmdajbd2 is a Performance Metrics Domain Agent (PMDA) which
           extracts performance metrics from the Journal Block Device
           subsystem (version 2) in the Linux kernel.  These metrics are
           exported by the kernel in procfs files, one file per block device.
           The JBD2 subsystem is used by several filesystems including ext3,
           ext4 and ocfs2.

           The jbd2 PMDA exports metrics that measure detailed journal
           transaction information, such as time spent waiting and locked,
           request rates, blocks used and so on.

           A brief description of the pmdajbd2 command line options follows
           (these are only relevant when running the PMDA as a daemon, and
           not as a shared library):

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, when running as a
                daemon a log file named jbd2.log is written in the current
                directory of when pmdajbd2 is started, i.e.
                $PCP_LOG_DIR/pmcd.  If the log file cannot be created or is
                not writable, output is written to the standard error
                instead.  When running in shared library mode, and diagnostic
                information will be written into the pmcd log file, namely
                $PCP_LOG_DIR/pmcd/pmcd.log.

           -j   Allows an alternate path to the jbd2 statistics files to be
                specified.  The default path is /proc/fs/jbd2.

           -U   User account under which to run the agent.  The default is
                the unprivileged "pcp" account in current versions of PCP,
                but in older versions the superuser account ("root") was used
                by default.

## [](#INSTALLATION)INSTALLATION

           This PMDA is installed by default and in the shared library mode
           (rather than as a separate daemon to pmcd(1)).  Thus, the names,
           help text and values for the jbd2 performance metrics should
           always be available.

           If you do not use these metrics you can remove this PMDA, do the
           following as root:

                # cd $PCP_PMDAS_DIR/jbd2
                # ./Remove

           If you want to enable the installation again, do the following as
           root:

                # cd $PCP_PMDAS_DIR/jbd2
                # ./Install

           pmdajbd2 is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdajbd2
           $PCP_PMDAS_DIR/jbd2/help
                  default help text file for the jbd2 metrics
           $PCP_PMDAS_DIR/jbd2/Install
                  installation script for the pmdajbd2 agent
           $PCP_PMDAS_DIR/jbd2/Remove
                  undo installation script for the pmdajbd2 agent
           $PCP_LOG_DIR/pmcd/jbd2.log
                  default log file for error messages and other information
                  from pmdajbd2

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

           PCPIntro(1), pmcd(1), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                        PMDAJBD2(1)

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
