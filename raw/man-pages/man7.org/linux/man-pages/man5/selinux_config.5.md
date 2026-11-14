---
{"title": "selinux_config(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/selinux_config.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# selinux_config(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    selinux_config(5)       SELinux configuration file      selinux_config(5)

## [](#NAME)NAME

           config - The SELinux sub-system configuration file.

## [](#DESCRIPTION)DESCRIPTION

           The SELinux config file controls the state of SELinux regarding:

                  1.  The policy enforcement status - enforcing, permissive
                      or disabled.

                  2.  The policy name or type that forms a path to the policy
                      to be loaded and its supporting configuration files.

                  3.  How SELinux-aware login applications should behave if
                      no valid SELinux users are configured.

                  4.  Whether the system is to be relabeled or not.

           The entries controlling these functions are described in the FILE
           FORMAT section.

           The fully qualified path name of the SELinux configuration file is
           /etc/selinux/config.

           If the config file is missing or corrupt, then no SELinux policy
           is loaded (i.e. SELinux is disabled).

           The sestatus (8) command and the libselinux function selinux_path
           (3) will return the location of the config file.

## [](#FILE_FORMAT)FILE FORMAT

           The config file supports the following parameters:

                  SELINUX = enforcing | permissive | disabled
                  SELINUXTYPE = policy_name
                  REQUIRESEUSERS = 0 | 1
                  AUTORELABEL = 0 | 1

           Where:
           SELINUX
                  This entry can contain one of three values:

                         enforcing
                             SELinux security policy is enforced.

                         permissive
                             SELinux security policy is not enforced but logs
                             the warnings (i.e. the action is allowed to
                             proceed).

                         disabled
                             No SELinux policy is loaded.  This option was
                             used to disable SELinux completely, which is now
                             deprecated.  Use the selinux=0 kernel boot
                             option instead (see selinux(8)).

                  The entry can be determined using the sestatus(8) command
                  or selinux_getenforcemode(3).

           SELINUXTYPE
                  The policy_name entry is used to identify the policy type,
                  and becomes the directory name of where the policy and its
                  configuration files are located.

                  The entry can be determined using the sestatus(8) command
                  or selinux_getpolicytype(3).

                  The policy_name is relative to a path that is defined
                  within the SELinux subsystem that can be retrieved by using
                  selinux_path(3). An example entry retrieved by
                  selinux_path(3) is:
                         /etc/selinux/

                  The policy_name is then appended to this and becomes the
                  'policy root' location that can be retrieved by
                  selinux_policy_root_path(3). An example entry retrieved is:
                         /etc/selinux/targeted

                  The actual binary policy is located relative to this
                  directory and also has a policy name pre-allocated. This
                  information can be retrieved using
                  selinux_binary_policy_path(3). An example entry retrieved
                  by selinux_binary_policy_path(3) is:
                         /etc/selinux/targeted/policy/policy

                  The binary policy name has by convention the SELinux policy
                  version that it supports appended to it. The maximum policy
                  version supported by the kernel can be determined using the
                  sestatus(8) command or security_policyvers(3). An example
                  binary policy file with the version is:
                         /etc/selinux/targeted/policy/policy.24

           REQUIRESEUSERS
                  This optional entry can be used to fail a login if there is
                  no matching or default entry in the seusers(5) file or if
                  the seusers file is missing.

                  It is checked by getseuserbyname(3) that is called by
                  SELinux-aware login applications such as PAM(8).

                  If set to 0 or the entry missing:
                         getseuserbyname(3) will return the GNU / Linux user
                         name as the SELinux user.

                  If set to 1:
                         getseuserbyname(3) will fail.

                  The getseuserbyname(3) man page should be consulted for its
                  use. The format of the seusers file is shown in seusers(5).

           AUTORELABEL
                  This is an optional entry that allows the file system to be
                  relabeled.

                  If set to 0 and there is a file called .autorelabel in the
                  root directory, then on a reboot, the loader will drop to a
                  shell where a root login is required. An administrator can
                  then manually relabel the file system.

                  If set to 1 or no entry present (the default) and there is
                  a .autorelabel file in the root directory, then the file
                  system will be automatically relabeled using fixfiles -F
                  restore

                  In both cases the /.autorelabel file will be removed so
                  that relabeling is not done again.

## [](#EXAMPLE)EXAMPLE

           This example config file shows the minimum contents for a system
           to run SELinux in enforcing mode, with a policy_name of
           'targeted':

                  SELINUX = enforcing
                  SELINUXTYPE = targeted

## [](#SEE_ALSO)SEE ALSO

           selinux(8), sestatus(8), selinux_path(3),
           selinux_policy_root_path(3), selinux_binary_policy_path(3),
           getseuserbyname(3), PAM(8), fixfiles(8), selinux_mkload_policy(3),
           selinux_getpolicytype(3), security_policyvers(3),
           selinux_getenforcemode(3), seusers(5)

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

    Security Enhanced Linux        18 Nov 2011              selinux_config(5)

------------------------------------------------------------------------

Pages that refer to this page: [selinux_colors_path(3)](../man3/selinux_colors_path.3.html),  [customizable_types(5)](../man5/customizable_types.5.html),  [default_contexts(5)](../man5/default_contexts.5.html),  [default_type(5)](../man5/default_type.5.html),  [failsafe_context(5)](../man5/failsafe_context.5.html),  [removable_context(5)](../man5/removable_context.5.html),  [securetty_types(5)](../man5/securetty_types.5.html),  [selabel_db(5)](../man5/selabel_db.5.html),  [selabel_file(5)](../man5/selabel_file.5.html),  [selabel_media(5)](../man5/selabel_media.5.html),  [selabel_x(5)](../man5/selabel_x.5.html),  [service_seusers(5)](../man5/service_seusers.5.html),  [seusers(5)](../man5/seusers.5.html),  [user_contexts(5)](../man5/user_contexts.5.html),  [virtual_domain_context(5)](../man5/virtual_domain_context.5.html),  [virtual_image_context(5)](../man5/virtual_image_context.5.html)

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
