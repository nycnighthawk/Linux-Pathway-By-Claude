---
{"title": "services(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/services.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# services(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    services(5)                File Formats Manual                services(5)

## [](#NAME)NAME

           services - Internet network services list

## [](#DESCRIPTION)DESCRIPTION

           services is a plain ASCII file providing a mapping between human-
           friendly textual names for internet services, and their underlying
           assigned port numbers and protocol types.  Every networking
           program should look into this file to get the port number (and
           protocol) for its service.  The C library routines getservent(3),
           getservbyname(3), getservbyport(3), setservent(3), and
           endservent(3) support querying this file from programs.

           Port numbers are assigned by the IANA (Internet Assigned Numbers
           Authority), and their current policy is to assign both TCP and UDP
           protocols when assigning a port number.  Therefore, most entries
           will have two entries, even for TCP-only services.

           Port numbers below 1024 (so-called "low numbered" ports) can be
           bound to only by root (see bind(2), tcp(7), and udp(7)).  This is
           so clients connecting to low numbered ports can trust that the
           service running on the port is the standard implementation, and
           not a rogue service run by a user of the machine.  Well-known port
           numbers specified by the IANA are normally located in this root-
           only space.

           The presence of an entry for a service in the services file does
           not necessarily mean that the service is currently running on the
           machine.  See inetd.conf(5) for the configuration of Internet
           services offered.  Note that not all networking services are
           started by inetd(8), and so won't appear in inetd.conf(5).  In
           particular, news (NNTP) and mail (SMTP) servers are often
           initialized from the system boot scripts.

           The location of the services file is defined by _PATH_SERVICES in
           <netdb.h>.  This is usually set to /etc/services.

           Each line describes one service, and is of the form:

                  service-name   port/protocol   [aliases ...]

           where:

           service-name
                  is the friendly name the service is known by and looked up
                  under.  It is case sensitive.  Often, the client program is
                  named after the service-name.

           port   is the port number (in decimal) to use for this service.

           protocol
                  is the type of protocol to be used.  This field should
                  match an entry in the protocols(5) file.  Typical values
                  include tcp and udp.

           aliases
                  is an optional space or tab separated list of other names
                  for this service.  Again, the names are case sensitive.

           Either spaces or tabs may be used to separate the fields.

           Comments are started by the hash sign (#) and continue until the
           end of the line.  Blank lines are skipped.

           The service-name should begin in the first column of the file,
           since leading spaces are not stripped.  service-names can be any
           printable characters excluding space and tab.  However, a
           conservative choice of characters should be used to minimize
           compatibility problems.  For example, a-z, 0-9, and hyphen (-)
           would seem a sensible choice.

           Lines not matching this format should not be present in the file.
           (Currently, they are silently skipped by getservent(3),
           getservbyname(3), and getservbyport(3).  However, this behavior
           should not be relied on.)

           This file might be distributed over a network using a network-wide
           naming service like Yellow Pages/NIS or BIND/Hesiod.

           A sample services file might look like this:

               netstat         15/tcp
               qotd            17/tcp          quote
               msp             18/tcp          # message send protocol
               msp             18/udp          # message send protocol
               chargen         19/tcp          ttytst source
               chargen         19/udp          ttytst source
               ftp             21/tcp
               # 22 - unassigned
               telnet          23/tcp

## [](#FILES)FILES

           /etc/services
                  The Internet network services list

           <netdb.h>
                  Definition of _PATH_SERVICES

## [](#SEE_ALSO)SEE ALSO

           listen(2), endservent(3), getservbyname(3), getservbyport(3),
           getservent(3), setservent(3), inetd.conf(5), protocols(5),
           inetd(8)

           Assigned Numbers RFC, most recently RFC 1700, (AKA STD0002).

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

    Linux man-pages 6.19            2026-02-08                    services(5)

------------------------------------------------------------------------

Pages that refer to this page: [getaddrinfo(3)](../man3/getaddrinfo.3.html),  [getnameinfo(3)](../man3/getnameinfo.3.html),  [getservent(3)](../man3/getservent.3.html),  [getservent_r(3)](../man3/getservent_r.3.html),  [pcap-filter(7)](../man7/pcap-filter.7.html),  [nscd(8)](../man8/nscd.8.html),  [rpc.rquotad(8)](../man8/rpc.rquotad.8.html),  [rsyslogd(8)](../man8/rsyslogd.8.html)

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
