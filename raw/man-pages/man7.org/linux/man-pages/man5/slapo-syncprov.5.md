---
{"title": "slapo-syncprov(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-syncprov.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-syncprov(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-SYNCPROV(5)          File Formats Manual          SLAPO-SYNCPROV(5)

## [](#NAME)NAME

           slapo-syncprov - Sync Provider overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The Sync Provider overlay implements the provider-side support for
           the LDAP Content Synchronization (RFC4533) as well as syncrepl
           replication support.  The overlay can be used with any backend
           that maintains entryCSN and entryUUID attributes for its entries.
           It also creates a contextCSN attribute in the root entry of the
           database.

           The contextCSN is updated for every write operation performed
           against the database. To reduce database contention, the
           contextCSN is only updated in memory. The value is written to the
           database on server shutdown and read into memory on startup, and
           maintained in memory thereafter. Checkpoints may be configured to
           write the contextCSN into the underlying database to minimize
           recovery time after an unclean shutdown.

           On databases that support inequality indexing, it is highly
           recommended to set an eq index on the entryCSN attribute when
           using this overlay.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the Sync Provider overlay.  They
           should appear after the overlay directive.

           syncprov-checkpoint <ops> <minutes>
                  After a write operation has succeeded, write the contextCSN
                  to the underlying database if <ops> write operations or
                  more than <minutes> time have passed since the last
                  checkpoint. Checkpointing is disabled by default.

           syncprov-sessionlog <ops>
                  Configures an in-memory session log for recording
                  information about write operations made on the database.
                  The <ops> specifies the number of operations that are
                  recorded in the log. All write operations (except Adds) are
                  recorded in the log.  When using the session log, it is
                  helpful to set an eq index on the entryUUID attribute in
                  the underlying database.

           syncprov-sessionlog-source <dn>
                  Should not be set when syncprov-sessionlog is set and vice
                  versa.

                  When accesslog for this database is configured and is
                  logging at this suffix, it can be used as the session log
                  source instead of the in-memory session log mentioned
                  above. This log has the advantage of not starting afresh
                  every time the server is restarted.

           syncprov-nopresent TRUE | FALSE
                  Specify that the Present phase of refreshing should be
                  skipped. This value should only be set TRUE for a syncprov
                  instance on top of a log database (such as one managed by
                  the accesslog overlay).  The default is FALSE.

           syncprov-reloadhint TRUE | FALSE
                  Specify that the overlay should honor the reloadHint flag
                  in the Sync Control. It must be set TRUE when using the
                  accesslog overlay for delta-based syncrepl replication
                  support.  The default is FALSE.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapo-accesslog(5).  OpenLDAP
           Administrator's Guide.

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

    OpenLDAP LDVERSION             RELEASEDATE              SLAPO-SYNCPROV(5)

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
