---
{"title": "network_namespaces(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/network_namespaces.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# network_namespaces(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    network...espaces(7) Miscellaneous Information Manualnetwork...espaces(7)

## [](#NAME)NAME

           network_namespaces - overview of Linux network namespaces

## [](#DESCRIPTION)DESCRIPTION

           Network namespaces provide isolation of the system resources
           associated with networking: network devices, IPv4 and IPv6
           protocol stacks, IP routing tables, firewall rules, the /proc/net
           directory (which is a symbolic link to /proc/pid/net), the
           /sys/class/net directory, various files under /proc/sys/net, port
           numbers (sockets), and so on.  In addition, network namespaces
           isolate the UNIX domain abstract socket namespace (see unix(7)).

           A physical network device can live in exactly one network
           namespace.  When a network namespace is freed (i.e., when the last
           process in the namespace terminates), its physical network devices
           are moved back to the initial network namespace (not to the
           namespace of the parent of the process).

           A virtual network (veth(4)) device pair provides a pipe-like
           abstraction that can be used to create tunnels between network
           namespaces, and can be used to create a bridge to a physical
           network device in another namespace.  When a namespace is freed,
           the veth(4) devices that it contains are destroyed.

           Use of network namespaces requires a kernel that is configured
           with the CONFIG_NET_NS option.

## [](#SEE_ALSO)SEE ALSO

           nsenter(1), unshare(1), clone(2), veth(4), proc(5), sysfs(5),
           namespaces(7), user_namespaces(7), brctl(8), ip(8), ip-address(8),
           ip-link(8), ip-netns(8), iptables(8), ovs-vsctl(8)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08           network...espaces(7)

------------------------------------------------------------------------

Pages that refer to this page: [getino(1)](../man1/getino.1.html),  [nsenter(1)](../man1/nsenter.1.html),  [unshare(1)](../man1/unshare.1.html),  [clone(2)](../man2/clone.2.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [veth(4)](../man4/veth.4.html),  [proc_pid_net(5)](../man5/proc_pid_net.5.html),  [systemd.socket(5)](../man5/systemd.socket.5.html),  [namespaces(7)](../man7/namespaces.7.html),  [rdma-system(8)](../man8/rdma-system.8.html)

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
