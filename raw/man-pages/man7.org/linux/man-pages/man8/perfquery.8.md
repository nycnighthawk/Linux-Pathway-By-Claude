---
{"title": "perfquery(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/perfquery.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perfquery(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    perfquery(8)               Open IB Diagnostics               perfquery(8)

## [](#Name)Name

           perfquery - query InfiniBand port counters on a single port

## [](#SYNOPSIS)SYNOPSIS

           perfquery [options] [<lid|guid> [[port(s)] [reset_mask]]]

## [](#DESCRIPTION)DESCRIPTION

           perfquery uses PerfMgt GMPs to obtain the PortCounters (basic
           performance and error counters), PortExtendedCounters,
           PortXmitDataSL, PortRcvDataSL, PortRcvErrorDetails,
           PortXmitDiscardDetails, PortExtendedSpeedsCounters, or
           PortSamplesControl from the PMA at the node/port specified.
           Optionally shows aggregated counters for all ports of node.
           Finally it can, reset after read, or just reset the counters.

           Note: In PortCounters, PortCountersExtended, PortXmitDataSL, and
           PortRcvDataSL, components that represent Data (e.g. PortXmitData
           and PortRcvData) indicate octets divided by 4 rather than just
           octets.

           Note: Inputting a port of 255 indicates an operation be performed
           on all ports.

           Note: For PortCounters, ExtendedCounters, and resets, multiple
           ports can be specified by either a comma separated list or a port
           range.  See examples below.

## [](#OPTIONS)OPTIONS

           -x, --extended
                  show extended port counters rather than (basic) port
                  counters.  Note that extended port counters attribute is
                  optional.

           -X, --xmtsl
                  show transmit data SL counter. This is an optional counter
                  for QoS.

           -S, --rcvsl
                  show receive data SL counter. This is an optional counter
                  for QoS.

           -D, --xmtdisc
                  show transmit discard details. This is an optional counter.

           -E, --rcverr
                  show receive error details. This is an optional counter.

           -D, --xmtdisc
                  show transmit discard details. This is an optional counter.

           -T, --extended_speeds
                  show extended speeds port counters. This is an optional
                  counter.

           --oprcvcounters
                  show Rcv Counters per Op code. This is an optional counter.

           --flowctlcounters
                  show flow control counters. This is an optional counter.

           --vloppackets
                  show packets received per Op code per VL. This is an
                  optional counter.

           --vlopdata
                  show data received per Op code per VL. This is an optional
                  counter.

           --vlxmitflowctlerrors
                  show flow control update errors per VL. This is an optional
                  counter.

           --vlxmitcounters
                  show ticks waiting to transmit counters per VL. This is an
                  optional counter.

           --swportvlcong
                  show sw port VL congestion. This is an optional counter.

           --rcvcc
                  show Rcv congestion control counters. This is an optional
                  counter.

           --slrcvfecn
                  show SL Rcv FECN counters. This is an optional counter.

           --slrcvbecn
                  show SL Rcv BECN counters. This is an optional counter.

           --xmitcc
                  show Xmit congestion control counters. This is an optional
                  counter.

           --vlxmittimecc
                  show VL Xmit Time congestion control counters. This is an
                  optional counter.

           -c, --smplctl
                  show port samples control.

           -a, --all_ports
                  show aggregated counters for all ports of the destination
                  lid, reset all counters for all ports, or if multiple ports
                  are specified, aggregate the counters of the specified
                  ports.  If the destination lid does not support the
                  AllPortSelect flag, all ports will be iterated through to
                  emulate AllPortSelect behavior.

           -l, --loop_ports
                  If all ports are selected by the user (either through the
                  -a option or port 255) or multiple ports are specified
                  iterate through each port rather than doing than aggregate
                  operation.

           -r, --reset_after_read
                  reset counters after read

           -R, --Reset_only
                  only reset counters

       Addressing Flags
           -G, --Guid     The address specified is a Port GUID

           -L, --Lid   The address specified is a LID

           -s, --sm_port <smlid>     use 'smlid' as the target lid for SA
           queries.

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

       Debugging flags
           -d     raise the IB debugging level.  May be used several times
                  (-ddd or -d -d -d).

           -e     show send and receive errors (timeouts and others)

           -h, --help      show the usage message

           -v, --verbose
                  increase the application verbosity level.  May be used
                  several times (-vv or -v -v -v)

           -V, --version     show the version info.

       Configuration flags
           -t, --timeout <timeout_ms> override the default timeout for the
           solicited mads.

           -y, --m_key <key>
                  use the specified M_key for requests. If non-numeric value
                  (like 'x') is specified then a value will be prompted for.

           --config, -z  <config_file> Specify alternate config file.
              Default:
              /ssd11/FOSS/rdma-core/build/etc/infiniband-diags/ibdiag.conf

## [](#FILES)FILES

       CONFIG FILE
           /ssd11/FOSS/rdma-core/build/etc/infiniband-diags/ibdiag.conf

           A global config file is provided to set some of the common options
           for all tools.  See supplied config file for details.

## [](#EXAMPLES)EXAMPLES

              perfquery                # read local port performance counters
              perfquery 32 1           # read performance counters from lid 32, port 1
              perfquery -x 32 1        # read extended performance counters from lid 32, port 1
              perfquery -a 32          # read perf counters from lid 32, all ports
              perfquery -r 32 1        # read performance counters and reset
              perfquery -x -r 32 1     # read extended performance counters and reset
              perfquery -R 0x20 1      # reset performance counters of port 1 only
              perfquery -x -R 0x20 1   # reset extended performance counters of port 1 only
              perfquery -R -a 32       # reset performance counters of all ports
              perfquery -R 32 2 0x0fff # reset only error counters of port 2
              perfquery -R 32 2 0xf000 # reset only non-error counters of port 2
              perfquery -a 32 1-10     # read performance counters from lid 32, port 1-10, aggregate output
              perfquery -l 32 1-10     # read performance counters from lid 32, port 1-10, output each port
              perfquery -a 32 1,4,8    # read performance counters from lid 32, port 1, 4, and 8, aggregate output
              perfquery -l 32 1,4,8    # read performance counters from lid 32, port 1, 4, and 8, output each port

## [](#AUTHOR)AUTHOR

           Hal Rosenstock
                  < <hal.rosenstock@gmail.com> >

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

                                    2017-08-21                   perfquery(8)

------------------------------------------------------------------------

Pages that refer to this page: [ibcheckerrs(8)](../man8/ibcheckerrs.8.html),  [ibclearcounters(8)](../man8/ibclearcounters.8.html),  [ibclearerrors(8)](../man8/ibclearerrors.8.html),  [ibdatacounts(8)](../man8/ibdatacounts.8.html)

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
