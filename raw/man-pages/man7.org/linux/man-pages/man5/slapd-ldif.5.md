---
{"title": "slapd-ldif(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-ldif.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-ldif(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-LDIF(5)              File Formats Manual              SLAPD-LDIF(5)

## [](#NAME)NAME

           slapd-ldif - LDIF backend to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The LDIF backend to slapd(8) is a basic storage backend that
           stores entries in text files in LDIF format, and exploits the
           filesystem to create the tree structure of the database.  It is
           intended as a cheap, low performance easy to use backend, and it
           is exploited by higher-level internal structures to provide a
           permanent storage.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the LDIF backend database.  That
           is, they must follow a "database ldif" line and come before any
           subsequent "backend" or "database" lines.  Other database options
           are described in the slapd.conf(5) manual page.

           directory <dir>
                  Specify the directory where the database tree starts.  The
                  directory must exist and grant appropriate permissions
                  (rwx) to the identity slapd is running with.

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The LDIF backend does not honor any of the access control
           semantics described in slapd.access(5).  Only read (=r) access to
           the entry pseudo-attribute and to the other attribute values of
           the entries returned by the search operation is honored, which is
           performed by the frontend.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd(8), ldif(5).

## [](#AUTHOR)AUTHOR

           Eric Stokes

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

    OpenLDAP LDVERSION             RELEASEDATE                  SLAPD-LDIF(5)

------------------------------------------------------------------------

Pages that refer to this page: [ldif(5)](../man5/ldif.5.html),  [slapd.backends(5)](../man5/slapd.backends.5.html)

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
