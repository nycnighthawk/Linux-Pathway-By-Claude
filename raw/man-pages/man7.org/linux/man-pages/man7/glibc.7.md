---
{"title": "libc(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/glibc.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# libc(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    libc(7)              Miscellaneous Information Manual             libc(7)

## [](#NAME)NAME

           libc - overview of standard C libraries on Linux

## [](#DESCRIPTION)DESCRIPTION

           The term “libc” is commonly used as a shorthand for the “standard
           C library” a library of standard functions that can be used by all
           C programs (and sometimes by programs in other languages).
           Because of some history (see below), use of the term “libc” to
           refer to the standard C library is somewhat ambiguous on Linux.

       glibc
           By far the most widely used C library on Linux is the GNU C
           Library ⟨http://www.gnu.org/software/libc/⟩, often referred to as
           glibc.  This is the C library that is nowadays used in all major
           Linux distributions.  It is also the C library whose details are
           documented in the relevant pages of the man-pages project
           (primarily in Section 3 of the manual).  Documentation of glibc is
           also available in the glibc manual, available via the command info
           libc.  Release 1.0 of glibc was made in September 1992.  (There
           were earlier 0.x releases.)  The next major release of glibc was
           2.0, at the beginning of 1997.

           The pathname /lib/libc.so.6 (or something similar) is normally a
           symbolic link that points to the location of the glibc library,
           and executing this pathname will cause glibc to display various
           information about the version installed on your system.

       Linux libc
           In the early to mid 1990s, there was for a while Linux libc, a
           fork of glibc 1.x created by Linux developers who felt that glibc
           development at the time was not sufficing for the needs of Linux.
           Often, this library was referred to (ambiguously) as just “libc”.
           Linux libc released major versions 2, 3, 4, and 5, as well as many
           minor versions of those releases.  Linux libc4 was the last
           version to use the a.out binary format, and the first version to
           provide (primitive) shared library support.  Linux libc 5 was the
           first version to support the ELF binary format; this version used
           the shared library soname libc.so.5.  For a while, Linux libc was
           the standard C library in many Linux distributions.

           However, notwithstanding the original motivations of the Linux
           libc effort, by the time glibc 2.0 was released (in 1997), it was
           clearly superior to Linux libc, and all major Linux distributions
           that had been using Linux libc soon switched back to glibc.  To
           avoid any confusion with Linux libc versions, glibc 2.0 and later
           used the shared library soname libc.so.6.

           Since the switch from Linux libc to glibc 2.0 occurred long ago,
           man-pages no longer takes care to document Linux libc details.
           Nevertheless, the history is visible in vestiges of information
           about Linux libc that remain in a few manual pages, in particular,
           references to libc4 and libc5.

       Other C libraries
           There are various other less widely used C libraries for Linux.
           These libraries are generally smaller than glibc, both in terms of
           features and memory footprint, and often intended for building
           small binaries, perhaps targeted at development for embedded Linux
           systems.  Among such libraries are uClibc
           ⟨http://www.uclibc.org/⟩, dietlibc ⟨http://www.fefe.de/dietlibc/⟩,
           and musl libc ⟨http://www.musl-libc.org/⟩.  Details of these
           libraries are covered by the man-pages project, where they are
           known.

## [](#SEE_ALSO)SEE ALSO

           syscalls(2), getauxval(3), proc(5), feature_test_macros(7),
           man-pages(7), standards(7), vdso(7)

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

    Linux man-pages 6.19            2025-12-25                        libc(7)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [intro(3)](../man3/intro.3.html),  [feature_test_macros(7)](../man7/feature_test_macros.7.html),  [standards(7)](../man7/standards.7.html)

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
