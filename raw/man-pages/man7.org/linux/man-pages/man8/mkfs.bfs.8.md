---
{"title": "mkfs.bfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mkfs.bfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mkfs.bfs(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MKFS.BFS(8)               System Administration               MKFS.BFS(8)

## [](#NAME)NAME

           mkfs.bfs - make an SCO bfs filesystem

## [](#SYNOPSIS)SYNOPSIS

           mkfs.bfs [options] device [block-count]

## [](#DESCRIPTION)DESCRIPTION

           mkfs.bfs creates an SCO bfs filesystem on a block device (usually
           a disk partition or a file accessed via the loop device).

           The block-count parameter is the desired size of the filesystem,
           in blocks. If nothing is specified, the entire partition will be
           used.

## [](#OPTIONS)OPTIONS

           -N, --inodes number
               Specify the desired number of inodes (at most 512). If nothing
               is specified, some default number in the range 48-512 is
               picked depending on the size of the partition.

           -V, --vname label
               Specify the volume label. I have no idea if/where this is
               used.

           -F, --fname name
               Specify the filesystem name. I have no idea if/where this is
               used.

           --lock[=mode]
               Use an exclusive BSD lock for the device or file that is
               operated upon. The optional argument mode can be yes (1), no
               (0), or nonblock. If the mode argument is omitted, it defaults
               to yes. This option overrides the environment variable
               $LOCK_BLOCK_DEVICE. The default is to not use any lock at all,
               but using a lock is recommended to avoid collisions with
               systemd-udevd(8) or other tools.

           -v, --verbose
               Explain what is being done.

           -c
               This option is silently ignored.

           -l
               This option is silently ignored.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit. Option -V only works as --version
               when it is the only option.

## [](#ENVIRONMENT)ENVIRONMENT

           LOCK_BLOCK_DEVICE=<mode>
               Use exclusive BSD lock. The mode is "1" or "0". See --lock for
               more details.

## [](#EXIT_STATUS)EXIT STATUS

           The exit status returned by mkfs.bfs is 0 when all went well, and
           1 when something went wrong.

## [](#SEE_ALSO)SEE ALSO

           mkfs(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The mkfs.bfs command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                    MKFS.BFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [mkfs(8)](../man8/mkfs.8.html)

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
