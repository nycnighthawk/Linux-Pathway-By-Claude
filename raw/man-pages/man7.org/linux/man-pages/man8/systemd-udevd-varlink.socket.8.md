---
{"title": "systemd-udevd.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-udevd-varlink.socket.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-udevd.service(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-UDEVD.SERVICE(8)  systemd-udevd.service  SYSTEMD-UDEVD.SERVICE(8)

## [](#NAME)NAME

           systemd-udevd.service, systemd-udevd-kernel.socket, systemd-udevd-
           varlink.socket, systemd-udevd - Device event managing daemon

## [](#SYNOPSIS)SYNOPSIS

           systemd-udevd.service

           systemd-udevd-kernel.socket

           systemd-udevd-varlink.socket

           /usr/lib/systemd/systemd-udevd [--daemon] [--debug]
                                          [--children-max=] [--exec-delay=]
                                          [--event-timeout=]
                                          [--resolve-names=early|late|never]
                                          [--version] [--help]

## [](#DESCRIPTION)DESCRIPTION

           systemd-udevd listens to kernel uevents. For every event,
           systemd-udevd executes matching instructions specified in udev
           rules. See udev(7).

           The behavior of the daemon can be configured using udev.conf(5),
           its command line options, environment variables, and on the kernel
           command line, or changed dynamically with udevadm control.

## [](#OPTIONS)OPTIONS

           -d, --daemon
               Detach and run in the background.

               Added in version 186.

           -D, --debug
               Print debug messages to standard error.

               Added in version 186.

           -c, --children-max=
               Limit the number of events executed in parallel.

               Added in version 186.

           -e, --exec-delay=
               Delay the execution of each RUN{program} parameter by the
               given number of seconds. This option might be useful when
               debugging system crashes during coldplug caused by loading
               non-working kernel modules.

               Added in version 186.

           -t, --event-timeout=
               Set the number of seconds to wait for events to finish. After
               this time, the event will be terminated. The default is 180
               seconds.

               Added in version 216.

           -s, --timeout-signal=
               Set the signal which systemd-udevd will send to forked off
               processes after reaching event timeout. The setting can be
               overridden at boot time with the kernel command line option
               udev.timeout_signal=. Setting to SIGABRT may be helpful in
               order to debug worker timeouts. Defaults to SIGKILL. Note that
               setting the option on the command line overrides the setting
               from the configuration file.

               Added in version 246.

           -N, --resolve-names=
               Specify when systemd-udevd should resolve names of users and
               groups. When set to early (the default), names will be
               resolved when the rules are parsed. When set to late, names
               will be resolved for every event. When set to never, names
               will never be resolved and all devices will be owned by root.

               Added in version 186.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           Parameters prefixed with "rd." will be read when systemd-udevd is
           used in an initrd, those without will be processed both in the
           initrd and on the host.

           udev.log_level=, rd.udev.log_level=
               Set the log level.

               Added in version 247.

           udev.trace[=BOOL], rd.udev.trace[=BOOL]
               Enable/disable trace logging. When enabled, udev.log_level=
               will be ignored, and "debug" level is assumed.

               Added in version 258.

           udev.children_max=, rd.udev.children_max=
               Limit the number of events executed in parallel.

               Added in version 186.

           udev.exec_delay=, rd.udev.exec_delay=
               Delay the execution of each RUN{program} parameter by the
               given number of seconds. This option might be useful when
               debugging system crashes during coldplug caused by loading
               non-working kernel modules.

               Added in version 186.

           udev.event_timeout=, rd.udev.event_timeout=
               Wait for events to finish up to the given number of seconds.
               This option might be useful if events are terminated due to
               kernel drivers taking too long to initialize.

               Added in version 216.

           udev.timeout_signal=, rd.udev.timeout_signal=
               Specifies a signal that systemd-udevd will send to workers on
               timeout. Note that kernel command line option overrides both
               the setting in the configuration file and the one on the
               program command line.

               Added in version 246.

           udev.blockdev_read_only, rd.udev.blockdev_read_only
               If specified, mark all physical block devices read-only as
               they appear. Synthetic block devices (such as loopback block
               devices or device mapper devices) are left as they are. This
               is useful to guarantee that the contents of physical block
               devices remains unmodified during runtime, for example to
               implement fully stateless systems, for testing or for recovery
               situations where corrupted file systems shall not be corrupted
               further through accidental modification.

               A block device may be marked writable again by issuing the
               blockdev --setrw command, see blockdev(8) for details.

               Added in version 246.

           net.ifnames=
               Network interfaces are renamed to give them predictable names
               when possible. It is enabled by default; specifying 0 disables
               it.

               Added in version 199.

           net.naming_scheme=
               Network interfaces are renamed to give them predictable names
               when possible (unless net.ifnames=0 is specified, see above).
               With this kernel command line option it is possible to pick a
               specific version of this algorithm and override the default
               chosen at compilation time. Expects one of the naming scheme
               identifiers listed in systemd.net-naming-scheme(7), or
               "latest" to select the latest scheme known (to this particular
               version of systemd-udevd.service).

               Note that selecting a specific scheme is not sufficient to
               fully stabilize interface naming: the naming is generally
               derived from driver attributes exposed by the kernel. As the
               kernel is updated, previously missing attributes
               systemd-udevd.service is checking might appear, which affects
               older name derivation algorithms, too.

               Added in version 240.

           net.ifname_policy=policy1[,policy2,...][,MAC]
               Specifies naming policies applied when renaming network
               interfaces. Takes a list of policies and an optional MAC
               address separated with comma. Each policy value must be one of
               the policies understood by the NamePolicy= setting in .link
               files, e.g.  "onboard" or "path". See systemd.link(5) for more
               details. When the MAC address is specified, the policies are
               applied to the interface which has the address. When no MAC
               address is specified, the policies are applied to all
               interfaces. This kernel command line argument can be specified
               multiple times.

               This argument is not directly read by systemd-udevd, but is
               instead converted to a .link file by
               systemd-network-generator.service(8). For this argument to
               take effect, systemd-network-generator.service must be
               enabled.

               Example:

                   net.ifname_policy=keep,kernel,path,slot,onboard,01:23:45:67:89:ab
                   net.ifname_policy=keep,kernel,path,slot,onboard,mac

               This is mostly equivalent to creating the following .link
               files:

                   # 91-name-policy-with-mac.link
                   [Match]
                   MACAddress=01:23:45:67:89:ab

                   [Link]
                   NamePolicy=keep kernel path slot onboard
                   AlternativeNamePolicy=path slot onboard

               and

                   # 92-name-policy-for-all.link
                   [Match]
                   OriginalName=*

                   [Link]
                   NamePolicy=keep kernel path slot onboard mac
                   AlternativeNamePolicy=path slot onboard mac

               Added in version 250.

## [](#SEE_ALSO)SEE ALSO

           udev.conf(5), udev(7), udevadm(8)

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

    systemd 262~devel                                SYSTEMD-UDEVD.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [networkctl(1)](../man1/networkctl.1.html),  [sd-device(3)](../man3/sd-device.3.html),  [sd_device_enumerator_new(3)](../man3/sd_device_enumerator_new.3.html),  [sd-hwdb(3)](../man3/sd-hwdb.3.html),  [sd_hwdb_get(3)](../man3/sd_hwdb_get.3.html),  [sd_hwdb_new(3)](../man3/sd_hwdb_new.3.html),  [udev_new(3)](../man3/udev_new.3.html),  [iocost.conf(5)](../man5/iocost.conf.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.link(5)](../man5/systemd.link.5.html),  [udev.conf(5)](../man5/udev.conf.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.net-naming-scheme(7)](../man7/systemd.net-naming-scheme.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [udev(7)](../man7/udev.7.html),  [cfdisk(8)](../man8/cfdisk.8.html),  [fdisk(8)](../man8/fdisk.8.html),  [mkfs.bfs(8)](../man8/mkfs.bfs.8.html),  [mkfs.cramfs(8)](../man8/mkfs.cramfs.8.html),  [mkfs.minix(8)](../man8/mkfs.minix.8.html),  [mkswap(8)](../man8/mkswap.8.html),  [sfdisk(8)](../man8/sfdisk.8.html),  [systemd-networkd.service(8)](../man8/systemd-networkd.service.8.html),  [systemd-network-generator.service(8)](../man8/systemd-network-generator.service.8.html),  [systemd-vconsole-setup.service(8)](../man8/systemd-vconsole-setup.service.8.html),  [udevadm(8)](../man8/udevadm.8.html),  [wipefs(8)](../man8/wipefs.8.html)

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
