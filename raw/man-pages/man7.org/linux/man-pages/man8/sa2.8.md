---
{"title": "sa2(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sa2.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sa2(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SA2(8)                     Linux User's Manual                     SA2(8)

## [](#NAME)NAME

           sa2 - Create a report from the current standard system activity
           daily data file.

## [](#SYNOPSIS)SYNOPSIS

           /usr/local/lib64/sa/sa2

## [](#DESCRIPTION)DESCRIPTION

           The sa2 command is a shell procedure variant of the sar command
           which writes a daily report in the sarDD or the sarYYYYMMDD file,
           where YYYY stands for the current year, MM for the current month
           and DD for the current day. By default the report is saved in the
           /var/log/sa directory. The sa2 command will also remove reports
           more than one week old by default.  You can however keep reports
           for a longer (or a shorter) period by setting the HISTORY
           environment variable. Read the sysstat(5) manual page for details.

           The sa2 command accepts most of the flags and parameters of the
           sar command.

           The sa2 command is designed to be started automatically by the
           cron command.

## [](#EXAMPLES)EXAMPLES

           To run the sa2 command daily, place the following entry in your
           root crontab file:

           5 19 * * 1-5 /usr/local/lib64/sa/sa2 -A

           This will generate by default a daily report called sarDD in the
           /var/log/sa directory, where the DD parameter is a number
           representing the day of the month.

## [](#FILES)FILES

           /var/log/sa/sarDD
           /var/log/sa/sarYYYYMMDD
                  The standard system activity daily report files and their
                  default location.  YYYY stands for the current year, MM for
                  the current month and DD for the current day.

## [](#AUTHOR)AUTHOR

           Sebastien Godard (sysstat <at> orange.fr)

## [](#SEE_ALSO)SEE ALSO

           sar(1), sadc(8), sa1(8), sadf(1), sysstat(5)

           https://github.com/sysstat/sysstat 
           https://sysstat.github.io/ 

## [](#COLOPHON)COLOPHON

           This page is part of the sysstat (sysstat performance monitoring
           tools) project.  Information about the project can be found at 
           ⟨http://sebastien.godard.pagesperso-orange.fr/⟩.  If you have a bug
           report for this manual page, send it to sysstat-AT-orange.fr.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/sysstat/sysstat.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-28.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux                          AUGUST 2023                         SA2(8)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogger_daily_report(1)](../man1/pmlogger_daily_report.1.html),  [sadf(1)](../man1/sadf.1.html),  [sar(1)](../man1/sar.1.html),  [sysstat(5)](../man5/sysstat.5.html),  [sa1(8)](../man8/sa1.8.html),  [sadc(8)](../man8/sadc.8.html)

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
