---
{"title": "ovn-br-controller(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ovn-br-controller.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ovn-br-controller(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ovn-br-controller(8)            OVN Manual           ovn-br-controller(8)

## [](#NAME)NAME

           ovn-br-controller - Open Virtual Network local OVS bridge
           controller

## [](#SYNOPSIS)SYNOPSIS

           ovn-br-controller [options] [ovs-database]

## [](#DESCRIPTION)DESCRIPTION

           ovn-br-controller is OVN logical flow based local controller
           daemon to control and program the Open vSwitch bridges. It
           connects up to the OVN bridge database (see ovn-br(5)) over the
           OVSDB protocol, and down to the Open vSwitch database (see
           ovs-vswitchd.conf.db(5)) over the OVSDB protocol and to
           ovs-vswitchd(8) via OpenFlow. ovn-br-controller processes and
           converts the OVN Logical flows configured in the OVN bridge
           database for the Open vSwitch bridges to OpenFlow rules and
           programs these flow rules to the Open vSwitch bridges.

## [](#CONFIGURATION)CONFIGURATION

           ovn-br-controller retrieves most of its configuration information
           from the local Open vSwitch’s ovsdb-server instance. The default
           location is db.sock in the local Open vSwitch’s "run" directory.
           It may be overridden by specifying the ovs-database argument as an
           OVSDB active or passive connection method, as described in
           ovsdb(7).

           ovn-br-controller assumes it gets configuration information from
           the following keys in the Open_vSwitch table of the local OVS
           instance:

                  external_ids:ovn-br-remote
                         The OVN bridge database that this system should
                         connect to for its configuration, in one of the same
                         forms documented above for the ovs-database.

           ovn-br-controller reads the following values from the Open_vSwitch
           database of the local OVS instance:

                  external_ids:ovnbr-managed from Interface table
                         If the value is true, then this interface is managed
                         by ovn-br-controller if this interface is connected
                         to the OVS bridge managed by ovn-br-controller.

                         Default value is true if this option is not defined.

                         CMS should set the value of this option to false if
                         it doesn’t want ovn-br-controller to manage it.

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

    OVN 25.09.90                ovn-br-controller        ovn-br-controller(8)

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
