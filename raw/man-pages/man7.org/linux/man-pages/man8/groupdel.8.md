---
{"title": "groupdel(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/groupdel.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groupdel(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CAVEATS](#CAVEATS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [EXIT VALUES](#EXIT_VALUES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GROUPDEL(8)             System Management Commands            GROUPDEL(8)

## [](#NAME)NAME

           groupdel - delete a group

## [](#SYNOPSIS)SYNOPSIS

           groupdel [options] GROUP

## [](#DESCRIPTION)DESCRIPTION

           The groupdel command modifies the system account files, deleting
           all entries that refer to GROUP. The named group must exist.

## [](#OPTIONS)OPTIONS

           The options which apply to the groupdel command are:

           -f, --force
               This option forces the removal of the group, even if there's
               some user having the group as the primary one.

           -h, --help
               Display help message and exit.

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

## [](#CAVEATS)CAVEATS

           You may not remove the primary group of any existing user. You
           must remove the user before you remove the group.

           You should manually check all file systems to ensure that no files
           remain owned by this group.

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

## [](#EXIT_VALUES)EXIT VALUES

           The groupdel command exits with the following values:

           0
               success

           2
               invalid command syntax

           6
               specified group doesn't exist

           8
               can't remove user's primary group

           10
               can't update group file

## [](#SEE_ALSO)SEE ALSO

           chfn(1), chsh(1), passwd(1), gpasswd(8), groupadd(8), groupmod(8),
           useradd(8), userdel(8), usermod(8).

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

    shadow-utils 4.19.0             08/04/2026                    GROUPDEL(8)

------------------------------------------------------------------------

Pages that refer to this page: [gpasswd(1)](../man1/gpasswd.1.html),  [groupadd(8)](../man8/groupadd.8.html),  [groupmems(8)](../man8/groupmems.8.html),  [groupmod(8)](../man8/groupmod.8.html),  [useradd(8)](../man8/useradd.8.html),  [userdel(8)](../man8/userdel.8.html),  [usermod(8)](../man8/usermod.8.html)

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
