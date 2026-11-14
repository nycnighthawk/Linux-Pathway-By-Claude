---
{"title": "stat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stat(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAT(1)                       User Commands                       STAT(1)

## [](#NAME)NAME

           stat - display file or file system status

## [](#SYNOPSIS)SYNOPSIS

           stat [OPTION]... FILE...

## [](#DESCRIPTION)DESCRIPTION

           Display file or file system status.

           Mandatory arguments to long options are mandatory for short
           options too.

           -L, --dereference
                  follow links

           -f, --file-system
                  display file system status instead of file status

           --cached=MODE
                  specify how to use cached attributes; useful on remote file
                  systems. See MODE below

           -c, --format=FORMAT
                  use the specified FORMAT instead of the default; output a
                  newline after each use of FORMAT

           --printf=FORMAT
                  like --format, but interpret backslash escapes, and do not
                  output a mandatory trailing newline; if you want a newline,
                  include \n in FORMAT

           -t, --terse
                  print the information in terse form

           --help display this help and exit

           --version
                  output version information and exit

           The MODE argument of --cached can be: always, never, or default.
           'always' will use cached attributes if available, while 'never'
           will try to synchronize with the latest attributes, and 'default'
           will leave it up to the underlying file system.

           The valid format sequences for files (without --file-system):

           %a     permission bits in octal (see '#' and '0' printf flags)

           %A     permission bits and file type in human readable form

           %b     number of blocks allocated (see %B)

           %B     the size in bytes of each block reported by %b

           %C     SELinux security context string

           %d     device number in decimal (st_dev)

           %D     device number in hex (st_dev)

           %Hd    major device number in decimal

           %Ld    minor device number in decimal

           %f     raw mode in hex

           %F     file type

           %g     group ID of owner

           %G     group name of owner

           %h     number of hard links

           %i     inode number

           %m     mount point

           %n     file name

           %N     quoted file name with dereference if symbolic link

           %o     optimal I/O transfer size hint

           %s     total size, in bytes

           %r     device type in decimal (st_rdev)

           %R     device type in hex (st_rdev)

           %Hr    major device type in decimal, for character/block device
                  special files

           %Lr    minor device type in decimal, for character/block device
                  special files

           %t     major device type in hex, for character/block device
                  special files

           %T     minor device type in hex, for character/block device
                  special files

           %u     user ID of owner

           %U     user name of owner

           %w     time of file birth, human-readable; - if unknown

           %W     time of file birth, seconds since Epoch; 0 if unknown

           %x     time of last access, human-readable

           %X     time of last access, seconds since Epoch

           %y     time of last data modification, human-readable

           %Y     time of last data modification, seconds since Epoch

           %z     time of last status change, human-readable

           %Z     time of last status change, seconds since Epoch

           Valid format sequences for file systems:

           %a     free blocks available to non-superuser

           %b     total data blocks in file system

           %c     total file nodes in file system

           %d     free file nodes in file system

           %f     free blocks in file system

           %i     file system ID in hex

           %l     maximum length of filenames

           %n     file name

           %s     block size (for faster transfers)

           %S     fundamental block size (for block counts)

           %t     file system type in hex

           %T     file system type in human readable form

       --terse is equivalent to the following FORMAT:
                  %n %s %b %f %u %g %D %i %h %t %T %X %Y %Z %W %o %C

       --terse --file-system is equivalent to the following FORMAT:
                  %n %i %l %t %s %S %b %f %a %c %d

           Your shell may have its own version of stat, which usually
           supersedes the version described here.  Please refer to your
           shell's documentation for details about the options it supports.

## [](#AUTHOR)AUTHOR

           Written by Michael Meskes.

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

           stat(2), statfs(2), statx(2)

           Full documentation <https://www.gnu.org/software/coreutils/stat>
           or available locally via: info '(coreutils) stat invocation'

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

    GNU coreutils 9.11              April 2026                        STAT(1)

------------------------------------------------------------------------

Pages that refer to this page: [namei(1)](../man1/namei.1.html),  [stat(2)](../man2/stat.2.html),  [statx(2)](../man2/statx.2.html),  [inode(7)](../man7/inode.7.html)

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
