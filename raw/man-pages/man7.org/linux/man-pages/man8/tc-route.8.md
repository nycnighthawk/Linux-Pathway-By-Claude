---
{"title": "tc-route(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-route.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-route(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Route classifier in tc(8)         Linux         Route classifier in tc(8)

## [](#NAME)NAME

           route - route traffic control filter

## [](#SYNOPSIS)SYNOPSIS

           tc filter ... route [ from REALM | fromif TAG ] [ to REALM ] [
                   classid CLASSID ] [ action ACTION_SPEC ]

## [](#DESCRIPTION)DESCRIPTION

           Match packets based on routing table entries. This filter centers
           around the possibility to assign a realm to routing table entries.
           For any packet to be classified by this filter, a routing table
           lookup is performed and the returned realm is used to decide on
           whether the packet is a match or not.

## [](#OPTIONS)OPTIONS

           action ACTION_SPEC
                  Apply an action from the generic actions framework on
                  matching packets.

           classid CLASSID
                  Push matching packets into the class identified by CLASSID.

           from REALM
           fromif TAG
                  Perform source route lookups.  TAG is the name of an
                  interface which must be present on the system at the time
                  of tc invocation.

           to REALM
                  Match if normal (i.e., destination) routing returns the
                  given REALM.

## [](#EXAMPLES)EXAMPLES

           Consider the subnet 192.168.2.0/24 being attached to eth0:

                  ip route add 192.168.2.0/24 dev eth0 realm 2

           The following route filter will then match packets from that
           subnet:

                  tc filter add ... route from 2 classid 1:2

           and pass packets on to class 1:2.

## [](#NOTES)NOTES

           Due to implementation details, realm values must be in a range
           from 0 to 255, inclusive. Alternatively, a verbose name defined in
           /etc/iproute2/rt_realms may be given instead.

## [](#SEE_ALSO)SEE ALSO

           tc(8), ip-route(8)

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

    iproute2                       21 Oct 2015      Route classifier in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc(8)](../man8/tc.8.html)

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
