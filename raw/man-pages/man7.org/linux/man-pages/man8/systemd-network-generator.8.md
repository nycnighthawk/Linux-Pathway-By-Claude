---
{"title": "systemd-network-generator.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-network-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-network-generator.service(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE OPTIONS](#KERNEL_COMMAND_LINE_OPTIONS) \| [CREDENTIALS](#CREDENTIALS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEM...ERVICE(8)  systemd-network-generator.service  SYSTEM...ERVICE(8)

## [](#NAME)NAME

           systemd-network-generator.service, systemd-network-generator -
           Generate network configuration from the kernel command line

## [](#SYNOPSIS)SYNOPSIS

           systemd-network-generator.service

           /usr/lib/systemd/systemd-network-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-network-generator.service is a system service that
           translates ip= and related settings on the kernel command line
           (see below) into systemd.network(5), systemd.netdev(5), and
           systemd.link(5) configuration files understood by
           systemd-networkd.service(8) and systemd-udevd.service(8).

           Files are generated in /run/systemd/network/.

           Note: despite the name, this generator executes as a normal
           systemd service and is not an implementation of the
           systemd.generator(7) concept.

## [](#KERNEL_COMMAND_LINE_OPTIONS)KERNEL COMMAND LINE OPTIONS

           This tool understands the following options:

           ip=, nameserver=, rd.route=, rd.peerdns=
               Translated into systemd.network(5) files.

               In addition to the parameters dracut.cmdline(7) defines the
               ip= option accepts the special value "link-local". If
               selected, the network interfaces will be configured for
               link-local addressing (IPv4LL, IPv6LL) only, DHCP or IPv6RA
               will not be enabled.

               Added in version 245.

           ifname=, net.ifname_policy=
               Translated into systemd.link(5) files.

               Added in version 245.

           vlan=, bond=, bridge=, bootdev=
               Translated into systemd.netdev(5) files.

               Added in version 245.

           BOOTIF=, rd.bootif=
               When BOOTIF is specified in the interface field of ip=, it is
               treated as a special placeholder rather than a real interface
               name. Then, in combination with the MAC address provided by
               BOOTIF=, this is translated into a systemd.network(5) file
               which matches on the provided MAC address. When rd.bootif=0 is
               passed, this functionality is disabled, and the BOOTIF= option
               is ignored.

               See dracut.cmdline(7) for details on the usage of these
               options.

               Added in version 261.

           See dracut.cmdline(7) and systemd-udevd.service(8) for option
           syntax and details.

## [](#CREDENTIALS)CREDENTIALS

           systemd-network-generator supports the service credentials logic
           as implemented by ImportCredential=/LoadCredential=/SetCredential=
           (see systemd.exec(5) for details). The following credentials are
           used when passed in:

           network.conf.*, network.link.*, network.netdev.*,
           network.network.*
               These credentials should contain valid networkd.conf(5),
               systemd.link(5), systemd.netdev(5), systemd.network(5)
               configuration data. From each matching credential a separate
               file is created. Example: a passed credential
               network.link.50-foobar will be copied into a configuration
               file 50-foobar.link.

               Note that the resulting files are created world-readable, it
               is hence recommended to not include secrets in these
               credentials, but to supply them via separate credentials
               directly to systemd-networkd.service(8).

               Added in version 256.

           Note that by default the systemd-networkd.service(8) service is
           set up to inherit the these credentials from the service manager.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-networkd.service(8), dracut(8)

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

    systemd 262~devel                                      SYSTEM...ERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.link(5)](../man5/systemd.link.5.html),  [systemd.netdev(5)](../man5/systemd.netdev.5.html),  [systemd.network(5)](../man5/systemd.network.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-networkd.service(8)](../man8/systemd-networkd.service.8.html),  [systemd-storagetm.service(8)](../man8/systemd-storagetm.service.8.html),  [systemd-udevd.service(8)](../man8/systemd-udevd.service.8.html)

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
