---
{"title": "load_policy(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/load_policy.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# load_policy(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LOAD_POLICY(8)           System Manager's Manual           LOAD_POLICY(8)

## [](#NAME)NAME

           load_policy - load a new SELinux policy into the kernel

## [](#SYNOPSIS)SYNOPSIS

           load_policy [-qi]

## [](#DESCRIPTION)DESCRIPTION

           load_policy loads the installed policy file into the kernel.  The
           existing policy boolean values are automatically preserved across
           policy reloads rather than being reset to the default values in
           the policy file.

## [](#OPTIONS)OPTIONS

           -q     suppress warning messages.

           -i     initial policy load. Only use this if this is the first
                  time policy is being loaded since boot (usually called from
                  initramfs).

## [](#EXIT_STATUS)EXIT STATUS

           0      Success

           1      Invalid option

           2      Policy load failed

           3      Initial policy load failed and enforcing mode requested

## [](#SEE_ALSO)SEE ALSO

           booleans(8)

## [](#AUTHORS)AUTHORS

           This manual page was written by Dan Walsh <dwalsh@redhat.com>.
           The program was written by Stephen Smalley <stephen.smalley.work@gmail.com>.

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

    Security Enhanced Linux          May 2003                  LOAD_POLICY(8)

------------------------------------------------------------------------

Pages that refer to this page: [booleans(8)](../man8/booleans.8.html),  [restorecon(8)](../man8/restorecon.8.html),  [setfiles(8)](../man8/setfiles.8.html)

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
