---
{"title": "ib_acme(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ib_acme.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ib_acme(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ib_acme(1)                       ib_acme                       ib_acme(1)

## [](#NAME)NAME

           ib_acme - test and configuration utility for the IB ACM

## [](#SYNOPSIS)SYNOPSIS

           ib_acme [-f addr_format] [-s src_addr] -d dest_addr [-v] [-c] [-e] [-P] [-S svc_addr] [-C repetitions]
           ib_acme [-A [addr_file]] [-O [opt_file]] [-D dest_dir] [-V]

## [](#DESCRIPTION)DESCRIPTION

           ib_acme provides assistance configuring and testing the ibacm
           service.  The first usage of the service will test that the ibacm
           is running and operating correctly.  The second usage model will
           automatically create address and configuration files for the ibacm
           service.

## [](#OPTIONS)OPTIONS

           -f addr_format
                  Specifies the format of the src_addr and dest_addr
                  parameters.  Valid address formats are: 'i' ip address, 'n'
                  host name, 'l' lid, 'g' gid, and 'u' unspecified.  If the
                  -f option is omitted, an unspecified address format is
                  assumed.  ib_acme will use getaddrinfo or other mechanisms
                  to determine which format the address uses.

           -s src_addr
                  Specifies the local source address of the path to resolve.
                  The source address can be an IP address, system network
                  name, or LID, as indicated by the addr_format option.

           -d dest_addr
                  Specifies the destination address of the path to resolve.
                  The destination address can be an IP address, system
                  network name, or LID, as indicated by the addr_format
                  option.

           -v     Indicates that the resolved path information should be
                  verified with the active IB SA.  Use of the -v option
                  provides a sanity check that resolved path information is
                  usable given the current cluster configuration.

           -c     Instructs the ACM service to only returned information that
                  currently resides in its local cache.

           -e [N] Displays one (N = 1, 2, ...) or all endpoints (N = 0 or not
                  present).

           -P [opt]
                  Queries performance data from the destination service.
                  Valid options are: "col" for outputting combined data in
                  column format,  "N" (N = 1, 2, ...) for outputting data for
                  a specific endpoint N,  "all" for outputting data for all
                  endpoints,  and "s" for outputting data for a specific
                  endpoint with the address given by the -s option.

           -S svc_addr
                  Hostname, IPv4-address or Unix-domain socket of ACM
                  service, default: /run/ibacm.sock

           -C repetitions
                  number of repetitions to perform resolution.  Used to
                  measure performance of ACM cache lookups.  Defaults to 1.

           -A [addr_file]
                  With this option, the ib_acme utility automatically
                  generates the address configuration file ibacm_addr.cfg.
                  The generated file is constructed using the system host
                  name.

           -O [opt_file]
                  With this option, the ib_acme utility automatically
                  generates the option configuration file ibacm_opts.cfg.
                  The generated file is currently generated using static
                  information.

           -D dest_dir
                  Specify the destination directory for the output files.

           -V     Enables verbose output.  When combined with -A or -O
                  options, ib_acme will display additional details, such as
                  generated address information saved to the ibacm_addr.cfg
                  file.

## [](#NOTES)NOTES

           The ib_acme utility performs two main functions.  With the -A and
           -O options, it automatically generates address or options
           configuration files.  The generated files are text based and may
           be edited.  These options are intended to provide a simple way to
           configure address and option information on all nodes on a
           cluster.

           The other function of the ib_acme utility is to test the ibacm
           service, including helping to verify that the service is usable
           given the current cluster configuration.  The ib_acme utility can
           resolve IP addresses, network names, or IB LIDs into a path
           record.  It can then compare that path record against one obtained
           by the SA.  When used to test the ibacm service, the ib_acme
           utility has the side effect of loading the ibacm caches.

           Multiple, numerical destinations can be specified by adding
           brackets [] to the end of a base destination name or address.
           Users may specify a list of numerical ranges inside the brackets
           using the following example as a guide: node[1-3,5,7-8].  This
           will result in testing node1, node2, node3, node5, node7, and
           node8.

## [](#SEE_ALSO)SEE ALSO

           ibacm(7), ibacm(8)

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

    ib_acme                         2014-06-16                     ib_acme(1)

------------------------------------------------------------------------

Pages that refer to this page: [ibacm(7)](../man7/ibacm.7.html),  [ibacm(8)](../man8/ibacm.8.html)

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
