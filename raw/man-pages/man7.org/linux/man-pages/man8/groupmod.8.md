---
{"title": "groupmod(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/groupmod.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groupmod(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [EXIT VALUES](#EXIT_VALUES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GROUPMOD(8)             System Management Commands            GROUPMOD(8)

## [](#NAME)NAME

           groupmod - modify a group definition on the system

## [](#SYNOPSIS)SYNOPSIS

           groupmod [options] GROUP

## [](#DESCRIPTION)DESCRIPTION

           The groupmod command modifies the definition of the specified
           GROUP by modifying the appropriate entry in the group database.

## [](#OPTIONS)OPTIONS

           The options which apply to the groupmod command are:

           -a, --append
               If group members are specified with -U, append them to the
               existing member list, rather than replacing it.

           -g, --gid GID
               The group ID of the given GROUP will be changed to GID.

               The value of GID must be a non-negative decimal integer. This
               value must be unique, unless the -o option is used.

               Users who use the group as primary group will be updated to
               keep the group as their primary group.

               Any files that have the old group ID and must continue to
               belong to GROUP, must have their group ID changed manually.

               No checks will be performed with regard to the GID_MIN,
               GID_MAX, SYS_GID_MIN, or SYS_GID_MAX from /etc/login.defs.

           -h, --help
               Display help message and exit.

           -n, --new-name NEW_GROUP
               The name of the group will be changed from GROUP to NEW_GROUP
               name.

           -o, --non-unique
               When used with the -g option, allow to change the group GID to
               a non-unique value.

           -p, --password PASSWORD
               The encrypted password, as returned by crypt(3).

               Note: This option is not recommended because the password (or
               encrypted password) will be visible by users listing the
               processes.

               You should make sure the password respects the system's
               password policy.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

           -P, --prefix PREFIX_DIR
               Apply changes in the PREFIX_DIR directory and use the
               configuration files from the PREFIX_DIR directory. This option
               does not chroot and is intended for preparing a
               cross-compilation target. Some limitations: NIS and LDAP
               users/groups are not verified. PAM authentication is using the
               host files. No SELINUX support.

           -U, --users
               A comma-separated list of usernames to add as members of the
               group.

               The default behavior (if the -g and -U options are not
               specified) is defined by the USERGROUPS_ENAB variable in
               /etc/login.defs.

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variables in /etc/login.defs change
           the behavior of this tool:

           MAX_MEMBERS_PER_GROUP (number)
               Maximum members per group entry. When the maximum is reached,
               a new group entry (line) is started in /etc/group (with the
               same name, same password, and same GID).

               The default value is 0, meaning that there are no limits in
               the number of members in a group.

               This feature (split group) permits to limit the length of
               lines in the group file. This is useful to make sure that
               lines for NIS groups are not larger than 1024 characters.

               If you need to enforce such limit, you can use 25.

               Note: split groups may not be supported by all tools (even in
               the Shadow toolsuite). You should not use this variable unless
               you really need it.

## [](#FILES)FILES

           /etc/group
               Group account information.

           /etc/gshadow
               Secure group account information.

           /etc/login.defs
               Shadow password suite configuration.

           /etc/passwd
               User account information.

## [](#EXIT_VALUES)EXIT VALUES

           The groupmod command exits with the following values:

           0
               E_SUCCESS: success

           2
               E_USAGE: invalid command syntax

           3
               E_BAD_ARG: invalid argument to option

           4
               E_GID_IN_USE: group id already in use

           6
               E_NOTFOUND: specified group doesn't exist

           9
               E_NAME_IN_USE: group name already in use

           10
               E_GRP_UPDATE: can't update group file

           11
               E_CLEANUP_SERVICE: can't setup cleanup service

           12
               E_PAM_USERNAME: can't determine your username for use with pam

           13
               E_PAM_ERROR: pam returned an error, see syslog facility id
               groupmod for the PAM error message

## [](#SEE_ALSO)SEE ALSO

           chfn(1), chsh(1), passwd(1), gpasswd(8), groupadd(8), groupdel(8),
           login.defs(5), useradd(8), userdel(8), usermod(8).

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

    shadow-utils 4.19.0             08/04/2026                    GROUPMOD(8)

------------------------------------------------------------------------

Pages that refer to this page: [gpasswd(1)](../man1/gpasswd.1.html),  [groupadd(8)](../man8/groupadd.8.html),  [groupdel(8)](../man8/groupdel.8.html),  [grpck(8)](../man8/grpck.8.html),  [useradd(8)](../man8/useradd.8.html),  [userdel(8)](../man8/userdel.8.html),  [usermod(8)](../man8/usermod.8.html)

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
