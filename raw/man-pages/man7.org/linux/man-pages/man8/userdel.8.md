---
{"title": "userdel(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/userdel.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# userdel(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [EXIT VALUES](#EXIT_VALUES) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    USERDEL(8)              System Management Commands             USERDEL(8)

## [](#NAME)NAME

           userdel - delete a user account and related files

## [](#SYNOPSIS)SYNOPSIS

           userdel [options] LOGIN

## [](#DESCRIPTION)DESCRIPTION

           The userdel command modifies the system account files, deleting
           all entries that refer to the user name LOGIN. The named user must
           exist.

## [](#OPTIONS)OPTIONS

           The options which apply to the userdel command are:

           -f, --force
               This option forces the removal of the user account and any
               other requested actions, skipping any safety checks.

               Note: This option is dangerous and may leave your system in an
               inconsistent state.

           -h, --help
               Display help message and exit.

           -r, --remove
               Files in the user's home directory will be removed along with
               the home directory itself and the user's mail spool. Files
               located in other file systems will have to be searched for and
               deleted manually.

               The mail spool is defined by the MAIL_DIR variable in the
               login.defs file.

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

           -Z, --selinux-user
               Remove any SELinux user mapping for the user's login.

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variables in /etc/login.defs change
           the behavior of this tool:

           MAIL_DIR (string)
               The mail spool directory. This is needed to manipulate the
               mailbox when its corresponding user account is modified or
               deleted. If not specified, a compile-time default is used. The
               parameter CREATE_MAIL_SPOOL in /etc/default/useradd determines
               whether the mail spool should be created.

           MAIL_FILE (string)
               Defines the location of the users mail spool files relatively
               to their home directory.

           The MAIL_DIR and MAIL_FILE variables are used by useradd, usermod,
           and userdel to create, move, or delete the user's mail spool.

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

           USERDEL_CMD (string)
               If defined, this command is run when removing a user. It
               should remove any at/cron/print jobs etc. owned by the user to
               be removed (passed as the first argument).

               The return code of the script is not taken into account.

               Here is an example script, which removes the user's cron, at
               and print jobs:

                   #! /bin/sh

                   # Check for the required argument.
                   if [ $# != 1 ]; then
                        echo "Usage: $0 username"
                        exit 1
                   fi

                   # Remove cron jobs.
                   crontab -r -u $1

                   # Remove at jobs.
                   # Note that it will remove any jobs owned by the same UID,
                   # even if it was shared by a different username.
                   AT_SPOOL_DIR=/var/spool/cron/atjobs
                   find $AT_SPOOL_DIR -name "[^.]*" -type f -user $1 -delete \;

                   # Remove print jobs.
                   lprm $1

                   # All done.
                   exit 0

           USERGROUPS_ENAB (boolean)
               If set to yes, userdel will remove the user's group if it
               contains no more members, and useradd will create by default a
               group with the name of the user.

## [](#FILES)FILES

           /etc/group
               Group account information.

           /etc/login.defs
               Shadow password suite configuration.

           /etc/passwd
               User account information.

           /etc/shadow
               Secure user account information.

           /etc/shadow-maint/userdel-pre.d/*,
           /etc/shadow-maint/userdel-post.d/*
               Run-part files to execute during user deletion. The
               environment variable ACTION will be populated with userdel and
               SUBJECT with the username.  userdel-pre.d will be executed
               prior to any user deletion.  userdel-post.d will execute after
               user deletion. If a script exits non-zero then execution will
               terminate.

           /etc/subgid
               Per user subordinate group IDs.

           /etc/subuid
               Per user subordinate user IDs.

## [](#EXIT_VALUES)EXIT VALUES

           The userdel command exits with the following values:

           0
               success

           1
               can't update password file

           2
               invalid command syntax

           6
               specified user doesn't exist

           8
               user currently logged in

           10
               can't update group file

           12
               can't remove home directory

## [](#CAVEATS)CAVEATS

           userdel will not allow you to remove an account if there are
           running processes which belong to this account. In that case, you
           may have to kill those processes or lock the user's password or
           account and remove the account later. The -f option can force the
           deletion of this account.

           You should manually check all file systems to ensure that no files
           remain owned by this user.

           You may not remove any NIS attributes on a NIS client. This must
           be performed on the NIS server.

           If USERGROUPS_ENAB is defined to yes in /etc/login.defs, userdel
           will delete the group with the same name as the user. To avoid
           inconsistencies in the passwd and group databases, userdel will
           check that this group is not used as a primary group for another
           user, and will just warn without deleting the group otherwise. The
           -f option can force the deletion of this group.

## [](#SEE_ALSO)SEE ALSO

           chfn(1), chsh(1), passwd(1), login.defs(5), gpasswd(8),
           groupadd(8), groupdel(8), groupmod(8), subgid(5), subuid(5),
           useradd(8), usermod(8).

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

    shadow-utils 4.19.0             08/04/2026                     USERDEL(8)

------------------------------------------------------------------------

Pages that refer to this page: [getsubids(1)](../man1/getsubids.1.html),  [newgidmap(1)](../man1/newgidmap.1.html),  [newuidmap(1)](../man1/newuidmap.1.html),  [subgid(5)](../man5/subgid.5.html),  [subuid(5)](../man5/subuid.5.html),  [groupadd(8)](../man8/groupadd.8.html),  [groupdel(8)](../man8/groupdel.8.html),  [groupmems(8)](../man8/groupmems.8.html),  [groupmod(8)](../man8/groupmod.8.html),  [useradd(8)](../man8/useradd.8.html),  [usermod(8)](../man8/usermod.8.html)

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
