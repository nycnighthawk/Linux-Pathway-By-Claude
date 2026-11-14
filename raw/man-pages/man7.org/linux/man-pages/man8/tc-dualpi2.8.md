---
{"title": "tc-dualpi2(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-dualpi2.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-dualpi2(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ALGORITHM](#ALGORITHM) \| [PARAMETERS](#PARAMETERS) \| [EXAMPLES](#EXAMPLES) \| [FILTERS](#FILTERS) \| [SEE ALSO](#SEE_ALSO) \| [SOURCES](#SOURCES) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DUALPI2(8)                        Linux                        DUALPI2(8)

## [](#NAME)NAME

           DUALPI2 - Dual Queue Proportional Integral Controller AQM -
           Improved with a square

## [](#SYNOPSIS)SYNOPSIS

           tc qdisc ... dualpi2
                   [ limit PACKETS ]
                   [ memlimit BYTES ]
                   [ coupling_factor NUMBER ]
                   [ step_thresh TIME|PACKETS ]
                   [ min_qlen_step PACKETS ]
                   [ drop_on_overload | overflow ]
                   [ drop_enqueue | drop_dequeue ]
                   [ l4s_ect | any_ect ]
                   [ classic_protection PERCENTAGE ]
                   [ max_rtt TIME  [ typical_rtt TIME ]]
                   [ target TIME ]
                   [ tupdate TIME ]
                   [ alpha float ]
                   [ beta float ]
                   [ split_gso | no_split_gso ]

## [](#DESCRIPTION)DESCRIPTION

           DUALPI2 AQM is a combination of the DUALQ Coupled-AQM with a PI2
           base-AQM. The PI2 AQM (details can be found in the paper cited
           below) is in turn both an extension and a simplification of the
           PIE AQM. PI2 makes quite some PIE heuristics unnecessary, while
           being able to control scalable congestion controls like TCP-
           Prague. With PI2, both Reno/Cubic can be used in parallel with
           Prague, maintaining window fairness. DUALQ provides latency
           separation between low latency Prague flows and Reno/Cubic flows
           that need a bigger queue. The main design goals are:
           •   L4S - Low Loss, Low Latency and Scalable congestion control
               support
           •   DualQ option to separate the L4S traffic in a low latency
               queue (L-queue), without harming remaining traffic that is
               scheduled in classic queue (C-queue) due to congestion-
               coupling
           •   Configurable overload strategies
           •   Use of sojourn time to reliably estimate queue delay
           •   Simple implementation
           •   Guaranteed stability and fast responsiveness

           The detailed PI2 parameters (alpha, beta, and tupdate) of DualPI2
           are hard to get right and typically give bad results if just tried
           or guessed. These parameters need to be calculated to a coherent
           set with a typical objective in mind. DualPI2 has a set of default
           parameters that can be used for the general Internet, where the
           maximum RTT is around 100ms and the typical RTT is around 15ms. It
           is highly recommended to use  max_rtt and  typical_rtt (or target)
           helper parameters if your deployment is deviating from the above
           objectives (e.g., in a data center). These helpers are used to
           provide the theoretically optimal PI2 parameters (alpha, beta, and
           tupdate) for those objectives, and that can be used as a basis for
           further finetuning, experimentation, and testing if desired.

## [](#ALGORITHM)ALGORITHM

           DUALPI2 is designed to provide low loss and low latency to L4S
           traffic, without harming classic traffic. Every update interval, a
           new internal base probability is calculated based on queue delay.
           The base probability is updated with a delta based on the
           difference between the current queue delay and the  target delay,
           and the queue growth compared with the queuing delay during the
           previous  tupdate interval. The integral gain factor alpha is used
           to correct slowly enough any persistent standing queue error to
           the user specified target delay, while the proportional gain
           factor beta is used to quickly compensate for queue changes
           (growth or shrink).

           The updated base probability is used as input to decide to mark
           and drop packets. DUALPI2 scales the calculated probability for
           each of the two queues accordingly. For the L-queue, the
           probability is multiplied by a coupling_factor , while for the C-
           queue, it is squared to compensate the squareroot rate equation of
           Reno/Cubic. The ECT identifier ( l4s_ect|any_ect ) is used to
           classify traffic into respective queues.

           If DUALPI2 AQM has detected overload (when excessive non-
           responsive traffic is sent), it can signal congestion solely using
           drop , irrespective of the ECN field, or alternatively limit the
           drop probability and let the queue grow and eventually overflow
           (like tail-drop).

           Additional details can be found in the RFC cited below.

## [](#PARAMETERS)PARAMETERS

           limit PACKETS
                  Limit the number of packets that can be enqueued. Incoming
                  packets will be dropped once this limit is reached. This
                  limit is common for the L-queue and C-queue. Defaults to
                  10000 packets. This is about 125ms delay on a 1Gbps link.

           memlimit BYTES
                  Limit the total amount of memory that can be used. Incoming
                  packets will be dropped once this memlimit is reached. This
                  memlimit is common for the L-queue and C-queue. Defaults to
                  10000 * interface MTU bytes.

           coupling_factor NUMBER
                  Set the coupling rate factor between Classic and L4S.
                  Defaults to 2

           l4s_ect|any_ect
                  Configures the ECT classifier. Packets whose ECT codepoint
                  matches this are sent to the L-queue, where they receive a
                  scalable marking. Defaults to l4s_ect , i.e., the L4S
                  identifier ECT(1). Setting this to any_ect causes all
                  packets whose ECN field is not zero to be sent to the L-
                  queue. This enables it to be backward compatible with,
                  e.g., DCTCP. Note DCTCP should only be used for intra-DC
                  traffic with very low RTTs and AQM delay targets bigger
                  than those RTTs, separated from Internet traffic (also if
                  Prague compliant CC), as it does not support all Prague
                  requirements that make sure that a congestion control can
                  work well with the range of RTTs on the Internet.

           step_thresh TIME | PACKETS
                  Set the step threshold for the L-queue. This will cause
                  packets with a sojourn time exceeding the threshold to
                  always be marked. This value can either be specified using
                  time units (i.e., us, ms, s), or in packets (p, pkt,
                  packet(s)). A value without units is assumed to be in time
                  (us). If defining the step in packets, be sure to disable
                  GRO on the ingress interfaces. Defaults to 1ms

           min_qlen_step PACKETS
                  Incoming packets enqueued to the L-queue may apply the step
                  threshold when the queue length of the L-queue exceeds this
                  value. Default to 0 packets. This means that every enqueued
                  packets to the L-queue with a sojourn time exceeds the step
                  threshold will be marked.

           drop_on_overload | overflow
                  Control the overload strategy.  drop_on_overload preserves
                  the delay in the L-queue by dropping in both queues on
                  overload.  overflow sacrifices delay to avoid losses,
                  eventually resulting in a taildrop behavior once the limit
                  is reached. Defaults to drop_on_overload

           drop_enqueue | drop_dequeue
                  Decide when packets are PI-based dropped or marked. The
                  step_thresh based L4S marking is always at dequeue.
                  Defaults to drop_dequeue

           classic_protection PERCENTAGE
                  Protects the C-queue from unresponsive traffic in the L-
                  queue. This bounds the maximal scheduling delay in the C-
                  queue to be (100 - PERCENTAGE) times greater than the one
                  in the L-queue. Defaults to 10

           typical_rtt TIME
           max_rtt TIME
                  Specify the maximum round trip time (RTT) and/or the
                  typical RTT of the traffic that will be controlled by
                  DUALPI2. These values are specified using time units (i.e.,
                  us, ms, s). A value without units is assumed to be in us.
                  If either max_rtt or typical_rtt is not specified, the
                  missing value will be computed from the following
                  relationship: max_rtt = typical_rtt * 6.  If any of these
                  parameters is given, it will be used to automatically
                  compute suitable values for alpha, beta, target, and
                  tupdate, according to the relationship from the appendix
                  A.1 in the IETF RFC cited below, to achieve a stable
                  control. Consequently, those derived values will override
                  their eventual user-provided ones. The default range of
                  operation for the qdisc uses max_rtt = 100ms and
                  typical_rtt = 15ms , which is suited to controlling
                  Internet traffic.

           target TIME
                  Set the expected queue delay. Defaults to 15 ms. A value
                  without units is assumed to be in us.

           tupdate TIME
                  Set the frequency at which the system drop probability is
                  calculated. Defaults to 16 ms. A value without units is
                  assumed to be in microseconds. This should be less than
                  one-third of the maximum RTT supported.

           alpha float
           beta float
                  Set alpha and beta, the integral and proportional gain
                  factors in Hz for the PI controller. These can be
                  calculated based on control theory. Defaults are 0.16 and
                  3.2 Hz, which provide stable control for RTT's up to 100ms
                  with tupdate of 16ms. Be aware, unlike with PIE, these are
                  the real unscaled gain factors. If not provided, they will
                  be automatically derived from typical_rtt and max_rtt , if
                  one of them or both are provided.

           split_gso | no_split_gso
                  Decide how to handle aggregated packets. Either treat the
                  aggregate as a single packet (thus all share fate with
                  respect to marks and drops) with no_split_gso , trading
                  some tail latency for CPU usage, or treat each packet
                  individually (i.e., split them) with split_gso to enable
                  fine-grained marking/dropping of packets to control
                  queueing latencies. Defaults to split_gso

## [](#EXAMPLES)EXAMPLES

           Setting DUALPI2 for the Internet with default parameters:
            # sudo tc qdisc add dev eth0 root dualpi2

           Setting DUALPI2 for datacenter with legacy DCTCP using ECT(0):
            # sudo tc qdisc add dev eth0 root dualpi2 any_ect

## [](#FILTERS)FILTERS

           This qdisc can be used in conjunction with tc-filters. More
           precisely, it will honor filters "stealing packets", as well as
           accept other classification schemes.

           Packets whose priority/classid are set to
                  1 will be enqueued in the L-queue, alongside L4S traffic,
                  and thus subject to the increased marking probability (or
                  drops if they are marked not-ECT).

           Packets whose priority/classid are set to
                  2 will also be enqueued in the L-queue, but will never be
                  dropped if they are not-ECT (unless the qdisc is full and
                  thus resorts to taildrop).

           Finally, all the other classid/priority map to the C-queue.

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-pie(8)

## [](#SOURCES)SOURCES

           •   IETF RFC9332 : https://datatracker.ietf.org/doc/html/rfc9332

           •   CoNEXT '16 Proceedings of the 12th International on Conference
               on emerging Networking Experiments and Technologies : "PI2: A
               Linearized AQM for both Classic and Scalable TCP"

## [](#AUTHORS)AUTHORS

           DUALPI2 was implemented by Koen De Schepper, Olga Albisser, Henrik
           Steen, Olivier Tilmans, and Chia-Yu Chang, also the authors of
           this man page. Please report bugs and corrections to the Linux
           networking development mailing list at <netdev@vger.kernel.org>.

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

    iproute2                       29 Oct 2024                     DUALPI2(8)

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
