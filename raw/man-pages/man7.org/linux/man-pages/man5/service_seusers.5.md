---
{"title": "service_seusers(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/service_seusers.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# service_seusers(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    service_seusers(5)        SELinux configuration        service_seusers(5)

## [](#NAME)NAME

           service_seusers - The SELinux GNU/Linux user and service to
           SELinux user mapping configuration files

## [](#DESCRIPTION)DESCRIPTION

           These are optional files that allow services to define an SELinux
           user when authenticating via SELinux-aware login applications such
           as PAM(8).

           There is one file for each GNU/Linux user name that will be
           required to run a service with a specific SELinux user name.

           The path for each configuration file is formed by the path
           returned by selinux_policy_root(3) with /logins/username appended
           (where username is a file representing the GNU/Linux user name).
           The default services directory is located at:
                  /etc/selinux/{SELINUXTYPE}/logins

           Where {SELINUXTYPE} is the entry from the selinux configuration
           file config (see selinux_config(5)).

           getseuser(3) reads this file to map services to an SELinux user.

## [](#FILE_FORMAT)FILE FORMAT

           Each line within the username file is formatted as follows with
           each component separated by a colon:
                  service:seuser[:range]

           Where:
                  service
                         The service name used by the application.
                  seuser
                         The SELinux user name.
                  range
                         The range for MCS/MLS policies.

## [](#EXAMPLES)EXAMPLES

           Example 1 - for the 'root' user:
                  # ./logins/root
                  ipa:user_u:s0
                  this_service:unconfined_u:s0

           Example 2 - for GNU/Linux user 'rch':
                  # ./logins/rch
                  ipa:unconfined_u:s0
                  that_service:unconfined_u:s0

## [](#SEE_ALSO)SEE ALSO

           selinux(8), PAM(8), selinux_policy_root(3), getseuser(3),
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

    Security Enhanced Linux        28-Nov-2011             service_seusers(5)

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
