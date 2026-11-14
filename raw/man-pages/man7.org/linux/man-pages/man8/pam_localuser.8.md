---
{"title": "pam_localuser(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_localuser.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_localuser(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_LOCALUSER(8)             Linux-PAM Manual            PAM_LOCALUSER(8)

## [](#NAME)NAME

           pam_localuser - require users to be listed in /etc/passwd

## [](#SYNOPSIS)SYNOPSIS

           pam_localuser.so [debug] [file=/path/passwd]

## [](#DESCRIPTION)DESCRIPTION

           pam_localuser is a PAM module to help implementing site-wide login
           policies, where they typically include a subset of the network's
           users and a few accounts that are local to a particular
           workstation. Using pam_localuser and pam_wheel or pam_listfile is
           an effective way to restrict access to either local users and/or a
           subset of the network's users.

           This could also be implemented using pam_listfile.so and a very
           short awk script invoked by cron, but it's common enough to have
           been separated out.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

           file=/path/passwd
               Use a file other than /etc/passwd.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (account, auth, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The new localuser was set successfully.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_CONV_ERR
               The conversation method supplied by the application failed to
               obtain the username.

           PAM_INCOMPLETE
               The conversation method supplied by the application returned
               PAM_CONV_AGAIN.

           PAM_SERVICE_ERR
               The user name is not valid or the passwd file is unavailable.

           PAM_PERM_DENIED
               The user is not listed in the passwd file.

## [](#EXAMPLES)EXAMPLES

           Add the following lines to /etc/pam.d/su to allow only local users
           or group wheel to use su.

               account sufficient pam_localuser.so
               account required pam_wheel.so

## [](#FILES)FILES

           /etc/passwd
               Local user account information.

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_localuser was written by Nalin Dahyabhai <nalin@redhat.com>.

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

    Linux-PAM                       08/04/2026               PAM_LOCALUSER(8)

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
