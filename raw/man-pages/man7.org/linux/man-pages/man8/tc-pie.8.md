---
{"title": "tc-pie(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-pie.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-pie(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ALGORITHM](#ALGORITHM) \| [PARAMETERS](#PARAMETERS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [SOURCES](#SOURCES) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PIE(8)                            Linux                            PIE(8)

## [](#NAME)NAME

           PIE - Proportional Integral controller-Enhanced AQM algorithm

## [](#SYNOPSIS)SYNOPSIS

           tc qdisc ... pie [ limit PACKETS ] [ target TIME ] [ tupdate TIME
           ] [ alpha int ] [ beta int ] [ ecn | noecn ] [ bytemode |
           nobytemode ] [ dq_rate_estimator | no_dq_rate_estimator ]

## [](#DESCRIPTION)DESCRIPTION

           Proportional Integral controller-Enhanced (PIE) is a control
           theoretic active queue management scheme. It is based on the
           proportional integral controller but aims to control delay. The
           main design goals are
            o Low latency control
            o High link utilization
            o Simple implementation
            o Guaranteed stability and fast responsiveness

## [](#ALGORITHM)ALGORITHM

           PIE is designed to control delay effectively. First, an average
           dequeue rate is estimated based on the standing queue. The rate is
           used to calculate the current delay. Then, on a periodic basis,
           the delay is used to calculate the dropping probability. Finally,
           on arrival, a packet is dropped (or marked) based on this
           probability.

           PIE makes adjustments to the probability based on the trend of the
           delay i.e.  whether it is going up or down.The delay converges
           quickly to the target value specified.

           alpha and beta are statically chosen parameters chosen to control
           the drop probability growth and are determined through control
           theoretic approaches. alpha determines how the deviation between
           the current and target latency changes probability. beta exerts
           additional adjustments depending on the latency trend.

           The drop probability is used to mark packets in ecn mode. However,
           as in RED, beyond 10% packets are dropped based on this
           probability. The bytemode is used to drop packets proportional to
           the packet size.

           Additional details can be found in the paper cited below.

## [](#PARAMETERS)PARAMETERS

       limit
           limit on the queue size in packets. Incoming packets are dropped
           when this limit is reached. Default is 1000 packets.

       target
           is the expected queue delay. The default target delay is 15ms.

       tupdate
           is the frequency at which the system drop probability is
           calculated. The default is 15ms.

       alpha
       beta
           alpha and beta are parameters chosen to control the drop
           probability. These should be in the range between 0 and 32.

       ecn | noecn
           is used to mark packets instead of dropping.  ecn to turn on ecn
           mode, noecn to turn off ecn mode. By default, ecn is turned off.

       bytemode | nobytemode
           is used to scale drop probability proportional to packet size.
           bytemode to turn on bytemode, nobytemode to turn off bytemode. By
           default, bytemode is turned off.

       dq_rate_estimator | no_dq_rate_estimator
           is used to calculate delay using Little's law.  dq_rate_estimator
           to turn on dq_rate_estimator, no_dq_rate_estimator to turn off
           no_dq_rate_estimator. By default, dq_rate_estimator is turned off.

## [](#EXAMPLES)EXAMPLES

            # tc qdisc add dev eth0 root pie
            # tc -s qdisc show
              qdisc pie 8036: dev eth0 root refcnt 2 limit 1000p target
           15.0ms tupdate 16.0ms alpha 2 beta 20
               Sent 31216108 bytes 20800 pkt (dropped 80, overlimits 0
           requeues 0)
               backlog 16654b 11p requeues 0
                prob 0.006161 delay 15666us
                pkts_in 20811 overlimit 0 dropped 80 maxq 50 ecn_mark 0

            # tc qdisc add dev eth0 root pie dq_rate_estimator
            # tc -s qdisc show
              qdisc pie 8036: dev eth0 root refcnt 2 limit 1000p target
           15.0ms tupdate 16.0ms alpha 2 beta 20
               Sent 63947420 bytes 42414 pkt (dropped 41, overlimits 0
           requeues 0)
               backlog 271006b 179p requeues 0
                prob 0.000092 delay 22200us avg_dq_rate 12145996
                pkts_in 41 overlimit 343 dropped 0 maxq 50 ecn_mark 0

            # tc qdisc add dev eth0 root pie limit 100 target 20ms tupdate
           30ms ecn
            # tc -s qdisc show
              qdisc pie 8036: dev eth0 root refcnt 2 limit 100p target 20.0ms
           tupdate 32.0ms alpha 2 beta 20 ecn
               Sent 6591724 bytes 4442 pkt (dropped 27, overlimits 0 requeues
           0)
               backlog 18168b 12p requeues 0
                prob 0.008845 delay 11348us
                pkts_in 4454 overlimit 0 dropped 27 maxq 65 ecn_mark 0

            # tc qdisc add dev eth0 root pie limit 100 target 50ms tupdate
           30ms bytemode
            # tc -s qdisc show
              qdisc pie 8036: dev eth0 root refcnt 2 limit 100p target 50.0ms
           tupdate 32.0ms alpha 2 beta 20 bytemode
               Sent 1616274 bytes 1137 pkt (dropped 0, overlimits 0 requeues
           0)
               backlog 13626b 9p requeues 0
                prob 0.000000 delay 0us
                pkts_in 1146 overlimit 0 dropped 0 maxq 23 ecn_mark 0

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-codel(8) tc-red(8)

## [](#SOURCES)SOURCES

            o RFC 8033: https://tools.ietf.org/html/rfc8033

## [](#AUTHORS)AUTHORS

           PIE was implemented by Vijay Subramanian and Mythili Prabhu, also
           the authors of this man page. Please report bugs and corrections
           to the Linux networking development mailing list at
           <netdev@vger.kernel.org>.

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

    iproute2                     16 January 2014                       PIE(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc(8)](../man8/tc.8.html),  [tc-dualpi2(8)](../man8/tc-dualpi2.8.html),  [tc-fq_pie(8)](../man8/tc-fq_pie.8.html)

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
