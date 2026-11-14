---
{"title": "astraceroute(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/astraceroute.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# astraceroute(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [USAGE EXAMPLE](#USAGE_EXAMPLE) \| [NOTE](#NOTE) \| [BUGS](#BUGS) \| [LEGAL](#LEGAL) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ASTRACEROUTE(8)            netsniff-ng toolkit            ASTRACEROUTE(8)

## [](#NAME)NAME

           astraceroute - autonomous system trace route utility

## [](#SYNOPSIS)SYNOPSIS

           astraceroute [options]

## [](#DESCRIPTION)DESCRIPTION

           astraceroute is a small utility to retrieve path information in a
           traceroute like way, but with additional geographical location
           information. It tracks the route of a packet from the local host
           to the remote host by successively increasing the IP's TTL field,
           starting from 1, in the hope that each intermediate node will send
           an ICMP TIME_EXCEEDED notification back to the local host when the
           TTL value is decremented to 0.

           astraceroute supports IPv4 and IPv6 queries and will display
           country and city information, if available, the AS number the hop
           belongs to, and its ISP name. astraceroute also displays timing
           information and reverse DNS data.

           Due to astraceroute's configurability, it is also possible to
           gather some more useful information about the hop regarding what
           it does and does not allow to pass through. This is done by using
           clear text strings for probing DPIs or ``great firewalls'' to
           determine if they will filter out blocked critical keywords. This
           tool might be a good start for further in-depth analysis of such
           systems.

## [](#OPTIONS)OPTIONS

           -H <host>, --host <host>
                  Hostname or IPv4 or IPv6 address of the remote host where
                  the AS route should be traced to. In the case of an IPv6
                  address or host, option -6 must be used. IPv4 is the
                  default.

           -p <port>, --port <port>
                  TCP port for the remote host to use. If not specified, the
                  default port used is 80.

           -i <device>, -d <device>, --dev <device>
                  Networking device to start the trace route from, e.g. eth0,
                  wlan0.

           -b <IP>, --bind <IP>
                  IP address to bind to other than the network device's
                  address. You must specify -6 for an IPv6 address.

           -f <ttl>, --init-ttl <ttl>
                  Initial TTL value to be used. This option might be useful
                  if you are not interested in the first n hops, but only the
                  following ones. The default initial TTL value is 1.

           -m <ttl>, --max-ttl <ttl>
                  Maximum TTL value to be used. If not otherwise specified,
                  the maximum TTL value is 30. Thus, after this has been
                  reached astraceroute exits.

           -q <num>, --num-probes <num>
                  Specifies the number of queries to be done on a particular
                  hop. The default is 2 query requests.

           -x <sec>, --timeout <sec>
                  Tells astraceroute the probe response timeout in seconds,
                  in other words the maximum time astraceroute must wait for
                  an ICMP response from the current hop. The default is 3
                  seconds.

           -X <string>, --payload <string>
                  Places an ASCII cleartext string into the packet payload.
                  Cleartext that contains whitespace must be put into quotes
                  (e.g.: "censor me").

           -l <len>, --totlen <len>
                  Specifies the total length of the packet. Payload that does
                  not have a cleartext string in it is padded with random
                  garbage.

           -4, --ipv4
                  Use IPv4 only requests. This is the default.

           -6, --ipv6
                  Use IPv6 only requests. This must be used when passing an
                  IPv6 host as an argument.

           -n, --numeric
                  Tells astraceroute to not perform reverse DNS lookup for
                  hop replies. The reverse option is -N.

           -u, --update
                  The built-in geo-database update mechanism will be invoked
                  to get Maxmind's latest version. To configure search
                  locations for databases, the file /etc/netsniff-
                  ng/geoip.conf contains possible addresses. Thus, to save
                  bandwidth or for mirroring Maxmind's databases (to bypass
                  their traffic limit policy), different hosts or IP
                  addresses can be placed into geoip.conf, separated by a
                  newline.

           -L, --latitude
                  Also show latitude and longitude of hops.

           -N, --dns
                  Tells astraceroute to perform reverse DNS lookup for hop
                  replies. The reverse option is -n.

           -S, --syn
                  Use TCP's SYN flag for the request.

           -A, --ack
                  Use TCP's ACK flag for the request.

           -F, --fin
                  Use TCP's FIN flag for the request.

           -P, --psh
                  Use TCP's PSH flag for the request.

           -U, --urg
                  Use TCP's URG flag for the request.

           -R, --rst
                  Use TCP's RST flag for the request.

           -E, --ecn-syn
                  Use TCP's ECN flag for the request.

           -t <tos>, --tos <tos>
                  Explicitly specify IP's TOS.

           -G, --nofrag
                  Set IP's no fragmentation flag.

           -Z, --show-packet
                  Show and dissect the returned packet.

           -v, --version
                  Show version information and exit.

           -h, --help
                  Show user help and exit.

## [](#USAGE_EXAMPLE)USAGE EXAMPLE

           astraceroute -i eth0 -N -S -H netsniff-ng.org
                  This sends out a TCP SYN probe via the ''eth0'' networking
                  device to the remote IPv4 host netsniff-ng.org. This
                  request is most likely to pass. Also, tell astraceroute to
                  perform reverse DNS lookups for each hop.

           astraceroute -6 -i eth0 -S -E -N -H www.6bone.net
                  In this example, a TCP SYN/ECN probe for the IPv6 host
                  www.6bone.net is being performed. Also in this case, the
                  ''eth0'' device is being used as well as a reverse DNS
                  lookup for each hop.

           astraceroute -i eth0 -N -F -H netsniff-ng.org
                  Here, we send out a TCP FIN probe to the remote host
                  netsniff-ng.org. Again, on each hop a reverse DNS lookup is
                  being done and the queries are transmitted from ''eth0''.
                  IPv4 is used.

           astraceroute -i eth0 -N -FPU -H netsniff-ng.org
                  As in most other examples, we perform a trace route to IPv4
                  host netsniff-ng.org and do a TCP Xmas probe this time.

           astraceroute -i eth0 -N -H netsniff-ng.org -X censor-me -Z
                  In this example, we have a Null probe to the remote host
                  netsniff-ng.org, port 80 (default) and this time, we append
                  the cleartext string "censor-me" into the packet payload to
                  test if a firewall or DPI will let this string pass. Such a
                  trace could be done once without and once with a blocked
                  string to gather possible information about censorship.

## [](#NOTE)NOTE

           If a TCP-based probe fails after a number of retries, astraceroute
           will automatically fall back to ICMP-based probes to pass through
           firewalls and routers used in load balancing for example.

           To gather more information about astraceroute's displayed AS
           numbers, see e.g.: http://bgp.he.net/AS<number>.

## [](#BUGS)BUGS

           The geographical locations are estimated with the help of
           Maxmind's GeoIP database and can differ from the real physical
           location. To decrease the possible errors, update the database
           regularly using astraceroute's --update option.

           At some point in time, we need a similar approach to gather more
           reliable path information such as in the paris-traceroute tool.

           Due to the generic nature of astraceroute, it currently has a
           built-in mechanism to stop the trace after a fixed number of hops,
           since the configurable TCP flags can have anything included. It is
           possible to decrease this number of course.  In the future, if a
           SYN probe is sent out, there should be a listener so that we can
           stop the trace if we detect a handshake in progress.

## [](#LEGAL)LEGAL

           astraceroute is licensed under the GNU GPL version 2.0.

## [](#HISTORY)HISTORY

           astraceroute was originally written for the netsniff-ng toolkit by
           Daniel Borkmann. It is currently maintained by Tobias Klauser
           <tklauser@distanz.ch> and Daniel Borkmann
           <dborkma@tik.ee.ethz.ch>.

## [](#SEE_ALSO)SEE ALSO

           netsniff-ng(8), trafgen(8), mausezahn(8), ifpps(8), bpfc(8),
           flowtop(8), curvetun(8)

## [](#AUTHOR)AUTHOR

           Manpage was written by Daniel Borkmann.

## [](#COLOPHON)COLOPHON

           This page is part of the Linux netsniff-ng toolkit project. A
           description of the project, and information about reporting bugs,
           can be found at http://netsniff-ng.org/.

## [](#COLOPHON)COLOPHON

           This page is part of the netsniff-ng (a free Linux networking
           toolkit) project.  Information about the project can be found at
           ⟨http://netsniff-ng.org/⟩.  If you have a bug report for this
           manual page, send it to netsniff-ng@googlegroups.com.  This page
           was obtained from the project's upstream Git repository
           ⟨https://github.com/netsniff-ng/netsniff-ng⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2025-06-11.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux                         03 March 2013               ASTRACEROUTE(8)

------------------------------------------------------------------------

Pages that refer to this page: [bpfc(8)](../man8/bpfc.8.html),  [curvetun(8)](../man8/curvetun.8.html),  [flowtop(8)](../man8/flowtop.8.html),  [ifpps(8)](../man8/ifpps.8.html),  [mausezahn(8)](../man8/mausezahn.8.html),  [netsniff-ng(8)](../man8/netsniff-ng.8.html),  [trafgen(8)](../man8/trafgen.8.html)

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
