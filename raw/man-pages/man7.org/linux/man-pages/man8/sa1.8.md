---
{"title": "sa1(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sa1.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sa1(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SA1(8)                     Linux User's Manual                     SA1(8)

## [](#NAME)NAME

           sa1 - Collect and store binary data in the system activity daily
           data file.

## [](#SYNOPSIS)SYNOPSIS

           /usr/local/lib64/sa/sa1 [ --boot | --rotate | --sleep | interval
           count ]

## [](#DESCRIPTION)DESCRIPTION

           The sa1 command is a shell procedure variant of the sadc command
           and handles all of the flags and parameters of that command. The
           sa1 command collects and stores binary data in the current
           standard system activity daily data file.

           The standard system activity daily data file is named saDD unless
           sadc's option -D is used, in which case its name is saYYYYMMDD,
           where YYYY stands for the current year, MM for the current month
           and DD for the current day. By default it is located in the
           /var/log/sa directory.

           The interval and count parameters specify that the record should
           be written count times at interval seconds. If no arguments are
           given to sa1 then a single record is written.

           The sa1 command is designed to be started automatically by the
           cron command.

## [](#OPTIONS)OPTIONS

           --boot This option tells sa1 that the sadc command should be
                  called without specifying the interval and count parameters
                  in order to insert a dummy record, marking the time when
                  the counters restart from 0.

           --rotate
                  Use this option to tell sa1 to insert a record of
                  statistics to the standard saDD system activity daily data
                  file of the previous day.  This should be done shortly
                  after midnight (on day DD+1) in order to make sure that the
                  data file covers the whole day, including the last interval
                  of time just before midnight.

           --sleep
                  This option tells sa1 that the sadc command should insert a
                  comment indicating that the system is entering or leaving
                  sleep mode (i.e. system suspend or hibernation).

## [](#EXAMPLE)EXAMPLE

           To collect data (including those from disks) every 10 minutes,
           place the following entry in your root crontab file:

           0,10,20,30,40,50 * * * * /usr/local/lib64/sa/sa1 1 1 -S DISK

           To rotate current system activity daily data file, ensuring it is
           complete, place the following entry in your root crontab file:

           0 0 * * * /usr/local/lib64/sa/sa1 --rotate

## [](#FILES)FILES

           /var/log/sa/saDD
           /var/log/sa/saYYYYMMDD
                  The standard system activity daily data files and their
                  default location.  YYYY stands for the current year, MM for
                  the current month and DD for the current day.

## [](#AUTHOR)AUTHOR

           Sebastien Godard (sysstat <at> orange.fr)

## [](#SEE_ALSO)SEE ALSO

           sar(1), sadc(8), sa2(8), sadf(1), sysstat(5)

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

    Linux                           JULY 2026                          SA1(8)

------------------------------------------------------------------------

Pages that refer to this page: [sadf(1)](../man1/sadf.1.html),  [sar(1)](../man1/sar.1.html),  [sysstat(5)](../man5/sysstat.5.html),  [sa2(8)](../man8/sa2.8.html),  [sadc(8)](../man8/sadc.8.html)

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
