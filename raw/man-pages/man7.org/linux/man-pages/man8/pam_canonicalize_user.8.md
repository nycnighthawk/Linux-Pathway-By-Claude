---
{"title": "pam_canonicalize_user(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_canonicalize_user.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_canonicalize_user(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_CANONICALIZE_USE(8)      Linux-PAM Manual     PAM_CANONICALIZE_USE(8)

## [](#NAME)NAME

           pam_canonicalize_user - Get user name and canonicalize it

## [](#SYNOPSIS)SYNOPSIS

           pam_canonicalize_user.so

## [](#DESCRIPTION)DESCRIPTION

           This PAM module uses the name of the user obtained via
           pam_get_user(3) as a key to query the password database, and
           replaces PAM_USER with the pw_name value that has been returned.

## [](#OPTIONS)OPTIONS

           This module does not recognise any options.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the auth module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_IGNORE
               The user name was set successfully.

           PAM_USER_UNKNOWN
               The user was not found.

           PAM_SYSTEM_ERR
               The application did not supply neither a user name nor a
               conversation method.

           PAM_INCOMPLETE
               The conversation method supplied by the application is waiting
               for an event.

           PAM_CONV_ERR
               The conversation method supplied by the application failed to
               obtain the user name.

           PAM_ABORT
               Error resuming an old conversation.

           PAM_BUF_ERR
               Memory buffer error.

## [](#EXAMPLES)EXAMPLES

           Prepend the PAM auth stack with the following line to canonicalize
           the user name before the authentication:

                       auth required pam_canonicalize_user.so

## [](#SEE_ALSO)SEE ALSO

           pam_get_user(3), pam_get_item(3), pam_set_item(3), getpwnam(3),
           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_canonicalize_user was written by Dmitry V. Levin
           <ldv@strace.io>.

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

    Linux-PAM                       08/04/2026        PAM_CANONICALIZE_USE(8)

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
