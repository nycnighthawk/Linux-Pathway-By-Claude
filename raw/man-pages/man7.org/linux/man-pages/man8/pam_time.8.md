---
{"title": "pam_time(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_time.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_time(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_TIME(8)                  Linux-PAM Manual                 PAM_TIME(8)

## [](#NAME)NAME

           pam_time - PAM module for time control access

## [](#SYNOPSIS)SYNOPSIS

           pam_time.so [conffile=conf-file] [debug] [noaudit]

## [](#DESCRIPTION)DESCRIPTION

           The pam_time PAM module does not authenticate the user, but
           instead it restricts access to a system and or specific
           applications at various times of the day and on specific days or
           over various terminal lines. This module can be configured to deny
           access to (individual) users based on their name, the time of day,
           the day of week, the service they are applying for and their
           terminal from which they are making their request.

           By default rules for time/port access are taken from config file
           /etc/security/time.conf. An alternative file can be specified with
           the conffile option.

           If there is no explicitly specified configuration file and
           /etc/security/time.conf does not exist,
           /usr/share/pam/security/time.conf is used.

           If Linux PAM is compiled with audit support the module will report
           when it denies access.

## [](#OPTIONS)OPTIONS

           conffile=/path/to/time.conf
               Indicate an alternative time.conf style configuration file to
               override the default.

           debug
               Some debug information is printed with syslog(3).

           noaudit
               Do not report logins at disallowed time to the audit
               subsystem.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the account type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               Access was granted.

           PAM_ABORT
               Not all relevant data could be gotten.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_PERM_DENIED
               Access was not granted.

           PAM_USER_UNKNOWN
               The user is not known to the system.

## [](#FILES)FILES

           /etc/security/time.conf
               Default configuration file

## [](#EXAMPLES)EXAMPLES

               #%PAM-1.0
               #
               # apply pam_time accounting to login requests
               #
               login  account  required  pam_time.so

## [](#SEE_ALSO)SEE ALSO

           time.conf(5), pam.d(5), pam(8).

## [](#AUTHOR)AUTHOR

           pam_time was written by Andrew G. Morgan <morgan@kernel.org>.

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

    Linux-PAM                       08/04/2026                    PAM_TIME(8)

------------------------------------------------------------------------

Pages that refer to this page: [time.conf(5)](../man5/time.conf.5.html)

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
