---
{"title": "systemd-imdsd@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-imdsd-early-network.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-imdsd@.service(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE OPTIONS](#KERNEL_COMMAND_LINE_OPTIONS) \| [CREDENTIALS](#CREDENTIALS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-IMDSD@.SERVICE(8) systemd-imdsd@.serviceSYSTEMD-IMDSD@.SERVICE(8)

## [](#NAME)NAME

           systemd-imdsd@.service, systemd-imdsd, systemd-imdsd.socket,
           systemd-imdsd-early-network.service - Cloud IMDS (Instance
           Metadata Service) client

## [](#SYNOPSIS)SYNOPSIS

           systemd-imdsd@.service

           systemd-imdsd.socket

           systemd-imdsd-early-network.service

           /usr/lib/systemd/systemd-imdsd

## [](#DESCRIPTION)DESCRIPTION

           systemd-imdsd@.service is a system service that provides local
           access to IMDS (Instance Metadata Service; or equivalent)
           functionality, as provided by many public clouds.

           The service provides a Varlink IPC interface via
           /run/systemd/io.systemd.InstanceMetadata to query IMDS fields.

           systemd-imdsd-early-network.service is a system service that
           generates a systemd-networkd.service(8) compatible
           systemd.network(5) file for configuring the early-boot network in
           order to be able to contact the IMDS endpoint.

           The systemd-imds(1) tool may be used to query information from
           this service.

## [](#KERNEL_COMMAND_LINE_OPTIONS)KERNEL COMMAND LINE OPTIONS

           The IMDS endpoint is typically determined automatically via
           hwdb(7) records, but can also be configured explicitly via the
           kernel command line, via the following options:

           systemd.imds.network=
               Takes one of "off", "locked", "unlocked". Controls whether and
               how to set up networking for IMDS endpoint access. Unless set
               to "off" early boot networking is enabled, ensuring that the
               IMDS endpoint can be reached. If set to "locked" direct access
               to the IMDS endpoint by regular unprivileged processes is
               disabled via a "prohibit" route, so that any access must be
               done through systemd-imdsd@.service or its associated tools.
               If set to "unlocked" (the default) this "prohibit" route is
               not created, and regular unprivileged processes can directly
               contact IMDS.

               Added in version 261.

           systemd.imds.vendor=
               A short string identifying the cloud vendor.

               Example:

                   systemd.imds.vendor=foobarcloud

               Added in version 261.

           systemd.imds.token_url=
               If a bearer token must be acquired to talk to the IMDS
               service, this is the URL to acquire it from.

               Added in version 261.

           systemd.imds.refresh_header_name=
               Takes a HTTP header field name (excluding the ":") that
               declares the header field for passing the TTL value (in
               seconds) to the HTTP server when acquiring a token. Only
               applies if systemd.imds.token_url= is set too.

               Added in version 261.

           systemd.imds.data_url=
               Takes the base URL to acquire the IMDS data from (the IMDS
               "endpoint"). All data fields are acquired from below this URL.
               This URL should typically not end in "/".

               The data URLs are concatenated from this base URL, the IMDS
               "key" and the suffix configured via
               systemd.imds.data_url_suffix= below. Well-known IMDS "keys"
               can be configured via the systemd.imds.key=* options below.

               Example:

                   systemd.imds.data_url=http://169.254.169.254/metadata

               Added in version 261.

           systemd.imds.data_url_suffix=
               If specified, this field is appended to the end of the data
               URL (after appending the IMDS "key" to the data base URL), see
               above.

               Example:

                   systemd.imds.data_url_suffix=?api-version=2025-04-07&format=text

               Added in version 261.

           systemd.imds.token_header_name=
               Takes a HTTP header field name (excluding the ":") that
               declares the header field to pass the bearer token acquired
               from the token URL (see above) in. Only applies if
               systemd.imds.token_url= is set too.

               Added in version 261.

           systemd.imds.extra_header=
               Takes a full HTTP header expression (both field name and
               value, separated by a colon ":") to pass to the HTTP server
               when requesting data. May be used multiple times to set
               multiple headers.

               Example:

                   systemd.imds.extra_header=Metadata:true

               Added in version 261.

           systemd.imds.address_ipv4=
               Configures the IPv4 address the IMDS endpoint is contacted on.
               This should typically be the IP address also configured via
               systemd.imds.data_url= (if IPv4 is used) and is used to set up
               IP routing.

               Example:

                   systemd.imds.address_ipv4=169.254.169.254

               Added in version 261.

           systemd.imds.address_ipv6=
               Configures the IPv6 address the IMDS endpoint is contacted on.
               This should typically be the IP address also configured via
               systemd.imds.data_url= (if IPv6 is used) and is used to set up
               IP routing.

               Added in version 261.

           systemd.imds.key.hostname=, systemd.imds.key.region=,
           systemd.imds.key.zone=, systemd.imds.key.ipv4_public=,
           systemd.imds.key.ipv6_public=, systemd.imds.key.ssh_key=,
           systemd.imds.key.userdata=, systemd.imds.key.userdata_base=,
           systemd.imds.key.userdata_base64=
               Configures strings to concatenate to the data base URL (see
               above) to acquire data for various "well-known" fields. These
               strings must begin with a "/". They should return the relevant
               data in plain text.

               A special case are the three "userdata" keys: the option
               systemd.imds.key.userdata_base= should be used if the IMDS
               service knows a concept of multiple userdata fields, and a
               field identifier thus still needs to be appended to the
               userdata base URL. The option systemd.imds.key.userdata=
               should be used if only a single userdata field is supported.
               The option systemd.imds.key.userdata_base64= should be used in
               the same case, but only if the userdata field is encoded in
               Base64.

               Example:

                   systemd.imds.key.hostname=/instance/compute/osProfile/computerName

               Added in version 261.

## [](#CREDENTIALS)CREDENTIALS

           systemd-imdsd@.service supports the service credentials logic as
           implemented by ImportCredential=/LoadCredential=/SetCredential=
           (see systemd.exec(5) for details). The following credentials are
           used when passed in:

           imds.vendor, imds.vendor_token, imds.refresh_header_name,
           imds.data_url, imds.data_url_suffix, imds.token_header_name,
           imds.extra_header, imds.extra_header2, imds.extra_header3,
           imds.extra_header..., imds.address_ipv4, imds.address_ipv6,
           imds.key_hostname, imds.key_region, imds.key_zone,
           imds.key_ipv4_public, imds.key_ipv6_public, imds.key_ssh_key,
           imds.key_userdata, imds.key_userdata_base,
           imds.key_userdata_base64
               The various IMDS endpoint parameters. The semantics are very
               close to those configurable via kernel command line, see above
               for the matching list.

               Added in version 261.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-imds(1), systemd-imds-generator(8),
           systemd-networkd.service(8)

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

    systemd 262~devel                               SYSTEMD-IMDSD@.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-imds(1)](../man1/systemd-imds.1.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-imds-generator(8)](../man8/systemd-imds-generator.8.html)

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
