---
{"title": "pam_sepermit(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_sepermit.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_sepermit(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_SEPERMIT(8)              Linux-PAM Manual             PAM_SEPERMIT(8)

## [](#NAME)NAME

           pam_sepermit - PAM module to allow/deny login depending on SELinux
           enforcement state

## [](#SYNOPSIS)SYNOPSIS

           pam_sepermit.so [debug] [conf=/path/to/config/file]

## [](#DESCRIPTION)DESCRIPTION

           The pam_sepermit module allows or denies login depending on
           SELinux enforcement state.

           When the users which are logging in match an entry in the config
           file they are allowed access only when SELinux is in enforcing
           mode. Otherwise they are denied access. For users not matching any
           entry in the config file the pam_sepermit module returns
           PAM_IGNORE return value.

           The config file contains a list of user names one per line with
           optional arguments. If the name is prefixed with @ character it
           means that all users in the group name match. If it is prefixed
           with a % character the SELinux user is used to match against the
           name instead of the account name. Note that when SELinux is
           disabled the SELinux user assigned to the account cannot be
           determined. This means that such entries are never matched when
           SELinux is disabled and pam_sepermit will return PAM_IGNORE.

           See sepermit.conf(5) for details.

           If there is no explicitly specified configuration file and
           /etc/security/sepermit.conf does not exist,
           /usr/share/pam/security/sepermit.conf is used.

## [](#OPTIONS)OPTIONS

           debug
               Turns on debugging via syslog(3).

           conf=/path/to/config/file
               Path to alternative config file overriding the default.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The auth and account module types are provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTH_ERR
               SELinux is disabled or in the permissive mode and the user
               matches.

           PAM_SUCCESS
               SELinux is in the enforcing mode and the user matches.

           PAM_IGNORE
               The user does not match any entry in the config file.

           PAM_USER_UNKNOWN
               The module was unable to determine the user's name.

           PAM_SERVICE_ERR
               Error during reading or parsing the config file.

## [](#FILES)FILES

           /etc/security/sepermit.conf
               Default configuration file

## [](#EXAMPLES)EXAMPLES

               auth     [success=done ignore=ignore default=bad] pam_sepermit.so
               auth     required  pam_unix.so
               account  required  pam_unix.so
               session  required  pam_permit.so

## [](#SEE_ALSO)SEE ALSO

           sepermit.conf(5), pam.conf(5), pam.d(5), pam(8) selinux(8)

## [](#AUTHOR)AUTHOR

           pam_sepermit and this manual page were written by Tomas Mraz
           <tmraz@redhat.com>.

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

    Linux-PAM                       08/04/2026                PAM_SEPERMIT(8)

------------------------------------------------------------------------

Pages that refer to this page: [sepermit.conf(5)](../man5/sepermit.conf.5.html)

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
