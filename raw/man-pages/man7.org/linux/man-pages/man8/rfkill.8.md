---
{"title": "rfkill(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rfkill.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rfkill(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [COMMANDS](#COMMANDS) \| [EXAMPLE](#EXAMPLE) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RFKILL(8)                 System Administration                 RFKILL(8)

## [](#NAME)NAME

           rfkill - tool for enabling and disabling wireless devices

## [](#SYNOPSIS)SYNOPSIS

           rfkill [options] [command] [ID|type ...]

## [](#DESCRIPTION)DESCRIPTION

           rfkill lists, enabling and disabling wireless devices.

           The command "list" output format is deprecated and maintained for
           backward compatibility only. The new output format is the default
           when no command is specified or when the option --output is used.

           The default output is subject to change. So whenever possible, you
           should avoid using default outputs in your scripts. Always
           explicitly define expected columns by using the --output option
           together with a columns list in environments where a stable output
           is required.

## [](#OPTIONS)OPTIONS

           -J, --json
               Use JSON output format.

           -n, --noheadings
               Do not print a header line.

           -o, --output
               Specify which output columns to print. Use --help to get a
               list of available columns.

           --output-all
               Output all available columns.

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

## [](#COMMANDS)COMMANDS

           help
               Display help text and exit.

           event
               Listen for rfkill events and display them on stdout.

           list [id|type ...]
               List the current state of all available devices. The command
               output format is deprecated, see the DESCRIPTION section. It
               is a good idea to check with list command id or type scope is
               appropriate before setting block or unblock. Special all type
               string will match everything. Use of multiple ID or type
               arguments is supported. Possible types are all, {wlan | wifi},
               bluetooth, {uwb | ultrawideband}, wimax, wwan, gps, fm, nfc.

           block id|type [...]
               Disable the corresponding device.

           unblock id|type [...]
               Enable the corresponding device. If the device is
               hard-blocked, for example via a hardware switch, it will
               remain unavailable though it is now soft-unblocked.

           toggle id|type [...]
               Enable or disable the corresponding device.

## [](#EXAMPLE)EXAMPLE

                 rfkill --output ID,TYPE
                 rfkill block all
                 rfkill unblock wlan
                 rfkill block bluetooth uwb wimax wwan gps fm nfc

## [](#AUTHORS)AUTHORS

           rfkill was originally written by Johannes Berg
           <johannes@sipsolutions.net> and Marcel Holtmann
           <marcel@holtmann.org>. The code has been later modified by Sami
           Kerola <kerolasa@iki.fi> and Karel Zak <kzak@redhat.com> for the
           util-linux project.

           This manual page was written by Darren Salt
           <linux@youmustbejoking.demon.co.uk> for the Debian project (and
           may be used by others).

## [](#SEE_ALSO)SEE ALSO

           powertop(8), systemd-rfkill(8), Linux kernel documentation
           <https://docs.kernel.org/driver-api/rfkill.html>

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The rfkill command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                      RFKILL(8)

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
