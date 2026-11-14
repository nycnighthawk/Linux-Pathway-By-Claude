---
{"title": "slapo-translucent(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-translucent.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-translucent(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [CAVEATS](#CAVEATS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-TRANSLUCENT(5)       File Formats Manual       SLAPO-TRANSLUCENT(5)

## [](#NAME)NAME

           slapo-translucent - Translucent Proxy overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The Translucent Proxy overlay can be used with a backend database
           such as slapd-mdb(5) to create a "translucent proxy".  Entries
           retrieved from a remote LDAP server may have some or all
           attributes overridden, or new attributes added, by entries in the
           local database before being presented to the client.

           A search operation is first populated with entries from the remote
           LDAP server, the attributes of which are then overridden with any
           attributes defined in the local database. Local overrides may be
           populated with the add, modify , and modrdn operations, the use of
           which is restricted to the root user.

           A compare operation will perform a comparison with attributes
           defined in the local database record (if any) before any
           comparison is made with data in the remote database.

## [](#CONFIGURATION)CONFIGURATION

           The Translucent Proxy overlay uses a proxied database, typically a
           (set of) remote LDAP server(s), which is configured with the
           options shown in slapd-ldap(5), slapd-meta(5) or similar.  These
           slapd.conf options are specific to the Translucent Proxy overlay;
           they must appear after the overlay directive that instantiates the
           translucent overlay.

           translucent_strict
                  By default, attempts to delete attributes in either the
                  local or remote databases will be silently ignored. The
                  translucent_strict directive causes these modifications to
                  fail with a Constraint Violation.

           translucent_no_glue
                  This configuration option disables the automatic creation
                  of "glue" records for an add or modrdn operation, such that
                  all parents of an entry added to the local database must be
                  created by hand. Glue records are always created for a
                  modify operation.

           translucent_local <attr[,attr...]>
                  Specify a list of attributes that should be searched for in
                  the local database when used in a search filter. By
                  default, search filters are only handled by the remote
                  database. With this directive, search filters will be split
                  into a local and remote portion, and local attributes will
                  be searched locally.

           translucent_remote <attr[,attr...]>
                  Specify a list of attributes that should be searched for in
                  the remote database when used in a search filter. This
                  directive complements the translucent_local directive.
                  Attributes may be specified as both local and remote if
                  desired.

           If neither translucent_local nor translucent_remote are specified,
           the default behavior is to search the remote database with the
           complete search filter. If only translucent_local is specified,
           searches will only be run on the local database. Likewise, if only
           translucent_remote is specified, searches will only be run on the
           remote database. In any case, both the local and remote entries
           corresponding to a search result will be merged before being
           returned to the client.

           translucent_bind_local
                  Enable looking for locally stored credentials for simple
                  bind when binding to the remote database fails.  Disabled
                  by default.

           translucent_pwmod_local
                  Enable RFC 3062 Password Modification extended operation on
                  locally stored credentials.  The operation only applies to
                  entries that exist in the remote database.  Disabled by
                  default.

## [](#ACCESS_CONTROL)ACCESS CONTROL

           Access control is delegated to either the remote DSA(s) or to the
           local database backend for auth and write operations.  It is
           delegated to the remote DSA(s) and to the frontend for read
           operations.  Local access rules involving data returned by the
           remote DSA(s) should be designed with care.  In fact, entries are
           returned by the remote DSA(s) only based on the remote fraction of
           the data, based on the identity the operation is performed as.  As
           a consequence, local rules might only be allowed to see a portion
           of the remote data.

## [](#CAVEATS)CAVEATS

           The Translucent Proxy overlay will disable schema checking in the
           local database, so that an entry consisting of overlay attributes
           need not adhere to the complete schema.

           Because the translucent overlay does not perform any DN rewrites,
           the local and remote database instances must have the same suffix.
           Other configurations will probably fail with No Such Object and
           other errors.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd-ldap(5).

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

    OpenLDAP LDVERSION             RELEASEDATE           SLAPO-TRANSLUCENT(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd-ldap(5)](../man5/slapd-ldap.5.html),  [slapd.overlays(5)](../man5/slapd.overlays.5.html)

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
