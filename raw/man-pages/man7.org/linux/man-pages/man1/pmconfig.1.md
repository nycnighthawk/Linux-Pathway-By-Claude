---
{"title": "pmconfig(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmconfig.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmconfig(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMCONFIG(1)              General Commands Manual              PMCONFIG(1)

## [](#NAME)NAME

           pmconfig - Performance Co-Pilot configuration parameters

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmconfig [-alLs?]  [name ...]

## [](#DESCRIPTION)DESCRIPTION

           pmconfig displays the values for some or all configuration
           parameters of the local Performance Co-Pilot toolkit installation.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -a, --all
                Reports all configuration parameters in the default format.

           -l, --list
                Synonym for the -a option, reports the same (default) format.

           -L, --library
                This option changes the default reporting mode so that the
                capabilities of the PCP library are reported, rather than the
                PCP environment.

           -s, --shell
                An output format suitable for sourcing in shell scripts which
                ensures configuration information is quoted and preceded by
                an export statement.  When not reporting the library
                capabilities, this mode will produce a statement that does
                not override an existing setting in the environment for PCP
                configuration variables.

           -?, --help
                Display usage message and exit.

           In the default operating mode, pmconfig is often used in
           conjunction with the $PCP_DIR environment variable to setup
           scripts running under the Windows operating system, where the
           filesystem hierarchy differs greatly to the of Linux/UNIX-based
           operating systems.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           pmGetConfig(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                        PMCONFIG(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogger_daily(1)](../man1/pmlogger_daily.1.html),  [pmgetconfig(3)](../man3/pmgetconfig.3.html),  [pcp.conf(5)](../man5/pcp.conf.5.html)

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
