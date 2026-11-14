---
{"title": "hostname(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/hostname.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# hostname(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    hostname(7)          Miscellaneous Information Manual         hostname(7)

## [](#NAME)NAME

           hostname - hostname resolution description

## [](#DESCRIPTION)DESCRIPTION

           Hostnames are domains, where a domain is a hierarchical dot-
           separated list of subdomains; for example, the machine "monet", in
           the "example" subdomain of the "com" domain, would be represented
           as "monet.example.com".

           Each element of the hostname must be from 1 to 63 characters long
           and the entire hostname, including the dots, can be at most 253
           characters long.  Valid characters for hostnames are ASCII(7)
           letters from a to z, the digits from 0 to 9, and the hyphen (-).
           A hostname may not start nor end with a hyphen.

           Hostnames are often used with network client and server programs,
           which must generally translate the name to an address for use.
           (This task is generally performed by either getaddrinfo(3) or the
           obsolete gethostbyname(3).)

           Hostnames are resolved by the NSS framework in glibc according to
           the hosts configuration in nsswitch.conf(5).  The DNS-based name
           resolver (in the dns NSS service module) resolves them in the
           following fashion.

           If the name consists of a single component (that is, contains no
           dot), and if the environment variable HOSTALIASES is set to the
           name of a file, that file is searched for any string matching the
           input hostname.  The file should consist of lines made up of two
           white-space separated strings, the first of which is the hostname
           alias, and the second of which is the complete hostname to be
           substituted for that alias.  If a case-insensitive match is found
           between the hostname to be resolved and the first field of a line
           in the file, the substituted name is looked up with no further
           processing.

           If the input name ends with a trailing dot, the trailing dot is
           removed, and the remaining name is looked up with no further
           processing.

           If the input name does not end with a trailing dot, it is looked
           up by searching through a list of domains until a match is found.
           The default search list includes first the local domain, then its
           parent domains with at least 2 name components (longest first).
           For example, in the domain cs.example.com, the name lithium.cchem
           will be checked first as lithium.cchem.cs.example and then as
           lithium.cchem.example.com.  lithium.cchem.com will not be tried,
           as there is only one component remaining from the local domain.
           The search path can be changed from the default by a system-wide
           configuration file (see resolver(5)).

## [](#SEE_ALSO)SEE ALSO

           getaddrinfo(3), gethostbyname(3), nsswitch.conf(5), resolver(5),
           mailaddr(7), named(8)

           IETF RFC 1123 ⟨http://www.ietf.org/rfc/rfc1123.txt⟩

           IETF RFC 1178 ⟨http://www.ietf.org/rfc/rfc1178.txt⟩

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

    Linux man-pages 6.19            2026-04-07                    hostname(7)

------------------------------------------------------------------------

Pages that refer to this page: [hostname(1)](../man1/hostname.1.html),  [getaddrinfo(3)](../man3/getaddrinfo.3.html),  [getaddrinfo_a(3)](../man3/getaddrinfo_a.3.html),  [gethostbyname(3)](../man3/gethostbyname.3.html),  [getnameinfo(3)](../man3/getnameinfo.3.html),  [resolver(3)](../man3/resolver.3.html),  [host.conf(5)](../man5/host.conf.5.html),  [hostname(5)](../man5/hostname.5.html),  [hosts(5)](../man5/hosts.5.html),  [resolv.conf(5)](../man5/resolv.conf.5.html),  [sm-notify(8)](../man8/sm-notify.8.html)

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
