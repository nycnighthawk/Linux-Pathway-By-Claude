---
{"title": "ip-sr(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-sr.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-sr(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-SR(8)                          Linux                          IP-SR(8)

## [](#NAME)NAME

           ip-sr - IPv6 Segment Routing management

## [](#SYNOPSIS)SYNOPSIS

           ip sr  { COMMAND | help }

           ip sr hmac show

           ip sr hmac set KEYID ALGO

           ip sr tunsrc show

           ip sr tunsrc set ADDRESS

## [](#DESCRIPTION)DESCRIPTION

           The ip sr command is used to configure IPv6 Segment Routing (SRv6)
           internal parameters.

           Those parameters include the mapping between an HMAC key ID and
           its associated hashing algorithm and secret, and the IPv6 address
           to use as source for encapsulated packets.

           The ip sr hmac set command prompts for a newline-terminated
           "passphrase" that will be used as the HMAC secret for the
           corresponding key ID. This "passphrase" is not stretched, and it
           is used directly as the HMAC key.  Therefore it must have enough
           entropy to be used as a key. For example, a correct use would be
           to use a passphrase that was generated using
           head -c 32 /dev/random | base64 -w 0.

           A blank "passphrase" removes the mapping.

           The currently supported algorithms for ALGO are sha1 and sha256.

           If the tunnel source is set to the address :: (which is the
           default), then an address of the egress interface will be
           selected. As this operation may hinder performances, it is
           recommended to set a non-default address.

## [](#EXAMPLES)EXAMPLES

       Configure an HMAC mapping for key ID 42 and hashing algorithm SHA-256
           # ip sr hmac set 42 sha256

       Set the tunnel source address to 2001:db8::1
           # ip sr tunsrc set 2001:db8::1

## [](#SEE_ALSO)SEE ALSO

           ip-route(8)

## [](#BUGS)BUGS

           ip sr hmac set does not stretch the passphrase.

## [](#AUTHOR)AUTHOR

           David Lebrun <david.lebrun@uclouvain.be>

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

    iproute2                       14 Apr 2017                       IP-SR(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html),  [ip-route(8)](../man8/ip-route.8.html)

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
