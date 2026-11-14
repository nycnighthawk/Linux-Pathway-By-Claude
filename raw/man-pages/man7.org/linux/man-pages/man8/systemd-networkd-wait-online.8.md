---
{"title": "systemd-networkd-wait-online.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-networkd-wait-online.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-networkd-wait-online.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTE...ERVICE(8)  systemd-networkd-wait-online.service SYSTE...ERVICE(8)

## [](#NAME)NAME

           systemd-networkd-wait-online.service, systemd-networkd-wait-
           online@.service, systemd-networkd-wait-online - Wait for network
           to come online

## [](#SYNOPSIS)SYNOPSIS

           systemd-networkd-wait-online.service

           systemd-networkd-wait-online@.service

           /usr/lib/systemd/systemd-networkd-wait-online

## [](#DESCRIPTION)DESCRIPTION

           systemd-networkd-wait-online is a oneshot system service (see
           systemd.service(5)), that waits for the network to be configured.
           By default, it will wait for all links it is aware of and which
           are managed by systemd-networkd.service(8) to be fully configured
           or failed, and for at least one link to be online. Here, online
           means that the link's operational state is equal or higher than
           "degraded". The threshold can be configured by
           --operational-state= option.

           The service systemd-networkd-wait-online.service invokes
           systemd-networkd-wait-online without any options. Thus, it waits
           for all managed interfaces to be configured or failed, and for at
           least one to be online.

           The service systemd-networkd-wait-online@.service takes an
           interface name, and invokes systemd-networkd-wait-online with -i
           and the specified interface name. Thus, wait for the specified
           interface to be configured and online. For example,
           systemd-networkd-wait-online@eth0.service waits for eth0 to be
           configured by systemd-networkd and online.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -i INTERFACE[:MIN_OPERSTATE[:MAX_OPERSTATE]],
           --interface=INTERFACE[:MIN_OPERSTATE[:MAX_OPERSTATE]]
               Network interface to wait for before deciding if the system is
               online. This is useful when a system has several interfaces
               which will be configured, but a particular one is necessary to
               access some network resources. When used, all other interfaces
               are ignored. This option may be used more than once to wait
               for multiple network interfaces. When this option is specified
               multiple times, then systemd-networkd-wait-online waits for
               all specified interfaces to be online. Optionally, required
               minimum and maximum operational states can be specified after
               a colon ":". Please see networkctl(1) for possible operational
               states. If the operational state is not specified here, then
               the value from RequiredForOnline= in the corresponding
               .network file is used if present, and "degraded" otherwise.

               Added in version 213.

           --ignore=INTERFACE
               Network interfaces to be ignored when deciding if the system
               is online. By default, only the loopback interface is ignored.
               This option may be used more than once to ignore multiple
               network interfaces.

               Added in version 219.

           -o MIN_OPERSTATE[:MAX_OPERSTATE],
           --operational-state=MIN_OPERSTATE[:MAX_OPERSTATE]
               Takes a minimum operational state and an optional maximum
               operational state. Please see networkctl(1) for possible
               operational states. If set, the specified value overrides
               RequiredForOnline= settings in .network files. But this does
               not override operational states specified in --interface=
               option.

               Added in version 242.

           -4, --ipv4
               Waiting for an IPv4 address of each network interface to be
               configured. If this option is specified with --any, then
               systemd-networkd-wait-online exits with success when at least
               one interface becomes online and has an IPv4 address. If the
               required minimum operational state is below "routable", then
               each link (or at least one link with --any) must have an IPv4
               link-local or routable address. If the required minimum
               operational state is "routable", then each link must have an
               IPv4 routable address.

               If neither --ipv4 nor --ipv6 is specified, then the value from
               RequiredFamilyForOnline= in the corresponding .network file is
               used if present.

               Added in version 249.

           -6, --ipv6
               Waiting for an IPv6 address of each network interface to be
               configured. If this option is specified with --any, then
               systemd-networkd-wait-online exits with success when at least
               one interface becomes online and has an IPv6 address. If the
               required minimum operational state is below "routable", then
               each link (or at least one link with --any) must have an IPv6
               link-local or routable address. If the required minimum
               operational state is "routable", then each link must have an
               IPv6 routable address.

               If neither --ipv4 nor --ipv6 is specified, then the value from
               RequiredFamilyForOnline= in the corresponding .network file is
               used if present.

               Added in version 249.

           --dns
               Waiting for DNS servers to be accessible on each interface. If
               this option is specified with --any, then
               systemd-networkd-wait-online exits with success when at least
               one interface becomes online and has an accessible DNS server.

               If a link has the property DefaultRoute=yes (either because
               the DNSDefaultRoute= network property is explicitly
               configured, or because the link does not have any
               "routing-only" domains), or if the search domain "." is
               configured, then wait for link-specific DNS servers to be
               accessible. Otherwise, allow global DNS servers to satisfy the
               condition.

               Added in version 258.

           --any
               Even if several interfaces are in configuring state,
               systemd-networkd-wait-online exits with success when at least
               one interface becomes online. When this option is specified
               with --interface=, then systemd-networkd-wait-online waits for
               one of the specified interfaces to be online. This option is
               useful when some interfaces may not have carrier on boot.

               Added in version 242.

           --timeout=SECS
               Fail the service if the network is not online by the time the
               timeout elapses. A timeout of 0 disables the timeout. Defaults
               to 120 seconds.

               Added in version 219.

           -q, --quiet
               Suppress log messages.

               Added in version 242.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.service(5), systemd-networkd.service(8),
           networkctl(1)

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

    systemd 262~devel                                       SYSTE...ERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.network(5)](../man5/systemd.network.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-networkd.service(8)](../man8/systemd-networkd.service.8.html)

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
