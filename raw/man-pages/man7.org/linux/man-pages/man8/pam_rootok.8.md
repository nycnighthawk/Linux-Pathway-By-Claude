---
{"title": "pam_rootok(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_rootok.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_rootok(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_ROOTOK(8)                Linux-PAM Manual               PAM_ROOTOK(8)

## [](#NAME)NAME

           pam_rootok - Gain only root access

## [](#SYNOPSIS)SYNOPSIS

           pam_rootok.so [debug]

## [](#DESCRIPTION)DESCRIPTION

           pam_rootok is a PAM module that authenticates the user if their
           UID is 0. Applications that are created setuid-root generally
           retain the UID of the user but run with the authority of an
           enhanced effective-UID. It is the real UID that is checked.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The auth, account and password module types are provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The UID is 0.

           PAM_AUTH_ERR
               The UID is not 0.

## [](#EXAMPLES)EXAMPLES

           In the case of the su(1) application the historical usage is to
           permit the superuser to adopt the identity of a lesser user
           without the use of a password. To obtain this behavior with PAM
           the following pair of lines are needed for the corresponding entry
           in the /etc/pam.d/su configuration file:

               # su authentication. Root is granted access by default.
               auth  sufficient   pam_rootok.so
               auth  required     pam_unix.so

## [](#SEE_ALSO)SEE ALSO

           su(1), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_rootok was written by Andrew G. Morgan, <morgan@kernel.org>.

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

    Linux-PAM                       08/04/2026                  PAM_ROOTOK(8)

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
