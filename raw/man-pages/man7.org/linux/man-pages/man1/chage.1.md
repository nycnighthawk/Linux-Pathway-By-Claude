---
{"title": "chage(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/chage.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chage(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTE](#NOTE) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [EXIT VALUES](#EXIT_VALUES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHAGE(1)                      User Commands                      CHAGE(1)

## [](#NAME)NAME

           chage - change user password expiry information

## [](#SYNOPSIS)SYNOPSIS

           chage [options] LOGIN

## [](#DESCRIPTION)DESCRIPTION

           The chage command changes password expiration information for a
           user. It sets the number of days between password changes and the
           date of the last password change. This information is used by the
           system to determine when the user must change their password.

## [](#OPTIONS)OPTIONS

           The options which apply to the chage command are:

           -d, --lastday LAST_DAY
               Set the date when the password was last changed. The value can
               be specified as a date in the YYYY-MM-DD format or as a number
               of days since 1970-01-01. The date is interpreted using the
               UTC timezone. If the LAST_DAY is set to 0, the user is forced
               to change their password upon the next login.

               Passing the value -1 or an empty string as the LAST_DAY clears
               the value and removes the password change requirement.

           -E, --expiredate EXPIRE_DATE
               Set the date on which the user's password expires and their
               account will no longer be accessible. The value can be
               specified as a date in the YYYY-MM-DD format or as a number of
               days since 1970-01-01. The date is interpreted using the UTC
               timezone. If the password expires, the user must contact the
               system administrator to regain access to the system.

               For example, the following command sets an account to expire
               in 180 days:

                            chage -E $(date -d +180days +%F)

               Passing the value -1 or an empty string as the EXPIRE_DATE
               removes the account expiration date.

           -h, --help
               Display help message and exit.

           -i, --iso8601
               When printing dates, use YYYY-MM-DD format.

           -I, --inactive INACTIVE
               Set the number of days of inactivity after a password has
               expired before the account is locked. The INACTIVE option is
               the number of days of inactivity. A user whose account is
               locked must contact the system administrator before being able
               to use the system again.

               Passing the number -1 as the INACTIVE will remove an account's
               inactivity.

           -l, --list
               Show account aging information.

           -m, --mindays MIN_DAYS
               Set the minimum number of days between password changes to
               MIN_DAYS. A value of zero for this field indicates that the
               user may change their password at any time.

           -M, --maxdays MAX_DAYS
               Set the maximum number of days during which a password is
               valid. When MAX_DAYS plus LAST_DAY is less than the current
               day, the user will be required to change their password before
               being able to use their account. This occurrence can be
               planned for in advance by use of the -W option, which provides
               the user with advance warning.

               Passing the number -1 as MAX_DAYS will remove checking a
               password's validity.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

           -P, --prefix PREFIX_DIR
               Apply changes to configuration files under the root filesystem
               found under the directory PREFIX_DIR. This option does not
               chroot and is intended for preparing a cross-compilation
               target. Some limitations: NIS and LDAP users/groups are not
               verified. No SELINUX support.

           -W, --warndays WARN_DAYS
               Set the number of days of warning before a password change is
               required. The WARN_DAYS option is the number of days prior to
               the password expiring that a user will be warned their
               password is about to expire.

           If none of the options are selected, chage operates in an
           interactive fashion, prompting the user with the current values
           for all of the fields. Enter the new value to change the field, or
           leave the line blank to use the current value. The current value
           is displayed between a pair of [ ] marks.

## [](#NOTE)NOTE

           The chage program requires a shadow password file to be available.

           The chage program will report only the information from the shadow
           password file. This implies that configuration from other sources
           (e.g. LDAP or empty password hash field from the passwd file) that
           affect the user's login will not be shown in the chage output.

           The chage program will also not report any inconsistency between
           the shadow and passwd files (e.g. missing x in the passwd file).
           The pwck can be used to check for this kind of inconsistencies.

           The chage command is restricted to the root user, except for the
           -l option, which may be used by an unprivileged user to determine
           when their password or account is due to expire.

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variables in /etc/login.defs change
           the behavior of this tool:

## [](#FILES)FILES

           /etc/passwd
               User account information.

           /etc/shadow
               Secure user account information.

## [](#EXIT_VALUES)EXIT VALUES

           The chage command exits with the following values:

           0
               success

           1
               permission denied

           2
               invalid command syntax

           15
               can't find the shadow password file

## [](#SEE_ALSO)SEE ALSO

           passwd(5), shadow(5).

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

    shadow-utils 4.19.0             08/04/2026                       CHAGE(1)

------------------------------------------------------------------------

Pages that refer to this page: [shadow(5)](../man5/shadow.5.html)

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
