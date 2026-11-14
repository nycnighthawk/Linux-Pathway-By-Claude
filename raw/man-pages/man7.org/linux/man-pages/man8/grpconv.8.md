---
{"title": "pwconv(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/grpconv.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pwconv(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PWCONV(8)               System Management Commands              PWCONV(8)

## [](#NAME)NAME

           pwconv, pwunconv, grpconv, grpunconv - convert between the
           system's shadowed and plain account files

## [](#SYNOPSIS)SYNOPSIS

           pwconv [options]

           pwunconv [options]

           grpconv [options]

           grpunconv [options]

## [](#DESCRIPTION)DESCRIPTION

           The pwconv command creates shadow from passwd and an optionally
           existing shadow.

           The pwunconv command creates a plain passwd from shadowed passwd
           and shadow and then removes shadow.

           The grpconv command creates gshadow from group and an optionally
           existing gshadow.

           The grpunconv command creates plain group from shadowed group and
           gshadow and then removes gshadow.

           These four programs all operate on the normal and shadow password
           and group files: /etc/passwd, /etc/group, /etc/shadow, and
           /etc/gshadow.

           Each program acquires the necessary locks before conversion.
           pwconv and grpconv are similar. First, entries in the shadowed
           file which don't exist in the plain file are removed. Then,
           entries in the shadowed file which don't have `x' as the password
           in plain file are updated. Any missing shadowed entries are added.
           Finally, passwords in the plain file are replaced with `x'. These
           programs can be used for initial conversion as well to update the
           shadowed file if the plain file has been edited by hand.

           pwconv will use the values of PASS_MIN_DAYS, PASS_MAX_DAYS, and
           PASS_WARN_AGE from /etc/login.defs when adding new entries to
           /etc/shadow.

           Likewise pwunconv and grpunconv are similar. Passwords in the
           plain file are updated from the shadowed file. Entries which exist
           in the plain file but not in the shadowed file are left alone.
           Finally, the shadowed file is removed. Some password aging
           information is lost by pwunconv. It will convert what it can.

## [](#OPTIONS)OPTIONS

           The options which apply to the pwconv, pwunconv, grpconv, and
           grpunconv commands are:

           -h, --help
               Display help message and exit.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

## [](#BUGS)BUGS

           Errors in the password or group files (such as invalid or
           duplicate entries) may cause these programs to loop forever or
           fail in other strange ways. Please run pwck and grpck to correct
           any such errors before converting to or from shadowed files.

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variable in /etc/login.defs changes
           the behavior of grpconv and grpunconv:

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

           The following configuration variables in /etc/login.defs change
           the behavior of pwconv:

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

           /etc/login.defs
               Shadow password suite configuration.

## [](#SEE_ALSO)SEE ALSO

           grpck(8), login.defs(5), pwck(8).

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

    shadow-utils 4.19.0             08/04/2026                      PWCONV(8)

------------------------------------------------------------------------

Pages that refer to this page: [gshadow(5)](../man5/gshadow.5.html),  [passwd(5)](../man5/passwd.5.html),  [passwd(5@@shadow-utils)](../man5/passwd.5@@shadow-utils.html),  [shadow(5)](../man5/shadow.5.html)

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
