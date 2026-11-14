---
{"title": "systemd-imds(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-imds.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-imds(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS AND COMMANDS](#OPTIONS_AND_COMMANDS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-IMDS(1)                systemd-imds               SYSTEMD-IMDS(1)

## [](#NAME)NAME

           systemd-imds, systemd-imds-import.service - Cloud IMDS (Instance
           Metadata Service) tool

## [](#SYNOPSIS)SYNOPSIS

           systemd-imds-import.service

           systemd-imds [OPTIONS...] [KEY]

## [](#DESCRIPTION)DESCRIPTION

           systemd-imds is a tool for acquiring data from IMDS (Instance
           Metadata Service), as provided in many cloud environments. It is a
           client to systemd-imdsd@.service(8), and provides access to IMDS
           data from shell environments.

           The tool can operate in one of five modes:

           •   Without positional arguments (and without the --well-known=
               switch) general IMDS service data and a few well known fields
               are displayed in human friendly form.

           •   With a positional argument (and without --well-known=) the
               IMDS data referenced by the specified key is acquired and
               written to standard output, in unprocessed form. IMDS keys are
               the part of the IMDS acquisition URL that are suffixed to the
               base URL. IMDS keys must begin with a slash ("/"). Note that
               IMDS keys are typically implementation-specific.

           •   With the --well-known= option specified (see below), the
               indicated well-known field is written to standard output, in
               unprocessed form. The concept of well-known fields abstracts
               IMDS implementation differences to some level, exposing a
               unified interface for IMDS fields that typically exist on many
               different implementations, but under implementation-specific
               keys.

           •   With the --userdata option specified (see below) the
               "userdata" provided via IMDS is written to standard output.
               Under the hood this is similar to --well-known=userdata-base,
               --well-known=userdata or --well-known=userdata-base64. Each of
               the three is tried in turn (in this order), and the first
               available is returned. For --well-known=userdata-base the
               "systemd-userdata" userdata item is requested. For
               --well-known=userdata-base64 the returned data is
               automatically Base64-decoded.

           •   With the --import option specified, various well known and
               userdata fields are imported into the local credential store,
               where they are used to configure and parameterize the system.
               For details see below.

           In addition, when invoked as a Varlink service (i.e. via socket
           activation through systemd-imds-metrics.socket), systemd-imds acts
           as an io.systemd.Metrics provider for systemd-report(1). It
           exposes the detected cloud vendor and the well-known "hostname",
           "region", "zone", "ipv4-public" and "ipv6-public" fields as
           metrics in the "io.systemd.InstanceMetadata."  namespace. The data
           is acquired on demand from systemd-imdsd@.service(8), benefiting
           from its local cache.

## [](#OPTIONS_AND_COMMANDS)OPTIONS AND COMMANDS

           --well-known=, -K
               Takes one of "hostname", "region", "zone", "ipv4-public",
               "ipv6-public", "ssh-key", "userdata", "userdata-base",
               "userdata-base64". Acquires a specific "well-known" field from
               IMDS. Many of these fields are commonly supported by various
               IMDS implementations, but typically some fields are not. Note
               that if --well-known=userdata-base is used an additional
               subkey should be specified as positional argument, which
               encodes the specific userdata item to acquire.

               Added in version 261.

           --refresh=
               Takes a time in seconds as argument, and indicates the
               required "freshness" of the data, in case cached data is used.

               Added in version 261.

           --cache=
               Takes a boolean. If set to false local caching of IMDS is
               disabled, and the data is always acquired fresh from the IMDS
               endpoint.

               Added in version 261.

           --userdata, -u
               Acquire this instance's IMDS user data, if available. See
               above for details.

               Added in version 261.

           --import
               Acquires IMDS data and writes relevant fields as credentials
               to /run/credstore/. This currently covers:

               •   If the IMDS user data is a valid JSON object containing a
                   field systemd.credentials (with a JSON array as value) it
                   is processed, importing arbitrary credentials listed in
                   the array. Each array item must have a name field
                   indicating the credential name. It may have one text, data
                   or encrypted field, containing the credential data. If
                   text is used the value shall be a literal string of the
                   credential value. If data is used the value may be
                   arbitrary binary data encoded in a Base64 string. If
                   encrypted is used the value shall be a Base64 encoded
                   encrypted credential. See systemd.system-credentials(7)
                   for information about credentials that may be imported
                   this way.

               •   If the well-known ssh-key field is available, its value
                   will be imported into the ssh.authorized_keys.root
                   credential.

               •   If the well-known hostname field is available, its value
                   will be imported into the firstboot.hostname credential.

               This command is invoked by the systemd-imds-import.service run
               at boot.

               Added in version 261.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-imdsd@.service(8), systemd-imds-generator(8),
           systemd-report(1), systemd.system-credentials(7)

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

    systemd 262~devel                                         SYSTEMD-IMDS(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-imdsd@.service(8)](../man8/systemd-imdsd@.service.8.html),  [systemd-imds-generator(8)](../man8/systemd-imds-generator.8.html)

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
