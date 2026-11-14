---
{"title": "pmdabpf(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdabpf.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdabpf(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDABCC(1)               General Commands Manual               PMDABCC(1)

## [](#NAME)NAME

           pmdabpf - eBPF PMDA

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/bpf/pmdabpf [-D debug]

## [](#DESCRIPTION)DESCRIPTION

           pmdabpf is a Performance Co-Pilot (PCP) Performance Metrics Domain
           Agent (PMDA) which extracts live performance data from eBPF
           programs utilizing BPF CO-RE (libbpf and BTF).

           pmdabpf loads and acts as a bridge for any number of configured,
           separate bpf PMDA modules. Existing libbpf tools should be
           possible to be utilized with the bpf PMDA modules with reasonable
           effort.

           See the eBPF, libbpf and BPF CO-RE documentation for detailed
           descriptions.

## [](#CONFIGURATION)CONFIGURATION

           pmdabpf reads a mandatory ini-style configuration file:

                  $PCP_PMDAS_DIR/bpf/bpf.conf

           Each section of the file corresponds to one bpf PMDA module.  The
           following global options are available for every module (their
           default values are shown in parenthesis):

           enabled (unset)
                  A boolean value to specify whether this bpf PMDA module
                  should be started or not.

           Modules may also support additional module-specific configuration
           options, refer to the default configuration file for their
           supported options.

## [](#INSTALLATION)INSTALLATION

           To install, the following must be done as root:

               # cd $PCP_PMDAS_DIR/bpf
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/bpf
               # ./Remove

           pmdabpf is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

           Some modules will start providing values only after having
           collected data from related system activity.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/bpf/bpf.conf
                configuration file for the pmdabpf agent

           $PCP_PMDAS_DIR/bpf/modules/*.{o,so}
                bpf PMDA modules available for the pmdabpf agent

           $PCP_PMDAS_DIR/bpf/Install
                installation script for the pmdabpf agent

           $PCP_PMDAS_DIR/bpf/Remove
                undo installation script for the pmdabpf agent

           $PCP_LOG_DIR/pmcd/bpf.log
                default log file for messages from the pmdabpf agent

           Note that the usual/default value for $PCP_PMDAS_DIR is
           /var/lib/pcp/pmdas and the default for $PCP_LOG_DIR is
           /var/log/pcp but these settings are platform dependent.

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

           PCPIntro(1), bpf(1) and pmcd(1).

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

    Performance Co-Pilot               PCP                         PMDABCC(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-atop(1)](../man1/pcp-atop.1.html)

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
