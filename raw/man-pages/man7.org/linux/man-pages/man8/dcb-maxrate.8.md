---
{"title": "dcb-maxrate(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dcb-maxrate.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dcb-maxrate(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PARAMETERS](#PARAMETERS) \| [EXAMPLE & USAGE](#EXAMPLE_&_USAGE) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DCB-MAXRATE(8)                    Linux                    DCB-MAXRATE(8)

## [](#NAME)NAME

           dcb-maxrate - show / manipulate port maxrate settings of the DCB
           (Data Center Bridging) subsystem

## [](#SYNOPSIS)SYNOPSIS

           dcb [ OPTIONS ] maxrate { COMMAND | help }

           dcb maxrate show dev DEV [ tc-maxrate ]

           dcb maxrate set dev DEV [ tc-maxrate RATE-MAP ]

           RATE-MAP := [ RATE-MAP ] RATE-MAPPING

           RATE-MAPPING := { TC | all }:RATE

           TC := { 0 .. 7 }

           RATE := { INTEGER[bit] | INTEGERKbit | INTEGERMib | ... }

## [](#DESCRIPTION)DESCRIPTION

           dcb maxrate is used to configure and inspect maximum rate at which
           traffic is allowed to egress from a given traffic class.

## [](#PARAMETERS)PARAMETERS

           The following describes only the write direction, i.e. as used
           with the set command. For the show command, the parameter name is
           to be used as a simple keyword without further arguments. This
           instructs the tool to show the value of a given parameter. When no
           parameters are given, the tool shows the complete maxrate
           configuration.

           tc-maxrate RATE-MAP
                  RATE-MAP uses the array parameter syntax, see dcb(8) for
                  details. Keys are TC indices, values are traffic rates in
                  bits per second.  The rates can use the notation documented
                  in section PARAMETERS at tc(8).  Note that under that
                  notation, "bit" stands for bits per second whereas "b"
                  stands for bytes per second. When showing, the command line
                  option -i toggles between using decadic and ISO/IEC
                  prefixes.

## [](#EXAMPLE_&_USAGE)EXAMPLE & USAGE

           Set rates of all traffic classes to 25Gbps, except for TC 6, which
           will have the rate of 100Gbps:

           # dcb maxrate set dev eth0 tc-maxrate all:25Gbit 6:100Gbit

           Show what was set:

           # dcb maxrate show dev eth0
           tc-maxrate 0:25Gbit 1:25Gbit 2:25Gbit 3:25Gbit 4:25Gbit 5:25Gbit
           6:100Gbit 7:25Gbit

## [](#EXIT_STATUS)EXIT STATUS

           Exit status is 0 if command was successful or a positive integer
           upon failure.

## [](#SEE_ALSO)SEE ALSO

           dcb(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           Report any bugs to the Network Developers mailing list
           <netdev@vger.kernel.org> where the development and maintenance is
           primarily done.  You do not have to be subscribed to the list to
           send a message there.

## [](#AUTHOR)AUTHOR

           Petr Machata <me@pmachata.org>

## [](#COLOPHON)COLOPHON

           This page is part of the iproute2 (utilities for controlling
           TCP/IP networking and traffic) project.  Information about the
           project can be found at 
           ⟨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2⟩.
           If you have a bug report for this manual page, send it to
           netdev@vger.kernel.org, shemminger@osdl.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/network/iproute2/iproute2.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iproute2                     22 November 2020              DCB-MAXRATE(8)

------------------------------------------------------------------------

Pages that refer to this page: [dcb(8)](../man8/dcb.8.html)

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
