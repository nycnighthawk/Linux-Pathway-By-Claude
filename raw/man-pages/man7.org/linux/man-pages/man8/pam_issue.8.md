---
{"title": "pam_issue(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_issue.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_issue(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_ISSUE(8)                 Linux-PAM Manual                PAM_ISSUE(8)

## [](#NAME)NAME

           pam_issue - PAM module to add issue file to user prompt

## [](#SYNOPSIS)SYNOPSIS

           pam_issue.so [noesc] [issue=issue-file-name]

## [](#DESCRIPTION)DESCRIPTION

           pam_issue is a PAM module to prepend an issue file to the username
           prompt. It also by default parses escape codes in the issue file
           similar to some common getty's (using \x format).

           Recognized escapes:

           \d
               current day

           \l
               name of this tty

           \m
               machine architecture (uname -m)

           \n
               machine's network node hostname (uname -n)

           \o
               domain name of this system

           \r
               release number of operating system (uname -r)

           \t
               current time

           \s
               operating system name (uname -s)

           \u
               number of users currently logged in

           \U
               same as \u except it is suffixed with "user" or "users" (eg.
               "1 user" or "10 users")

           \v
               operating system version and build date (uname -v)

## [](#OPTIONS)OPTIONS

           noesc
               Turns off escape code parsing.

           issue=issue-file-name
               The file to output if not using the default.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the auth module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_BUF_ERR
               Memory buffer error.

           PAM_IGNORE
               The prompt was already changed.

           PAM_SERVICE_ERR
               A service module error occurred.

           PAM_SUCCESS
               The new prompt was set successfully.

## [](#EXAMPLES)EXAMPLES

           Add the following line to /etc/pam.d/login to set the user
           specific issue at login:

                       auth optional pam_issue.so issue=/etc/issue

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_issue was written by Ben Collins <bcollins@debian.org>.

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

    Linux-PAM                       08/04/2026                   PAM_ISSUE(8)

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
