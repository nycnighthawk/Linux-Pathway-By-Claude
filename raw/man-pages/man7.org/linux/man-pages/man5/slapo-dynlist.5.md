---
{"title": "slapo-dynlist(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-dynlist.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-dynlist(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [AUTHORIZATION](#AUTHORIZATION) \| [EXAMPLE](#EXAMPLE) \| [FILES](#FILES) \| [BACKWARD COMPATIBILITY](#BACKWARD_COMPATIBILITY) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-DYNLIST(5)           File Formats Manual           SLAPO-DYNLIST(5)

## [](#NAME)NAME

           slapo-dynlist - Dynamic List overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The dynlist overlay to slapd(8) allows expansion of dynamic lists
           and groups.  Any time an entry with a specific objectClass
           (defined in the overlay configuration) is being returned, the LDAP
           URI-valued occurrences of a specific attribute (also defined in
           the overlay configuration) are expanded into the corresponding
           entries.

           For a dynamic list, the values of the attributes listed in the URI
           are added from the matching entries to the original entry.  No
           recursion is allowed, to avoid potential infinite loops.  The
           resulting entry must comply with the LDAP data model, so
           constraints are enforced.  For example, if a SINGLE-VALUE
           attribute is listed, only the first value found during the list
           expansion appears in the final entry.

           For a dynamic group, the DNs of the matching entries are added to
           a member attribute in the original entry.

           All dynamic behavior is disabled when the manageDSAit control (RFC
           3296) is used.  In that case, the contents of the original entry
           is returned; namely, the URLs are returned instead of being
           expanded.

## [](#CONFIGURATION)CONFIGURATION

           The config directives that are specific to the dynlist overlay
           must be prefixed by dynlist-, to avoid potential conflicts with
           directives specific to the underlying database or to other stacked
           overlays.

           overlay dynlist
                  This directive adds the dynlist overlay to the current
                  database, or to the frontend, if used before any database
                  instantiation; see slapd.conf(5) for details.

           This slapd.conf configuration option is defined for the dynlist
           overlay. It may have multiple occurrences, and it must appear
           after the overlay directive.

           dynlist-attrset <group-oc> [<URI>] <URL-ad> [options]

                  The value group-oc is the name of the objectClass that
                  triggers the dynamic expansion of the data.

                  The optional URI restricts expansion only to entries
                  matching the DN, the scope and the filter portions of the
                  URI.

                  The value URL-ad is the name of the attributeDescription
                  that contains the URI that is expanded by the overlay; if
                  none is present, no expansion occurs.  If the intersection
                  of the attributes requested by the search operation (or the
                  asserted attribute for compares) and the attributes listed
                  in the URI is empty, no expansion occurs for that specific
                  URI.  It must be a subtype of labeledURI.

                  The remaining options depend on whether a dynamic list or a
                  dynamic group is being configured.

                  For a dynamic list, the allowed options have the form

                  [<mapped-ad>:<list-ad> ...]

                  The mapped-ad can be used to remap attributes obtained
                  through expansion.  The list-ad must be one of the
                  attributes returned in the expansion of the URIs in the
                  URL-ad attribute of the dynamic entry. Multiple mapping
                  statements can be used.  Note that in order for dynamic
                  lists to be usable in a search filter, the dynamic
                  attributes to be filtered must be explicitly mapped. They
                  can be mapped to themselves if no transformation is
                  required.

                  For a dynamic group, the allowed options are

                  <member-ad>[+<memberOf-ad>[@<static-oc>[*]]]

                  The member-ad is required; this attribute will list the DN
                  of the entries resulting from the internal search.  In this
                  case, the attrs portion of the URIs in the URL-ad attribute
                  must be absent, and the DNs of all the entries resulting
                  from the expansion of the URIs are listed as values of this
                  attribute.  Compares that assert the value of the member-ad
                  attribute of entries with group-oc objectClass apply as if
                  the DN of the entries resulting from the expansion of the
                  URI were present in the group-oc entry as values of the
                  member-ad attribute.  If the optional memberOf-ad attribute
                  is also specified, then it will be populated with the DNs
                  of the dynamic groups that an entry is a member of.  If the
                  optional static-oc objectClass is also specified, then the
                  memberOf attribute will also be populated with the DNs of
                  the static groups that an entry is a member of.  Note that
                  using the same static-oc objectClass in more than one
                  dynamic group configuration is not supported.  If the
                  optional * character is also specified, then the member and
                  memberOf values will be populated recursively, for nested
                  groups. Note that currently nesting is only supported for
                  Search operations, not Compares.

           dynlist-simple TRUE | FALSE
                  This option downgrades to the behavior of the OpenLDAP 2.4
                  dynlist overlay.  It disables memberOf processing, nested
                  group support, and filter evaluation of dynamically
                  generated values.  The default is FALSE.

           The dynlist overlay may be used with any backend, but it is mainly
           intended for use with local storage backends.  In case the URI
           expansion is very resource-intensive and occurs frequently with
           well-defined patterns, one should consider adding a proxycache
           later on in the overlay stack.

## [](#AUTHORIZATION)AUTHORIZATION

           By default the expansions are performed using the identity of the
           current LDAP user.  This identity may be overridden by setting the
           dgIdentity attribute in the group's entry to the DN of another
           LDAP user.  In that case the dgIdentity will be used when
           expanding the URIs in the object.  Setting the dgIdentity to a
           zero-length string will cause the expansions to be performed
           anonymously.  Note that the dgIdentity attribute is defined in the
           dyngroup schema, and this schema must be loaded before the
           dgIdentity authorization feature may be used.  If the dgAuthz
           attribute is also present in the group's entry, its values are
           used to determine what identities are authorized to use the
           dgIdentity to expand the group.  Values of the dgAuthz attribute
           must conform to the (experimental) OpenLDAP authz syntax.  When
           using dynamic memberOf in search filters, search access to the
           entryDN pseudo-attribute is required.

## [](#EXAMPLE)EXAMPLE

           This example collects all the email addresses of a database into a
           single entry; first of all, make sure that slapd.conf contains the
           directives:

               include /path/to/dyngroup.schema
               # ...

               database <database>
               # ...

               overlay dynlist
               dynlist-attrset groupOfURLs memberURL

           and that slapd loads dynlist.la, if compiled as a run-time module;
           then add to the database an entry like

               dn: cn=Dynamic List,ou=Groups,dc=example,dc=com
               objectClass: groupOfURLs
               cn: Dynamic List
               memberURL: ldap:///ou=People,dc=example,dc=com?mail?sub?(objectClass=person)

           If no <attrs> are provided in the URI, all (non-operational)
           attributes are collected.

           The values of the above list can not be evaluated in a search
           filter. To enable filter evaluation on the dynamic list, the
           configuration must be changed to explicitly map the dynamic
           attributes to be filtered. In this case mail is just mapped to
           itself.

               include /path/to/dyngroup.schema
               # ...

               database <database>
               # ...

               overlay dynlist
               dynlist-attrset groupOfURLs memberURL mail:mail

           This example implements the dynamic group feature on the member
           attribute:

               include /path/to/dyngroup.schema
               # ...

               database <database>
               # ...

               overlay dynlist
               dynlist-attrset groupOfURLs memberURL member

           A dynamic group with dgIdentity authorization could be created
           with an entry like

               dn: cn=Dynamic Group,ou=Groups,dc=example,dc=com
               objectClass: groupOfURLs
               objectClass: dgIdentityAux
               cn: Dynamic Group
               memberURL: ldap:///ou=People,dc=example,dc=com??sub?(objectClass=person)
               dgIdentity: cn=Group Proxy,ou=Services,dc=example,dc=com

           This example extends the dynamic group feature to add a dynamic
           dgMemberOf attribute to all the members of a dynamic group:

               include /path/to/dyngroup.schema
               # ...

               database <database>
               # ...

               overlay dynlist
               dynlist-attrset groupOfURLs memberURL member+dgMemberOf

           This example extends the dynamic memberOf feature to add the
           memberOf attribute to all the members of both static and dynamic
           groups:

               include /path/to/dyngroup.schema
               # ...

               database <database>
               # ...

               overlay dynlist
               dynlist-attrset groupOfURLs memberURL member+memberOf@groupOfNames

           This dynamic memberOf feature can fully replace the functionality
           of the slapo-memberof(5) overlay.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#BACKWARD_COMPATIBILITY)BACKWARD COMPATIBILITY

           The dynlist overlay has been reworked with the 2.5 release to use
           a consistent namespace as with other overlays. As a side-effect
           the following cn=config parameters are deprecated and will be
           removed in a future release: olcDlAttrSet is replaced with
           olcDynListAttrSet olcDynamicList is replaced with olcDynListConfig

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd(8).  The slapo-dynlist(5)
           overlay supports dynamic configuration via back-config.

## [](#BUGS)BUGS

           Filtering on dynamic groups may return incomplete results if the
           search operation uses the pagedResults control.

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           This module was written in 2004 by Pierangelo Masarati for SysNet
           s.n.c.

           Attribute remapping was contributed in 2008 by Emmanuel Dreyfus.

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

    OpenLDAP LDVERSION             RELEASEDATE               SLAPO-DYNLIST(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.overlays(5)](../man5/slapd.overlays.5.html),  [slapo-dynlist(5)](../man5/slapo-dynlist.5.html),  [slapo-memberof(5)](../man5/slapo-memberof.5.html),  [slapo-nestgroup(5)](../man5/slapo-nestgroup.5.html)

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
