---
{"title": "rdma_cm(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/rdma_cm.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rdma_cm(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [RDMA VERBS](#RDMA_VERBS) \| [CLIENT OPERATION](#CLIENT_OPERATION) \| [SERVER OPERATION](#SERVER_OPERATION) \| [RETURN CODES](#RETURN_CODES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RDMA_CM(7)            Librdmacm Programmer's Manual            RDMA_CM(7)

## [](#NAME)NAME

           rdma_cm - RDMA communication manager.

## [](#SYNOPSIS)SYNOPSIS

           #include <rdma/rdma_cma.h>

## [](#DESCRIPTION)DESCRIPTION

           Used to establish communication over RDMA transports.

## [](#NOTES)NOTES

           The RDMA CM is a communication manager used to setup reliable,
           connected and unreliable datagram data transfers.  It provides an
           RDMA transport neutral interface for establishing connections.
           The API concepts are based on sockets, but adapted for queue pair
           (QP) based semantics: communication must be over a specific RDMA
           device, and data transfers are message based.

           The RDMA CM can control both the QP and communication management
           (connection setup / teardown) portions of an RDMA API, or only the
           communication management piece.  It works in conjunction with the
           verbs API defined by the libibverbs library.  The libibverbs
           library provides the underlying interfaces needed to send and
           receive data.

           The RDMA CM can operate asynchronously or synchronously.  The mode
           of operation is controlled by the user through the use of the
           rdma_cm event channel parameter in specific calls.  If an event
           channel is provided, an rdma_cm identifier will report its event
           data (results of connecting, for example), on that channel.  If a
           channel is not provided, then all rdma_cm operations for the
           selected rdma_cm identifier will block until they complete.

           The RDMA CM gives an option to different libibverbs providers to
           advertise and use various specific to that provider QP
           configuration options. This functionality is called ECE (enhanced
           connection establishment).

## [](#RDMA_VERBS)RDMA VERBS

           The rdma_cm supports the full range of verbs available through the
           libibverbs library and interfaces.  However, it also provides
           wrapper functions for some of the more commonly used verbs
           funcationality.  The full set of abstracted verb calls are:

           rdma_reg_msgs  - register an array of buffers for sending and
           receiving

           rdma_reg_read  - registers a buffer for RDMA read operations

           rdma_reg_write - registers a buffer for RDMA write operations

           rdma_dereg_mr  - deregisters a memory region

           rdma_post_recv  - post a buffer to receive a message

           rdma_post_send  - post a buffer to send a message

           rdma_post_read  - post an RDMA to read data into a buffer

           rdma_post_write - post an RDMA to send data from a buffer

           rdma_post_recvv  - post a vector of buffers to receive a message

           rdma_post_sendv  - post a vector of buffers to send a message

           rdma_post_readv  - post a vector of buffers to receive an RDMA
           read

           rdma_post_writev - post a vector of buffers to send an RDMA write

           rdma_post_ud_send - post a buffer to send a message on a UD QP

           rdma_get_send_comp - get completion status for a send or RDMA
           operation

           rdma_get_recv_comp - get information about a completed receive

## [](#CLIENT_OPERATION)CLIENT OPERATION

           This section provides a general overview of the basic operation
           for the active, or client, side of communication.  This flow
           assume asynchronous operation with low level call details shown.
           For synchronous operation, calls to rdma_create_event_channel,
           rdma_get_cm_event, rdma_ack_cm_event, and
           rdma_destroy_event_channel would be eliminated.  Abstracted calls,
           such as rdma_create_ep encapsulate several of these calls under a
           single API.  Users may also refer to the example applications for
           code samples.  A general connection flow would be:

           rdma_getaddrinfo
                  retrieve address information of the destination

           rdma_create_event_channel
                  create channel to receive events

           rdma_create_id
                  allocate an rdma_cm_id, this is conceptually similar to a
                  socket

           rdma_resolve_addr
                  obtain a local RDMA device to reach the remote address

           rdma_get_cm_event
                  wait for RDMA_CM_EVENT_ADDR_RESOLVED event

           rdma_ack_cm_event
                  ack event

           rdma_create_qp
                  allocate a QP for the communication

           rdma_resolve_route
                  determine the route to the remote address

           rdma_get_cm_event
                  wait for RDMA_CM_EVENT_ROUTE_RESOLVED event

           rdma_ack_cm_event
                  ack event

           rdma_connect
                  connect to the remote server

           rdma_get_cm_event
                  wait for RDMA_CM_EVENT_ESTABLISHED event

           rdma_ack_cm_event
                  ack event

           Perform data transfers over connection

           rdma_disconnect
                  tear-down connection

           rdma_get_cm_event
                  wait for RDMA_CM_EVENT_DISCONNECTED event

           rdma_ack_cm_event
                  ack event

           rdma_destroy_qp
                  destroy the QP

           rdma_destroy_id
                  release the rdma_cm_id

           rdma_destroy_event_channel
                  release the event channel

           rdma_freeaddrinfo
                  release the list of rdma_addrinfo structures

           rdma_set_local_ece
                  set desired ECE options

           An almost identical process is used to setup unreliable datagram
           (UD) communication between nodes.  No actual connection is formed
           between QPs however, so disconnection is not needed.

           Although this example shows the client initiating the disconnect,
           either side of a connection may initiate the disconnect.

## [](#SERVER_OPERATION)SERVER OPERATION

           This section provides a general overview of the basic operation
           for the passive, or server, side of communication.  A general
           connection flow would be:

           rdma_create_event_channel
                  create channel to receive events

           rdma_create_id
                  allocate an rdma_cm_id, this is conceptually similar to a
                  socket

           rdma_bind_addr
                  set the local port number to listen on

           rdma_listen
                  begin listening for connection requests

           rdma_get_cm_event
                  wait for RDMA_CM_EVENT_CONNECT_REQUEST event with a new
                  rdma_cm_id

           rdma_create_qp
                  allocate a QP for the communication on the new rdma_cm_id

           rdma_accept
                  accept the connection request

           rdma_ack_cm_event
                  ack event

           rdma_get_cm_event
                  wait for RDMA_CM_EVENT_ESTABLISHED event

           rdma_ack_cm_event
                  ack event

           Perform data transfers over connection

           rdma_get_cm_event
                  wait for RDMA_CM_EVENT_DISCONNECTED event

           rdma_ack_cm_event
                  ack event

           rdma_disconnect
                  tear-down connection

           rdma_destroy_qp
                  destroy the QP

           rdma_destroy_id
                  release the connected rdma_cm_id

           rdma_destroy_id
                  release the listening rdma_cm_id

           rdma_destroy_event_channel
                  release the event channel

           rdma_get_remote_ece
                  get ECe options sent by the client

           rdma_set_local_ece
                  set desired ECE options

## [](#RETURN_CODES)RETURN CODES

           =  0   success

           = -1   error - see errno for more details

           Most librdmacm functions return 0 to indicate success, and a -1
           return value to indicate failure.  If a function operates
           asynchronously, a return value of 0 means that the operation was
           successfully started.  The operation could still complete in
           error; users should check the status of the related event.  If the
           return value is -1, then errno will contain additional information
           regarding the reason for the failure.

           Prior versions of the library would return -errno and not set
           errno for some cases related to ENOMEM, ENODEV, ENODATA, EINVAL,
           and EADDRNOTAVAIL codes. Applications that want to check these
           codes and have compatibility with prior library versions must
           manually set errno to the negative of the return code if it is <
           -1.

## [](#SEE_ALSO)SEE ALSO

           rdma_accept(3), rdma_ack_cm_event(3), rdma_bind_addr(3),
           rdma_connect(3), rdma_create_ep(3), rdma_create_event_channel(3),
           rdma_create_id(3), rdma_create_qp(3), rdma_dereg_mr(3),
           rdma_destroy_ep(3), rdma_destroy_event_channel(3),
           rdma_destroy_id(3), rdma_destroy_qp(3), rdma_disconnect(3),
           rdma_event_str(3), rdma_free_devices(3), rdma_freeaddrinfo(3),
           rdma_getaddrinfo(3), rdma_get_cm_event(3), rdma_get_devices(3),
           rdma_get_dst_port(3), rdma_get_local_addr(3),
           rdma_get_peer_addr(3), rdma_get_recv_comp(3),
           rdma_get_remote_ece(3), rdma_get_request(3),
           rdma_get_send_comp(3), rdma_get_src_port(3),
           rdma_join_multicast(3), rdma_leave_multicast(3), rdma_listen(3),
           rdma_migrate_id(3), rdma_notify(3), rdma_post_read(3)
           rdma_post_readv(3), rdma_post_recv(3), rdma_post_recvv(3),
           rdma_post_send(3), rdma_post_sendv(3), rdma_post_ud_send(3),
           rdma_post_write(3), rdma_post_writev(3), rdma_query_addrinfo(3),
           rdma_reg_msgs(3), rdma_reg_read(3), rdma_reg_write(3),
           rdma_reject(3), rdma_resolve_addr(3), rdma_resolve_addrinfo(3),
           rdma_resolve_route(3), rdma_get_remote_ece(3), rdma_set_option(3),
           rdma_write_cm_event(3), mckey(1), rdma_client(1), rdma_server(1),
           rping(1), ucmatose(1), udaddy(1)

## [](#COLOPHON)COLOPHON

           This page is part of the rdma-core (RDMA Core Userspace Libraries
           and Daemons) project.  Information about the project can be found
           at ⟨https://github.com/linux-rdma/rdma-core⟩.  If you have a bug
           report for this manual page, send it to
           linux-rdma@vger.kernel.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/linux-rdma/rdma-core.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    librdmacm                       2010-07-19                     RDMA_CM(7)

------------------------------------------------------------------------

Pages that refer to this page: [cmtime(1)](../man1/cmtime.1.html),  [mckey(1)](../man1/mckey.1.html),  [rcopy(1)](../man1/rcopy.1.html),  [rdma_client(1)](../man1/rdma_client.1.html),  [rdma_server(1)](../man1/rdma_server.1.html),  [rdma_xclient(1)](../man1/rdma_xclient.1.html),  [rdma_xserver(1)](../man1/rdma_xserver.1.html),  [riostream(1)](../man1/riostream.1.html),  [rping(1)](../man1/rping.1.html),  [rstream(1)](../man1/rstream.1.html),  [ucmatose(1)](../man1/ucmatose.1.html),  [udaddy(1)](../man1/udaddy.1.html),  [udpong(1)](../man1/udpong.1.html),  [rdma_connect(3)](../man3/rdma_connect.3.html),  [rdma_create_ep(3)](../man3/rdma_create_ep.3.html),  [rdma_create_event_channel(3)](../man3/rdma_create_event_channel.3.html),  [rdma_create_id(3)](../man3/rdma_create_id.3.html),  [rdma_dereg_mr(3)](../man3/rdma_dereg_mr.3.html),  [rdma_get_recv_comp(3)](../man3/rdma_get_recv_comp.3.html),  [rdma_get_remote_ece(3)](../man3/rdma_get_remote_ece.3.html),  [rdma_get_send_comp(3)](../man3/rdma_get_send_comp.3.html),  [rdma_init_qp_attr(3)](../man3/rdma_init_qp_attr.3.html),  [rdma_listen(3)](../man3/rdma_listen.3.html),  [rdma_migrate_id(3)](../man3/rdma_migrate_id.3.html),  [rdma_post_read(3)](../man3/rdma_post_read.3.html),  [rdma_post_readv(3)](../man3/rdma_post_readv.3.html),  [rdma_post_recv(3)](../man3/rdma_post_recv.3.html),  [rdma_post_recvv(3)](../man3/rdma_post_recvv.3.html),  [rdma_post_send(3)](../man3/rdma_post_send.3.html),  [rdma_post_sendv(3)](../man3/rdma_post_sendv.3.html),  [rdma_post_ud_send(3)](../man3/rdma_post_ud_send.3.html),  [rdma_post_write(3)](../man3/rdma_post_write.3.html),  [rdma_post_writev(3)](../man3/rdma_post_writev.3.html),  [rdma_reg_msgs(3)](../man3/rdma_reg_msgs.3.html),  [rdma_reg_read(3)](../man3/rdma_reg_read.3.html),  [rdma_reg_write(3)](../man3/rdma_reg_write.3.html),  [rdma_set_local_ece(3)](../man3/rdma_set_local_ece.3.html),  [ibacm(8)](../man8/ibacm.8.html)

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
