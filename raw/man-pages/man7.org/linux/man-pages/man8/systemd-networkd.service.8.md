---
{"title": "systemd-networkd.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-networkd.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-networkd.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION FILES](#CONFIGURATION_FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-N...D.SERVICE(8) systemd-networkd.serviceSYSTEMD-N...D.SERVICE(8)

## [](#NAME)NAME

           systemd-networkd.service, systemd-networkd - Network manager

## [](#SYNOPSIS)SYNOPSIS

           systemd-networkd.service

           /usr/lib/systemd/systemd-networkd

## [](#DESCRIPTION)DESCRIPTION

           systemd-networkd is a system service that manages networks. It
           detects and configures network devices as they appear, as well as
           creating virtual network devices.

           Certain low-level settings of physical network devices (e.g.
           device names and altnames) as well as the creation of SR-IOV
           virtual functions on physical network interfaces may be managed by
           systemd-udevd(8) according to the contents of systemd.link(5)
           files.

           systemd-networkd will create "virtual" network devices (e.g.
           bridges and tunnels) based on the configuration in
           systemd.netdev(5) files, respecting the [Match] sections in those
           files.

           systemd-networkd will manage network addresses and routes for any
           link for which it finds a .network file with an appropriate
           [Match] section, see systemd.network(5). For those links, it will
           flush existing network addresses and routes when bringing up the
           device (except when directed not to). Any links not matched by one
           of the .network files will be ignored. It is also possible to
           explicitly tell systemd-networkd to ignore a link by using the
           Unmanaged=yes option, see systemd.network(5).

           When systemd-networkd exits, it generally leaves existing network
           devices and configuration intact. This makes it possible to
           transition from the initrd and to restart the service without
           breaking connectivity. This also means that when configuration is
           updated and systemd-networkd is restarted, netdev interfaces for
           which configuration was removed will not be dropped, and may need
           to be cleaned up manually.

           systemd-networkd may be introspected and controlled at runtime
           using networkctl(1).

           See org.freedesktop.network1(5) and org.freedesktop.LogControl1(5)
           for a description of the D-Bus API.

## [](#CONFIGURATION_FILES)CONFIGURATION FILES

           The configuration files are read from the files located in the
           system network directory /usr/lib/systemd/network, the volatile
           runtime network directory /run/systemd/network and the local
           administration network directory /etc/systemd/network.

           Networks are configured in .network files, see systemd.network(5),
           and virtual network devices are configured in .netdev files, see
           systemd.netdev(5).

## [](#SEE_ALSO)SEE ALSO

           networkctl(1), systemd(1), systemd.link(5), systemd.network(5),
           systemd.netdev(5), systemd-networkd-wait-online.service(8),
           systemd-network-generator.service(8), org.freedesktop.network1(5)

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

    systemd 262~devel                                SYSTEMD-N...D.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [networkctl(1)](../man1/networkctl.1.html),  [resolvectl(1)](../man1/resolvectl.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [systemd-vmspawn(1)](../man1/systemd-vmspawn.1.html),  [hostname(5)](../man5/hostname.5.html),  [networkd.conf(5)](../man5/networkd.conf.5.html),  [org.freedesktop.network1(5)](../man5/org.freedesktop.network1.5.html),  [org.freedesktop.resolve1(5)](../man5/org.freedesktop.resolve1.5.html),  [resolved.conf(5)](../man5/resolved.conf.5.html),  [systemd.link(5)](../man5/systemd.link.5.html),  [systemd.netdev(5)](../man5/systemd.netdev.5.html),  [systemd.network(5)](../man5/systemd.network.5.html),  [timesyncd.conf(5)](../man5/timesyncd.conf.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-imdsd@.service(8)](../man8/systemd-imdsd@.service.8.html),  [systemd-networkd-wait-online.service(8)](../man8/systemd-networkd-wait-online.service.8.html),  [systemd-network-generator.service(8)](../man8/systemd-network-generator.service.8.html),  [systemd-resolved.service(8)](../man8/systemd-resolved.service.8.html),  [systemd-timesyncd.service(8)](../man8/systemd-timesyncd.service.8.html)

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
