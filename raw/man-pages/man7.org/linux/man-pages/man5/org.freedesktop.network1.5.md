---
{"title": "org.freedesktop.network1(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/org.freedesktop.network1.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# org.freedesktop.network1(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [INTRODUCTION](#INTRODUCTION) \| [THE MANAGER OBJECT](#THE_MANAGER_OBJECT) \| [LINK OBJECT](#LINK_OBJECT) \| [NETWORK OBJECT](#NETWORK_OBJECT) \| [DHCP SERVER OBJECT](#DHCP_SERVER_OBJECT) \| [DHCPV4 CLIENT OBJECT](#DHCPV4_CLIENT_OBJECT) \| [DHCPV6 CLIENT OBJECT](#DHCPV6_CLIENT_OBJECT) \| [EXAMPLES](#EXAMPLES) \| [VERSIONING](#VERSIONING) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ORG.FREED....NETWORK1(5) org.freedesktop.network1ORG.FREED....NETWORK1(5)

## [](#NAME)NAME

           org.freedesktop.network1 - The D-Bus interface of systemd-networkd

## [](#INTRODUCTION)INTRODUCTION

           systemd-networkd.service(8) is a system service that manages and
           configures network interfaces. This page describes the D-Bus
           interface.

## [](#THE_MANAGER_OBJECT)THE MANAGER OBJECT

           The service exposes the following interfaces on the Manager object
           on the bus:

               node /org/freedesktop/network1 {
                 interface org.freedesktop.network1.Manager {
                   methods:
                     ListLinks(out a(iso) links);
                     GetLinkByName(in  s name,
                                   out i ifindex,
                                   out o path);
                     GetLinkByIndex(in  i ifindex,
                                    out s name,
                                    out o path);
                     SetLinkNTP(in  i ifindex,
                                in  as servers);
                     SetLinkDNS(in  i ifindex,
                                in  a(iay) addresses);
                     SetLinkDNSEx(in  i ifindex,
                                  in  a(iayqs) addresses);
                     SetLinkDomains(in  i ifindex,
                                    in  a(sb) domains);
                     SetLinkDefaultRoute(in  i ifindex,
                                         in  b enable);
                     SetLinkLLMNR(in  i ifindex,
                                  in  s mode);
                     SetLinkMulticastDNS(in  i ifindex,
                                         in  s mode);
                     SetLinkDNSOverTLS(in  i ifindex,
                                       in  s mode);
                     SetLinkDNSSEC(in  i ifindex,
                                   in  s mode);
                     SetLinkDNSSECNegativeTrustAnchors(in  i ifindex,
                                                       in  as names);
                     RevertLinkNTP(in  i ifindex);
                     RevertLinkDNS(in  i ifindex);
                     RenewLink(in  i ifindex);
                     ForceRenewLink(in  i ifindex);
                     ReconfigureLink(in  i ifindex);
                     Reload();
                     DescribeLink(in  i ifindex,
                                  out s json);
                     Describe(out s json);
                   properties:
                     readonly s OperationalState = '...';
                     readonly s CarrierState = '...';
                     readonly s AddressState = '...';
                     readonly s IPv4AddressState = '...';
                     readonly s IPv6AddressState = '...';
                     readonly s OnlineState = '...';
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly t NamespaceId = ...;
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
                     readonly u NamespaceNSID = ...;
                 };
                 interface org.freedesktop.DBus.Peer { ... };
                 interface org.freedesktop.DBus.Introspectable { ... };
                 interface org.freedesktop.DBus.Properties { ... };
               };

           Provides information about the manager.

       Properties
           NamespaceId contains the inode number of the network namespace
           that the network service runs in. A client may compare this with
           the inode number of its own network namespace to verify whether
           the service manages the same network namespace.

           NamespaceNSID contains the "nsid" identifier the kernel maintains
           for the network namespace, if there's one assigned.

## [](#LINK_OBJECT)LINK OBJECT

               node /org/freedesktop/network1/link/_1 {
                 interface org.freedesktop.network1.Link {
                   methods:
                     SetNTP(in  as servers);
                     SetDNS(in  a(iay) addresses);
                     SetDNSEx(in  a(iayqs) addresses);
                     SetDomains(in  a(sb) domains);
                     SetDefaultRoute(in  b enable);
                     SetLLMNR(in  s mode);
                     SetMulticastDNS(in  s mode);
                     SetDNSOverTLS(in  s mode);
                     SetDNSSEC(in  s mode);
                     SetDNSSECNegativeTrustAnchors(in  as names);
                     RevertNTP();
                     RevertDNS();
                     Renew();
                     ForceRenew();
                     Reconfigure();
                     Describe(out s json);
                   properties:
                     readonly s OperationalState = '...';
                     readonly s CarrierState = '...';
                     readonly s AddressState = '...';
                     readonly s IPv4AddressState = '...';
                     readonly s IPv6AddressState = '...';
                     readonly s OnlineState = '...';
                     readonly s AdministrativeState = '...';
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
                     readonly (tt) BitRates = ...;
                 };
                 interface org.freedesktop.DBus.Peer { ... };
                 interface org.freedesktop.DBus.Introspectable { ... };
                 interface org.freedesktop.DBus.Properties { ... };
               };

           Provides information about interfaces.

## [](#NETWORK_OBJECT)NETWORK OBJECT

               node /org/freedesktop/network1/network/_1 {
                 interface org.freedesktop.network1.Network {
                   properties:
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly s Description = '...';
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly s SourcePath = '...';
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly as MatchMAC = ['...', ...];
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly as MatchPath = ['...', ...];
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly as MatchDriver = ['...', ...];
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly as MatchType = ['...', ...];
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly as MatchName = ['...', ...];
                 };
                 interface org.freedesktop.DBus.Peer { ... };
                 interface org.freedesktop.DBus.Introspectable { ... };
                 interface org.freedesktop.DBus.Properties { ... };
               };

           Provides information about .network files.

## [](#DHCP_SERVER_OBJECT)DHCP SERVER OBJECT

               node /org/freedesktop/network1/link/_1 {
                 interface org.freedesktop.network1.DHCPServer {
                   properties:
                     readonly a(uayayayayt) Leases = [...];
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly u PoolSize = ...;
                     @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
                     readonly u PoolOffset = ...;
                 };
                 interface org.freedesktop.DBus.Peer { ... };
                 interface org.freedesktop.DBus.Introspectable { ... };
                 interface org.freedesktop.DBus.Properties { ... };
                 interface org.freedesktop.network1.Link { ... };
               };

           Provides information about the DHCP server. The Leases property
           contains the currently active leases. The PoolSize property
           contains the total number of addresses in the dynamic address
           pool. The PoolOffset property contains the offset from the subnet
           base address where the pool starts. These correspond to the
           PoolSize= and PoolOffset= settings in systemd.network(5).
           UINT32_MAX is used as a sentinel value for PoolSize and PoolOffset
           to indicate that the information is unavailable (i.e. no DHCP
           server is configured or the link is in relay mode), rather than a
           valid pool size or offset.

## [](#DHCPV4_CLIENT_OBJECT)DHCPV4 CLIENT OBJECT

               node /org/freedesktop/network1/link/_1 {
                 interface org.freedesktop.network1.DHCPv4Client {
                   properties:
                     readonly s State = '...';
                 };
                 interface org.freedesktop.DBus.Peer { ... };
                 interface org.freedesktop.DBus.Introspectable { ... };
                 interface org.freedesktop.DBus.Properties { ... };
                 interface org.freedesktop.network1.Link { ... };
               };

           Provides information about DHCPv4 client status.

## [](#DHCPV6_CLIENT_OBJECT)DHCPV6 CLIENT OBJECT

               node /org/freedesktop/network1/link/_1 {
                 interface org.freedesktop.network1.DHCPv6Client {
                   properties:
                     readonly s State = '...';
                 };
                 interface org.freedesktop.DBus.Peer { ... };
                 interface org.freedesktop.DBus.Introspectable { ... };
                 interface org.freedesktop.DBus.Properties { ... };
                 interface org.freedesktop.network1.Link { ... };
               };

           Provides information about DHCPv6 client status.

## [](#EXAMPLES)EXAMPLES

           Example 1. Introspect org.freedesktop.network1.Manager on the bus

               $ gdbus introspect --system \
                 --dest org.freedesktop.network1 \
                 --object-path /org/freedesktop/network1

           Example 2. Introspect org.freedesktop.network1.Link on the bus

               $ gdbus introspect --system \
                 --dest org.freedesktop.network1 \
                 --object-path /org/freedesktop/network1/link/_11

## [](#VERSIONING)VERSIONING

           These D-Bus interfaces follow the usual interface versioning
           guidelines[1].

## [](#HISTORY)HISTORY

       DHCP Server Object
           PoolSize and PoolOffset were added in version 261.

       DHCPv4 Client Object
           State was added in version 255.

       DHCPv6 Client Object
           State was added in version 255.

       Manager Object
           NamespaceNSID was added in version 256.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-networkd.service(8), networkctl(1)

## [](#NOTES)NOTES

            1. the usual interface versioning guidelines
               https://0pointer.de/blog/projects/versioning-dbus.html

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                ORG.FREED....NETWORK1(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-networkd.service(8)](../man8/systemd-networkd.service.8.html)

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
