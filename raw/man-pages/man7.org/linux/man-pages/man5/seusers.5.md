---
{"title": "seusers(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/seusers.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# seusers(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    seusers(5)                SELinux configuration                seusers(5)

## [](#NAME)NAME

           seusers - The SELinux GNU/Linux user to SELinux user mapping
           configuration file

## [](#DESCRIPTION)DESCRIPTION

           The seusers file contains a list GNU/Linux user to SELinux user
           mapping for use by SELinux-aware login applications such as
           PAM(8).

           selinux_usersconf_path(3) will return the active policy path to
           this file. The default SELinux users mapping file is located at:
                  /etc/selinux/{SELINUXTYPE}/seusers

           Where {SELINUXTYPE} is the entry from the selinux configuration
           file config (see selinux_config(5)).

           getseuserbyname(3) reads this file to map a GNU/Linux user or
           group to an SELinux user.

## [](#FILE_FORMAT)FILE FORMAT

           Each line of the seusers configuration file consists of the
           following:

                  [%group_id]|[user_id]:seuser_id[:range]

           Where:
                  group_id|user_id
                         The  GNU/Linux user id, or if preceded by the
                         percentage (%) symbol, then a GNU/Linux group id.
                         An optional entry set to __default__ can be provided
                         as a fall back if required.
                  seuser_id
                         The SELinux  user identity.
                  range
                         The optional level or range for an MLS/MCS policy.

## [](#EXAMPLE)EXAMPLE

           # ./seusers
           system_u:system_u:s0-s15:c0.c255
           root:root:s0-s15:c0.c255
           fred:user_u:s0
           __default__:user_u:s0
           %user_group:user_u:s0

## [](#SEE_ALSO)SEE ALSO

           selinux(8), PAM(8), selinux_usersconf_path(3), getseuserbyname(3),
           selinux_config(5)

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Security Enhanced Linux        28-Nov-2011                     seusers(5)

------------------------------------------------------------------------

Pages that refer to this page: [selinux_config(5)](../man5/selinux_config.5.html)

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
