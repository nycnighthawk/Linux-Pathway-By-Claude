---
{"title": "pcap-linktype(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/pcap-linktype.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcap-linktype(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    PCAP-LINKTYPE(7)     Miscellaneous Information Manual    PCAP-LINKTYPE(7)

## [](#NAME)NAME

           pcap-linktype - link-layer header types supported by libpcap

## [](#DESCRIPTION)DESCRIPTION

           For a live capture or ``savefile'', libpcap supplies, as the
           return value of the pcap_datalink(3PCAP) routine, a value that
           indicates the type of link-layer header at the beginning of the
           packets it provides.  This is not necessarily the type of link-
           layer header that the packets being captured have on the network
           from which they're being captured; for example, packets from an
           IEEE 802.11 network might be provided by libpcap with Ethernet
           headers that the network adapter or the network adapter driver
           generates from the 802.11 headers.  The names for those values
           begin with DLT_, so they are sometimes called "DLT_ values".

           The pcap_datalink_val_to_name(3PCAP) and
           pcap_datalink_name_to_val(3PCAP) routines can be used to translate
           between DLT_ values and names.  Some capture devices support more
           than one link-layer header type.  The pcap_list_datalinks(3PCAP)
           routine can be used to retrieve the supported link-layer header
           types of a capture device and the pcap_set_datalink(3PCAP) routine
           can be used to change the link-layer header type of a capture
           device.

           The values stored in the link-layer header type field in the
           savefile header are, in most but not all cases, the same as the
           values returned by pcap_datalink().  The names for those values
           begin with LINKTYPE_.

           The link-layer header types supported by libpcap are described at
           https://www.tcpdump.org/linktypes.html .

## [](#SEE_ALSO)SEE ALSO

           pcap(3PCAP)

## [](#COLOPHON)COLOPHON

           This page is part of the libpcap (packet capture library) project.
           Information about the project can be found at 
           ⟨http://www.tcpdump.org/⟩.  If you have a bug report for this
           manual page, see ⟨http://www.tcpdump.org/#patches⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/the-tcpdump-group/libpcap.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                  1 October 2024             PCAP-LINKTYPE(7)

------------------------------------------------------------------------

Pages that refer to this page: [pcap_datalink(3pcap)](../man3/pcap_datalink.3pcap.html),  [pcap_free_datalinks(3pcap)](../man3/pcap_free_datalinks.3pcap.html),  [pcap_list_datalinks(3pcap)](../man3/pcap_list_datalinks.3pcap.html),  [pcap_open_dead(3pcap)](../man3/pcap_open_dead.3pcap.html),  [pcap_open_dead_with_tstamp_precision(3pcap)](../man3/pcap_open_dead_with_tstamp_precision.3pcap.html),  [pcap-savefile(5)](../man5/pcap-savefile.5.html)

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
