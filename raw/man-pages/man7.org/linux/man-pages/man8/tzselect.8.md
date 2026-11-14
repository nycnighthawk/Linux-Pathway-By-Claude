---
{"title": "tzselect(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tzselect.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tzselect(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [FILES](#FILES) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    tzselect(8)              System Manager's Manual              tzselect(8)

## [](#NAME)NAME

           tzselect - select a timezone

## [](#SYNOPSIS)SYNOPSIS

           tzselect [ -c coord ] [ -n limit ] [ --help ] [ --version ]

## [](#DESCRIPTION)DESCRIPTION

           The tzselect program asks the user for information about the
           current location, and outputs the resulting timezone to standard
           output.  The output is suitable as a value for the TZ environment
           variable.

           All interaction with the user is done via standard input and
           standard error.

## [](#OPTIONS)OPTIONS

           -c coord
                  Instead of asking for continent and then country and then
                  city, ask for selection from time zones whose largest
                  cities are closest to the location with geographical
                  coordinates coord.  Use ISO 6709 notation for coord, that
                  is, a latitude immediately followed by a longitude.  The
                  latitude and longitude should be signed integers followed
                  by an optional decimal point and fraction: positive numbers
                  represent north and east, negative south and west.
                  Latitudes with two and longitudes with three integer digits
                  are treated as degrees; latitudes with four or six and
                  longitudes with five or seven integer digits are treated as
                  DDMM, DDDMM, DDMMSS, or DDDMMSS representing DD or DDD
                  degrees, MM minutes, and zero or SS seconds, with any
                  trailing fractions represent fractional minutes or (if SS
                  is present) seconds.  The decimal point is that of the
                  current locale.  For example, in the (default) C locale,
                  -c +40.689-074.045 specifies 40.689 degrees N, 74.045
                  degrees W, -c +4041.4-07402.7 specifies 40 degrees 41.4
                  minutes N, 74 degrees 2.7 minutes W, and -c +404121-0740240
                  specifies 40 degrees 41 minutes 21 seconds N, 74 degrees 2
                  minutes 40 seconds W.  If coord is not one of the
                  documented forms, the resulting behavior is unspecified.

           -n limit
                  When -c is used, display the closest limit locations
                  (default 10).

           --help Output help information and exit.

           --version
                  Output version information and exit.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           AWK    Name of a POSIX-compliant awk program (default: awk).

           TZDIR  Name of the directory containing timezone data files
                  (default: /usr/share/zoneinfo).

## [](#FILES)FILES

           TZDIR/iso3166.tab
                  Table of ISO 3166 2-letter country codes and country names.

           TZDIR/zone1970.tab
                  Table of country codes, latitude and longitude, timezones,
                  and descriptive comments.

           TZDIR/TZ
                  Timezone data file for timezone TZ.

## [](#EXIT_STATUS)EXIT STATUS

           The exit status is zero if a timezone was successfully obtained
           from the user, nonzero otherwise.

## [](#SEE_ALSO)SEE ALSO

           newctime(3), tzfile(5), zdump(8), zic(8)

## [](#NOTES)NOTES

           Applications should not assume that tzselect's output matches the
           user's political preferences.

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Time Zone Database                                            tzselect(8)

------------------------------------------------------------------------

Pages that refer to this page: [pcpintro(1)](../man1/pcpintro.1.html),  [tzfile(5)](../man5/tzfile.5.html),  [environ(7)](../man7/environ.7.html)

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
