---
{"title": "sha512sum(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/sha512sum.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sha512sum(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SHA512SUM(1)                  User Commands                  SHA512SUM(1)

## [](#NAME)NAME

           sha512sum - compute and check SHA512 message digest

## [](#SYNOPSIS)SYNOPSIS

           sha512sum [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           Print or check SHA512 (512-bit) checksums.  Legacy interface to
           the cksum utility.

           With no FILE, or when FILE is -, read standard input.

           -b, --binary
                  read in binary mode

           -c, --check
                  read checksums from the FILEs and check them

           --tag  create a BSD-style checksum

           -t, --text
                  read in text mode (default)

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

           --help display this help and exit

           --version
                  output version information and exit

           The sums are computed as described in FIPS-180-2.  When checking,
           the input should be a former output of this program.  The default
           mode is to print a line with: checksum, a space, a character
           indicating input mode ('*' for binary, ' ' for text or where
           binary is insignificant), and name for each FILE.

           There is no difference between binary mode and text mode on GNU
           systems.

## [](#AUTHOR)AUTHOR

           Written by Ulrich Drepper, Scott Miller, and David Madore.

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

           cksum(1)

           Full documentation
           <https://www.gnu.org/software/coreutils/sha512sum>
           or available locally via: info '(coreutils) sha2 utilities'

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

    GNU coreutils 9.11              April 2026                   SHA512SUM(1)

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
