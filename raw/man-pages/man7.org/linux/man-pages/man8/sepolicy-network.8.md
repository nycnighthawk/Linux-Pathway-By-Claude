---
{"title": "sepolicy-network(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sepolicy-network.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sepolicy-network(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sepolicy-network(8)                                   sepolicy-network(8)

## [](#NAME)NAME

           sepolicy-network - Examine the SELinux Policy and generate a
           network report

## [](#SYNOPSIS)SYNOPSIS

           sepolicy network [-h] (-l | -a application [application ...] | -p
           PORT [PORT ...] | -t TYPE [TYPE ...] | -d DOMAIN [DOMAIN ...])

## [](#DESCRIPTION)DESCRIPTION

           Use sepolicy network to examine SELinux Policy and generate
           network reports.

## [](#OPTIONS)OPTIONS

           -a, --application
                  Generate a report listing the ports to which the specified
                  init application is allowed to connect and or bind

           -d, --domain
                  Generate a report listing the ports to which the specified
                  domain is allowed to connect and or bind

           -l, --list
                  List all Network Port Types defined in SELinux Policy

           -h, --help
                  Display help message

           -t, --type
                  Generate a report listing the port numbers associate with
                  the specified SELinux port type

           -p, --port
                  Generate a report listing the SELinux port types associate
                  with the specified port number

## [](#EXAMPLES)EXAMPLES

           sepolicy network -p 22
           22: tcp ssh_port_t 22
           22: udp reserved_port_t 1-511
           22: tcp reserved_port_t 1-511

           sepolicy network -a /usr/sbin/sshd
           sshd_t: tcp name_connect
                111 (portmap_port_t)
                53 (dns_port_t)
                88, 750, 4444 (kerberos_port_t)
                9080 (ocsp_port_t)
                9180, 9701, 9443-9447 (pki_ca_port_t)
                32768-61000 (ephemeral_port_t)
                all ports < 1024 (reserved_port_type)
                all ports with out defined types (port_t)
           sshd_t: tcp name_bind
                22 (ssh_port_t)
                5900-5983, 5985-5999 (vnc_port_t)
                6000-6020 (xserver_port_t)
                32768-61000 (ephemeral_port_t)
                all ports > 500 and  < 1024 (rpc_port_type)
                all ports with out defined types (port_t)
           sshd_t: udp name_bind
                32768-61000 (ephemeral_port_t)
                all ports > 500 and  < 1024 (rpc_port_type)
                all ports with out defined types (port_t)

## [](#AUTHOR)AUTHOR

           This man page was written by Daniel Walsh <dwalsh@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           sepolicy(8), selinux(8), semanage(8)

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                     20121005             sepolicy-network(8)

------------------------------------------------------------------------

Pages that refer to this page: [sepolicy(8)](../man8/sepolicy.8.html)

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
