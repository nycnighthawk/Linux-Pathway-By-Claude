---
{"title": "sctp(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/sctp.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sctp(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ADDRESS FORMATS](#ADDRESS_FORMATS) \| [SYSCTLS](#SYSCTLS) \| [STATISTICS](#STATISTICS) \| [CONTROL MSGS](#CONTROL_MSGS) \| [EVENTS and NOTIFICATIONS](#EVENTS_and_NOTIFICATIONS) \| [SOCKET OPTIONS](#SOCKET_OPTIONS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SCTP(7)                 Linux Programmer's Manual                 SCTP(7)

## [](#NAME)NAME

           sctp - SCTP protocol.

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>
           #include <netinet/in.h>
           #include <netinet/sctp.h>

           sctp_socket = socket(PF_INET, SOCK_STREAM, IPPROTO_SCTP);
           sctp_socket = socket(PF_INET, SOCK_SEQPACKET, IPPROTO_SCTP);

## [](#DESCRIPTION)DESCRIPTION

           This is an implementation of the SCTP protocol as defined in
           RFC4960. It is a message oriented, reliable transport protocol
           with direct support for multihoming that runs on top of ip(7), and
           supports both v4 and v6 versions.

           Like TCP, SCTP provides reliable, connection oriented data
           delivery with congestion control. Unlike TCP, SCTP also provides
           message boundary preservation, ordered and unordered message
           delivery, multi-streaming and multi-homing. Detection of data
           corruption, loss of data and duplication of data is achieved by
           using checksums and sequence numbers. A selective retransmission
           mechanism is applied to correct loss or corruption of data.

           This implementation supports a mapping of SCTP into sockets API as
           defined in the RFC6458(Sockets API extensions for SCTP). Two
           styles of interfaces are supported.

           A one-to-many style interface with 1 to MANY relationship between
           socket and associations where the outbound association setup is
           implicit. The syntax of a one-to-many style socket() call is

           sd = socket(PF_INET, SOCK_SEQPACKET, IPPROTO_SCTP);

           A typical server in this style uses the following socket calls in
           sequence to prepare an endpoint for servicing requests.

                1. socket()
                2. bind()
                3. listen()
                4. recvmsg()
                5. sendmsg()
                6. close()

           A typical client uses the following calls in sequence to setup an
           association with a server to request services.

                1. socket()
                2. sendmsg()
                3. recvmsg()
                4. close()

           A one-to-one style interface with a 1 to 1 relationship between
           socket and association which enables existing TCP applications to
           be ported to SCTP with very little effort. The syntax of a one-to-
           one style socket() call is

           sd = socket(PF_INET, SOCK_STREAM, IPPROTO_SCTP);

           A typical server in one-to-one style uses the following system
           call sequence to prepare an SCTP endpoint for servicing requests:

                1. socket()
                2. bind()
                3. listen()
                4. accept()

           The accept() call blocks until a new association is set up. It
           returns with a new socket descriptor. The server then uses the new
           socket descriptor to communicate with the client, using recv() and
           send() calls to get requests and send back responses. Then it
           calls

                5. close()

           to terminate the association. A typical client uses the following
           system call sequence to setup an association with a server to
           request services:

                1. socket()
                2. connect()

           After returning from connect(), the client uses send() and recv()
           calls to send out requests and receive responses from the server.
           The client calls

                3. close()

           to terminate this association when done.

## [](#ADDRESS_FORMATS)ADDRESS FORMATS

           SCTP is built on top of IP (see ip(7)).  The address formats
           defined by ip(7) apply to SCTP.  SCTP only supports point-to-point
           communication; broadcasting and multicasting are not supported.

## [](#SYSCTLS)SYSCTLS

           These variables can be accessed by the /proc/sys/net/sctp/* files
           or with the sysctl(2) interface.  In addition, most IP sysctls
           also apply to SCTP. See ip(7).

           Please check kernel documentation for this, at
           Documentation/networking/ip-sysctl.rst.

## [](#STATISTICS)STATISTICS

           These variables can be accessed by the /proc/net/sctp/* files.

           assocs Displays the following information about the active
                  associations.  assoc ptr, sock ptr, socket style, sock
                  state, association state, hash bucket, association id,
                  bytes in transmit queue, bytes in receive queue, user id,
                  inode, local port, remote port, local addresses, remote
                  addresses, heartbeat interval, in streams, out streams, max
                  retransmissions, init retries, shutdown retries,
                  retransmitted chunks, sock transmit queue committed bytes,
                  sock transmit queue bytes, and sock send and receive buffer
                  bytes.

           eps    Displays the following information about the active
                  endpoints.  endpoint ptr, sock ptr, socket style, sock
                  state, hash bucket, local port, user id, inode and local
                  addresses.

           snmp   Displays the following statistics related to SCTP states,
                  packets and chunks.

           SctpCurrEstab
                  The number of associations for which the current state is
                  either ESTABLISHED, SHUTDOWN-RECEIVED or SHUTDOWN-PENDING.

           SctpActiveEstabs
                  The number of times that associations have made a direct
                  transition to the ESTABLISHED state from the COOKIE-ECHOED
                  state. The upper layer initiated the association attempt.

           SctpPassiveEstabs
                  The number of times that associations have made a direct
                  transition to the ESTABLISHED state from the CLOSED state.
                  The remote endpoint initiated the association attempt.

           SctpAborteds
                  The number of times that associations have made a direct
                  transition to the CLOSED state from any state using the
                  primitive 'ABORT'. Ungraceful termination of the
                  association.

           SctpShutdowns
                  The number of times that associations have made a direct
                  transition to the CLOSED state from either the SHUTDOWN-
                  SENT state or the SHUTDOWN-ACK-SENT state. Graceful
                  termination of the association.

           SctpOutOfBlues
                  The number of out of the blue packets received by the host.
                  An out of the blue packet is an SCTP packet correctly
                  formed, including the proper checksum, but for which the
                  receiver was unable to identify an appropriate association.

           SctpChecksumErrors
                  The number of SCTP packets received with an invalid
                  checksum.

           SctpOutCtrlChunks
                  The number of SCTP control chunks sent (retransmissions are
                  not included).  Control chunks are those chunks different
                  from DATA.

           SctpOutOrderChunks
                  The number of SCTP ordered data chunks sent
                  (retransmissions are not included).

           SctpOutUnorderChunks
                  The number of SCTP unordered chunks(data chunks in which
                  the U bit is set to 1) sent (retransmissions are not
                  included).

           SctpInCtrlChunks
                  The number of SCTP control chunks received (no duplicate
                  chunks included).

           SctpInOrderChunks
                  The number of SCTP ordered data chunks received (no
                  duplicate chunks included).

           SctpInUnorderChunks
                  The number of SCTP unordered chunks(data chunks in which
                  the U bit is set to 1) received (no duplicate chunks
                  included).

           SctpFragUsrMsgs
                  The number of user messages that have to be fragmented
                  because of the MTU.

           SctpReasmUsrMsgs
                  The number of user messages reassembled, after conversion
                  into DATA chunks.

           SctpOutSCTPPacks
                  The number of SCTP packets sent. Retransmitted DATA chunks
                  are included.

           SctpInSCTPPacks
                  The number of SCTP packets received. Duplicates are
                  included.

           SctpT1InitExpireds
                  The number of timer T1 INIT expired.

           SctpT1CookieExpireds
                  The number of timer T1 COOKIE-ECHO expired.

           SctpT2ShutdownExpireds
                  The number of timer T2 SHUTDOWN expired.

           SctpT3RtxExpireds
                  The number of timer T3 RTX expired.

           SctpT4RtoExpireds
                  The number of timer T4 RTO expired.

           SctpT5ShutdownGuardExpireds
                  The number of timer T5 SHUTDOWN GUARD expired.

           SctpDelaySackExpireds
                  The number of timer DELAY_SACK expired.

           SctpAutocloseExpireds
                  The number of timer AUTOCLOSE expired.

           SctpT3Retransmits
                  The number of T3 timer retransmission.

           SctpPmtudRetransmits
                  The number of PMTUD retransmission.

           SctpFastRetransmits
                  The number of FAST retransmission.

           SctpInPktSoftirq
                  The number of SCTP packets received in Softirq.

           SctpInPktBacklog
                  The number of SCTP packets received in Backlog.

           SctpInPktDiscards
                  The number of SCTP packets discarded in receiving.

           SctpInDataChunkDiscards
                  The number of SCTP data chunks discarded in receiving.

## [](#CONTROL_MSGS)CONTROL MSGS

           The ancillary data is carried in msg_control field of struct
           msghdr, which is used in sendmsg(2) and recvmsg(2) call. The SCTP
           stack uses the ancillary data to communicate the attributes, such
           as SCTP_RCVINFO, of the message stored in msg_iov to the socket
           endpoint.  Each ancillary data item is preceded by a struct
           cmsghdr, see cmsg(3).  The different cmsg types for SCTP are
           listed below, and all these related macros and structures are
           defined in /usr/include/netinet/sctp.h.

           SCTP_INIT
                  This cmsg provides information for initializing new SCTP
                  associations for sendmsg() with struct sctp_initmsg, which
                  is the same as SCTP_INITMSG socket option's data structure.

           SCTP_SNDRCV
                  This cmsg specifies SCTP options for sendmsg() and
                  describes SCTP header information about a received message
                  through recvmsg() with struct sctp_sndrcvinfo. It mixes the
                  send and receive path, and SCTP_SNDINFO and SCTP_RCVINFO
                  split this information, so these structures should be used,
                  when possible, since SCTP_SNDRCV is deprecated.
                  sctp_sendmsg(3) and sctp_send(3) provide a simple way to
                  use this cmsg.

                  Note that an application must use the SCTP_RECVRCVINFO
                  socket option to enable the delivery of this information.

           SCTP_EXTRCV
                  This cmsg specifies SCTP options for SCTP header
                  information about a received message via recvmsg() with
                  struct sctp_extrcvinfo, and this structure is an extended
                  version of SCTP_SNDRCV. Note that data in the next message
                  is not valid unless the current message is completely read,
                  i.e., unless the MSG_EOR is set. SCTP_NXTINFO should be
                  used when possible, since SCTP_EXTRCV is considered
                  deprecated.  sctp_recvmsg(3) provides a simple way to use
                  this cmsg.

                  Note that an application must use the SCTP_RECVNXTINFO
                  socket option to enable the delivery of this information.

           SCTP_RCVINFO, SCTP_NXTINFO
                  These cmsgs describe SCTP receive information about a
                  received message through recvmsg() with struct
                  sctp_rcvinfo, and SCTP receive information of the next
                  message that will be delivered through recvmsg() if this
                  information is already available when delivering the
                  current message with struct sctp_nxtinfo.  sctp_recvv(3)
                  provides a simple way to use these cmsgs.

                  Note that an application must use the SCTP_RECVRCVINFO and
                  SCTP_RECVNXTINFO socket options accordingly to enable the
                  delivery of this information.

           SCTP_SNDINFO, SCTP_PRINFO, SCTP_AUTHINFO, SCTP_DSTADDRV4,
           SCTP_DSTADDRV6
                  These cmsgs specifie a couple of SCTP options for sendmsg()
                  for SEND, PRSCTP, AUTH and DSTADDR information with struct
                  sctp_sndinfo, sctp_prinfo, sctp_authinfo and in(6)_addr
                  accordingly.  sctp_sendv(3) provides a simple way to use
                  these cmsgs.

## [](#EVENTS_and_NOTIFICATIONS)EVENTS and NOTIFICATIONS

           An SCTP application may need to understand and process events and
           errors that happen on the SCTP stack. These events include network
           status changes, association startups, remote operational errors,
           and undeliverable messages.  When a notification arrives,
           recvmsg() returns the notification in the application-supplied
           data buffer via msg_iov, and sets MSG_NOTIFICATION in msg_flags.
           See socket option SCTP_EVENT for the event enabling. The different
           events are listed below, and all these related macros and
           structures are defined in /usr/include/netinet/sctp.h.

           SCTP_ASSOC_CHANGE
                  Communication notifications inform the application that an
                  SCTP association has either begun or ended. The
                  notification format is struct sctp_assoc_change.

           SCTP_PEER_ADDR_CHANGE
                  When a destination address of a multi-homed peer encounters
                  a state change, a peer address change event is sent. The
                  notification format is struct sctp_paddr_change.

           SCTP_REMOTE_ERROR
                  A remote peer may send an Operation Error message to its
                  peer.  This message indicates a variety of error conditions
                  on an association.  The notification format is struct
                  sctp_remote_error.

           SCTP_SEND_FAILED
                  If SCTP cannot deliver a message, it can return back the
                  message as a notification if the SCTP_SEND_FAILED event is
                  enabled. The notification format is struct
                  sctp_send_failed. Please note that this notification is
                  deprecated. Use SCTP_SEND_FAILED_EVENT instead.

           SCTP_SHUTDOWN_EVENT
                  When a peer sends a SHUTDOWN, SCTP delivers this
                  notification to inform the application that it should cease
                  sending data. The notification format is struct
                  sctp_shutdown_event.

           SCTP_ADAPTATION_INDICATION
                  When a peer sends an Adaptation Layer Indication parameter,
                  SCTP delivers this notification to inform the application
                  about the peer's adaptation layer indication. The
                  notification format is struct sctp_adaptation_event.

           SCTP_PARTIAL_DELIVERY_EVENT
                  When a receiver is engaged in a partial delivery of a
                  message, this notification will be used to indicate various
                  events. The notification format is struct sctp_pdapi_event.

           SCTP_AUTHENTICATION_EVENT
                  This is used to report different events relating to the use
                  of the extension to authenticate SCTP messages. The
                  notification format is struct sctp_authkey_event.

           SCTP_SENDER_DRY_EVENT
                  When the SCTP stack has no more user data to send or
                  retransmit, this notification is given to the user.  Also,
                  at the time when a user app subscribes to this event, if
                  there is no data to be sent or retransmit, the stack will
                  immediately send up this notification. The notification
                  format is struct sctp_sender_dry_event.

           SCTP_SEND_FAILED_EVENT
                  If SCTP cannot deliver a message, it can return back the
                  message as a notification if the SCTP_SEND_FAILED_EVENT
                  event is enabled. The notification format is struct
                  sctp_send_failed_event.

## [](#SOCKET_OPTIONS)SOCKET OPTIONS

           To set or get a SCTP socket option, call getsockopt(2) to read or
           setsockopt(2) to write the option with the option level argument
           set to SOL_SCTP.  Note that all these macros and structures
           described for parameters are defined in
           /usr/include/netinet/sctp.h, and for one-to-one style sockets a
           specified assoc_id works the same as SCTP_FUTURE_ASSOC.

           SCTP_RTOINFO.
                  This option is used to get or set the protocol parameters
                  used to initialize and bound retransmission timeout(RTO).

                  The parameter type is struct sctp_rtoinfo, for reading and
                  writing.  srto_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

                  Default: srto_max=sysctl_net.sctp.rto_max,
                  srto_min=sysctl_net.sctp.rto_min,
                  srto_initial=sysctl_net.sctp.rto_initial.

           SCTP_ASSOCINFO
                  This option is used to both examine and set various
                  association and endpoint parameters.

                  The parameter type is struct sctp_assocparams, for reading
                  and writing.  sasoc_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC. Note that some fields of this structure
                  are for reading only:

                    struct sctp_assocparams {
                            sctp_assoc_t    sasoc_assoc_id;
                            __u16           sasoc_asocmaxrxt; (RW)
                            __u16           sasoc_number_peer_destinations;
                  (R)
                            __u32           sasoc_peer_rwnd; (R)
                            __u32           sasoc_local_rwnd; (R)
                            __u32           sasoc_cookie_life; (RW)
                    };

                  Default:
                  sasoc_asocmaxrxt=sysctl_net.sctp.association_max_retrans,
                  sasoc_cookie_life=sysctl_net.sctp.valid_cookie_life.

           SCTP_INITMSG
                  This option is used to get or set the protocol parameters
                  for the default association initialization.

                  The parameter type is struct sctp_initmsg, for reading and
                  writing.

                  Default: sinit_num_ostreams=10, sinit_max_instreams=10,
                  sinit_max_attempts=sysctl_net.sctp.max_init_retransmits,
                  sinit_max_init_timeo=sysctl_net.sctp.rto_max.

           SCTP_NODELAY
                  Turn on/off any Nagle-like algorithm. This means that
                  packets are generally sent as soon as possible and no
                  unnecessary delays are introduced, at the cost of more
                  packets in the network.

                  The parameter type is int boolean, for reading and writing.

                  Default: 0.

           SCTP_AUTOCLOSE
                  This socket option is applicable to the one-to-many style
                  socket only.  When set it will cause associations that are
                  idle for more than the specified number of seconds to
                  automatically close. An association being idle is defined
                  an association that has NOT sent or received user data
                  within a period.

                  The parameter type is int(seconds), for reading and
                  writing. 0 indicates that no automatic close of any
                  associations should be performed.

                  Default: sysctl_net.sctp.max_autoclose.

           SCTP_SET_PEER_PRIMARY_ADDR
                  Requests that the peer mark the enclosed address as the
                  association primary. The enclosed address must be one of
                  the association's locally bound addresses.

                  The parameter type is struct sctp_setpeerprim, for writing
                  only.  sspp_assoc_id is a specified assoc_id.

                  Default: the 1st local address added.  Require:
                  SCTP_ASCONF_SUPPORTED.

           SCTP_PRIMARY_ADDR
                  Requests that the local SCTP stack use the enclosed peer
                  address as the association primary. The enclosed address
                  must be one of the association peer's addresses.

                  The parameter type is struct sctp_prim, for writing only.
                  ssp_assoc_id is a specified assoc_id.

                  Default: the 1st peer address added.  Require:
                  SCTP_ASCONF_SUPPORTED.

           SCTP_DISABLE_FRAGMENTS
                  If enabled no SCTP message fragmentation will be performed.
                  Instead if a message being sent exceeds the current PMTU
                  size, the message will NOT be sent and an error will be
                  indicated to the user.

                  The parameter type is int boolean, for reading and writing.

                  Default: 0.

           SCTP_PEER_ADDR_PARAMS
                  Using this option, applications can enable or disable
                  heartbeats for any peer address of an association, modify
                  an address's heartbeat interval, force a heartbeat to be
                  sent immediately, and adjust the address's maximum number
                  of retransmissions sent before an address is considered
                  unreachable.

                  The parameter type is struct sctp_paddrparams, for reading
                  and writing.  spp_address is a specified transport address
                  or 0, spp_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

                  Default: hbinterval=sysctl_net.sctp.hb_interval,
                  pathmaxrxt=sysctl_net.sctp.path_max_retrans,
                  pathmtu=dev/route's,
                  sackdelay=sysctl_net.sctp.sack_timeout,
                  param_flags=HB_ENABLE|PMTUD_ENABLE|SACKDELAY_ENABLE,
                  flowlabel=0, dscp=0.

           SCTP_DEFAULT_SEND_PARAM
                  Applications that wish to use the sendto() system call may
                  wish to specify a default set of parameters that would
                  normally be supplied through the inclusion of ancillary
                  data. This option has been obsoleted by
                  SCTP_DEFAULT_SNDINFO.

                  The parameter type is struct sctp_sndrcvinfo. For reading,
                  sinfo_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC. For writing, sinfo_assoc_id is a
                  specified assoc_id or SCTP_{FUTURE|CURRENT|ALL}_ASSOC.

                  Default: default_stream=0, default_flags=0, default_ppid=0,
                  default_context=0, default_timetolive=0.

           SCTP_EVENTS
                  This socket option is used to specify various notifications
                  and ancillary data the user wishes to receive. This option
                  has been obsoleted by SCTP_EVENT.

                  The parameter type is struct sctp_event_subscribe, for
                  reading and writing.

                  Default: 0.

           SCTP_I_WANT_MAPPED_V4_ADDR
                  This socket option is used to turn on or off mapped V4
                  addresses. If this option is turned on and the socket is
                  type PF_INET6, then IPv4 addresses will be mapped to V6
                  representation. If this option is turned off, then no
                  mapping will be done of V4 addresses and a user will
                  receive both PF_INET6 and PF_INET type addresses on the
                  socket.

                  The parameter type is int boolean, for reading and writing.

                  Default: 1.

           SCTP_MAXSEG
                  This socket option specifies the maximum size to put in any
                  outgoing SCTP DATA chunk. If a message is larger than this
                  size it will be fragmented by SCTP into the specified size.
                  Note that the underlying SCTP implementation may fragment
                  into smaller sized chunks when the PMTU of the underlying
                  association is smaller than the value set by the user. 0
                  indicates the user is NOT limiting fragmentation and only
                  the PMTU will effect SCTP's choice of DATA chunk size.

                  The parameter type is struct sctp_assoc_value, for reading
                  and writing.  assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

                  Default: 0(no limit).

           SCTP_STATUS
                  Applications can retrieve current status information about
                  an association, including association state, peer receiver
                  window size, number of unacked data chunks, and number of
                  data chunks pending receipt.

                  The parameter type is struct sctp_status, for reading only.
                  sstat_assoc_id is a specified assoc_id.

           SCTP_GET_PEER_ADDR_INFO
                  Applications can retrieve information about a specific peer
                  address of an association, including its reachability
                  state, congestion window, and retransmission timer values.

                  The parameter type is struct sctp_paddrinfo, for reading
                  only. spinfo_address is a specified transport address,
                  sas_assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC.

           SCTP_GET_ASSOC_STATS
                  Applications can retrieve current statistics about an
                  association, including SACKs sent and received, SCTP
                  packets sent and received.

                  The parameter type is struct sctp_assoc_stats, for reading
                  only.  sas_assoc_id is a specified assoc_id.

           SCTP_DELAYED_ACK, SCTP_DELAYED_ACK_TIME, SCTP_DELAYED_SACK
                  These options will affect the way delayed SACKs are
                  performed. They allow the application to get or set the
                  delayed SACK time, in milliseconds, and also allow changing
                  the delayed SACK frequency. Changing the frequency to 1
                  disables the delayed SACK algorithm. Note that if
                  sack_delay or sack_freq is 0 when setting this option, the
                  current values will remain unchanged.

                  The parameter type is struct sctp_sack_info. For reading,
                  sack_assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC.
                  For writing, sack_assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC.

                  Default: sackdelay=sysctl_net.sctp.sack_timeout,sackfreq=2.

           SCTP_CONTEXT
                  This option allows the setting, on an association basis, of
                  a default context that will be received on reading messages
                  from the peer.  This is especially helpful for an
                  application when using one-to-many style sockets to keep
                  some reference to an internal state machine that is
                  processing messages on the association.  Note that the
                  setting of this value only affects received messages from
                  the peer and does not affect the value that is saved with
                  outbound messages.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC.

                  Default: 0.

           SCTP_FRAGMENT_INTERLEAVE
                  Fragmented interleave controls how the presentation of
                  messages occurs for the message receiver. There are three
                  levels of fragment interleave defined: level 0:
                  SCTP_FRAGMENT_INTERLEAVE = 0; level 1:
                  SCTP_FRAGMENT_INTERLEAVE = 1; level 2:
                  SCTP_FRAGMENT_INTERLEAVE = 1 & SCTP_INTERLEAVING_SUPPORTED
                  = 1.

                  The parameter type is int boolean, for reading and writing.

                  Default: 0.

           SCTP_PARTIAL_DELIVERY_POINT
                  This option will set or get the SCTP partial delivery
                  point.  This point is the size of a message where the
                  partial delivery API will be invoked to help free up rwnd
                  space for the peer.  Setting this to a lower value will
                  cause partial deliveries to happen more often.  This option
                  expects an integer that sets or gets the partial delivery
                  point in bytes.  Note also that the call will fail if the
                  user attempts to set this value larger than the socket
                  receive buffer size. Note that any single message having a
                  length smaller than or equal to the SCTP partial delivery
                  point will be delivered in a single read call as long as
                  the user-provided buffer is large enough to hold the
                  message.

                  The parameter type is uint32_t, for reading and writing.

                  Default: 0.

           SCTP_MAX_BURST
                  This option will allow a user to change the maximum burst
                  of packets that can be emitted by this association.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC.

                  Default: sysctl_net.sctp.max_burst.

           SCTP_AUTH_CHUNK
                  This option adds a chunk type that the user is requesting
                  to be received only in an authenticated way, and it only
                  affects the future associations.

                  The parameter type is struct sauth_chunk, for writing only.

                  Default: no chunks.  Require: SCTP_AUTH_SUPPORTED.  RFC:
                  RFC4895.

           SCTP_HMAC_IDENT
                  This option gets or sets the list of Hashed Message
                  Authentication Code (HMAC) algorithms that the local
                  endpoint requires the peer to use.

                  The parameter type is struct sctp_hmacalgo, for reading and
                  writing.  shmac_idents can include
                  SCTP_AUTH_HMAC_ID_{SHA1|SHA256}.

                  Default: SCTP_AUTH_HMAC_ID_SHA1.  Require:
                  SCTP_AUTH_SUPPORTED.

           SCTP_AUTH_KEY
                  This option will set a shared secret key that is used to
                  build an association shared key.

                  The parameter type is struct sctp_authkey, for writing
                  only. sca_assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC.

                  Default: null_key.  Require: SCTP_AUTH_SUPPORTED.

           SCTP_AUTH_ACTIVE_KEY
                  This option will get or set the active shared key to be
                  used to build the association shared key.

                  The parameter type is struct sctp_authkeyid, for writing
                  only.  scact_assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC.

                  Default: 0.  Require: SCTP_AUTH_SUPPORTED.

           SCTP_AUTH_DEACTIVATE_KEY
                  This set option indicates that the application will no
                  longer send user messages using the indicated key
                  identifier.

                  The parameter type is struct sctp_authkeyid, for writing
                  only.  scact_assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC.

                  Require: SCTP_AUTH_SUPPORTED.

           SCTP_AUTH_DELETE_KEY
                  This set option will delete an SCTP association's shared
                  secret key that has been deactivated.

                  The parameter type is struct sctp_authkeyid, for writing
                  only.  scact_assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC.

                  Require: SCTP_AUTH_SUPPORTED.

           SCTP_PEER_AUTH_CHUNKS
                  This option gets a list of chunk types for a specified
                  association that the peer requires to be received
                  authenticated only.

                  The parameter type is struct sctp_authchunks, for reading
                  only.  gauth_assoc_id is a specified assoc_id.

                  Require: SCTP_AUTH_SUPPORTED.

           SCTP_LOCAL_AUTH_CHUNKS
                  This option gets a list of chunk types for a specified
                  association that the local endpoint requires to be received
                  authenticated only.

                  The parameter type is struct sctp_authchunks, for reading
                  only.  gauth_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

                  Require: SCTP_AUTH_SUPPORTED.

           SCTP_GET_ASSOC_NUMBER
                  This option gets the current number of associations that
                  are attached to a one-to-many style socket. Note that this
                  number is only a snapshot.  This means that the number of
                  associations may have changed when the caller gets back the
                  option result.

                  The parameter type is uint32_t, for reading only.

           SCTP_GET_ASSOC_ID_LIST
                  This option gets the current list of SCTP association
                  identifiers of the SCTP associations handled by a one-to-
                  many style socket. It uses struct sctp_assoc_ids and must
                  provide a large enough buffer to hold all association
                  identifiers. If the buffer is too small, an error must be
                  returned. The user can use the SCTP_GET_ASSOC_NUMBER socket
                  option to get an idea of how large the buffer has to be.

                  The parameter type is struct sctp_assoc_ids, for reading
                  only.

           SCTP_EXPOSE_POTENTIALLY_FAILED_STATE, SCTP_EXPOSE_PF_STATE
                  Applications can control the exposure of the PF path state
                  in the SCTP_PEER_ADDR_CHANGE event, and if pf_expose is not
                  'enabled', no notification will be sent for a transport
                  state change to SCTP_PF.  It also affects the
                  SCTP_GET_PEER_ADDR_INFO socket option, and if pf_expose is
                  'disabled', users can not access the transport info via
                  SCTP_GET_PEER_ADDR_INFO option.

                  The parameter type is struct sctp_assoc_value, for reading
                  and writing.  assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

                  Default: sysctl_net.sctp.pf_expose.

           SCTP_PEER_ADDR_THLDS
                  Applications can control the SCTP-PF behavior by getting or
                  setting the number of consecutive timeouts before a peer
                  address is considered PF or unreachable..

                  The parameter type is struct sctp_paddrthlds, for reading
                  and writing.  spt_address is a specified transport address
                  or 0, spt_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

                  Default: pathmaxrxt=sysctl_net.sctp.path_max_retrans,
                  ps_retrans=sysctl_net.sctp.ps_retrans.

           SCTP_PEER_ADDR_THLDS_V2
                  Similar to SCTP_PEER_ADDR_THLDS, but it can also be used by
                  applications to set and get the number of timeouts before
                  the primary path is changed automatically by the Primary
                  Path Switchover function.

                  The parameter type is struct sctp_paddrthlds_v2, for
                  reading and writing.  spt_address is a specified transport
                  address or 0, spt_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

                  Default: pathmaxrxt=sysctl_net.sctp.path_max_retrans,
                  ps_retrans=sysctl_net.sctp.ps_retrans,
                  pf_retrans=sysctl_net.sctp.pf_retrans.

           SCTP_RECVRCVINFO
                  Setting this option specifies that SCTP_RCVINFO (SCTP
                  receive information about a received message) is returned
                  as ancillary data by recvmsg(). See CONTROL MSGS for more
                  details.

                  The parameter type is int, for reading and writing.

                  Default: 0.

           SCTP_RECVNXTINFO
                  Setting this option specifies that SCTP_NXTINFO (SCTP
                  receive information of the next message) is returned as
                  ancillary data by recvmsg(). See CONTROL MSGS for details.

                  The parameter type is int, for reading and writing.

                  Default: 0.

           SCTP_DEFAULT_SNDINFO
                  This option obsoletes SCTP_DEFAULT_SEND_PARAM.

                  The parameter type is struct sctp_sndinfo. For reading,
                  snd_assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC.
                  For writing, snd_assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC.

                  Default: default_stream=0, default_flags=0, default_ppid=0,
                  default_context=0.

           SCTP_REUSE_PORT
                  This option is similar to the socket level option
                  SO_REUSEADDR, besides only supports one-to-one style SCTP
                  sockets and must not be used after calling bind() or
                  sctp_bindx().

                  The parameter type is int, for reading and writing.

                  Default: 0.

           SCTP_SOCKOPT_BINDX_ADD
                  This option allows the user to bind a specific subset of
                  addresses or, if the SCTP extension ASCONF is supported
                  (see SCTP_ASCONF_SUPPORTED), add specific addresses. The
                  API sctp_bindx() is based on this.

                  The parameter type is struct sockaddr[], for writing only.

           SCTP_SOCKOPT_BINDX_REM
                  Similar to SCTP_SOCKOPT_BINDX_ADD, but delete specific
                  addresses. The API sctp_bindx() is based on this.

                  The parameter type is struct sockaddr[], for writing only.

           SCTP_SOCKOPT_PEELOFF
                  This option branches off an UDP type association into a
                  separate socket returned back to users. The API
                  sctp_peeloff() is based on this option.

                  The parameter type is sctp_peeloff_arg_t, for reading only.
                  associd is a specified assoc_id.

           SCTP_SOCKOPT_PEELOFF_FLAGS
                  Peel off an UDP type association from a socket similar to
                  SCTP_SOCKOPT_PEELOFF option, but it allows the flags like
                  O_CLOEXEC and O_NONBLOCK to be used when creating the new
                  socket. The API sctp_peeloff_flags() is based on this
                  option.

                  The parameter type is sctp_peeloff_flags_arg_t, for reading
                  only. associd is a specified assoc_id.

           SCTP_SOCKOPT_CONNECTX_OLD
                  This option allows a user to specify multiple addresses at
                  which a peer can be reached, and the kernel stack will use
                  the list of addresses to set up the association. The API
                  sctp_connectx() is based on this option.

                  The parameter type is struct sockaddr[], for writing only.

           SCTP_SOCKOPT_CONNECTX
                  Similar to SCTP_SOCKOPT_CONNECTX_OLD, but it returns the
                  new assoc's id.  The API sctp_connectx2() is based on this
                  option.

                  The parameter type is struct sockaddr[], for writing only.
                  The new assoc's id is passed to users by the return value.

           SCTP_SOCKOPT_CONNECTX3
                  Similar to SCTP_SOCKOPT_CONNECTX, but it uses different
                  type parameter. The API sctp_connectx3() is based on this
                  option.

                  The parameter type is struct sctp_getaddrs_old, for reading
                  only. assoc_id is set to the new assoc's id by kernel and
                  passed to users.

           SCTP_GET_PEER_ADDRS
                  This option is used to gets all peer addresses in an
                  association. The API sctp_getpaddrs() is based on this
                  option.

                  The parameter type is struct sctp_getaddrs, for reading
                  only. assoc_id is a specified assoc_id.

           SCTP_GET_LOCAL_ADDRS
                  This option is used to get all local addresses in an
                  association. The API sctp_getladdrs() is based on this
                  option.

                  The parameter type is struct sctp_getaddrs, for reading
                  only. assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

           SCTP_ADAPTATION_LAYER
                  This option requests that the local endpoint set the
                  specified Adaptation Layer Indication parameter for all
                  future INIT and INIT-ACK exchanges.

                  The parameter type is struct sctp_setadaptation, for
                  reading and writing.

                  Default: 0.

           SCTP_EVENT
                  This option obsoletes SCTP_EVENTS socket option, and it can
                  set or get one specific type of event for a specified
                  association.

                  The parameter type is struct sctp_event. For reading,
                  se_assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC.
                  For writing, se_assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC. se_type can be one of enum
                  sctp_sn_type.

                  Default: 0.

           SCTP_PR_SUPPORTED
                  This socket option allows the enabling or disabling of the
                  negotiation of PR-SCTP support for future associations.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, assoc_id is SCTP_FUTURE_ASSOC.

                  Default: sysctl_net.sctp.prsctp_enable.  RFC: RFC7496.

           SCTP_DEFAULT_PRINFO
                  This option sets and gets the default parameters for PR-
                  SCTP.

                  The parameter type is struct sctp_default_prinfo. For
                  reading, pr_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC. For writing, pr_assoc_id is a specified
                  assoc_id or SCTP_{FUTURE|CURRENT|ALL}_ASSOC. pr_policy can
                  be SCTP_PR_SCTP_{NONE|TTL|RTX|PRIO}.

                  Default: SCTP_PR_SCTP_NONE.  Require: SCTP_DEFAULT_PRINFO.

           SCTP_PR_ASSOC_STATUS
                  This option is used to get Association-Specific PR-SCTP
                  Status.

                  The parameter type is struct sctp_prstatus, for reading
                  only.  sprstat_assoc_id is a specified assoc_id,
                  sprstat_policy can be SCTP_PR_SCTP_{TTL|RTX|PRIO|ALL}.

           SCTP_PR_STREAM_STATUS
                  This option is used to get Stream-Specific PR-SCTP Status.

                  The parameter type is struct sctp_prstatus, for reading
                  only.  sprstat_assoc_id is a specified assoc_id,
                  sprstat_policy can be SCTP_PR_SCTP_{TTL|RTX|PRIO|ALL}.

           SCTP_RECONFIG_SUPPORTED
                  Enable the Stream Reconfiguration(RECONF) for the future
                  associations.  For different type of requests enabling, see
                  SCTP_ENABLE_STREAM_RESET option.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, assoc_id is SCTP_FUTURE_ASSOC.

                  Default: sysctl_net.sctp.reconf_enable.  RFC: RFC6525.

           SCTP_ENABLE_STREAM_RESET
                  This option allows a user to control whether the kernel
                  processes or denies incoming requests in RECONF chunks.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC. assoc_value can be
                  SCTP_ENABLE_{RESET_STREAM_REQ|RESET_ASSOC_REQ|CHANGE_ASSOC_REQ}.

                  Default: 0.  Require: SCTP_RECONFIG_SUPPORTED.

           SCTP_RESET_STREAMS
                  This option allows the user to request the reset of
                  incoming and/or outgoing streams.

                  The parameter type is struct sctp_reset_streams, for
                  writing only.  srs_assoc_id is a specified assoc_id.

                  Require: SCTP_ENABLE_STREAM_RESET.

           SCTP_RESET_ASSOC
                  This option allows a user to request the reset of the
                  SSN/TSN.

                  The parameter type is sctp_assoc_t, for writing only. It is
                  a specified assoc_id.

                  Require: SCTP_ENABLE_STREAM_RESET.

           SCTP_ADD_STREAMS
                  This option allows a user to request the addition of a
                  number of incoming and/or outgoing streams.

                  The parameter type is struct sctp_add_streams, for writing
                  only.  sas_assoc_id is a specified assoc_id.

                  Require: SCTP_ENABLE_STREAM_RESET.

           SCTP_STREAM_SCHEDULER
                  This option is used to select a stream scheduler for data
                  sending.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, assoc_id is a specified assoc_id or
                  SCTP_{FUTURE|CURRENT|ALL}_ASSOC. assoc_value can be
                  SCTP_SS_{FCFS|PRIO|RR|FC|WFQ}.

                  Default: SCTP_SS_FCFS.  RFC: RFC8260.

           SCTP_STREAM_SCHEDULER_VALUE
                  Some stream schedulers require additional information to be
                  set for individual streams.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id. For writing, assoc_id is
                  a specified assoc_id or SCTP_CURRENT_ASSOC.

                  Require: SCTP_STREAM_SCHEDULER.

           SCTP_INTERLEAVING_SUPPORTED
                  This socket option allows the enabling or disabling of the
                  negotiation of user message interleaving support for future
                  associations.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, assoc_id is SCTP_FUTURE_ASSOC.

                  Default: sysctl_net.sctp.intl_enable.  Require:
                  SCTP_FRAGMENT_INTERLEAVE.  RFC: RFC8260.

           SCTP_ASCONF_SUPPORTED
                  Enable the Dynamic Address Reconfiguration(ASCONF) for the
                  future associations.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, assoc_id is SCTP_FUTURE_ASSOC.

                  Default: sysctl_net.sctp.addip_enable.  RFC: RFC5061.

           SCTP_AUTO_ASCONF
                  This option will enable or disable the use of the automatic
                  generation of ASCONF chunks to add and delete addresses to
                  an existing association.  Note that this option has two
                  caveats, namely a) it only affects sockets that are bound
                  to all addresses available to the SCTP stack, and b) the
                  system administrator may have an overriding control that
                  turns the ASCONF feature off no matter what setting the
                  socket option may have.

                  The parameter type is int boolean, for reading and writing.

                  Default: sysctl_net.sctp.default_auto_asconf.

           SCTP_AUTH_SUPPORTED
                  Enable AUTH for the future associations.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, ssoc_id is SCTP_FUTURE_ASSOC.

                  Default: sysctl_net.sctp.auth_enable.  RFC: RFC4895.

           SCTP_ECN_SUPPORTED
                  Enable ECN for the future associations.

                  The parameter type is struct sctp_assoc_value. For reading,
                  assoc_id is a specified assoc_id or SCTP_FUTURE_ASSOC. For
                  writing, assoc_id is SCTP_FUTURE_ASSOC.

                  Default: sysctl_net.sctp.ecn_enable.

           SCTP_REMOTE_UDP_ENCAPS_PORT
                  This option is used to set the encapsulation port(a remote
                  listening or dest port) for SCTP over UDP, which allows
                  SCTP traffic to pass through legacy NATs that do not
                  provide native SCTP support.

                  The parameter type is struct sctp_udpencaps, for reading
                  and writing.  sue_address is a specified transport address
                  or 0, sue_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

                  Default: sysctl_net.sctp.encap_port.  RFC: RFC6951.

           SCTP_PLPMTUD_PROBE_INTERVAL
                  This option is used to configure the PROBE_INTERVAL for the
                  Packetization Layer Path MTU Discovery(PLPMTUD). It can be
                  set to a value >= 5000 or 0(disabled).

                  The parameter type is struct sctp_probeinterval, for
                  reading and writing.  spi_address is a specified transport
                  address or 0, spi_assoc_id is a specified assoc_id or
                  SCTP_FUTURE_ASSOC.

                  Default: 0(disabled).  RFC: RFC8899.

## [](#AUTHORS)AUTHORS

           Sridhar Samudrala <sri@us.ibm.com>

## [](#SEE_ALSO)SEE ALSO

           socket(7), socket(2), ip(7), bind(2), listen(2), accept(2),
           connect(2), sendmsg(2), recvmsg(2), sysctl(2), getsockopt(2),
           sctp_bindx(3), sctp_connectx(3), sctp_sendmsg(3), sctp_sendv(3),
           sctp_send(3), sctp_recvmsg(3), sctp_recvv(3), sctp_peeloff(3),
           sctp_getladdrs(3), sctp_getpaddrs(3), sctp_opt_info(3).

           RFC2960, RFC3309 for the SCTP specification.

## [](#COLOPHON)COLOPHON

           This page is part of the lksctp-tools (Linux kernel SCTP tools)
           project.  Information about the project can be found at [unknown
           -- if you know, please contact man-pages@man7.org] If you have a
           bug report for this manual page, send it to sctp@vger.kernel.org.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/sctp/lksctp-tools.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2024-09-26.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux Man Page                  2005-10-25                        SCTP(7)

------------------------------------------------------------------------

Pages that refer to this page: [sctp_bindx(3)](../man3/sctp_bindx.3.html),  [sctp_connectx(3)](../man3/sctp_connectx.3.html),  [sctp_getladdrs(3)](../man3/sctp_getladdrs.3.html),  [sctp_getpaddrs(3)](../man3/sctp_getpaddrs.3.html),  [sctp_opt_info(3)](../man3/sctp_opt_info.3.html),  [sctp_peeloff(3)](../man3/sctp_peeloff.3.html),  [sctp_recvmsg(3)](../man3/sctp_recvmsg.3.html),  [sctp_recvv(3)](../man3/sctp_recvv.3.html),  [sctp_send(3)](../man3/sctp_send.3.html),  [sctp_sendmsg(3)](../man3/sctp_sendmsg.3.html),  [sctp_sendv(3)](../man3/sctp_sendv.3.html),  [ip(7)](../man7/ip.7.html)

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
