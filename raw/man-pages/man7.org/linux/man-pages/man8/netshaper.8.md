---
{"title": "netshaper(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/netshaper.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# netshaper(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [PARAMETERS](#PARAMETERS) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NETSHAPER(8)                      Linux                      NETSHAPER(8)

## [](#NAME)NAME

           netshaper - show / manipulate network device hardware shaping
           configuration

## [](#SYNOPSIS)SYNOPSIS

           netshaper [ OPTIONS ] { COMMAND | help }

           OPTIONS := { -V[ersion] | -c[olor] | -help }

           netshaper set dev DEV handle scope HANDLE_SCOPE [ id HANDLE_ID ] [
                   bw-min BW_MIN ] [ bw-max BW_MAX ] [ weight WEIGHT ]

           netshaper  {  show  |  delete  } dev DEV handle scope HANDLE_SCOPE
                   [ id HANDLE_ID ]

           netshaper group dev DEV handle scope { node | netdev } [ id
                   HANDLE_ID ] [ parent scope { netdev [ id PARENT_ID ] |
                   node id PARENT_ID } ] [ bw-min BW_MIN ] [ bw-max BW_MAX ]
                   [ weight WEIGHT ] leaves LEAF_SPEC [ LEAF_SPEC ... ]

                       LEAF_SPEC := scope queue id ID [ weight WEIGHT ] [
                       priority PRIO ]

## [](#DESCRIPTION)DESCRIPTION

           netshaper allows configuration and management of hardware rate
           limiting (shaping) capabilities available on network devices. The
           API provides control over shapers at different levels including
           network devices, queues, and scheduling nodes, enabling
           manipulation of the device's scheduling tree.

           Each shaper is uniquely identified within a device by a handle,
           which consists of a scope and an optional id.  Depending on the
           scope value, shapers are attached to specific hardware objects:

           netdev Shapers attached to the entire network device. The id
                  parameter is optional for this scope (defaults to 0 if not
                  specified).

           queue  Shapers attached to specific device queues. The id
                  parameter is required and specifies the queue number.

           node   Intermediate scheduling nodes that can be placed at
                  arbitrary locations in the scheduling tree. The id
                  parameter is required for set, show, and delete commands.
                  For the group command it is optional; if omitted, the
                  kernel auto-assigns one.

## [](#COMMANDS)COMMANDS

       netshaper set
           - Create or update a shaper configuration

           Creates or updates a shaper with the specified parameters. At
           least one of bw-min, bw-max, or weight must be provided. The id
           parameter is required for queue and node scopes and optional for
           netdev scope.

       netshaper show
           - Display shaper information

           Shows the current configuration of the specified shaper, including
           bandwidth limits, weight, and parent information.

       netshaper delete
           - Remove a shaper configuration

           Removes the specified shaper configuration from the device.

       netshaper group
           - Create a scheduling hierarchy

           Creates a scheduling group by binding one or more queue leaf
           shapers to a netdev or node handle in a single operation. The
           command specifies the target handle, its parent, optional
           bandwidth and weight parameters, and the set of queue leaves to
           attach.

## [](#PARAMETERS)PARAMETERS

           dev DEV
                  Specifies the network device name on which to operate.

           handle Defines the shaper handle consisting of:

                  scope HANDLE_SCOPE
                         The shaper scope, which can be: netdev (device-level
                         shaper), queue (queue-level shaper), or node
                         (scheduling node shaper).

                  id HANDLE_ID
                         Numeric identifier for the shaper. Required for
                         queue and node scopes. Optional for netdev scope
                         (defaults to 0). For the group command, node id may
                         be omitted to let the kernel auto-assign one.

           bw-min BW_MIN
                  Minimum guaranteed bandwidth for the shaper. Accepts values
                  with suffixes: kbit, mbit, gbit for kilobits, megabits, and
                  gigabits per second respectively.

           bw-max BW_MAX
                  Maximum bandwidth limit for the shaper. Accepts the same
                  suffixes as bw-min.

           weight WEIGHT
                  Scheduling weight for the shaper, used for weighted fair
                  sharing among siblings under the same parent node. Value is
                  an unsigned integer.

           parent Defines the parent for the group command. The parent scope
                  must be node or netdev; queue is not valid as a parent
                  scope.  For parent scope node, id is required. For parent
                  scope netdev, id is optional.  When omitted, the parent is
                  inherited from the leaves' current parent, which requires
                  all leaves to share the same parent.

           leaves Specifies one or more leaf shapers to attach to the group.
                  Each leaf must use scope queue; no other scope is accepted
                  for leaves.  Each leaf is given as scope queue id ID, with
                  optional weight and priority parameters for per-queue
                  scheduling within the group.  Multiple leaves can be
                  specified in sequence.

## [](#OPTIONS)OPTIONS

           -V, -Version
                  Print the version of the netshaper utility and exit.

           -c[color] = {always | auto | never}
                  Configure color output. If the parameter is omitted or
                  always, color output is enabled regardless of stdout state.
                  If the parameter is auto, stdout is checked to be a
                  terminal before enabling color output. If the parameter is
                  never, color output is disabled. If specified multiple
                  times, the last one takes precedence.

           -help  Display usage information and exit.

## [](#EXAMPLES)EXAMPLES

           Example 1: Create a device-level shaper
                  # netshaper set dev foo handle scope netdev bw-max 10gbit
                  Creates a netdev-scoped shaper with maximum bandwidth of 10
                  Gbit/s.

           Example 2: Set bandwidth and weight on a queue shaper
                  # netshaper set dev foo handle scope queue id 0 \
                      bw-min 1gbit bw-max 5gbit weight 10
                  Creates a queue-scoped shaper on queue 0 with
                  minimum/maximum bandwidth limits and a scheduling weight.

           Example 3: Show shaper configuration
                  # netshaper show dev foo handle scope netdev
                  Displays the current shaper configuration for the specified
                  device and handle.

           Example 4: Create a scheduling hierarchy with group
                  # netshaper group dev foo handle scope node \
                      parent scope netdev bw-max 10gbit \
                      leaves scope queue id 0 weight 3 \
                      scope queue id 1 weight 2
                  Creates a node shaper under the netdev parent, grouping
                  queues 0 and 1 as leaves. The 10 Gbit/s cap applies to the
                  node itself.

           Example 5: Delete shaper configuration
                  # netshaper delete dev foo handle scope netdev
                  Removes the specified shaper configuration.

## [](#NOTES)NOTES

           •      For netdev scope, the id parameter is optional and defaults
                  to 0 if not specified.

           •      For queue and node scopes, the id parameter is required.
                  For the group command, node id may be omitted to let the
                  kernel auto-assign one.

           •      Bandwidth values support standard suffixes: kbit (kilobits
                  per second), mbit (megabits per second), gbit (gigabits per
                  second).

           •      The group command attaches queue leaves to a netdev or node
                  handle in a single atomic operation.

## [](#SEE_ALSO)SEE ALSO

           ip(8), ip-link(8), tc(8)

## [](#AUTHOR)AUTHOR

           Erni Sri Satya Vennela <ernis@linux.microsoft.com>
           Mohsin Bashir <hmohsin@meta.com>

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

    iproute2                       19 May 2026                   NETSHAPER(8)

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
