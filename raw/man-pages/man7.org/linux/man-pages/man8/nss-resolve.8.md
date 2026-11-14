---
{"title": "nss-resolve(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/nss-resolve.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nss-resolve(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NSS-RESOLVE(8)                 nss-resolve                 NSS-RESOLVE(8)

## [](#NAME)NAME

           nss-resolve, libnss_resolve.so.2 - Hostname resolution via
           systemd-resolved.service

## [](#SYNOPSIS)SYNOPSIS

           libnss_resolve.so.2

## [](#DESCRIPTION)DESCRIPTION

           nss-resolve is a plug-in module for the GNU Name Service Switch
           (NSS) functionality of the GNU C Library (glibc) enabling it to
           resolve hostnames via the systemd-resolved(8) local network name
           resolution service. It replaces the nss-dns plug-in module that
           traditionally resolves hostnames via DNS.

           To activate the NSS module, add "resolve [!UNAVAIL=return]" to the
           line starting with "hosts:" in /etc/nsswitch.conf. Specifically,
           it is recommended to place "resolve" early in /etc/nsswitch.conf's
           "hosts:" line. It should be before the "files" entry, since
           systemd-resolved supports /etc/hosts internally, but with caching.
           To the contrary, it should be after "mymachines", to give
           hostnames given to local VMs and containers precedence over names
           received over DNS. Finally, we recommend placing "dns" somewhere
           after "resolve", to fall back to nss-dns if
           systemd-resolved.service is not available.

           Note that systemd-resolved will synthesize DNS resource records in
           a few cases, for example for "localhost" and the current local
           hostname, see systemd-resolved(8) for the full list. This
           duplicates the functionality of nss-myhostname(8), but it is still
           recommended (see examples below) to keep nss-myhostname configured
           in /etc/nsswitch.conf, to keep those names resolvable if
           systemd-resolved is not running.

           Please keep in mind that nss-myhostname (and nss-resolve) also
           resolve in the other direction — from locally attached IP
           addresses to hostnames. If you rely on that lookup being provided
           by DNS, you might want to order things differently.

           Communication between nss-resolve and systemd-resolved.service
           takes place via the /run/systemd/resolve/io.systemd.Resolve
           AF_UNIX socket.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           $SYSTEMD_NSS_RESOLVE_VALIDATE
               Takes a boolean argument. When false, cryptographic validation
               of resource records via DNSSEC will be disabled. This may be
               useful for testing, or when system time is known to be
               unreliable.

               Added in version 250.

           $SYSTEMD_NSS_RESOLVE_SYNTHESIZE
               Takes a boolean argument. When false, synthetic records, e.g.
               for the local host name, will not be returned. See section
               SYNTHETIC RECORDS in systemd-resolved.service(8) for more
               information. This may be useful to query the "public" resource
               records, independent of the configuration of the local
               machine.

               Added in version 250.

           $SYSTEMD_NSS_RESOLVE_CACHE
               Takes a boolean argument. When false, the cache of previously
               queried records will not be used by systemd-resolved(8).

               Added in version 250.

           $SYSTEMD_NSS_RESOLVE_ZONE
               Takes a boolean argument. When false, answers using locally
               registered public LLMNR/mDNS resource records will not be
               returned.

               Added in version 250.

           $SYSTEMD_NSS_RESOLVE_TRUST_ANCHOR
               Takes a boolean argument. When false, answers using locally
               configured trust anchors will not be used.

               Added in version 250.

           $SYSTEMD_NSS_RESOLVE_NETWORK
               Takes a boolean argument. When false, answers will be returned
               without using the network, i.e. either from local sources or
               the cache in systemd-resolved(8).

               Added in version 250.

           $SYSTEMD_NSS_RESOLVE_INTERFACE
               Takes an interface name or index as an argument. When
               specified, answers will only be obtained from name servers
               belonging to the specified interface.

               Added in version 260.

## [](#EXAMPLE)EXAMPLE

           Here is an example /etc/nsswitch.conf file that enables
           nss-resolve correctly:

               passwd:         files systemd
               group:          files [SUCCESS=merge] systemd
               shadow:         files systemd
               gshadow:        files systemd

               hosts:          mymachines resolve [!UNAVAIL=return] files myhostname dns
               networks:       files

               protocols:      db files
               services:       db files
               ethers:         db files
               rpc:            db files

               netgroup:       nis

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-resolved(8), nss-systemd(8),
           nss-myhostname(8), nss-mymachines(8), nsswitch.conf(5),
           systemd.syntax(7)

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

    systemd 262~devel                                          NSS-RESOLVE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [nss-myhostname(8)](../man8/nss-myhostname.8.html),  [nss-mymachines(8)](../man8/nss-mymachines.8.html),  [nss-systemd(8)](../man8/nss-systemd.8.html),  [systemd-resolved.service(8)](../man8/systemd-resolved.service.8.html)

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
