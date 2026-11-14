---
{"title": "dcb-apptrust(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dcb-apptrust.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dcb-apptrust(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [PARAMETERS](#PARAMETERS) \| [EXAMPLE & USAGE](#EXAMPLE_&_USAGE) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DCB-APPTRUST(8)                   Linux                   DCB-APPTRUST(8)

## [](#NAME)NAME

           dcb-apptrust - show / configure per-selector trust and trust order
           of the application priority table of the DCB (Data Center
           Bridging) subsystem

## [](#SYNOPSIS)SYNOPSIS

           dcb [ OPTIONS ] apptrust { COMMAND | help }

           dcb apptrust show dev DEV [ order ]

           dcb apptrust set dev DEV [ order SEL-LIST ]

           SEL-LIST := [ SEL-LIST ] SEL

           SEL := { ethtype | stream-port | dgram-port | port | dscp | pcp }

## [](#DESCRIPTION)DESCRIPTION

           dcb apptrust is used to configure per-selector trust and trust
           order of the Application Priority Table, see dcb-app(8) for
           details on how to configure app table entries.

           Selector trust can be used by the software stack or drivers (most
           likely the latter) when querying the APP table, to determine
           whether an APP entry should take effect. Additionally, the order
           of the trusted selectors dictates which selector should take
           precedence, in the case of multiple different APP table selectors
           being present.

## [](#COMMANDS)COMMANDS

           show   Displays all trusted selectors.

           set    Sets a new list of trusted selectors. An empty list is
                  effectively the same as removing trust entirely.

## [](#PARAMETERS)PARAMETERS

           The following describes only the write direction, i.e. as used
           with the set command. For the show command, the parameter name is
           to be used as a simple keyword without further arguments. This
           instructs the tool to show the values of a given parameter.

           order SEL-LIST
                  SEL-LIST is a space-separated list of selector names.
                  Possible selector values are: ethtype, stream-port, dgram-
                  port, port, dscp, and pcp

## [](#EXAMPLE_&_USAGE)EXAMPLE & USAGE

           Set trust order to: dscp, pcp for eth0:

           # dcb apptrust set dev eth0 order dscp pcp

           Set trust order to: port (stream or dgram), pcp, ethtype for eth1:

           # dcb apptrust set dev eth1 order port pcp ethtype

           Show what was set:

           # dcb apptrust show dev eth0
           order: port pcp ethtype

## [](#EXIT_STATUS)EXIT STATUS

           Exit status is 0 if command was successful or a positive integer
           upon failure.

## [](#SEE_ALSO)SEE ALSO

           dcb(8), dcb-app(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           Report any bugs to the Network Developers mailing list
           <netdev@vger.kernel.org> where the development and maintenance is
           primarily done.  You do not have to be subscribed to the list to
           send a message there.

## [](#AUTHOR)AUTHOR

           Daniel Machon <daniel.machon@microchip.com>

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

    iproute2                     22 November 2022             DCB-APPTRUST(8)

------------------------------------------------------------------------

Pages that refer to this page: [dcb(8)](../man8/dcb.8.html),  [dcb-rewr(8)](../man8/dcb-rewr.8.html)

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
