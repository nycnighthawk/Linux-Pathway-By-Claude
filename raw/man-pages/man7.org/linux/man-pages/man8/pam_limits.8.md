---
{"title": "pam_limits(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_limits.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_limits(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_LIMITS(8)                Linux-PAM Manual               PAM_LIMITS(8)

## [](#NAME)NAME

           pam_limits - PAM module to limit resources

## [](#SYNOPSIS)SYNOPSIS

           pam_limits.so [conf=/path/to/limits.conf] [debug] [set_all]
                         [utmp_early] [noaudit]

## [](#DESCRIPTION)DESCRIPTION

           The pam_limits PAM module sets limits on the system resources that
           can be obtained in a user-session. Users of uid=0 are affected by
           this limits, too.

           By default limits are taken from the /etc/security/limits.conf
           config file or, if that one is not present, the file
           /usr/share/pam/security/limits.conf. Then individual *.conf files
           from the /etc/security/limits.d/ and
           /usr/share/pam/security/limits.d directories are read. If
           /etc/security/limits.d/@filename@.conf exists, then
           /usr/share/pam/security/limits.d/@filename@.conf will not be used.
           All limits.d/*.conf files are sorted by their @filename@.conf in
           lexicographic order regardless of which of the directories they
           reside in. The effect of the individual files is the same as if
           all the files were concatenated together in the order of parsing.
           If a config file is explicitly specified with the config option
           the files in the above directories are not parsed.

           The module must not be called by a multithreaded application.

           If Linux PAM is compiled with audit support the module will report
           when it denies access based on limit of maximum number of
           concurrent login sessions.

## [](#OPTIONS)OPTIONS

           conf=/path/to/limits.conf
               Indicate an alternative limits.conf style configuration file
               to override the default.

           debug
               Print debug information.

           set_all
               Set the limits for which no value is specified in the
               configuration file to the one from the process with the PID 1.
               Please note that if the init process is systemd these limits
               will not be the kernel default limits and this option should
               not be used.

           utmp_early
               Some broken applications actually allocate a utmp entry for
               the user before the user is admitted to the system. If some of
               the services you are configuring PAM for do this, you can
               selectively use this module argument to compensate for this
               behavior and at the same time maintain system-wide consistency
               with a single limits.conf file.

           noaudit
               Do not report exceeded maximum logins count to the audit
               subsystem.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the session module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_ABORT
               Cannot get current limits.

           PAM_IGNORE
               No limits found for this user.

           PAM_PERM_DENIED
               New limits could not be set.

           PAM_SERVICE_ERR
               Cannot read config file.

           PAM_SESSION_ERR
               Error recovering account name.

           PAM_SUCCESS
               Limits were changed.

           PAM_USER_UNKNOWN
               The user is not known to the system.

## [](#FILES)FILES

           /etc/security/limits.conf
               Default configuration file

           /usr/share/pam/security/limits.conf
               Default configuration file if /etc/security/limits.conf does
               not exist.

## [](#EXAMPLES)EXAMPLES

           For the services you need resources limits (login for example) put
           a the following line in /etc/pam.d/login as the last line for that
           service (usually after the pam_unix session line):

               #%PAM-1.0
               #
               # Resource limits imposed on login sessions via pam_limits
               #
               session  required  pam_limits.so

           Replace "login" for each service you are using this module.

## [](#SEE_ALSO)SEE ALSO

           limits.conf(5), pam.d(5), pam(8).

## [](#AUTHORS)AUTHORS

           pam_limits was initially written by Cristian Gafton
           <gafton@redhat.com>

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

    Linux-PAM                       08/04/2026                  PAM_LIMITS(8)

------------------------------------------------------------------------

Pages that refer to this page: [limits.conf(5)](../man5/limits.conf.5.html)

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
