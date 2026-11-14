---
{"title": "ibaddr(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ibaddr.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ibaddr(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IBADDR(8)                   OpenIB Diagnostics                  IBADDR(8)

## [](#Name)Name

           IBADDR - query InfiniBand address(es)

## [](#SYNOPSIS)SYNOPSIS

           ibaddr [options]

## [](#DESCRIPTION)DESCRIPTION

           Display the lid (and range) as well as the GID address of the port
           specified (by DR path, lid, or GUID) or the local port by default.

           Note: this utility can be used as simple address resolver.

## [](#OPTIONS)OPTIONS

           --gid_show, -g show gid address only

           --lid_show, -l show lid range only

           --Lid_show, -L show lid range (in decimal) only

       Addressing Flags
           -D, --Direct     The address specified is a directed route

              Examples:
                 [options] -D [options] "0"          # self port
                 [options] -D [options] "0,1,2,1,4"  # out via port 1, then 2, ...

                 (Note the second number in the path specified must match the port being
                 used.  This can be specified using the port selection flag '-P' or the
                 port found through the automatic selection process.)

           -G, --Guid     The address specified is a Port GUID

           -s, --sm_port <smlid>     use 'smlid' as the target lid for SA
           queries.

       Debugging flags
           -d     raise the IB debugging level.  May be used several times
                  (-ddd or -d -d -d).

           -e     show send and receive errors (timeouts and others)

           -h, --help      show the usage message

           -v, --verbose
                  increase the application verbosity level.  May be used
                  several times (-vv or -v -v -v)

           -V, --version     show the version info.

       Port Selection flags
           -C, --Ca <ca_name>    use the specified ca_name.

           -P, --Port <ca_port>    use the specified ca_port.

           -Y, --pkey-idx <idx>
                  P_Key table index (0-65535, default 0) used for the
                  outgoing SA/GMP MADs.  SMP (SMI directed-route/LID-routed)
                  MADs always use P_Key index 0.

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

       Configuration flags
           -y, --m_key <key>
                  use the specified M_key for requests. If non-numeric value
                  (like 'x') is specified then a value will be prompted for.

           -t, --timeout <timeout_ms> override the default timeout for the
           solicited mads.

           --config, -z  <config_file> Specify alternate config file.
              Default:
              /ssd11/FOSS/rdma-core/build/etc/infiniband-diags/ibdiag.conf

## [](#FILES)FILES

       CONFIG FILE
           /ssd11/FOSS/rdma-core/build/etc/infiniband-diags/ibdiag.conf

           A global config file is provided to set some of the common options
           for all tools.  See supplied config file for details.

## [](#EXAMPLES)EXAMPLES

              ibaddr                  # local port\'s address
              ibaddr 32               # show lid range and gid of lid 32
              ibaddr -G 0x8f1040023   # same but using guid address
              ibaddr -l 32            # show lid range only
              ibaddr -L 32            # show decimal lid range only
              ibaddr -g 32            # show gid address only

## [](#SEE_ALSO)SEE ALSO

           ibroute (8), ibtracert (8)

## [](#AUTHOR)AUTHOR

           Hal Rosenstock
                  < <halr@voltaire.com> >

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

                                    2013-10-11                      IBADDR(8)

------------------------------------------------------------------------

Pages that refer to this page: [ibcheckerrs(8)](../man8/ibcheckerrs.8.html),  [ibchecknode(8)](../man8/ibchecknode.8.html),  [ibcheckport(8)](../man8/ibcheckport.8.html),  [ibcheckportstate(8)](../man8/ibcheckportstate.8.html),  [ibcheckportwidth(8)](../man8/ibcheckportwidth.8.html),  [ibdatacounts(8)](../man8/ibdatacounts.8.html)

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
