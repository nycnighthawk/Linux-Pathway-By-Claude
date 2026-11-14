---
{"title": "udaddy(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/udaddy.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# udaddy(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UDADDY(1)                       librdmacm                       UDADDY(1)

## [](#NAME)NAME

           udaddy - RDMA CM datagram setup and simple ping-pong test.

## [](#SYNOPSIS)SYNOPSIS

           udaddy [-s server_address] [-b bind_address] [-c connections]
                     [-C message_count] [-S message_size] [-p port_space]
           udaddy -s server_address [-b bind_address] [-c connections]
                     [-C message_count] [-S message_size] [-t tos] [-p port_space]

## [](#DESCRIPTION)DESCRIPTION

           Establishes a set of unreliable RDMA datagram communication paths
           between two nodes using the librdmacm, optionally transfers
           datagrams between the nodes, then tears down the communication.

## [](#OPTIONS)OPTIONS

           -s server_address
                  The network name or IP address of the server system
                  listening for communication.  The used name or address must
                  route over an RDMA device.  This option must be specified
                  by the client.

           -b bind_address
                  The local network address to bind to.  To bind to any
                  address with IPv6 use -b ::0 .

           -c connections
                  The number of communication paths to establish between the
                  client and server.  The test uses unreliable datagram
                  communication, so no actual connections are formed.
                  (default 1)

           -C message_count
                  The number of messages to transfer over each connection.
                  (default 10)

           -S message_size
                  The size of each message transferred, in bytes.  This value
                  must be smaller than the MTU of the underlying RDMA
                  transport, or an error will occur.  (default 100)

           -t tos Indicates the type of service used for the communication.
                  Type of service is implementation dependent based on subnet
                  configuration.

           -p port_space
                  The port space of the datagram communication.  May be
                  either the RDMA UDP (0x0111) or IPoIB (0x0002) port space.
                  (default RDMA_PS_UDP)

## [](#NOTES)NOTES

           Basic usage is to start udaddy on a server system, then run udaddy
           -s server_name on a client system.

           Because this test maps RDMA resources to userspace, users must
           ensure that they have available system resources and permissions.
           See the libibverbs README file for additional details.

## [](#SEE_ALSO)SEE ALSO

           rdma_cm(7), ucmatose(1), mckey(1), rping(1)

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

    librdmacm                       2007-05-15                      UDADDY(1)

------------------------------------------------------------------------

Pages that refer to this page: [mckey(1)](../man1/mckey.1.html),  [rdma_client(1)](../man1/rdma_client.1.html),  [rdma_server(1)](../man1/rdma_server.1.html),  [rdma_xclient(1)](../man1/rdma_xclient.1.html),  [rdma_xserver(1)](../man1/rdma_xserver.1.html),  [rping(1)](../man1/rping.1.html),  [ucmatose(1)](../man1/ucmatose.1.html),  [rdma_cm(7)](../man7/rdma_cm.7.html)

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
