---
{"title": "faillog(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/faillog.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# faillog(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CAVEATS](#CAVEATS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FAILLOG(8)              System Management Commands             FAILLOG(8)

## [](#NAME)NAME

           faillog - display faillog records or set login failure limits

## [](#SYNOPSIS)SYNOPSIS

           faillog [options]

## [](#DESCRIPTION)DESCRIPTION

           faillog displays the contents of the failure log database
           (/var/log/faillog). It can also set the failure counters and
           limits. When faillog is run without arguments, it only displays
           the faillog records of the users who had a login failure.

## [](#OPTIONS)OPTIONS

           The options which apply to the faillog command are:

           -a, --all
               Display (or act on) faillog records for all users having an
               entry in the faillog database.

               The range of users can be restricted with the -u option.

               In display mode, this is still restricted to existing users
               but forces the display of the faillog entries even if they are
               empty.

               With the -l, -m, -r, -t options, the users' records are
               changed, even if the user does not exist on the system. This
               is useful to reset records of users that have been deleted or
               to set a policy in advance for a range of users.

           -h, --help
               Display help message and exit.

           -l, --lock-secs SEC
               Lock account for SEC seconds after failed login.

               Write access to /var/log/faillog is required for this option.

           -m, --maximum MAX
               Set the maximum number of login failures after the account is
               disabled to MAX.

               Selecting a MAX value of 0 has the effect of not placing a
               limit on the number of failed logins.

               The maximum failure count should always be 0 for root to
               prevent a denial of services attack against the system.

               Write access to /var/log/faillog is required for this option.

           -r, --reset
               Reset the counters of login failures.

               Write access to /var/log/faillog is required for this option.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

           -t, --time DAYS
               Display faillog records more recent than DAYS.

           -u, --user LOGIN|RANGE
               Display faillog record or maintains failure counters and
               limits (if used with -l, -m or -r options) only for the
               specified user(s).

               The users can be specified by a login name, a numerical user
               ID, or a RANGE of users. This RANGE of users can be specified
               with a min and max values (UID_MIN-UID_MAX), a max value
               (-UID_MAX), or a min value (UID_MIN-).

           When none of the -l, -m, or -r options are used, faillog displays
           the faillog record of the specified user(s).

## [](#CAVEATS)CAVEATS

           faillog only prints out users with no successful login since the
           last failure. To print out a user who has had a successful login
           since their last failure, you must explicitly request the user
           with the -u flag, or print out all users with the -a flag.

## [](#FILES)FILES

           /var/log/faillog
               Failure logging file.

## [](#SEE_ALSO)SEE ALSO

           login(1), faillog(5).

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

    shadow-utils 4.19.0             08/04/2026                     FAILLOG(8)

------------------------------------------------------------------------

Pages that refer to this page: [faillog(5)](../man5/faillog.5.html)

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
