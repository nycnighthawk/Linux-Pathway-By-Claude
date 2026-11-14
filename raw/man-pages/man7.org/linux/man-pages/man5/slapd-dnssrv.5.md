---
{"title": "slapd-dnssrv(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-dnssrv.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-dnssrv(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-DNSSRV(5)            File Formats Manual            SLAPD-DNSSRV(5)

## [](#NAME)NAME

           slapd-dnssrv - DNS SRV referral backend to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The DNSSRV backend to slapd(8) serves up referrals based upon SRV
           resource records held in the Domain Name System.

           This backend is experimental.

## [](#CONFIGURATION)CONFIGURATION

           The DNSSRV backend has no backend nor database specific options.
           It is configured simply by "database dnssrv" followed a suffix
           directive, e.g. suffix "".

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The dnssrv backend does not honor all ACL semantics as described
           in slapd.access(5).  In fact, this backend only implements the
           search operation when the manageDSAit control (RFC 3296) is used,
           otherwise for every operation a referral, whenever appropriate, or
           an error is returned.  Currently, there is no means to condition
           the returning of the referral by means of ACLs; no access control
           is implemented, except for read (=r) access to the returned
           entries, which is actually provided by the frontend.  Note,
           however, that the information returned by this backend is
           collected through the DNS, so it is public by definition.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           "OpenLDAP Root Service - An experimental LDAP referral service"
           [RFC 3088],
           "OpenLDAP LDAP Root Service"
           <http://www.openldap.org/faq/?file=393)>,
           slapd.conf(5), slapd(8)

## [](#COLOPHON)COLOPHON

           This page is part of the OpenLDAP (an open source implementation
           of the Lightweight Directory Access Protocol) project.
           Information about the project can be found at 
           ⟨http://www.openldap.org/⟩.  If you have a bug report for this
           manual page, see ⟨http://www.openldap.org/its/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.openldap.org/openldap/openldap.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    OpenLDAP LDVERSION             RELEASEDATE                SLAPD-DNSSRV(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.backends(5)](../man5/slapd.backends.5.html)

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
