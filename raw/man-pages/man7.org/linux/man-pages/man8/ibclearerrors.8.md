---
{"title": "ibclearerrors(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ibclearerrors.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ibclearerrors(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IBCLEARERRORS(8)            OpenIB Diagnostics           IBCLEARERRORS(8)

## [](#NAME)NAME

           ibclearerrors - clear error counters in IB subnet

## [](#SYNOPSIS)SYNOPSIS

           ibclearerrors [-h] [-N | -nocolor] [<topology-file> | -C ca_name
           -P ca_port -t(imeout) timeout_ms]

## [](#DESCRIPTION)DESCRIPTION

           ibclearerrors is a script which clears the PMA error counters in
           PortCounters by either walking the IB subnet topology or using an
           already saved topology file.

## [](#OPTIONS)OPTIONS

           -N | -nocolor  use mono rather than color mode

           -C <ca_name>    use the specified ca_name.

           -P <ca_port>    use the specified ca_port.

           -t <timeout_ms> override the default timeout for the solicited
           mads.

## [](#SEE_ALSO)SEE ALSO

           ibnetdiscover(8), perfquery(8)

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

    OpenIB                         May 21, 2007              IBCLEARERRORS(8)

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
