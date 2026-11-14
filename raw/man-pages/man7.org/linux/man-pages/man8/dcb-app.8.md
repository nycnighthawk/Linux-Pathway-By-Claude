---
{"title": "dcb-app(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dcb-app.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dcb-app(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [PARAMETERS](#PARAMETERS) \| [EXAMPLE & USAGE](#EXAMPLE_&_USAGE) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DCB-APP(8)                        Linux                        DCB-APP(8)

## [](#NAME)NAME

           dcb-app - show / manipulate application priority table of the DCB
           (Data Center Bridging) subsystem

## [](#SYNOPSIS)SYNOPSIS

           dcb [ OPTIONS ] app { COMMAND | help }

           dcb app  {  show  |  flush  }  dev DEV [ default-prio ] [ ethtype-
                   prio ] [ stream-port-prio ] [ dgram-port-prio ] [ port-
                   prio ] [ dscp-prio ] [ pcp-prio ]

           dcb app  {  add  |  del  |  replace  }  dev DEV [ default-prio
                   PRIO-LIST ] [ ethtype-prio ET-MAP ] [ stream-port-prio
                   PORT-MAP ] [ dgram-port-prio PORT-MAP ] [ port-prio PORT-
                   MAP ] [ dscp-prio DSCP-MAP ] [ pcp-prio PCP-MAP ]

           PRIO-LIST := [ PRIO-LIST ] PRIO

           ET-MAP := [ ET-MAP ] ET-MAPPING

           ET-MAPPING := ET:PRIO

           PORT-MAP := [ PORT-MAP ] PORT-MAPPING

           PORT-MAPPING := PORT:PRIO

           DSCP-MAP := [ DSCP-MAP ] DSCP-MAPPING

           DSCP-MAPPING := { DSCP | all }:PRIO

           PCP-MAP := [ PCP-MAP ] PCP-MAPPING

           PCP-MAPPING := PCP:PRIO

           ET := { 0x600 .. 0xffff }

           PORT := { 1 .. 65535 }

           DSCP := { 0 .. 63 }

           PCP := { 0(nd/de) .. 7(nd/de) }

           PRIO := { 0 .. 7 }

## [](#DESCRIPTION)DESCRIPTION

           dcb app is used to configure the APP table, or application
           priority table in the DCB (Data Center Bridging) subsystem. The
           APP table is used to assign priority to traffic based on values in
           one of several headers: EtherType, L4 destination port, or DSCP.
           It also allows configuration of port-default priority that is
           chosen if no other prioritization rule applies.

           DCB APP entries are 3-tuples of selector, protocol ID, and
           priority. Selector is an enumeration that picks one of the
           prioritization namespaces. Currently it mostly corresponds to
           configurable parameters described below. Protocol ID is a value in
           the selector namespace. E.g. for EtherType selector, protocol IDs
           are the individual EtherTypes, for DSCP they are individual code
           points. The priority is the priority that should be assigned to
           traffic that matches the selector and protocol ID.

           The APP table is a set of DCB APP entries. The only requirement is
           that duplicate entries are not added. Notably, it is valid to have
           conflicting priority assignment for the same selector and protocol
           ID. For example, the set of two APP entries (DSCP, 10, 1) and
           (DSCP, 10, 2), where packets with DSCP of 10 should get priorities
           1 and 2, form a well-defined APP table. The dcb app tool allows
           low-level management of the app table by adding and deleting
           individual APP 3-tuples through add and del commands. On the other
           hand, the command replace does what one would typically want in
           this situation--first adds the new configuration, and then removes
           the obsolete one, so that only one prioritization is in effect for
           a given selector and protocol ID.

## [](#COMMANDS)COMMANDS

           show   Displays all entries with a given selector. When no
                  selector is given, shows all APP table entries categorized
                  per selector.

           flush  Removes all entries with a given selector. When no selector
                  is given, removes all APP table entries.

           add
           del    Add and, respectively, remove individual APP 3-tuples to
                  and from the DCB APP table.

           replace
                  Takes the list of entries mentioned as parameter, and adds
                  those that are not present in the APP table yet. Then
                  removes those entries, whose selector and protocol ID have
                  been mentioned as parameter, but not with the exact same
                  priority. This has the effect of, for the given selector
                  and protocol ID, ensuring that the table only contains the
                  priority (or priorities) given as parameter.

## [](#PARAMETERS)PARAMETERS

           The following table shows parameters in a way that they would be
           used with add, del and replace commands. For show and flush, the
           parameter name is to be used as a simple keyword without further
           arguments.

           default-prio PRIO-LIST
                  The priority to be used for traffic whose priority is
                  otherwise unspecified. The argument is a list of individual
                  priorities. Note that default-prio rules are configured as
                  triplets (EtherType, 0, PRIO).  dcb app translates these
                  rules to the symbolic name default-prio and back.

           ethtype-prio ET-MAP
                  ET-MAP uses the array parameter syntax, see dcb(8) for
                  details. Keys are EtherType values. Values are priorities
                  to be assigned to traffic with the matching EtherType.

           stream-port-prio PORT-MAP
           dgram-port-prio PORT-MAP
           port-prio PORT-MAP
                  PORT-MAP uses the array parameter syntax, see dcb(8) for
                  details. Keys are L4 destination port numbers that match
                  on, respectively, TCP and SCTP traffic, UDP and DCCP
                  traffic, and either of those. Values are priorities that
                  should be assigned to matching traffic.

           dscp-prio DSCP-MAP
                  DSCP-MAP uses the array parameter syntax, see dcb(8) for
                  details. Keys are DSCP points, values are priorities
                  assigned to traffic with matching DSCP. DSCP points can be
                  written either directly as numeric values, or using
                  symbolic names specified in /etc/iproute2/rt_dsfield
                  (however note that the file specifies full 8-bit dsfield
                  values, whereas dcb app will only use the higher six bits).
                  dcb app show will similarly format DSCP values as symbolic
                  names if possible. The command line option -N turns the
                  show translation off.

           pcp-prio PCP-MAP
                  PCP-MAP uses the array parameter syntax, see dcb(8) for
                  details. Keys are PCP/DEI. Values are priorities assigned
                  to traffic with matching PCP/DEI. PCP/DEI values are
                  written as a combination of numeric and symbolic values, to
                  accommodate both. PCP is always in numerical form, e.g., 0
                  .. 7 and DEI in symbolic form, e.g., 'de' (drop-eligible),
                  indicating that the DEI bit is 1 or 'nd' (not-drop-
                  eligible), indicating that the DEI bit is 0.  In
                  combination 2de:1 translates to a mapping of PCP=2 and
                  DEI=1 to priority 1.

## [](#EXAMPLE_&_USAGE)EXAMPLE & USAGE

           Prioritize traffic with DSCP 0 to priority 0, 24 to 3 and 48 to 6:

           # dcb app add dev eth0 dscp-prio 0:0 24:3 48:6

           Add another rule to configure DSCP 24 to priority 2 and show the
           result:

           # dcb app add dev eth0 dscp-prio 24:2
           # dcb app show dev eth0 dscp-prio
           dscp-prio 0:0 CS3:2 CS3:3 CS6:6
           # dcb -N app show dev eth0 dscp-prio
           dscp-prio 0:0 24:2 24:3 48:6

           Reconfigure the table so that the only rule for DSCP 24 is for
           assignment of priority 4:

           # dcb app replace dev eth0 dscp-prio 24:4
           # dcb app -N show dev eth0 dscp-prio
           dscp-prio 0:0 24:4 48:6

           Flush all DSCP rules:

           # dcb app flush dev eth0 dscp-prio
           # dcb app show dev eth0 dscp-prio
           (nothing)

           Add a rule to map traffic with PCP 1 and DEI 0 to priority 1 and
           PCP 2 and DEI 1 to priority 2:

           # dcb app add dev eth0 pcp-prio 1nd:1 2de:2
           # dcb app show dev eth0 pcp-prio
           pcp-prio 1nd:1 2de:2

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

    iproute2                     6 December 2020                   DCB-APP(8)

------------------------------------------------------------------------

Pages that refer to this page: [dcb(8)](../man8/dcb.8.html),  [dcb-apptrust(8)](../man8/dcb-apptrust.8.html),  [dcb-rewr(8)](../man8/dcb-rewr.8.html)

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
