---
{"title": "ip-vrf(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-vrf.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-vrf(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CAVEATS](#CAVEATS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-VRF(8)                         Linux                         IP-VRF(8)

## [](#NAME)NAME

           ip-vrf - run a command against a vrf

## [](#SYNOPSIS)SYNOPSIS

           ip vrf  { COMMAND | help }

           ip vrf show [ NAME ]

           ip vrf identify [ PID ]

           ip vrf pids NAME

           ip vrf exec [ NAME ] command...

## [](#DESCRIPTION)DESCRIPTION

           A VRF provides traffic isolation at layer 3 for routing, similar
           to how a VLAN is used to isolate traffic at layer 2.
           Fundamentally, a VRF is a separate routing table. Network devices
           are associated with a VRF by enslaving the device to the VRF. At
           that point network addresses assigned to the device are local to
           the VRF with host and connected routes moved to the table
           associated with the VRF.

           A process can specify a VRF using several APIs -- binding the
           socket to the VRF device using SO_BINDTODEVICE, setting the VRF
           association using IP_UNICAST_IF or IPV6_UNICAST_IF, or specifying
           the VRF for a specific message using IP_PKTINFO or IPV6_PKTINFO.

           By default a process is not bound to any VRF. An association can
           be set explicitly by making the program use one of the APIs
           mentioned above or implicitly using a helper to set
           SO_BINDTODEVICE for all IPv4 and IPv6 sockets (AF_INET and
           AF_INET6) when the socket is created. This ip-vrf command is a
           helper to run a command against a specific VRF with the VRF
           association inherited parent to child.

           ip vrf show [ NAME ] - Show all configured VRF

                  This command lists all VRF and their corresponding table
                  ids. If NAME is given, then only that VRF and table id is
                  shown. The latter command is useful for scripting where the
                  table id for a VRF is needed.

           ip vrf exec [ NAME ] cmd ... - Run cmd against the named VRF

                  This command allows applications that are VRF unaware to be
                  run against a VRF other than the default VRF (main table).
                  A command can be run against the default VRF by passing the
                  "default" as the VRF name. This is useful if the current
                  shell is associated with another VRF (e.g, Management VRF).

                  This command requires the system to be booted with cgroup
                  v2 (e.g. with systemd, add
                  systemd.unified_cgroup_hierarchy=1 to the kernel command
                  line).

                  This command also requires to be run as root. Alternatively
                  it can be run by an unprivileged user if the following
                  capabilities(7) are given:

                  CAP_BPF
                         To load the BPF program.

                  CAP_NET_ADMIN
                         To set the socket into the cgroup.

                  CAP_DAC_OVERRIDE
                         To create the cgroup subdir in /sys.

                  If these capabilities are added and if ip(8) is built with
                  libcap(3) then these capabilities will be dropped before
                  cmd is executed by ip vrf exec.  For every other
                  unprivileged invocation of ip(8) all capabilities will be
                  dropped.

                  NOTE: capabilities will NOT be dropped if CAP_NET_ADMIN is
                  set to INHERITABLE to avoid breaking programs with ambient
                  capabilities that call ip.

           ip vrf identify [PID] - Report VRF association for process

                  This command shows the VRF association of the specified
                  process. If PID is not specified then the id of the current
                  process is used.

           ip vrf pids NAME - Report processes associated with the named VRF

                  This command shows all process ids that are associated with
                  the given VRF.

## [](#CAVEATS)CAVEATS

           This command requires a kernel compiled with CGROUPS and
           CGROUP_BPF enabled.

           The VRF helper *only* affects network layer sockets.

## [](#EXAMPLES)EXAMPLES

           ip vrf exec red ssh 10.100.1.254
                  Executes ssh to 10.100.1.254 against the VRF red table.

## [](#SEE_ALSO)SEE ALSO

           ip(8), ip-link(8), ip-address(8), ip-route(8), ip-neighbor(8)

## [](#AUTHOR)AUTHOR

           Original Manpage by David Ahern

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

    iproute2                        7 Dec 2016                      IP-VRF(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html)

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
