---
{"title": "lastlog2(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lastlog2.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lastlog2(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LASTLOG2(8)                   User Commands                   LASTLOG2(8)

## [](#NAME)NAME

           lastlog2 - displays date of last login for all users or a specific
           one

## [](#SYNOPSIS)SYNOPSIS

           lastlog2 [options]

## [](#DESCRIPTION)DESCRIPTION

           lastlog2 displays the content of the last-login database. The
           login-name, last-login-time, tty and remote-host will be printed.
           By default (no flags) all last-login entries are printed, in the
           order they were first written into the database.

           If a user has never logged in, the message **Never logged in** is
           displayed in the last-login-time column.

           Only the entries for the current users of the system are
           displayed. Other entries may exist for users that have meanwhile
           been deleted.

           Compared to lastlog(8), this command is Y2038-safe, and uses
           SQLite3 instead of a sparse file to store the information.

## [](#OPTIONS)OPTIONS

           -a, --active
               Do not print entries for users who have never logged in.

           -b, --before days
               Print only the last-login records older than days.

           -C, --clear
               Clear the last-login record of a user. This option can only be
               used together with -u (--user).

           -d, --database file
               Use file as lastlog2 database.

           -i, --import file
               Import data from an old lastlog file named file. Existing
               entries in the lastlog2 database will be overwritten.

           -j, --journal [mode]
               Show the current SQLite journal mode, or set it to mode.
               Without an argument, displays the current journal mode. With
               an argument, sets the journal mode to the specified value.

               Supported modes: WAL, DELETE, TRUNCATE, PERSIST, MEMORY, OFF.

               WAL (Write-Ahead Logging) mode is recommended for
               high-concurrency scenarios as it allows readers and writers to
               operate concurrently without blocking each other. This
               significantly reduces database lock contention in environments
               with frequent SSH logins. The journal mode setting is
               persistent and only needs to be set once.

               See sqlite3(1) PRAGMA journal_mode for more details about
               journal modes.

           -r, --rename newname
               Rename the user given with -u to this newname. This option can
               only be used together with -u (--user).

           -s, --service
               Display the PAM service used to login in the last column.

           -S, --set
               Set the last-login record of a user to the current time. This
               option can only be used together with -u (--user).

           -t, --time days
               Print only last-login records more recent than days.

           -u, --user login
               Print (or modify) the last-login record of the user login.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXAMPLES)EXAMPLES

           Display the current journal mode:

               lastlog2 -j

           Enable WAL mode for better concurrency (recommended for
           high-traffic servers):

               lastlog2 -j WAL

           Switch back to the default DELETE mode:

               lastlog2 -j DELETE

## [](#FILES)FILES

           /var/lib/lastlog/lastlog2.db
               Lastlog2 logging database file

## [](#AUTHORS)AUTHORS

           lastlog2 was written by Thorsten Kukuk for liblastlog2(3).

## [](#SEE_ALSO)SEE ALSO

           liblastlog2(3)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The lastlog2 command is part of the util-linux package which can
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                    LASTLOG2(8)

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
