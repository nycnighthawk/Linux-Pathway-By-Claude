---
{"title": "slapo-accesslog(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-accesslog.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-accesslog(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [EXAMPLES](#EXAMPLES) \| [SCHEMA](#SCHEMA) \| [NOTES](#NOTES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-ACCESSLOG(5)         File Formats Manual         SLAPO-ACCESSLOG(5)

## [](#NAME)NAME

           slapo-accesslog - Access Logging overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The Access Logging overlay can be used to record all accesses to a
           given backend database on another database. This allows all of the
           activity on a given database to be reviewed using arbitrary LDAP
           queries, instead of just logging to local flat text files.
           Configuration options are available for selecting a subset of
           operation types to log, and to automatically prune older log
           records from the logging database.  Log records are stored with
           audit schema (see below) to assure their readability whether
           viewed as LDIF or in raw form.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the Access Logging overlay.
           They should appear after the overlay directive.

           logdb <suffix>
                  Specify the suffix of a database to be used for storing the
                  log records.  The specified database must be defined
                  elsewhere in the configuration and must support an ordered
                  return of results such as slapd-mdb(5) The access controls
                  on the log database should prevent general access. The
                  suffix entry of the log database will be created
                  automatically by this overlay. The log entries will be
                  generated as the immediate children of the suffix entry.

           logops <operations>
                  Specify which types of operations to log. The valid
                  operation types are abandon, add, bind, compare, delete,
                  extended, modify, modrdn, search, and unbind. Aliases for
                  common sets of operations are also available:

                  writes add, delete, modify, modrdn

                  reads  compare, search

                  session
                         abandon, bind, unbind

                  all    all operations

           logbase <operations> <baseDN>
                  Specify a set of operations that will only be logged if
                  they occur under a specific subtree of the database. The
                  operation types are as above for the logops setting, and
                  delimited by a '|' character.

           logold <filter>
                  Specify a filter for matching against Deleted and Modified
                  entries. If the entry matches the filter, the old contents
                  of the entry will be logged along with the current request.

           logoldattr <attr> ...
                  Specify a list of attributes whose old contents are always
                  logged in Modify and ModRDN requests that match any of the
                  filters configured in logold.  Usually only the contents of
                  attributes that were actually modified will be logged; by
                  default no old attributes are logged for ModRDN requests.

           logpurge <age> <interval>
                  Specify the maximum age for log entries to be retained in
                  the database, and how often to scan the database for old
                  entries. Both the age and interval are specified as a time
                  span in days, hours, minutes, and seconds. The time format
                  is [ddd+]hh:mm[:ss] i.e., the days and seconds components
                  are optional but hours and minutes are required. Except for
                  days, which can be up to 5 digits, each numeric field must
                  be exactly two digits. For example
                         logpurge 2+00:00 1+00:00
                  would specify that the log database should be scanned every
                  day for old entries, and entries older than two days should
                  be deleted. When using a log database that supports ordered
                  indexing on generalizedTime attributes, specifying an eq
                  index on the reqStart attribute will greatly benefit the
                  performance of the purge operation.

           logsuccess TRUE | FALSE
                  If set to TRUE then log records will only be generated for
                  successful requests, i.e., requests that produce a result
                  code of 0 (LDAP_SUCCESS).  If FALSE, log records are
                  generated for all requests whether they succeed or not. The
                  default is FALSE.

## [](#EXAMPLES)EXAMPLES

                database mdb
                suffix dc=example,dc=com
                ...
                overlay accesslog
                logdb cn=log
                logops writes reads
                logbase search|compare ou=testing,dc=example,dc=com
                logold (objectclass=person)

                database mdb
                suffix cn=log
                ...
                index reqStart eq
                access to *
                  by dn.base="cn=admin,dc=example,dc=com" read

## [](#SCHEMA)SCHEMA

           The accesslog overlay utilizes the "audit" schema described
           herein.  This schema is specifically designed for accesslog
           auditing and is not intended to be used otherwise.  It is also
           noted that the schema described here is a work in progress, and
           hence subject to change without notice.  The schema is loaded
           automatically by the overlay.

           The schema includes a number of object classes and associated
           attribute types as described below.

           The root entry of the underlying accesslog database makes use of
           the auditContainer class which is as follows:

               (  1.3.6.1.4.1.4203.666.11.5.2.0
                   NAME 'auditContainer'
                   DESC 'AuditLog container'
                   SUP top STRUCTURAL
                   MAY ( cn $ reqStart $ reqEnd ) )

           There is a basic auditObject class from which two additional
           classes, auditReadObject and auditWriteObject are derived. Object
           classes for each type of LDAP operation are further derived from
           these classes. This object class hierarchy is designed to allow
           flexible yet efficient searches of the log based on either a
           specific operation type's class, or on more general
           classifications. The definition of the auditObject class is as
           follows:

               (  1.3.6.1.4.1.4203.666.11.5.2.1
                   NAME 'auditObject'
                   DESC 'OpenLDAP request auditing'
                   SUP top STRUCTURAL
                   MUST ( reqStart $ reqType $ reqSession )
                   MAY ( reqDN $ reqAuthzID $ reqControls $ reqRespControls $
                       reqEnd $ reqResult $ reqMessage $ reqReferral $
               reqEntryUUID ) )

           Note that all of the OIDs used in the logging schema currently
           reside under the OpenLDAP Experimental branch. It is anticipated
           that they will migrate to a Standard branch in the future.

           An overview of the attributes follows: reqStart and reqEnd provide
           the start and end time of the operation, respectively. They use
           generalizedTime syntax. The reqStart attribute is also used as the
           RDN for each log entry.

           The reqType attribute is a simple string containing the type of
           operation being logged, e.g.  add, delete, search, etc. For
           extended operations, the type also includes the OID of the
           extended operation, e.g.  extended(1.1.1.1)

           The reqSession attribute is an implementation-specific identifier
           that is common to all the operations associated with the same LDAP
           session. Currently this is slapd's internal connection ID, stored
           in decimal.

           The reqDN attribute is the distinguishedName of the target of the
           operation. E.g., for a Bind request, this is the Bind DN. For an
           Add request, this is the DN of the entry being added. For a Search
           request, this is the base DN of the search.

           The reqAuthzID attribute is the distinguishedName of the user that
           performed the operation.  This will usually be the same name as
           was established at the start of a session by a Bind request (if
           any) but may be altered in various circumstances.

           The reqControls and reqRespControls attributes carry any controls
           sent by the client on the request and returned by the server in
           the response, respectively. The attribute values are just
           uninterpreted octet strings.

           The reqResult attribute is the numeric LDAP result code of the
           operation, indicating either success or a particular LDAP error
           code. An error code may be accompanied by a text error message
           which will be recorded in the reqMessage attribute.

           The reqReferral attribute carries any referrals that were returned
           with the result of the request.

           The reqEntryUUID attribute records the entryUUID attribute of the
           entry operated on, for an Add request, this is the entryUUID of
           the newly created entry.

           Operation-specific classes are defined with additional attributes
           to carry all of the relevant parameters associated with the
           operation:

               (  1.3.6.1.4.1.4203.666.11.5.2.4
                   NAME 'auditAbandon'
                   DESC 'Abandon operation'
                   SUP auditObject STRUCTURAL
                   MUST reqId )

           For the Abandon operation the reqId attribute contains the message
           ID of the request that was abandoned.

               (  1.3.6.1.4.1.4203.666.11.5.2.5
                   NAME 'auditAdd'
                   DESC 'Add operation'
                   SUP auditWriteObject STRUCTURAL
                   MUST reqMod )

           The Add class inherits from the auditWriteObject class. The Add
           and Modify classes are very similar. The reqMod attribute carries
           all of the attributes of the original entry being added.  (Or in
           the case of a Modify operation, all of the modifications being
           performed.) The values are formatted as
                  attribute:<+|-|=|#> [ value]
           Where '+' indicates an Add of a value, '-' for Delete, '=' for
           Replace, and '#' for Increment. In an Add operation, all of the
           reqMod values will have the '+' designator.

               (  1.3.6.1.4.1.4203.666.11.5.2.6
                   NAME 'auditBind'
                   DESC 'Bind operation'
                   SUP auditObject STRUCTURAL
                   MUST ( reqVersion $ reqMethod ) )

           The Bind class includes the reqVersion attribute which contains
           the LDAP protocol version specified in the Bind as well as the
           reqMethod attribute which contains the Bind Method used in the
           Bind. This will be the string SIMPLE for LDAP Simple Binds or
           SASL(<mech>) for SASL Binds.  Note that unless configured as a
           global overlay, only Simple Binds using DNs that reside in the
           current database will be logged.

               (  1.3.6.1.4.1.4203.666.11.5.2.7
                   NAME 'auditCompare'
                   DESC 'Compare operation'
                   SUP auditObject STRUCTURAL
                   MUST reqAssertion )

           For the Compare operation the reqAssertion attribute carries the
           Attribute Value Assertion used in the compare request.

               (  1.3.6.1.4.1.4203.666.11.5.2.8
                   NAME 'auditDelete'
                   DESC 'Delete operation'
                   SUP auditWriteObject STRUCTURAL
                   MAY reqOld )

           The Delete operation needs no further parameters. However, the
           reqOld attribute may optionally be used to record the contents of
           the entry prior to its deletion. The values are formatted as
                  attribute: value
           The reqOld attribute is only populated if the entry being deleted
           matches the configured logold filter.

               (  1.3.6.1.4.1.4203.666.11.5.2.9
                   NAME 'auditModify'
                   DESC 'Modify operation'
                   SUP auditWriteObject STRUCTURAL
                   MAY ( reqOld $ reqMod ) )

           The Modify operation contains a description of modifications in
           the reqMod attribute, which was already described above in the Add
           operation. It may optionally contain the previous contents of any
           modified attributes in the reqOld attribute, using the same format
           as described above for the Delete operation.  The reqOld attribute
           is only populated if the entry being modified matches the
           configured logold filter.

               (  1.3.6.1.4.1.4203.666.11.5.2.10
                   NAME 'auditModRDN'
                   DESC 'ModRDN operation'
                   SUP auditWriteObject STRUCTURAL
                   MUST ( reqNewRDN $ reqDeleteOldRDN )
                   MAY ( reqNewSuperior $ reqMod $ reqOld ) )

           The ModRDN class uses the reqNewRDN attribute to carry the new RDN
           of the request.  The reqDeleteOldRDN attribute is a Boolean value
           showing TRUE if the old RDN was deleted from the entry, or FALSE
           if the old RDN was preserved.  The reqNewSuperior attribute
           carries the DN of the new parent entry if the request specified
           the new parent.  The reqOld attribute is only populated if the
           entry being modified matches the configured logold filter and
           contains attributes in the logoldattr list.

               (  1.3.6.1.4.1.4203.666.11.5.2.11
                   NAME 'auditSearch'
                   DESC 'Search operation'
                   SUP auditReadObject STRUCTURAL
                   MUST ( reqScope $ reqDerefAliases $ reqAttrsOnly )
                   MAY ( reqFilter $ reqAttr $ reqEntries $ reqSizeLimit $
                         reqTimeLimit ) )

           For the Search class the reqScope attribute contains the scope of
           the original search request, using the values specified for the
           LDAP URL format. I.e.  base, one, sub, or subord.  The
           reqDerefAliases attribute is one of never, finding, searching, or
           always, denoting how aliases will be processed during the search.
           The reqAttrsOnly attribute is a Boolean value showing TRUE if only
           attribute names were requested, or FALSE if attributes and their
           values were requested.  The reqFilter attribute carries the filter
           used in the search request.  The reqAttr attribute lists the
           requested attributes if specific attributes were requested.  The
           reqEntries attribute is the integer count of how many entries were
           returned by this search request.  The reqSizeLimit and
           reqTimeLimit attributes indicate what limits were requested on the
           search operation.

               (  1.3.6.1.4.1.4203.666.11.5.2.12
                   NAME 'auditExtended'
                   DESC 'Extended operation'
                   SUP auditObject STRUCTURAL
                   MAY reqData )

           The Extended class represents an LDAP Extended Operation. As noted
           above, the actual OID of the operation is included in the reqType
           attribute of the parent class. If any optional data was provided
           with the request, it will be contained in the reqData attribute as
           an uninterpreted octet string.

## [](#NOTES)NOTES

           The Access Log implemented by this overlay may be used for a
           variety of other tasks, e.g. as a ChangeLog for a replication
           mechanism, as well as for security/audit logging purposes.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5).

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           This module was written in 2005 by Howard Chu of Symas
           Corporation.

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

    OpenLDAP LDVERSION             RELEASEDATE             SLAPO-ACCESSLOG(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.conf(5)](../man5/slapd.conf.5.html),  [slapd-config(5)](../man5/slapd-config.5.html),  [slapd.overlays(5)](../man5/slapd.overlays.5.html),  [slapo-syncprov(5)](../man5/slapo-syncprov.5.html)

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
