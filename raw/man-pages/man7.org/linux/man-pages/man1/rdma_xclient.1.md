---
{"title": "rdma_xclient(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rdma_xclient.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rdma_xclient(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RDMA_XCLIENT(1)                 librdmacm                 RDMA_XCLIENT(1)

## [](#NAME)NAME

           rdma_xclient - RDMA CM communication client test program

## [](#SYNOPSIS)SYNOPSIS

           rdma_xclient [-s server_address] [-p server_port] [-c comm_type]

## [](#DESCRIPTION)DESCRIPTION

           Uses synchronous librdmam calls to establish an RDMA connection
           between two nodes.  This example is intended to provide a very
           simple coding example of how to use RDMA.

## [](#OPTIONS)OPTIONS

           -s server_address
                  Specifies the address of the system that the rdma_server is
                  running on.  By default, the client will attempt to connect
                  to the server using 127.0.0.1.

           -p server_port
                  Specifies the port number that the server listens on.  By
                  default the server listens on port 7471.

           -c communication type
                  Specifies the type of communication established with the
                  server program.  'r' results in using a reliable-connected
                  QP (the default).  'x' uses extended reliable-connected XRC
                  QPs.

## [](#NOTES)NOTES

           Basic usage is to start rdma_xserver, then connect to the server
           using the rdma_client program.

           Because this test maps RDMA resources to userspace, users must
           ensure that they have available system resources and permissions.
           See the libibverbs README file for additional details.

## [](#SEE_ALSO)SEE ALSO

           rdma_cm(7), udaddy(1), mckey(1), rping(1), rdma_xserver(1),
           rdma_client(1)

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

    librdmacm                       2011-06-15                RDMA_XCLIENT(1)

------------------------------------------------------------------------

Pages that refer to this page: [rdma_xserver(1)](../man1/rdma_xserver.1.html)

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
