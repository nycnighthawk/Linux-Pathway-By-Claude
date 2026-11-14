---
{"title": "e2freefrag(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/e2freefrag.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# e2freefrag(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    E2FREEFRAG(8)            System Manager's Manual            E2FREEFRAG(8)

## [](#NAME)NAME

           e2freefrag - report free space fragmentation information

## [](#SYNOPSIS)SYNOPSIS

           e2freefrag [ -c chunk_kb ] [ -h ] filesys

## [](#DESCRIPTION)DESCRIPTION

           e2freefrag is used to report free space fragmentation on ext2/3/4
           file systems.  filesys is the file system device name (e.g.
           /dev/hdc1, /dev/md0).  The e2freefrag program will scan the block
           bitmap information to check how many free blocks are present as
           contiguous and aligned free space. The percentage of contiguous
           free blocks of size and of alignment chunk_kb is reported.  It
           also displays the minimum/maximum/average free chunk size in the
           file system, along with a histogram of all free chunks.  This
           information can be used to gauge the level of free space
           fragmentation in the file system.

## [](#OPTIONS)OPTIONS

           -c chunk_kb
                  If a chunk size is specified, then e2freefrag will print
                  how many free chunks of size chunk_kb are available in
                  units of kilobytes (Kb).  The chunk size must be a power of
                  two and be larger than file system block size.

           -h     Print the usage of the program.

## [](#EXAMPLE)EXAMPLE

           # e2freefrag /dev/vgroot/lvhome
           Device: /dev/vgroot/lvhome
           Blocksize: 4096 bytes
           Total blocks: 1504085
           Free blocks: 292995 (19.5%)

           Min. free extent: 4 KB
           Max. free extent: 24008 KB
           Avg. free extent: 252 KB

           HISTOGRAM OF FREE EXTENT SIZES:
           Extent Size Range :   Free extents   Free Blocks  Percent
               4K...    8K- :           704           704     0.2%
               8K...   16K- :           810          1979     0.7%
              16K...   32K- :           843          4467     1.5%
              32K...   64K- :           579          6263     2.1%
              64K...  128K- :           493         11067     3.8%
             128K...  256K- :           394         18097     6.2%
             256K...  512K- :           281         25477     8.7%
             512K... 1024K- :           253         44914    15.3%
               1M...    2M- :           143         51897    17.7%
               2M...    4M- :            73         50683    17.3%
               4M...    8M- :            37         52417    17.9%
               8M...   16M- :             7         19028     6.5%
              16M...   32M- :             1          6002     2.0%

## [](#AUTHOR)AUTHOR

           This version of e2freefrag was written by Rupesh Thakare, and
           modified by Andreas Dilger <adilger@sun.com>, and Kalpak Shah.

## [](#SEE_ALSO)SEE ALSO

           debugfs(8), dumpe2fs(8), e2fsck(8)

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

    E2fsprogs version 1.47.4        March 2025                  E2FREEFRAG(8)

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
