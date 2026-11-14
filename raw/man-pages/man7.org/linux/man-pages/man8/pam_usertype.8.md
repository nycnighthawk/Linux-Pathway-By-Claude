---
{"title": "pam_usertype(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_usertype.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_usertype(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_USERTYPE(8)              Linux-PAM Manual             PAM_USERTYPE(8)

## [](#NAME)NAME

           pam_usertype - check if the authenticated user is a system or
           regular account

## [](#SYNOPSIS)SYNOPSIS

           pam_usertype.so [flag...] {condition}

## [](#DESCRIPTION)DESCRIPTION

           pam_usertype.so is designed to succeed or fail authentication
           based on type of the account of the authenticated user. The type
           of the account is decided with help of SYS_UID_MAX settings in
           /etc/login.defs. One use is to select whether to load other
           modules based on this test.

           The module should be given only one condition as module argument.
           Authentication will succeed only if the condition is met.

## [](#OPTIONS)OPTIONS

           The following flags are supported:

           use_uid
               Evaluate conditions using the account of the user whose UID
               the application is running under instead of the user being
               authenticated.

           audit
               Log unknown users to the system log.

           Available conditions are:

           issystem
               Succeed if the user is a system user.

           isregular
               Succeed if the user is a regular user.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (account, auth, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The condition was true.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_CONV_ERR
               The conversation method supplied by the application failed to
               obtain the username.

           PAM_INCOMPLETE
               The conversation method supplied by the application returned
               PAM_CONV_AGAIN.

           PAM_AUTH_ERR
               The condition was false.

           PAM_SERVICE_ERR
               A service error occurred or the arguments can't be parsed
               correctly.

           PAM_USER_UNKNOWN
               User was not found.

## [](#EXAMPLES)EXAMPLES

           Skip remaining modules if the user is a system user:

               account sufficient pam_usertype.so issystem

## [](#SEE_ALSO)SEE ALSO

           login.defs(5), pam(8)

## [](#AUTHOR)AUTHOR

           Pavel Březina <pbrezina@redhat.com>

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

    Linux-PAM                       08/04/2026                PAM_USERTYPE(8)

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
