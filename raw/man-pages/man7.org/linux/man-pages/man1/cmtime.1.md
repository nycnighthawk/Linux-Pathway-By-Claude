---
{"title": "cmtime(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cmtime.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cmtime(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CMTIME(1)                       librdmacm                       CMTIME(1)

## [](#NAME)NAME

           cmtime - RDMA CM connection steps timing test.

## [](#SYNOPSIS)SYNOPSIS

           cmtime -C controller_address
                     (-B bind_interface | -b bind_address)
                     [-L]
                     [-c connections_per_pair] [-P num_peers]
                     [-p controller_port]
                     [-q base_qpn] [-n num_threads]
                     [-m mimic_qp_delay_us] [-r retries]
                     [-t timeout_ms]
                     [-S]

## [](#DESCRIPTION)DESCRIPTION

           Determines min, max, and average times for various "steps" in RDMA
           CM connection setup and teardown between clients and servers.

           To use, start one or more servers (-L), plus one or more clients.
           Each client will establish -c number of connections to each
           server.  By default, the test runs with 1 client and 1 server.

           One process will act as a controller process.  The controller
           coordinates the clients and servers -- uses out-of-band sockets to
           collect and distribute addresses and keeps clients and servers in
           sync as they advance through each "step".

           "Steps" that are timed are: create ID, bind address, resolve
           address, resolve route, create QP, modify QP to INIT, modify QP to
           RTR, modify QP to RTS, CM connect, client establish, disconnect,
           destroy QP, and destroy ID.

           Many operations are asynchronous, allowing progress on multiple
           connections simultanesously.  The 'sum' output adds the time that
           all connections took for a given step.  The average 'us/conn' is
           the sum divided by the number of connections.  This is useful to
           identify steps which take a significant amount of time.  The min
           and max values are the smallest and largest times that any single
           connection took to complete a given step.

           The 'total' and 'avg/iter' times measure the time to complete a
           given step for all connections.  These two values take into
           account asynchronous operations.  For steps which are serial, the
           total and sum values will be roughly the same.  For asynchronous
           steps, the total may be significantly lower than the sum, as
           multiple connections will be in progress simultanesously.  The
           avg/iter is the total time divided by the number of connections.

           In many cases, times may not be available or only available on the
           clients.  Is such situations, the output will show 0.  Stats
           printed by each instance pertain to connections handled by it --
           on runs with multiple clients and/or servers (-P > 2) further
           external aggregation might be required.

## [](#OPTIONS)OPTIONS

           -C controller_address
                  The network name or IP address of the instance which will
                  provide step synchronization.  This option must be
                  specified by all instances.  The first instance to start
                  which discovers this address as local will act as
                  controller and will synchronize all other instances via an
                  out-of-band channel as benchmark steps progress.  Any type
                  of instance (client or server) can act as controller.

           -B bind_interface
                  The local RDMA interface to bind to.  Only one of -B or -b
                  is accepted.

           -b bind_address
                  The local network address to bind to.  Only one of -B or -b
                  is accepted.

           -L     Whether this instance is an RDMA CM server (set) or client
                  (unset).  (default client/unset) -c connections_per_pair
                  The number of connections to establish between each client-
                  server pair.  (default 100)

           -P num_peers
                  Total number of peers (clients, servers) which are going to
                  be started.  (default 2)

           -p controller_port
                  The controller's port number.

           -q base_qpn
                  The first QP number to use when creating connections
                  without allocating hardware QPs.  The test will use the
                  values between base_qpn and base_qpn plus connections when
                  connecting.  (default 1000)

           -n num_threads
                  Sets the number of threads to spawn used to process
                  connection events and hardware operations.  (default 1)

           -m mimic_qp_delay_us
                  "Simulates" QP creation and modify calls by replacing them
                  with a simple sleep function instead.  This allows testing
                  the CM at larger scale than would be practical, or even
                  possible given system configuration settings, if HW
                  resources needed to be allocated.

           -r retries
                  Number of retries when resolving address or route.
                  (default 2)

           -S     Run connection rate test using sockets.  This provides a
                  baseline comparison of RDMA connections versus TCP
                  connections.  Sockets are set to blocking mode.  Only
                  supported in 1 client 1 server mode (-P 2).

           -t timeout_ms
                  Timeout in millseconds (ms) when resolving address or
                  route.  (default 2000 - 2 seconds)

## [](#EXAMPLES)EXAMPLES

           One client connecting to one server:

             server$ cmtime -B enp1s0f0np0 -C 192.0.2.1 -L
             client$ cmtime -B enp1s0f0np0 -C 192.0.2.1

           Two clients connecting to three servers, 6k connections in total:

             client1$ cmtime -B enp1s0f0np0 -P 5 -C 192.0.2.1 -c 1000
             client2$ cmtime -B enp1s0f0np0 -P 5 -C 192.0.2.1 -c 1000
             server1$ cmtime -B enp1s0f0np0 -P 5 -C 192.0.2.1 -c 1000 -L
             server2$ cmtime -B enp1s0f0np0 -P 5 -C 192.0.2.1 -c 1000 -L
             server3$ cmtime -B enp1s0f0np0 -P 5 -C 192.0.2.1 -c 1000 -L

## [](#NOTES)NOTES

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

    librdmacm                       2025-09-03                      CMTIME(1)

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
