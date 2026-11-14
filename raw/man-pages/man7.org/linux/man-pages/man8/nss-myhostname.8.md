---
{"title": "nss-myhostname(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/nss-myhostname.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nss-myhostname(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NSS-MYHOSTNAME(8)             nss-myhostname            NSS-MYHOSTNAME(8)

## [](#NAME)NAME

           nss-myhostname, libnss_myhostname.so.2 - Hostname resolution for
           the locally configured system hostname

## [](#SYNOPSIS)SYNOPSIS

           libnss_myhostname.so.2

## [](#DESCRIPTION)DESCRIPTION

           nss-myhostname is a plug-in module for the GNU Name Service Switch
           (NSS) functionality of the GNU C Library (glibc), primarily
           providing hostname resolution for the locally configured system
           hostname as returned by gethostname(2). The precise hostnames
           resolved by this module are:

           •   The local, configured hostname is resolved to all locally
               configured IP addresses ordered by their scope, or — if none
               are configured — the IPv4 address 127.0.0.2 (which is on the
               local loopback) and the IPv6 address ::1 (which is the local
               host).

           •   The hostnames "localhost" and "localhost.localdomain" (as well
               as any hostname ending in ".localhost" or
               ".localhost.localdomain") are resolved to the IP addresses
               127.0.0.1 and ::1.

           •   The hostname "_gateway" is resolved to all current default
               routing gateway addresses, ordered by their metric. This
               assigns a stable hostname to the current gateway, useful for
               referencing it independently of the current network
               configuration state.

           •   The hostname "_outbound" is resolved to the local IPv4 and
               IPv6 addresses that are most likely used for communication
               with other hosts. This is the preferred source addresses of
               default gateways if specified, or determined by requesting a
               routing decision to the configured default gateways from the
               kernel and then using the local IP addresses selected by this
               decision. This hostname is only available if there is at least
               one local default gateway configured. This assigns a stable
               hostname to the local outbound IP addresses, useful for
               referencing them independently of the current network
               configuration state.

           Various software relies on an always-resolvable local hostname.
           When using dynamic hostnames, this is traditionally achieved by
           patching /etc/hosts at the same time as changing the hostname.
           This is problematic since it requires a writable /etc/ file system
           and is fragile because the file might be edited by the
           administrator at the same time. With nss-myhostname enabled,
           changing /etc/hosts is unnecessary, and on many systems, the file
           becomes entirely optional.

           To activate the NSS modules, add "myhostname" to the line starting
           with "hosts:" in /etc/nsswitch.conf.

           It is recommended to place "myhostname" after "files" and before
           "dns". This resolves well-known hostnames like "localhost" and the
           machine hostnames locally. It is consistent with the behaviour of
           nss-resolve, and still allows overriding via /etc/hosts.

           Please keep in mind that nss-myhostname (and nss-resolve) also
           resolve in the other direction — from locally attached IP
           addresses to hostnames. If you rely on that lookup being provided
           by DNS, you might want to order things differently.

## [](#EXAMPLE)EXAMPLE

           Here is an example /etc/nsswitch.conf file that enables
           nss-myhostname correctly:

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

           To test, use glibc's getent(1) tool:

               $ getent ahosts `hostname`
               ::1       STREAM omega
               ::1       DGRAM
               ::1       RAW
               127.0.0.2       STREAM
               127.0.0.2       DGRAM
               127.0.0.2       RAW

           In this case, the local hostname is omega.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), nss-systemd(8), nss-resolve(8), nss-mymachines(8),
           nsswitch.conf(5), getent(1)

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

    systemd 262~devel                                       NSS-MYHOSTNAME(8)

------------------------------------------------------------------------

Pages that refer to this page: [org.freedesktop.hostname1(5)](../man5/org.freedesktop.hostname1.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [nss-mymachines(8)](../man8/nss-mymachines.8.html),  [nss-resolve(8)](../man8/nss-resolve.8.html),  [nss-systemd(8)](../man8/nss-systemd.8.html)

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
