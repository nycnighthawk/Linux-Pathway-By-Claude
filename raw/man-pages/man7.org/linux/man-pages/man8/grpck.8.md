---
{"title": "grpck(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/grpck.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# grpck(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [EXIT VALUES](#EXIT_VALUES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GRPCK(8)                System Management Commands               GRPCK(8)

## [](#NAME)NAME

           grpck - verify integrity of group files

## [](#SYNOPSIS)SYNOPSIS

           grpck [options] [group [ shadow ]]

## [](#DESCRIPTION)DESCRIPTION

           The grpck command verifies the integrity of the groups
           information. It checks that all entries in /etc/group and
           /etc/gshadow have the proper format and contain valid data. The
           user is prompted to delete entries that are improperly formatted
           or which have other uncorrectable errors.

           Checks are made to verify that each entry has:

           •   the correct number of fields

           •   a unique and valid group name

           •   a valid group identifier (/etc/group only)

           •   a valid list of members and administrators

           •   a corresponding entry in the /etc/gshadow file (respectively
               /etc/group for the gshadow checks)

           The checks for correct number of fields and unique group name are
           fatal. If an entry has the wrong number of fields, the user will
           be prompted to delete the entire line. If the user does not answer
           affirmatively, all further checks are bypassed. An entry with a
           duplicated group name is prompted for deletion, but the remaining
           checks will still be made. All other errors are warnings and the
           user is encouraged to run the groupmod command to correct the
           error.

           The commands which operate on the /etc/group and /etc/gshadow
           files are not able to alter corrupted or duplicated entries.
           grpck should be used in those circumstances to remove the
           offending entries.

## [](#OPTIONS)OPTIONS

           The -r and -s options cannot be combined.

           The options which apply to the grpck command are:

           -h, --help
               Display help message and exit.

           -r, --read-only
               Execute the grpck command in read-only mode. This causes all
               questions regarding changes to be answered no without user
               intervention.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

           -s, --sort
               Sort entries in /etc/group and /etc/gshadow by GID.

           -S, --silence-warnings
               Suppress more controversial warnings, in particular warnings
               about inconsistency between group members listed in /etc/group
               and /etc/ghadow.

           By default, grpck operates on /etc/group and /etc/gshadow. The
           user may select alternate files with the group and shadow
           parameters.

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

           /etc/passwd
               User account information.

## [](#EXIT_VALUES)EXIT VALUES

           The grpck command exits with the following values:

           0
               success

           1
               invalid command syntax

           2
               one or more bad group entries

           3
               can't open group files

           4
               can't lock group files

           5
               can't update group files

## [](#SEE_ALSO)SEE ALSO

           group(5), groupmod(8), gshadow(5), passwd(5), pwck(8), shadow(5).

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

    shadow-utils 4.19.0             08/04/2026                       GRPCK(8)

------------------------------------------------------------------------

Pages that refer to this page: [gpasswd(1)](../man1/gpasswd.1.html),  [gshadow(5)](../man5/gshadow.5.html),  [pwck(8)](../man8/pwck.8.html),  [pwconv(8)](../man8/pwconv.8.html)

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
