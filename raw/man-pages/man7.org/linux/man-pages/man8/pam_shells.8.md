---
{"title": "pam_shells(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_shells.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_shells(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_SHELLS(8)                Linux-PAM Manual               PAM_SHELLS(8)

## [](#NAME)NAME

           pam_shells - PAM module to check for valid login shell

## [](#SYNOPSIS)SYNOPSIS

           pam_shells.so

## [](#DESCRIPTION)DESCRIPTION

           pam_shells is a PAM module that only allows access to the system
           if the user's shell is listed in /etc/shells.

           It also checks if needed files (e.g.  /etc/shells) are plain files
           and not world writable.

## [](#OPTIONS)OPTIONS

           This module does not recognise any options.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The auth and account module types are provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTH_ERR
               Access to the system was denied.

           PAM_SUCCESS
               The user's login shell was listed as valid shell in
               /etc/shells.

           PAM_USER_UNKNOWN
               The user does not exist or the user's login shell could not be
               determined.

           PAM_SERVICE_ERR
               The module was not able to get the name of the user.

## [](#EXAMPLES)EXAMPLES

               auth  required  pam_shells.so

## [](#SEE_ALSO)SEE ALSO

           shells(5), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_shells was written by Erik Troan <ewt@redhat.com>.

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

    Linux-PAM                       08/04/2026                  PAM_SHELLS(8)

------------------------------------------------------------------------

Pages that refer to this page: [shells(5)](../man5/shells.5.html)

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
