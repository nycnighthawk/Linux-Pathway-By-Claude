---
{"title": "pam_stress(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_stress.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_stress(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_STRESS(8)                Linux-PAM Manual               PAM_STRESS(8)

## [](#NAME)NAME

           pam_stress - The stress-testing PAM module

## [](#SYNOPSIS)SYNOPSIS

           pam_stress.so [debug] [no_warn] [use_first_pass] [try_first_pass]
                         [rootok] [expired] [fail_1] [fail_2] [prelim]
                         [required]

## [](#DESCRIPTION)DESCRIPTION

           The pam_stress PAM module is mainly intended to give the
           impression of failing as a fully functioning module might.

## [](#OPTIONS)OPTIONS

           debug
               Put lots of information in syslog. *NOTE* this option writes
               passwords to syslog, so don't use anything sensitive when
               testing.

           no_warn
               Do not give warnings about things (otherwise warnings are
               issued via the conversation function)

           use_first_pass
               Do not prompt for a password, for pam_sm_authentication
               function just use item PAM_AUTHTOK.

           try_first_pass
               Do not prompt for a password unless there has been no previous
               authentication token (item PAM_AUTHTOK is NULL)

           rootok
               This is intended for the pam_sm_chauthtok function and it
               instructs this function to permit root to change the user's
               password without entering the old password.

           expired
               An argument intended for the account and chauthtok module
               parts. It instructs the module to act as if the user's
               password has expired

           fail_1
               This instructs the module to make its first function fail.

           fail_2
               This instructs the module to make its second function (if
               there is one) fail.

           prelim
               For pam_sm_chauthtok, means fail on PAM_PRELIM_CHECK.

           required
               For pam_sm_chauthtok, means fail if the user hasn't already
               been authenticated by this module. (See stress_new_pwd data
               string in the NOTES.)

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (auth, account, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_BUF_ERR
               Memory buffer error.

           PAM_PERM_DENIED
               Permission denied.

           PAM_AUTH_ERR
               Access to the system was denied.

           PAM_CONV_ERR
               Conversation failure.

           PAM_SUCCESS
               The function passes all checks.

           PAM_USER_UNKNOWN
               The user is not known to the system.

           PAM_CRED_ERR
               Failure involving user credentials.

           PAM_NEW_AUTHTOK_REQD
               Authentication token is no longer valid; new one required.

           PAM_SESSION_ERR
               Session failure.

           PAM_TRY_AGAIN
               Failed preliminary check by service.

           PAM_AUTHTOK_LOCK_BUSY
               Authentication token lock busy.

           PAM_AUTHTOK_ERR
               Authentication token manipulation error.

           PAM_SYSTEM_ERR
               System error.

## [](#NOTES)NOTES

           This module uses the stress_new_pwd data string which tells
           pam_sm_chauthtok that pam_sm_acct_mgmt says we need a new
           password. The only possible value for this data string is 'yes'.

## [](#EXAMPLES)EXAMPLES

               #%PAM-1.0
               #
               # Any of the following will suffice
               account  required pam_stress.so
               auth     required pam_stress.so
               password required pam_stress.so
               session  required pam_stress.so

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8).

## [](#AUTHORS)AUTHORS

           The pam_stress PAM module was developed by Andrew Morgan
           <morgan@linux.kernel.org>. The man page for pam_stress was written
           by Lucas Ramage <ramage.lucas@protonmail.com>.

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

    Linux-PAM                       08/04/2026                  PAM_STRESS(8)

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
