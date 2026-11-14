---
{"title": "xfs_ncheck(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xfs_ncheck.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xfs_ncheck(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xfs_ncheck(8)            System Manager's Manual            xfs_ncheck(8)

## [](#NAME)NAME

           xfs_ncheck - generate pathnames from i-numbers for XFS

## [](#SYNOPSIS)SYNOPSIS

           xfs_ncheck [ -i ino ] ... [ -f ] [ -s ] [ -l logdev ] device
           xfs_ncheck -V

## [](#DESCRIPTION)DESCRIPTION

           xfs_ncheck with no -i arguments generates an inode number and
           pathname list of all files on the given filesystem. Names of
           directory files are followed by /..  The output is not sorted in
           any particular order.  The filesystem to be examined is specified
           by the device argument, which should be the disk or volume device
           for the filesystem.  Filesystems stored in files can also be
           checked, using the -f flag.

## [](#OPTIONS)OPTIONS

           -f       Specifies that the filesystem image to be processed is
                    stored in a regular file at device (see the mkfs.xfs -d
                    file option). This might happen if an image copy of a
                    filesystem has been made into an ordinary file.

           -l logdev
                    Specifies the device where the filesystem's external log
                    resides.  Only for those filesystems which use an
                    external log. See the mkfs.xfs -l option, and refer to
                    xfs(5) for a detailed description of the XFS log.

           -s       Limits the report to special files and files with
                    setuserid mode.  This option may be used to detect
                    violations of security policy.

           -i ino   Limits the report to only those files whose inode numbers
                    follow.  May be given multiple times to select multiple
                    inode numbers.

           -V       Prints the version number and exits.

           If the filesystem is seriously corrupted, or very busy and looks
           like it is corrupt, a message of the form that would be generated
           by the xfs_db(8) "check" command may appear.

           xfs_ncheck is only useful with XFS filesystems.

## [](#SEE_ALSO)SEE ALSO

           mkfs.xfs(8), xfs(5).

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

                                                                xfs_ncheck(8)

------------------------------------------------------------------------

Pages that refer to this page: [xfs_db(8)](../man8/xfs_db.8.html),  [xfs_fsr(8)](../man8/xfs_fsr.8.html)

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
