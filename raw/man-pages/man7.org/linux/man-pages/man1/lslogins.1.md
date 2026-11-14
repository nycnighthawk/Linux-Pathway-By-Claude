---
{"title": "lslogins(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lslogins.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lslogins(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [ENVIRONMENT](#ENVIRONMENT) \| [HISTORY](#HISTORY) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LSLOGINS(1)                   User Commands                   LSLOGINS(1)

## [](#NAME)NAME

           lslogins - display information about known users in the system

## [](#SYNOPSIS)SYNOPSIS

           lslogins [options] [-s|-u[=UID]] [-g groups] [-l logins]
           [username]

## [](#DESCRIPTION)DESCRIPTION

           Examine the wtmp and btmp logs, /etc/shadow (if necessary) and
           /passwd and output the desired data.

           The optional argument username forces lslogins to print all
           available details about the specified user only. In this case the
           output format is different than in case of -l or -g and unknown is
           username reported as an error.

           The default action is to list info about all the users in the
           system.

## [](#OPTIONS)OPTIONS

           Mandatory arguments to long options are mandatory for short
           options too.

           -a, --acc-expiration
               Display data about the date of last password change and the
               account expiration date (see shadow(5) for more info).
               (Requires root privileges.)

           --btmp-file path
               Alternate path for btmp.

           -c, --colon-separate
               Separate info about each user with a colon instead of a
               newline.

           -e, --export
               Output data in the format of NAME=VALUE. See also option
               --shell.

           -f, --failed
               Display data about the users' last failed login attempts.

           -G, --supp-groups
               Show information about supplementary groups.

           -g, --groups groups
               Only show data of users belonging to groups. More than one
               group may be specified; the list has to be comma-separated.
               Unknown group names are ignored.

               Note that the relation between user and group may be invisible
               for the primary group if the user is not explicitly specified
               as group member (e.g., in /etc/group). If the command lslogins
               scans for groups then it uses the groups database only, and
               the user database with primary GID is not used at all.

           -L, --last
               Display data containing information about the users' last
               login sessions.

           -l, --logins logins
               Only show data of users with a login specified in logins (user
               names or user IDs). More than one login may be specified; the
               list has to be comma-separated. Unknown login names are
               ignored.

           -n, --newline
               Display each piece of information on a separate line.

           --noheadings
               Do not print a header line.

           --notruncate
               Don’t truncate output.

           -o, --output list
               Specify which output columns to print. The default list of
               columns may be extended if list is specified in the format
               +list.

           --output-all
               Output all available columns. --list-columns to get a list of
               all supported columns.

           -H, --list-columns
               List the columns that can be specified with the --output
               option. Can be used with --json or --raw to get the list in a
               machine-readable format.

           -p, --pwd
               Display information related to login by password (see also
               -afL).

           -r, --raw
               Raw output (no columnation).

           -J, --json
               JSON format output.

           -s, --system-accs
               Show system accounts. These are by default all accounts with a
               UID between 101 and 999 (inclusive), with the exception of
               either nobody or nfsnobody (UID 65534). This hardcoded default
               may be overridden by the parameters SYS_UID_MIN and
               SYS_UID_MAX in the file /etc/login.defs.

           --time-format type
               Display dates in short, full or iso format. The default is
               short, this time format is designed to be space efficient and
               human readable.

           -u, --user-accs
               Show user accounts. These are by default all accounts with a
               UID above 1000 (inclusive), with the exception of either
               nobody or nfsnobody (UID 65534). This hardcoded default may be
               overridden by the parameters UID_MIN and UID_MAX in the file
               /etc/login.defs.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

           --wtmp-file path
               Alternate path for wtmp.

           --lastlog-file path
               Alternate path for lastlog(8).

           -y, --shell
               The column name will be modified to contain only characters
               allowed for shell variable identifiers. This is usable, for
               example, with --export. Note that this feature has been
               automatically enabled for --export in version 2.37, but due to
               compatibility issues, now it’s necessary to request this
               behavior by --shell.

           -Z, --context
               Display the users' security context.

           -z, --print0
               Delimit user entries with a nul character, instead of a
               newline.

## [](#EXIT_STATUS)EXIT STATUS

           0
               if OK,

           1
               if incorrect arguments specified,

           2
               if a serious error occurs (e.g., a corrupt log).

## [](#NOTES)NOTES

           The default UID thresholds are read from /etc/login.defs.

       Password status
           Multiple fields describe password status.

           "Password is locked"
               The password is prefixed by '!!', and the user cannot login
               although the password is set or empty. This is common for new
               accounts without a set password.

           "Password not required (empty)"
               The password is not set (hash is missing); this is common for
               locked system accounts. Not requiring a password does not mean
               the user can log-in without a password. It depends on the
               password "lock" status.

           "Login by password disabled"
               'yes' means that there is no valid password. The password hash
               is missing, or the hash method is unknown or contains invalid
               chars.

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

## [](#HISTORY)HISTORY

           The lslogins utility is inspired by the logins utility, which
           first appeared in FreeBSD 4.10.

## [](#AUTHORS)AUTHORS

           Ondrej Oprala <ooprala@redhat.com>, Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           group(5), passwd(5), shadow(5), utmp(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The lslogins command is part of the util-linux package which can
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                    LSLOGINS(1)

------------------------------------------------------------------------

Pages that refer to this page: [utmp(5)](../man5/utmp.5.html)

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
