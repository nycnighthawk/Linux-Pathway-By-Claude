---
{"title": "ldapdelete(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ldapdelete.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ldapdelete(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LDAPDELETE(1)            General Commands Manual            LDAPDELETE(1)

## [](#NAME)NAME

           ldapdelete - LDAP delete entry tool

## [](#SYNOPSIS)SYNOPSIS

           ldapdelete [-V[V]] [-d debuglevel] [-n] [-v] [-c] [-f file] [-r]
           [-z sizelimit] [-M[M]] [-x] [-D binddn] [-W] [-w passwd]
           [-y passwdfile] [-H ldapuri] [-P {2|3}] [-e [!]ext[=extparam]]
           [-E [!]ext[=extparam]] [-o opt[=optparam]] [-O security-
           properties] [-I] [-Q] [-N] [-U authcid] [-R realm] [-X authzid]
           [-Y mech] [-Z[Z]] [DN [...]]

## [](#DESCRIPTION)DESCRIPTION

           ldapdelete is a shell-accessible interface to the
           ldap_delete_ext(3) library call.

           ldapdelete opens a connection to an LDAP server, binds, and
           deletes one or more entries.  If one or more DN arguments are
           provided, entries with those Distinguished Names are deleted.
           Each DN should be provided using the LDAPv3 string representation
           as defined in RFC 4514.  If no DN arguments are provided, a list
           of DNs is read from standard input (or from file if the -f flag is
           used).

## [](#OPTIONS)OPTIONS

           -V[V]  Print version info.  If -VV is given, only the version
                  information is printed.

           -d debuglevel
                  Set the LDAP debugging level to debuglevel.  ldapdelete
                  must be compiled with LDAP_DEBUG defined for this option to
                  have any effect.

           -n     Show what would be done, but don't actually delete entries.
                  Useful for debugging in conjunction with -v.

           -v     Use verbose mode, with many diagnostics written to standard
                  output.

           -c     Continuous operation mode.  Errors  are  reported,  but
                  ldapdelete will  continue  with  deletions.   The default
                  is to exit after reporting an error.

           -f file
                  Read a series of DNs from file, one per line, performing an
                  LDAP delete for each.

           -r     Do a recursive delete.  If the DN specified isn't a leaf,
                  its children, and all their children are deleted down the
                  tree.  No verification is done, so if you add this switch,
                  ldapdelete will happily delete large portions of your tree.
                  Use with care.

           -z sizelimit
                  Use sizelimit when searching for children DN to delete, to
                  circumvent any server-side size limit.  Only useful in
                  conjunction with -r.

           -M[M]  Enable manage DSA IT control.  -MM makes control critical.

           -x     Use simple authentication instead of SASL.

           -D binddn
                  Use the Distinguished Name binddn to bind to the LDAP
                  directory.  For SASL binds, the server is expected to
                  ignore this value.

           -W     Prompt for simple authentication.  This is used instead of
                  specifying the password on the command line.

           -w passwd
                  Use passwd as the password for simple authentication.

           -y passwdfile
                  Use complete contents of passwdfile as the password for
                  simple authentication.

           -H ldapuri
                  Specify URI(s) referring to the ldap server(s); only the
                  protocol/host/port fields are allowed; a list of URI,
                  separated by whitespace or commas is expected.

           -P {2|3}
                  Specify the LDAP protocol version to use.

           -e [!]ext[=extparam]

           -E [!]ext[=extparam]

                  Specify general extensions with -e and delete extensions
                  with -E.  ´!´ indicates criticality.

                  General extensions:
                    [!]assert=<filter>    (an RFC 4515 Filter)
                    !authzid=<authzid>    ("dn:<dn>" or "u:<user>")
                    [!]bauthzid           (RFC 3829 authzid control)
                    [!]chaining[=<resolve>[/<cont>]]
                    [!]manageDSAit
                    [!]noop
                    ppolicy
                    [!]postread[=<attrs>] (a comma-separated attribute list)
                    [!]preread[=<attrs>]  (a comma-separated attribute list)
                    [!]relax
                    sessiontracking[=<username>]
                    abandon,cancel,ignore (SIGINT sends abandon/cancel,
                    or ignores response; if critical, doesn't wait for SIGINT.
                    not really controls)

                  Delete extensions:
                    (none)

           -o opt[=optparam]

                  Specify any ldap.conf(5) option or one of the following:
                    nettimeout=<timeout>  (in seconds, or "none" or "max")
                    ldif_wrap=<width>     (in columns, or "no" for no wrapping)

           -O security-properties
                  Specify SASL security properties.

           -I     Enable SASL Interactive mode.  Always prompt.  Default is
                  to prompt only as needed.

           -Q     Enable SASL Quiet mode.  Never prompt.

           -N     Do not use reverse DNS to canonicalize SASL host name.

           -U authcid
                  Specify the authentication ID for SASL bind. The form of
                  the identity depends on the actual SASL mechanism used.

           -R realm
                  Specify the realm of authentication ID for SASL bind. The
                  form of the realm depends on the actual SASL mechanism
                  used.

           -X authzid
                  Specify the requested authorization ID for SASL bind.
                  authzid must be one of the following formats:
                  dn:<distinguished name> or u:<username>

           -Y mech
                  Specify the SASL mechanism to be used for authentication.
                  If it's not specified, the program will choose the best
                  mechanism the server knows.

           -Z[Z]  Issue StartTLS (Transport Layer Security) extended
                  operation. If you use -ZZ, the command will require the
                  operation to be successful.

## [](#EXAMPLE)EXAMPLE

           The following command:

               ldapdelete "cn=Delete Me,dc=example,dc=com"

           will attempt to delete the entry named "cn=Delete
           Me,dc=example,dc=com".  Of course it would probably be necessary
           to supply authentication credentials.

## [](#DIAGNOSTICS)DIAGNOSTICS

           Exit status is 0 if no errors occur.  Errors result in a non-zero
           exit status and a diagnostic message being written to standard
           error.

## [](#SEE_ALSO)SEE ALSO

           ldap.conf(5), ldapadd(1), ldapmodify(1), ldapmodrdn(1),
           ldapsearch(1), ldap(3), ldap_delete_ext(3)

## [](#AUTHOR)AUTHOR

           The OpenLDAP Project <http://www.openldap.org/>

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

    OpenLDAP LDVERSION             RELEASEDATE                  LDAPDELETE(1)

------------------------------------------------------------------------

Pages that refer to this page: [ldapmodify(1)](../man1/ldapmodify.1.html),  [ldapmodrdn(1)](../man1/ldapmodrdn.1.html),  [ldapsearch(1)](../man1/ldapsearch.1.html)

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
