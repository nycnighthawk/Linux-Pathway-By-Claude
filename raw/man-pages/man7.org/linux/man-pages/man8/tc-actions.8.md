---
{"title": "tc-actions(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-actions.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-actions(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPERATIONS](#OPERATIONS) \| [ACTION OPTIONS](#ACTION_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    actions in tc(8)                  Linux                  actions in tc(8)

## [](#NAME)NAME

           actions - independently defined actions in tc

## [](#SYNOPSIS)SYNOPSIS

           tc [ TC_OPTIONS ] actions add | change | replace ACTSPEC

           tc [ TC_OPTIONS ] actions get | delete ACTISPEC

           tc [ TC_OPTIONS ] actions flush ACTNAMESPEC

           tc [ TC_OPTIONS ] actions ls | list ACTNAMESPEC [ ACTFILTER ]

                   ACTSPEC := action ACTDETAIL [ INDEXSPEC ] [ COOKIESPEC ] [
                   FLAGS ] [ HWSTATSSPEC ] [ CONTROL ] [ SKIPSPEC ]

                   ACTISPEC := ACTNAMESPEC INDEXSPEC

                   ACTNAMESPEC := action ACTNAME

                   INDEXSPEC := index INDEX

                   ACTFILTER := since MSTIME

                   COOKIESPEC := cookie COOKIE

                   FLAGS := no_percpu

                   HWSTATSSPEC := hw_stats { immediate | delayed | disabled }

                   ACTDETAIL := ACTNAME ACTPARAMS

                   ACTNAME may be any valid action type: gact, mirred, bpf,
                   connmark, csum, police, etc.

                   MSTIME Time since last update.

                   CONTROL := { reclassify | pipe | drop | continue | ok }

                   SKIPSPEC := { skip_sw | skip_hw }

                   TC_OPTIONS These are the options that are specific to tc
                   and not only the options. Refer to tc(8) for more
                   information.

## [](#DESCRIPTION)DESCRIPTION

           The actions object in tc allows a user to define actions
           independently of a classifier (filter). These actions can then be
           assigned to one or more filters, with any packets matching the
           classifier's criteria having that action performed on them.

           Each action type (mirred, police, etc.) will have its own table to
           store all created actions.

## [](#OPERATIONS)OPERATIONS

           add    Create a new action in that action's table.

           change
           replace
                  Make modifications to an existing action.

           get    Display the action with the specified index value. When
                  combined with the -s option for tc, display the statistics
                  for that action.

           delete Delete the action with the specified index value. If the
                  action is already associated with a classifier, it does not
                  delete the classifier.

           ls
           list   List all the actions in the specified table. When combined
                  with the -s option for tc, display the statistics for all
                  actions in the specified table.  When combined with the
                  option since allows doing a millisecond time-filter since
                  the last time an action was used in the datapath.

           flush  Delete all actions stored in the specified table.

## [](#ACTION_OPTIONS)ACTION OPTIONS

           Note that these options are available to all action types.

           index INDEX
                  Specify the table index value of an action.  INDEX is a
                  32-bit value that is unique to the specific type of action
                  referenced.

                  For add, change, and replace operations, the index is
                  optional.  When adding a new action, specifying an index
                  value will assign the action to that index unless that
                  index value has already been assigned. Omitting the index
                  value for an add operation will cause the kernel to assign
                  a value to the new action.

                  For get and delete operations, the index is required to
                  identify the specific action to be displayed or deleted.

           cookie COOKIE
                  In addition to the specific action, mark the matching
                  packet with the value specified by COOKIE.  The COOKIE is a
                  128-bit value that will not be interpreted by the kernel
                  whatsoever.  As such, it can be used as a correlating value
                  for maintaining user state.  The value to be stored is
                  completely arbitrary and does not require a specific
                  format. It is stored inside the action structure itself.

           FLAGS  Action-specific flags. Currently, the only supported flag
                  is no_percpu which indicates that action is expected to
                  have minimal software data-path traffic and doesn't need to
                  allocate stat counters with percpu allocator.  This option
                  is intended to be used by hardware-offloaded actions.

           hw_stats HW_STATS
                  Specifies the type of HW stats of new action. If omitted,
                  any stats counter type is going to be used, according to
                  driver and its resources.  The HW_STATS indicates the type.
                  Any of the following are valid:

                  immediate
                         Means that in dump, user gets the current HW stats
                         state from the device queried at the dump time.

                  delayed
                         Means that in dump, user gets HW stats that might be
                         out of date for some time, maybe couple of seconds.
                         This is the case when driver polls stats updates
                         periodically or when it gets async stats update from
                         the device.

                  disabled
                         No HW stats are going to be available in dump.

           since MSTIME
                  When dumping large number of actions, a millisecond time-
                  filter can be specified MSTIME.  The MSTIME is a
                  millisecond count since last time a packet hit the action.
                  As an example specifying "since 20000" implies to dump all
                  actions that have seen packets in the last 20 seconds. This
                  option is useful when the kernel has a large number of
                  actions and you are only interested in recently used
                  actions.

           CONTROL
                  The CONTROL indicates how tc should proceed after executing
                  the action. Any of the following are valid:

                  reclassify
                         Restart the classifiction by jumping back to the
                         first filter attached to the action's parent.

                  pipe   Continue with the next action. This is the default
                         control.

                  drop   Drop the packet without running any further actions.

                  continue
                         Continue the classification with the next filter.

                  pass   Return to the calling qdisc for packet processing,
                         and end classification of this packet.

           SKIPSPEC
                  The SKIPSPEC indicates how tc should proceed when executing
                  the action. Any of the following are valid:

                  skip_sw
                         Do not process action by software. If hardware has
                         no offload support for this action, operation will
                         fail.

                  skip_hw
                         Do not process action by hardware.

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-bpf(8), tc-connmark(8), tc-csum(8), tc-ife(8),
           tc-mirred(8), tc-nat(8), tc-pedit(8), tc-police(8), tc-simple(8),
           tc-skbedit(8), tc-skbmod(8), tc-tunnel_key(8), tc-vlan(8),
           tc-xt(8)

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

    iproute2                        1 Aug 2017               actions in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc-gact(8)](../man8/tc-gact.8.html),  [tc-simple(8)](../man8/tc-simple.8.html)

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
