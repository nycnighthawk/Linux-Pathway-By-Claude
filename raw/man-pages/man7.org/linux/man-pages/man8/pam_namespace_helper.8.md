---
{"title": "pam_namespace_helper(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_namespace_helper.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_namespace_helper(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_NAMESPACE_HELPER(8)      Linux-PAM Manual     PAM_NAMESPACE_HELPER(8)

## [](#NAME)NAME

           pam_namespace_helper - Helper binary that creates home directories

## [](#SYNOPSIS)SYNOPSIS

           pam_namespace_helper

## [](#DESCRIPTION)DESCRIPTION

           pam_namespace_helper is a helper program for the pam_namespace
           module that sets up a private namespace for a session with
           polyinstantiated directories. The helper ensures that the
           namespace mount points exist before they are started to be used
           for the polyinstantiated directories. Mount points for home
           directories (lines with $HOME) are not created.

           pam_namespace_helper should be run by systemd at system startup.
           It should also be run by the administrator after defining the
           polyinstantiated directories but before enabling them.

## [](#SEE_ALSO)SEE ALSO

           pam_namespace(8)

## [](#AUTHOR)AUTHOR

           Written by Topi Miettinen.

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

    Linux-PAM                       08/04/2026        PAM_NAMESPACE_HELPER(8)

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
