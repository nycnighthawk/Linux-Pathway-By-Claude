---
{"title": "groupmems(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/groupmems.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groupmems(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SETUP](#SETUP) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GROUPMEMS(8)            System Management Commands           GROUPMEMS(8)

## [](#NAME)NAME

           groupmems - administer members of a user's primary group

## [](#SYNOPSIS)SYNOPSIS

           groupmems -a user_name | -d user_name | [-g group_name] | -l | -p

## [](#DESCRIPTION)DESCRIPTION

           The groupmems command allows a user to administer their own group
           membership list without the requirement of superuser privileges.
           The groupmems utility is for systems that configure its users to
           be in their own name sake primary group (i.e., guest / guest).

           Only the superuser, as administrator, can use groupmems to alter
           the memberships of other groups.

## [](#OPTIONS)OPTIONS

           The options which apply to the groupmems command are:

           -a, --add user_name
               Add a user to the group membership list.

               If the /etc/gshadow file exist, and the group has no entry in
               the /etc/gshadow file, a new entry will be created.

           -d, --delete user_name
               Delete a user from the group membership list.

               If the /etc/gshadow file exist, the user will be removed from
               the list of members and administrators of the group.

               If the /etc/gshadow file exist, and the group has no entry in
               the /etc/gshadow file, a new entry will be created.

           -g, --group group_name
               The superuser can specify which group membership list to
               modify.

           -h, --help
               Display help message and exit.

           -l, --list
               List the group membership list.

           -p, --purge
               Purge all users from the group membership list.

               If the /etc/gshadow file exist, and the group has no entry in
               the /etc/gshadow file, a new entry will be created.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

## [](#SETUP)SETUP

           The groupmems executable should be in mode 2710 as user root and
           in group groups. The system administrator can add users to group
           groups to allow or disallow them using the groupmems utility to
           manage their own group membership list.

                    $ groupadd -r groups
                    $ chmod 2710 groupmems
                    $ chown root:groups groupmems
                    $ groupmems -g groups -a gk4

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
               secure group account information

## [](#SEE_ALSO)SEE ALSO

           chfn(1), chsh(1), passwd(1), groupadd(8), groupdel(8), useradd(8),
           userdel(8), usermod(8).

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

    shadow-utils 4.19.0             08/04/2026                   GROUPMEMS(8)

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
