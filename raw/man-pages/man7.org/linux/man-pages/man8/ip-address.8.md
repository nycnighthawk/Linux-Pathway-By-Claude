---
{"title": "ip-address(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-address.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-address(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-ADDRESS(8)                     Linux                     IP-ADDRESS(8)

## [](#NAME)NAME

           ip-address - protocol address management

## [](#SYNOPSIS)SYNOPSIS

           ip [ OPTIONS ] address  { COMMAND | help }

           ip address { add | change | replace } IFADDR dev IFNAME [ LIFETIME
                   ] [ CONFFLAG-LIST ]

           ip address del IFADDR dev IFNAME [ mngtmpaddr ]

           ip address { save | flush } [ dev IFNAME ] [ scope SCOPE-ID ] [
                   metric METRIC ] [ to PREFIX ] [ FLAG-LIST ] [ label
                   PATTERN ] [ up ]

           ip address [ show [ dev IFNAME ] [ scope SCOPE-ID ] [ to PREFIX ]
                   [ FLAG-LIST ] [ label PATTERN ] [ master DEVICE ] [ type
                   TYPE ] [ vrf NAME ] [ up ] [ nomaster ] proto ADDRPROTO ]
                   ]

           ip address { showdump | restore }

           IFADDR := PREFIX | ADDR peer PREFIX [ broadcast ADDR ] [ anycast
                   ADDR ] [ label LABEL ] [ scope SCOPE-ID ] [ proto
                   ADDRPROTO ]

           SCOPE-ID := [ host | link | global | NUMBER ]

           ADDRPROTO := [ NAME | NUMBER ]

           FLAG-LIST := [ FLAG-LIST ] FLAG

           FLAG := [ [-]permanent | [-]dynamic | [-]secondary | [-]primary |
                   [-]tentative | [-]deprecated | [-]dadfailed | [-]temporary
                   | CONFFLAG-LIST ]

           CONFFLAG-LIST := [ CONFFLAG-LIST ] CONFFLAG

           CONFFLAG := [ home | mngtmpaddr | nodad | optimistic |
                   noprefixroute | autojoin ]

           LIFETIME := [ valid_lft LFT ] [ preferred_lft LFT ]

           LFT := [ forever | SECONDS ]

           TYPE := [ bridge | bridge_slave | bond | bond_slave | can | dummy
                   | hsr | ifb | ipoib | macvlan | macvtap | vcan | veth |
                   vlan | vxlan | ip6tnl | ipip | sit | gre | gretap | erspan
                   | ip6gre | ip6gretap | ip6erspan | vti | vrf | nlmon |
                   ipvlan | lowpan | geneve | macsec ]

## [](#DESCRIPTION)DESCRIPTION

           The address is a protocol (IPv4 or IPv6) address attached to a
           network device. Each device must have at least one address to use
           the corresponding protocol. It is possible to have several
           different addresses attached to one device. These addresses are
           not discriminated, so that the term alias is not quite appropriate
           for them and we do not use it in this document.

           The ip address command displays addresses and their properties,
           adds new addresses and deletes old ones.

       ip address add - add new protocol address.
           dev IFNAME
                  the name of the device to add the address to.

           local ADDRESS (default)
                  the address of the interface. The format of the address
                  depends on the protocol. It is a dotted quad for IP and a
                  sequence of hexadecimal halfwords separated by colons for
                  IPv6. The ADDRESS may be followed by a slash and a decimal
                  number which encodes the network prefix length.

           peer ADDRESS
                  the address of the remote endpoint for pointopoint
                  interfaces.  Again, the ADDRESS may be followed by a slash
                  and a decimal number, encoding the network prefix length.
                  If a peer address is specified, the local address cannot
                  have a prefix length. The network prefix is associated with
                  the peer rather than with the local address.

           broadcast ADDRESS
                  the broadcast address on the interface.

                  It is possible to use the special symbols '+' and '-'
                  instead of the broadcast address. In this case, the
                  broadcast address is derived by setting/resetting the host
                  bits of the interface prefix.

           label LABEL
                  Each address may be tagged with a label string.  The
                  maximum allowed total length of label is 15 characters.

           scope SCOPE_VALUE
                  the scope of the area where this address is valid.  The
                  available scopes are listed in
                  /usr/lib/iproute2/rt_scopesor
                  /etc/iproute2/rt_scopes(hasprecedenceifexists).  Predefined
                  scope values are:

                          global - the address is globally valid.

                          site - (IPv6 only, deprecated) the address is site
                          local, i.e. it is valid inside this site.

                          link - the address is link local, i.e. it is valid
                          only on this device.

                          host - the address is valid only inside this host.

           metric NUMBER
                  priority of prefix route associated with address.

           valid_lft LFT
                  the valid lifetime of this address; see section 5.5.4 of
                  RFC 4862. When it expires, the address is removed by the
                  kernel.  Defaults to forever.

           preferred_lft LFT
                  the preferred lifetime of this address; see section 5.5.4
                  of RFC 4862. When it expires, the address is no longer used
                  for new outgoing connections. Defaults to forever.

           home   (IPv6 only) designates this address the "home address" as
                  defined in RFC 6275.

           mngtmpaddr
                  (IPv6 only) make the kernel manage temporary addresses
                  created from this one as template on behalf of Privacy
                  Extensions (RFC3041). For this to become active, the
                  use_tempaddr sysctl setting has to be set to a value
                  greater than zero.  The given address needs to have a
                  prefix length of 64. This flag allows to use privacy
                  extensions in a manually configured network, just like if
                  stateless auto-configuration was active.

           nodad  (IPv6 only) do not perform Duplicate Address Detection (RFC
                  4862) when adding this address.

           optimistic
                  (IPv6 only) When performing Duplicate Address Detection,
                  use the RFC 4429 optimistic variant.

           noprefixroute
                  Do not automatically create a route for the network prefix
                  of the added address, and don't search for one to delete
                  when removing the address. Changing an address to add this
                  flag will remove the automatically added prefix route,
                  changing it to remove this flag will create the prefix
                  route automatically.

           autojoin
                  Joining multicast groups on Ethernet level via ip maddr
                  command does not work if connected to an Ethernet switch
                  that does IGMP snooping since the switch would not
                  replicate multicast packets on ports that did not have IGMP
                  reports for the multicast addresses.

                  Linux VXLAN interfaces created via ip link add vxlan have
                  the group option that enables them to do the required join.

                  Using the autojoin flag when adding a multicast address
                  enables similar functionality for Openvswitch VXLAN
                  interfaces as well as other tunneling mechanisms that need
                  to receive multicast traffic.

           proto ADDRPROTO
                  the protocol identifier of this route.  ADDRPROTO may be a
                  number or a string from the file
                  /etc/iproute2/rt_addrprotos.  If the protocol ID is not
                  given,

                  ip assumes protocol 0. Several protocol values have a fixed
                  interpretation. Namely:

                          kernel_lo - The ::1 address that kernel installs on
                          a loopback netdevice has this
                            protocol value

                          kernel_ra - IPv6 addresses installed in response to
                          router advertisement messages

                          kernel_ll - Link-local addresses have this protocol
                          value

                  The rest of the values are not reserved and the
                  administrator is free to assign (or not to assign) protocol
                  tags.

       ip address delete - delete protocol address
           Arguments: coincide with the arguments of ip addr add.  The device
           name is a required argument. The rest are optional.  If no
           arguments are given, the first address is deleted.

       ip address show - look at protocol addresses
           dev IFNAME (default)
                  name of device.

           scope SCOPE_VAL
                  only list addresses with this scope.

           to PREFIX
                  only list addresses matching this prefix.

           label PATTERN
                  only list addresses with labels matching the PATTERN.
                  PATTERN is a usual shell style pattern.

           master DEVICE
                  only list interfaces enslaved to this master device.

           vrf NAME
                  only list interfaces enslaved to this vrf.

           type TYPE
                  only list interfaces of the given type.

                  Note that the type name is not checked against the list of
                  supported types - instead it is sent as-is to the kernel.
                  Later it is used to filter the returned interface list by
                  comparing it with the relevant attribute in case the kernel
                  didn't filter already. Therefore any string is accepted,
                  but may lead to empty output.

           up     only list running interfaces.

           nomaster
                  only list interfaces with no master.

           dynamic and permanent
                  (IPv6 only) only list addresses installed due to stateless
                  address configuration or only list permanent (not dynamic)
                  addresses. These two flags are inverses of each other, so
                  -dynamic is equal to permanent and -permanent is equal to
                  dynamic.

           tentative
                  (IPv6 only) only list addresses which have not yet passed
                  duplicate address detection.

           -tentative
                  (IPv6 only) only list addresses which are not in the
                  process of duplicate address detection currently.

           deprecated
                  (IPv6 only) only list deprecated addresses.

           -deprecated
                  (IPv6 only) only list addresses not being deprecated.

           dadfailed
                  (IPv6 only) only list addresses which have failed duplicate
                  address detection.

           -dadfailed
                  (IPv6 only) only list addresses which have not failed
                  duplicate address detection.

           temporary or secondary
                  List temporary IPv6 or secondary IPv4 addresses only. The
                  Linux kernel shares a single bit for those, so they are
                  actually aliases for each other although the meaning
                  differs depending on address family.

           -temporary or -secondary
                  These flags are aliases for primary.

           primary
                  List only primary addresses, in IPv6 exclude temporary
                  ones. This flag is the inverse of temporary and secondary.

           -primary
                  This is an alias for temporary or secondary.

           proto ADDRPROTO
                  Only show addresses with a given protocol, or those for
                  which the kernel response did not include protocol. See the
                  corresponding argument to ip addr add for details about
                  address protocols.

       ip address flush - flush protocol addresses
           This command flushes the protocol addresses selected by some
           criteria.

           This command has the same arguments as show except that type and
           master selectors are not supported.  Another difference is that it
           does not run when no arguments are given.

           Warning: This command and other flush commands are unforgiving.
           They will cruelly purge all the addresses.

           With the -statistics option, the command becomes verbose. It
           prints out the number of deleted addresses and the number of
           rounds made to flush the address list.  If this option is given
           twice, ip address flush also dumps all the deleted addresses in
           the format described in the previous subsection.

## [](#EXAMPLES)EXAMPLES

           ip address show
               Shows IPv4 and IPv6 addresses assigned to all network
               interfaces. The 'show' subcommand can be omitted.

           ip address show up
               Same as above except that only addresses assigned to active
               network interfaces are shown.

           ip address show dev eth0
               Shows IPv4 and IPv6 addresses assigned to network interface
               eth0.

           ip address add 2001:0db8:85a3::0370:7334/64 dev eth1
               Adds an IPv6 address to network interface eth1.

           ip address delete 2001:0db8:85a3::0370:7334/64 dev eth1
               Delete the IPv6 address added above.

           ip address flush dev eth4 scope global
               Removes all global IPv4 and IPv6 addresses from device eth4.
               Without 'scope global' it would remove all addresses including
               IPv6 link-local ones.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           Original Manpage by Michail Litvak <mci@owl.openwall.com>

## [](#COLOPHON)COLOPHON

           This page is part of the iproute2 (utilities for controlling
           TCP/IP networking and traffic) project.  Information about the
           project can be found at 
           ⟨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2⟩.
           If you have a bug report for this manual page, send it to
           netdev@vger.kernel.org, shemminger@osdl.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/network/iproute2/iproute2.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iproute2                       20 Dec 2011                  IP-ADDRESS(8)

------------------------------------------------------------------------

Pages that refer to this page: [network_namespaces(7)](../man7/network_namespaces.7.html),  [ip(8)](../man8/ip.8.html),  [ip-vrf(8)](../man8/ip-vrf.8.html),  [wg(8)](../man8/wg.8.html),  [wg-quick(8)](../man8/wg-quick.8.html)

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
