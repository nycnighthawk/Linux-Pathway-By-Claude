---
{"title": "pathname(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/pathname.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pathname(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    pathname(7)          Miscellaneous Information Manual         pathname(7)

## [](#NAME)NAME

           pathname, filename - how pathnames are encoded and interpreted

## [](#DESCRIPTION)DESCRIPTION

           Some system calls allow you to pass a pathname as a parameter.
           When writing code that deals with pathnames, there are kernel-
           space requirements that you must comply with, and user-space
           requirements that you should comply with.

           The kernel stores pathnames as C strings, that is, sequences of
           non-null bytes terminated by a null byte.  There are a few general
           rules that apply to all pathnames:

           •  The last byte in the sequence needs to be a null byte.

           •  Any other bytes in the sequence need to be non-null bytes.

           •  A 0x2F byte ('/') is always interpreted as a directory
              separator, and cannot be part of a filename.

           •  A pathname can be at most PATH_MAX bytes long (see
              limits.h(0p)).  A pathname that's longer than PATH_MAX bytes
              can be split into multiple smaller pathnames and opened
              piecewise using openat(2).

           •  A filename can be at most a certain number of bytes long.  The
              number is filesystem-specific (see _PC_NAME_MAX in
              fpathconf(3)).  For maximum portability, programs should be
              able to handle filenames that are as long as the relevant
              filesystems will allow.  For maximum portability, programs and
              users should limit the length of their own pathnames to
              NAME_MAX bytes (see limits.h(0p)).

           Some filesystems or APIs may apply further restrictions, such as
           requiring shorter filenames, or restricting the allowed bytes in a
           filename.

           For maximum interoperability, programs and users should also limit
           the characters that they use for their own pathnames to characters
           in the POSIX Portable Filename Character Set
           ⟨https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html#tag_03_265⟩.

## [](#VERSIONS)VERSIONS

           POSIX.1-2024 encourages implementations to disallow creation of
           filenames containing new-line characters.  Linux doesn't follow
           this, and allows using new-line characters.

## [](#SEE_ALSO)SEE ALSO

           limits.h(0p), open(2), fpathconf(3), path_resolution(7), mount(8)

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

    Linux man-pages 6.19            2026-02-08                    pathname(7)

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
