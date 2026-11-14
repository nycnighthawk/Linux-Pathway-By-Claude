---
{"title": "tc-connmark(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-connmark.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-connmark(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Connmark retr...r action in tc(8) Linux Connmark retr...r action in tc(8)

## [](#NAME)NAME

           connmark - netfilter connmark retriever action

## [](#SYNOPSIS)SYNOPSIS

           tc ... action connmark [ zone u16_zone_index ] [ CONTROL ] [ index
                   u32_index ]

           CONTROL := { reclassify | pipe | drop | continue | ok }

## [](#DESCRIPTION)DESCRIPTION

           The connmark action is used to restore the connection's mark value
           into the packet's fwmark.

## [](#OPTIONS)OPTIONS

           zone u16_zone_index
                  Specify the conntrack zone when doing conntrack lookups for
                  packets.  u16_zone_index is a 16bit unsigned decimal value.

           CONTROL
                  How to continue after executing this action.

                  reclassify
                         Restarts classification by jumping back to the first
                         filter attached to this action's parent.

                  pipe   Continue with the next action, this is the default.

                  drop
                  shot   Packet will be dropped without running further
                         actions.

                  continue
                         Continue classification with next filter in line.

                  pass   Return to calling qdisc for packet processing. This
                         ends the classification process.

           index u32_index
                  Specify an index for this action in order to being able to
                  identify it in later commands.  u32_index is a 32bit
                  unsigned decimal value.

## [](#SEE_ALSO)SEE ALSO

           tc(8)

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

    iproute2                       11 Jan 201C6onnmark retr...r action in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc-actions(8)](../man8/tc-actions.8.html),  [tc-ctinfo(8)](../man8/tc-ctinfo.8.html)

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
