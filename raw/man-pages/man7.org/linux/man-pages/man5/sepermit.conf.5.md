---
{"title": "sepermit.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/sepermit.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sepermit.conf(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SEPERMIT.CONF(5)             Linux-PAM Manual            SEPERMIT.CONF(5)

## [](#NAME)NAME

           sepermit.conf - configuration file for the pam_sepermit module

## [](#DESCRIPTION)DESCRIPTION

           The lines of the configuration file have the following syntax:

           <user>[:<option>:<option>...]

           The user can be specified in the following manner:

           •   a username

           •   a groupname, with @group syntax. This should not be confused
               with netgroups.

           •   a SELinux user name with %seuser syntax.

           The recognized options are:

           exclusive
               Only single login session will be allowed for the user and the
               user's processes will be killed on logout.

           ignore
               The module will never return PAM_SUCCESS status for the user.
               It will return PAM_IGNORE if SELinux is in the enforcing mode,
               and PAM_AUTH_ERR otherwise. It is useful if you want to
               support passwordless guest users and other confined users with
               passwords simultaneously.

           The lines which start with # character are comments and are
           ignored.

## [](#EXAMPLES)EXAMPLES

           These are some example lines which might be specified in
           /etc/security/sepermit.conf.

               %guest_u:exclusive
               %staff_u:ignore
               %user_u:ignore

## [](#SEE_ALSO)SEE ALSO

           pam_sepermit(8), pam.d(5), pam(8), selinux(8),

## [](#AUTHOR)AUTHOR

           pam_sepermit and this manual page were written by Tomas Mraz
           <tmraz@redhat.com>

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

    Linux-PAM                       08/04/2026               SEPERMIT.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [pam_sepermit(8)](../man8/pam_sepermit.8.html)

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
