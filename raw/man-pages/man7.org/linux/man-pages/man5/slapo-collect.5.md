---
{"title": "slapo-collect(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-collect.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-collect(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-COLLECT(5)           File Formats Manual           SLAPO-COLLECT(5)

## [](#NAME)NAME

           slapo-collect - Collective attributes overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The collect overlay is used to provide a relatively coarse
           implementation of RFC 3671 collective attributes.  In X.500, a
           collective attribute is "a user attribute whose values are the
           same for each member of an entry collection".

           Collective attributes are added to entries returned by a search
           operation when the entry is within the scope of the related
           ancestor.  Collective attributes can only be modified when the
           modification affects the related ancestor.

## [](#CONFIGURATION)CONFIGURATION

           This slapd.conf option applies to the collect overlay.  It should
           appear after the overlay directive.

           collectinfo <DN> <attrlist>
                  Specify the DN of the ancestor entry and the set of related
                  collective attributes, where attrlist is a comma-separated
                  list of attributes.  The DN should be within the naming
                  context of the database.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), The slapo-collect(5) overlay
           supports dynamic configuration via back-config.

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           This module was written in 2003 by Howard Chu.  This man page was
           written in 2008 by Pierangelo Masarati.  OpenLDAP Software is
           developed and maintained by The OpenLDAP Project
           <http://www.openldap.org/>.  OpenLDAP Software is derived from the
           University of Michigan LDAP 3.3 Release.

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

    OpenLDAP LDVERSION             RELEASEDATE               SLAPO-COLLECT(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.overlays(5)](../man5/slapd.overlays.5.html),  [slapo-collect(5)](../man5/slapo-collect.5.html)

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
