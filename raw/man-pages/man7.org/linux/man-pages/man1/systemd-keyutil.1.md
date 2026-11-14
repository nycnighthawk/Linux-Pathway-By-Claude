---
{"title": "systemd-keyutil(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-keyutil.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-keyutil(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-KEYUTIL(1)           systemd-keyutil           SYSTEMD-KEYUTIL(1)

## [](#NAME)NAME

           systemd-keyutil - Perform various operations on private keys and
           X.509 certificates

## [](#SYNOPSIS)SYNOPSIS

           systemd-keyutil [OPTIONS...] {COMMAND}

## [](#DESCRIPTION)DESCRIPTION

           systemd-keyutil can be used to perform various operations on
           private keys and X.509 certificates.

## [](#COMMANDS)COMMANDS

           validate
               Checks that we can load the private key and certificate
               specified with --private-key= and --certificate= respectively.

               As a side effect, if the private key is loaded from a
               PIN-protected hardware token, this command can be used to
               cache the PIN in the kernel keyring. The
               $SYSTEMD_ASK_PASSWORD_KEYRING_TIMEOUT_SEC and
               $SYSTEMD_ASK_PASSWORD_KEYRING_TYPE environment variables can
               be used to control how long and in which kernel keyring the
               PIN is cached.

               Added in version 257.

           extract-public
               This commands prints the public key in PEM format extracted
               from either the certificate given with --certificate= or the
               private key given with --private-key=.

               Added in version 257.

           extract-certificate
               This command prints the X.509 certificate in PEM format
               extracted from the certificate given with --certificate=. This
               is useful when loading a certificate from an OpenSSL provider
               (e.g. a hardware token) and wanting to output a standalone PEM
               certificate that can be used without the provider.

               Added in version 260.

           pkcs7
               This command embeds the PKCS#1 signature (RSA) provided with
               --signature= in a PKCS#7 signature using the certificate given
               with --certificate= and writes it to the file specified with
               --output= in PKCS#7 format (p7s). If --content= is provided it
               is included in the p7s, otherwise a "detached" signature is
               created. The --hash-algorithm= option, which defaults to
               "SHA256", specifies what hash algorithm was used to generate
               the signature.

               Added in version 258.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --private-key=PATH/URI, --private-key-source=TYPE[:NAME],
           --certificate=PATH, --certificate-source=TYPE[:NAME]
               Set the private key and certificate to use. The --certificate=
               option takes a path to a PEM encoded X.509 certificate or a
               URI that's passed to the OpenSSL provider configured with
               --certificate-source. The --certificate-source takes one of
               "file" or "provider", with the latter being followed by a
               specific provider identifier, separated with a colon, e.g.
               "provider:pkcs11". The --private-key= option can take a path
               or a URI that will be passed to the OpenSSL engine or
               provider, as specified by --private-key-source= as a
               "type:name" tuple, such as "engine:pkcs11".

               Added in version 257.

           --signature=PATH
               Input PKCS#1 signature for the pkcs7 command.

               Added in version 258.

           --content=PATH
               Input data that corresponds to the PKCS#1 signature for the
               pkcs7 command, used for generating inline (i.e.
               non-"detached") PKCS#7 signatures.

               Added in version 258.

           --hash-algorithm=ALGORITHM
               Hash algorithm used to generate the PKCS#1 signature for the
               pkcs7 command. This should be a valid openssl digest
               algorithm; use "openssl list -digest-algorithms" to see a list
               of valid algorithms on your system. Defaults to "SHA256".

               Added in version 258.

           --output=PATH
               Output PKCS#7 signature for the pkcs7 command.

               Added in version 258.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#SEE_ALSO)SEE ALSO

           systemd-sbsign(1), systemd-measure(1)

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                      SYSTEMD-KEYUTIL(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
