---
{"title": "ranlib(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ranlib.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ranlib(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RANLIB(1)                 GNU Development Tools                 RANLIB(1)

## [](#NAME)NAME

           ranlib - generate an index to an archive

## [](#SYNOPSIS)SYNOPSIS

           ranlib [--plugin name] [-DhHvVt] archive

## [](#DESCRIPTION)DESCRIPTION

           ranlib generates an index to the contents of an archive and stores
           it in the archive.  The index lists each symbol defined by a
           member of an archive that is a relocatable object file.

           You may use nm -s or nm --print-armap to list this index.

           An archive with such an index speeds up linking to the library and
           allows routines in the library to call each other without regard
           to their placement in the archive.

           The GNU ranlib program is another form of GNU ar; running ranlib
           is completely equivalent to executing ar -s.

## [](#OPTIONS)OPTIONS

           -h
           -H
           --help
               Show usage information for ranlib.

           -v
           -V
           --version
               Show the version number of ranlib.

           -D  Operate in deterministic mode.  The symbol map archive
               member's header will show zero for the UID, GID, and
               timestamp.  When this option is used, multiple runs will
               produce identical output files.

               If binutils was configured with
               --enable-deterministic-archives, then this mode is on by
               default.  It can be disabled with the -U option, described
               below.

           -t  Update the timestamp of the symbol map of an archive.

           -U  Do not operate in deterministic mode.  This is the inverse of
               the -D option, above: the archive index will get actual UID,
               GID, timestamp, and file mode values.

               If binutils was configured without
               --enable-deterministic-archives, then this mode is on by
               default.

           @file
               Read command-line options from file.  The options read are
               inserted in place of the original @file option.  If file does
               not exist, or cannot be read, then the option will be treated
               literally, and not removed.

               Options in file are separated by whitespace.  A whitespace
               character may be included in an option by surrounding the
               entire option in either single or double quotes.  Any
               character (including a backslash) may be included by prefixing
               the character to be included with a backslash.  The file may
               itself contain additional @file options; any such options will
               be processed recursively.

## [](#SEE_ALSO)SEE ALSO

           ar(1), nm(1), and the Info entries for binutils.

## [](#COPYRIGHT)COPYRIGHT

           Copyright (c) 1991-2026 Free Software Foundation, Inc.

           Permission is granted to copy, distribute and/or modify this
           document under the terms of the GNU Free Documentation License,
           Version 1.3 or any later version published by the Free Software
           Foundation; with no Invariant Sections, with no Front-Cover Texts,
           and with no Back-Cover Texts.  A copy of the license is included
           in the section entitled "GNU Free Documentation License".

## [](#COLOPHON)COLOPHON

           This page is part of the binutils (a collection of tools for
           working with executable binaries) project.  Information about the
           project can be found at ⟨http://www.gnu.org/software/binutils/⟩.
           If you have a bug report for this manual page, see
           ⟨http://sourceware.org/bugzilla/enter_bug.cgi?product=binutils⟩.
           This page was obtained from the tarball binutils-with-
           gold-2.46.1.tar.gz fetched from
           ⟨https://ftp.gnu.org/gnu/binutils/⟩ on 2026-08-03.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    binutils-2.46.1                 2026-08-03                      RANLIB(1)

------------------------------------------------------------------------

Pages that refer to this page: [ar(1)](../man1/ar.1.html),  [nm(1)](../man1/nm.1.html),  [strings(1)](../man1/strings.1.html)

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
