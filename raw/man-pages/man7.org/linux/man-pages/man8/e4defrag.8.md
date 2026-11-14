---
{"title": "e4defrag(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/e4defrag.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# e4defrag(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    E4DEFRAG(8)              System Manager's Manual              E4DEFRAG(8)

## [](#NAME)NAME

           e4defrag - online defragmenter for ext4 file system

## [](#SYNOPSIS)SYNOPSIS

           e4defrag [ -c ] [ -v ] target ...

## [](#DESCRIPTION)DESCRIPTION

           e4defrag reduces fragmentation of extent based file. The file
           targeted by e4defrag is created on ext4 file system made with "-O
           extent" option (see mke2fs(8)).  The targeted file gets more
           contiguous blocks and improves the file access speed.

           target is a regular file, a directory, or a device that is mounted
           as ext4 file system.  If target is a directory, e4defrag reduces
           fragmentation of all files in it. If target is a device, e4defrag
           gets the mount point of it and reduces fragmentation of all files
           in this mount point.

## [](#OPTIONS)OPTIONS

           -c     Get a current fragmentation count and an ideal
                  fragmentation count, and calculate fragmentation score
                  based on them. By seeing this score, we can determine
                  whether we should execute e4defrag to target.  When used
                  with -v option, the current fragmentation count and the
                  ideal fragmentation count are printed for each file.

                  Also this option outputs the average data size in one
                  extent. If you see it, you'll find the file has ideal
                  extents or not. Note that the maximum extent size is
                  131072KB in ext4 file system (if block size is 4KB).

                  If this option is specified, target is never defragmented.

           -v     Print error messages and the fragmentation count before and
                  after defrag for each file.

## [](#NOTES)NOTES

           e4defrag does not support swap file, files in lost+found
           directory, and files allocated in indirect blocks. When target is
           a device or a mount point, e4defrag doesn't defragment files in
           mount point of other device.

           It is safe to run e4defrag on a file while it is actively in use
           by another application.  Since the contents of file blocks are
           copied using the page cache, this can result in a performance
           slowdown to both e4defrag and the application due to contention
           over the system's memory and disk bandwidth.

           If the file system's free space is fragmented, or if there is
           insufficient free space available, e4defrag may not be able to
           improve the file's fragmentation.

           Non-privileged users can execute e4defrag to their own file, but
           the score is not printed if -c option is specified. Therefore, it
           is desirable to be executed by root user.

## [](#AUTHOR)AUTHOR

           Written by Akira Fujita <a-fujita@rs.jp.nec.com> and Takashi Sato
           <t-sato@yk.jp.nec.com>.

## [](#SEE_ALSO)SEE ALSO

           mke2fs(8), mount(8).

## [](#COLOPHON)COLOPHON

           This page is part of the e2fsprogs (utilities for ext2/3/4
           filesystems) project.  Information about the project can be found
           at ⟨http://e2fsprogs.sourceforge.net/⟩.  It is not known how to
           report bugs for this man page; if you know, please send a mail to
           man-pages@man7.org.  This page was obtained from the project's
           upstream Git repository
           ⟨git://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git⟩ on
           2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-04-03.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    e4defrag version 2.0             May 2009                     E4DEFRAG(8)

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
