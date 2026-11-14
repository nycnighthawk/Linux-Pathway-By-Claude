---
{"title": "sync(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/sync.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sync(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [BUGS](#BUGS) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYNC(1)                       User Commands                       SYNC(1)

## [](#NAME)NAME

           sync - Synchronize cached writes to persistent storage

## [](#SYNOPSIS)SYNOPSIS

           sync [OPTION] [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           Synchronize cached writes to persistent storage

           If one or more files are specified, sync only them, or their
           containing file systems.

           -d, --data
                  sync only file data, no unneeded metadata

           -f, --file-system
                  sync the file systems that contain the files

           --help display this help and exit

           --version
                  output version information and exit

## [](#BUGS)BUGS

           Persistence guarantees vary per system.  See the system calls
           below for more details.

## [](#AUTHOR)AUTHOR

           Written by Jim Meyering and Giuseppe Scrivano.

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

           fdatasync(2), fsync(2), sync(2), syncfs(2)

           Full documentation <https://www.gnu.org/software/coreutils/sync>
           or available locally via: info '(coreutils) sync invocation'

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

    GNU coreutils 9.11              April 2026                        SYNC(1)

------------------------------------------------------------------------

Pages that refer to this page: [bdflush(2)](../man2/bdflush.2.html),  [fsync(2)](../man2/fsync.2.html),  [Q_XQUOTASYNC(2const)](../man2/Q_XQUOTASYNC.2const.html),  [sync(2)](../man2/sync.2.html),  [proc_sys_vm(5)](../man5/proc_sys_vm.5.html),  [btrfs-filesystem(8)](../man8/btrfs-filesystem.8.html)

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
