---
{"title": "tc-tbf(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-tbf.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-tbf(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ALGORITHM](#ALGORITHM) \| [PARAMETERS](#PARAMETERS) \| [EXAMPLE & USAGE](#EXAMPLE_&_USAGE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TC(8)                             Linux                             TC(8)

## [](#NAME)NAME

           tbf - Token Bucket Filter

## [](#SYNOPSIS)SYNOPSIS

           tc qdisc ... tbf rate rate burst bytes/cell ( latency ms | limit
           bytes ) [ mpu bytes [ peakrate rate mtu bytes/cell ] ]

           burst is also known as buffer and maxburst. mtu is also known as
           minburst.

## [](#DESCRIPTION)DESCRIPTION

           The Token Bucket Filter is a classful queueing discipline
           available for traffic control with the tc(8) command.

           TBF is a pure shaper and never schedules traffic. It is non-work-
           conserving and may throttle itself, although packets are
           available, to ensure that the configured rate is not exceeded.  It
           is able to shape up to 1mbit/s of normal traffic with ideal
           minimal burstiness, sending out data exactly at the configured
           rates.

           Much higher rates are possible but at the cost of losing the
           minimal burstiness. In that case, data is on average dequeued at
           the configured rate but may be sent much faster at millisecond
           timescales. Because of further queues living in network adaptors,
           this is often not a problem.

## [](#ALGORITHM)ALGORITHM

           As the name implies, traffic is filtered based on the expenditure
           of tokens.  Tokens roughly correspond to bytes, with the
           additional constraint that each packet consumes some tokens, no
           matter how small it is. This reflects the fact that even a zero-
           sized packet occupies the link for some time.

           On creation, the TBF is stocked with tokens which correspond to
           the amount of traffic that can be burst in one go. Tokens arrive
           at a steady rate, until the bucket is full.

           If no tokens are available, packets are queued, up to a configured
           limit. The TBF now calculates the token deficit, and throttles
           until the first packet in the queue can be sent.

           If it is not acceptable to burst out packets at maximum speed, a
           peakrate can be configured to limit the speed at which the bucket
           empties. This peakrate is implemented as a second TBF with a very
           small bucket, so that it doesn't burst.

           To achieve perfection, the second bucket may contain only a single
           packet, which leads to the earlier mentioned 1mbit/s limit.

           This limit is caused by the fact that the kernel can only throttle
           for at minimum 1 'jiffy', which depends on HZ as 1/HZ. For perfect
           shaping, only a single packet can get sent per jiffy - for HZ=100,
           this means 100 packets of on average 1000 bytes each, which
           roughly corresponds to 1mbit/s.

## [](#PARAMETERS)PARAMETERS

           See tc(8) for how to specify the units of these values.

           limit or latency
                  Limit is the number of bytes that can be queued waiting for
                  tokens to become available. You can also specify this the
                  other way around by setting the latency parameter, which
                  specifies the maximum amount of time a packet can sit in
                  the TBF. The latter calculation takes into account the size
                  of the bucket, the rate and possibly the peakrate (if set).
                  These two parameters are mutually exclusive.

           burst  Also known as buffer or maxburst.  Size of the bucket, in
                  bytes. This is the maximum amount of bytes that tokens can
                  be available for instantaneously.  In general, larger
                  shaping rates require a larger buffer. For 10mbit/s on
                  Intel, you need at least 10kbyte buffer if you want to
                  reach your configured rate!

                  If your buffer is too small, packets may be dropped because
                  more tokens arrive per timer tick than fit in your bucket.
                  The minimum buffer size can be calculated by dividing the
                  rate by HZ.

                  Token usage calculations are performed using a table which
                  by default has a resolution of 8 packets.  This resolution
                  can be changed by specifying the cell size with the burst.
                  For example, to specify a 6000 byte buffer with a 16 byte
                  cell size, set a burst of 6000/16. You will probably never
                  have to set this. Must be an integral power of 2.

           mpu    A zero-sized packet does not use zero bandwidth. For
                  ethernet, no packet uses less than 64 bytes. The Minimum
                  Packet Unit determines the minimal token usage (specified
                  in bytes) for a packet. Defaults to zero.

           rate   The speed knob. See remarks above about limits! See tc(8)
                  for units.

           Furthermore, if a peakrate is desired, the following parameters
           are available:

           peakrate
                  Maximum depletion rate of the bucket. The peakrate does not
                  need to be set, it is only necessary if perfect millisecond
                  timescale shaping is required.

           mtu/minburst
                  Specifies the size of the peakrate bucket. For perfect
                  accuracy, should be set to the MTU of the interface.  If a
                  peakrate is needed, but some burstiness is acceptable, this
                  size can be raised. A 3000 byte minburst allows around
                  3mbit/s of peakrate, given 1000 byte packets.

                  Like the regular burstsize you can also specify a cell
                  size.

## [](#EXAMPLE_&_USAGE)EXAMPLE & USAGE

           To attach a TBF with a sustained maximum rate of 0.5mbit/s, a
           peakrate of 1.0mbit/s, a 5kilobyte buffer, with a pre-bucket queue
           size limit calculated so the TBF causes at most 70ms of latency,
           with perfect peakrate behaviour, issue:

           # tc qdisc add dev eth0 handle 10: root tbf rate 0.5mbit \
             burst 5kb latency 70ms peakrate 1mbit       \
             minburst 1540

           To attach an inner qdisc, for example sfq, issue:

           # tc qdisc add dev eth0 parent 10:1 handle 100: sfq

           Without inner qdisc TBF queue acts as bfifo. If the inner qdisc is
           changed the limit/latency is not effective anymore.

## [](#SEE_ALSO)SEE ALSO

           tc(8)

## [](#AUTHOR)AUTHOR

           Alexey N. Kuznetsov, <kuznet@ms2.inr.ac.ru>. This manpage
           maintained by bert hubert <ahu@ds9a.nl>

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

    iproute2                     13 December 2001                       TC(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc(8)](../man8/tc.8.html),  [tc-htb(8)](../man8/tc-htb.8.html),  [tc-prio(8)](../man8/tc-prio.8.html)

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
