---
{"title": "default_contexts(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/default_contexts.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# default_contexts(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    default_contexts(5)       SELinux configuration       default_contexts(5)

## [](#NAME)NAME

           default_contexts - The SELinux default contexts configuration file

## [](#DESCRIPTION)DESCRIPTION

           The default contexts configuration file default_contexts contains
           entries that allow SELinux-aware login applications such as PAM(8)

           SELinux-aware login applications generally use one or more of the
           following libselinux functions that read these files from the
           active policy path:
                  get_default_context(3)
                  get_ordered_context_list(3)
                  get_ordered_context_list_with_level(3)
                  get_default_context_with_level(3)
                  get_default_context_with_role(3)
                  get_default_context_with_rolelevel(3)
                  query_user_context(3)
                  manual_user_enter_context(3)

           The default context configuration file path for the active policy
           is returned by selinux_default_contexts_path(3). The default,
           default contexts file is:
                  /etc/selinux/{SELINUXTYPE}/contexts/default_contexts

           Where {SELINUXTYPE} is the entry from the selinux configuration
           file config (see selinux_config(5)).

## [](#FILE_FORMAT)FILE FORMAT

           Each line in the default configuration file consists of the
           following:
                  login_process user_login_process [user_login_process] ...

           Where:
                  login_process
                         This consists of a role:type[:range] entry that
                         represents the login process context that are
                         defined in the policy.
                  user_login_process
                         This consists of one or more role:type[:range]
                         entries that represent the user login process
                         context defined in the policy.

## [](#EXAMPLE)EXAMPLE

           # ./contexts/default_contexts
           system_r:crond_t:s0            system_r:system_crond_t:s0
           system_r:local_login_t:s0      user_r:user_t:s0 staff_r:staff_t:s0
           system_r:remote_login_t:s0     user_r:user_t:s0
           system_r:sshd_t:s0             user_r:user_t:s0
           system_r:sulogin_t:s0          sysadm_r:sysadm_t:s0
           system_r:xdm_t:s0              user_r:user_t:s0

## [](#SEE_ALSO)SEE ALSO

           selinux(8), selinux_default_contexts_path(3), PAM(8),
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

    Security Enhanced Linux        28-Nov-2011            default_contexts(5)

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
