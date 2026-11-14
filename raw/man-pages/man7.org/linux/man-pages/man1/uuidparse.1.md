---
{"title": "uuidparse(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/uuidparse.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uuidparse(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OUTPUT](#OUTPUT) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UUIDPARSE(1)                  User Commands                  UUIDPARSE(1)

## [](#NAME)NAME

           uuidparse - a utility to parse unique identifiers

## [](#SYNOPSIS)SYNOPSIS

           uuidparse [options] uuid

## [](#DESCRIPTION)DESCRIPTION

           This command will parse unique identifier inputs from either
           command line arguments or standard input. The inputs are
           white-space separated.

## [](#OUTPUT)OUTPUT

       Variants
           ┌───────────┬──────────────────────────┐
           │           │                          │
           │ NCS       │ Network Computing System │
           │           │ identifier. These were   │
           │           │ the original UUIDs.      │
           ├───────────┼──────────────────────────┤
           │           │                          │
           │ DCE       │ The Open Software        │
           │           │ Foundation’s (OSF)       │
           │           │ Distributed Computing    │
           │           │ Environment UUIDs.       │
           ├───────────┼──────────────────────────┤
           │           │                          │
           │ Microsoft │ Microsoft Windows        │
           │           │ platform globally unique │
           │           │ identifier (GUID).       │
           ├───────────┼──────────────────────────┤
           │           │                          │
           │ other     │ Unknown variant. Usually │
           │           │ invalid input data.      │
           └───────────┴──────────────────────────┘

       Types
           ┌────────────┬──────────────────────────┐
           │            │                          │
           │ nil        │ Special type for zero in │
           │            │ type file.               │
           ├────────────┼──────────────────────────┤
           │            │                          │
           │ time-based │ The DCE time based.      │
           ├────────────┼──────────────────────────┤
           │            │                          │
           │ DCE        │ The DCE time and MAC     │
           │            │ Address.                 │
           ├────────────┼──────────────────────────┤
           │            │                          │
           │ name-based │ RFC 4122 md5sum hash.    │
           ├────────────┼──────────────────────────┤
           │            │                          │
           │ random     │ RFC 4122 random.         │
           ├────────────┼──────────────────────────┤
           │            │                          │
           │ sha1-based │ RFC 4122 sha-1 hash.     │
           ├────────────┼──────────────────────────┤
           │            │                          │
           │ unknown    │ Unknown type. Usually    │
           │            │ invalid input data.      │
           └────────────┴──────────────────────────┘

## [](#OPTIONS)OPTIONS

           -J, --json
               Use JSON output format.

           -n, --noheadings
               Do not print a header line.

           -o, --output
               Specify which output columns to print. Use --help to get a
               list of all supported columns.

           -r, --raw
               Use the raw output format.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

           LIBSMARTCOLS_JSON=compact|lines
               Control JSON output format when using --json. Supported values
               are compact for JSON output with minimal whitespace, and lines
               for JSON Lines format (one JSON object per line). If unset or
               set to any other value, pretty-printed JSON is used.

## [](#AUTHORS)AUTHORS

           Sami Kerola <kerolasa@iki.fi>

## [](#SEE_ALSO)SEE ALSO

           uuidgen(1), libuuid(3), RFC 4122
           <https://tools.ietf.org/html/rfc4122>

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The uuidparse command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                   UUIDPARSE(1)

------------------------------------------------------------------------

Pages that refer to this page: [uuidgen(1)](../man1/uuidgen.1.html)

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
