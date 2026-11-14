---
{"title": "pwhistory.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/pwhistory.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pwhistory.conf(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PWHISTORY.CONF(5)            Linux-PAM Manual           PWHISTORY.CONF(5)

## [](#NAME)NAME

           pwhistory.conf - pam_pwhistory configuration file

## [](#DESCRIPTION)DESCRIPTION

           pwhistory.conf provides a way to configure the default settings
           for saving the last passwords for each user. This file is read by
           the pam_pwhistory module and is the preferred method over
           configuring pam_pwhistory directly.

           The file has a very simple name = value format with possible
           comments starting with # character. The whitespace at the
           beginning of line, end of line, and around the = sign is ignored.

## [](#OPTIONS)OPTIONS

           debug
               Turns on debugging via syslog(3).

           enforce_for_root
               If this option is set, the check is enforced for root, too.

           remember=N
               The last N passwords for each user are saved. The default is
               10. Value of 0 makes the module to keep the existing contents
               of the opasswd file unchanged.

           retry=N
               Prompt user at most N times before returning with error. The
               default is 1.

           file=/path/filename
               Store password history in file /path/filename rather than the
               default location. The default location is
               /etc/security/opasswd.

## [](#EXAMPLES)EXAMPLES

           /etc/security/pwhistory.conf file example:

               debug
               remember=5
               file=/tmp/opasswd

## [](#FILES)FILES

           /etc/security/pwhistory.conf
               the config file for custom options

## [](#SEE_ALSO)SEE ALSO

           pwhistory(8), pam_pwhistory(8), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_pwhistory was written by Thorsten Kukuk. The support for
           pwhistory.conf was written by Iker Pedrosa.

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

    Linux-PAM                       08/04/2026              PWHISTORY.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [pam_pwhistory(8)](../man8/pam_pwhistory.8.html)

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
