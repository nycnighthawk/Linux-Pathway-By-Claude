---
{"title": "ldapexop(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ldapexop.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ldapexop(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LDAPEXOP(1)              General Commands Manual              LDAPEXOP(1)

## [](#NAME)NAME

           ldapexop - issue LDAP extended operations

## [](#SYNOPSIS)SYNOPSIS

           ldapexop [-V[V]] [-d debuglevel] [-n] [-v] [-f file] [-x]
           [-D binddn] [-W] [-w passwd] [-y passwdfile] [-H URI]
           [-e [!]ext[=extparam]] [-o opt[=optparam]] [-O security-
           properties] [-I] [-Q] [-N] [-U authcid] [-R realm] [-X authzid]
           [-Y mech] [-Z[Z]] {oid | oid:data | oid::b64data | whoami |
           cancel cancel-id | refresh DN [ttl]}

## [](#DESCRIPTION)DESCRIPTION

           ldapexop issues the LDAP extended operation specified by oid or
           one of the special keywords whoami, cancel, or refresh.

           Additional data for the extended operation can be passed to the
           server using data or base-64 encoded as b64data in the case of
           oid, or using the additional parameters in the case of the
           specially named extended operations above.

           Please note that ldapexop behaves differently for the same
           extended operation when it was given as an OID or as a specially
           named operation:

           Calling ldapexop with the OID of the whoami (RFC 4532) extended
           operation

             ldapexop [<options>] 1.3.6.1.4.1.4203.1.11.3

           yields

             # extended operation response
             data:: <base64 encoded response data>

           while calling it with the keyword whoami

             ldapexop [<options>] whoami

           results in

             dn:<client's identity>

## [](#OPTIONS)OPTIONS

           -V[V]  Print version info.  If-VV is given, only the version
                  information is printed.

           -d debuglevel
                  Set the LDAP debugging level to debuglevel.

           -n     Show what would be done but don't actually do it.  Useful
                  for debugging in conjunction with -v.

           -v     Run in verbose mode, with many diagnostics written to
                  standard output.

           -f file
                  Read operations from file.

           -x     Use simple authentication instead of SASL.

           -D binddn
                  Use the Distinguished Name binddn to bind to the LDAP
                  directory.

           -W     Prompt for simple authentication.  This is used instead of
                  specifying the password on the command line.

           -w passwd
                  Use passwd as the password for simple authentication.

           -y passwdfile
                  Use complete contents of passwdfile as the password for
                  simple authentication.

           -H URI Specify URI(s) referring to the ldap server(s); only the
                  protocol/host/port fields are allowed; a list of URI,
                  separated by whitespace or commas is expected.

           -e [!]ext[=extparam]
                  Specify general extensions.  ´!´ indicates criticality.
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
                  the ID depends on the actual SASL mechanism used.

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
                  Without this option, the program will choose the best
                  mechanism the server knows.

           -Z[Z]  Issue StartTLS (Transport Layer Security) extended
                  operation.  Giving it twice (-ZZ) will require the
                  operation to be successful.

## [](#DIAGNOSTICS)DIAGNOSTICS

           Exit status is zero if no errors occur.  Errors result in a non-
           zero exit status and a diagnostic message being written to
           standard error.

## [](#SEE_ALSO)SEE ALSO

           ldap_extended_operation_s(3)

## [](#AUTHOR)AUTHOR

           This manual page was written by Peter Marschall based on
           ldapexop's usage message and a few tests with ldapexop.  Do not
           expect it to be complete or absolutely correct.

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

                                                                  LDAPEXOP(1)

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
