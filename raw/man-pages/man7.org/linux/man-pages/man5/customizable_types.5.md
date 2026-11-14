---
{"title": "customizable_types(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/customizable_types.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# customizable_types(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    customizable_types(5)     SELinux configuration     customizable_types(5)

## [](#NAME)NAME

           customizable_types - The SELinux customizable types configuration
           file

## [](#DESCRIPTION)DESCRIPTION

           The customizable_types file contains a list of types that can be
           customised in some way by SELinux-aware applications.

           Generally this is a file context type that is usually set on files
           that need to be shared among certain domains and where the
           administrator wants to manually manage the type.

           The  use  of customizable types is deprecated as the preferred
           approach is to use semanage(8) fcontext(8) ...(8).  However,
           SELinux-aware applications such as setfiles(8) will use this
           information to obtain a list of types relating to files that
           should not be relabeled.

           selinux_customizable_types_path(3) will return the active policy
           path to this file. The default customizable types file is:
                  /etc/selinux/{SELINUXTYPE}/contexts/customizable_types

           Where {SELINUXTYPE} is the entry from the selinux configuration
           file config (see selinux_config(5)).

           is_context_customizable(3) reads this file to determine if a
           context is customisable or not for the active policy.

## [](#FILE_FORMAT)FILE FORMAT

           Each line in the file consists of the following:
                  type

           Where:
                  type
                         The type defined in the policy that can be
                         customised.

## [](#EXAMPLE)EXAMPLE

           # ./contexts/customizable_types
           mount_loopback_t
           public_content_rw_t
           public_content_t
           swapfile_t
           sysadm_untrusted_content_t

## [](#SEE_ALSO)SEE ALSO

           selinux(8), selinux_customizable_types_path(3),
           is_context_customizable(3), semanage(8), setfiles(8),
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

    Security Enhanced Linux        28-Nov-2011          customizable_types(5)

------------------------------------------------------------------------

Pages that refer to this page: [restorecon(8)](../man8/restorecon.8.html)

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
