---
{"title": "ucmatose(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ucmatose.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ucmatose(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UCMATOSE(1)                     librdmacm                     UCMATOSE(1)

## [](#NAME)NAME

           ucmatose - RDMA CM connection and simple ping-pong test.

## [](#SYNOPSIS)SYNOPSIS

           ucmatose [-s server_address] [-b bind_address]
                     [-f address_format] [-P port_space]
                     [-c connections] [-C message_count] [-S message_size] [-a ack_timeout]
           ucmatose -s server_address [-b bind_address]
                     [-f address_format] [-P port_space]
                     [-c connections] [-C message_count] [-S message_size] [-t tos] [-a ack_timeout]

## [](#DESCRIPTION)DESCRIPTION

           Establishes a set of reliable RDMA connections between two nodes
           using the librdmacm, optionally transfers data between the nodes,
           then disconnects.

## [](#OPTIONS)OPTIONS

           -s server_address
                  The network name or IP address of the server system
                  listening for connections.  The used name or address must
                  route over an RDMA device.  This option must be specified
                  by the client.

           -b bind_address
                  The local network address to bind to.  To bind to any
                  address with IPv6 use -b ::0 .

           -f address_format
                  Specifies the format of the server and bind address.  Be
                  default, the format is determined by getaddrinfo() as
                  either being a hostname, an IPv4 address, or an IPv6
                  address.  This option may be used to indicate that a
                  specific address format has been provided.  Supported
                  address_format values are: name, ip, ipv6, and gid.

           -P port_space
                  Specifies the port space for the connection.  Be default,
                  the port space is the RDMA TCP port space. (Note that the
                  RDMA port space may be separate from that used for IP.)
                  Supported port_space values are: tcp and ib.

           -c connections
                  The number of connections to establish between the client
                  and server.  (default 1)

           -C message_count
                  The number of messages to transfer over each connection.
                  (default 10)

           -S message_size
                  The size of each message transferred, in bytes.  (default
                  100)

           -t tos Indicates the type of service used for the communication.
                  Type of service is implementation dependent based on subnet
                  configuration.

           -a ack_timeout
                  Indicates the QP ACK timeout value that should be used.
                  The value calculated according to the formula 4.096 *
                  2^(ack_timeout) usec.

           -m     Tests event channel migration.  Migrates all communication
                  identifiers to a different event channel for disconnect
                  events.

## [](#NOTES)NOTES

           Basic usage is to start ucmatose on a server system, then run
           ucmatose -s server_name on a client system.

           Because this test maps RDMA resources to userspace, users must
           ensure that they have available system resources and permissions.
           See the libibverbs README file for additional details.

## [](#SEE_ALSO)SEE ALSO

           rdma_cm(7), udaddy(1), mckey(1), rping(1)

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

    librdmacm                       2007-05-15                    UCMATOSE(1)

------------------------------------------------------------------------

Pages that refer to this page: [mckey(1)](../man1/mckey.1.html),  [rping(1)](../man1/rping.1.html),  [udaddy(1)](../man1/udaddy.1.html),  [rdma_cm(7)](../man7/rdma_cm.7.html)

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
