---
{"title": "genpmda(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/genpmda.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# genpmda(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GENPMDA(1)               General Commands Manual               GENPMDA(1)

## [](#NAME)NAME

           genpmda - Performance Co-Pilot PMDA Generator

## [](#SYNOPSIS)SYNOPSIS

           genpmda [-dv] [-D domain] [-n pmns] [-o dir] [-s stdpmid] [-t
           topdir] -c config -i IAM

## [](#DESCRIPTION)DESCRIPTION

           genpmda is a rapid application development tool for creating new
           Performance Metrics Domain Agents, see PMDA(3).  It provides a
           very easy and efficient way to extend the Performance Co-pilot
           (PCP) with new performance metrics without needing to understand
           the low level details of how PMDAs are constructed.

           genpmda reads a config file containing an augmented Performance
           Metrics Name Space, see PMNS(5), and automatically generates
           virtually all of the source code to implement a fully functional
           PMDA, including the Makefile, name space, support scripts for
           configuring the new PMDA, and the metrics help text.  Fairly
           simple PMDAs can be automatically generated from the config file
           without writing any additional code.  More complicated PMDAs, e.g.
           containing multiple instance domains, require only the refresh
           methods for the instance domains to be written manually.

           An example of the config file format accepted by genpmda is given
           below.

## [](#OPTIONS)OPTIONS

           Required options:

           -c config
                input config file, see example below

           -i IAM
                PMDA name IAM, should appear in stdpmid or the -D option must
                be used to specify a domain.

           Other options:

           -d   generate an Install script for a daemon PMDA (default is DSO)

           -D domain
                use domain number in the generated pmns and domain.h (if -s
                is not given)

           -n pmns
                use pmns as root of the namespace (default matches -i flag)

           -o dir
                use dir for generated source code, default ./generated

           -s stdpmid
                path to stdpmid (default ../../pmns/stdpmid)

           -t topdir
                use topdir in generated GNUmakefile, default ../../..

           -v   print verbose messages about what genpmda is doing.

           Example:
               Generate an "example" PMDA using domain 99:

               genpmda -D 99 -v -i EXAMPLE -c example.conf

           Here is example.conf config file (for the required -c option):

                example {
                    metric
                }

                example.metric {
                    ##  metric            string
                    ##  pmid              EXAMPLE:CLUSTER:0
                    ##  indom             PM_INDOM_NULL
                    ##  type              PM_TYPE_STRING
                    ##  units             PMDA_PMUNITS(0,0,0,0,0,0)
                    ##  semantics         PM_SEM_DISCRETE
                    ##  briefhelptext     one line help text for example.metric.string
                    ##  helptext          long help text for example.metric.string
                    ##  helptext          This is the second line of the long help text
                    ##  helptext          and this is the third line.
                    ##  fetch             function example_string_fetch_callback
                    ##  code              atom->cp = "hello world";
                    ##  code              return 1;
                    ##  endmetric
                }

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), PMDA(3), pcp.conf(5), pcp.env(5) and PMNS(5).

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

    Performance Co-Pilot               PCP                         GENPMDA(1)

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
