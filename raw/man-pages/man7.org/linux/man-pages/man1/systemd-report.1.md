---
{"title": "systemd-report(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-report.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-report(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-REPORT(1)             systemd-report            SYSTEMD-REPORT(1)

## [](#NAME)NAME

           systemd-report - Generate report of system metrics

## [](#SYNOPSIS)SYNOPSIS

           systemd-report [OPTIONS...]

## [](#DESCRIPTION)DESCRIPTION

           Note: this command is experimental for now. While it is likely to
           become a regular component of systemd, it might still change in
           behaviour and interface.

           systemd-report requests metrics from the system and writes them to
           standard output.

## [](#COMMANDS)COMMANDS

           The following commands are understood:

           metrics [MATCH...]
               Acquire a list of metrics values from all local services
               providing them, and write them to standard output. Optionally
               takes one or more match expressions for filtering the metrics
               to show. The expression either may be a literal metric family
               name to search for, or a prefix of one (which will be matched
               only at dot boundaries). If multiple matches are specified as
               multiple parameters, any metric matching any of the specified
               matches are shown.

               Added in version 260.

           describe [MATCH...]
               Acquire a list of metric families from all local services
               providing them, and write them to standard output. This
               returns primarily static information about metrics, their data
               types and human readable description, without values.

               Match expressions supported by metrics are supported by
               describe too.

               Added in version 260.

           generate [MATCH...]
               Acquire a list of metrics and build a JSON report.

               Match expressions supported by metrics are supported here too.

               Added in version 261.

           upload [MATCH...]
               This command can be used to send the report built by generate
               to an external server. Two upload mechanisms are supported. If
               an "http://" or "https://" URL is specified with --url=, an
               HTTP upload will be performed to the specified location.
               Otherwise, any sockets under /run/systemd/report.upload/ will
               be used to call io.systemd.Report.Uploader.Upload().

               Match expressions supported by metrics are supported here too.

               Added in version 261.

           list-sources
               Show list of known metrics sources.

               Added in version 260.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --system, --user
               Query per-system metrics sources (the default), or the
               per-user metrics sources.

               Added in version 260.

           --no-pager
               Do not pipe output into a pager.

           --json=MODE
               Shows output formatted as JSON. Expects one of "short" (for
               the shortest possible output without any redundant whitespace
               or line breaks), "pretty" (for a pretty version of the same,
               with indentation and line breaks) or "off" (to turn off JSON
               output, the default).

           -j
               Equivalent to --json=pretty if running on a terminal, and
               --json=short otherwise.

           --no-legend
               Do not print the legend, i.e. column headers and the footer
               with hints.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

           --url=URL
               Upload the collected report to the specified address instead
               of writing it to standard output.  URL must point to a server
               accepting POST requests with a JSON-formatted report body.

               Note: both "http://" and "https://" URLs are supported, but
               connections over plain HTTP are made without encryption. Thus,
               this mode should only be used in specific situations where
               integrity and confidentiality of the report is not required or
               is ensured through some other means. Using "https://" is
               recommended.

               Added in version 261.

           --key=FILENAME
               Takes a path to a SSL key file in PEM format, used for client
               certificate authentication when uploading. Can also be set to
               "-", to disable client certificate authentication. Defaults to
               /etc/ssl/private/systemd-report.pem.

               Added in version 261.

           --cert=FILENAME
               Takes a path to a SSL certificate file in PEM format, used for
               client certificate authentication when uploading. Defaults to
               /etc/ssl/certs/systemd-report.pem.

               Added in version 261.

           --trust=FILENAME|all
               Takes a path to a SSL CA certificate file in PEM format used
               to verify the server certificate, or the literal string all to
               disable certificate checking entirely. Defaults to
               /etc/ssl/ca/trusted.pem.

               Added in version 261.

           --network-timeout=SEC
               Timeout for the network upload operation. Takes a value in
               seconds (or in other time units if suffixed with "ms", "min",
               "h", etc.); see systemd.time(7) for details. Defaults to 30
               seconds.

               Added in version 261.

           --extra-header=NAME: VALUE
               Inject an additional HTTP header into the upload request. May
               be specified multiple times to add several headers. Passing an
               empty string clears any headers added by previous
               --extra-header= uses.

               Added in version 261.

           --sign=MODE
               Controls whether and how the report generated by generate or
               uploaded by upload is cryptographically signed. Signatures are
               acquired by calling io.systemd.Report.Signer.Sign() on each
               socket found under /run/systemd/report.sign/.

               When signing is requested (any value other than no) the report
               is emitted as a JSON-SEQ stream: the report object comes
               first, followed by one signature object per acquired signature
               (possibly none, in best-effort mode), each covering the
               precise binary representation of the report object. With no
               the report is emitted as a single plain JSON object. Takes one
               of the following values:

               no
                   Do not sign the report; it is emitted as a single plain
                   JSON object. This is the default.

                   Added in version 262.

               best-effort
                   Never fail because of signing. Any acquired signatures are
                   included. The operation succeeds even if none could be
                   acquired, in which case the JSON-SEQ stream simply
                   contains no signature objects.

                   Added in version 262.

               require-one
                   Require at least one signature. Individual signers that
                   fail or return no signature are tolerated, but the
                   operation fails if not a single signature could be
                   acquired.

                   Added in version 262.

               require-all
                   Require every signer to succeed with at least one
                   signature. The operation fails if no signer is present, if
                   any signer returns an error, or if any signer returns no
                   signature.

                   Added in version 262.

               Defaults to no.

               Added in version 262.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1)

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

    systemd 262~devel                                       SYSTEMD-REPORT(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-imds(1)](../man1/systemd-imds.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-report-files@.service(8)](../man8/systemd-report-files@.service.8.html),  [systemd-report-sign-plain@.service(8)](../man8/systemd-report-sign-plain@.service.8.html),  [systemd-report-sign-tsm@.service(8)](../man8/systemd-report-sign-tsm@.service.8.html)

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
