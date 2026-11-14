---
{"title": "cups-x509(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cups-x509.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cups-x509(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SUB-COMMANDS](#SUB-COMMANDS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cups-x509(1)                   OpenPrinting                  cups-x509(1)

## [](#NAME)NAME

           cups-x509 - manage x.509 certificates and certificate requests

## [](#SYNOPSIS)SYNOPSIS

           cups-x509 --help
           cups-x509 --version
           cups-x509 [ --pin ] [ --require-ca ] [ -C COUNTRY ] [ -L LOCALITY
           ] [ -O ORGANIZATION ] [ -R CSR-FILENAME ] [ -S STATE-PROVINCE ] [
           -U ORGANIZATIONAL-UNIT ] [ -a SUBJECT-ALT-NAME ] [ -d DAYS ] [ -p
           PURPOSE ] [ -r ROOT-NAME ] [ -t TYPE ] [ -u USAGE ] SUB-COMMAND
           [ARGUMENT(S)]

## [](#DESCRIPTION)DESCRIPTION

           The cups-x509 utility manages X.509 certificates and certificate
           requests, and supports client and server tests.

## [](#OPTIONS)OPTIONS

           The following options are recognized by cups-x509:

           --help
                Show program usage.

           --pin
                Pin the server's X.509 certificate found by the client
                command.

           --require-ca
                Require the server's X.509 certificate found by the client
                command to be signed by a known CA.

           --version
                Show the CUPS version.

           -C COUNTRY
                Specify the country for new X.509 certificates and
                certificate requests.

           -L LOCALITY
                Specify the locality (city, town, etc.) for new X.509
                certificates and certificate requests.

           -O ORGANIZATION
                Specify the organization name for new X.509 certificates and
                certificate requests.

           -R CSR-FILENAME
                Specify an X.509 certificate signing request in PEM format to
                be used when signing a certificate with the ca command.

           -S STATE-PROVINCE
                Specify the state/province name for new X.509 certificates
                and certificate requests.

           -U ORGANIZATIONAL-UNIT
                Specify the organizational unit name for new X.509
                certificates and certificate requests.

           -a SUBJECT-ALT-NAME
                Specify an alternate name for new X.509 certificates and
                certificate requests.

           -d DAYS
                Specify the number of days before a new X.509 certificate
                will expire.

           -p PURPOSE
                Specify the purpose of the X.509 certificate or certificate
                request as a comma-delimited list of purposes.  The supported
                purposes are "serverAuth" for TLS server authentication,
                "clientAuth" for TLS client authentication, "codeSigning" for
                executable code signing, "emailProtection" for S/MIME
                encryption and signing, "timeStamping" for secure timestamps,
                and "OCSPSigning" for Online Certificate Status Protocol
                services.

           -r ROOT-NAME
                Specify the common name of the X.509 root certificate to use.
                The default root certificate is named "_site_".

           -t TYPE
                Specify the certificate type - "rsa-2048" for 2048-bit RSA,
                "rsa-3072" for 3072-bit RSA, "rsa-4096" for 4096-bit RSA,
                "ecdsa-p256" for 256-bit ECDSA, "ecdsa-p384" for 384-bit
                ECDSA, or "ecdsa-p521" for 521-bit ECDSA.

           -u USAGE
                Specify the usage for the certificate as a comma-delimited
                list of uses.  The supported uses are "digitalSignature",
                "nonRepudiation", "keyEncipherment", "dataEncipherment",
                "keyAgreement", "keyCertSign", "cRLSign", "encipherOnly", and
                "decipherOnly".  The preset "default-ca" specifies those uses
                required for a Certificate Authority, and the preset
                "default-tls" specifies those uses required for TLS.

## [](#SUB-COMMANDS)SUB-COMMANDS

       ca COMMON-NAME
           Sign a certificate request for the specified common name.

       cacert COMMON-NAME
           Create a CA certificate for the specified common name.

       cert COMMON-NAME
           Create a certificate for the specified common name.

       client URI
           Connect to the specified URI and validate the server's
           certificate.

       csr COMMON-NAME
           Create a certificate signing request for the specified common
           name.

       install COMMON-NAME FILENAME.crt [FILENAME.key]
           Installs a certificate and optional private key for the specified
           common name.  The certificate and private key are PEM-encoded
           files.

       server COMMON-NAME[:PORT]
           Run a HTTPS test server that echos back the resource path for
           every GET request.  If PORT is not specified, uses a port number
           from 8000 to 8999.

       show COMMON-NAME
           Shows any stored credentials for the specified common name.

## [](#EXAMPLES)EXAMPLES

           Create a certificate signing request for a 384-bit ECDSA
           certificate for "server.example.com":
                cups-x509 csr -t ecdsa-p384 server.example.com
           Install the certificate you get back from the CA for
           "server.example.com":
                cups-x509 install server.example.com server.example.com.crt
           Run a test server for "server.exmaple.com" on port 8080:
                cups-x509 server SERVER-NAME:8080
           Test a HTTPS client connection to "www.example.com" with
           validation:
                cups-x509 client --require-ca https://www.example.com/

## [](#SEE_ALSO)SEE ALSO

           cups(1)

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2025 by OpenPrinting.

## [](#COLOPHON)COLOPHON

           This page is part of the CUPS (a standards-based, open source
           printing system) project.  Information about the project can be
           found at ⟨https://github.com/openprinting/cups⟩.  If you have a
           bug report for this manual page, see
           ⟨https://github.com/OpenPrinting/cups/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/openprinting/cups⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    2025-10-23                         CUPS                      cups-x509(1)

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
