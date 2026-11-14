---
{"title": "pmdabtrfs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdabtrfs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdabtrfs(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDABTRFS(1)             General Commands Manual             PMDABTRFS(1)

## [](#NAME)NAME

           pmdabtrfs - btrfs filesystem performance metrics domain agent
           (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/btrfs/pmdabtrfs [-D debug] [-d domain] [-l logfile]

## [](#DESCRIPTION)DESCRIPTION

           pmdabtrfs is a Performance Metrics Domain Agent (PMDA) which
           extracts performance metrics from the btrfs filesystem via sysfs
           (/sys/fs/btrfs).

           The btrfs PMDA exports metrics covering filesystem information
           (label, sizes, generation, checksum algorithm), transaction commit
           statistics, space allocation for data, metadata and system block
           groups, per-device error statistics, and async discard statistics.

           Metrics are organized into two instance domains: one for btrfs
           filesystems (keyed by UUID) and one for devices (keyed by
           UUID::devid).  Labels are provided for each instance, including
           the filesystem UUID, label, and device ID where applicable.

           A brief description of the pmdabtrfs command line options follows:

           -d   The performance metrics domain number must be set to a unique
                value.

           -l   Location of the log file.  By default, a log file named
                btrfs.log is written in the current directory of pmcd(1) when
                pmdabtrfs is started, i.e.  $PCP_LOG_DIR/pmcd.  If the log
                file cannot be created or is not writable, output is written
                to the standard error instead.

## [](#INSTALLATION)INSTALLATION

           The btrfs PMDA requires a Linux system with one or more mounted
           btrfs filesystems.  The PMDA reads statistics from sysfs and does
           not require root privileges.

           Install the PMDA using the Install script:

                # cd $PCP_PMDAS_DIR/btrfs
                # ./Install

           To remove the PMDA use the Remove script:

                # cd $PCP_PMDAS_DIR/btrfs
                # ./Remove

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmdabtrfs are as follows:
           ┌────────┬───────────────────────────────────────────────────┐
           │ Option │ Description                                       │
           ├────────┼───────────────────────────────────────────────────┤
           │ appl0  │ warn if the btrfs sysfs directory cannot be found │
           └────────┴───────────────────────────────────────────────────┘

## [](#ENVIRONMENT)ENVIRONMENT

           The BTRFS_PATH environment variable can be set to override the
           default sysfs path (/sys/fs/btrfs) for testing purposes.

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

    Performance Co-Pilot               PCP                       PMDABTRFS(1)

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
