---
{"title": "lastlog(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lastlog.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lastlog(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTE](#NOTE) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [CAVEATS](#CAVEATS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LASTLOG(8)              System Management Commands             LASTLOG(8)

## [](#NAME)NAME

           lastlog - reports the most recent login of all users or of a given
           user

## [](#SYNOPSIS)SYNOPSIS

           lastlog [options]

## [](#DESCRIPTION)DESCRIPTION

           lastlog formats and prints the contents of the last login log
           /var/log/lastlog file. The login-name, port, and last login time
           will be printed. The default (no flags) causes lastlog entries to
           be printed, sorted by their order in /etc/passwd.

## [](#OPTIONS)OPTIONS

           The options which apply to the lastlog command are:

           -b, --before DAYS
               Print only lastlog records older than DAYS.

           -C, --clear
               Clear lastlog record of a user. This option can be used only
               together with -u (--user).

           -h, --help
               Display help message and exit.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

           -S, --set
               Set lastlog record of a user to the current time. This option
               can be used only together with -u (--user).

           -t, --time DAYS
               Print the lastlog records more recent than DAYS.

           -u, --user LOGIN|RANGE
               Print the lastlog record of the specified user(s).

               The users can be specified by a login name, a numerical user
               ID, or a RANGE of users. This RANGE of users can be specified
               with a min and max values (UID_MIN-UID_MAX), a max value
               (-UID_MAX), or a min value (UID_MIN-).

           -a
               Print the lastlog records of the users that have logged in at
               least once. Excludes records for users with '**Never logged
               in**'.

           If the user has never logged in the message ** Never logged in**
           will be displayed instead of the port and time.

           Only the entries for the current users of the system will be
           displayed. Other entries may exist for users that were deleted
           previously.

## [](#NOTE)NOTE

           The lastlog file is a database which contains info on the last
           login of each user. You should not rotate it. It is a sparse file,
           so its size on the disk is usually much smaller than the one shown
           by "ls -l" (which can indicate a really big file if you have in
           passwd users with a high UID). You can display its real size with
           "ls -s".

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variables in /etc/login.defs change
           the behavior of this tool:

           LASTLOG_UID_MAX (number)
               Highest user ID number for which the lastlog entries should be
               updated. As higher user IDs are usually tracked by remote user
               identity and authentication services there is no need to
               create a huge sparse lastlog file for them.

               No LASTLOG_UID_MAX option present in the configuration means
               that there is no user ID limit for writing lastlog entries.

## [](#FILES)FILES

           /var/log/lastlog
               Database times of previous user logins.

## [](#CAVEATS)CAVEATS

           Large gaps in UID numbers will cause the lastlog program to run
           longer with no output to the screen (i.e. if in lastlog database
           there is no entries for users with UID between 170 and 800 lastlog
           will appear to hang as it processes entries with UIDs 171-799).

           Having high UIDs can create problems when handling the
           /var/log/lastlog with external tools. Although the actual file is
           sparse and does not use too much space, certain applications are
           not designed to identify sparse files by default and may require a
           specific option to handle them.

## [](#COLOPHON)COLOPHON

           This page is part of the shadow-utils (utilities for managing
           accounts and shadow password files) project.  Information about
           the project can be found at 
           ⟨https://github.com/shadow-maint/shadow⟩.  If you have a bug report
           for this manual page, send it to
           pkg-shadow-devel@alioth-lists.debian.net.  This page was obtained
           from the tarball shadow-4.19.0.tar fetched from
           ⟨https://github.com/shadow-maint/shadow/releases⟩ on 2026-08-04.
           If you discover any rendering problems in this HTML version of the
           page, or you believe there is a better or more up-to-date source
           for the page, or you have corrections or improvements to the
           information in this COLOPHON (which is not part of the original
           manual page), send a mail to man-pages@man7.org

    shadow-utils 4.19.0             08/04/2026                     LASTLOG(8)

------------------------------------------------------------------------

Pages that refer to this page: [login(1)](../man1/login.1.html),  [lslogins(1)](../man1/lslogins.1.html),  [ll2_import_lastlog(3)](../man3/ll2_import_lastlog.3.html),  [lastlog2(8)](../man8/lastlog2.8.html)

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
