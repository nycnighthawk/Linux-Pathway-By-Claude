---
{"title": "unix_chkpwd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/unix_chkpwd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# unix_chkpwd(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UNIX_CHKPWD(8)               Linux-PAM Manual              UNIX_CHKPWD(8)

## [](#NAME)NAME

           unix_chkpwd - Helper binary that verifies the password of the
           current user

## [](#SYNOPSIS)SYNOPSIS

           unix_chkpwd [...]

## [](#DESCRIPTION)DESCRIPTION

           unix_chkpwd is a helper program for the pam_unix module that
           verifies the password of the current user. It also checks password
           and account expiration dates in shadow. It is not intended to be
           run directly from the command line and logs a security violation
           if done so.

           It is typically installed setuid root or setgid shadow.

           The interface of the helper - command line options, and
           input/output data format are internal to the pam_unix module and
           it should not be called directly from applications.

## [](#SEE_ALSO)SEE ALSO

           pam_unix(8)

## [](#AUTHOR)AUTHOR

           Written by Andrew Morgan and other various people.

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

    Linux-PAM                       08/04/2026                 UNIX_CHKPWD(8)

------------------------------------------------------------------------

Pages that refer to this page: [pam_unix(8)](../man8/pam_unix.8.html)

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
