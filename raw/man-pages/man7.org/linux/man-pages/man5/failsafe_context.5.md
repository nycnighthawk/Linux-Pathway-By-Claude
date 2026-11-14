---
{"title": "failsafe_context(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/failsafe_context.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# failsafe_context(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    failsafe_context(5)       SELinux configuration       failsafe_context(5)

## [](#NAME)NAME

           failsafe_context - The SELinux fail safe context configuration
           file

## [](#DESCRIPTION)DESCRIPTION

           The failsafe_context file allows SELinux-aware applications such
           as PAM(8) to obtain a known valid login context for an
           administrator if no valid default entries can be found elsewhere.

           selinux_failsafe_context_path(3) will return the active policy
           path to this file. The default failsafe context file is:
                  /etc/selinux/{SELINUXTYPE}/contexts/failsafe_context

           Where {SELINUXTYPE} is the entry from the selinux configuration
           file config (see selinux_config(5)).

           The following functions read this file from the active policy path
           if they cannot obtain a default context:
                  get_default_context(3)
                  get_ordered_context_list(3)
                  get_ordered_context_list_with_level(3)
                  get_default_context_with_level(3)
                  get_default_context_with_role(3)
                  get_default_context_with_rolelevel(3)
                  query_user_context(3)
                  manual_user_enter_context(3)

## [](#FILE_FORMAT)FILE FORMAT

           The file consists of a single line entry as follows:
                  role:type[:range]

           Where:
                  role type range
                         A role, type and optional range (for MCS/MLS),
                         separated by colons (:) to form a valid login
                         process context for an administrator to access the
                         system.

## [](#EXAMPLE)EXAMPLE

           # ./contexts/failsafe_context
           unconfined_r:unconfined_t:s0

## [](#SEE_ALSO)SEE ALSO

           selinux(8), selinux_failsafe_context_path(3), PAM(8),
           selinux_default_type_path(3), get_default_context(3),
           get_ordered_context_list(3),
           get_ordered_context_list_with_level(3),
           get_default_context_with_level(3),
           get_default_context_with_role(3),
           get_default_context_with_rolelevel(3), query_user_context(3),
           manual_user_enter_context(3), selinux_config(5)

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

    Security Enhanced Linux        28-Nov-2011            failsafe_context(5)

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
