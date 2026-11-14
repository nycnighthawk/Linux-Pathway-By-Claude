---
{"title": "xfs_info(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xfs_info.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xfs_info(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xfs_info(8)              System Manager's Manual              xfs_info(8)

## [](#NAME)NAME

           xfs_info - display XFS filesystem geometry information

## [](#SYNOPSIS)SYNOPSIS

           xfs_info [ -t mtab ] [ mount-point | block-device | file-image ]
           xfs_info -V

## [](#DESCRIPTION)DESCRIPTION

           xfs_info displays geometry information about an existing XFS
           filesystem.  The mount-point argument is the pathname of a
           directory where the filesystem is mounted.  The block-device or
           file-image contain a raw XFS filesystem.  The existing contents of
           the filesystem are undisturbed.

## [](#OPTIONS)OPTIONS

           -t     Specifies an alternate mount table file (default is
                  /proc/mounts if it exists, else /etc/mtab).  This is used
                  when working with filesystems mounted without writing to
                  /etc/mtab file - refer to mount(8) for further details.
                  This option has no effect with the block-device or file-
                  image parameters.

           -V     Prints the version number and exits. The mount-point
                  argument is not required with -V.

## [](#EXAMPLES)EXAMPLES

           Understanding xfs_info output.

           Suppose one has the following "xfs_info /dev/sda" output:

             meta-data=/dev/pmem0             isize=512    agcount=8, agsize=5974144 blks
                      =                       sectsz=512   attr=2, projid32bit=1
                      =                       crc=1        finobt=1, sparse=1, rmapbt=1
                      =                       reflink=1
             data     =                       bsize=4096   blocks=47793152, imaxpct=25
                      =                       sunit=32     swidth=128 blks
             naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
             log      =internal log           bsize=4096   blocks=23336, version=2
                      =                       sectsz=512   sunit=0 blks, lazy-count=1
             realtime =none                   extsz=4096   blocks=0, rtextents=0

           Here, the data section of the output indicates "bsize=4096",
           meaning the data block size for this filesystem is 4096 bytes.
           This section also shows "sunit=32 swidth=128 blks", which means
           the stripe unit is 32*4096 bytes = 128 kibibytes and the stripe
           width is 128*4096 bytes = 512 kibibytes.  A single stripe of this
           filesystem therefore consists of four stripe units (128 blocks /
           32 blocks per unit).

## [](#SEE_ALSO)SEE ALSO

           mkfs.xfs(8), md(4), lvm(8), mount(8).

## [](#COLOPHON)COLOPHON

           This page is part of the xfsprogs (utilities for XFS filesystems)
           project.  Information about the project can be found at 
           ⟨http://xfs.org/⟩.  If you have a bug report for this manual page,
           send it to linux-xfs@vger.kernel.org.  This page was obtained from
           the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/fs/xfs/xfsprogs-dev.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-17.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                                                  xfs_info(8)

------------------------------------------------------------------------

Pages that refer to this page: [xfsctl(3)](../man3/xfsctl.3.html),  [xfs(5)](../man5/xfs.5.html),  [fsadm(8)](../man8/fsadm.8.html),  [xfs_db(8)](../man8/xfs_db.8.html),  [xfs_growfs(8)](../man8/xfs_growfs.8.html),  [xfs_spaceman(8)](../man8/xfs_spaceman.8.html)

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
