---
{"title": "newgrp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/newgrp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# newgrp(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NEWGRP(1)                     User Commands                     NEWGRP(1)

## [](#NAME)NAME

           newgrp - log in to a new group

## [](#SYNOPSIS)SYNOPSIS

           newgrp [-] [group]

## [](#DESCRIPTION)DESCRIPTION

           The newgrp command is used to change the current group ID during a
           login session. If the optional - flag is given, the user's
           environment will be reinitialized as though the user had logged
           in, otherwise the current environment, including current working
           directory, remains unchanged.

           newgrp changes the current real group ID to the named group, or to
           the default group listed in /etc/passwd if no group name is given.
           newgrp also tries to add the group to the user groupset. If not
           root, the user will be prompted for a password if she does not
           have a password (in /etc/shadow if this user has an entry in the
           shadowed password file, or in /etc/passwd otherwise) and the group
           does, or if the user is not listed as a member and the group has a
           password. The user will be denied access if the group password is
           empty and the user is not listed as a member.

           If there is an entry for this group in /etc/gshadow, then the list
           of members and the password of this group will be taken from this
           file, otherwise, the entry in /etc/group is considered.

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variables in /etc/login.defs change
           the behavior of this tool:

           SYSLOG_SG_ENAB (boolean)
               Enable "syslog" logging of sg activity.

## [](#FILES)FILES

           /etc/passwd
               User account information.

           /etc/shadow
               Secure user account information.

           /etc/group
               Group account information.

           /etc/gshadow
               Secure group account information.

## [](#SEE_ALSO)SEE ALSO

           id(1), login(1), su(1), sg(1), gpasswd(1), group(5), gshadow(5).

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

    shadow-utils 4.19.0             08/04/2026                      NEWGRP(1)

------------------------------------------------------------------------

Pages that refer to this page: [flock(1)](../man1/flock.1.html),  [gpasswd(1)](../man1/gpasswd.1.html),  [pmdammv(1)](../man1/pmdammv.1.html),  [sg(1)](../man1/sg.1.html),  [group(5)](../man5/group.5.html),  [gshadow(5)](../man5/gshadow.5.html),  [credentials(7)](../man7/credentials.7.html)

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
