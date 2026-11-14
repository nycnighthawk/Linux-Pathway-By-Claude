---
{"title": "pmerr(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmerr.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmerr(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMERR(1)                 General Commands Manual                 PMERR(1)

## [](#NAME)NAME

           pmerr - translate Performance Co-Pilot error codes into error
           messages

## [](#SYNOPSIS)SYNOPSIS

           pmerr [-?]  code ...
           pmerr -l

## [](#DESCRIPTION)DESCRIPTION

           pmerr accepts standard Performance Co-Pilot (PCP) error codes via
           the code argument(s) and generates the corresponding error text.

           Each code may be an integer, a hexadecimal value or a hexadecimal
           value prefixed by either ``0x'' or ``0X''.

           Error codes must be less than zero, so if code is a positive
           number, a warning message is produced, and the negated value is
           used.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -l, --list
                This alternative invocation causes all known error codes to
                be listed, along with their symbolic names and error text.

           -?, --help
                Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PMAPI(3), pmErrStr(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                           PMERR(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmcd(1)](../man1/pmcd.1.html),  [pmprobe(1)](../man1/pmprobe.1.html),  [pcpintro(3)](../man3/pcpintro.3.html),  [pmdiscoversetup(3)](../man3/pmdiscoversetup.3.html),  [pmerrstr(3)](../man3/pmerrstr.3.html)

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
