---
{"title": "ls(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ls.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ls(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LS(1)                         User Commands                         LS(1)

## [](#NAME)NAME

           ls - list directory contents

## [](#SYNOPSIS)SYNOPSIS

           ls [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           List information about the FILEs (the current directory by
           default).  Sort entries alphabetically if none of -cftuvSUX nor
           --sort is specified.

           Mandatory arguments to long options are mandatory for short
           options too.

           -a, --all
                  do not ignore entries starting with .

           -A, --almost-all
                  do not list implied . and ..

           --author
                  with -l, print the author of each file

           -b, --escape
                  print C-style escapes for nongraphic characters

           --block-size=SIZE
                  with -l, scale sizes by SIZE when printing them; e.g.,
                  '--block-size=M'; see SIZE format below

           -B, --ignore-backups
                  do not list implied entries ending with ~

           -c     with -lt: sort by, and show, ctime (time of last change of
                  file status information); with -l: show ctime and sort by
                  name; otherwise: sort by ctime, newest first

           -C     list entries by columns

           --color[=WHEN]
                  color the output WHEN; more info below

           -d, --directory
                  list directories themselves, not their contents

           -D, --dired
                  generate output designed for Emacs' dired mode

           -f     same as -a -U

           -F, --classify[=WHEN]
                  append indicator (one of */=>@|) to entries WHEN

           --file-type
                  like -F, except do not append '*'

           --format=WORD
                  across,horizontal (-x), commas (-m), long (-l),
                  single-column (-1), verbose (-l), vertical (-C)

           --full-time
                  like -l --time-style=full-iso

           -g     like -l, but do not list owner

           --group-directories-first
                  group directories before files

           -G, --no-group
                  in a long listing, don't print group names

           -h, --human-readable
                  with -l and -s, print sizes like 1K 234M 2G etc.

           --si   likewise, but use powers of 1000 not 1024

           -H, --dereference-command-line
                  follow symbolic links listed on the command line

           --dereference-command-line-symlink-to-dir
                  follow each command line symbolic link that points to a
                  directory

           --hide=PATTERN
                  do not list implied entries matching shell PATTERN
                  (overridden by -a or -A)

           --hyperlink[=WHEN]
                  hyperlink file names WHEN

           --indicator-style=WORD
                  append indicator with style WORD to entry names: none
                  (default), slash (-p), file-type (--file-type), classify
                  (-F)

           -i, --inode
                  print the index number of each file

           -I, --ignore=PATTERN
                  do not list implied entries matching shell PATTERN

           -k, --kibibytes
                  default to 1024-byte blocks for file system usage; used
                  only with -s and per directory totals

           -l     use a long listing format

           -L, --dereference
                  when showing file information for a symbolic link, show
                  information for the file the link references rather than
                  for the link itself

           -m     fill width with a comma separated list of entries

           -n, --numeric-uid-gid
                  like -l, but list numeric user and group IDs

           -N, --literal
                  print entry names without quoting

           -o     like -l, but do not list group information

           -p, --indicator-style=slash
                  append / indicator to directories

           -q, --hide-control-chars
                  print ? instead of nongraphic characters

           --show-control-chars
                  show nongraphic characters as-is; the default, unless
                  program is 'ls' and output is a terminal

           -Q, --quote-name
                  enclose entry names in double quotes

           --quoting-style=WORD
                  use quoting style WORD for entry names: literal, locale,
                  shell, shell-always, shell-escape, shell-escape-always, c,
                  escape (overrides QUOTING_STYLE environment variable)

           -r, --reverse
                  reverse order while sorting

           -R, --recursive
                  list subdirectories recursively

           -s, --size
                  print the allocated size of each file, in blocks

           -S     sort by file size, largest first

           --sort=WORD
                  change default 'name' sort to WORD: none (-U), size (-S),
                  time (-t), version (-v), extension (-X), name, width

           --time=WORD
                  select which timestamp used to display or sort; access time
                  (-u): atime, access, use; metadata change time (-c): ctime,
                  status; modified time (default): mtime, modification; birth
                  time: birth, creation; with -l, WORD determines which time
                  to show; with --sort=time, sort by WORD (newest first)

           --time-style=TIME_STYLE
                  time/date format with -l; see TIME_STYLE below

           -t     sort by time, newest first; see --time

           -T, --tabsize=COLS
                  assume tab stops at each COLS instead of 8

           -u     with -lt: sort by, and show, access time; with -l: show
                  access time and sort by name; otherwise: sort by access
                  time, newest first

           -U     do not sort directory entries

           -v     natural sort of (version) numbers within text

           -w, --width=COLS
                  set output width to COLS.  0 means no limit

           -x     list entries by lines instead of by columns

           -X     sort alphabetically by entry extension

           -Z, --context
                  print any security context of each file

           --zero end each output line with NUL, not newline

           -1     list one file per line

           --help display this help and exit

           --version
                  output version information and exit

           The SIZE argument is an integer and optional unit (example: 10K is
           10*1024).  Units are K,M,G,T,P,E,Z,Y,R,Q (powers of 1024) or
           KB,MB,... (powers of 1000).  Binary prefixes can be used, too:
           KiB=K, MiB=M, and so on.

           The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or
           +FORMAT.  FORMAT is interpreted like in date(1).  If FORMAT is
           FORMAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files
           and FORMAT2 to recent files.  TIME_STYLE prefixed with 'posix-'
           takes effect only outside the POSIX locale.  Also the TIME_STYLE
           environment variable sets the default style to use.

           The WHEN argument defaults to 'always' and can also be 'auto' or
           'never'.

           Using color to distinguish file types is disabled both by default
           and with --color=never.  With --color=auto, ls emits color codes
           only when standard output is connected to a terminal.  The
           LS_COLORS environment variable can change the settings.  Use the
           dircolors(1) command to set it.

       Exit status:
           0      if OK,

           1      if minor problems (e.g., cannot access subdirectory),

           2      if serious trouble (e.g., cannot access command-line
                  argument).

## [](#AUTHOR)AUTHOR

           Written by Richard M. Stallman and David MacKenzie.

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

           dircolors(1)

           Full documentation <https://www.gnu.org/software/coreutils/ls>
           or available locally via: info '(coreutils) ls invocation'

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

    GNU coreutils 9.11              April 2026                          LS(1)

------------------------------------------------------------------------

Pages that refer to this page: [column(1)](../man1/column.1.html),  [find(1)](../man1/find.1.html),  [namei(1)](../man1/namei.1.html),  [pv(1)](../man1/pv.1.html),  [rpmdeps(1)](../man1/rpmdeps.1.html),  [stat(2)](../man2/stat.2.html),  [statx(2)](../man2/statx.2.html),  [glob(3)](../man3/glob.3.html),  [core(5)](../man5/core.5.html),  [dir_colors(5)](../man5/dir_colors.5.html),  [passwd(5)](../man5/passwd.5.html),  [proc(5)](../man5/proc.5.html),  [proc_pid_task(5)](../man5/proc_pid_task.5.html),  [mq_overview(7)](../man7/mq_overview.7.html),  [rpm-queryformat(7)](../man7/rpm-queryformat.7.html),  [symlink(7)](../man7/symlink.7.html),  [lsblk(8)](../man8/lsblk.8.html),  [lsof(8)](../man8/lsof.8.html),  [rpm(8)](../man8/rpm.8.html),  [setfiles(8)](../man8/setfiles.8.html)

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
