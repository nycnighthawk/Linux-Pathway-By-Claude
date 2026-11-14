---
{"title": "ibidsverify(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ibidsverify.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ibidsverify(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IBIDSVERIFY(8)             Open IB Diagnostics             IBIDSVERIFY(8)

## [](#NAME)NAME

           ibidsverify - validate IB identifiers in subnet and report errors

## [](#SYNOPSIS)SYNOPSIS

           ibidsverify.pl [-h] [-R]

## [](#DESCRIPTION)DESCRIPTION

           ibidsverify.pl is a perl script which uses a full topology file
           that was created by ibnetdiscover, scans the network to validate
           the LIDs and GUIDs in the subnet. The validation consists of
           checking that there are no zero or duplicate identifiers.

           Finally, ibidsverify.pl will also reuse the cached ibnetdiscover
           output from some of the other diag tools which makes it a bit
           faster than running ibnetdiscover from scratch.

## [](#OPTIONS)OPTIONS

           -R Recalculate the ibnetdiscover information, ie do not use the
           cached information.  This option is slower but should be used if
           the diag tools have not been used for some time or if there are
           other reasons to believe the fabric has changed.

           -C <ca_name>    use the specified ca_name.

           -P <ca_port>    use the specified ca_port.

## [](#EXIT_STATUS)EXIT STATUS

           Exit status is 1 if errors are found, 0 otherwise.

## [](#FILES)FILES

       CONFIG FILE
           /ssd11/FOSS/rdma-core/build/etc/infiniband-diags/ibdiag.conf

           A global config file is provided to set some of the common options
           for all tools.  See supplied config file for details.

## [](#SEE_ALSO)SEE ALSO

           ibnetdiscover(8)

## [](#AUTHOR)AUTHOR

           Hal Rosenstock
                  <  <halr@voltaire.com>  >

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

                                    2017-08-21                 IBIDSVERIFY(8)

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
