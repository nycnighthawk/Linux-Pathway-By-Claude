---
{"title": "pam_faildelay(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_faildelay.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_faildelay(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_FAILDELAY(8)             Linux-PAM Manual            PAM_FAILDELAY(8)

## [](#NAME)NAME

           pam_faildelay - Change the delay on failure per-application

## [](#SYNOPSIS)SYNOPSIS

           pam_faildelay.so [debug] [delay=microseconds]

## [](#DESCRIPTION)DESCRIPTION

           pam_faildelay is a PAM module that can be used to set the delay on
           failure per-application.

           If no delay is given, pam_faildelay will use the value of
           FAIL_DELAY from /etc/login.defs.

## [](#OPTIONS)OPTIONS

           debug
               Turns on debugging messages sent to syslog.

           delay=N
               Set the delay on failure to N microseconds.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the auth module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_IGNORE
               Delay was successful adjusted.

           PAM_SYSTEM_ERR
               The specified delay was not valid.

## [](#EXAMPLES)EXAMPLES

           The following example will set the delay on failure to 10 seconds:

               auth  optional  pam_faildelay.so  delay=10000000

## [](#SEE_ALSO)SEE ALSO

           pam_fail_delay(3), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_faildelay was written by Darren Tucker <dtucker@zip.com.au>.

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

    Linux-PAM                       08/04/2026               PAM_FAILDELAY(8)

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
