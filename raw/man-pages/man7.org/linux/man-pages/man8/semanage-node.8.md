---
{"title": "semanage-node(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/semanage-node.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semanage-node(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    semanage-node(8)                                         semanage-node(8)

## [](#NAME)NAME

           semanage-node - SELinux Policy Management node mapping tool

## [](#SYNOPSIS)SYNOPSIS

           semanage node [-h] [-n] [-N] [-S STORE] [ --add -M NETMASK -p
           PROTOCOL -t TYPE -r RANGE node | --delete -M NETMASK -p PROTOCOL
           node | --deleteall | --extract | --list [-C] | --modify -M NETMASK
           -p PROTOCOL -t TYPE -r RANGE node ]

## [](#DESCRIPTION)DESCRIPTION

           semanage is used to configure certain elements of SELinux policy
           without requiring modification to or recompilation from policy
           sources.  semanage node controls the IP address to node type
           definitions.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Show this help message and exit

           -n, --noheading
                  Do not print heading when listing the specified object type

           -N, --noreload
                  Do not reload policy after commit

           -S STORE, --store STORE
                  Select an alternate SELinux Policy Store to manage

           -C, --locallist
                  List local customizations

           -a, --add
                  Add a record of the specified object type

           -d, --delete
                  Delete a record of the specified object type

           -m, --modify
                  Modify a record of the specified object type

           -l, --list
                  List records of the specified object type

           -E, --extract
                  Extract customizable commands, for use within a transaction

           -D, --deleteall
                  Remove all local customizations

           -M NETMASK, --netmask NETMASK
                  Network Mask, either in CIDR (/16) or address mask notation
                  (255.255.0.0, ffff::)

           -t TYPE, --type TYPE
                  SELinux type for the object

           -r RANGE, --range RANGE
                  MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range
                  for SELinux login mapping defaults to the SELinux user
                  record range. SELinux Range for SELinux user defaults to
                  s0.

           -p PROTO, --proto PROTO
                  Protocol for the specified port (tcp|udp) or internet
                  protocol version for the specified node (ipv4|ipv6).

## [](#EXAMPLE)EXAMPLE

           Apply type node_t to ipv4 node 127.0.0.2
           # semanage node -a -t node_t -p ipv4 -M 255.255.255.255 127.0.0.2

## [](#SEE_ALSO)SEE ALSO

           selinux(8), semanage(8)

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

                                     20130617                semanage-node(8)

------------------------------------------------------------------------

Pages that refer to this page: [semanage(8)](../man8/semanage.8.html)

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
