---
{"title": "group(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/group.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# group(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    group(5)                   File Formats Manual                   group(5)

## [](#NAME)NAME

           group - user group file

## [](#DESCRIPTION)DESCRIPTION

           The /etc/group file is a text file that defines the groups on the
           system.  There is one entry per line, with the following format:

               group_name:password:GID:user_list

           The fields are as follows:

           group_name
                  the name of the group.

           password
                  the (encrypted) group password.  If this field is empty, no
                  password is needed.

           GID    the numeric group ID.

           user_list
                  a list of the usernames that are members of this group,
                  separated by commas.

## [](#FILES)FILES

           /etc/group

## [](#BUGS)BUGS

           As the 4.2BSD initgroups(3) man page says: no one seems to keep
           /etc/group up-to-date.

## [](#SEE_ALSO)SEE ALSO

           chgrp(1), gpasswd(1), groups(1), login(1), newgrp(1), sg(1),
           getgrent(3), getgrnam(3), gshadow(5), passwd(5), vigr(8)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2025-05-17                       group(5)

------------------------------------------------------------------------

Pages that refer to this page: [gpasswd(1)](../man1/gpasswd.1.html),  [indomcachectl(1)](../man1/indomcachectl.1.html),  [lslogins(1)](../man1/lslogins.1.html),  [newgrp(1)](../man1/newgrp.1.html),  [sg(1)](../man1/sg.1.html),  [fgetgrent(3)](../man3/fgetgrent.3.html),  [getgrent(3)](../man3/getgrent.3.html),  [getgrent_r(3)](../man3/getgrent_r.3.html),  [getgrnam(3)](../man3/getgrnam.3.html),  [getgrouplist(3)](../man3/getgrouplist.3.html),  [group_member(3)](../man3/group_member.3.html),  [putgrent(3)](../man3/putgrent.3.html),  [gshadow(5)](../man5/gshadow.5.html),  [passwd(5)](../man5/passwd.5.html),  [rpm-config(5)](../man5/rpm-config.5.html),  [credentials(7)](../man7/credentials.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [grpck(8)](../man8/grpck.8.html),  [nscd(8)](../man8/nscd.8.html),  [pwck(8)](../man8/pwck.8.html),  [rpm(8)](../man8/rpm.8.html),  [rpm-common(8)](../man8/rpm-common.8.html),  [vipw(8)](../man8/vipw.8.html)

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
