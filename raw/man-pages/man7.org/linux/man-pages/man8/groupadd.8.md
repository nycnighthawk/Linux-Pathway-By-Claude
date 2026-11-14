---
{"title": "groupadd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/groupadd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groupadd(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [CAVEATS](#CAVEATS) \| [EXIT VALUES](#EXIT_VALUES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GROUPADD(8)             System Management Commands            GROUPADD(8)

## [](#NAME)NAME

           groupadd - create a new group

## [](#SYNOPSIS)SYNOPSIS

           groupadd [OPTIONS] NEWGROUP

## [](#DESCRIPTION)DESCRIPTION

           The groupadd command creates a new group account using the values
           specified on the command line plus the default values from the
           system. The new group will be entered into the system files as
           needed.

           Groupnames may contain only lower and upper case letters, digits,
           underscores, or dashes. They can end with a dollar sign. Dashes
           are not allowed at the beginning of the groupname. Fully numeric
           groupnames and groupnames . or .. are also disallowed.

           Groupnames may only be up to 32 characters long.

## [](#OPTIONS)OPTIONS

           The options which apply to the groupadd command are:

           -f, --force
               This option causes the command to simply exit with success
               status if the specified group already exists. When used with
               -g, and the specified GID already exists, another (unique) GID
               is chosen (i.e.  -g is turned off).

           -g, --gid GID
               The numerical value of the group's ID.  GID must be unique,
               unless the -o option is used. The value must be non-negative.
               The default is to use the smallest ID value greater than or
               equal to GID_MIN and greater than every other group.

               See also the -r option and the GID_MAX description.

           -h, --help
               Display help message and exit.

           -K, --key KEY=VALUE
               Overrides /etc/login.defs defaults (GID_MIN, GID_MAX and
               others). Multiple -K options can be specified.

               Example: -K GID_MIN=100  -K GID_MAX=499

               Note: -K GID_MIN=10,GID_MAX=499 doesn't work yet.

           -o, --non-unique
               permits the creation of a group with an already used numerical
               ID. As a result, for this GID, the mapping towards group
               NEWGROUP may not be unique.

           -p, --password PASSWORD
               defines an initial password for the group account. PASSWORD is
               expected to be encrypted, as returned by crypt (3).

               Without this option, the group account will be locked and with
               no password defined, i.e. a single exclamation mark in the
               respective field of ths system account file /etc/group or
               /etc/gshadow.

               Note: This option is not recommended because the password (or
               encrypted password) will be visible by users listing the
               processes.

               You should make sure the password respects the system's
               password policy.

           -r, --system
               Create a system group.

               The numeric identifiers of new system groups are chosen in the
               SYS_GID_MIN-SYS_GID_MAX range, defined in login.defs, instead
               of GID_MIN-GID_MAX.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

           -P, --prefix PREFIX_DIR
               Apply changes to configuration files under the root filesystem
               found under the directory PREFIX_DIR. This option does not
               chroot and is intended for preparing a cross-compilation
               target. Some limitations: NIS and LDAP users/groups are not
               verified. PAM authentication is using the host files. No
               SELINUX support.

           -U, --users
               A comma-separated list of usernames to add as members of the
               group.

               The default behavior (if the -g, -N, and -U options are not
               specified) is defined by the USERGROUPS_ENAB variable in
               /etc/login.defs.

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variables in /etc/login.defs change
           the behavior of this tool:

           GID_MAX (number), GID_MIN (number)
               Range of group IDs used for the creation of regular groups by
               useradd, groupadd, or newusers.

               The default value for GID_MIN (resp.  GID_MAX) is 1000 (resp.
               60000).

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

           SYS_GID_MAX (number), SYS_GID_MIN (number)
               Range of group IDs used for the creation of system groups by
               useradd, groupadd, or newusers.

               The default value for SYS_GID_MIN (resp.  SYS_GID_MAX) is 101
               (resp.  GID_MIN-1).

## [](#FILES)FILES

           /etc/group
               Group account information.

           /etc/gshadow
               Secure group account information.

           /etc/login.defs
               Shadow password suite configuration.

## [](#CAVEATS)CAVEATS

           You may not add a NIS or LDAP group. This must be performed on the
           corresponding server.

           If the groupname already exists in an external group database such
           as NIS or LDAP, groupadd will deny the group creation request.

## [](#EXIT_VALUES)EXIT VALUES

           The groupadd command exits with the following values:

           0
               success

           2
               invalid command syntax

           3
               invalid argument to option

           4
               GID is already used (when called without -o)

           9
               group name is already used

           10
               can't update group file

## [](#SEE_ALSO)SEE ALSO

           chfn(1), chsh(1), passwd(1), gpasswd(8), groupdel(8), groupmod(8),
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

    shadow-utils 4.19.0             08/04/2026                    GROUPADD(8)

------------------------------------------------------------------------

Pages that refer to this page: [gpasswd(1)](../man1/gpasswd.1.html),  [homectl(1)](../man1/homectl.1.html),  [rpm-sysusers(7)](../man7/rpm-sysusers.7.html),  [chgpasswd(8)](../man8/chgpasswd.8.html),  [groupdel(8)](../man8/groupdel.8.html),  [groupmems(8)](../man8/groupmems.8.html),  [groupmod(8)](../man8/groupmod.8.html),  [useradd(8)](../man8/useradd.8.html),  [userdel(8)](../man8/userdel.8.html),  [usermod(8)](../man8/usermod.8.html)

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
