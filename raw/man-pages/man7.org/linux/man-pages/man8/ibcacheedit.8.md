---
{"title": "ibcacheedit(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ibcacheedit.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ibcacheedit(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IBCACHEEDIT(8)             Open IB Diagnostics             IBCACHEEDIT(8)

## [](#NAME)NAME

           ibcacheedit - edit an ibnetdiscover cache

## [](#SYNOPSIS)SYNOPSIS

           ibcacheedit [options] <orig.cache> <new.cache>

## [](#DESCRIPTION)DESCRIPTION

           ibcacheedit allows users to edit an ibnetdiscover cache created
           through the --cache option in ibnetdiscover(8) .

## [](#OPTIONS)OPTIONS

           --switchguid BEFOREGUID:AFTERGUID
                  Specify a switchguid that should be changed.  The before
                  and after guid should be separated by a colon.  On
                  switches, port guids are identical to the switch guid, so
                  port guids will be adjusted as well on switches.

           --caguid BEFOREGUID:AFTERGUID
                  Specify a caguid that should be changed.  The before and
                  after guid should be separated by a colon.

           --sysimgguid BEFOREGUID:AFTERGUID
                  Specify a sysimgguid that should be changed.  The before
                  and after guid should be spearated by a colon.

           --portguid NODEGUID:BEFOREGUID:AFTERGUID
                  Specify a portguid that should be changed.  The nodeguid of
                  the port (e.g. switchguid or caguid) should be specified
                  first, followed by a colon, the before port guid, another
                  colon, then the after port guid.  On switches, port guids
                  are identical to the switch guid, so the switch guid will
                  be adjusted as well on switches.

       Debugging flags
           -h, --help      show the usage message

           -V, --version     show the version info.

## [](#AUTHORS)AUTHORS

           Albert Chu
                  <  <chu11@llnl.gov>  >

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

                                    2017-08-21                 IBCACHEEDIT(8)

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
