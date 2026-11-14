---
{"title": "slapd-null(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-null.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-null(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [EXAMPLE](#EXAMPLE) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-NULL(5)              File Formats Manual              SLAPD-NULL(5)

## [](#NAME)NAME

           slapd-null - Null backend to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The Null backend to slapd(8) is surely the most useful part of
           slapd:
           - Searches return success but no entries.
           - Compares return compareFalse.
           - Updates return success (unless readonly is on) but do nothing.
           - Binds other than as the rootdn fail unless the database option
           "bind on" is given.
           - The slapadd(8) and slapcat(8) tools are equally exciting.
           Inspired by the /dev/null device.

## [](#CONFIGURATION)CONFIGURATION

           This slapd.conf option applies to the NULL backend database.  That
           is, it must follow a "database null" line and come before any
           subsequent "database" lines.  Other database options are described
           in the slapd.conf(5) manual page.

           bind <on/off>
                  Allow binds as any DN in this backend's suffix, with any
                  password.  The default is "off".

           dosearch <on/off>
                  If enabled, a single entry will be returned on all search
                  requests.  The entry's DN will be the same as the database
                  suffix.  The default is "off".

## [](#EXAMPLE)EXAMPLE

           Here is a possible slapd.conf extract using the Null backend:

                  database null
                  suffix   "cn=Nothing"
                  bind     on

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The null backend does not honor any of the access control
           semantics described in slapd.access(5).

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd(8), slapadd(8), slapcat(8).

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

    OpenLDAP LDVERSION             RELEASEDATE                  SLAPD-NULL(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.backends(5)](../man5/slapd.backends.5.html),  [slapcat(8)](../man8/slapcat.8.html),  [slapschema(8)](../man8/slapschema.8.html)

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
