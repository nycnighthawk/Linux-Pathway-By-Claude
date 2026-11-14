---
{"title": "xfs_bmap(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xfs_bmap.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xfs_bmap(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xfs_bmap(8)              System Manager's Manual              xfs_bmap(8)

## [](#NAME)NAME

           xfs_bmap - print block mapping for an XFS file

## [](#SYNOPSIS)SYNOPSIS

           xfs_bmap [ -adelpv ] [ -n num_extents ] file
           xfs_bmap -V

## [](#DESCRIPTION)DESCRIPTION

           xfs_bmap prints the map of disk blocks used by files in an XFS
           filesystem.  The map lists each extent used by the file, as well
           as regions in the file that do not have any corresponding blocks
           (holes).  Each line of the listings takes the following form:

                  extent: [startoffset..endoffset]: startblock..endblock

           Holes are marked by replacing the startblock..endblock with hole.
           All the file offsets and disk blocks are in units of 512-byte
           blocks, no matter what the filesystem's block size is.

## [](#OPTIONS)OPTIONS

           -a     If this option is specified, information about the file's
                  attribute fork is printed instead of the default data fork.

           -e     If this option is used, xfs_bmap obtains all delayed
                  allocation extents, and does not flush dirty pages to disk
                  before querying extent data. With the -v option, the flags
                  column will show which extents have not yet been allocated.

           -l     If this option is used, then

                       <nblocks>  blocks

                  will be appended to each line.  nblocks is the length of
                  the extent described on the line in units of 512-byte
                  blocks.

                  This flag has no effect if the -v option is used.

           -n num_extents
                  If this option is given, xfs_bmap will display at most
                  num_extents extents. In the absence of -n, xfs_bmap will
                  display all extents in the file.

           -p     If this option is used, xfs_bmap obtains all unwritten
                  (preallocated) extents that do not contain written data.
                  With the -v option, the flags column will show which
                  extents are preallocated/unwritten.

           -v     Shows verbose information. When this flag is specified,
                  additional AG specific information is appended to each line
                  in the following form:

                       agno (startagoffset..endagoffset) nblocks flags

                  A second -v option will print out the flags legend.

           -V     Prints the version number and exits.

## [](#SEE_ALSO)SEE ALSO

           xfs_fsr(8), xfs(5).

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

                                                                  xfs_bmap(8)

------------------------------------------------------------------------

Pages that refer to this page: [xfs_io(8)](../man8/xfs_io.8.html)

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
