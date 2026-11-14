---
{"title": "standards(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/standards.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# standards(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    standards(7)         Miscellaneous Information Manual        standards(7)

## [](#NAME)NAME

           standards - C and UNIX Standards

## [](#DESCRIPTION)DESCRIPTION

           The STANDARDS section that appears in many manual pages identifies
           various standards to which the documented interface conforms.  The
           following list briefly describes these standards.

       Research Unix
           V7     Version 7 (also known as Seventh Edition) UNIX, released by
                  AT&T/Bell Labs in 1979.  After this point, UNIX systems
                  diverged into two main dialects: BSD and System V.  Sources
                  are available online
                  ⟨https://www.tuhs.org/cgi-bin/utree.pl?file=V7⟩.

       BSD
           4.2BSD This is an implementation standard defined by the 4.2
                  release of the Berkeley Software Distribution, released by
                  the University of California at Berkeley.  This was the
                  first Berkeley release that contained a TCP/IP stack and
                  the sockets API.  4.2BSD was released in 1983.  Sources are
                  available online
                  ⟨https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD⟩.

                  Earlier major BSD releases included 3BSD (1980), 4BSD
                  (1980), and 4.1BSD (1981).

           4.3BSD The successor to 4.2BSD, released in 1986.  Sources are
                  available online
                  ⟨https://www.tuhs.org/cgi-bin/utree.pl?file=4.3BSD⟩.

           4.4BSD The successor to 4.3BSD, released in 1993.  This was the
                  last major Berkeley release.  Sources are available online
                  ⟨https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD⟩.

       Unix/TS
           Unix/TS 4
                  This was an internal release of Unix that was never
                  released to the public (in which case it would have been
                  called System IV).  The previous major AT&T release was
                  System III, released in 1981.

           System V (SVr1)
                  This is an implementation standard defined by AT&T's
                  milestone 1983 release of its commercial System V (five)
                  release.

           System V release 2 (SVr2)
                  This was the next System V release, made in 1985.  The SVr2
                  was formally described in the System V Interface Definition
                  Issue 1 (SVID 1) published in 1985.

           System V release 3 (SVr3)
                  This was the successor to SVr2, released in 1986.  This
                  release was formally described in the System V Interface
                  Definition Issue 2 (SVID 2)
                  ⟨https://bitsavers.org/pdf/att/unix/SVID/System_V_Interface_Definition_Issue_2_Volume_1_1986.pdf⟩.

           System V release 4 (SVr4)
                  This was the successor to SVr3, released in 1989.  This
                  version of System V is described in the "Programmer's
                  Reference Manual: Operating System API (Intel processors)"
                  (Prentice-Hall 1992, ISBN 0-13-951294-2) This release was
                  formally described in the System V Interface Definition
                  Third Edition (SVID 3)
                  ⟨https://archive.org/details/systemvinterface0001unse/⟩,
                  and is considered the definitive System V release.

           SVID 4 System V Interface Definition version 4, issued in 1995.
                  Available online at
                  ⟨http://www.sco.com/developers/devspecs/⟩.

       Standard C
           K&R    This refers to the C language as specified in “The C
                  Programming Language” [Brian W. Kernighan and Dennis M.
                  Ritchie; Prentice Hall; 1st Ed., 1978].

           C89    This was the first C language standard, ratified by ANSI
                  (American National Standards Institute) in 1989
                  (X3.159-1989).  Sometimes this is known as ANSI C, but
                  since C99 is also an ANSI standard, this term is ambiguous.
                  It is available online
                  ⟨https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub160.pdf⟩.

                  The rationale for the C89 standard is also available online
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/C89Rationale.pdf⟩.

                  This standard was also ratified by ISO (International
                  Standards Organization) and IEC (International
                  Electrotechnical Commision) in 1990 (ISO/IEC 9899:1990),
                  and is thus occasionally referred to as ISO C90.

           C94    Technical Corrigendum 1
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/tc1.htm⟩
                  of C90 was ratified by ISO/IEC in 1994
                  (ISO/IEC 9899:1990/Cor1:1994).

           C95    This amendment of the C language standard was ratified by
                  ISO/IEC in 1995 (ISO/IEC 9899:1990/Amd1:1995).  A draft is
                  available online
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/n412.pdf⟩.

                  The primary change in C95 was support for international
                  character sets.

           C96    Technical Corrigendum 2
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/tc2.htm⟩
                  of C90 was ratified by ISO/IEC in 1996
                  (ISO/IEC 9899:1990/Cor2:1996).  A draft is available online
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/n457.pdf⟩.

           C99    This revision of the C language standard was ratified by
                  ISO/IEC in 1999 (ISO/IEC 9899:1999).

                  Technical Corrigendum 1
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/9899tc1/n32071.PDF⟩
                  of C99 was ratified by ISO/IEC in 2001
                  (ISO/IEC 9899:1999/Cor1:2001).

                  Technical Corrigendum 2
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/9899-1999_cor_2-2004.pdf⟩
                  of C99 was ratified by ISO/IEC in 2004
                  (ISO/IEC 9899:1999/Cor2:2004).

                  Technical Corrigendum 3
                  ⟨https://www.open-std.org/JTC1/SC22/WG14/www/docs/n1235.pdf⟩
                  of C99 was ratified by ISO/IEC in 2007
                  (ISO/IEC 9899:1999/Cor3:2007).  A draft is available online
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf⟩.

                  The rationale for the C99 standard is also available online
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/C99RationaleV5.10.pdf⟩.

           C11    This revision of the C language standard was ratified by
                  ISO/IEC in 2011 (ISO/IEC 9899:2011).  A draft is available
                  online
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf⟩.

                  Technical Corrigendum 1
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1606.pdf⟩
                  of C11 was ratified by ISO/IEC in 2012
                  (ISO/IEC 9899:2011/Cor1:2012).

           C17    This revision of the C language standard was ratified by
                  ISO/IEC in 2018 (ISO/IEC 9899:2018).  A draft is available
                  online
                  ⟨https://web.archive.org/web/20181230041359if_/http://www.open-std.org/jtc1/sc22/wg14/www/abq/c17_updated_proposed_fdis.pdf⟩.

           C23    This revision of the C language standard was ratified by
                  ISO/IEC in 2024 (ISO/IEC 9899:2024).  A draft is available
                  online
                  ⟨https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3220.pdf⟩.

       POSIX and SUS
           POSIX.1-1988
                  This was the first POSIX standard, ratified by IEEE in 1998
                  (IEEE Std 1003.1-1988).  The term "POSIX" was coined by
                  Richard Stallman.  It is available online
                  ⟨https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub151-1.pdf⟩.

           POSIX.1-1990
                  Part 1, "Portable Operating System Interface for Computing
                  Environments".  Ratified by IEEE in 1990,
                  (IEEE Std 1003.1-1990), and ratified by ISO/IEC in 1990
                  (ISO/IEC 9945-1:1990).  It is available online
                  ⟨https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub151-2.pdf⟩.

           POSIX.2
                  Part 2, which describes commands and utilities.  Ratified
                  by IEEE in 1992 (IEEE Std 1003.2-1992), and ratified by
                  ISO/IEC in 1993 (ISO/IEC 9945-2:1993).

           POSIX.1b (formerly known as POSIX.4)
                  Part 1b, which describes real-time facilities for portable
                  operating systems.  Ratified by IEEE in 1993
                  (IEEE Std 1003.1b-1993).

           POSIX.1c (formerly known as POSIX.4a)
                  Part 1c, which describes the POSIX threads interfaces.
                  Ratified by IEEE in 1995 (IEEE Std 1003.1c-1995).

           POSIX.1d
                  Part 1d, which describes additional real-time extensions.
                  Ratified by IEEE in 1999 (IEEE Std 1003.1d-1999).

           POSIX.1g
                  Part 1g, which describes networking APIs (including
                  sockets).  Ratified by IEEE in 2000
                  (IEEE Std 1003.1g-2000).

           POSIX.1j
                  Part 1j, which describes advanced real-time extensions.
                  Ratified by IEEE in 2000 (IEEE Std 1003.1j-2000).

           POSIX.1-1996
                  A revision of POSIX.1 which incorporated POSIX.1b and
                  POSIX.1c.  Ratified by ISO/IEC in 1996
                  (ISO/IEC 9945-1:1996).

           XPG3   Released in 1989, this was the first release of the X/Open
                  Portability Guide to be based on a POSIX standard
                  (POSIX.1-1988).  It is also known as Issue 3.  This
                  multivolume guide was developed by the X/Open Group, a
                  multivendor consortium.

           XPG4   A revision of the X/Open Portability Guide, released in
                  1992.  It is also known as Issue 4.  This revision
                  incorporated POSIX.2.

           XPG4v2 A 1994 revision of XPG4.  This is also referred to as
                  Spec 1170, where 1170 referred to the number of interfaces
                  defined by this standard.

           SUS (SUSv1)
                  Single UNIX Specification.  This was a repackaging of
                  XPG4v2 and other X/Open standards (X/Open Curses Issue 4
                  version 2, X/Open Networking Service (XNS) Issue 4).
                  Systems conforming to this standard can be branded UNIX 95.

           SUSv2  Single UNIX Specification version 2.  Sometimes also
                  referred to as Issue 5.  This standard appeared in 1997.
                  Systems conforming to this standard can be branded UNIX 98.
                  See also ⟨http://www.unix.org/version2/⟩.)

           POSIX.1-2001
           SUSv3  This was a 2001 revision and consolidation of the POSIX.1,
                  POSIX.2, and SUS standards into a single document,
                  conducted under the auspices of the Austin Group
                  ⟨http://www.opengroup.org/austin/⟩.  The standard is
                  available online at ⟨http://www.unix.org/version3/⟩.

                  The standard defines two levels of conformance: POSIX
                  conformance, which is a baseline set of interfaces required
                  of a conforming system; and XSI Conformance, which
                  additionally mandates a set of interfaces (the "XSI
                  extension") which are only optional for POSIX conformance.
                  XSI-conformant systems can be branded UNIX 03.

                  The POSIX.1-2001 document is broken into four parts:

                  XBD: Definitions, terms, and concepts, header file
                  specifications.

                  XSH: Specifications of functions (i.e., system calls and
                  library functions in actual implementations).

                  XCU: Specifications of commands and utilities (i.e., the
                  area formerly described by POSIX.2).

                  XRAT: Informative text on the other parts of the standard.

                  POSIX.1-2001 is aligned with C99, so that all of the
                  library functions standardized in C99 are also standardized
                  in POSIX.1-2001.

                  The Single UNIX Specification version 3 (SUSv3) comprises
                  the Base Specifications containing XBD, XSH, XCU, and XRAT
                  as above, plus X/Open Curses Issue 4 version 2 as an extra
                  volume that is not in POSIX.1-2001.

           POSIX.1-2001 2002 edition
                  Technical Corrigendum 1 of POSIX.1-2001 was ratified by
                  IEEE in 2002 (IEEE Std 1003.1-2001/Cor1-2002).

                  This is informally known as POSIX.1-2002.

           POSIX.1-2001 2004 edition
                  Technical Corrigendum 2 of POSIX.1-2001 was ratified by
                  IEEE in 2004 (IEEE Std 1003.1-2001/Cor2-2004).  It is
                  available online
                  ⟨https://pubs.opengroup.org/onlinepubs/009695399/⟩.

                  This is informally known as POSIX.1-2004.

           POSIX.1-2008
           SUSv4  Work on the next revision of POSIX.1/SUS was completed and
                  ratified in 2008.  The standard is available online at
                  ⟨http://www.unix.org/version4/⟩, and also here
                  ⟨https://pubs.opengroup.org/onlinepubs/9699919799.2008edition/⟩.

                  The changes in this revision are not as large as those that
                  occurred for POSIX.1-2001/SUSv3, but a number of new
                  interfaces are added and various details of existing
                  specifications are modified.  Many of the interfaces that
                  were optional in POSIX.1-2001 become mandatory in the 2008
                  revision of the standard.  A few interfaces that are
                  present in POSIX.1-2001 are marked as obsolete in
                  POSIX.1-2008, or removed from the standard altogether.

                  The revised standard is structured in the same way as its
                  predecessor.  The Single UNIX Specification version 4
                  (SUSv4) comprises the Base Specifications containing XBD,
                  XSH, XCU, and XRAT, plus X/Open Curses Issue 7 as an extra
                  volume that is not in POSIX.1-2008.

                  Again there are two levels of conformance: the baseline
                  POSIX Conformance, and XSI Conformance, which mandates an
                  additional set of interfaces beyond those in the base
                  specification.

                  In general, where the STANDARDS section of a manual page
                  lists POSIX.1-2001, it can be assumed that the interface
                  also conforms to POSIX.1-2008, unless otherwise noted.

                  Further information can be found on the Austin Group web
                  site, ⟨http://www.opengroup.org/austin/⟩.

           POSIX.1-2008 2013 edition
                  Technical Corrigendum 1 of POSIX.1-2008 was ratified by
                  IEEE in 2013 (IEEE Std 1003.1-2008/Cor1-2013).  It is
                  available online
                  ⟨https://pubs.opengroup.org/onlinepubs/9699919799.2013edition/⟩.

                  This is informally known as POSIX.1-2013.

           POSIX.1-2008 2016 edition
                  Technical Corrigendum 2 of POSIX.1-2008 was ratified by
                  IEEE in 2016 (IEEE Std 1003.1-2008/Cor2-2016).  It is
                  available online
                  ⟨https://pubs.opengroup.org/onlinepubs/9699919799.2016edition/⟩.

           SUSv4 2016 edition
                  This is equivalent to POSIX.1-2008 2016 edition, with the
                  addition of the XCurses specification.

           POSIX.1-2017
                  This revision of POSIX is technically identical to
                  POSIX.1-2008 2016 edition.  Ratified by IEEE in 2017
                  (IEEE Std 1003.1-2017).  It is available online
                  ⟨https://pubs.opengroup.org/onlinepubs/9699919799/⟩.

           SUSv4 2018 edition
                  This is equivalent to POSIX.1-2017, with the addition of
                  the XCurses specification.

           POSIX.1-2024
           SUSv5  Work on the next revision of POSIX.1/SUS was completed and
                  ratified by IEEE in 2024 (IEEE Std 1003.1-2024).  It is
                  available online
                  ⟨https://pubs.opengroup.org/onlinepubs/9799919799/⟩.

                  POSIX.1-2024 is aligned with C17, so that all of the
                  library functions standardized in C17 are also standardized
                  in POSIX.1-2024.

                  Further information can be found on the Austin Group web
                  site ⟨http://www.opengroup.org/austin/⟩.

           The interfaces documented in POSIX.1/SUS are available as manual
           pages under sections 0p (header files), 1p (commands), and 3p
           (functions); thus one can write man 3p open.

       Other standards
           LFS    The Large File Summit specification, completed in 1996.
                  This specification defined mechanisms that allowed 32-bit
                  systems to support the use of large files (i.e., 64-bit
                  file offsets).  See
                  ⟨https://www.opengroup.org/platform/lfs.html⟩.

## [](#SEE_ALSO)SEE ALSO

           getconf(1), confstr(3), pathconf(3), sysconf(3), attributes(7),
           feature_test_macros(7), libc(7), posixoptions(7),
           system_data_types(7)

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

    Linux man-pages 6.19            2026-08-03                   standards(7)

------------------------------------------------------------------------

Pages that refer to this page: [intro(2)](../man2/intro.2.html),  [intro(3)](../man3/intro.3.html),  [matherr(3)](../man3/matherr.3.html),  [intro(4)](../man4/intro.4.html),  [intro(5)](../man5/intro.5.html),  [feature_test_macros(7)](../man7/feature_test_macros.7.html),  [intro(7)](../man7/intro.7.html),  [libc(7)](../man7/libc.7.html),  [man-pages(7)](../man7/man-pages.7.html),  [nptl(7)](../man7/nptl.7.html),  [posixoptions(7)](../man7/posixoptions.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [system_data_types(7)](../man7/system_data_types.7.html)

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
