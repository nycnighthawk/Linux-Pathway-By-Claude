---
{"title": "slapo-pbind(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-pbind.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-pbind(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-PBIND(5)             File Formats Manual             SLAPO-PBIND(5)

## [](#NAME)NAME

           slapo-pbind - proxy bind overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The pbind overlay to slapd(8) forwards Simple Binds on a local
           database to a remote LDAP server instead of processing them
           locally. The remote connection is managed using an instance of the
           ldap backend.

           The pbind overlay uses a subset of the ldap backend's config
           directives. They are described in more detail in slapd-ldap(5).

           Note: this overlay is built into the ldap backend; it is not a
           separate module.

           overlay pbind
                  This directive adds the proxy bind overlay to the current
                  backend.  The proxy bind overlay may be used with any
                  backend, but it is mainly intended for use with local
                  storage backends.

           uri <ldapurl>
                  LDAP server to use.

           tls <TLS parameters>
                  Specify the use of TLS.

           network-timeout <time>
                  Set the network timeout.

           quarantine <quarantine parameters>
                  Turns on quarantine of URIs that returned LDAP_UNAVAILABLE.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd-ldap(5), slapd(8).

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

    OpenLDAP LDVERSION             RELEASEDATE                 SLAPO-PBIND(5)

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
