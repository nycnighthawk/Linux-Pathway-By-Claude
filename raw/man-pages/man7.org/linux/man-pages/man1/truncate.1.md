---
{"title": "truncate(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/truncate.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# truncate(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRUNCATE(1)                   User Commands                   TRUNCATE(1)

## [](#NAME)NAME

           truncate - shrink or extend the size of a file to the specified
           size

## [](#SYNOPSIS)SYNOPSIS

           truncate OPTION... FILE...

## [](#DESCRIPTION)DESCRIPTION

           Shrink or extend the size of each FILE to the specified size

           A FILE argument that does not exist is created.

           If a FILE is larger than the specified size, the extra data is
           lost.  If a FILE is shorter, it is extended and the sparse
           extended part (hole) reads as zero bytes.

           Mandatory arguments to long options are mandatory for short
           options too.

           -c, --no-create
                  do not create any files

           -o, --io-blocks
                  treat SIZE as number of IO blocks instead of bytes

           -r, --reference=RFILE
                  base size on RFILE

           -s, --size=SIZE
                  set or adjust the file size by SIZE bytes

           --help display this help and exit

           --version
                  output version information and exit

           The SIZE argument is an integer and optional unit (example: 10K is
           10*1024).  Units are K,M,G,T,P,E,Z,Y,R,Q (powers of 1024) or
           KB,MB,... (powers of 1000).  Binary prefixes can be used, too:
           KiB=K, MiB=M, and so on.

           SIZE may also be prefixed by one of the following modifying
           characters: '+' extend by, '-' reduce by, '<' at most, '>' at
           least, '/' round down to multiple of, '%' round up to multiple of.

## [](#AUTHOR)AUTHOR

           Written by Padraig Brady.

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

           dd(1), truncate(2), ftruncate(2)

           Full documentation
           <https://www.gnu.org/software/coreutils/truncate>
           or available locally via: info '(coreutils) truncate invocation'

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

    GNU coreutils 9.11              April 2026                    TRUNCATE(1)

------------------------------------------------------------------------

Pages that refer to this page: [fallocate(1)](../man1/fallocate.1.html),  [truncate(2)](../man2/truncate.2.html),  [swapon(8)](../man8/swapon.8.html)

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
