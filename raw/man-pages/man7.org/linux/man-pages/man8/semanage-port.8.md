---
{"title": "semanage-port(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/semanage-port.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semanage-port(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    semanage-port(8)                                         semanage-port(8)

## [](#NAME)NAME

           semanage-port - SELinux Policy Management port mapping tool

## [](#SYNOPSIS)SYNOPSIS

           semanage port [-h] [-n] [-N] [-S STORE] [ --add -t TYPE -p
           PROTOCOL -r RANGE port_name | port_range | --delete -p PROTOCOL
           port_name | port_range | --deleteall | --extract | --list [-C] |
           --modify -t TYPE -p PROTOCOL -r RANGE port_name | port_range ]

## [](#DESCRIPTION)DESCRIPTION

           semanage is used to configure certain elements of SELinux policy
           without requiring modification to or recompilation from policy
           sources.  semanage port controls the port number to port type
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

           -t TYPE, --type TYPE
                  SELinux type for the object

           -r RANGE, --range RANGE
                  MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range
                  for SELinux login mapping defaults to the SELinux user
                  record range. SELinux Range for SELinux user defaults to
                  s0.

           -p PROTO, --proto PROTO
                  Protocol for the specified port (tcp|udp|dccp|sctp) or
                  internet protocol version for the specified node
                  (ipv4|ipv6).

## [](#EXAMPLE)EXAMPLE

           List all port definitions
           # semanage port -l
           Allow Apache to listen on tcp port 81 (i.e. assign tcp port 81 label http_port_t, which apache is allowed to listen on)
           # semanage port -a -t http_port_t -p tcp 81
           Allow sshd to listen on tcp port 8991 (i.e. assign tcp port 8991 label ssh_port_t, which sshd is allowed to listen on)
           # semanage port -a -t ssh_port_t -p tcp 8991
           Add a custom port 9999 with MLS range s0:c0.c255 (MLS/MCS systems only). Verify with seinfo.
           # semanage port -a -t http_port_t -p tcp -r s0:c0.c255 9999
           # seinfo --portcon -x | grep 9999

## [](#SEE_ALSO)SEE ALSO

           selinux(8), semanage(8)

## [](#AUTHOR)AUTHOR

           This man page was written by Daniel Walsh <dwalsh@redhat.com>

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

                                     20130617                semanage-port(8)

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
