---
{"title": "ip-fou(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-fou.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-fou(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-FOU(8)                         Linux                         IP-FOU(8)

## [](#NAME)NAME

           ip-fou - Foo-over-UDP receive port configuration

           ip-gue - Generic UDP Encapsulation receive port configuration

## [](#SYNOPSIS)SYNOPSIS

           ip [ OPTIONS ] fou  { COMMAND | help }

           ip fou add port PORT { gue | ipproto PROTO  } [ local IFADDR  ] [
                   peer IFADDR  ] [ peer_port PORT  ] [ dev IFNAME  ]
           ip fou del port PORT [ local IFADDR  ] [ peer IFADDR  ] [
                   peer_port PORT  ] [ dev IFNAME  ]
           ip fou show

## [](#DESCRIPTION)DESCRIPTION

           The ip fou commands are used to create and delete receive ports
           for Foo-over-UDP (FOU) as well as Generic UDP Encapsulation (GUE).

           Foo-over-UDP allows encapsulating packets of an IP protocol
           directly over UDP. The receiver infers the protocol of a packet
           received on a FOU UDP port to be the protocol configured for the
           port.

           Generic UDP Encapsulation (GUE) encapsulates packets of an IP
           protocol within UDP and an encapsulation header. The encapsulation
           header contains the IP protocol number for the encapsulated
           packet.

           When creating a FOU or GUE receive port, the port number is
           specified in PORT argument. If FOU is used, the IP protocol number
           associated with the port is specified in PROTO argument. You can
           bind a port to a local address/interface, by specifying the
           address in the local IFADDR argument or the device in the IFNAME
           argument. If you would like to connect the port, you can specify
           the peer address in the peer IFADDR argument and peer port in the
           peer_port PORT argument.

           A FOU or GUE receive port is deleted by specifying PORT in the
           delete command, as well as local address/interface or peer
           address/port (if set).

## [](#EXAMPLES)EXAMPLES

       Configure a FOU receive port for GRE bound to 7777
           # ip fou add port 7777 ipproto 47

       Configure a FOU receive port for IPIP bound to 8888
           # ip fou add port 8888 ipproto 4

       Configure a GUE receive port bound to 9999
           # ip fou add port 9999 gue

       Delete the GUE receive port bound to 9999
           # ip fou del port 9999

       Configure a FOU receive port for GRE bound to 1.2.3.4:7777
           # ip fou add port 7777 ipproto 47 local 1.2.3.4

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           Tom Herbert <therbert@google.com>

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

    iproute2                        2 Nov 2014                      IP-FOU(8)

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
