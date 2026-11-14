---
{"title": "pmdanetcheck(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdanetcheck.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdanetcheck(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDANETCHECK(1)          General Commands Manual          PMDANETCHECK(1)

## [](#NAME)NAME

           pmdanetcheck - netcheck PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdanetcheck is a Performance Co-Pilot (PCP) Performance Metrics
           Domain Agent (PMDA) which does basic network checks on the local
           host by using simple Python modules and, in some cases, external
           utilities such as ping(1).

           pmdanetcheck loads and acts as a bridge for any number of
           configured, separate PCP netcheck PMDA Python modules running
           Python code or external programs.  Existing Python modules and
           programs should be possible to be utilized with PCP netcheck PMDA
           modules with minimal effort.

           Note that on SELinux enabled systems for pmdanetcheck to be able
           to use the ping(1) command the pcp group must be able to create
           ICMP Echo sockets; please make sure the group id for pcp is
           included in the range at /proc/sys/net/ipv4/ping_group_range and
           refer to icmp(7) for more details on this.

## [](#CONFIGURATION)CONFIGURATION

           pmdanetcheck reads a mandatory ini-style configuration file:

                  $PCP_PMDAS_DIR/netcheck/netcheck.conf

           This file must contain a [pmda] section.  The following PMDA
           options are available (their default values are shown in
           parenthesis), options marked with asterisk (*) can be overridden
           in module-specific configuration sections:

           modules (unset)
                  The pmdanetcheck PMDA reads module-specific configuration
                  for each module listed in the comma-separated list of
                  modules (mandatory).

           hosts (DGW,DNS) *
                  A comma-separated list of hosts (optional) specifies the
                  hosts to run the checks for.  The special values DGW, DNS,
                  NTP will be translated to the default gateway, nameservers
                  listed in /etc/resolv.conf, and timeservers listed in
                  /etc/chrony.conf, respectively, on PMDA startup.

           background_check (True) *
                  A boolean value for background_check (optional) controls
                  whether to run checks constantly in the background or only
                  on demand.  Refer to the default configuration file for
                  more discussion about this.

           check_hosts_parallel (True) *
                  check_hosts_parallel (optional) controls whether modules
                  should check hosts one by one or in parallel.

           check_interval (1m) *
                  check_interval (optional) specifies the time interval
                  between two consecutive checks for hosts when checks are
                  done in the background.  Refer to PCPIntro(1) for a
                  complete description of the syntax for the time interval.

           align_interval (True) *
                  align_interval (optional) specifies whether to take the
                  previous check duration into account when pausing between
                  checks.

           module_failure_fatal (True)
                  A boolean value for module_failure_fatal (optional)
                  controls whether a module failing to initialize should
                  cause the whole PMDA to abort (this is the default) or to
                  start up with possibly remaining functional modules.
                  Module configuration errors and internal errors (such as
                  failing to register the provided PMNS metrics, see pmns(5))
                  will always cause the PMDA to fail to start.

           For each module listed in modules a corresponding [module] section
           must be defined.  Each [module] section can contain at least the
           following options (their default values are shown in parenthesis):

           timeout (1)
                  Force a hard timeout (optional) for each individual network
                  check operation.

           debug (False)
                  Enable logging of internal debug messages (rarely used).

           The module-specific options modules accept are described in the
           default configuration file.

           Modules expect basic network functionality to be present on the
           system, for example the localhost address being reachable.

## [](#INSTALLATION)INSTALLATION

           To install, the following must be done as root:

               # cd $PCP_PMDAS_DIR/netcheck
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/netcheck
               # ./Remove

           pmdanetcheck is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

           In case module_failure_fatal is set to False, the PMDA
           installation will be considered successful if some (but not all)
           configured modules fail to load, in such cases metrics provided by
           the failing modules will not be available.  The pmdanetcheck agent
           log file (see below) will contain detailed information about
           activation of each module.

           Modules will provide real values only after having collected data.
           For example, for the ping module the metric value is the exit
           value of the ping(1) command and for ping_latency the average
           packet latency as reported by ping(1).  For metrics indicating
           status, 0 denotes success.  In case a check has not finished yet
           its metric value is -1.  If a check was terminated during
           execution due to timeout the value is -2.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/netcheck/netcheck.conf
                configuration file for the pmdanetcheck agent

           $PCP_PMDAS_DIR/netcheck/netcheck/*.{py,python}
                PCP netcheck PMDA Python modules for the pmdanetcheck agent

           $PCP_PMDAS_DIR/netcheck/Install
                installation script for the pmdanetcheck agent

           $PCP_PMDAS_DIR/netcheck/Remove
                undo installation script for the pmdanetcheck agent

           $PCP_LOG_DIR/pmcd/netcheck.log
                default log file for messages from the pmdanetcheck agent

           Note that the usual/default value for $PCP_PMDAS_DIR is
           /var/lib/pcp/pmdas and the default for $PCP_LOG_DIR is
           /var/log/pcp but these settings are platform dependent.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), ping(1), pmcd(1), getaddrinfo(3), resolver(3),
           gai.conf(5), resolv.conf(5), resolver(5), icmp(7) and ip(8).

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

    Performance Co-Pilot               PCP                    PMDANETCHECK(1)

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
