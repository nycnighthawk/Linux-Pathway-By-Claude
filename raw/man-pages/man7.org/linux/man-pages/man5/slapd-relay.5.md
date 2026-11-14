---
{"title": "slapd-relay(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-relay.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-relay(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [MASSAGING](#MASSAGING) \| [ACCESS RULES](#ACCESS_RULES) \| [SCENARIOS](#SCENARIOS) \| [EXAMPLES](#EXAMPLES) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-RELAY(5)             File Formats Manual             SLAPD-RELAY(5)

## [](#NAME)NAME

           slapd-relay - relay backend to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The primary purpose of this slapd(8) backend is to map a naming
           context defined in a database running in the same slapd(8)
           instance into a virtual naming context, with attributeType and
           objectClass manipulation, if required.  It requires the
           slapo-rwm(5) overlay.

           This backend and the above mentioned overlay are experimental.

## [](#CONFIGURATION)CONFIGURATION

           The following slapd.conf directives apply to the relay backend
           database.  That is, they must follow a "database relay" line and
           come before any subsequent "backend" or "database" lines.  Other
           database options are described in the slapd.conf(5) manual page;
           only the suffix directive is allowed by the relay backend.

           relay <real naming context>
                  The naming context of the database that is presented under
                  a virtual naming context.  The presence of this directive
                  implies that one specific database, i.e. the one serving
                  the real naming context, will be presented under a virtual
                  naming context.

## [](#MASSAGING)MASSAGING

           The relay database does not automatically rewrite the naming
           context of requests and responses.  For this purpose, the
           slapo-rwm(5) overlay must be explicitly instantiated, and
           configured as appropriate.  Usually, the rwm-suffixmassage
           directive suffices if only naming context rewriting is required.

## [](#ACCESS_RULES)ACCESS RULES

           One important issue is that access rules are based on the identity
           that issued the operation.  After massaging from the virtual to
           the real naming context, the frontend sees the operation as
           performed by the identity in the real naming context.  Moreover,
           since back-relay bypasses the real database frontend operations by
           short-circuiting operations through the internal backend API, the
           original database access rules do not apply but in selected cases,
           i.e. when the backend itself applies access control.  As a
           consequence, the instances of the relay database must provide own
           access rules that are consistent with those of the original
           database, possibly adding further specific restrictions.  So,
           access rules in the relay database must refer to identities in the
           real naming context.  Examples are reported in the EXAMPLES
           section.

## [](#SCENARIOS)SCENARIOS

           If no relay directive is given, the relay database does not refer
           to any specific database, but the most appropriate one is looked-
           up after rewriting the request DN for the operation that is being
           handled.

           This allows one to write carefully crafted rewrite rules that
           cause some of the requests to be directed to one database, and
           some to another; e.g., authentication can be mapped to one
           database, and searches to another, or different target databases
           can be selected based on the DN of the request, and so.

           Another possibility is to map the same operation to different
           databases based on details of the virtual naming context, e.g.
           groups on one database and persons on another.

## [](#EXAMPLES)EXAMPLES

           To implement a plain virtual naming context mapping that refers to
           a single database, use

             database                relay
             suffix                  "dc=virtual,dc=naming,dc=context"
             relay                   "dc=real,dc=naming,dc=context"
             overlay                 rwm
             rwm-suffixmassage       "dc=real,dc=naming,dc=context"

           To implement a plain virtual naming context mapping that looks up
           the real naming context for each operation, use

             database                relay
             suffix                  "dc=virtual,dc=naming,dc=context"
             overlay                 rwm
             rwm-suffixmassage       "dc=real,dc=naming,dc=context"

           This is useful, for instance, to relay different databases that
           share the terminal portion of the naming context (the one that is
           rewritten).

           To implement the old-fashioned suffixalias, e.g. mapping the
           virtual to the real naming context, but not the results back from
           the real to the virtual naming context, use

             database                relay
             suffix                  "dc=virtual,dc=naming,dc=context"
             relay                   "dc=real,dc=naming,dc=context"
             overlay                 rwm
             rwm-rewriteEngine       on
             rwm-rewriteContext      default
             rwm-rewriteRule         "dc=virtual,dc=naming,dc=context"
                                     "dc=real,dc=naming,dc=context" ":@"
             rwm-rewriteContext      searchFilter
             rwm-rewriteContext      searchEntryDN
             rwm-rewriteContext      searchAttrDN
             rwm-rewriteContext      matchedDN

           Note that the slapo-rwm(5) overlay is instantiated, but the
           rewrite rules are written explicitly, rather than automatically as
           with the rwm-suffixmassage statement, to map all the virtual to
           real naming context data flow, but none of the real to virtual.

           Access rules:

             database                mdb
             suffix                  "dc=example,dc=com"
             # skip...
             access to dn.subtree="dc=example,dc=com"
                     by dn.exact="cn=Supervisor,dc=example,dc=com" write
                     by * read

             database                relay
             suffix                  "o=Example,c=US"
             relay                   "dc=example,dc=com"
             overlay                 rwm
             rwm-suffixmassage       "dc=example,dc=com"
             # skip ...
             access to dn.subtree="o=Example,c=US"
                     by dn.exact="cn=Supervisor,dc=example,dc=com" write
                     by dn.exact="cn=Relay Supervisor,dc=example,dc=com" write
                     by * read

           Note that, in both databases, the identities (the <who> clause)
           are in the real naming context, i.e.  `dc=example,dc=com', while
           the targets (the <what> clause) are in the real and in the virtual
           naming context, respectively.

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The relay backend does not honor any of the access control
           semantics described in slapd.access(5); all access control is
           delegated to the relayed database(s).  Only read (=r) access to
           the entry pseudo-attribute and to the other attribute values of
           the entries returned by the search operation is honored, which is
           performed by the frontend.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapo-rwm(5), slapd(8).

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

    OpenLDAP LDVERSION             RELEASEDATE                 SLAPD-RELAY(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.backends(5)](../man5/slapd.backends.5.html),  [slapd-ldap(5)](../man5/slapd-ldap.5.html),  [slapd-meta(5)](../man5/slapd-meta.5.html),  [slapo-rwm(5)](../man5/slapo-rwm.5.html)

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
