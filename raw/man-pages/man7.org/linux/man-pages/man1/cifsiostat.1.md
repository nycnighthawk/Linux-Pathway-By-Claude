---
{"title": "cifsiostat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cifsiostat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cifsiostat(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [REPORT](#REPORT) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [BUG](#BUG) \| [FILE](#FILE) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CIFSIOSTAT(1)              Linux User's Manual              CIFSIOSTAT(1)

## [](#NAME)NAME

           cifsiostat - Report CIFS statistics.

## [](#SYNOPSIS)SYNOPSIS

           cifsiostat [ -h ] [ -k | -m | -G ] [ -t ] [ -U ] [ -V ] [ -y ] [
           --dec={ 0 | 1 | 2 } ] [ --human ] [ -o JSON ] [ --pretty ] [
           interval [ count ] ]

## [](#DESCRIPTION)DESCRIPTION

           The cifsiostat command displays statistics about read and write
           operations on CIFS filesystems.

           The interval parameter specifies the amount of time in seconds
           between each report. The first report contains statistics for the
           time since system startup (boot), unless the -y option is used (in
           this case, the first report is omitted).  Each subsequent report
           contains statistics collected during the interval since the
           previous report.  A report consists of a CIFS header row followed
           by a line of statistics for each CIFS filesystem that is mounted.
           The count parameter can be specified in conjunction with the
           interval parameter. If the count parameter is specified, the value
           of count determines the number of reports generated at interval
           seconds apart. If the interval parameter is specified without the
           count parameter, the cifsiostat command generates reports
           continuously.

## [](#REPORT)REPORT

           The CIFS report provides statistics for each mounted CIFS
           filesystem.  The report shows the following fields:

           Filesystem:
                  This columns shows the mount point of the CIFS filesystem.

           rB/s (rkB/s, rMB/s, rGB/s)
                  Indicate the average number of bytes (kibibytes, mebibytes,
                  gibibytes) read per second.

           wB/s (wkB/s, wMB/s, wGB/s)
                  Indicate the average number of bytes (kibibytes, mebibytes,
                  gibibytes) written per second.

           rop/s  Indicate the number of 'read' operations that were issued
                  to the filesystem per second.

           wop/s  Indicate the number of 'write' operations that were issued
                  to the filesystem per second.

           fo/s   Indicate the number of open files per second.

           fc/s   Indicate the number of closed files per second.

           fd/s   Indicate the number of deleted files per second.

## [](#OPTIONS)OPTIONS

           --dec={ 0 | 1 | 2 }
                  Specify the number of decimal places to use (0 to 2,
                  default value is 2).

           -h     This option is equivalent to specifying --human --pretty.

           --human
                  Print sizes in human readable format (e.g. 1.0k, 1.2M,
                  etc.)  The units displayed with this option supersede any
                  other default units (e.g.  kibibytes, sectors...)
                  associated with the metrics.

           -G     Display statistics in gibibytes per second.

           -k     Display statistics in kibibytes per second.

           -m     Display statistics in mebibytes per second.

           -o JSON
                  Display the statistics in JSON (JavaScript Object Notation)
                  format.  JSON output field order is undefined, and new
                  fields may be added in the future.

           --pretty
                  Make the CIFS report easier to read by a human.

           -t     Print the time for each report displayed. The timestamp
                  format may depend on the value of the S_TIME_FORMAT
                  environment variable (see below) and on whether option -U
                  has been used.

           -U     Display timestamp (UTC - Coordinated Universal Time) in
                  seconds from the epoch.

           -V     Print version number then exit.

           -y     Omit first report with statistics since system boot, if
                  displaying multiple records at given interval.

## [](#ENVIRONMENT)ENVIRONMENT

           The cifsiostat command takes into account the following
           environment variables:

           S_COLORS
                  By default statistics are displayed in color when the
                  output is connected to a terminal.  Use this variable to
                  change the settings. Possible values for this variable are
                  never, always or auto (the latter is equivalent to the
                  default settings).
                  Please note that the color (being red, yellow, or some
                  other color) used to display a value is not indicative of
                  any kind of issue simply because of the color. It only
                  indicates different ranges of values.

           S_COLORS_SGR
                  Specify the colors and other attributes used to display
                  statistics on the terminal.  Its value is a colon-separated
                  list of capabilities that defaults to
                  I=32;22:N=34;1:Z=34;22.  Supported capabilities are:

                  I=     SGR substring for filesystem names.

                  N=     SGR substring for non-zero statistics values.

                  Z=     SGR substring for zero values.

           S_TIME_FORMAT
                  If this variable exists and its value is ISO then the
                  current locale will be ignored when printing the date in
                  the report header. The cifsiostat command will use the ISO
                  8601 format (YYYY-MM-DD) instead.  The timestamp displayed
                  with option -t will also be compliant with ISO 8601 format.

## [](#BUG)BUG

           /proc filesystem must be mounted for cifsiostat to work.

           Although cifsiostat displays units corresponding to kilobytes
           (kB), megabytes (MB), gigabytes (GB)..., it actually uses
           kibibytes (kiB), mebibytes (MiB), gibibytes (GiB)...  A kibibyte
           is equal to 1024 bytes, a mebibyte is equal to 1024 kibibytes, and
           a gibibyte is equal to 1024 mebibytes.

## [](#FILE)FILE

           /proc/fs/cifs/Stats contains CIFS statistics.

## [](#AUTHORS)AUTHORS

           Written by Ivana Varekova (varekova <at> redhat.com)
           Maintained by Sebastien Godard (sysstat <at> orange.fr)

## [](#SEE_ALSO)SEE ALSO

           sar(1), pidstat(1), mpstat(1), vmstat(8), iostat(1), tapestat(1),
           nfsiostat(1)

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

    Linux                           JULY 2025                   CIFSIOSTAT(1)

------------------------------------------------------------------------

Pages that refer to this page: [iostat(1)](../man1/iostat.1.html)

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
