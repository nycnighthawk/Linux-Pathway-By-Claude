---
{"title": "ovn-sim(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ovn-sim.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ovn-sim(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [AUTHOR](#AUTHOR) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OVN-SIM(1)              Open Virtual Network (OVN)             OVN-SIM(1)

## [](#NAME)NAME

           ovn-sim - Open Virtual Network simulator environment

## [](#SYNOPSIS)SYNOPSIS

           ovn-sim [option]… [script]…

## [](#DESCRIPTION)DESCRIPTION

           ovn-sim is a wrapper script that adds ovn related commands on top
           of ovs-sim.

           ovs-sim provides a convenient environment for running one or more
           Open vSwitch instances and related software in a sandboxed
           simulation environment.

           To use ovn-sim, first build Open vSwitch, then invoke it directly
           from the build directory, e.g.:

              git clone https://github.com/openvswitch/ovs.git
              cd ovs
              ./boot.sh && ./configure && make
              cd ..
              git clone https://github.com/ovn-org/ovn.git
              cd ovn
              ./boot.sh && ./configure --with-ovs-source=${PWD}/../ovs
              make
              utilities/ovn-sim

           See documentation on ovs-sim for info on simulator, including the
           parameters you can use.

       OVN Commands
           These commands interact with OVN, the Open Virtual Network.

           ovn_start [options]
                  Creates and initializes the central OVN databases (both
                  ovn-sb(5) and ovn-nb(5)) and starts an instance of
                  ovsdb-server for each one.  Also starts an instance of
                  ovn-northd.

                  The following options are available:

                     --nbdb-model model
                            Uses the given database model for the northbound
                            database.  The model may be standalone (the
                            default), backup, or clustered.

                     --nbdb-servers n
                            For a clustered northbound database, the number
                            of servers in the cluster.  The default is 3.

                     --sbdb-model model
                            Uses the given database model for the southbound
                            database.  The model may be standalone (the
                            default), backup, or clustered.

                     --sbdb-servers n
                            For a clustered southbound database, the number
                            of servers in the cluster.  The default is 3.

           ovn_attach network bridge ip [masklen]
                  First, this command attaches bridge to interconnection
                  network network, just like net_attach network bridge.
                  Second, it configures (simulated) IP address ip (with
                  network mask length masklen, which defaults to 24) on
                  bridge. Finally, it configures the Open vSwitch database to
                  work with OVN and starts ovn-controller.

## [](#EXAMPLES)EXAMPLES

           Simulating hypervisors, starting ovn controller (via ovn_attach)
           and adding a logical port on each one of them:

              ovn_start
              ovn-nbctl ls-add lsw0
              net_add n1
              for i in 0 1; do
                  sim_add hv$i
                  as hv$i
                  ovs-vsctl add-br br-phys
                  ovn_attach n1 br-phys 192.168.0.`expr $i + 1`
                  ovs-vsctl add-port br-int vif$i -- \
                      set Interface vif$i external-ids:iface-id=lp$i
                  ovn-nbctl lsp-add lsw0 lp$i
                  ovn-nbctl lsp-set-addresses lp$i f0:00:00:00:00:0$i
              done

           Here’s a primitive OVN “scale test” (adjust the scale by changing
           n in the first line):

              n=200; export n
              ovn_start --sbdb-model=clustered
              net_add n1
              ovn-nbctl ls-add br0
              for i in `seq $n`; do
                  (sim_add hv$i
                  as hv$i
                  ovs-vsctl add-br br-phys
                  y=$(expr $i / 256)
                  x=$(expr $i % 256)
                  ovn_attach n1 br-phys 192.168.$y.$x
                  ovs-vsctl add-port br-int vif$i -- \
                      set Interface vif$i external-ids:iface-id=lp$i) &
                  case $i in
                      *50|*00) echo $i; wait ;;
                  esac
              done
              wait
              for i in `seq $n`; do
                  yy=$(printf %02x $(expr $i / 256))
                  xx=$(printf %02x $(expr $i % 256))
                  ovn-nbctl lsp-add br0 lp$i
                  ovn-nbctl lsp-set-addresses lp$i f0:00:00:00:$yy:$xx
              done

           When the scale test has finished initializing, you can watch the
           logical ports come up with a command like this:

              watch 'for i in `seq $n`; do \
              if test `ovn-nbctl lsp-get-up lp$i` != up; then echo $i; fi; done'

## [](#AUTHOR)AUTHOR

           The Open Virtual Network (OVN) Development Community

## [](#COPYRIGHT)COPYRIGHT

           2020-2024, The Open Virtual Network (OVN) Development Community

## [](#COLOPHON)COLOPHON

           This page is part of the Open Virtual Network (Daemons for Open
           vSwitch that translate virtual network configurations into
           OpenFlow) project.  Information about the project can be found at
           ⟨https://www.ovn.org/⟩.  If you have a bug report for this manual
           page, send it to bugs@openvswitch.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/ovn-org/ovn⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-31.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    25.03.90                       Aug 10, 2025                    OVN-SIM(1)

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
