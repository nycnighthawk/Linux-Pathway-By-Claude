---
{"title": "slapcat(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/slapcat.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapcat(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [LIMITATIONS](#LIMITATIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPCAT(8C)                                                   SLAPCAT(8C)

## [](#NAME)NAME

           slapcat - SLAPD database to LDIF utility

## [](#SYNOPSIS)SYNOPSIS

           SBINDIR/slapcat [-afilter] [-bsuffix] [-c] [-ddebug-level]
           [-fslapd.conf] [-Fconfdir] [-g] [-HURI] [-lldif-file] [-ndbnum]
           [-ooption[=value]] [-ssubtree-dn] [-v]

## [](#DESCRIPTION)DESCRIPTION

           Slapcat is used to generate an LDAP Directory Interchange Format
           (LDIF) output based upon the contents of a slapd(8) database.  It
           opens the given database determined by the database number or
           suffix and writes the corresponding LDIF to standard output or the
           specified file.  Databases configured as subordinate of this one
           are also output, unless -g is specified.

           The entry records are presented in database order, not superior
           first order.  The entry records will include all (user and
           operational) attributes stored in the database.  The entry records
           will not include dynamically generated attributes (such as
           subschemaSubentry).

           The output of slapcat is intended to be used as input to
           slapadd(8).  The output of slapcat cannot generally be used as
           input to ldapadd(1) or other LDAP clients without first editing
           the output.  This editing would normally include reordering the
           records into superior first order and removing no-user-
           modification operational attributes.

## [](#OPTIONS)OPTIONS

           -a filter
                  Only dump entries matching the asserted filter.  For
                  example

                  slapcat -a \
                      "(!(entryDN:dnSubtreeMatch:=ou=People,dc=example,dc=com))"

                  will dump all but the "ou=People,dc=example,dc=com" subtree
                  of the "dc=example,dc=com" database.  Deprecated; use -H
                  ldap:///???(filter) instead.

           -b suffix
                  Use the specified suffix to determine which database to
                  generate output for. By default, the first database that
                  supports the requested operation is used. The -b cannot be
                  used in conjunction with the -n option.

           -c     Enable continue (ignore errors) mode.  Multiple occurrences
                  of -c make slapcat(8) try harder.

           -d debug-level
                  Enable debugging messages as defined by the specified
                  debug-level; see slapd(8) for details.

           -f slapd.conf
                  Specify an alternative slapd.conf(5) file.

           -F confdir
                  specify a config directory.  If both -f and -F are
                  specified, the config file will be read and converted to
                  config directory format and written to the specified
                  directory.  If neither option is specified, an attempt to
                  read the default config directory will be made before
                  trying to use the default config file. If a valid config
                  directory exists then the default config file is ignored.

           -g     disable subordinate gluing.  Only the specified database
                  will be processed, and not its glued subordinates (if any).

           -H  URI
                  use dn, scope and filter from URI to only handle matching
                  entries.

           -l ldif-file
                  Write LDIF to specified file instead of standard output.

           -n dbnum
                  Generate output for the dbnum-th database listed in the
                  configuration file. The config database slapd-config(5), is
                  always the first database, so use -n 0 to select it.

                  The -n cannot be used in conjunction with the -b option.

           -o option[=value]
                  Specify an option with a(n optional) value.  Possible
                  generic options/values are:

                         syslog=<subsystems>  (see `-s' in slapd(8))
                         syslog-level=<level> (see `-S' in slapd(8))
                         syslog-user=<user>   (see `-l' in slapd(8))

                         ldif_wrap={no|<n>}

                  n is the number of columns allowed for the LDIF output
                  (n equal to 0 uses the default, corresponding to 78).
                  The minimum is 2, leaving space for one character and one
                  continuation character.
                  Use no for no wrap.

           -s subtree-dn
                  Only dump entries in the subtree specified by this DN.
                  Implies -b subtree-dn if no
                  -b
                  or
                  -n
                  option is given.
                  Deprecated; use -H ldap:///subtree-dn instead.

           -v     Enable verbose mode.

## [](#LIMITATIONS)LIMITATIONS

           For some backend types, your slapd(8) should not be running (at
           least, not in read-write mode) when you do this to ensure
           consistency of the database. It is always safe to run slapcat with
           the slapd-mdb(5), and slapd-null(5) backends.

## [](#EXAMPLES)EXAMPLES

           To make a text backup of your SLAPD database and put it in a file
           called ldif, give the command:

                SBINDIR/slapcat -l ldif

## [](#SEE_ALSO)SEE ALSO

           ldap(3), ldif(5), slapadd(8), ldapadd(1), slapd(8)

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

    OpenLDAP LDVERSION             RELEASEDATE                    SLAPCAT(8C)

------------------------------------------------------------------------

Pages that refer to this page: [ldif(5)](../man5/ldif.5.html),  [slapd.access(5)](../man5/slapd.access.5.html),  [slapd.conf(5)](../man5/slapd.conf.5.html),  [slapd-config(5)](../man5/slapd-config.5.html),  [slapd-mdb(5)](../man5/slapd-mdb.5.html),  [slapd-null(5)](../man5/slapd-null.5.html),  [slapd.plugin(5)](../man5/slapd.plugin.5.html),  [slapd-wt(5)](../man5/slapd-wt.5.html),  [slapadd(8)](../man8/slapadd.8.html),  [slapcat(8)](../man8/slapcat.8.html),  [slapd(8)](../man8/slapd.8.html),  [slapmodify(8)](../man8/slapmodify.8.html),  [slaptest(8)](../man8/slaptest.8.html)

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
