---
{"title": "slapo-refint(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-refint.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-refint(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-REFINT(5)            File Formats Manual            SLAPO-REFINT(5)

## [](#NAME)NAME

           slapo-refint - Referential Integrity overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The Referential Integrity overlay can be used with a backend
           database such as slapd-mdb(5) to maintain the cohesiveness of a
           schema which utilizes reference attributes.

           Integrity is maintained by updating database records which contain
           the named attributes to match the results of a modrdn or delete
           operation. For example, if the integrity attribute were configured
           as manager, deletion of the record
           "uid=robert,ou=people,dc=example,dc=com" would trigger a search
           for all other records which have a manager attribute containing
           that DN. Entries matching that search would have their manager
           attribute removed.  Or, renaming the same record into
           "uid=george,ou=people,dc=example,dc=com" would trigger a search
           for all other records which have a manager attribute containing
           that DN.  Entries matching that search would have their manager
           attribute deleted and replaced by the new DN.

           rootdn must be set for the database.  refint runs as the rootdn to
           gain access to make its updates.  rootpw is not needed.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the Referential Integrity
           overlay.  They should appear after the overlay directive.

           refint_attributes <attribute> [...]
                  Specify one or more attributes for which integrity will be
                  maintained as described above.

           refint_nothing <string>
                  Specify an arbitrary value to be used as a placeholder when
                  the last value would otherwise be deleted from an
                  attribute. This can be useful in cases where the schema
                  requires the existence of an attribute for which
                  referential integrity is enforced. The attempted deletion
                  of a required attribute will otherwise result in an Object
                  Class Violation, causing the request to fail.  The string
                  must be a valid DN.

           refint_modifiersname <DN>
                  Specify the DN to be used as the modifiersName of the
                  internal modifications performed by the overlay.  It
                  defaults to "cn=Referential Integrity Overlay".

           Modifications performed by this overlay are not propagated during
           replication. This overlay must be configured identically on
           replication consumers in order to maintain full synchronization
           with the provider.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5).

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           OpenLDAP Software is developed and maintained by The OpenLDAP
           Project <http://www.openldap.org/>.  OpenLDAP Software is derived
           from the University of Michigan LDAP 3.3 Release.

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

    OpenLDAP LDVERSION             RELEASEDATE                SLAPO-REFINT(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.overlays(5)](../man5/slapd.overlays.5.html),  [slapo-memberof(5)](../man5/slapo-memberof.5.html)

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
