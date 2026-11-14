---
{"title": "slappasswd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/slappasswd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slappasswd(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [LIMITATIONS](#LIMITATIONS) \| [SECURITY CONSIDERATIONS](#SECURITY_CONSIDERATIONS) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPPASSWD(8C)                                             SLAPPASSWD(8C)

## [](#NAME)NAME

           slappasswd - OpenLDAP password utility

## [](#SYNOPSIS)SYNOPSIS

           SBINDIR/slappasswd [-v] [-u] [-g|-s secret|-T file] [-h hash]
           [-c salt-format] [-n] [-o option[=value]]

## [](#DESCRIPTION)DESCRIPTION

           Slappasswd is used to generate an userPassword value suitable for
           use with ldapmodify(1), slapd.conf(5) rootpw configuration
           directive or the slapd-config(5) olcRootPW configuration
           directive.

## [](#OPTIONS)OPTIONS

           -v     enable verbose mode.

           -u     Generate RFC 2307 userPassword values (the default).
                  Future versions of this program may generate alternative
                  syntaxes by default.  This option is provided for forward
                  compatibility.

           -s secret
                  The secret to hash.  If this, -g and -T are absent, the
                  user will be prompted for the secret to hash.  -s, -g and
                  -T are mutually exclusive flags.

           -g     Generate the secret.  If this, -s and -T are absent, the
                  user will be prompted for the secret to hash.  -s, -g and
                  -T are mutually exclusive flags.  If this is present,
                  {CLEARTEXT} is used as scheme.  -g and -h are mutually
                  exclusive flags.

           -T "file"
                  Hash the contents of the file.  If this, -g and -s are
                  absent, the user will be prompted for the secret to hash.
                  -s, -g and -T and mutually exclusive flags.

           -h "scheme"
                  If -h is specified, one of the following RFC 2307 schemes
                  may be specified: {CRYPT}, {MD5}, {SMD5}, {SSHA}, and
                  {SHA}.  The default is {SSHA}.

                  Note that scheme names may need to be protected, due to {
                  and }, from expansion by the user's command interpreter.

                  {SHA} and {SSHA} use the SHA-1 algorithm (FIPS 160-1), the
                  latter with a seed.

                  {MD5} and {SMD5} use the MD5 algorithm (RFC 1321), the
                  latter with a seed.

                  {CRYPT} uses the crypt(3).

                  {CLEARTEXT} indicates that the new password should be added
                  to userPassword as clear text.  Unless {CLEARTEXT} is used,
                  this flag is incompatible with option -g.

           -c crypt-salt-format
                  Specify the format of the salt passed to crypt(3) when
                  generating {CRYPT} passwords.  This string needs to be in
                  sprintf(3) format and may include one (and only one) %s
                  conversion.  This conversion will be substituted with a
                  string of random characters from [A-Za-z0-9./].  For
                  example, '%.2s' provides a two character salt and '$1$%.8s'
                  tells some versions of crypt(3) to use an MD5 algorithm and
                  provides 8 random characters of salt.  The default is '%s',
                  which provides 31 characters of salt.

           -n     Omit the trailing newline; useful to pipe the credentials
                  into a command.

           -o option[=value]
                  Specify an option with a(n optional) value.  Possible
                  generic options/values are:

                         module-path=<pathspec> (see `modulepath' in slapd.conf(5))
                         module-load="<filename> [<arguments>...]" (see `moduleload' in slapd.conf(5))

                  You can load a dynamically loadable password hash module by
                  using this option.

## [](#LIMITATIONS)LIMITATIONS

           The practice of storing hashed passwords in userPassword violates
           Standard Track (RFC 4519) schema specifications and may hinder
           interoperability.  A new attribute type, authPassword, to hold
           hashed passwords has been defined (RFC 3112), but is not yet
           implemented in slapd(8).

           It should also be noted that the behavior of crypt(3) is platform
           specific.

## [](#SECURITY_CONSIDERATIONS)SECURITY CONSIDERATIONS

           Use of hashed passwords does not protect passwords during protocol
           transfer.  TLS or other eavesdropping protections should be in-
           place before using LDAP simple bind.

           The hashed password values should be protected as if they were
           clear text passwords.

## [](#SEE_ALSO)SEE ALSO

           ldappasswd(1), ldapmodify(1), slapd(8), slapd.conf(5),
           slapd-config(5), RFC 2307, RFC 4519, RFC 3112

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

    OpenLDAP LDVERSION             RELEASEDATE                 SLAPPASSWD(8C)

------------------------------------------------------------------------

Pages that refer to this page: [ldapcompare(1)](../man1/ldapcompare.1.html),  [slapd.conf(5)](../man5/slapd.conf.5.html),  [slapd-config(5)](../man5/slapd-config.5.html),  [slappw-argon2(5)](../man5/slappw-argon2.5.html),  [slapd(8)](../man8/slapd.8.html)

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
