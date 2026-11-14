---
{"title": "pam_timestamp(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_timestamp.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_timestamp(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_TIMESTAMP(8)             Linux-PAM Manual            PAM_TIMESTAMP(8)

## [](#NAME)NAME

           pam_timestamp - Authenticate using cached successful
           authentication attempts

## [](#SYNOPSIS)SYNOPSIS

           pam_timestamp.so [timestampdir=directory]
                            [timestamp_timeout=number] [verbose] [debug]

## [](#DESCRIPTION)DESCRIPTION

           In a nutshell, pam_timestamp caches successful authentication
           attempts, and allows you to use a recent successful attempt as the
           basis for authentication. This is similar mechanism which is used
           in sudo.

           When an application opens a session using pam_timestamp, a
           timestamp file is created in the timestampdir directory for the
           user. When an application attempts to authenticate the user, a
           pam_timestamp will treat a sufficiently recent timestamp file as
           grounds for succeeding.

## [](#OPTIONS)OPTIONS

           timestampdir=directory
               Specify an alternate directory where pam_timestamp creates
               timestamp files.

           timestamp_timeout=number
               How long should pam_timestamp treat timestamp as valid after
               their last modification date (in seconds). Default is 300
               seconds.

           verbose
               Attempt to inform the user when access is granted.

           debug
               Turns on debugging messages sent to syslog(3).

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The auth and session module types are provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTH_ERR
               The module was not able to retrieve the user name or no valid
               timestamp file was found.

           PAM_SUCCESS
               Everything was successful.

           PAM_SESSION_ERR
               Timestamp file could not be created or updated.

## [](#NOTES)NOTES

           Users can get confused when they are not always asked for
           passwords when running a given program. Some users reflexively
           begin typing information before noticing that it is not being
           asked for.

## [](#EXAMPLES)EXAMPLES

               auth sufficient pam_timestamp.so verbose
               auth required   pam_unix.so

               session required pam_unix.so
               session optional pam_timestamp.so

## [](#FILES)FILES

           /var/run/pam_timestamp/...
               timestamp files and directories

## [](#SEE_ALSO)SEE ALSO

           pam_timestamp_check(8), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_timestamp was written by Nalin Dahyabhai.

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

    Linux-PAM                       08/04/2026               PAM_TIMESTAMP(8)

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
