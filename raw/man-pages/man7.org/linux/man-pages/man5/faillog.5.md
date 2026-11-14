---
{"title": "faillog(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/faillog.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# faillog(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FAILLOG(5)            File Formats and Configuratio            FAILLOG(5)

## [](#NAME)NAME

           faillog - login failure logging file

## [](#DESCRIPTION)DESCRIPTION

           /var/log/faillog maintains a count of login failures and the
           limits for each account.

           The file contains fixed length records, indexed by numerical UID.
           Each record contains the count of login failures since the last
           successful login; the maximum number of failures before the
           account is disabled; the line on which the last login failure
           occurred; the date of the last login failure; and the duration (in
           seconds) during which the account will be locked after a failure.

           The structure of the file is:

               struct    faillog {
                    short   fail_cnt;
                    short   fail_max;
                    char    fail_line[12];
                    time_t  fail_time;
                    long    fail_locktime;
               };

## [](#FILES)FILES

           /var/log/faillog
               Failure logging file.

## [](#SEE_ALSO)SEE ALSO

           faillog(8)

## [](#COLOPHON)COLOPHON

           This page is part of the shadow-utils (utilities for managing
           accounts and shadow password files) project.  Information about
           the project can be found at 
           ⟨https://github.com/shadow-maint/shadow⟩.  If you have a bug report
           for this manual page, send it to
           pkg-shadow-devel@alioth-lists.debian.net.  This page was obtained
           from the tarball shadow-4.19.0.tar fetched from
           ⟨https://github.com/shadow-maint/shadow/releases⟩ on 2026-08-04.
           If you discover any rendering problems in this HTML version of the
           page, or you believe there is a better or more up-to-date source
           for the page, or you have corrections or improvements to the
           information in this COLOPHON (which is not part of the original
           manual page), send a mail to man-pages@man7.org

    shadow-utils 4.19.0             08/04/2026                     FAILLOG(5)

------------------------------------------------------------------------

Pages that refer to this page: [faillog(8)](../man8/faillog.8.html)

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
