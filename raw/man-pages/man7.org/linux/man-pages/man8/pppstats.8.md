---
{"title": "pppstats(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pppstats.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pppstats(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PPPSTATS(8)              System Manager's Manual              PPPSTATS(8)

## [](#NAME)NAME

           pppstats - print PPP statistics

## [](#SYNOPSIS)SYNOPSIS

           pppstats [ -a ] [ -d ] [ -v ] [ -r ] [ -z ] [ -c <count> ] [ -w
           <secs> ] [ interface ]

## [](#DESCRIPTION)DESCRIPTION

           The pppstats utility reports PPP-related statistics at regular
           intervals for the specified PPP interface.  If the interface is
           unspecified, it will default to ppp0.  The display is split
           horizontally into input and output sections containing columns of
           statistics describing the properties and volume of packets
           received and transmitted by the interface.

           The options are as follows:

           -a     Display absolute values rather than deltas.  With this
                  option, all reports show statistics for the time since the
                  link was initiated.  Without this option, the second and
                  subsequent reports show statistics for the time since the
                  last report.

           -d     Show data rate (kB/s) instead of bytes.

           -c count
                  Repeat the display count times.  If this option is not
                  specified, the default repeat count is 1 if the -w option
                  is not specified, otherwise infinity.

           -r     Display additional statistics summarizing the compression
                  ratio achieved by the packet compression algorithm in use.

           -v     Display additional statistics relating to the performance
                  of the Van Jacobson TCP header compression algorithm.

           -w wait
                  Pause wait seconds between each display.  If this option is
                  not specified, the default interval is 5 seconds.

           -z     Instead of the standard display, show statistics indicating
                  the performance of the packet compression algorithm in use.

           The following fields are printed on the input side when the -z
           option is not used:

           IN     The total number of bytes received by this interface.

           PACK   The total number of packets received by this interface.

           VJCOMP The number of header-compressed TCP packets received by
                  this interface.

           VJUNC  The number of header-uncompressed TCP packets received by
                  this interface.  Not reported when the -r option is
                  specified.

           VJERR  The number of corrupted or bogus header-compressed TCP
                  packets received by this interface.  Not reported when the
                  -r option is specified.

           VJTOSS The number of VJ header-compressed TCP packets dropped on
                  reception by this interface because of preceding errors.
                  Only reported when the -v option is specified.

           NON-VJ The total number of non-TCP packets received by this
                  interface. Only reported when the -v option is specified.

           RATIO  The compression ratio achieved for received packets by the
                  packet compression scheme in use, defined as the
                  uncompressed size divided by the compressed size.  Only
                  reported when the -r option is specified.

           UBYTE  The total number of bytes received, after decompression of
                  compressed packets.  Only reported when the -r option is
                  specified.

           The following fields are printed on the output side:

           OUT    The total number of bytes transmitted from this interface.

           PACK   The total number of packets transmitted from this
                  interface.

           VJCOMP The number of TCP packets transmitted from this interface
                  with VJ-compressed TCP headers.

           VJUNC  The number of TCP packets transmitted from this interface
                  with VJ-uncompressed TCP headers.  Not reported when the -r
                  option is specified.

           NON-VJ The total number of non-TCP packets transmitted from this
                  interface.  Not reported when the -r option is specified.

           VJSRCH The number of searches for the cached header entry for a VJ
                  header compressed TCP packet.  Only reported when the -v
                  option is specified.

           VJMISS The number of failed searches for the cached header entry
                  for a VJ header compressed TCP packet.  Only reported when
                  the -v option is specified.

           RATIO  The compression ratio achieved for transmitted packets by
                  the packet compression scheme in use, defined as the size
                  before compression divided by the compressed size.  Only
                  reported when the -r option is specified.

           UBYTE  The total number of bytes to be transmitted, before packet
                  compression is applied.  Only reported when the -r option
                  is specified.

           When the -z option is specified, pppstats instead displays the
           following fields, relating to the packet compression algorithm
           currently in use.  If packet compression is not in use, these
           fields will all display zeroes.  The fields displayed on the input
           side are:

           COMPRESSED BYTE
                  The number of bytes of compressed packets received.

           COMPRESSED PACK
                  The number of compressed packets received.

           INCOMPRESSIBLE BYTE
                  The number of bytes of incompressible packets (that is,
                  those which were transmitted in uncompressed form)
                  received.

           INCOMPRESSIBLE PACK
                  The number of incompressible packets received.

           COMP RATIO
                  The recent compression ratio for incoming packets, defined
                  as the uncompressed size divided by the compressed size
                  (including both compressible and incompressible packets).

           The fields displayed on the output side are:

           COMPRESSED BYTE
                  The number of bytes of compressed packets transmitted.

           COMPRESSED PACK
                  The number of compressed packets transmitted.

           INCOMPRESSIBLE BYTE
                  The number of bytes of incompressible packets transmitted
                  (that is, those which were transmitted in uncompressed
                  form).

           INCOMPRESSIBLE PACK
                  The number of incompressible packets transmitted.

           COMP RATIO
                  The recent compression ratio for outgoing packets.

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

                                   26 June 1995                   PPPSTATS(8)

------------------------------------------------------------------------

Pages that refer to this page: [pppd(8)](../man8/pppd.8.html)

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
