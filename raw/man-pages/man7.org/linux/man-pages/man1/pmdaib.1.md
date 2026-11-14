---
{"title": "pmdaib(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdaib.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdaib(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIG FILE](#CONFIG_FILE) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAIB(1)                General Commands Manual                PMDAIB(1)

## [](#NAME)NAME

           pmdaib - Infiniband performance metrics domain agent (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/infiniband/pmdaib [-c configFile] [-D debug] [-d
           domain] [-l logfile] [-w]

## [](#DESCRIPTION)DESCRIPTION

           pmdaib is a Performance Metrics Domain Agent (PMDA) which exports
           information and performance metrics about local Infiniband HCAs
           and local or remote Infiniband GUIDs.

           A brief description of the pmdaib command line options follows:

           -c   Location of the config file.  By default, the config file is
                named $PCP_PMDAS_DIR/infiniband/config.  See CONFIG FILE for
                more information.

           -d   Specify an alternate performance metrics domain number.
                Almost never necessary.

           -l   Location of the log file.  By default, a log file named
                ib.log is written to $PCP_LOG_DIR/pmcd.  If the log file
                cannot be created or is not writable, output is written to
                the standard error instead.

           -w   Write out the default config file to
                $PCP_PMDAS_DIR/infiniband and exit immediately.  The written
                config file will contain the local HCA ports.  It will not
                overwrite an existing file.  This argument should only be
                used to create the template config file and should never
                appear in pmcd.conf.  See CONFIG FILE for more information on
                the file format and on monitoring remote GUIDs.

## [](#CONFIG_FILE)CONFIG FILE

           By default, the PMDA will operate without using a config file.  In
           this mode of operation the local HCA ports will be monitored.
           Note that if a new HCA is added to the machine that instance
           domain naming may change because it will always be based on the
           kernel's naming.

           In cases where this is not acceptable, or in the case where
           monitoring remote Infiniband ports is required, a config file must
           be created.  A "template" file can be created by running the
           pmdaib daemon with the -w argument.  This will create a config
           file with the local ports and GUIDs.

           If the config file is executable then it will be run and the
           output will be used as the config file.

           The config file is composed of line-based records.  Blank lines
           and everything after the hash (#) character are ignored.  Each
           line has 6 fields:

           [instName] [portGUID] [portNum] via [localPortName]:[localPortNum]

           The first field is used to give a static instance name to the
           Infiniband port that has a specific GUID.  All of the other fields
           must be properly specified in order to monitor a particular port.

           For example, to monitor port 1 of the local HCA called 'mthca0' a
           possible config file line would be:

           myPort1 0xdeadbeef01234567 1 via mthca0:1

           Remote ports can be easily monitored by specifying the GUID of the
           HCA or switch and specifying the remote port number.  The
           localPortName:localPortNum tuple specifies which local HCA and
           port to use as the "first hop" in contacting the remote GUID.
           E.g., to monitor port 13 of a remote switch which is connected to
           the fabric on the first port of the second HCA:

           switch13 0xfeeffeefabcdabcd 13 via mthca1:1

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), PMAPI(3) and ibnetdiscover(8).

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

    Performance Co-Pilot               PCP                          PMDAIB(1)

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
