---
{"title": "booleans(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/booleans.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# booleans(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    booleans(8)         SELinux Command Line documentation        booleans(8)

## [](#NAME)NAME

           booleans - Policy booleans enable runtime customization of SELinux
           policy

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes SELinux policy booleans.  The SELinux
           policy can include conditional rules that are enabled or disabled
           based on the current values of a set of policy booleans.  These
           policy booleans allow runtime modification of the security policy
           without having to load a new policy.

           For example, the boolean httpd_enable_cgi allows the httpd daemon
           to run cgi scripts if it is enabled.  If the administrator does
           not want to allow execution of cgi scripts, he can simply disable
           this boolean value.

           The policy defines a default value for each boolean, typically
           false.  These default values can be overridden via local settings
           created via the setsebool(8) utility, using -P to make the setting
           persistent across reboots.  The system-config-securitylevel tool
           provides a graphical interface for altering the settings.  The
           load_policy(8) program will preserve current boolean settings upon
           a policy reload by default, or can optionally reset booleans to
           the boot-time defaults via the -b option.

           Boolean values can be listed by using the getsebool(8) utility and
           passing it the -a option.

           Boolean values can also be changed at runtime via the setsebool(8)
           utility or the togglesebool(8) utility.  By default, these
           utilities only change the current boolean value and do not affect
           the persistent settings, unless the -P option is used to
           setsebool.

## [](#AUTHOR)AUTHOR

           This manual page was written by Dan Walsh <dwalsh@redhat.com>.
           The SELinux conditional policy support was developed by Tresys
           Technology.

## [](#SEE_ALSO)SEE ALSO

           getsebool(8), setsebool(8), selinux(8), togglesebool(8)

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

    dwalsh@redhat.com              11 Aug 2004                    booleans(8)

------------------------------------------------------------------------

Pages that refer to this page: [security_load_booleans(3)](../man3/security_load_booleans.3.html),  [getsebool(8)](../man8/getsebool.8.html),  [load_policy(8)](../man8/load_policy.8.html),  [selinux(8)](../man8/selinux.8.html),  [setsebool(8)](../man8/setsebool.8.html),  [togglesebool(8)](../man8/togglesebool.8.html)

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
