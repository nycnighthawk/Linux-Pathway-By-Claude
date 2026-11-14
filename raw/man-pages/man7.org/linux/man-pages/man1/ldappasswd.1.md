---
{"title": "ldappasswd(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ldappasswd.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ldappasswd(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LDAPPASSWD(1)            General Commands Manual            LDAPPASSWD(1)

## [](#NAME)NAME

           ldappasswd - change the password of an LDAP entry

## [](#SYNOPSIS)SYNOPSIS

           ldappasswd [-V[V]] [-d debuglevel] [-n] [-v] [-A] [-a oldPasswd]
           [-t oldpasswdfile] [-S] [-s newPasswd] [-T newpasswdfile] [-x]
           [-D binddn] [-W] [-w passwd] [-y passwdfile] [-H ldapuri]
           [-e [!]ext[=extparam]] [-E [!]ext[=extparam]] [-o opt[=optparam]]
           [-O security-properties] [-I] [-Q] [-N] [-U authcid] [-R realm]
           [-X authzid] [-Y mech] [-Z[Z]] [user]

## [](#DESCRIPTION)DESCRIPTION

           ldappasswd is a tool to set the password of an LDAP user.
           ldappasswd uses the LDAPv3 Password Modify (RFC 3062) extended
           operation.

           ldappasswd sets the password of associated with the user [or an
           optionally specified user].  If the new password is not specified
           on the command line and the user doesn't enable prompting, the
           server will be asked to generate a password for the user.

           ldappasswd is neither designed nor intended to be a replacement
           for passwd(1) and should not be installed as such.

## [](#OPTIONS)OPTIONS

           -V[V]  Print version info.  If -VV is given, only the version
                  information is printed.

           -d debuglevel
                  Set the LDAP debugging level to debuglevel.  ldappasswd
                  must be compiled with LDAP_DEBUG defined for this option to
                  have any effect.

           -n     Do not set password. (Can be useful when used in
                  conjunction with -v or -d)

           -v     Increase the verbosity of output.  Can be specified
                  multiple times.

           -A     Prompt for old password.  This is used instead of
                  specifying the password on the command line.

           -a oldPasswd
                  Set the old password to oldPasswd.

           -t oldPasswdFile
                  Set the old password to the contents of oldPasswdFile.

           -S     Prompt for new password.  This is used instead of
                  specifying the password on the command line.

           -s newPasswd
                  Set the new password to newPasswd.

           -T newPasswdFile
                  Set the new password to the contents of newPasswdFile.

           -x     Use simple authentication instead of SASL.

           -D binddn
                  Use the Distinguished Name binddn to bind to the LDAP
                  directory.  For SASL binds, the server is expected to
                  ignore this value.

           -W     Prompt for bind password.  This is used instead of
                  specifying the password on the command line.

           -w passwd
                  Use passwd as the password to bind with.

           -y passwdfile
                  Use complete contents of passwdfile as the password for
                  simple authentication.

           -H ldapuri
                  Specify URI(s) referring to the ldap server(s); only the
                  protocol/host/port fields are allowed; a list of URI,
                  separated by whitespace or commas is expected.

           -e [!]ext[=extparam]

           -E [!]ext[=extparam]

                  Specify general extensions with -e and passwd modify
                  extensions with -E.  ´!´ indicates criticality.

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

                  Passwd Modify extensions:
                    (none)

           -o opt[=optparam]]

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
                  dn:<distinguished name> or u:<username>.

           -Y mech
                  Specify the SASL mechanism to be used for authentication.
                  If it's not specified, the program will choose the best
                  mechanism the server knows.

           -Z[Z]  Issue StartTLS (Transport Layer Security) extended
                  operation. If you use -ZZ, the command will require the
                  operation to be successful

## [](#SEE_ALSO)SEE ALSO

           ldap_sasl_bind(3), ldap_extended_operation(3), ldap_start_tls_s(3)

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

    OpenLDAP LDVERSION             RELEASEDATE                  LDAPPASSWD(1)

------------------------------------------------------------------------

Pages that refer to this page: [slappw-argon2(5)](../man5/slappw-argon2.5.html),  [slappasswd(8)](../man8/slappasswd.8.html)

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
