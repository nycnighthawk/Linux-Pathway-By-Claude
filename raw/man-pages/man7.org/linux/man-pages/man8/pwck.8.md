---
{"title": "pwck(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pwck.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pwck(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [EXIT VALUES](#EXIT_VALUES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PWCK(8)                 System Management Commands                PWCK(8)

## [](#NAME)NAME

           pwck - verify the integrity of password files

## [](#SYNOPSIS)SYNOPSIS

           pwck [options] [PASSWORDFILE [ SHADOWFILE ]]

## [](#DESCRIPTION)DESCRIPTION

           The pwck command verifies the integrity of the users and
           authentication information. It checks that all entries in
           /etc/passwd and /etc/shadow have the proper format and contain
           valid data. The user is prompted to delete entries that are
           improperly formatted or which have other uncorrectable errors.

           Checks are made to verify that each entry has:

           •   the correct number of fields

           •   a unique and valid user name

           •   a valid user and group identifier

           •   a valid primary group

           •   a valid home directory

           •   a valid login shell

           Checks for shadowed password information are enabled when the
           second file parameter SHADOWFILE is specified or when /etc/shadow
           exists on the system.

           These checks are the following:

           •   every passwd entry has a matching shadow entry, and every
               shadow entry has a matching passwd entry

           •   passwords are specified in the shadowed file

           •   shadow entries have the correct number of fields

           •   shadow entries are unique in shadow

           •   the last password changes are not in the future

           The checks for correct number of fields and unique user name are
           fatal. If the entry has the wrong number of fields, the user will
           be prompted to delete the entire line. If the user does not answer
           affirmatively, all further checks are bypassed. An entry with a
           duplicated user name is prompted for deletion, but the remaining
           checks will still be made. All other errors are warnings and the
           user is encouraged to run the usermod command to correct the
           error.

           The commands which operate on the /etc/passwd file are not able to
           alter corrupted or duplicated entries.  pwck should be used in
           those circumstances to remove the offending entry.

## [](#OPTIONS)OPTIONS

           The -r and -s options cannot be combined.

           The options which apply to the pwck command are:

           --badname
               Allow names that do not conform to standards.

           -h, --help
               Display help message and exit.

           -q, --quiet
               Report errors only. The warnings which do not require any
               action from the user won't be displayed.

           -r, --read-only
               Execute the pwck command in read-only mode.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

           -s, --sort
               Sort entries in /etc/passwd and /etc/shadow by UID.

           By default, pwck operates on the files /etc/passwd and
           /etc/shadow. The user may select alternate files with the passwd
           and shadow parameters.

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variables in /etc/login.defs change
           the behavior of this tool:

           NONEXISTENT (string)
               If a system account intentionally does not have a home
               directory that exists, this string can be provided in the
               /etc/passwd entry for the account to indicate this. The result
               is that pwck will not emit a spurious warning for this
               account.

           PASS_MAX_DAYS (number)
               The maximum number of days a password may be used. If the
               password is older than this, a password change will be forced.
               If not specified, -1 will be assumed (which disables the
               restriction).

           PASS_MIN_DAYS (number)
               The minimum number of days allowed between password changes.
               Any password changes attempted sooner than this will be
               rejected. If not specified, 0 will be assumed (which disables
               the restriction).

           PASS_WARN_AGE (number)
               The number of days warning given before a password expires. A
               zero means warning is given only upon the day of expiration, a
               value of -1 means no warning is given. If not specified, no
               warning will be provided.

## [](#FILES)FILES

           /etc/group
               Group account information.

           /etc/passwd
               User account information.

           /etc/shadow
               Secure user account information.

## [](#EXIT_VALUES)EXIT VALUES

           The pwck command exits with the following values:

           0
               success

           1
               invalid command syntax

           2
               one or more bad password entries

           3
               can't open password files

           4
               can't lock password files

           5
               can't update password files

           6
               can't sort password files

## [](#SEE_ALSO)SEE ALSO

           group(5), grpck(8), passwd(5), shadow(5), usermod(8).

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

    shadow-utils 4.19.0             08/04/2026                        PWCK(8)

------------------------------------------------------------------------

Pages that refer to this page: [passwd(5@@shadow-utils)](../man5/passwd.5@@shadow-utils.html),  [shadow(5)](../man5/shadow.5.html),  [grpck(8)](../man8/grpck.8.html),  [pwconv(8)](../man8/pwconv.8.html)

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
