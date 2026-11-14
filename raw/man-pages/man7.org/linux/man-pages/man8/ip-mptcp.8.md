---
{"title": "ip-mptcp(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-mptcp.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-mptcp(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-MPTCP(8)                       Linux                       IP-MPTCP(8)

## [](#NAME)NAME

           ip-mptcp - MPTCP path manager configuration

## [](#SYNOPSIS)SYNOPSIS

           ip [ OPTIONS ] mptcp { endpoint  | limits  | help  }

           ip mptcp endpoint add IFADDR [ port PORT ] [ dev IFNAME ] [ id ID
                   ] [ FLAG-LIST ]

           ip mptcp endpoint delete id ID [ IFADDR ]

           ip mptcp endpoint change [ id ID ] [ IFADDR ] [ port PORT ]
                   CHANGE-OPT

           ip mptcp endpoint show [ id ID ]

           ip mptcp endpoint flush

           FLAG-LIST := [ FLAG-LIST ] FLAG

           FLAG := [ signal | subflow | laminar | backup | fullmesh ]

           CHANGE-OPT := [ backup | nobackup | fullmesh | nofullmesh ]

           ip mptcp limits set [ subflow SUBFLOW_NR ] [ add_addr_accepted
                   ADD_ADDR_ACCEPTED_NR ]

           ip mptcp limits show

           ip mptcp monitor

## [](#DESCRIPTION)DESCRIPTION

           MPTCP is a transport protocol built on top of TCP that allows TCP
           connections to use multiple paths to maximize resource usage and
           increase redundancy. The ip-mptcp sub-commands allow configuring
           several aspects of the MPTCP path manager, which is in charge of
           subflows creation:

           The endpoint object specifies the IP addresses that will be used
           and/or announced for additional subflows:

           ip mptcp endpoint add      add new MPTCP endpoint
           ip mptcp endpoint delete   delete existing MPTCP endpoint
           ip mptcp endpoint show     get existing MPTCP endpoint
           ip mptcp endpoint flush    flush all existing MPTCP endpoints

           IFADDR An IPv4 or IPv6 address. When used with the delete id
                  operation, an IFADDR is only included when the ID is 0.

           PORT   When a port number is specified, incoming MPTCP subflows
                  for already established MPTCP sockets will be accepted on
                  the specified port, regardless the original listener port
                  accepting the first MPTCP subflow and/or this peer being
                  actually on the client side. This option has to be used in
                  combination with the signal flag.

           IFNAME is the network interface name attached to the endpoint. It
                  is important to specify this device name linked to the
                  address to make sure the system knows how to route packets
                  from the specified IP address to the correct network
                  interface.  Without this, it might be required to add IP
                  rules and routes to have the expected behavior.

           ID     is a unique numeric identifier, between 0 and 255, for the
                  given endpoint. It is not possible to add endpoints with ID
                  0, because this special ID is reserved for the initial
                  subflow. For rules linked to the initial subflow, the path-
                  manager will look at endpoints matching the same address,
                  and port if set, ignoring the ID.

           signal The endpoint will be announced/signalled to each peer via
                  an MPTCP ADD_ADDR sub-option. Typically, a server would be
                  responsible for this. Upon reception of an ADD_ADDR sub-
                  option, the other peer, typically the client side, can try
                  to create additional subflows, see ADD_ADDR_ACCEPTED_NR.

           subflow
                  If additional subflow creation is allowed by the MPTCP
                  limits, the MPTCP path manager will try to create an
                  additional subflow using this endpoint as the source
                  address after the MPTCP connection is established. A client
                  would typically do this.

           laminar
                  The endpoint will be used to create new subflows from the
                  associated address to additional addresses announced by the
                  other peer. This will be done if allowed by the MPTCP
                  limits, and if the associated address is not already being
                  used by another subflow from the same MPTCP connection.
                  Note that the fullmesh flag takes precedence over the
                  laminar one. Without any of these two flags, the path-
                  manager will create new subflows to additional addresses
                  announced by the other peer by selecting the source address
                  from the routing tables, which is harder to configure if
                  the announced address is not known in advance.

           backup If this is a subflow endpoint, the subflows created using
                  this endpoint will have the backup flag set during the
                  connection process. This flag instructs the remote peer to
                  only send data on a given subflow when all non-backup
                  subflows are unavailable. When using the default packet
                  scheduler with a 'backup' endpoint, outgoing data from the
                  local peer is also affected: packets will only be sent from
                  this endpoint when all non-backup subflows are unavailable.

           fullmesh
                  If this is a subflow endpoint and additional subflow
                  creation is allowed by the MPTCP limits, the MPTCP path
                  manager will try to create an additional subflow for each
                  known peer address, using this endpoint as the source
                  address. This will occur after the MPTCP connection is
                  established. If the peer did not announce any additional
                  addresses using the MPTCP ADD_ADDR sub-option, this will
                  behave the same as a plain subflow endpoint. When the peer
                  does announce addresses, each received ADD_ADDR sub-option
                  will trigger creation of an additional subflow to generate
                  a full mesh topology. This fullmesh flag should always be
                  used in combination with the subflow one to be useful,
                  except for the address used by the initial subflow, where
                  subflow is then optional.

           implicit
                  In some scenarios, an MPTCP subflow can use a local address
                  mapped by an implicit endpoint created by the in-kernel
                  path manager. Once set, the implicit flag cannot be
                  removed, but other flags can be added to the endpoint.
                  Implicit endpoints cannot be created from user-space.

           The limits object specifies the constraints for subflow creations:

           ip mptcp limits show   get current MPTCP subflow creation limits
           ip mptcp limits set    change the MPTCP subflow creation limits

           SUBFLOW_NR
                  specifies the maximum number of additional subflows allowed
                  for each MPTCP connection. Additional subflows can be
                  created due to: incoming accepted ADD_ADDR sub-option,
                  local subflow endpoints, additional subflows started by the
                  peer.

           ADD_ADDR_ACCEPTED_NR
                  specifies the maximum number of incoming ADD_ADDR sub-
                  options accepted for each MPTCP connection. After receiving
                  the specified number of ADD_ADDR sub-options, any other
                  incoming one will be ignored for the MPTCP connection
                  lifetime. When an ADD_ADDR sub-option is accepted and there
                  are no local fullmesh endpoints, the MPTCP path manager
                  will try to create a new subflow using the address in the
                  ADD_ADDR sub-option as the destination address and a source
                  address determined using local routing resolution When
                  fullmesh endpoints are available, the MPTCP path manager
                  will try to create new subflows using each fullmesh
                  endpoint as a source address and the peer's ADD_ADDR
                  address as the destination.  In both cases the SUBFLOW_NR
                  limit is enforced.

           monitor displays creation and deletion of MPTCP connections as
           well as addition or removal of remote addresses and subflows.

## [](#AUTHOR)AUTHOR

           Original Manpage by Paolo Abeni <pabeni@redhat.com>

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

    iproute2                        4 Apr 2020                    IP-MPTCP(8)

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
