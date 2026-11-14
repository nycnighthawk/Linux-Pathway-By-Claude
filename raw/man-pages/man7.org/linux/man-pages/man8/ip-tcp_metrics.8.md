---
{"title": "ip-tcp_metrics(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-tcp_metrics.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-tcp_metrics(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-TCP_METRICS(8)                 Linux                 IP-TCP_METRICS(8)

## [](#NAME)NAME

           ip-tcp_metrics - management for TCP Metrics

## [](#SYNOPSIS)SYNOPSIS

           ip [ OPTIONS ] tcp_metrics { COMMAND | help }

           ip tcp_metrics { show | flush } SELECTOR

           ip tcp_metrics delete [ address ] ADDRESS

           SELECTOR := [ [ address ] PREFIX ]

## [](#DESCRIPTION)DESCRIPTION

           ip tcp_metrics is used to manipulate entries in the kernel that
           keep TCP information for IPv4 and IPv6 destinations. The entries
           are created when TCP sockets want to share information for
           destinations and are stored in a cache keyed by the destination
           address. The saved information may include values for metrics
           (initially obtained from routes), recent TSVAL for TIME-WAIT
           recycling purposes, state for the Fast Open feature, etc.  For
           performance reasons the cache can not grow above configured limit
           and the older entries are replaced with fresh information,
           sometimes reclaimed and used for new destinations. The kernel
           never removes entries, they can be flushed only with this tool.

       ip tcp_metrics show - show cached entries
           address PREFIX (default)
                  IPv4/IPv6 prefix or address. If no prefix is provided all
                  entries are shown.

           The output may contain the following information:

           age <S.MMM>sec - time after the entry was created, reset or
           updated with metrics from sockets. The entry is reset and
           refreshed on use with metrics from route if the metrics are not
           updated in last hour. Not all cached values reset the age on
           update.

           cwnd <N> - CWND metric value

           fo_cookie <HEX-STRING> - Cookie value received in SYN-ACK to be
           used by Fast Open for next SYNs

           fo_mss <N> - MSS value received in SYN-ACK to be used by Fast Open
           for next SYNs

           fo_syn_drops <N>/<S.MMM>sec ago - Number of drops of initial
           outgoing Fast Open SYNs with data detected by monitoring the
           received SYN-ACK after SYN retransmission.  The seconds show the
           time after last SYN drop and together with the drop count can be
           used to disable Fast Open for some time.

           reordering <N> - Reordering metric value

           rtt <N>us - RTT metric value

           rttvar <N>us - RTTVAR metric value

           ssthresh <SSTHRESH> - SSTHRESH metric value

           tw_ts <TSVAL>/<SEC>sec ago - recent TSVAL and the seconds after
           saving it into TIME-WAIT socket

       ip tcp_metrics delete - delete single entry
           address ADDRESS (default)
                  IPv4/IPv6 address. The address is a required argument.

       ip tcp_metrics flush - flush entries
           This command flushes the entries selected by some criteria.

           This command has the same arguments as show.

## [](#EXAMPLES)EXAMPLES

           ip tcp_metrics show address 192.168.0.0/24
               Shows the entries for destinations from subnet

           ip tcp_metrics show 192.168.0.0/24
               The same but address keyword is optional

           ip tcp_metrics
               Show all is the default action

           ip tcp_metrics delete 192.168.0.1
               Removes the entry for 192.168.0.1 from cache.

           ip tcp_metrics flush 192.168.0.0/24
               Removes entries for destinations from subnet

           ip tcp_metrics flush all
               Removes all entries from cache

           ip -6 tcp_metrics flush all
               Removes all IPv6 entries from cache keeping the IPv4 entries.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           Original Manpage by Julian Anastasov <ja@ssi.bg>

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

    iproute2                       23 Aug 2012              IP-TCP_METRICS(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html)

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
