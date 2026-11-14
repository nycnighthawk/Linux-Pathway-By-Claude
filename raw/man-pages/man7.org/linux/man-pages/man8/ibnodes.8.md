---
{"title": "ibnodes(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ibnodes.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ibnodes(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [DEPENDENCIES](#DEPENDENCIES) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IBNODES(8)                  OpenIB Diagnostics                 IBNODES(8)

## [](#NAME)NAME

           IBNODES - show InfiniBand nodes in topology

## [](#SYNOPSIS)SYNOPSIS

           ibnodes [options] [<topology-file>]

## [](#DESCRIPTION)DESCRIPTION

           ibnodes is a script which either walks the IB subnet topology or
           uses an already saved topology file and extracts the IB nodes (CAs
           and switches).

## [](#OPTIONS)OPTIONS

           -C, --Ca <ca_name>    use the specified ca_name.

           -P, --Port <ca_port>    use the specified ca_port.

           -t, --timeout <timeout_ms> override the default timeout for the
           solicited mads.

           -h, --help      show the usage message

           --config, -z  <config_file> Specify alternate config file.
              Default:
              /ssd11/FOSS/rdma-core/build/etc/infiniband-diags/ibdiag.conf

       Local port Selection
           Multiple port/Multiple CA support: when no IB device or port is
           specified (see the "local umad parameters" below), the libibumad
           library selects the port to use by the following criteria:

              1. the first port that is ACTIVE.

              2. if not found, the first port that is UP (physical link up).

              If a port and/or CA name is specified, the libibumad library
              attempts to fulfill the user request, and will fail if it is
              not possible.

              For example:

                  ibaddr                 # use the first port (criteria #1 above)
                  ibaddr -C mthca1       # pick the best port from "mthca1" only.
                  ibaddr -P 2            # use the second (active/up) port from the first available IB device.
                  ibaddr -C mthca0 -P 2  # use the specified port only.

## [](#FILES)FILES

       CONFIG FILE
           /ssd11/FOSS/rdma-core/build/etc/infiniband-diags/ibdiag.conf

           A global config file is provided to set some of the common options
           for all tools.  See supplied config file for details.

       NODE NAME MAP FILE FORMAT
           The node name map is used to specify user friendly names for nodes
           in the output.  GUIDs are used to perform the lookup.

           This functionality is provided by the opensm-libs package.  See
           opensm(8) for the file location for your installation.

           Generically:

              # comment
              <guid> "<name>"

           Example:

              # IB1
              # Line cards
              0x0008f104003f125c "IB1 (Rack 11 slot 1   ) ISR9288/ISR9096 Voltaire sLB-24D"
              0x0008f104003f125d "IB1 (Rack 11 slot 1   ) ISR9288/ISR9096 Voltaire sLB-24D"
              0x0008f104003f10d2 "IB1 (Rack 11 slot 2   ) ISR9288/ISR9096 Voltaire sLB-24D"
              0x0008f104003f10d3 "IB1 (Rack 11 slot 2   ) ISR9288/ISR9096 Voltaire sLB-24D"
              0x0008f104003f10bf "IB1 (Rack 11 slot 12  ) ISR9288/ISR9096 Voltaire sLB-24D"

              # Spines
              0x0008f10400400e2d "IB1 (Rack 11 spine 1   ) ISR9288 Voltaire sFB-12D"
              0x0008f10400400e2e "IB1 (Rack 11 spine 1   ) ISR9288 Voltaire sFB-12D"
              0x0008f10400400e2f "IB1 (Rack 11 spine 1   ) ISR9288 Voltaire sFB-12D"
              0x0008f10400400e31 "IB1 (Rack 11 spine 2   ) ISR9288 Voltaire sFB-12D"
              0x0008f10400400e32 "IB1 (Rack 11 spine 2   ) ISR9288 Voltaire sFB-12D"

              # GUID   Node Name
              0x0008f10400411a08 "SW1  (Rack  3) ISR9024 Voltaire 9024D"
              0x0008f10400411a28 "SW2  (Rack  3) ISR9024 Voltaire 9024D"
              0x0008f10400411a34 "SW3  (Rack  3) ISR9024 Voltaire 9024D"
              0x0008f104004119d0 "SW4  (Rack  3) ISR9024 Voltaire 9024D"

## [](#SEE_ALSO)SEE ALSO

           ibnetdiscover(8)

## [](#DEPENDENCIES)DEPENDENCIES

           ibnetdiscover, ibnetdiscover format

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

                                    2012-05-14                     IBNODES(8)

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
