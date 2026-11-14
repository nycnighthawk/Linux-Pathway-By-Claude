---
{"title": "pcp-check(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-check.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-check(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMPONENT SCRIPTS](#COMPONENT_SCRIPTS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [CAVEAT](#CAVEAT) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-CHECK(1)             General Commands Manual             PCP-CHECK(1)

## [](#NAME)NAME

           pcp-check - manage the configuration of optional PCP components

## [](#SYNOPSIS)SYNOPSIS

           $pcp-check [-a] [-d] [-l] [-n] [-s] [-v] [-x] [component ...]
           $pcp-check [-a] [-c script]] [-d] [-l] [-n] [-s] [-v] [-x]
           $PCP_BINADM_DIR/pmcheck ...

## [](#DESCRIPTION)DESCRIPTION

           The Performance Co-Pilot (PCP) includes a number of core
           components that are likely to be pre-configured and operational,
           but it also includes a larger number of components that are not
           active by default.  In the context of pmcheck these components
           cover services that are typically started as part of the system
           boot procedure, e.g.  pmcd(1), pmlogger(1), pmproxy(1), etc. or
           optional Performance Metric Domain Agents (PMDAs) that augment the
           available performance metrics exported by pmcd(1).

           pmcheck allows the interrogation of the state of components with
           the -s, --state option.  Components can be activated with the -a,
           --activate option, or deactivated with the -d, --deactivate
           option.  These three options are clearly mutually exclusive for
           any single execution of pmcheck, and in the absence of any of them
           -s is assumed to be the default.

           The set of components to be interrogated or configured are
           specified by the component name(s) from the command line, else all
           known components in the absence of any component arguments.  When
           one or more component arguments are specified, these may
           optionally be sh(1) (glob) patterns that are matched against the
           names of the known components.

           The -l, --list option reports on known components.  With one or
           more components each is reported.  Without any component arguments
           the -l option lists all known components, which is simply all the
           component scripts (see the COMPONENT SCRIPTS section below) stored
           in the $PCP_SHARE_DIR/lib/pmcheck directory.  If the -v option is
           also used, a short description of each requested component is also
           displayed.

           Additional components can be integrated into the pmcheck
           framework, and the -c, --file option allows an alternate sh(1)
           script to be used instead of a script associated with a known
           component.

           In concert with the -a or -d options, the -n, --show-me option
           performs a dry run, showing the sh(1) commands that would be
           needed to perform the reconfiguration, but no reconfiguration is
           done.  Commands that need to be run as ``root'' are prefixed with
           # and other commands are prefixed with $.

           The -v, --verbose option increases reporting verbosity.

           The -x, --trace option may be used specify that the component
           scripts are run with -x option to sh(1).  This can assist with
           debugging the failure of a component script or during the
           development of a new component script, probably also involving the
           -c option to pmcheck.

           The -?, --help option displays a usage message.

           As a convience, pmcheck .  is an alias for pcp-check.

## [](#COMPONENT_SCRIPTS)COMPONENT SCRIPTS

           The pmcheck framework is extensible, as the set of known
           components is defined by the names of the component scripts in the
           $PCP_SHARE_DIR/lib/pmcheck directory.

           Each component script needs to abide by the following rules for
           correct integration with pmcheck:

           • The script will be run with sh(1), if you need some other
             scripting language then you must provide a sh(1) wrapper.
           • Since each script is responsible for one component, the name of
             the component is implied, however the name of the component is
             also passed from pmcheck as the sole argument after the options.
             This allows generic component scripts to be implemented as hard
             links below $PCP_SHARE_DIR/lib/pmcheck.
           • When called with a -l, --list option the script does nothing,
             unless it is also called with a -v option in which case a short
             description of the component is displayed on standard output.
           • When called with a -s, --state option, the script must exit with
             the an exit code that indicates the component's state, namely 0
             (active), 1 (inactive, but could be activated by pmcheck), 2
             (inactive and cannot be activated by pmcheck).  The distinction
             between exit codes 1 and 2 is based on many factors, but 1
             usually means all of the required software packages (PCP and
             other) are installed, required prerequisite services are running
             or could be safely started, and any component configuration can
             assume default settings or can be reliably deduced, e.g. a port
             number for communications.  Conversely, 2 means automatic
             activation of the component is not possible and some end-user
             intervention is required.
           • When called with a -a, --activate option the script must
             activate the component.  This means making any required
             configuration change so that it is restarted at the next system
             reboot or pmcd(1) restart, and starting the component if it is
             currently inactive,
           • When called with a -d, --deactivate option the script must
             deactivate the component.  This means stopping the component if
             it is currently active, and making any required configuration
             change so that it is not restarted at the next system reboot or
             pmcd(1) restart.
           • When called with a -n, --show-me option the script must perform
             a dry run and echo any required commands on standard output as
             per the rules described above for the -n option of pmcheck.
           • If a -v, --verbose option is also specified, the script should
             provide explanatory text on standard output to help explain,
             particularly in cases where the component is not active or the
             reconfiguration failed.

           To assist with component script development, the file
           $PCP_SHARE_DIR/lib/checkproc.sh may be sourced (after sourcing
           $PCP_DIR/etc/pcp.env).  checkproc.sh provides the following
           services:

           • A temporary directory is created and the shell variable $tmp is
             assigned to the full pathname of the directory.
           • The shell variable $status is used to return the exit status
             from the script [defaults to 0].
           • The shell variable $component is assigned to the associated
             component name.
           • The shell variable $prog is assigned to the script's basename
             (so the component name in the default case).
           • A trap is installed to cleanup $tmp and exit with $status.
           • A _do_args shell procedure that handles all command argument
             parsing.
           • Shell variables $aflag, $dflag, $lflag or $sflag have default
             values of false and are set to true by _do_args when the -a, -d,
             -l or -s options are parsed.
           • The shell variable $show_me has the default value of false and
             is set to true by _do_args when the -n option is parsed.
           • The shell variable $verbose counts number of -v options parsed
             by _do_args.
           • A _ctl_svc shell procedure that handles status requests and all
             reconfiguration operations for services that are managed by
             systemctl(1) or init(1) or similar infrastructure layers.
             _ctl_svc takes 2 arguments, the first is an action (one of
             state, start, stop, activate (enable and start), or deactivate
             (stop and disable), and the second is the name of the component;
             for systemctl(1) managed components, name should be the basename
             of the service, e.g.  pmcd for the pmcd.service systemd(1) unit,
             otherwise name is the name of the init(1) or similar ``rc''
             script.
           • _ctl_svc will return a value (via $?  when called from a shell
             script) that matches the exit codes defined above for each
             action.
           • A _ctl_pmda shell procedure that handles status requests and all
             reconfiguration operations for a PMDA that is connected to
             pmcd(1).  _ctl_pmda takes at least 2 arguments, the first is an
             action (one of state, activate or deactivate, and the second
             argument is the name of the PMDA.  For the install action, there
             is a third argument for the name of the PMDA's executable or DSO
             and an optional fourth argument is the name of a file providing
             the input required for the PMDA's Install script (defaults to
             /dev/null).
           • _ctl_pmda will return a value (via $?  when called from a shell
             script) that matches the exit codes defined above for each
             action.

           So the following is the simplest possible component script for a
           system service.

           #!/bin/sh
           . $PCP_DIR/etc/pcp.env || exit 1
           . $PCP_SHARE_DIR/lib/checkproc.sh
           _do_args "$@"
           if $lflag
           then
               [ $verbose -gt 0 ] && echo "my description"
           elif $sflag
           then
               _ctl_svc state $component
               status=$?
           elif $aflag
           then
               _ctl_svc activate $component || status=1
           elif $dflag
           then
               _ctl_svc deactivate $component || status=1
           fi

           And the following is the simplest possible component script for a
           PMDA.

           #!/bin/sh
           . $PCP_DIR/etc/pcp.env || exit 1
           . $PCP_SHARE_DIR/lib/checkproc.sh
           _do_args "$@"
           if $lflag
           then
               [ $verbose -gt 0 ] && echo "my description"
           elif $sflag
           then
               _ctl_pmda state $component
               status=$?
           elif $aflag
           then
               _ctl_pmda activate $component || status=1
           elif $dflag
           then
               _ctl_pmda deactivate $component || status=1
           fi

## [](#DIAGNOSTICS)DIAGNOSTICS

           For pmcheck (not the component scripts) the exit status is
           typically 0, but values of 9 or 99 indicate serious internal
           botches.

           When the -a or -d options are used, the success or failure of the
           reconfiguration is reported on standard output.

## [](#CAVEAT)CAVEAT

           Some components have prerequisites that demand additional non-PCP
           services be installed, configured and operational, e.g. a database
           server or a key-value server.  In these cases, probing the status
           of the non-PCP service may be subject to some access controls and
           if pmcheck is run as a non-root user, then the output from -s (the
           default) may be incomplete or misleading; in these circumstances,
           running pmcheck as root should provide a more accurate report.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           init(1), PCPIntro(1), pmcd(1), pmlogger(1), pmproxy(1), sh(1),
           systemctl(1), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                       PCP-CHECK(1)

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
