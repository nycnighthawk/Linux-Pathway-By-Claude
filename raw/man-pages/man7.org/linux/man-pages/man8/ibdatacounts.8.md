---
{"title": "ibdatacounts(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ibdatacounts.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ibdatacounts(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IBDATACOUNTS(8)             OpenIB Diagnostics            IBDATACOUNTS(8)

## [](#NAME)NAME

           ibdatacounts - get IB port data counters

## [](#SYNOPSIS)SYNOPSIS

           ibdatacounts [-h] [-b] [-v] [-G] [-N | -nocolor] [-C ca_name] [-P
           ca_port] [-t(imeout) timeout_ms] <lid|guid> [<port>]

## [](#DESCRIPTION)DESCRIPTION

           Obtain PMA data counters from specified port (or node).  Port
           address is lid unless -G option is used to specify a GUID address.

## [](#OPTIONS)OPTIONS

           -G      use GUID address argument. In most cases, it is the Port
           GUID.
                   Example:
                   "0x08f1040023"

           -v      increase the verbosity level

           -b      brief mode

           -N | -nocolor use mono rather than color mode

           -C <ca_name>    use the specified ca_name.

           -P <ca_port>    use the specified ca_port.

           -t <timeout_ms> override the default timeout for the solicited
           mads.

## [](#EXAMPLE)EXAMPLE

           ibdatacounts 2           # show data counters for lid 2

           ibdatacounts 2   4       # show data counters for lid 2 port 4

## [](#SEE_ALSO)SEE ALSO

           perfquery(8), ibaddr(8)

## [](#AUTHOR)AUTHOR

           Hal Rosenstock
                  <halr@voltaire.com>

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

    OpenIB                         May 30, 2007               IBDATACOUNTS(8)

------------------------------------------------------------------------

Pages that refer to this page: [ibdatacounters(8)](../man8/ibdatacounters.8.html)

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
