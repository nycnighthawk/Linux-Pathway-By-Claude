---
{"title": "slapo-memberof(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-memberof.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-memberof(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [BACKWARD COMPATIBILITY](#BACKWARD_COMPATIBILITY) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-MEMBEROF(5)          File Formats Manual          SLAPO-MEMBEROF(5)

## [](#NAME)NAME

           slapo-memberof - Reverse Group Membership overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The memberof overlay to slapd(8) allows automatic reverse group
           membership maintenance.  Any time a group entry is modified, its
           members are modified as appropriate in order to keep a DN-valued
           "is member of" attribute updated with the DN of the group.

           Note that the dynlist overlay can also provide this functionality
           and may be suitable for less demanding environments.

## [](#CONFIGURATION)CONFIGURATION

           The config directives that are specific to the memberof overlay
           must be prefixed by memberof-, to avoid potential conflicts with
           directives specific to the underlying database or to other stacked
           overlays.

           overlay memberof
                  This directive adds the memberof overlay to the current
                  database; see slapd.conf(5) for details.

           The following slapd.conf configuration options are defined for the
           memberof overlay.

           memberof-group-oc <group-oc>
                  The value <group-oc> is the name of the objectClass that
                  triggers the reverse group membership update.  It defaults
                  to groupOfNames.

           memberof-member-ad <member-ad>
                  The value <member-ad> is the name of the attribute that
                  contains the names of the members in the group objects; it
                  must be DN-valued.  It defaults to member.

           memberof-memberof-ad <memberof-ad>
                  The value <memberof-ad> is the name of the attribute that
                  contains the names of the groups an entry is member of; it
                  must be DN-valued.  Its contents are automatically updated
                  by the overlay.  It defaults to memberOf.

           memberof-dn <dn>
                  The value <dn> contains the DN that is used as
                  modifiersName for internal modifications performed to
                  update the reverse group membership.  It defaults to the
                  rootdn of the underlying database.

           memberof-dangling {ignore, drop, error}
                  This option determines the behavior of the overlay when,
                  during a modification, it encounters dangling references.
                  The default is ignore, which may leave dangling references.
                  Other options are drop, which discards those modifications
                  that would result in dangling references, and error, which
                  causes modifications that would result in dangling
                  references to fail.

           memberof-dangling-error <error-code>
                  If memberof-dangling is set to error, this configuration
                  parameter can be used to modify the response code returned
                  in case of violation.  It defaults to "constraint
                  violation", but other implementations are known to return
                  "no such object" instead.

           memberof-refint {true|FALSE}
                  This option determines whether the overlay will try to
                  preserve referential integrity or not.  If set to TRUE,
                  when an entry containing values of the "is member of"
                  attribute is modified, the corresponding groups are
                  modified as well. Note that while this overlay handles
                  renames of individual groups and members, it doesn't handle
                  changes due to subtree renames. For referential integrity
                  on subtree renames the slapo-refint(5) overlay should also
                  be used.

           memberof-addcheck {true|FALSE}
                  This option determines whether the overlay will check newly
                  added entries for membership in any existing groups. This
                  check is useful if populated groups are created in the
                  directory before the entries they reference. The situation
                  often occurs during replication, which may replicate
                  entries in random order.  If set to TRUE, every Add
                  operation will search for groups referencing the added
                  entry and populate its memberof attribute with the group
                  DNs. Note that memberof-dangling must be left on its
                  default setting of ignore for this option to work.

           The memberof overlay may be used with any backend that provides
           full read-write functionality, but it is mainly intended for use
           with local storage backends. The maintenance operations it
           performs are internal to the server on which the overlay is
           configured and are never replicated. Consumer servers should be
           configured with their own instances of the memberOf overlay if it
           is desired to maintain these memberOf attributes on the consumers.
           Consumers must also be configured to exclude the memberof
           attribute from replication.  (See the exattrs option in the
           consumer configuration.)

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#BACKWARD_COMPATIBILITY)BACKWARD COMPATIBILITY

           The memberof overlay has been reworked with the 2.5 release to use
           a consistent namespace as with other overlays. As a side-effect
           the following cn=config parameters are deprecated and will be
           removed in a future release: olcMemberOf is replaced with
           olcMemberOfConfig

## [](#SEE_ALSO)SEE ALSO

           slapo-dynlist(5), slapo-refint(5), slapd.conf(5), slapd-config(5),
           slapd(8).  The slapo-memberof(5) overlay supports dynamic
           configuration via back-config.

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           This module was written in 2005 by Pierangelo Masarati for SysNet
           s.n.c.

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

    OpenLDAP LDVERSION             RELEASEDATE              SLAPO-MEMBEROF(5)

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
