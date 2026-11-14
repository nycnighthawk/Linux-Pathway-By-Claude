---
{"title": "rpm-payloadflags(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/rpm-payloadflags.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-payloadflags(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-PAYLOADFLAGS(7)  Miscellaneous Information Manual RPM-PAYLOADFLAGS(7)

## [](#NAME)NAME

           rpm-payloadflags - RPM payload flags

## [](#SYNOPSIS)SYNOPSIS

           w[FLAGS].TYPE

## [](#DESCRIPTION)DESCRIPTION

           The payload flags determine how the payload of an RPM package is
           compressed when the package is built. The flags are stored in the
           Payloadcompressor and Payloadflags tags of the package header,
           which are used to determine how to uncompress the payload contents
           during installation.

           The peculiar syntax is directly inherited from librpm's Fopen() IO
           API, where w means opening a file for writing.

           The following compression types are supported, but availability
           may vary depending on how RPM was compiled.

           ┌────────┬───────────────────────────────────────────────────────┐
           │  TYPE  │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ ufdio  │ uncompressed                                          │
           ├────────┼───────────────────────────────────────────────────────┤
           │ gzdio  │ gzip (aka zlib)                                       │
           ├────────┼───────────────────────────────────────────────────────┤
           │ bzdio  │ bzip2                                                 │
           ├────────┼───────────────────────────────────────────────────────┤
           │ xzdio  │ xz                                                    │
           ├────────┼───────────────────────────────────────────────────────┤
           │ lzdio  │ legacy lzma                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ zstdio │ zstd                                                  │
           └────────┴───────────────────────────────────────────────────────┘

           The compression FLAGS must be listed in the following order and
           can be any of:

           ┌────────┬───────────────────────────────────────┬───────────────┐
           │ FLAGS  │ Description                           │     Types     │
           ├────────┼───────────────────────────────────────┼───────────────┤
           │ <0-9>  │ compression level                     │  all (ufdio   │
           │        │                                       │  ignores)     │
           ├────────┼───────────────────────────────────────┼───────────────┤
           │ T[0-N] │ number of threads (no number or 0 =   │ xzdio, zstdio │
           │        │ autodetect)                           │               │
           ├────────┼───────────────────────────────────────┼───────────────┤
           │ L<0-9> │ window size(see --long in zstd(1))    │    zstdio     │
           └────────┴───────────────────────────────────────┴───────────────┘

           If a flag is omitted, the compressor's default value will be used.

           A higher compression level generally means better compression
           ratio at the cost of increased resource use and compression times.

           T is equivalent to T0 and causes the number of threads to be
           automatically detected. Note that while using threads can speed up
           compression considerably, it typically causes the compression
           ratio to go down, and make the output less predictable.

## [](#EXAMPLES)EXAMPLES

           ┌──────────────┬─────────────────────────────────────────────────┐
           │ Mode         │ Description                                     │
           ├──────────────┼─────────────────────────────────────────────────┤
           │ w9.gzdio     │ gzip level 9, default for package payload       │
           ├──────────────┼─────────────────────────────────────────────────┤
           │ w9.bzdio     │ bzip2 level 9, bzip2's default                  │
           ├──────────────┼─────────────────────────────────────────────────┤
           │ w.xzdio      │ xz default level                                │
           ├──────────────┼─────────────────────────────────────────────────┤
           │ w7T16.xzdio  │ xz level 7 using 16 threads                     │
           ├──────────────┼─────────────────────────────────────────────────┤
           │ w7T0.xzdio   │ xz level 7, autodetect no. of threads           │
           ├──────────────┼─────────────────────────────────────────────────┤
           │ w6.lzdio     │ lzma (legacy) level 6, lzma's default           │
           ├──────────────┼─────────────────────────────────────────────────┤
           │ w19T8.zstdio │ zstd level 19 using 8 threads                   │
           ├──────────────┼─────────────────────────────────────────────────┤
           │ w7T.zstdio   │ zstd level 7, autodetect no. of threads         │
           ├──────────────┼─────────────────────────────────────────────────┤
           │ w.ufdio      │ uncompressed                                    │
           └──────────────┴─────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           rpmbuild-config(5), rpm-config(5)

           http://www.rpm.org/ 

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03            RPM-PAYLOADFLAGS(7)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild-config(5)](../man5/rpmbuild-config.5.html),  [rpm-lua(7)](../man7/rpm-lua.7.html)

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
