---
{"title": "pmdakvm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdakvm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdakvm(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [CAVEATS](#CAVEATS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAKVM(1)               General Commands Manual               PMDAKVM(1)

## [](#NAME)NAME

           pmdakvm - Linux virtualization performance metrics domain agent
           (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/kvm/pmdakvm [-D debug]

## [](#DESCRIPTION)DESCRIPTION

           pmdakvm is a Performance Metrics Domain Agent (PMDA) which exports
           metric values from the Linux KVM (Kernel Virtual Machine)
           virtualization subsystem.

           Per-processor KVM trace metrics from the kernel events enumerated
           below /sys/kernel/debug/tracing/events/kvm can be configured
           statically using the pmdakvm configuration file,
           /etc/pcp/kvm/kvm.conf.

## [](#INSTALLATION)INSTALLATION

           Optionally configure trace points in the configuration file, then
           install the KVM PMDA by using the Install script as root:

               # cd $PCP_PMDAS_DIR/kvm
               # ./Install

           To uninstall, do the following as root:

               # cd $PCP_PMDAS_DIR/kvm
               # ./Remove

           pmdakvm is launched by pmcd(1) and should never be executed
           directly. The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#CAVEATS)CAVEATS

           When pmdakvm is running, it holds references to kernel resources
           within the KVM device driver.  It is thus not possible to unload
           or reload the device driver module while the PMDA is running.  The
           ideal procedure to follow in order to reload the kernel module is
           the reverse of that described in the ``INSTALLATION'' section
           above - i.e. first run ./Remove, then reload the kernel module,
           then run ./Install.

## [](#FILES)FILES

           $PCP_SYSCONF_DIR/kvm/kvm.conf
               configuration file for the pmdakvm agent

           $PCP_PMDAS_DIR/kvm/Install
               installation script for the pmdakvm agent

           $PCP_PMDAS_DIR/kvm/Remove
               undo installation script for the pmdakvm agent

           $PCP_LOG_DIR/pmcd/kvm.log
               default log file for error messages from pmdakvm

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
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

           PCPIntro(1), pmcd(1) and kvm(1).

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

    Performance Co-Pilot               PCP                         PMDAKVM(1)

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
