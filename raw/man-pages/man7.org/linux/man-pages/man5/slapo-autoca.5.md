---
{"title": "slapo-autoca(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-autoca.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-autoca(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-AUTOCA(5)            File Formats Manual            SLAPO-AUTOCA(5)

## [](#NAME)NAME

           slapo-autoca - Automatic Certificate Authority overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The Automatic CA overlay generates X.509 certificate/key pairs for
           entries in the directory. The DN of a generated certificate is
           identical to the DN of the entry containing it. On startup it
           looks for a CA certificate and key in the suffix entry of the
           database which it will use to sign all subsequently generated
           certificates. A new CA certificate and key will be generated and
           stored in the suffix entry if none already exists. The CA
           certificate is stored in the cACertificate;binary attribute of the
           suffix entry, and the private key is stored in the
           cAPrivateKey;binary attribute of the suffix entry. These
           attributes may be overwritten if some other CA certificate/key
           pair is desired for use.

           Certificates for users and servers are generated on demand using a
           Search request returning only the userCertificate;binary and
           userPrivateKey;binary attributes. Any Search for anything besides
           exactly these two attributes is ignored by the overlay. Note that
           these values are stored in ASN.1 DER form in the directory so the
           ";binary" attribute option is mandatory.

           Entries that do not belong to selected objectClasses will be
           ignored by the overlay. By default, entries of objectClass person
           will be treated as users, and entries of objectClass ipHost will
           be treated as servers. There are slight differences in the set of
           X.509V3 certificate extensions added to the certificate between
           users and servers.

           The CA's private key is stored in a cAPrivateKey attribute, and
           user and server private keys are stored in the userPrivateKey
           attribute. The private key values are encoded in PKCS#8 format.
           It is essential that access to these attributes be properly
           secured with ACLs. Both of these attributes inherit from the
           pKCS8PrivateKey attribute, so it is sufficient to use a single ACL
           rule like

                   access to attrs=pKCS8PrivateKey by self ssf=128 write

           at the beginning of the rules.

           Currently there is no automated management for expiration or
           revocation.  Obsolete certificates and keys must be manually
           removed by deleting an entry's userCertificate and userPrivateKey
           attributes.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the Automatic CA overlay.  They
           should appear after the overlay directive.

           userClass <objectClass>
                  Specify the objectClass to be treated as user entries.

           serverClass <objectClass>
                  Specify the objectClass to be treated as server entries.

           userKeybits <integer>
                  Specify the size of the private key to use for user
                  certificates.  The default is 2048 and the minimum is 512.

           serverKeybits <integer>
                  Specify the size of the private key to use for server
                  certificates.  The default is 2048 and the minimum is 512.

           caKeybits <integer>
                  Specify the size of the private key to use for the CA
                  certificate.  The default is 2048 and the minimum is 512.

           userDays <integer>
                  Specify the duration for a user certificate's validity.
                  The default is 365, 1 year.

           serverDays <integer>
                  Specify the duration for a server certificate's validity.
                  The default is 1826, 5 years.

           caDays <integer>
                  Specify the duration for the CA certificate's validity.
                  The default is 3652, 10 years.

           localDN <DN>
                  Specify the DN of an entry that represents this server.
                  Requests to generate a certificate/key pair for this DN
                  will also install the certificate and key into slapd's TLS
                  settings in cn=config for immediate use.

## [](#EXAMPLES)EXAMPLES

             database mdb
             ...
             overlay autoca
             caKeybits 4096

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5).

## [](#AUTHOR)AUTHOR

           Howard Chu

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

    OpenLDAP LDVERSION             RELEASEDATE                SLAPO-AUTOCA(5)

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
