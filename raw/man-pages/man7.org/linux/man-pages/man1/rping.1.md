---
{"title": "rping(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rping.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rping(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPING(1)                        librdmacm                        RPING(1)

## [](#NAME)NAME

           rping - RDMA CM connection and RDMA ping-pong test.

## [](#SYNOPSIS)SYNOPSIS

           rping -s [-v] [-V] [-d] [-P] [-a address] [-p port]
                     [-C message_count] [-S message_size]
           rping -c [-v] [-V] [-d] [-I address] -a address [-p port]
                     [-C message_count] [-S message_size]

## [](#DESCRIPTION)DESCRIPTION

           Establishes a reliable RDMA connection between two nodes using the
           librdmacm, optionally performs RDMA transfers between the nodes,
           then disconnects.

## [](#OPTIONS)OPTIONS

           -s     Run as the server.

           -c     Run as the client.

           -a address
                  On the server, specifies the network address to bind the
                  connection to.  To bind to any address with IPv6 use -a ::0
                  .  On the client, specifies the server address to connect
                  to.

           -I address
                  The address to bind to as the source IP address to use.
                  This is useful if you have multiple addresses on the same
                  network or complex routing.

           -p     Port number for listening server.

           -v     Display ping data.

           -V     Validate ping data.

           -d     Display debug information.

           -C message_count
                  The number of messages to transfer over each connection.
                  (default infinite)

           -S message_size
                  The size of each message transferred, in bytes.  (default
                  100)

           -P     Run the server in persistent mode.  This allows multiple
                  rping clients to connect to a single server instance. The
                  server will run until killed.

           -q     Control QP Creation/Modification directly from the
                  application, instead of rdma_cm.

## [](#NOTES)NOTES

           Because this test maps RDMA resources to userspace, users must
           ensure that they have available system resources and permissions.
           See the libibverbs README file for additional details.

## [](#SEE_ALSO)SEE ALSO

           rdma_cm(7), ucmatose(1), udaddy(1), mckey(1)

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

    librdmacm                       2007-05-15                       RPING(1)

------------------------------------------------------------------------

Pages that refer to this page: [mckey(1)](../man1/mckey.1.html),  [rdma_client(1)](../man1/rdma_client.1.html),  [rdma_server(1)](../man1/rdma_server.1.html),  [rdma_xclient(1)](../man1/rdma_xclient.1.html),  [rdma_xserver(1)](../man1/rdma_xserver.1.html),  [ucmatose(1)](../man1/ucmatose.1.html),  [udaddy(1)](../man1/udaddy.1.html),  [rdma_cm(7)](../man7/rdma_cm.7.html)

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
