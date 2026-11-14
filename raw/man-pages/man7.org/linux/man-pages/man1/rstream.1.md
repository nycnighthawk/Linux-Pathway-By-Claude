---
{"title": "rstream(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rstream.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rstream(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RSTREAM(1)                      librdmacm                      RSTREAM(1)

## [](#NAME)NAME

           rstream - streaming over RDMA ping-pong test.

## [](#SYNOPSIS)SYNOPSIS

           rstream [-s server_address] [-b bind_address] [-f address_format]
                          [-B buffer_size] [-I iterations] [-C transfer_count]
                          [-S transfer_size] [-p server_port] [-T test_option]

## [](#DESCRIPTION)DESCRIPTION

           Uses the streaming over RDMA protocol (rsocket) to connect and
           exchange data between a client and server application.

## [](#OPTIONS)OPTIONS

           -s server_address
                  The network name or IP address of the server system
                  listening for connections.  The used name or address must
                  route over an RDMA device.  This option must be specified
                  by the client.

           -b bind_address
                  The local network address to bind to.

           -f address_format
                  Supported address formats are ip, ipv6, gid, or name.

           -B buffer_size
                  Indicates the size of the send and receive network buffers.

           -I iterations
                  The number of times that the specified number of messages
                  will be exchanged between the client and server.  (default
                  1000)

           -C transfer_count
                  The number of messages to transfer from the client to the
                  server and back again on each iteration.  (default 1000)

           -S transfer_size
                  The size of each send transfer, in bytes.  (default 1000)
                  If 'all' is specified, rstream will run a series of tests
                  of various sizes.

           -p server_port
                  The server's port number.

           -T test_option
                  Specifies test parameters.  Available options are:

           s | socket  - uses standard socket calls to transfer data

           a | async - uses asynchronous operation (e.g. select / poll)

           b | blocking - uses blocking calls

           f | fork - fork server processing (forces -T s option)

           n | nonblocking - uses non-blocking calls

           r | resolve - use rdma cm to resolve address

           v | verify - verifies data transfers

## [](#NOTES)NOTES

           Basic usage is to start rstream on a server system, then run
           rstream -s server_name on a client system.  By default, rstream
           will run a series of latency and bandwidth performance tests.
           Specifying a different iterations, transfer_count, or
           transfer_size will run a user customized test using default values
           where none have been specified.

           Because this test maps RDMA resources to userspace, users must
           ensure that they have available system resources and permissions.
           See the libibverbs README file for additional details.

## [](#SEE_ALSO)SEE ALSO

           rdma_cm(7)

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

    librdmacm                       2011-11-16                     RSTREAM(1)

------------------------------------------------------------------------

Pages that refer to this page: [riostream(1)](../man1/riostream.1.html)

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
