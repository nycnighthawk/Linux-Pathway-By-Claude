---
{"title": "removable_context(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/removable_context.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# removable_context(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    removable_context(5)      SELinux configuration      removable_context(5)

## [](#NAME)NAME

           removable_context - The SELinux removable devices context
           configuration file

## [](#DESCRIPTION)DESCRIPTION

           This file contains the default label that should be used for
           removable devices.

           selinux_removable_context_path(3) will return the active policy
           path to this file. The default removable context file is:
                  /etc/selinux/{SELINUXTYPE}/contexts/removable_context

           Where {SELINUXTYPE} is the entry from the selinux configuration
           file config (see selinux_config(5)).

## [](#FILE_FORMAT)FILE FORMAT

           The file consists of a single line entry as follows:
                  user:role:type[:range]

           Where:
                  user role type range
                         A user, role, type and optional range (for MCS/MLS)
                         separated by colons (:) that will be applied to
                         removable devices.

## [](#EXAMPLE)EXAMPLE

           # ./contexts/removable_contexts
           system_u:object_r:removable_t:s0

## [](#SEE_ALSO)SEE ALSO

           selinux(8), selinux_removable_context_path(3), selinux_config(5)

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

    Security Enhanced Linux        28-Nov-2011           removable_context(5)

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
