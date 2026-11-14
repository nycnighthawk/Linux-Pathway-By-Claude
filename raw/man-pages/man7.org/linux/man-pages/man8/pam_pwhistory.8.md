---
{"title": "pam_pwhistory(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_pwhistory.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_pwhistory(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_PWHISTORY(8)             Linux-PAM Manual            PAM_PWHISTORY(8)

## [](#NAME)NAME

           pam_pwhistory - PAM module to remember last passwords

## [](#SYNOPSIS)SYNOPSIS

           pam_pwhistory.so [debug] [use_authtok] [enforce_for_root]
                            [remember=N] [retry=N] [authtok_type=STRING]
                            [file=/path/filename] [conf=/path/to/config-file]

## [](#DESCRIPTION)DESCRIPTION

           This module saves the last passwords for each user in order to
           force password change history and keep the user from alternating
           between the same password too frequently.

           This module does not work together with kerberos. In general, it
           does not make much sense to use this module in conjunction with
           NIS or LDAP, since the old passwords are stored on the local
           machine and are not available on another machine for password
           history checking.

## [](#OPTIONS)OPTIONS

           debug
               Turns on debugging via syslog(3).

           use_authtok
               When password changing enforce the module to use the new
               password provided by a previously stacked password module
               (this is used in the example of the stacking of the
               pam_passwdqc module documented below).

           enforce_for_root
               If this option is set, the check is enforced for root, too.

           remember=N
               The last N passwords for each user are saved. The default is
               10. Value of 0 makes the module to keep the existing contents
               of the opasswd file unchanged.

           retry=N
               Prompt user at most N times before returning with error. The
               default is 1.

           authtok_type=STRING
               See pam_get_authtok(3) for more details.

           file=/path/filename
               Store password history in file /path/filename rather than the
               default location. The default location is
               /etc/security/opasswd.

           conf=/path/to/config-file
               Use another configuration file instead of the default
               /etc/security/pwhistory.conf.

           The options for configuring the module behavior are described in
           the pwhistory.conf(5) manual page. The options specified on the
           module command line override the values from the configuration
           file.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the password module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTHTOK_ERR
               No new password was entered, the user aborted password change
               or new password couldn't be set.

           PAM_IGNORE
               Password history was disabled.

           PAM_MAXTRIES
               Password was rejected too often.

           PAM_USER_UNKNOWN
               User is not known to system.

## [](#EXAMPLES)EXAMPLES

           An example password section would be:

               #%PAM-1.0
               password     required       pam_pwhistory.so
               password     required       pam_unix.so        use_authtok

           In combination with pam_passwdqc:

               #%PAM-1.0
               password     required       pam_passwdqc.so    config=/etc/passwdqc.conf
               password     required       pam_pwhistory.so   use_authtok
               password     required       pam_unix.so        use_authtok

## [](#FILES)FILES

           /etc/security/opasswd
               Default file with password history

           /etc/security/pwhistory.conf
               Config file for pam_pwhistory options

           /usr/share/pam/security/pwhistory.conf
               Config file for pam_pwhistory options. It will be used if
               /etc/security/pwhistory.conf does not exist.

## [](#SEE_ALSO)SEE ALSO

           pwhistory.conf(5), pam.conf(5), pam.d(5), pam(8)
           pam_get_authtok(3)

## [](#AUTHOR)AUTHOR

           pam_pwhistory was written by Thorsten Kukuk <kukuk@thkukuk.de>

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

    Linux-PAM                       08/04/2026               PAM_PWHISTORY(8)

------------------------------------------------------------------------

Pages that refer to this page: [pwhistory.conf(5)](../man5/pwhistory.conf.5.html),  [pwhistory_helper(8)](../man8/pwhistory_helper.8.html)

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
