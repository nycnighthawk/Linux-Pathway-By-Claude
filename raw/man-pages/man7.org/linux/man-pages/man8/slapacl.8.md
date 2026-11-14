---
{"title": "slapacl(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/slapacl.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapacl(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPACL(8C)                                                   SLAPACL(8C)

## [](#NAME)NAME

           slapacl - Check access to a list of attributes.

## [](#SYNOPSIS)SYNOPSIS

           SBINDIR/slapacl -b DN [-d debug-level] [-D authcDN | -U authcID]
           [-f slapd.conf] [-F confdir] [-o option[=value]] [-u] [-v]
           [-X authzID | -o  authzDN=DN] [attr[/access][:value]] [...]

## [](#DESCRIPTION)DESCRIPTION

           slapacl is used to check the behavior of slapd(8) by verifying
           access to directory data according to the access control list
           directives defined in its configuration.  It opens the
           slapd.conf(5) configuration file or the slapd-config(5) backend,
           reads in the access/olcAccess directives, and then parses the attr
           list given on the command-line; if none is given, access to the
           entry pseudo-attribute is tested.

## [](#OPTIONS)OPTIONS

           -b DN  specify the DN which access is requested to; the
                  corresponding entry is fetched from the database, and thus
                  it must exist.  The DN is also used to determine what rules
                  apply; thus, it must be in the naming context of a
                  configured database. By default, the first database that
                  supports the requested operation is used.  See also -u.

           -d debug-level
                  enable debugging messages as defined by the specified
                  debug-level; see slapd(8) for details.

           -D authcDN
                  specify a DN to be used as identity through the test
                  session when selecting appropriate <by> clauses in access
                  lists.

           -f slapd.conf
                  specify an alternative slapd.conf(5) file.

           -F confdir
                  specify a config directory.  If both -f and -F are
                  specified, the config file will be read and converted to
                  config directory format and written to the specified
                  directory.  If neither option is specified, an attempt to
                  read the default config directory will be made before
                  trying to use the default config file. If a valid config
                  directory exists then the default config file is ignored.

           -o option[=value]
                  Specify an option with a(n optional) value.  Possible
                  generic options/values are:

                         syslog=<subsystems>  (see `-s' in slapd(8))
                         syslog-level=<level> (see `-S' in slapd(8))
                         syslog-user=<user>   (see `-l' in slapd(8))

                  Possible options/values specific to slapacl are:

                         authzDN
                         domain
                         peername
                         sasl_ssf
                         sockname
                         sockurl
                         ssf
                         tls_ssf
                         transport_ssf

                  See the related fields in slapd.access(5) for details.

           -u     enable dry-run mode. Do not fetch any entries from the
                  database.  In this case, a fake entry with the DN given
                  with the -b option is used, with no attributes.  As a
                  consequence, those rules that depend on the contents of the
                  target object or any other database objects will not behave
                  as with the real object.  The DN given with the -b option
                  is still used to select what rules apply; thus, it must be
                  in the naming context of a configured database.  See also
                  -b.

           -U authcID
                  specify an ID to be mapped to a DN as by means of
                  authz-regexp or authz-rewrite rules (see slapd.conf(5) for
                  details); mutually exclusive with -D.

           -v     enable verbose mode.

           -X authzID
                  specify an authorization ID to be mapped to a DN as by
                  means of authz-regexp or authz-rewrite rules (see
                  slapd.conf(5) for details); mutually exclusive with -o
                  authzDN=DN.

## [](#EXAMPLES)EXAMPLES

           The command

                SBINDIR/slapacl -f ETCDIR/slapd.conf -v \
                       -U bjorn -b "o=University of Michigan,c=US" \
                    "o/read:University of Michigan"

           tests whether the user bjorn can access the attribute o of the
           entry o=University of Michigan,c=US at read level.

## [](#SEE_ALSO)SEE ALSO

           ldap(3), slapd(8), slaptest(8), slapauth(8)

           "OpenLDAP Administrator's Guide"
           (http://www.OpenLDAP.org/doc/admin/)

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

    OpenLDAP LDVERSION             RELEASEDATE                    SLAPACL(8C)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.access(5)](../man5/slapd.access.5.html),  [slapd.conf(5)](../man5/slapd.conf.5.html),  [slapd-config(5)](../man5/slapd-config.5.html),  [slapd(8)](../man8/slapd.8.html)

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
