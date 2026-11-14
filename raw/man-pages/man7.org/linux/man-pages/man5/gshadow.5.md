---
{"title": "gshadow(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/gshadow.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gshadow(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GSHADOW(5)            File Formats and Configuration           GSHADOW(5)

## [](#NAME)NAME

           gshadow - shadowed group file

## [](#DESCRIPTION)DESCRIPTION

           /etc/gshadow contains the shadowed information for group accounts.

           This file must not be readable by regular users if password
           security is to be maintained.

           Each line of this file contains the following colon-separated
           fields:

           group name
               It must be a valid group name, which exists on the system.

           encrypted password
               Refer to crypt(3) for details on how this string is
               interpreted.

               If the password field contains some string that is not a valid
               result of crypt(3), for instance ! or *, users will not be
               able to use a unix password to access the group (but group
               members do not need the password).

               The password is used when a user who is not a member of the
               group wants to gain the permissions of this group (see
               newgrp(1)).

               This field may be empty, in which case only the group members
               can gain the group permissions.

               A password field which starts with an exclamation mark means
               that the password is locked. The remaining characters on the
               line represent the password field before the password was
               locked.

               This password supersedes any password specified in /etc/group.

           administrators
               It must be a comma-separated list of user names.

               Administrators can change the password or the members of the
               group.

               Administrators also have the same permissions as the members
               (see below).

           members
               It must be a comma-separated list of user names.

               Members can access the group without being prompted for a
               password.

               You should use the same list of users as in /etc/group.

## [](#FILES)FILES

           /etc/group
               Group account information.

           /etc/gshadow
               Secure group account information.

## [](#SEE_ALSO)SEE ALSO

           gpasswd(5), group(5), grpck(8), grpconv(8), newgrp(1).

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

    shadow-utils 4.19.0             08/04/2026                     GSHADOW(5)

------------------------------------------------------------------------

Pages that refer to this page: [gpasswd(1)](../man1/gpasswd.1.html),  [newgrp(1)](../man1/newgrp.1.html),  [sg(1)](../man1/sg.1.html),  [group(5)](../man5/group.5.html),  [grpck(8)](../man8/grpck.8.html),  [vipw(8)](../man8/vipw.8.html)

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
