---
{"title": "clockdiff(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/clockdiff.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# clockdiff(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [WARNINGS](#WARNINGS) \| [SEE ALSO](#SEE_ALSO) \| [REFERENCES](#REFERENCES) \| [AUTHOR](#AUTHOR) \| [SECURITY](#SECURITY) \| [AVAILABILITY](#AVAILABILITY) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CLOCKDIFF(8)                     iputils                     CLOCKDIFF(8)

## [](#NAME)NAME

           clockdiff - measure clock difference between hosts

## [](#SYNOPSIS)SYNOPSIS

           clockdiff [-o] [-o1] [--time-format ctime iso] [-V] {destination}

## [](#DESCRIPTION)DESCRIPTION

           clockdiff Measures clock difference between us and destination
           with 1 msec resolution using ICMP TIMESTAMP [2] packets or,
           optionally, IP TIMESTAMP option [3] added to ICMP ECHO. [1]

## [](#OPTIONS)OPTIONS

           -o
               Use IP TIMESTAMP with ICMP ECHO instead of ICMP TIMESTAMP
               messages. It is useful with some destinations, which do not
               support ICMP TIMESTAMP (f.e. Solaris <2.4).

           -o1
               Slightly different form of -o, namely it uses three-term IP
               TIMESTAMP with prespecified hop addresses instead of four term
               one. What flavor works better depends on target host.
               Particularly, -o is better for Linux.

           -T, --time-format ctime iso
               Print time stamp in output either ISO-8601 format or classical
               ctime format. The ctime format is default. The ISO time stamp
               includes timezone, and is easier to parse.

           -I
               Alias of --time-format iso option and argument.

           -h, --help
               Print help and exit.

           -V, --version
               Print version and exit.

## [](#WARNINGS)WARNINGS

               • Some nodes (Cisco) use non-standard timestamps, which is
               allowed by RFC, but makes timestamps mostly useless.

               • Some nodes generate messed timestamps (Solaris>2.4), when
               run xntpd. Seems, its IP stack uses a corrupted clock source,
               which is synchronized to time-of-day clock periodically and
               jumps randomly making timestamps mostly useless. Good news is
               that you can use NTP in this case, which is even better.

               • clockdiff shows difference in time modulo 24 days.

## [](#SEE_ALSO)SEE ALSO

           ping(8), arping(8), tracepath(8).

## [](#REFERENCES)REFERENCES

           [1] ICMP ECHO, RFC0792, page 14.

           [2] ICMP TIMESTAMP, RFC0792, page 16.

           [3] IP TIMESTAMP option, RFC0791, 3.1, page 16.

## [](#AUTHOR)AUTHOR

           clockdiff was compiled by Alexey Kuznetsov <kuznet@ms2.inr.ac.ru>.
           It was based on code borrowed from BSD timed daemon.

## [](#SECURITY)SECURITY

           clockdiff requires CAP_NET_RAW and CAP_SYS_NICE capabilities to be
           executed. It is safe to be used as set-uid root.

## [](#AVAILABILITY)AVAILABILITY

           clockdiff is part of iputils package.

## [](#COLOPHON)COLOPHON

           This page is part of the iputils (IP utilities) project.
           Information about the project can be found at 
           ⟨http://www.skbuff.net/iputils/⟩.  If you have a bug report for
           this manual page, send it to yoshfuji@skbuff.net,
           netdev@vger.kernel.org.  This page was obtained from the project's
           upstream Git repository ⟨https://github.com/iputils/iputils.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-16.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iputils 20250605                                             CLOCKDIFF(8)

------------------------------------------------------------------------

Pages that refer to this page: [arping(8)](../man8/arping.8.html)

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
