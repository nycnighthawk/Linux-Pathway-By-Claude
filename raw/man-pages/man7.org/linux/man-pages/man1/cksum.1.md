---
{"title": "cksum(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cksum.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cksum(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CKSUM(1)                      User Commands                      CKSUM(1)

## [](#NAME)NAME

           cksum - compute and verify file checksums

## [](#SYNOPSIS)SYNOPSIS

           cksum [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           Print or verify checksums.  By default use the 32 bit CRC
           algorithm.

           With no FILE, or when FILE is -, read standard input.

           Mandatory arguments to long options are mandatory for short
           options too.

           -a, --algorithm=TYPE
                  select the digest type to use.  See DIGEST below

           --base64
                  emit base64-encoded digests, not hexadecimal

           -c, --check
                  read checksums from the FILEs and check them

           -l, --length=BITS
                  digest length in bits; must not exceed the max size and
                  must be a multiple of 8 for blake2b; must be 224, 256, 384,
                  or 512 for sha2 or sha3

           --raw  emit a raw binary digest, not hexadecimal

           --tag  create a BSD-style checksum (the default)

           --untagged
                  create a reversed style checksum, without digest type

           -z, --zero
                  end each output line with NUL, not newline, and disable
                  file name escaping

       The following five options are useful only when verifying checksums:
           --ignore-missing
                  don't fail or report status for missing files

           --quiet
                  don't print OK for each successfully verified file

           --status
                  don't output anything, status code shows success

           --strict
                  exit non-zero for improperly formatted checksum lines

           -w, --warn
                  warn about improperly formatted checksum lines

           --debug
                  indicate which implementation used

           --help display this help and exit

           --version
                  output version information and exit

       DIGEST determines the digest algorithm and default output format:
           sysv   (equivalent to sum -s)

           bsd    (equivalent to sum -r)

           crc    (equivalent to cksum)

           crc32b (only available through cksum)

           md5    (equivalent to md5sum)

           sha1   (equivalent to sha1sum)

           sha2   (equivalent to sha{224,256,384,512}sum)

           sha3   (only available through cksum)

           blake2b
                  (equivalent to b2sum)

           sm3    (only available through cksum)

           When checking, the input should be a former output of this
           program, or equivalent standalone program.

## [](#AUTHOR)AUTHOR

           Written by Padraig Brady and Q. Frank Xia.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to: bug-coreutils@gnu.org
           GNU coreutils home page: <https://www.gnu.org/software/coreutils/>
           General help using GNU software: <https://www.gnu.org/gethelp/>
           Report any translation bugs to
           <https://translationproject.org/team/>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2026 Free Software Foundation, Inc.  License GPLv3+:
           GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
           This is free software: you are free to change and redistribute it.
           There is NO WARRANTY, to the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           Full documentation <https://www.gnu.org/software/coreutils/cksum>
           or available locally via: info '(coreutils) cksum invocation'

## [](#COLOPHON)COLOPHON

           This page is part of the coreutils (basic file, shell and text
           manipulation utilities) project.  Information about the project
           can be found at ⟨http://www.gnu.org/software/coreutils/⟩.  If you
           have a bug report for this manual page, see
           ⟨http://www.gnu.org/software/coreutils/⟩.  This page was obtained
           from the tarball coreutils-9.11.tar.xz fetched from
           ⟨http://ftp.gnu.org/gnu/coreutils/⟩ on 2026-08-03.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    GNU coreutils 9.11              April 2026                       CKSUM(1)

------------------------------------------------------------------------

Pages that refer to this page: [b2sum(1)](../man1/b2sum.1.html),  [md5sum(1)](../man1/md5sum.1.html),  [sha1sum(1)](../man1/sha1sum.1.html),  [sha224sum(1)](../man1/sha224sum.1.html),  [sha256sum(1)](../man1/sha256sum.1.html),  [sha384sum(1)](../man1/sha384sum.1.html),  [sha512sum(1)](../man1/sha512sum.1.html)

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
