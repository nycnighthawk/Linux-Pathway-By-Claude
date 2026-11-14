---
{"title": "mailaddr(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/mailaddr.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mailaddr(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mailaddr(7)          Miscellaneous Information Manual         mailaddr(7)

## [](#NAME)NAME

           mailaddr - mail addressing description

## [](#DESCRIPTION)DESCRIPTION

           This manual page gives a brief introduction to SMTP mail
           addresses, as used on the Internet.  These addresses are in the
           general format

               user@domain

           where a domain is a hierarchical dot-separated list of subdomains.
           These examples are valid forms of the same address:

               john.doe@monet.example.com
               John Doe <john.doe@monet.example.com>
               john.doe@monet.example.com (John Doe)

           The domain part ("monet.example.com") is a mail-accepting domain.
           It can be a host and in the past it usually was, but it doesn't
           have to be.  The domain part is not case sensitive.

           The local part ("john.doe") is often a username, but its meaning
           is defined by the local software.  Sometimes it is case sensitive,
           although that is unusual.  If you see a local-part that looks like
           garbage, it is usually because of a gateway between an internal e-
           mail system and the net, here are some examples:

               "surname/admd=telemail/c=us/o=hp/prmd=hp"@some.where
               USER%SOMETHING@some.where
               machine!machine!name@some.where
               I2461572@some.where

           (These are, respectively, an X.400 gateway, a gateway to an
           arbitrary internal mail system that lacks proper internet support,
           an UUCP gateway, and the last one is just boring username policy.)

           The real-name part ("John Doe") can either be placed before <>, or
           in () at the end.  (Strictly speaking the two aren't the same, but
           the difference is beyond the scope of this page.)  The name may
           have to be quoted using "", for example, if it contains ".":

               "John Q. Doe" <john.doe@monet.example.com>

       Abbreviation
           Some mail systems let users abbreviate the domain name.  For
           instance, users at example.com may get away with "john.doe@monet"
           to send mail to John Doe.  This behavior is deprecated.  Sometimes
           it works, but you should not depend on it.

       Route-addrs
           In the past, sometimes one had to route a message through several
           hosts to get it to its final destination.  Addresses which show
           these relays are termed "route-addrs".  These use the syntax:

               <@hosta,@hostb:user@hostc>

           This specifies that the message should be sent to hosta, from
           there to hostb, and finally to hostc.  Many hosts disregard route-
           addrs and send directly to hostc.

           Route-addrs are very unusual now.  They occur sometimes in old
           mail archives.  It is generally possible to ignore all but the
           "user@hostc" part of the address to determine the actual address.

       Postmaster
           Every site is required to have a user or user alias designated
           "postmaster" to which problems with the mail system may be
           addressed.  The "postmaster" address is not case sensitive.

## [](#FILES)FILES

           /etc/aliases
           ~/.forward

## [](#SEE_ALSO)SEE ALSO

           mail(1), aliases(5), forward(5), sendmail(8)

           IETF RFC 5322 ⟨http://www.ietf.org/rfc/rfc5322.txt⟩

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

    4.2 Berkeley Distribution       2026-02-08                    mailaddr(7)

------------------------------------------------------------------------

Pages that refer to this page: [hostname(7)](../man7/hostname.7.html),  [uri(7)](../man7/uri.7.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man7/mailaddr.7.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
