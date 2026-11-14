---
{"title": "pam_ftp(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_ftp.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_ftp(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_FTP(8)                   Linux-PAM Manual                  PAM_FTP(8)

## [](#NAME)NAME

           pam_ftp - PAM module for anonymous access module

## [](#SYNOPSIS)SYNOPSIS

           pam_ftp.so [debug] [ignore] [users=XXX,YYY,...]

## [](#DESCRIPTION)DESCRIPTION

           pam_ftp is a PAM module which provides a pluggable anonymous ftp
           mode of access.

           This module intercepts the user's name and password. If the name
           is ftp or anonymous, the user's password is broken up at the @
           delimiter into a PAM_RUSER and a PAM_RHOST part; these pam-items
           being set accordingly. The username (PAM_USER) is set to ftp. In
           this case the module succeeds. Alternatively, the module sets the
           PAM_AUTHTOK item with the entered password and fails.

           This module is not safe and easily spoofable.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

           ignore
               Pay no attention to the email address of the user (if
               supplied).

           ftp=XXX,YYY,...
               Instead of ftp or anonymous, provide anonymous login to the
               comma separated list of users: XXX,YYY,.... Should the
               applicant enter one of these usernames the returned username
               is set to the first in the list: XXX.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the auth module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The authentication was successful.

           PAM_USER_UNKNOWN
               User not known.

## [](#EXAMPLES)EXAMPLES

           Add the following line to /etc/pam.d/ftpd to handle ftp style
           anonymous login:

               #
               # ftpd; add ftp-specifics. These lines enable anonymous ftp over
               #       standard UN*X access (the listfile entry blocks access to
               #       users listed in /etc/ftpusers)
               #
               auth    sufficient  pam_ftp.so
               auth    required    pam_unix.so use_first_pass
               auth    required    pam_listfile.so \
                          onerr=succeed item=user sense=deny file=/etc/ftpusers

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_ftp was written by Andrew G. Morgan <morgan@kernel.org>.

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

    Linux-PAM                       08/04/2026                     PAM_FTP(8)

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
