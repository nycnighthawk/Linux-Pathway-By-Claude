---
{"title": "mkhomedir_helper(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mkhomedir_helper.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mkhomedir_helper(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MKHOMEDIR_HELPER(8)          Linux-PAM Manual         MKHOMEDIR_HELPER(8)

## [](#NAME)NAME

           mkhomedir_helper - Helper binary that creates home directories

## [](#SYNOPSIS)SYNOPSIS

           mkhomedir_helper {user}
                            [umask [ path-to-skel [ home_mode [ path-to-vendor-skel ] ] ]]

## [](#DESCRIPTION)DESCRIPTION

           mkhomedir_helper is a helper program for the pam_mkhomedir module
           that creates home directories and populates them with contents of
           the specified skel directory.

           The default value of umask is 0022 and the default value of
           path-to-skel is /etc/skel. The default value of home_mode is
           computed from the value of umask.

           path-to-vendor-skel doesn't have default value. When set to a
           path, home directory will be populated by contents of path-to-skel
           first, and then by contents of path.

           The helper is separated from the module to not require direct
           access from login SELinux domains to the contents of user home
           directories. The SELinux domain transition happens when the module
           is executing the mkhomedir_helper.

           The helper never touches home directories if they already exist.

## [](#SEE_ALSO)SEE ALSO

           pam_mkhomedir(8)

## [](#AUTHOR)AUTHOR

           Written by Tomas Mraz based on the code originally in
           pam_mkhomedir module.

## [](#COLOPHON)COLOPHON

           This page is part of the linux-pam (Pluggable Authentication
           Modules for Linux) project.  Information about the project can be
           found at ⟨http://www.linux-pam.org/⟩.  If you have a bug report
           for this manual page, see ⟨//www.linux-pam.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/linux-pam/linux-pam.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux-PAM                       08/04/2026            MKHOMEDIR_HELPER(8)

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
