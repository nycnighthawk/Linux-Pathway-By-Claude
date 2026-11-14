---
{"title": "du(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/du.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# du(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PATTERNS](#PATTERNS) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DU(1)                         User Commands                         DU(1)

## [](#NAME)NAME

           du - estimate file space usage

## [](#SYNOPSIS)SYNOPSIS

           du [OPTION]... [FILE]...
           du [OPTION]... --files0-from=F

## [](#DESCRIPTION)DESCRIPTION

           Summarize device usage of the set of FILEs, recursively for
           directories.

           Mandatory arguments to long options are mandatory for short
           options too.

           -0, --null
                  end each output line with NUL, not newline

           -a, --all
                  write counts for all files, not just directories

           -A, --apparent-size
                  print apparent sizes rather than device usage; although the
                  apparent size is usually smaller, it may be larger due to
                  holes in ('sparse') files, internal fragmentation, indirect
                  blocks, etc.

           -B, --block-size=SIZE
                  scale sizes by SIZE before printing them; See SIZE format
                  below; E.g., '-BM' prints sizes in units of 1,048,576 bytes

           -b, --bytes
                  equivalent to '--apparent-size --block-size=1'

           -c, --total
                  produce a grand total

           -D, --dereference-args
                  dereference only symlinks that are listed on the command
                  line

           -d, --max-depth=N
                  print the total for a directory (or file, with --all) only
                  if it is N or fewer levels below the command line argument;
                  --max-depth=0 is the same as --summarize

           --files0-from=F
                  summarize device usage of the NUL-terminated file names
                  specified in file F;  if F is -, read names from standard
                  input

           -H     equivalent to --dereference-args (-D)

           -h, --human-readable
                  print sizes in human readable format (e.g., 1K 234M 2G)

           --inodes
                  list inode usage information instead of block usage

           -k     like --block-size=1K

           -L, --dereference
                  dereference all symbolic links

           -l, --count-links
                  count sizes many times if hard linked

           -m     like --block-size=1M

           -P, --no-dereference
                  don't follow any symbolic links (this is the default)

           -S, --separate-dirs
                  for directories do not include size of subdirectories

           --si   like -h, but use powers of 1000 not 1024

           -s, --summarize
                  display only a total for each argument

           -t, --threshold=SIZE
                  exclude entries smaller than SIZE if positive, or entries
                  greater than SIZE if negative

           --time show time of the last modification of any file in the
                  directory, or any of its subdirectories

           --time=WORD
                  show time as WORD instead of modification time: atime,
                  access, use, ctime or status

           --time-style=STYLE
                  time/date format with --time; see TIME_STYLE below

           -X, --exclude-from=FILE
                  exclude files that match any pattern in FILE

           --exclude=PATTERN
                  exclude files that match PATTERN

           -x, --one-file-system
                  skip directories on different file systems

           --help display this help and exit

           --version
                  output version information and exit

           Display values are in units of the first available SIZE from
           --block-size, and the DU_BLOCK_SIZE, BLOCK_SIZE and BLOCKSIZE
           environment variables.  Otherwise, units default to 1024 bytes (or
           512 if POSIXLY_CORRECT is set).

           The SIZE argument is an integer and optional unit (example: 10K is
           10*1024).  Units are K,M,G,T,P,E,Z,Y,R,Q (powers of 1024) or
           KB,MB,... (powers of 1000).  Binary prefixes can be used, too:
           KiB=K, MiB=M, and so on.

           The --time-style STYLE argument can be full-iso, long-iso, iso, or
           +FORMAT.  FORMAT is interpreted like in date(1).  Also the
           TIME_STYLE environment variable sets the default style to use.

## [](#PATTERNS)PATTERNS

           PATTERN is a shell pattern (not a regular expression).  The
           pattern ? matches any one character, whereas * matches any string
           (composed of zero, one or multiple characters).  For example, *.o
           will match any files whose names end in .o.  Therefore, the
           command

                  du --exclude='*.o'

           will skip all files and subdirectories ending in .o (including the
           file .o itself).

## [](#AUTHOR)AUTHOR

           Written by Torbjorn Granlund, David MacKenzie, Paul Eggert, and
           Jim Meyering.

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

           Full documentation <https://www.gnu.org/software/coreutils/du>
           or available locally via: info '(coreutils) du invocation'

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

    GNU coreutils 9.11              April 2026                          DU(1)

------------------------------------------------------------------------

Pages that refer to this page: [tmpfs(5)](../man5/tmpfs.5.html),  [symlink(7)](../man7/symlink.7.html)

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
