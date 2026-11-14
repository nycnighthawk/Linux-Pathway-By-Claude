---
{"title": "pam_debug(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_debug.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_debug(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_DEBUG(8)                 Linux-PAM Manual                PAM_DEBUG(8)

## [](#NAME)NAME

           pam_debug - PAM module to debug the PAM stack

## [](#SYNOPSIS)SYNOPSIS

           pam_debug.so [auth=value] [cred=value] [acct=value]
                        [prechauthtok=value] [chauthtok=value] [auth=value]
                        [open_session=value] [close_session=value]

## [](#DESCRIPTION)DESCRIPTION

           The pam_debug PAM module is intended as a debugging aide for
           determining how the PAM stack is operating. This module returns
           what its module arguments tell it to return.

## [](#OPTIONS)OPTIONS

           auth=value
               The pam_sm_authenticate(3) function will return value.

           cred=value
               The pam_sm_setcred(3) function will return value.

           acct=value
               The pam_sm_acct_mgmt(3) function will return value.

           prechauthtok=value
               The pam_sm_chauthtok(3) function will return value if the
               PAM_PRELIM_CHECK flag is set.

           chauthtok=value
               The pam_sm_chauthtok(3) function will return value if the
               PAM_PRELIM_CHECK flag is not set.

           open_session=value
               The pam_sm_open_session(3) function will return value.

           close_session=value
               The pam_sm_close_session(3) function will return value.

           Where value can be one of: success, open_err, symbol_err,
           service_err, system_err, buf_err, perm_denied, auth_err,
           cred_insufficient, authinfo_unavail, user_unknown, maxtries,
           new_authtok_reqd, acct_expired, session_err, cred_unavail,
           cred_expired, cred_err, no_module_data, conv_err, authtok_err,
           authtok_recover_err, authtok_lock_busy, authtok_disable_aging,
           try_again, ignore, abort, authtok_expired, module_unknown,
           bad_item, conv_again, incomplete.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (auth, account, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               Default return code if no other value was specified, else
               specified return value.

## [](#EXAMPLES)EXAMPLES

               auth    requisite       pam_permit.so
               auth    [success=2 default=ok]  pam_debug.so auth=perm_denied cred=success
               auth    [default=reset]         pam_debug.so auth=success cred=perm_denied
               auth    [success=done default=die] pam_debug.so
               auth    optional        pam_debug.so auth=perm_denied cred=perm_denied
               auth    sufficient      pam_debug.so auth=success cred=success

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_debug was written by Andrew G. Morgan <morgan@kernel.org>.

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

    Linux-PAM                       08/04/2026                   PAM_DEBUG(8)

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
