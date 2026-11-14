---
{"title": "slapo-deref(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-deref.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-deref(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-DEREF(5)             File Formats Manual             SLAPO-DEREF(5)

## [](#NAME)NAME

           slapo-deref - Dereference Control overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

           ETCDIR/slapd.d

## [](#DESCRIPTION)DESCRIPTION

           This overlay implements the draft Dereference control. The overlay
           can be used with any backend or globally for all backends.

## [](#EXAMPLES)EXAMPLES

             database mdb
             ...
             overlay deref

           Given these entries:
             dn: cn=Howard Chu,ou=people,dc=example,dc=org
             objectClass: inetOrgPerson
             cn: Howard Chu
             sn: Chu
             uid: hyc

             dn: cn=Pierangelo Masarati,ou=people,dc=example,dc=org
             objectClass: inetOrgPerson
             cn: Pierangelo Masarati
             sn: Masarati
             uid: ando

             dn: cn=Test Group,ou=groups,dc=example,dc=org
             objectClass: groupOfNames
             cn: Test Group
             member: cn=Howard Chu,ou=people,dc=example,dc=org
             member: cn=Pierangelo Masarati,ou=people,dc=example,dc=org

           A search could be performed with a Dereference request control
           value specified as

             { member, uid }

           I.e.,
             ldapsearch -x -b dc=example,dc=org -E 'deref=member:uid'

           and the "cn=Test Group" entry would be returned with the response
           control value
             { { member, cn=Howard Chu,ou=people,dc=example,dc=org,
                 { { uid, [hyc] } } },
               { member, cn=Pierangelo Masarati,ou=people,dc=example,dc=org,
                 { { uid, [ando] } } } }

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

           ETCDIR/slapd.d
                  default slapd configuration directory

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5).

           "OpenLDAP Administrator's Guide"
           (http://www.OpenLDAP.org/doc/admin/)

           IETF LDAP Dereference Control proposal by P. Masarati, H. Chu, in
           IETF document "draft-masarati-ldap-deref-00.txt".

## [](#AUTHOR)AUTHOR

           Pierangelo Masarati

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

    OpenLDAP LDVERSION             RELEASEDATE                 SLAPO-DEREF(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.overlays(5)](../man5/slapd.overlays.5.html)

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
