---
{"title": "pam_deny(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_deny.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_deny(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_DENY(8)                  Linux-PAM Manual                 PAM_DENY(8)

## [](#NAME)NAME

           pam_deny - The locking-out PAM module

## [](#SYNOPSIS)SYNOPSIS

           pam_deny.so

## [](#DESCRIPTION)DESCRIPTION

           This module can be used to deny access. It always indicates a
           failure to the application through the PAM framework. It might be
           suitable for using for default (the OTHER) entries.

## [](#OPTIONS)OPTIONS

           This module does not recognise any options.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (account, auth, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTH_ERR
               This is returned by the account and auth services.

           PAM_CRED_ERR
               This is returned by the setcred function.

           PAM_AUTHTOK_ERR
               This is returned by the password service.

           PAM_SESSION_ERR
               This is returned by the session service.

## [](#EXAMPLES)EXAMPLES

               #%PAM-1.0
               #
               # If we don't have config entries for a service, the
               # OTHER entries are used. To be secure, warn and deny
               # access to everything.
               other auth     required       pam_warn.so
               other auth     required       pam_deny.so
               other account  required       pam_warn.so
               other account  required       pam_deny.so
               other password required       pam_warn.so
               other password required       pam_deny.so
               other session  required       pam_warn.so
               other session  required       pam_deny.so

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_deny was written by Andrew G. Morgan <morgan@kernel.org>

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

    Linux-PAM                       08/04/2026                    PAM_DENY(8)

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
