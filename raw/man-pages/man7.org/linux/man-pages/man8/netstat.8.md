---
{"title": "netstat(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/netstat.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# netstat(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [NOTES](#NOTES) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OUTPUT](#OUTPUT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NETSTAT(8)         Linux System Administrator's Manual         NETSTAT(8)

## [](#NAME)NAME

           netstat - print network connections, routing tables, interface
           statistics, masquerade connections, and multicast memberships

## [](#SYNOPSIS)SYNOPSIS

           netstat [address_family_options] [--tcp|-t] [--udp|-u]
                   [--udplite|-U] [--sctp|-S] [--raw|-w] [--l2cap|-2]
                   [--rfcomm|-f] [--listening|-l] [--all|-a] [--numeric|-n]
                   [--numeric-hosts] [--numeric-ports] [--numeric-users]
                   [--symbolic|-N] [--extend|-e|-ee] [--timers|-o]
                   [--program|-p] [--verbose|-v] [--continuous|-c]
                   [--wide|-W]

           netstat {--route|-r} [address_family_options] [--extend|-e|-ee]
                   [--verbose|-v] [--numeric|-n] [--numeric-hosts]
                   [--numeric-ports] [--numeric-users] [--continuous|-c]

           netstat {--interfaces|-i} [--all|-a] [--extend|-e] [--numeric|-n]
                   [--numeric-hosts] [--continuous|-c]

           netstat {--groups|-g} [--numeric|-n] [--numeric-hosts]
                   [--numeric-ports] [--numeric-users] [--continuous|-c]

           netstat {--masquerade|-M} [--extend|-e] [--numeric|-n]
                   [--numeric-hosts] [--numeric-ports] [--numeric-users]
                   [--continuous|-c]

           netstat {--statistics|-s} [--tcp|-t] [--udp|-u] [--udplite|-U]
                   [--sctp|-S] [--raw|-w]

           netstat {--version|-V}
           netstat {--help|-h}

           address_family_options:
           [-4|--inet] [-6|--inet6] [--protocol={inet,inet6,unix,ipx,
           ax25,netrom,ddp,bluetooth, ... } ] [--unix|-x] [--inet|--ip]
           [--ax25] [--x25] [--rose] [--ash] [--bluetooth] [--ipx] [--netrom]
           [--ddp|--appletalk] [--econet|--ec]

## [](#NOTES)NOTES

           This  program  is mostly obsolete.  Replacement for netstat is ss.
           Replacement for netstat -r is ip route.  Replacement  for  netstat
           -i is ip -s link.  Replacement for netstat -g is ip maddr.

## [](#DESCRIPTION)DESCRIPTION

           Netstat prints information about the Linux networking subsystem.

       Invocation Mode
           The  type  of information printed is controlled by the first argu‐
           ment, as follows:

           (none) By default, netstat displays a list of open sockets.  If
                  you don't specify any address families, then the active
                  sockets of all configured address families will be printed.

           --route, -r
                  Display the kernel routing tables. See the description in
                  route(8) for details.  netstat -r and route -e produce the
                  same output.

           --groups, -g
                  Display multicast group membership information for IPv4 and
                  IPv6.

           --interfaces, -i
                  Display a table of all network interfaces and their respec‐
                  tive reception and transmission errors counters. Without
                  the --extended option it produces same output as ifconfig
                  -s, otherwise the detailed list.

           --masquerade, -M
                  Display a list of masqueraded connections.

           --statistics, -s
                  Display summary (SNMP) statistics for each protocol.

## [](#OPTIONS)OPTIONS

           --verbose, -v
                  Tell the user what is going on by being verbose. Especially
                  print some useful information about unconfigured address
                  families.

           --wide, -W
                  Do not truncate addresses by using output as wide as need‐
                  ed. This is optional for now to not break existing scripts.

           --numeric, -n
                  Show numerical addresses instead of trying to determine
                  symbolic host, port or user names.

           --numeric-hosts
                  shows numerical host addresses but does not affect the res‐
                  olution of port or user names.

           --numeric-ports
                  shows numerical port numbers but does not affect the reso‐
                  lution of host or user names.

           --numeric-users
                  shows numerical user IDs but does not affect the resolution
                  of host or port names.

           --protocol=Family, -A Family
                  Specifies the address families (perhaps better described as
                  low level protocols) for which connections are to be shown.
                  Family is a comma (',') separated list of address family
                  keywords like inet, inet6, unix, ipx, ax25, netrom, econet,
                  ddp, and bluetooth.
                  This has the same effect as using the --inet|-4, --in‐
                  et6|-6, --unix|-x, --ipx, --ax25, --netrom, --ddp, and
                  --bluetooth options.

                  The address family inet (IPv4) includes raw, udp, udplite
                  and tcp protocol sockets.

                  The address family bluetooth includes l2cap and rfcomm pro‐
                  tocol sockets.

           -c, --continuous
                  This will cause netstat to print the selected information
                  every second continuously.

           -e, --extend
                  Display additional information.  Use this option twice for
                  maximum detail.

           -o, --timers
                  Include information related to networking timers.

           -p, --program
                  Show the PID and name of the program (this is not trustwor‐
                  thy) to which each socket belongs.  A hyphen is shown if
                  the user has no permission to inspect the other process, or
                  if the socket belongs to the kernel (e.g. a kernel service,
                  or the process has exited but the socket hasn't finished
                  closing yet).

           -l, --listening
                  Show only listening sockets.  (These are omitted by de‐
                  fault.)

           -a, --all
                  Show both listening and non-listening sockets.  With the
                  --interfaces option, show interfaces that are not up.

           -F     Print routing information from the FIB.  (This is the de‐
                  fault.)

           -C     Print routing information from the route cache.  (The cache
                  is no longer provided with Linux kernel 3.6).

## [](#OUTPUT)OUTPUT

       Active Internet connections (TCP, UDP, UDPLite, raw)
           Proto  The protocol (tcp, udp, udpl, raw) used by the socket.

           Recv-Q Established: The count of bytes not copied by the user pro‐
                  gram connected to this socket.
                  Listening: Since Kernel 2.6.18 this column contains the
                  current accept queue.

           Send-Q Established: The count of bytes not acknowledged by the re‐
                  mote host.
                  Listening: Since Kernel 2.6.18 this column contains the
                  maximum size of the syn backlog.

           Local Address
                  Address and port number of the local end of the socket.
                  Unless the --numeric (-n) option is specified, the socket
                  address is resolved to its canonical host name (FQDN), and
                  the port number is translated into the corresponding ser‐
                  vice name.

           Foreign Address
                  Address and port number of the remote end of the socket.
                  Analogous to "Local Address".

           State  The state of the socket. Since there are no states in raw
                  mode and usually no states used in UDP and UDPLite, this
                  column may be left blank.  Normally this can be one of sev‐
                  eral values:

                  ESTABLISHED
                         The socket has an established connection.

                  SYN_SENT
                         The socket is actively attempting to establish a
                         connection.

                  SYN_RECV
                         A connection request has been received from the net‐
                         work.

                  FIN_WAIT1
                         The socket is closed, and the connection is shutting
                         down.

                  FIN_WAIT2
                         Connection is closed, and the socket is waiting for
                         a shutdown from the remote end.

                  TIME_WAIT
                         The socket is waiting after close to handle packets
                         still in the network.

                  CLOSE  The socket is not being used.

                  CLOSE_WAIT
                         The remote end has shut down, waiting for the socket
                         to close.

                  LAST_ACK
                         The remote end has shut down, and the socket is
                         closed. Waiting for acknowledgement.

                  LISTEN The socket is listening for incoming connections.
                         Such sockets are not included in the output unless
                         you specify the --listening (-l) or --all (-a) op‐
                         tion.

                  CLOSING
                         Both sockets are shut down but we still don't have
                         all our data sent.

                  UNKNOWN
                         The state of the socket is unknown.

           User   The username or the user id (UID) of the owner of the sock‐
                  et.

           PID/Program name
                  Slash-separated pair of the process id (PID) and process
                  name of the process that owns the socket.  --program causes
                  this column to be included.  You will also need superuser
                  privileges to see this information on sockets you don't
                  own.  This identification information is not yet available
                  for IPX sockets.

           Timer  TCP timer associated with this socket. The format is
                  timer(a/b/c).  The timer is one of the following values:

                  off    There is no timer set for this socket.

                  on     The retransmission timer is active for the socket.

                  keepalive
                         The keepalive timer is active for the socket.

                  timewait
                         The connection is closing and the timewait timer is
                         active for the socket.

                         The values in the brackets:

                         a      Timer value.

                         b      Number of retransmissions sent.

                         c      Number of keepalives sent.

       Active UNIX domain Sockets
           Proto  The protocol (usually unix) used by the socket.

           RefCnt The reference count (i.e. attached processes via this sock‐
                  et).

           Flags  The flags displayed is SO_ACCEPTON (displayed as ACC),
                  SO_WAITDATA (W) or SO_NOSPACE (N).  SO_ACCECPTON is used on
                  unconnected sockets if their corresponding processes are
                  waiting for a connect request.  The other flags are not of
                  normal interest.

           Type   There are several types of socket access:

                  SOCK_DGRAM
                         The socket is used in Datagram (connectionless)
                         mode.

                  SOCK_STREAM
                         This is a stream (connection) socket.

                  SOCK_RAW
                         The socket is used as a raw socket.

                  SOCK_RDM
                         This one serves reliably-delivered messages.

                  SOCK_SEQPACKET
                         This is a sequential packet socket.

                  SOCK_PACKET
                         Raw interface access socket.

                  UNKNOWN
                         Who ever knows what the future will bring us - just
                         fill in here :-)

           State  This field will contain one of the following keywords:

                  FREE   The socket is not allocated

                  LISTENING
                         The socket is listening for a connection request.
                         Such sockets are only included in the output if you
                         specify the --listening (-l) or --all (-a) option.

                  CONNECTING
                         The socket is about to establish a connection.

                  CONNECTED
                         The socket is connected.

                  DISCONNECTING
                         The socket is disconnecting.

                  (empty)
                         The socket is not connected to another one.

                  UNKNOWN
                         This state should never happen.

           PID/Program name
                  Process ID (PID) and process name of the process that has
                  the socket open.  More info available in Active Internet
                  connections section written above.

           Path   This is the path name as which the corresponding processes
                  attached to the socket.

       Active IPX sockets
           (this needs to be done by somebody who knows it)

       Active NET/ROM sockets
           (this needs to be done by somebody who knows it)

       Active AX.25 sockets
           (this needs to be done by somebody who knows it)

       Kernel Interface table (-i)
           Output format depends on the --extended flag.  if not specified
           the output is compatible to the short ifconfig -s statistics ta‐
           ble, otherwise the detailed interface list is used.  Both docu‐
           mented in ifconfig(8).

       Kernel IP routing table (-r)
           Output format depends on the --extended flags.  If not specified
           the output is the same as route -e.  If one is specified, the out‐
           put is the same as route default format.  If the extended option
           is specified twice, the output is same as route -ee.  All three
           documented in route(8).

## [](#FILES)FILES

           /etc/services -- The services translation file

           /proc -- Mount point for the proc filesystem, which gives access
           to kernel status information via the following files.

           /proc/net/dev -- device information

           /proc/net/raw -- raw socket information

           /proc/net/tcp -- TCP socket information

           /proc/net/udp -- UDP socket information

           /proc/net/udplite -- UDPLite socket information

           /proc/net/igmp -- IGMP multicast information

           /proc/net/unix -- Unix domain socket information

           /proc/net/ipx -- IPX socket information

           /proc/net/ax25 -- AX25 socket information

           /proc/net/appletalk -- DDP (appletalk) socket information

           /proc/net/nr -- NET/ROM socket information

           /proc/net/route -- IP routing information

           /proc/net/ax25_route -- AX25 routing information

           /proc/net/ipx_route -- IPX routing information

           /proc/net/nr_nodes -- NET/ROM nodelist

           /proc/net/nr_neigh -- NET/ROM neighbours

           /proc/net/ip_masquerade -- masqueraded connections

           /sys/kernel/debug/bluetooth/l2cap -- Bluetooth L2CAP information

           /sys/kernel/debug/bluetooth/rfcomm -- Bluetooth serial connections

           /proc/net/snmp -- statistics

## [](#EXAMPLES)EXAMPLES

           List all open TCP and UDP ports, with the corresponding process's
           PID (requires root).  This lets you answer "which process is lis‐
           tening on port 8080?":

                  netstat -tulpn

           Show the route table (it's often best to pass -n to display IP ad‐
           dresses rather than hostnames):

                  netstat -rn

## [](#BUGS)BUGS

           Occasionally strange information may appear if a socket changes as
           it is viewed. This is unlikely to occur.

           The performance when listing large number of sockets on busy
           servers is low, use the netlink(7) based ss(8) command instead.

## [](#SEE_ALSO)SEE ALSO

           Homepage of the net-tools project: 
           ⟨https://net-tools.sourceforge.io⟩

           route(8), ifconfig(8), iptables(8), ss(8), ip(8)
           proc(5)

## [](#AUTHORS)AUTHORS

           The netstat user interface was written by Fred Baumgarten
           <dc6iq@insu1.etec.uni-karlsruhe.de>, the man page by Matt Welsh
           <mdw@tc.cornell.edu>.  It was updated by Alan Cox
           <Alan.Cox@linux.org>, Tuan Hoang <tqhoang@yahoo.com>, and Bernd
           Eckenfels <net-tools@lina.inka.de>.  UDPLite options were added by
           Brian Micek <bmicek@gmail.com>.

## [](#COLOPHON)COLOPHON

           This page is part of the net-tools (networking utilities) project.
           Information about the project can be found at 
           ⟨http://net-tools.sourceforge.net/⟩.  If you have a bug report for
           this manual page, see ⟨http://net-tools.sourceforge.net/⟩.  This
           page was obtained from the project's upstream Git repository
           ⟨git://git.code.sf.net/p/net-tools/code⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-12.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    net-tools                       2026-05-10                     NETSTAT(8)

------------------------------------------------------------------------

Pages that refer to this page: [networks(5)](../man5/networks.5.html),  [proc(5)](../man5/proc.5.html),  [proc_pid_net(5)](../man5/proc_pid_net.5.html),  [icmp(7)](../man7/icmp.7.html),  [arp(8)](../man8/arp.8.html),  [ifconfig(8)](../man8/ifconfig.8.html),  [netcap(8)](../man8/netcap.8.html),  [rarp(8)](../man8/rarp.8.html),  [route(8)](../man8/route.8.html),  [traceroute(8)](../man8/traceroute.8.html)

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
