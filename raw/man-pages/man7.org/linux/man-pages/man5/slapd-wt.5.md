---
{"title": "slapd-wt(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-wt.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-wt(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-WT(5)                File Formats Manual                SLAPD-WT(5)

## [](#NAME)NAME

           slapd-wt - WiredTiger backend to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The wt backend to slapd(8) uses WiredTiger database library to
           store data.

           The wt backend is experimental module that have potential high
           write performance and high concurrency performance.  This backend
           have not some basic feature yet. Please backup data using slapcat
           before update the module.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the wt backend database.  That
           is, they must follow a "database wt" line and come before any
           subsequent "backend" or "database" lines.  Other database options
           are described in the slapd.conf(5) manual page.

           directory <directory>
                  Specify WiredTiger home directory that containing this
                  database and associated indexes live.  A separate directory
                  must be specified for each database.  The default is
                  LOCALSTATEDIR/openldap-data.

           idlcache <boolean>
                  Use the in-memory idlcache. The default is true.

           index {<attrlist>|default} [pres,eq,approx,sub,<special>]
                  Specify the indexes to maintain for the given attribute (or
                  list of attributes).  Some attributes only support a subset
                  of indexes.  If only an <attr> is given, the indices
                  specified for default are maintained.  Note that setting a
                  default does not imply that all attributes will be indexed.
                  Also, for best performance, an eq index should always be
                  configured for the objectClass attribute.

           mode <integer>
                  back-wt does not support mode option. use umask instead.

           wtconfig {create,cache_size=512M,async=(enabled)}
                  Specify configuration for wiredtiger, This parameter is
                  pass to wiredtiger_open(3).

                  create create the database if it does not exist.

                  cache_size
                         maximum heap memory to allocate for the cache.

                  async  asynchronous operations configuration options.
                         disabled by default.

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The wt backend honors access control semantics as indicated in
           slapd.access(5).

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd(8), slapadd(8), slapcat(8),
           slapindex(8), slapmodify(8), WiredTiger documentation.

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           OpenLDAP Software is developed and maintained by The OpenLDAP
           Project <http://www.openldap.org/>.  OpenLDAP Software is derived
           from the University of Michigan LDAP 3.3 Release.  Written by
           HAMANO Tsukasa <hamano@osstech.co.jp>.

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

    OpenLDAP LDVERSION             RELEASEDATE                    SLAPD-WT(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.backends(5)](../man5/slapd.backends.5.html)

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
