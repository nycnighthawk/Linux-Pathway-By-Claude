---
{"title": "tc-hfsc(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-hfsc.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-hfsc(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION (qdisc)](#DESCRIPTION_(qdisc)) \| [DESCRIPTION (class)](#DESCRIPTION_(class)) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    HFSC(8)                           Linux                           HFSC(8)

## [](#NAME)NAME

           HFSC - Hierarchical Fair Service Curve's control under linux

## [](#SYNOPSIS)SYNOPSIS

           tc qdisc add ... hfsc [ default CLASSID ]

           tc class add ... hfsc [ [ rt SC ] [ ls SC ] | [ sc SC ] ] [ ul SC ]

           rt : realtime service curve
           ls : linkshare service curve
           sc : rt+ls service curve
           ul : upperlimit service curve

           • at least one of rt, ls or sc must be specified
           • ul can only be specified with ls or sc

           SC := [ [ m1 BPS ] d SEC ] m2 BPS
                  m1 : slope of the first segment
                  d  : x-coordinate of intersection
                  m2 : slope of the second segment

           SC := [ [ umax BYTE ] dmax SEC ] rate BPS
                  umax : maximum unit of work
                  dmax : maximum delay
                  rate : rate

           For description of BYTE, BPS and SEC - please see UNITS section of
           tc(8).

## [](#DESCRIPTION_(qdisc))DESCRIPTION (qdisc)

           HFSC qdisc has only one optional parameter - default. CLASSID
           specifies the minor part of the default classid, where packets not
           classified by other means (e.g. u32 filter, CLASSIFY target of
           iptables) will be enqueued. If default is not specified,
           unclassified packets will be dropped.

## [](#DESCRIPTION_(class))DESCRIPTION (class)

           HFSC class is used to create a class hierarchy for HFSC scheduler.
           For explanation of the algorithm, and the meaning behind rt, ls,
           sc and ul service curves - please refer to tc-hfsc(7).

           As you can see in SYNOPSIS, service curve (SC) can be specified in
           two ways. Either as maximum delay for certain amount of work, or
           as a bandwidth assigned for certain amount of time. Obviously, m1
           is simply umax/dmax.

           Both m2 and rate are mandatory. If you omit other parameters, you
           will specify linear service curve.

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-hfsc(7), tc-stab(8)

           Please direct bugreports and patches to: <netdev@vger.kernel.org>

## [](#AUTHOR)AUTHOR

           Manpage created by Michal Soltys (soltys@ziu.info)

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

    iproute2                     31 October 2011                      HFSC(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc-hfsc(7)](../man7/tc-hfsc.7.html),  [tc(8)](../man8/tc.8.html),  [tc-stab(8)](../man8/tc-stab.8.html)

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
