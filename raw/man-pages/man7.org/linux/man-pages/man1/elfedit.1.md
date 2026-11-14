---
{"title": "elfedit(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/elfedit.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# elfedit(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ELFEDIT(1)                GNU Development Tools                ELFEDIT(1)

## [](#NAME)NAME

           elfedit - update ELF header and program property of ELF files

## [](#SYNOPSIS)SYNOPSIS

           elfedit [--input-mach=machine]
                   [--input-type=type]
                   [--input-osabi=osabi]
                   [--input-abiversion=version]
                   --output-mach=machine
                   --output-type=type
                   --output-osabi=osabi
                   --output-abiversion=version
                   --enable-x86-feature=feature
                   --disable-x86-feature=feature
                   [-v|--version]
                   [-h|--help]
                   elffile...

## [](#DESCRIPTION)DESCRIPTION

           elfedit updates the ELF header and program property of ELF files
           which have the matching ELF machine and file types.  The options
           control how and which fields in the ELF header and program
           property should be updated.

           elffile... are the ELF files to be updated.  32-bit and 64-bit ELF
           files are supported, as are archives containing ELF files.

## [](#OPTIONS)OPTIONS

           The long and short forms of options, shown here as alternatives,
           are equivalent. At least one of the --output-mach, --output-type,
           --output-osabi, --output-abiversion, --enable-x86-feature and
           --disable-x86-feature options must be given.

           --input-mach=machine
               Set the matching input ELF machine type to machine.  If
               --input-mach isn't specified, it will match any ELF machine
               types.

               The supported ELF machine types are, i386, IAMCU, L1OM, K1OM
               and x86-64.

           --output-mach=machine
               Change the ELF machine type in the ELF header to machine.  The
               supported ELF machine types are the same as --input-mach.

           --input-type=type
               Set the matching input ELF file type to type.  If --input-type
               isn't specified, it will match any ELF file types.

               The supported ELF file types are, rel, exec and dyn.

           --output-type=type
               Change the ELF file type in the ELF header to type.  The
               supported ELF types are the same as --input-type.

           --input-osabi=osabi
               Set the matching input ELF file OSABI to osabi.  If
               --input-osabi isn't specified, it will match any ELF OSABIs.

               The supported ELF OSABIs are, none, HPUX, NetBSD, GNU, Linux
               (alias for GNU), Solaris, AIX, Irix, FreeBSD, TRU64, Modesto,
               OpenBSD, OpenVMS, NSK, AROS and FenixOS.

           --output-osabi=osabi
               Change the ELF OSABI in the ELF header to osabi.  The
               supported ELF OSABI are the same as --input-osabi.

           --input-abiversion=version
               Set the matching input ELF file ABIVERSION to version.
               version must be between 0 and 255.  If --input-abiversion
               isn't specified, it will match any ELF ABIVERSIONs.

           --output-abiversion=version
               Change the ELF ABIVERSION in the ELF header to version.
               version must be between 0 and 255.

           --enable-x86-feature=feature
               Set the feature bit in program property in exec or dyn ELF
               files with machine types of i386 or x86-64.  The supported
               features are, ibt, shstk, lam_u48 and lam_u57.

           --disable-x86-feature=feature
               Clear the feature bit in program property in exec or dyn ELF
               files with machine types of i386 or x86-64.  The supported
               features are the same as --enable-x86-feature.

               Note: --enable-x86-feature and --disable-x86-feature are
               available only on hosts with mmap support.

           -v
           --version
               Display the version number of elfedit.

           -h
           --help
               Display the command-line options understood by elfedit.

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

           readelf(1), and the Info entries for binutils.

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

    binutils-2.46.1                 2026-08-03                     ELFEDIT(1)

------------------------------------------------------------------------

Pages that refer to this page: [elf(5)](../man5/elf.5.html)

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
