---
{"title": "securetty_types(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/securetty_types.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# securetty_types(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    securetty_types(5)        SELinux configuration        securetty_types(5)

## [](#NAME)NAME

           securetty_types - The SELinux secure tty type configuration file

## [](#DESCRIPTION)DESCRIPTION

           The securetty_types file contains a list of types associated to
           secure tty type that are defined in the policy for use by SELinux-
           aware applications.

           selinux_securetty_types_path(3) will return the active policy path
           to this file. The default securetty types file is:
                  /etc/selinux/{SELINUXTYPE}/contexts/securetty_types

           Where {SELINUXTYPE} is the entry from the selinux configuration
           file config (see selinux_config(5)).

           selinux_check_securetty_context(3) reads this file to determine if
           a context is for a secure tty defined in the active policy.

           SELinux-aware applications such as newrole(1) use this information
           to check the status of a tty.

## [](#FILE_FORMAT)FILE FORMAT

           Each line in the file consists of the following entry:

                  type
                         One or more type entries that are defined in the
                         policy for secure tty devices.

## [](#EXAMPLE)EXAMPLE

           # ./contexts/securetty_types
           sysadm_tty_device_t
           user_tty_device_t
           staff_tty_device_t

## [](#SEE_ALSO)SEE ALSO

           selinux(8), selinux_securetty_types_path(3), newrole(1),
           selinux_check_securetty_context(3), selinux_config(5)

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

    Security Enhanced Linux        28-Nov-2011             securetty_types(5)

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
