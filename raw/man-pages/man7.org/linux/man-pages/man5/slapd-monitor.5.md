---
{"title": "slapd-monitor(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-monitor.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-monitor(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [USAGE](#USAGE) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [KNOWN LIMITATIONS](#KNOWN_LIMITATIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-MONITOR(5)           File Formats Manual           SLAPD-MONITOR(5)

## [](#NAME)NAME

           slapd-monitor - Monitor backend to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The monitor backend to slapd(8) is not an actual database; if
           enabled, it is automatically generated and dynamically maintained
           by slapd with information about the running status of the daemon.

           To inspect all monitor information, issue a subtree search with
           base cn=Monitor, requesting that attributes "+" and "*" are
           returned.  The monitor backend produces mostly operational
           attributes, and LDAP only returns operational attributes that are
           explicitly requested.  Requesting attribute "+" is an extension
           which requests all operational attributes.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the monitor backend database.
           That is, they must follow a "database monitor" line and come
           before any subsequent "backend" or "database" lines.

           As opposed to most databases, the monitor database can be
           instantiated only once, i.e. only one occurrence of "database
           monitor" can occur in the slapd.conf(5) file.  Moreover, the
           suffix of the database cannot be explicitly set by means of the
           suffix directive.  The suffix is automatically set to
           "cn=Monitor".

           The monitor database honors the rootdn and the rootpw directives,
           and the usual ACL directives, e.g. the access directive.

           Other database options are described in the slapd.conf(5) manual
           page.

## [](#USAGE)USAGE

           The usage is:

           1) enable the monitor backend at configure:

                  configure --enable-monitor

           2) activate the monitor database in the slapd.conf(5) file:

                  database monitor

           3) add ACLs as detailed in slapd.access(5) to control access to
           the database, e.g.:

                  access to dn.subtree="cn=Monitor"
                       by dn.exact="uid=Admin,dc=my,dc=org" write
                       by users read
                       by * none

           4) ensure that the core.schema file is loaded.
                  The monitor backend relies on some standard track
                  attributeTypes that must be already defined when the
                  backend is started.

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The monitor backend honors access control semantics as indicated
           in slapd.access(5), including the disclose access privilege, on
           all currently implemented operations.

## [](#KNOWN_LIMITATIONS)KNOWN LIMITATIONS

           The monitor backend does not honor size/time limits in search
           operations.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd.access(5), slapd(8),
           ldap(3).

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

    OpenLDAP LDVERSION             RELEASEDATE               SLAPD-MONITOR(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.backends(5)](../man5/slapd.backends.5.html),  [lloadd(8)](../man8/lloadd.8.html)

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
