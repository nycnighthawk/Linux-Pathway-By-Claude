---
{"title": "togglesebool(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/togglesebool.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# togglesebool(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    togglesebool(8)     SELinux Command Line documentation    togglesebool(8)

## [](#NAME)NAME

           togglesebool - flip the current value of a SELinux boolean

## [](#SYNOPSIS)SYNOPSIS

           togglesebool boolean...

## [](#DESCRIPTION)DESCRIPTION

           togglesebool flips the current value of a list of booleans. If the
           value is currently a 1, then it will be changed to a 0 and vice
           versa. Only the "in memory" values are changed; the boot-time
           settings are unaffected.

## [](#AUTHOR)AUTHOR

           This man page was written by Steve Grubb <sgrubb@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           selinux(8), booleans(8), getsebool(8), setsebool(8)

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

    sgrubb@redhat.com              26 Oct 2004                togglesebool(8)

------------------------------------------------------------------------

Pages that refer to this page: [security_load_booleans(3)](../man3/security_load_booleans.3.html),  [booleans(8)](../man8/booleans.8.html),  [selinux(8)](../man8/selinux.8.html),  [setsebool(8)](../man8/setsebool.8.html)

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
