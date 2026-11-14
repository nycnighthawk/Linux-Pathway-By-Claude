---
{"title": "ibacm(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/ibacm.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ibacm(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [RETURN CODES](#RETURN_CODES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IBACM(7)                    IB ACM User Guide                    IBACM(7)

## [](#NAME)NAME

           ibacm - InfiniBand communication management assistant

## [](#SYNOPSIS)SYNOPSIS

           #include <infiniband/acm.h>

## [](#DESCRIPTION)DESCRIPTION

           Used to resolve remote endpoint information before establishing
           communications over InfiniBand.

## [](#NOTES)NOTES

           Th IB ACM provides scalable address and route resolution services
           over InfiniBand.  It resolves system network names and IP
           addresses to InfiniBand path record data using efficient
           mechanisms, including caching of data.

           The IB ACM provides information needed to establish a connection,
           but does not implement the communication management protocol.  It
           provides services similar to rdma_getaddrinfo, rdma_resolve_addr,
           and rdma_resolve_route using IB multicast.  The IB ACM does not
           require IPoIB or use standard naming services, such as DNS, and
           limits network communication, especially with the IB SA.  The
           ib_acme utility assists in verifying what options of the ibacm
           service may be usable for the current fabric topology.

           Client interactions with the ibacm service are done over sockets
           through a standard TCP connection.  The librdmacm abstracts this
           interaction.

## [](#RETURN_CODES)RETURN CODES

           == 0   success

           != 0   error

## [](#SEE_ALSO)SEE ALSO

           ib_acme(1), ibacm(8)

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

    IBACM                           2014-06-16                       IBACM(7)

------------------------------------------------------------------------

Pages that refer to this page: [ib_acme(1)](../man1/ib_acme.1.html),  [ibacm(8)](../man8/ibacm.8.html)

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
