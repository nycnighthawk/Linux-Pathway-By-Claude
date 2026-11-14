---
{"title": "pcp-kube-pods(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-kube-pods.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-kube-pods(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP_KUBE_PODS(1)         General Commands Manual         PCP_KUBE_PODS(1)

## [](#NAME)NAME

           pcp-kube-pods - list Kubernetes pods to scan for running PCP
           services

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/discover/pcp-kube-pods

## [](#DESCRIPTION)DESCRIPTION

           pcp-kube-pods uses kubectl(1) to provide a list of IP addresses
           for PODs running in a local Kubernetes cluster, that may be
           running PCP services like pmcd(1) and pmproxy(1).

           It is used by the pmfind(1) command and the pmDiscoverServices(3)
           API as a ``shell'' command.

           The script invokes the kubectl get pod command line (see
           kubectl-get(1)) to discover IP addresses for pods.  The
           .status.podIP output field is extracted from the Kubernetes pod
           object(s).  Additional options can be specified via configuration
           file, such as -l service=database to restrict the results using
           Kubernetes pod labels.  The default configuration file is
           $PCP_SYSCONF_DIR/discover/pcp-kube-pods.conf.

           If no local kubectl command is found, nothing is reported and an
           exit code indicating success is returned.

## [](#DIAGNOSTICS)DIAGNOSTICS

           All diagnostics produced are provided by the kubectl command.

           The kubectl exit status is propagated unchanged.

## [](#FILES)FILES

           $PCP_BINADM_DIR/discover
                default path to address discovery commands like pcp-kube-pods

           $PCP_SYSCONF_DIR/discover/pcp-kube-pods.conf
                configuration file containing command line options passed to
                kubectl-get

           $PCP_SYSCONF_DIR/discover/pcp-kube-pods.disabled
                existence of this file causes the script to report nothing

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           kubectl-get(1), kubectl(1), pmcd(1), pmfind(1),
           pmDiscoverServices(3) and pcp.env(5).

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

    Performance Co-Pilot               PCP                   PCP_KUBE_PODS(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmfind(1)](../man1/pmfind.1.html),  [pmdiscoverservices(3)](../man3/pmdiscoverservices.3.html)

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
