---
{"title": "pam_wheel(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_wheel.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_wheel(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_WHEEL(8)                 Linux-PAM Manual                PAM_WHEEL(8)

## [](#NAME)NAME

           pam_wheel - Only permit root access to members of group wheel

## [](#SYNOPSIS)SYNOPSIS

           pam_wheel.so [debug] [deny] [group=name] [root_only] [trust]
                        [use_uid]

## [](#DESCRIPTION)DESCRIPTION

           The pam_wheel PAM module is used to enforce the so-called wheel
           group. By default it permits access to the target user if the
           applicant user is a member of the wheel group. If no group with
           this name exist, the module is using the group with the group-ID
           0.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

           deny
               Reverse the sense of the auth operation: if the user is trying
               to get UID 0 access and is a member of the wheel group (or the
               group of the group option), deny access. Conversely, if the
               user is not in the group, return PAM_IGNORE (unless trust was
               also specified, in which case we return PAM_SUCCESS).

           group=name
               Instead of checking the wheel or GID 0 groups, use the name
               group to perform the authentication.

           root_only
               The check for wheel membership is done only when the target
               user UID is 0.

           trust
               The pam_wheel module will return PAM_SUCCESS instead of
               PAM_IGNORE if the user is a member of the wheel group (thus
               with a little play stacking the modules the wheel members may
               be able to su to root without being prompted for a passwd).

           use_uid
               The check will be done against the real uid of the calling
               process, instead of trying to obtain the user from the login
               session associated with the terminal in use.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The auth and account module types are provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTH_ERR
               Authentication failure.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_IGNORE
               The return value should be ignored by PAM dispatch.

           PAM_PERM_DENY
               Permission denied.

           PAM_SERVICE_ERR
               Cannot determine the user name.

           PAM_SUCCESS
               Success.

           PAM_USER_UNKNOWN
               User not known.

## [](#EXAMPLES)EXAMPLES

           The root account gains access by default (rootok), only wheel
           members can become root (wheel) but Unix authenticate non-root
           applicants.

               su      auth     sufficient     pam_rootok.so
               su      auth     required       pam_wheel.so
               su      auth     required       pam_unix.so

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_wheel was written by Cristian Gafton <gafton@redhat.com>.

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

    Linux-PAM                       08/04/2026                   PAM_WHEEL(8)

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
