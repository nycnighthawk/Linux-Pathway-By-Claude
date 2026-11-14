---
{"title": "mailto.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/mailto.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mailto.conf(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mailto.conf(5)                 OpenPrinting                mailto.conf(5)

## [](#NAME)NAME

           mailto.conf - configuration file for cups email notifier

## [](#DESCRIPTION)DESCRIPTION

           The mailto.conf file defines the local mail server and email
           notification preferences for CUPS.

           Each line in the file can be a configuration directive, a blank
           line, or a comment.  Configuration directives typically consist of
           a name and zero or more values separated by whitespace.  The
           configuration directive name and values are case-insensitive.
           Comment lines start with the # character.

       DIRECTIVES
           Cc cc-address@domain.com
                Specifies an additional recipient for all email
                notifications.

           From from-address@domain.com
                Specifies the sender of email notifications.

           Sendmail sendmail command and options
                Specifies the sendmail command to use when sending email
                notifications.  Only one Sendmail or SMTPServer line may be
                present in the mailto.conf file.  If multiple lines are
                present, only the last one is used.

           SMTPServer servername
                Specifies a SMTP server to send email notifications to.  Only
                one Sendmail or SMTPServer line may be present in the
                mailto.conf file.  If multiple lines are present, only the
                last one is used.

           Subject subject-prefix
                Specifies a prefix string for the subject line of an email
                notification.

## [](#SEE_ALSO)SEE ALSO

           cupsd(8), CUPS Online Help (http://localhost:631/help)

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2020-2024 by OpenPrinting.

## [](#COLOPHON)COLOPHON

           This page is part of the CUPS (a standards-based, open source
           printing system) project.  Information about the project can be
           found at ⟨https://github.com/openprinting/cups⟩.  If you have a
           bug report for this manual page, see
           ⟨https://github.com/OpenPrinting/cups/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/openprinting/cups⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    2021-02-28                         CUPS                    mailto.conf(5)

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
