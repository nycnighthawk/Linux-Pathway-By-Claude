---
{"title": "pam_mail(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_mail.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_mail(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_MAIL(8)                  Linux-PAM Manual                 PAM_MAIL(8)

## [](#NAME)NAME

           pam_mail - Inform about available mail

## [](#SYNOPSIS)SYNOPSIS

           pam_mail.so [close] [debug] [dir=maildir] [empty] [hash=count]
                       [noenv] [nopen] [quiet] [standard]

## [](#DESCRIPTION)DESCRIPTION

           The pam_mail PAM module provides the "you have new mail" service
           to the user. It can be plugged into any application that has
           credential or session hooks. It gives a single message indicating
           the newness of any mail it finds in the user's mail folder. This
           module also sets the PAM environment variable, MAIL, to the user's
           mail directory.

           If the mail spool file (be it /var/mail/$USER or a pathname given
           with the dir= parameter) is a directory then pam_mail assumes it
           is in the Maildir format.

## [](#OPTIONS)OPTIONS

           close
               Indicate if the user has any mail also on logout.

           debug
               Print debug information.

           dir=maildir
               Look for the user's mail in an alternative location defined by
               maildir/<login>. The default location for mail is
               /var/mail/<login>. Note, if the supplied maildir is prefixed
               by a '~', the directory is interpreted as indicating a file in
               the user's home directory.

           empty
               Also print message if user has no mail.

           hash=count
               Mail directory hash depth. For example, a hashcount of 2 would
               make the mail file be /var/spool/mail/u/s/user.

           noenv
               Do not set the MAIL environment variable.

           nopen
               Don't print any mail information on login. This flag is useful
               to get the MAIL environment variable set, but to not display
               any information about it.

           quiet
               Only report when there is new mail.

           standard
               Old style "You have..." format which doesn't show the mail
               spool being used. This also implies "empty".

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The session and auth (on establishment and deletion of
           credentials) module types are provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_BUF_ERR
               Memory buffer error.

           PAM_SERVICE_ERR
               Badly formed arguments.

           PAM_SUCCESS
               Success.

           PAM_USER_UNKNOWN
               User not known.

## [](#EXAMPLES)EXAMPLES

           Add the following line to /etc/pam.d/login to indicate that the
           user has new mail when they login to the system.

               session  optional  pam_mail.so standard

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_mail was written by Andrew G. Morgan <morgan@kernel.org>.

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

    Linux-PAM                       08/04/2026                    PAM_MAIL(8)

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
