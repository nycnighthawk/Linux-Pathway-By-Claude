---
{"title": "pam_nologin(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_nologin.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_nologin(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_NOLOGIN(8)               Linux-PAM Manual              PAM_NOLOGIN(8)

## [](#NAME)NAME

           pam_nologin - Prevent non-root users from login

## [](#SYNOPSIS)SYNOPSIS

           pam_nologin.so [file=/path/nologin] [successok]

## [](#DESCRIPTION)DESCRIPTION

           pam_nologin is a PAM module that prevents users from logging into
           the system when /var/run/nologin or /etc/nologin exists. The
           contents of the file are displayed to the user. The pam_nologin
           module has no effect on the root user's ability to log in.

## [](#OPTIONS)OPTIONS

           file=/path/nologin
               Use this file instead the default /var/run/nologin or
               /etc/nologin.

           successok
               Return PAM_SUCCESS if no file exists, the default is
               PAM_IGNORE.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The auth and account module types are provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTH_ERR
               The user is not root and /etc/nologin exists, so the user is
               not permitted to log in.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_IGNORE
               This is the default return value.

           PAM_SUCCESS
               Success: either the user is root or the nologin file does not
               exist.

           PAM_USER_UNKNOWN
               User not known to the underlying authentication module.

## [](#EXAMPLES)EXAMPLES

           The suggested usage for /etc/pam.d/login is:

               auth  required  pam_nologin.so

## [](#NOTES)NOTES

           In order to make this module effective, all login methods should
           be secured by it. It should be used as a required method listed
           before any sufficient methods in order to get standard Unix
           nologin semantics. Note, the use of successok module argument
           causes the module to return PAM_SUCCESS and as such would break
           such a configuration - failing sufficient modules would lead to a
           successful login because the nologin module succeeded.

## [](#SEE_ALSO)SEE ALSO

           nologin(5), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_nologin was written by Michael K. Johnson
           <johnsonm@redhat.com>.

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

    Linux-PAM                       08/04/2026                 PAM_NOLOGIN(8)

------------------------------------------------------------------------

Pages that refer to this page: [nologin(8)](../man8/nologin.8.html),  [systemd-user-sessions.service(8)](../man8/systemd-user-sessions.service.8.html)

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
