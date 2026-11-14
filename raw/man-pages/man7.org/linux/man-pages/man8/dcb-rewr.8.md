---
{"title": "dcb-rewr(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dcb-rewr.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dcb-rewr(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [PARAMETERS](#PARAMETERS) \| [EXAMPLE & USAGE](#EXAMPLE_&_USAGE) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DCB-REWR(8)                       Linux                       DCB-REWR(8)

## [](#NAME)NAME

           dcb-rewr - show / manipulate the rewrite table of the DCB (Data
           Center Bridging) subsystem

## [](#SYNOPSIS)SYNOPSIS

           dcb [ OPTIONS ] rewr { COMMAND | help }

           dcb rewr  {  show  |  flush  }  dev DEV [ prio-dscp ] [ prio-pcp ]

           dcb rewr  {  add  |  del  |  replace  }  dev DEV [ prio-dscp DSCP-
                   MAP ] [ prio-pcp PCP-MAP ]

           DSCP-MAP := [ DSCP-MAP ] DSCP-MAPPING

           DSCP-MAPPING := PRIO:{ DSCP | all }

           PCP-MAP := [ PCP-MAP ] PCP-MAPPING

           PCP-MAPPING := PRIO:PCP

           DSCP := { 0 .. 63 }

           PCP := { 0(nd/de) .. 7(nd/de) }

           PRIO := { 0 .. 7 }

## [](#DESCRIPTION)DESCRIPTION

           dcb rewr is used to configure the rewrite table, in the DCB (Data
           Center Bridging) subsystem.  The rewrite table is used to rewrite
           certain values in the packet headers, based on packet priority.

           DCB rewrite entries are, like DCB APP entries, 3-tuples of
           selector, protocol ID, and priority. Selector is an enumeration
           that picks one of the prioritization namespaces. Currently, only
           the DSCP and PCP selector namespaces are supported by dcb rewr.

           The rewrite table is a list of DCB rewrite rules that applies to
           packets with matching priority. Notably, it is valid to have
           conflicting rewrite assignments for the same selector and
           priority. For example, the set of two rewrite entries (DSCP, 10,
           1) and (DSCP, 11, 1), where packets with priority 1 should have
           their DSCP values rewritten to both 10 and 11, form a well-defined
           rewrite table.  dcb rewr tool allows low-level management of the
           rewrite table by adding and deleting individual rewrite 3-tuples
           through add and del commands. On the other hand, the command
           replace does what one would typically want in this
           situation--first adds the new configuration, and then removes the
           obsolete one, so that only one rewrite rule is in effect for a
           given selector and priority.

## [](#COMMANDS)COMMANDS

           show   Displays all entries with a given selector. When no
                  selector is given, shows all rewrite table entries
                  categorized per selector.

           flush  Removes all entries with a given selector. When no selector
                  is given, removes all rewrite table entries.

           add
           del    Add and, respectively, remove individual rewrite 3-tuples
                  to and from the DCB rewrite table.

           replace
                  Takes the list of entries mentioned as parameter, and adds
                  those that are not present in the rewrite table yet. Then
                  removes those entries, whose selector and priority have
                  been mentioned as parameter, but not with the exact same
                  protocol ID. This has the effect of, for the given selector
                  and priority, ensuring that the table only contains the
                  protocol ID (or IDs) given as parameter.

## [](#PARAMETERS)PARAMETERS

           The following table shows parameters in a way that they would be
           used with add, del and replace commands. For show and flush, the
           parameter name is to be used as a simple keyword without further
           arguments.

           prio-dscp DSCP-MAP
                  DSCP-MAP uses the array parameter syntax, see dcb(8) for
                  details. Keys are priorities, values are DSCP points for
                  traffic with matching priority. DSCP points can be written
                  either directly as numeric values, or using symbolic names
                  specified in /etc/iproute2/rt_dsfield (however note that
                  the file specifies full 8-bit dsfield values, whereas dcb
                  rewr will only use the higher six bits).  dcb rewr show
                  will similarly format DSCP values as symbolic names if
                  possible. The command line option -N turns the show
                  translation off.

           prio-pcp PCP-MAP
                  PCP-MAP uses the array parameter syntax, see dcb(8) for
                  details. Keys are priorities. Values are PCP/DEI for
                  traffic with matching priority. PCP/DEI values are written
                  as a combination of numeric and symbolic values, to
                  accommodate both. PCP is always in numeric form, e.g., 0 ..
                  7 and DEI in symbolic form, e.g., 'de' (drop-eligible),
                  indicating that the DEI bit is 1 or 'nd' (not-drop-
                  eligible), indicating that the DEI bit is 0. In combination
                  1:2de translates to a mapping of priority 1 to PCP=2 and
                  DEI=1.

## [](#EXAMPLE_&_USAGE)EXAMPLE & USAGE

           Add a rule to rewrite DSCP to 0, 24 and 48 for traffic with
           priority 0, 3 and 6, respectively:

           # dcb rewr add dev eth0 prio-dscp 0:0 3:24 6:48

           Add a rule to rewrite DSCP to 25 for traffic with priority 3:

           # dcb rewr add dev eth0 prio-dscp 3:25
           # dcb rewr show dev eth0 prio-dscp
           prio-dscp 0:0 3:CS3 3:25 6:CS6
           # dcb -N rewr show dev eth0 prio-dscp
           prio-dscp 0:0 3:24 3:25 6:48

           Reconfigure the table so that only one rule exists for rewriting
           traffic with priority 3.

           # dcb rewr replace dev eth0 prio-dscp 3:26
           # dcb rewr -N show dev eth0 prio-dscp
           prio-dscp 0:0 3:26 6:48

           Flush all DSCP rules:

           # dcb rewr flush dev eth0 prio-dscp
           # dcb rewr show dev eth0 prio-dscp
           (nothing)

           Add a rule to rewrite PCP to 1 and DEI to 0 for traffic with
           priority 1 and a rule to rewrite PCP to 2 and DEI to 1 for traffic
           with priority 2:

           # dcb rewr add dev eth0 prio-pcp 1:1nd 2:2de
           # dcb rewr show dev eth0 prio-pcp
           prio-pcp 1:1nd 2:2de

## [](#EXIT_STATUS)EXIT STATUS

           Exit status is 0 if command was successful or a positive integer
           upon failure.

## [](#SEE_ALSO)SEE ALSO

           dcb(8), dcb-app(8), dcb-apptrust(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           Report any bugs to the Network Developers mailing list
           <netdev@vger.kernel.org> where the development and maintenance is
           primarily done. You do not have to be subscribed to the list to
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

    iproute2                       15 May 2023                    DCB-REWR(8)

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
