---
{"title": "faillock(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/faillock.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# faillock(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FAILLOCK(8)                  Linux-PAM Manual                 FAILLOCK(8)

## [](#NAME)NAME

           faillock - Tool for displaying and modifying the authentication
           failure record files

## [](#SYNOPSIS)SYNOPSIS

           faillock [--dir /path/to/tally-directory] [--user username]
                    [--reset]

## [](#DESCRIPTION)DESCRIPTION

           The pam_faillock.so module maintains a list of failed
           authentication attempts per user during a specified interval and
           locks the account in case there were more than deny consecutive
           failed authentications. It stores the failure records into
           per-user files in the tally directory.

           The faillock command is an application which can be used to
           examine and modify the contents of the tally files. It can display
           the recent failed authentication attempts of the username or clear
           the tally files of all or individual usernames.

## [](#OPTIONS)OPTIONS

           --conf /path/to/config-file
               The file where the configuration is located. The default is
               /etc/security/faillock.conf.

           --dir /path/to/tally-directory
               The directory where the user files with the failure records
               are kept.

               The priority to set this option is to use the value provided
               from the command line. If this isn't provided, then the value
               from the configuration file is used. Finally, if neither of
               them has been provided, then /var/run/faillock is used.

           --user username
               The user whose failure records should be displayed or cleared.

           --reset
               Instead of displaying the user's failure records, clear them.

## [](#FILES)FILES

           /var/run/faillock/*
               the files logging the authentication failures for users

## [](#SEE_ALSO)SEE ALSO

           pam_faillock(8), pam(8)

## [](#AUTHOR)AUTHOR

           faillock was written by Tomas Mraz.

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

    Linux-PAM                       08/04/2026                    FAILLOCK(8)

------------------------------------------------------------------------

Pages that refer to this page: [faillock.conf(5)](../man5/faillock.conf.5.html),  [pam_faillock(8)](../man8/pam_faillock.8.html)

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
