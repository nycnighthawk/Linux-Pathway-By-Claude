---
{"title": "user_contexts(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/user_contexts.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# user_contexts(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    user_contexts(5)          SELinux configuration          user_contexts(5)

## [](#NAME)NAME

           user_contexts - The SELinux user contexts configuration files

## [](#DESCRIPTION)DESCRIPTION

           These optional user context configuration files contain entries
           that allow SELinux-aware login applications such as PAM(8)
           (running in their own process context), to determine the context
           that a users login session should run under.

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

           There can be one file for each SELinux user configured on the
           system. The file  path is formed using the path returned by
           selinux_user_contexts_path(3) for the active policy, with the
           SELinux user name appended, for example:
                  /etc/selinux/{SELINUXTYPE}/contexts/users/unconfined_u
                  /etc/selinux/{SELINUXTYPE}/contexts/users/xguest_u

           Where {SELINUXTYPE} is the entry from the selinux configuration
           file config (see selinux_config(5)).

           These files contain context information as described in the FILE
           FORMAT section.

## [](#FILE_FORMAT)FILE FORMAT

           Each line in the user context configuration file consists of the
           following:
                  login_process user_login_process

           Where:
                  login_process
                         This consists of a role:type[:range] entry that
                         represents the login process context.
                  user_login_process
                         This consists of a role:type[:range] entry that
                         represents the user login process context.

## [](#EXAMPLE)EXAMPLE

           # Example for xguest_u at
           /etc/selinux/targeted/contexts/users/xguest_u
           system_r:crond_t:s0           xguest_r:xguest_t:s0
           system_r:initrc_t:s0          xguest_r:xguest_t:s0
           system_r:local_login_t:s0     xguest_r:xguest_t:s0
           system_r:remote_login_t:s0    xguest_r:xguest_t:s0
           system_r:sshd_t:s0            xguest_r:xguest_t:s0
           system_r:xdm_t:s0             xguest_r:xguest_t:s0
           xguest_r:xguest_t:s0          xguest_r:xguest_t:s0

## [](#SEE_ALSO)SEE ALSO

           selinux(8), selinux_user_contexts_path(3), PAM(8),
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

    Security Enhanced Linux        28-Nov-2011               user_contexts(5)

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
