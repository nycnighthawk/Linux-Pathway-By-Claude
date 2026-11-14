---
{"title": "pam_lastlog2(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_lastlog2.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_lastlog2(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_LASTLOG2(8)           System Administration           PAM_LASTLOG2(8)

## [](#NAME)NAME

           pam_lastlog2 - PAM module to display date of last login

## [](#SYNOPSIS)SYNOPSIS

           pam_lastlog2.so [debug] [silent] [silent_if=<services>]
           [database=<file>]

## [](#DESCRIPTION)DESCRIPTION

           pam_lastlog2 is a PAM module to display a line of information
           about the last login of the user. The module uses the
           /var/lib/lastlog/lastlog2.db database file to store all
           information.

           Compared to pam_lastlog this PAM module is Y2038 safe and uses
           sqlite3 to store the information.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

           silent
               Avoid all messages except errors and don’t inform the user
               about any previous login, only update the
               /var/lib/lastlog/lastlog2.db database.

           silent_if=<services>
               The argument services is a comma separated list of PAM
               services. If a service is listed here, the last login message
               will not be shown.

           database=<file>
               Use file instead of /var/lib/lastlog/lastlog2.db.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The session module type is provided for displaying the information
           about the last login and updating the lastlog file.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               Everything was successful.

           PAM_SERVICE_ERR
               Internal service module error. This includes error reading
               from or writing to the database.

           PAM_USER_UNKNOWN
               User not known.

           PAM_IGNORE
               Returned by service types which do nothing.

## [](#EXAMPLES)EXAMPLES

           Add the following line to e.g. /etc/pam.d/login to display the
           last login time of a user:

           session  optional pam_lastlog2.so silent_if=gdm,gdm-password

           It is up to the administrator to decide if the user can login
           (optional/required) when pam_lastlog2 has returned an error.

## [](#AUTHOR)AUTHOR

           pam_lastlog2 was written by Thorsten Kukuk <kukuk@suse.com>.

## [](#SEE_ALSO)SEE ALSO

           liblastlog2(3), pam.conf(5), pam.d(5), pam(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The pam_lastlog2 library is part of the util-linux package since
           version 2.40. It can be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                PAM_LASTLOG2(8)

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
