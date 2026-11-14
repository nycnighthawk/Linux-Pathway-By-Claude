---
{"title": "sendmail(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sendmail.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sendmail(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SENDMAIL(8)               System Manager's Manual             SENDMAIL(8)

## [](#NAME)NAME

           sendmail — a mail enqueuer for smtpd(8)

## [](#SYNOPSIS)SYNOPSIS

           sendmail [-tv] [-F name] [-f from] to ...

## [](#DESCRIPTION)DESCRIPTION

           The sendmail utility is a local enqueuer for the smtpd(8) daemon,
           compatible with mailwrapper(8).  The message is read on standard
           input (stdin) until sendmail encounters an end-of-file.  The
           sendmail enqueuer is not intended to be used directly to send
           mail, but rather via a frontend known as a mail user agent.

           Unless the optional -t flag is specified, one or more recipients
           must be specified on the command line.

           The options are as follows:

           -F name
                   Set the sender's full name.

           -f from
                   Set the sender's address.

           -t      Read the message's To:, Cc:, and Bcc: fields for
                   recipients.  The Bcc: field will be deleted before
                   sending.

           -v      Enable verbose output.

           To maintain compatibility with Sendmail, Inc.'s implementation of
           sendmail, various other flags are accepted, but have no effect.

## [](#EXIT_STATUS)EXIT STATUS

           The utility exits 0 on success, and >0 if an error occurs.

## [](#SEE_ALSO)SEE ALSO

           smtpctl(8), smtpd(8)

## [](#AUTHORS)AUTHORS

           OpenSMTPD is primarily developed by Gilles Chehade, Eric Faurot,
           and Charles Longeau, with contributions from various OpenBSD
           hackers.  It is distributed under the ISC license.

           This manpage was written by Ryan Kavanagh ⟨rak@debian.org⟩ for the
           Debian project and is distributed under the ISC license.

## [](#COLOPHON)COLOPHON

           This page is part of the OpenSMTPD (a FREE implementation of the
           server-side SMTP protocol) project.  Information about the project
           can be found at https://www.opensmtpd.org/.  If you have a bug
           report for this manual page, see
           ⟨https://github.com/OpenSMTPD/OpenSMTPD/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/OpenSMTPD/OpenSMTPD.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-03-26.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    GNU                          October 23, 2015                 SENDMAIL(8)

------------------------------------------------------------------------

Pages that refer to this page: [sysexits.h(3head)](../man3/sysexits.h.3head.html),  [boot(7)](../man7/boot.7.html),  [mailaddr(7)](../man7/mailaddr.7.html),  [cron(8)](../man8/cron.8.html)

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
