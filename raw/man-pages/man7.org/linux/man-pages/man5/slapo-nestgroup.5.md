---
{"title": "slapo-nestgroup(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-nestgroup.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-nestgroup(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-NESTGROUP(5)         File Formats Manual         SLAPO-NESTGROUP(5)

## [](#NAME)NAME

           slapo-nestgroup - Nested Group overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The nestgroup overlay to slapd(8) supports evaluation of nested
           groups in Search operations. Support consists of four possible
           features: inclusion of parent groups when searching with (member=)
           filters, inclusion of child groups when searching with (memberOf=)
           filters, expansion of child groups when returning member
           attributes, and expansion of parent groups when returning memberOf
           attributes. Each of these features may be enabled independently.
           By default, no features are enabled, so this overlay does nothing
           unless explicitly enabled.

## [](#CONFIGURATION)CONFIGURATION

           The config directives that are specific to the nestgroup overlay
           must be prefixed by nestgroup-, to avoid potential conflicts with
           directives specific to the underlying database or to other stacked
           overlays.

           overlay nestgroup
                  This directive adds the nestgroup overlay to the current
                  database; see slapd.conf(5) for details.

           The following slapd.conf configuration options are defined for the
           nestgroup overlay.

           nestgroup-member <member-ad>
                  The value <member-ad> is the name of the attribute that
                  contains the names of the members in the group objects; it
                  must be DN-valued.  It defaults to member.

           nestgroup-memberof <memberof-ad>
                  The value <memberof-ad> is the name of the attribute that
                  contains the names of the groups an entry is member of; it
                  must be DN-valued.  It defaults to memberOf.

           nestgroup-base <dn>
                  The value <dn> specifies a subtree that contains group
                  entries in the DIT. This may be specified multiple times
                  for multiple distinct subtrees.  It has no default and the
                  overlay does no processing unless it is explicitly
                  configured.

           nestgroup-flags {member-filter, memberof-filter, member-values,
           memberof-values}
                  This option specifies which features to enable in the
                  overlay.  By default, nothing is enabled and the overlay is
                  a no-op.

           The nestgroup overlay may be used with any backend that provides
           standard search functionality.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapo-dynlist(5), slapo-memberof(5), slapd.conf(5),
           slapd-config(5), slapd(8).  The slapo-nestgroup(5) overlay
           supports dynamic configuration via back-config.

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           This module was written in 2024 by Howard Chu of Symas
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

    OpenLDAP LDVERSION             RELEASEDATE             SLAPO-NESTGROUP(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapo-nestgroup(5)](../man5/slapo-nestgroup.5.html)

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
