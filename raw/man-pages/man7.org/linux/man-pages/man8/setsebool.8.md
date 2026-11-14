---
{"title": "setsebool(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/setsebool.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setsebool(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setsebool(8)        SELinux Command Line documentation       setsebool(8)

## [](#NAME)NAME

           setsebool - set SELinux boolean value

## [](#SYNOPSIS)SYNOPSIS

           setsebool [ -PNV ] boolean value | bool1=val1 bool2=val2 ...

## [](#DESCRIPTION)DESCRIPTION

           setsebool sets the current state of a particular SELinux boolean
           or a list of booleans to a given value. The value may be 1 or true
           or on to enable the boolean, or 0 or false or off to disable it.

           Without the -P option, only the current boolean value is affected;
           the boot-time default settings are not changed.

           If the -P option is given, all pending values are written to the
           policy file on disk. So they will be persistent across reboots.

           If the -N option is given, the policy on disk is not reloaded into
           the kernel.

           If the -V option is given, verbose error messages will be printed
           from semanage libraries.

## [](#EXAMPLE)EXAMPLE

           Enable container_use_devices boolean (will return to persistent value after reboot)
           # setsebool container_use_devices 1
           Persistently enable samba_create_home_dirs and samba_enable_home_dirs booleans
           # setsebool -P samba_create_home_dirs=on samba_enable_home_dirs=on

## [](#AUTHOR)AUTHOR

           This manual page was written by Dan Walsh <dwalsh@redhat.com>.
           The program was written by Tresys Technology.

## [](#SEE_ALSO)SEE ALSO

           getsebool(8), booleans(8), togglesebool(8), semanage(8)

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

    dwalsh@redhat.com              11 Aug 2004                   setsebool(8)

------------------------------------------------------------------------

Pages that refer to this page: [booleans(8)](../man8/booleans.8.html),  [getsebool(8)](../man8/getsebool.8.html),  [selinux(8)](../man8/selinux.8.html),  [semanage-boolean(8)](../man8/semanage-boolean.8.html),  [sepolicy-booleans(8)](../man8/sepolicy-booleans.8.html),  [togglesebool(8)](../man8/togglesebool.8.html)

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
