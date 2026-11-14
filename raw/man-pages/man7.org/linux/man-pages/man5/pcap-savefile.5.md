---
{"title": "pcap-savefile(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/pcap-savefile.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcap-savefile(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    PCAP-SAVEFILE(5)           File Formats Manual           PCAP-SAVEFILE(5)

## [](#NAME)NAME

           pcap-savefile - libpcap savefile format

## [](#DESCRIPTION)DESCRIPTION

           NOTE: applications and libraries should, if possible, use libpcap
           to read savefiles, rather than having their own code to read
           savefiles.  If, in the future, a new file format is supported by
           libpcap, applications and libraries using libpcap to read
           savefiles will be able to read the new format of savefiles, but
           applications and libraries using their own code to read savefiles
           will have to be changed to support the new file format.

           ``Savefiles'' read and written by libpcap and applications using
           libpcap start with a per-file header.  The format of the per-file
           header is:
                  ┌───────────────────────────────────────────────────┐
                  │                   Magic number                    │
                  ├─────────────────────────┬─────────────────────────┤
                  │      Major version      │      Minor version      │
                  ├─────────────────────────┴─────────────────────────┤
                  │                     Reserved1                     │
                  ├───────────────────────────────────────────────────┤
                  │                     Reserved2                     │
                  ├───────────────────────────────────────────────────┤
                  │                  Snapshot length                  │
                  ├───────────────────────────────────────────────────┤
                  │ Link-layer header type and additional information │
                  └───────────────────────────────────────────────────┘

           The per-file header length is 24 octets.

           All fields in the per-file header are in the byte order of the
           host writing the file.  Normally, the first field in the per-file
           header is a 4-byte magic number, with the value 0xa1b2c3d4.  The
           magic number, when read by a host with the same byte order as the
           host that wrote the file, will have the value 0xa1b2c3d4, and,
           when read by a host with the opposite byte order as the host that
           wrote the file, will have the value 0xd4c3b2a1.  That allows
           software reading the file to determine whether the byte order of
           the host that wrote the file is the same as the byte order of the
           host on which the file is being read, and thus whether the values
           in the per-file and per-packet headers need to be byte-swapped.

           If the magic number has the value 0xa1b23c4d (with the two nibbles
           of the two lower-order bytes of the magic number swapped), which
           would be read as 0xa1b23c4d by a host with the same byte order as
           the host that wrote the file and as 0x4d3cb2a1 by a host with the
           opposite byte order as the host that wrote the file, the file
           format is the same as for regular files, except that the time
           stamps for packets are given in seconds and nanoseconds rather
           than seconds and microseconds.

           Following this are:

                  A 2-byte file format major version number; the current
                  version number is 2 (big-endian 0x00 0x02 or little-endian
                  0x02 0x00).

                  A 2-byte file format minor version number; the current
                  version number is 4 (big-endian 0x00 0x04 or little-endian
                  0x04 0x00).

                  A 4-byte not used - SHOULD be filled with 0 by pcap file
                  writers, and MUST be ignored by pcap file readers.  This
                  value was documented by some older implementations as "GMT
                  to local correction" or "time zone offset".  Some older
                  pcap file writers stored non-zero values in this field.

                  A 4-byte not used - SHOULD be filled with 0 by pcap file
                  writers, and MUST be ignored by pcap file readers.  This
                  value was documented by some older implementations as
                  "accuracy of timestamps".  Some older pcap file writers
                  stored non-zero values in this field.

                  A 4-byte number giving the "snapshot length" of the
                  capture; packets longer than the snapshot length are
                  truncated to the snapshot length.  Specifically, when
                  libpcap is writing to a savefile (from a live packet
                  capture or otherwise), if the savefile's snapshot length is
                  N, it writes to the savefile only the first N bytes of a
                  packet longer than N bytes; when libpcap is reading from a
                  savefile, it delivers at most N bytes for any packet in the
                  savefile.  Other software that needs to access savefiles
                  directly should implement the same logic.

                  A 4-byte number giving the link-layer header type for
                  packets in the capture and optional additional information.

                  This format of this field is:

                                1                   2                   3
            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
           |FCS len|R|P|     Reserved3     |        Link-layer type        |
           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

                  The field is shown as if it were in the byte order of the
                  host reading or writing the file, with bit 0 being the
                  most-significant bit of the field and bit 31 being the
                  least-significant bit of the field.

                  Link-layer type (16 bits): A 16-bit value giving the link-
                  layer header type for packets in the file; see
                  pcap-linktype(7) for the LINKTYPE_ values that can appear
                  in this field.

                  Reserved3 (10 bits): not used - MUST be set to zero by pcap
                  writers, and MUST NOT be interpreted by pcap readers; a
                  reader SHOULD treat a non-zero value as an error.

                  P (1 bit): A bit that, if set, indicates that the Frame
                  Check Sequence (FCS) length value is present and, if not
                  set, indicates that the FCS value is not present.

                  R (1 bit): not used - MUST be set to zero by pcap writers,
                  and MUST NOT be interpreted by pcap readers; a reader
                  SHOULD treat a non-zero value as an error.

                  FCS len (4 bits): A 4-bit unsigned value giving the number
                  of 16-bit (2-octet) words of FCS that are appended to each
                  packet, if the P bit is set; if the P bit is not set, and
                  the FCS length is not indicated by the link-layer type
                  value, the FCS length is unknown.  The valid values of the
                  FCS len field are between 0 and 15; Ethernet, for example,
                  would have an FCS length value of 2, corresponding to a
                  4-octet FCS.

           Following the per-file header are zero or more packets; each
           packet begins with a per-packet header, which is immediately
           followed by the raw packet data.  The format of the per-packet
           header is:
                  ┌───────────────────────────────────────────────┐
                  │           Time stamp, seconds value           │
                  ├───────────────────────────────────────────────┤
                  │ Time stamp, microseconds or nanoseconds value │
                  ├───────────────────────────────────────────────┤
                  │        Length of captured packet data         │
                  ├───────────────────────────────────────────────┤
                  │    Un-truncated length of the packet data     │
                  └───────────────────────────────────────────────┘

           The per-packet header length is 16 octets.

           All fields in the per-packet header are in the byte order of the
           host writing the file.  The per-packet header begins with a time
           stamp giving the approximate time the packet was captured; the
           time stamp consists of a 4-byte value, giving the time in seconds
           since January 1, 1970, 00:00:00 UTC, followed by a 4-byte value,
           giving the time in microseconds or nanoseconds since that second,
           depending on the magic number in the file header.  Following that
           are a 4-byte value giving the number of bytes of captured data
           that follow the per-packet header and a 4-byte value giving the
           number of bytes that would have been present had the packet not
           been truncated by the snapshot length.  The two lengths will be
           equal if the number of bytes of packet data are less than or equal
           to the snapshot length.

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

                                   21 Jan 2025               PCAP-SAVEFILE(5)

------------------------------------------------------------------------

Pages that refer to this page: [pcap_dump_fopen(3pcap)](../man3/pcap_dump_fopen.3pcap.html),  [pcap_dump_open(3pcap)](../man3/pcap_dump_open.3pcap.html),  [pcap_fopen_offline(3pcap)](../man3/pcap_fopen_offline.3pcap.html),  [pcap_fopen_offline_with_tstamp_precision(3pcap)](../man3/pcap_fopen_offline_with_tstamp_precision.3pcap.html),  [pcap_open_offline(3pcap)](../man3/pcap_open_offline.3pcap.html),  [pcap_open_offline_with_tstamp_precision(3pcap)](../man3/pcap_open_offline_with_tstamp_precision.3pcap.html)

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
