---
{"title": "pppdump(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pppdump.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pppdump(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PPPDUMP(8)               System Manager's Manual               PPPDUMP(8)

## [](#NAME)NAME

           pppdump - convert PPP record file to readable format

## [](#SYNOPSIS)SYNOPSIS

           pppdump [ -h | -p [ -d ]] [ -r ] [ -a ] [ -m mru ] [ file ...  ]

## [](#DESCRIPTION)DESCRIPTION

           The pppdump utility converts the files written using the record
           option of pppd into a human-readable format.  If one or more
           filenames are specified, pppdump will read each in turn; otherwise
           it will read its standard input.  In each case the result is
           written to standard output.

           The options are as follows:

           -h     Prints the bytes sent and received in hexadecimal.  If
                  neither this option nor the -p option is specified, the
                  bytes are printed as the characters themselves, with non-
                  printing and non-ASCII characters printed as escape
                  sequences.

           -p     Collects the bytes sent and received into PPP packets,
                  interpreting the async HDLC framing and escape characters
                  and checking the FCS (frame check sequence) of each packet.
                  The packets are printed as hex values and as characters
                  (non-printable characters are printed as `.').

           -d     With the -p option, this option causes pppdump to
                  decompress packets which have been compressed with the BSD-
                  Compress or Deflate methods.

           -r     Reverses the direction indicators, so that `sent' is
                  printed for bytes or packets received, and `rcvd' is
                  printed for bytes or packets sent.

           -a     Prints absolute times.

           -m mru Use mru as the MRU (maximum receive unit) for both
                  directions of the link when checking for over-length PPP
                  packets (with the -p option).

## [](#SEE_ALSO)SEE ALSO

           pppd(8)

## [](#COLOPHON)COLOPHON

           This page is part of the ppp (An implementation of the Point-to-
           Point Protocol (PPP)) project.  Information about the project can
           be found at ⟨https://ppp.samba.org/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://github.com/paulusmack/ppp/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/paulusmack/ppp⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-25.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                   1 April 1999                    PPPDUMP(8)

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
