---
{"title": "slapo-auditlog(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-auditlog.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-auditlog(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [COMMENT FIELD INFORMATION](#COMMENT_FIELD_INFORMATION) \| [EXAMPLE](#EXAMPLE) \| [EXAMPLE CHANGELOG](#EXAMPLE_CHANGELOG) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-AUDITLOG(5)          File Formats Manual          SLAPO-AUDITLOG(5)

## [](#NAME)NAME

           slapo-auditlog - Audit Logging overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

           ETCDIR/slapd.d

## [](#DESCRIPTION)DESCRIPTION

           The Audit Logging overlay can be used to record all changes on a
           given backend database to a specified log file. Changes are logged
           as standard LDIF, with an additional comment header providing six
           fields of information about the change. A second comment header is
           added at the end of the operation to note the termination of the
           change.

           For Add and Modify operations the identity comes from the
           modifiersName associated with the operation. This is usually the
           same as the requestor's identity, but may be set by other overlays
           to reflect other values.

## [](#CONFIGURATION)CONFIGURATION

           Both slapd.conf and back-config style configuration are supported.

           overlay auditlog
                  This directive loads the auditlog overlay.

           auditlog <filename>

           olcAuditlogFile: <filename>
                  Specify the fully qualified path for the log file.

           auditlognonblocking {on|off}

           olcAuditlogNonBlocking: {on|off}
                  Open <filename> in non-blocking mode.  Useful if <filename>
                  is a named pipe and slapd should not block if no reader is
                  available.

## [](#COMMENT_FIELD_INFORMATION)COMMENT FIELD INFORMATION

           The first field is the operation type.
           The second field is the timestamp of the operation in seconds
           since epoch.
           The third field is the suffix of the database.
           The fourth field is the recorded modifiersName.
           The fifth field is the originating IP address and port.
           The sixth field is the connection number. A connection number of
           -1 indicates an internal slapd operation.

## [](#EXAMPLE)EXAMPLE

           The following LDIF could be used to add this overlay to cn=config
           (adjust to suit)

                  dn: olcOverlay=auditlog,olcDatabase={1}mdb,cn=config
                  changetype: add
                  objectClass: olcOverlayConfig
                  objectClass: olcAuditLogConfig
                  olcOverlay: auditlog
                  olcAuditlogFile: /tmp/auditlog.ldif

## [](#EXAMPLE_CHANGELOG)EXAMPLE CHANGELOG

                  # modify 1614223245 dc=example,dc=com cn=admin,dc=example,dc=com IP=[::1]:47270 conn=1002
                  dn: uid=joepublic,ou=people,dc=example,dc=com
                  changetype: modify
                  replace: displayName
                  displayName: Joe Public
                  -
                  replace: entryCSN
                  entryCSN: 20210225032045.045229Z#000000#001#000000
                  -
                  replace: modifiersName
                  modifiersName: cn=admin,dc=example,dc=com
                  -
                  replace: modifyTimestamp
                  modifyTimestamp: 20210225032045Z
                  -
                  # end modify 1614223245

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

           ETCDIR/slapd.d
                  default slapd configuration directory

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5).

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

    OpenLDAP LDVERSION             RELEASEDATE              SLAPO-AUDITLOG(5)

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
