---
{"title": "slapo-sssvlv(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-sssvlv.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-sssvlv(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-SSSVLV(5)            File Formats Manual            SLAPO-SSSVLV(5)

## [](#NAME)NAME

           slapo-sssvlv - Server Side Sorting and Virtual List View overlay
           to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           This overlay implements the LDAP Server Side Sorting (RFC2891)
           control as well as the Virtual List View control. It also replaces
           the default implementation of the LDAP PagedResults (RFC2696)
           control, to ensure that it works with Sorting. The overlay can be
           used with any backend or globally for all backends.

           Since a complete result set must be generated in memory before
           sorting can be performed, processing sort requests can have a
           large impact on the server's memory use. As such, any connection
           is limited to having only a limited number of sort requests active
           at a time. Additional limits may be configured as described below.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the SSSVLV overlay.  They should
           appear after the overlay directive.

           sssvlv-max <num>
                  Set the maximum number of concurrent sort requests allowed
                  across all connections. The default is one half of the
                  number of server threads.

           sssvlv-maxkeys <num>
                  Set the maximum number of keys allowed in a sort request.
                  The default is 5.

           sssvlv-maxperconn <num>
                  Set the maximum number of concurrent paged search requests
                  per connection. The default is 5. The number of concurrent
                  requests remains limited by sssvlv-max.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

           ETCDIR/slapd.d
                  default slapd configuration directory

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5).

           "OpenLDAP Administrator's Guide"
           (http://www.OpenLDAP.org/doc/admin/)

           IETF LDAP Virtual List View proposal by D. Boreham, J.
           Sermersheim, and A. Kashi in IETF document "draft-ietf-ldapext-
           ldapv3-vlv-09.txt".

## [](#AUTHOR)AUTHOR

           Howard Chu

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

    OpenLDAP LDVERSION             RELEASEDATE                SLAPO-SSSVLV(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.overlays(5)](../man5/slapd.overlays.5.html)

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
