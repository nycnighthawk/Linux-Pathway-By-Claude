---
{"title": "xfs_spaceman(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xfs_spaceman.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xfs_spaceman(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMANDS](#COMMANDS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xfs_spaceman(8)          System Manager's Manual          xfs_spaceman(8)

## [](#NAME)NAME

           xfs_spaceman - show free space information about an XFS filesystem

## [](#SYNOPSIS)SYNOPSIS

           xfs_spaceman [ -c cmd ] file
           xfs_spaceman -V

## [](#DESCRIPTION)DESCRIPTION

           xfs_spaceman reports and controls free space usage in an XFS
           filesystem.

## [](#OPTIONS)OPTIONS

           -c cmd xfs_spaceman commands may be run interactively (the
                  default) or as arguments on the command line. Multiple -c
                  arguments may be given. The commands are run in the
                  sequence given, then the program exits.

## [](#COMMANDS)COMMANDS

           freesp [ -dgrs ] [-a agno]... [ -b | -e bsize | -h bsize | -m
           factor ]
                  With no arguments, freesp shows a histogram of all free
                  space extents in the filesystem.  The command takes the
                  following options:

                     -a agno
                         Collect free space information from this allocation
                         group.  This option can be specified multiple times
                         to collect from multiple groups.

                     -b  This argument establishes that the histogram bin
                         sizes are successive powers of two.  This is the
                         default, and is mutually exclusive with the -e, -h,
                         and -m options.

                     -d  Print debugging information such as the raw free
                         space extent information.

                     -g  Print the free space block and extent counts for
                         each AG.

                     -e bsize
                         Set all histogram bin sizes to a specific value.
                         This option is mutually exclusive with the -b, -h,
                         and -m options.

                     -h bsize
                         Create a histogram bin with a lower bound of this
                         value.  The upper bound of this bin will be one less
                         than the lower bound of the next highest histogram
                         bin.  This option can be given multiple times to
                         control the exact bin sizes.  This option is
                         mutually exclusive with the -b, -e, and -m options.

                     -m factor
                         Create each histogram bin with a size that is this
                         many times the size of the prvious bin created.
                         This option is mutually exclusive with the -b, -e,
                         and -h options.

                     -r  Query the realtime device for free space
                         information.

                     -s  Display a summary of the free space information
                         found.

           info   Displays selected geometry information about the
                  filesystem.  The opened file must be a mount point of a XFS
                  filesystem.  The output will have the same format that
                  xfs_info(8) prints when querying a filesystem.

           health [ -a agno] [ -c ] [ -f ] [ -i inum ] [ -n ] [ -q ] [ -r
           rgno ] [ paths ]
                  Reports the health of the given group of filesystem
                  metadata.
                     -a agno
                         Report on the health of the given allocation group.
                     -c  Scan all inodes in the filesystem and report each
                         file's health status.  If the -a option is given,
                         scan only the inodes in that AG.
                     -f  Report on the health of metadata that affect the
                         entire filesystem.
                     -i inum
                         Report on the health of a specific inode.
                     -n  When reporting on the health of a file, try to
                         report the full file path, if possible.  This option
                         is disabled by default to minimize runtime.
                     -q  Report only unhealthy metadata.
                     -r  Report on the health of the given realtime group.
                     paths
                         Report on the health of the files at the given path.

           help [ command ]
                  Display a brief description of one or all commands.

           prealloc [ -u id ] [ -g id ] [ -p id ] [ -m minlen ] [ -s ]
                  Removes speculative preallocation.  If no -u, -g, or -p
                  options are given, this command acts on all files.  The
                  command takes the following options:

                     -u uid
                         Clear all speculative preallocations for files with
                         this user id.  This option can be given in
                         combination with the -g  and  -p options.

                     -g gid
                         Clear all speculative preallocations for files with
                         this group id.  This option can be given in
                         combination with the -u  and  -p options.

                     -p pid
                         Clear all speculative preallocations for files with
                         this project id.  This option can be given in
                         combination with the -u  and  -g options.

                     -m minlen
                         Ignore all files smaller than this size.  Units can
                         be supplied for this argument.

                     -s  Wait for removal to complete.

           print  Display a list of all open files.

           quit   Exit xfs_spaceman.

           trim ( -a agno | -f | offset length ) [ -m minlen ]
                  Instructs the underlying storage device to release all
                  storage that may be backing free space in the filesystem.
                  The command takes the following options: (One of -a, -f, or
                  the offset/length pair are required.)

                     -a agno
                         Trim free space extents in the given allocation
                         group.  This option is mutually exclusive with the
                         -f option and the offset/length options.

                     -f  Trim all free space in the filesystem.  This option
                         is mutually exclusive with the -a option and the
                         offset/length options.

                     option, length
                         Trim all free space within the physical range
                         defined by the offset and length from this
                         filesystem.  Units can be appended to these
                         arguments.  This option is mutually exclusive with
                         the -a and -f options.

                     -m minlen
                         Do not trim free space extents shorter than this
                         length.  Units can be appended to this argument.

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

                                                              xfs_spaceman(8)

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
