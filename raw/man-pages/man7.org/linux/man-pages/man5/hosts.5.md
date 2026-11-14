---
{"title": "hosts(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/hosts.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# hosts(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    hosts(5)                   File Formats Manual                   hosts(5)

## [](#NAME)NAME

           hosts - static table lookup for hostnames

## [](#SYNOPSIS)SYNOPSIS

           /etc/hosts

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes the format of the /etc/hosts file.
           This file is a simple text file that associates IP addresses with
           hostnames, one line per IP address.  For each host a single line
           should be present with the following information:

                  IP_address canonical_hostname [aliases...]

           The IP address can conform to either IPv4 or IPv6.  Fields of the
           entry are separated by any number of blanks and/or tab characters.
           Text from a "#" character until the end of the line is a comment,
           and is ignored.  Host names may contain only alphanumeric
           characters, minus signs ("-"), and periods (".").  They must begin
           with an alphabetic character and end with an alphanumeric
           character.  Optional aliases provide for name changes, alternate
           spellings, shorter hostnames, or generic hostnames (for example,
           localhost).  If required, a host may have two separate entries in
           this file; one for each version of the Internet Protocol (IPv4 and
           IPv6).

           The Berkeley Internet Name Domain (BIND) Server implements the
           Internet name server for UNIX systems.  It augments or replaces
           the /etc/hosts file or hostname lookup, and frees a host from
           relying on /etc/hosts being up to date and complete.

           In modern systems, even though the host table has been superseded
           by DNS, it is still widely used for:

           bootstrapping
                  Most systems have a small host table containing the name
                  and address information for important hosts on the local
                  network.  This is useful when DNS is not running, for
                  example during system bootup.

           NIS    Sites that use NIS use the host table as input to the NIS
                  host database.  Even though NIS can be used with DNS, most
                  NIS sites still use the host table with an entry for all
                  local hosts as a backup.

           isolated nodes
                  Very small sites that are isolated from the network use the
                  host table instead of DNS.  If the local information rarely
                  changes, and the network is not connected to the Internet,
                  DNS offers little advantage.

## [](#FILES)FILES

           /etc/hosts

## [](#NOTES)NOTES

           Modifications to this file normally take effect immediately,
           except in cases where the file is cached by applications.

       Historical notes
           RFC 952 gave the original format for the host table, though it has
           since changed.

           Before the advent of DNS, the host table was the only way of
           resolving hostnames on the fledgling Internet.  Indeed, this file
           could be created from the official host data base maintained at
           the Network Information Control Center (NIC), though local changes
           were often required to bring it up to date regarding unofficial
           aliases and/or unknown hosts.  The NIC no longer maintains the
           hosts.txt files, though looking around at the time of writing
           (circa 2000), there are historical hosts.txt files on the WWW.  I
           just found three, from 92, 94, and 95.

## [](#EXAMPLES)EXAMPLES

           # The following lines are desirable for IPv4 capable hosts
           127.0.0.1       localhost

           # 127.0.1.1 is often used for the FQDN of the machine
           127.0.1.1       thishost.example.org   thishost
           192.168.1.10    foo.example.org        foo
           192.168.1.13    bar.example.org        bar
           146.82.138.7    master.debian.org      master
           209.237.226.90  www.opensource.org

           # The following lines are desirable for IPv6 capable hosts
           ::1             localhost ip6-localhost ip6-loopback
           ff02::1         ip6-allnodes
           ff02::2         ip6-allrouters

## [](#SEE_ALSO)SEE ALSO

           hostname(1), resolver(3), host.conf(5), resolv.conf(5),
           resolver(5), hostname(7), named(8)

           Internet RFC 952

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

    Linux man-pages 6.19            2026-02-11                       hosts(5)

------------------------------------------------------------------------

Pages that refer to this page: [getent(1)](../man1/getent.1.html),  [hostname(1)](../man1/hostname.1.html),  [gethostbyname(3)](../man3/gethostbyname.3.html),  [getnameinfo(3)](../man3/getnameinfo.3.html),  [inet(3)](../man3/inet.3.html),  [host.conf(5)](../man5/host.conf.5.html),  [resolv.conf(5)](../man5/resolv.conf.5.html),  [systemd.rr(5)](../man5/systemd.rr.5.html),  [pcap-filter(7)](../man7/pcap-filter.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [nscd(8)](../man8/nscd.8.html),  [rarp(8)](../man8/rarp.8.html),  [systemd-resolved.service(8)](../man8/systemd-resolved.service.8.html)

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
