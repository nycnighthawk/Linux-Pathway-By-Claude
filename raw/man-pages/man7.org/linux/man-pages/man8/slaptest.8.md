---
{"title": "slaptest(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/slaptest.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slaptest(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPTEST(8C)                                                 SLAPTEST(8C)

## [](#NAME)NAME

           slaptest - Check the suitability of the OpenLDAP slapd
           configuration

## [](#SYNOPSIS)SYNOPSIS

           SBINDIR/slaptest [-d debug-level] [-f slapd.conf] [-F confdir]
           [-ndbnum] [-o option[=value]] [-Q] [-u] [-v]

## [](#DESCRIPTION)DESCRIPTION

           Slaptest is used to check the conformance of the slapd(8)
           configuration.  It opens the slapd.conf(5) configuration file or
           the slapd-config(5) backend, and parses it according to the
           general and the backend-specific rules, checking its sanity.

## [](#OPTIONS)OPTIONS

           -d debug-level
                  enable debugging messages as defined by the specified
                  debug-level; see slapd(8) for details.

           -f slapd.conf
                  specify an alternative slapd.conf(5) file.

           -F confdir
                  specify a config directory.  If both -f and -F are
                  specified, the config file will be read and converted to
                  config directory format and written to the specified
                  directory.  If neither option is specified, slaptest will
                  attempt to read the default config directory before trying
                  to use the default config file. If a valid config directory
                  exists then the default config file is ignored. If dry-run
                  mode is also specified, no conversion will occur. Note:
                  this conversion may fail if used on a fresh config where
                  the configured backends haven't been created yet. In that
                  case, use slapcat(8) to do the conversion instead.

           -n dbnum
                  Just open and test the dbnum-th database listed in the
                  configuration file.  To only test the config database
                  slapd-config(5), use -n 0 as it is always the first
                  database.

           -o option[=value]
                  Specify an option with a(n optional) value.  Possible
                  generic options/values are:

                         syslog=<subsystems>  (see `-s' in slapd(8))
                         syslog-level=<level> (see `-S' in slapd(8))
                         syslog-user=<user>   (see `-l' in slapd(8))

           -Q     Be extremely quiet: only the exit code indicates success
                  (0) or not (any other value).

           -u     enable dry-run mode (i.e. don't fail if databases cannot be
                  opened, but config is fine).

           -v     enable verbose mode.

## [](#EXAMPLES)EXAMPLES

           To check a slapd.conf(5) give the command:

                SBINDIR/slaptest -f /ETCDIR/slapd.conf -v

## [](#SEE_ALSO)SEE ALSO

           ldap(3), slapd(8), slapdn(8)

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

    OpenLDAP LDVERSION             RELEASEDATE                   SLAPTEST(8C)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.access(5)](../man5/slapd.access.5.html),  [slapd.conf(5)](../man5/slapd.conf.5.html),  [slapd-config(5)](../man5/slapd-config.5.html),  [slapacl(8)](../man8/slapacl.8.html),  [slapauth(8)](../man8/slapauth.8.html),  [slapd(8)](../man8/slapd.8.html),  [slapdn(8)](../man8/slapdn.8.html)

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
