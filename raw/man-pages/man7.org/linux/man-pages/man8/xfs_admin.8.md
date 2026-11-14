---
{"title": "xfs_admin(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xfs_admin.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xfs_admin(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xfs_admin(8)             System Manager's Manual             xfs_admin(8)

## [](#NAME)NAME

           xfs_admin - change parameters of an XFS filesystem

## [](#SYNOPSIS)SYNOPSIS

           xfs_admin [ -eflpu ] [ -O featurelist ] [ -c 0|1 ] [ -L label ] [
           -U uuid ] [ -r rtdev ] device [ logdev ]
           xfs_admin -V

## [](#DESCRIPTION)DESCRIPTION

           xfs_admin uses the xfs_db(8) command to modify various parameters
           of a filesystem.

           Devices that are mounted cannot be modified.  Administrators must
           unmount filesystems before xfs_admin or xfs_db(8) can convert
           parameters.  A number of parameters of a mounted filesystem can be
           examined and modified using the xfs_growfs(8) command.

           The optional logdev parameter specifies the device special file
           where the filesystem's external log resides.  This is required
           only for filesystems that use an external log.  See the mkfs.xfs
           -l option, and refer to xfs(5) for a detailed description of the
           XFS log.

## [](#OPTIONS)OPTIONS

           -e     Enables unwritten extent support on a filesystem that does
                  not already have this enabled (for legacy filesystems, it
                  can't be disabled anymore at mkfs time).

                  This option only applies to the deprecated V4 format.

           -f     Specifies that the filesystem image to be processed is
                  stored in a regular file at device (see the mkfs.xfs -d
                  file option).

           -j     Enables version 2 log format (journal format supporting
                  larger log buffers).

                  This option only applies to the deprecated V4 format.

           -l     Print the current filesystem label.

           -p     Enable 32bit project identifier support (PROJID32BIT
                  feature).

                  This option only applies to the deprecated V4 format.

           -u     Print the current filesystem UUID (Universally Unique
                  IDentifier).

           -c 0|1 Enable (1) or disable (0) lazy-counters in the filesystem.

                  Lazy-counters may not be disabled on Version 5 superblock
                  filesystems (i.e. those with metadata CRCs enabled).

                  In other words, this option only applies to the deprecated
                  V4 format.

                  This operation may take quite a bit of time on large
                  filesystems as the entire filesystem needs to be scanned
                  when this option is changed.

                  With lazy-counters enabled, the superblock is not modified
                  or logged on every change of the free-space and inode
                  counters. Instead, enough information is kept in other
                  parts of the filesystem to be able to maintain the counter
                  values without needing to keep them in the superblock. This
                  gives significant improvements in performance on some
                  configurations and metadata intensive workloads.

           -L label
                  Set the filesystem label to label.  XFS filesystem labels
                  can be at most 12 characters long; if label is longer than
                  12 characters, xfs_admin will truncate it and print a
                  warning message.  The filesystem label can be cleared using
                  the special "--" value for label.

           -O feature1=status,feature2=status...
                  Add or remove features on an existing V5 filesystem.  The
                  features should be specified as a comma-separated list.
                  status should be either 0 to disable the feature or 1 to
                  enable the feature.  Note, however, that most features
                  cannot be disabled.

                  NOTE: Administrators must ensure the filesystem is clean by
                  running xfs_repair -n to inspect the filesystem before
                  performing the upgrade.  If corruption is found, recovery
                  procedures (e.g. reformat followed by restoration from
                  backup; or running xfs_repair without the -n) must be
                  followed to clean the filesystem.

                  Supported features are as follows:

                  inobtcount
                      Keep a count the number of blocks in each inode btree
                      in the AGI.  This reduces mount time by speeding up
                      metadata space reservation calculations.  The
                      filesystem cannot be downgraded after this feature is
                      enabled.  Once enabled, the filesystem will not be
                      writable by older kernels.  This feature was added to
                      Linux 5.10.

                  bigtime
                      Upgrade a filesystem to support larger timestamps up to
                      the year 2486.  The filesystem cannot be downgraded
                      after this feature is enabled.  Once enabled, the
                      filesystem will not be mountable by older kernels.
                      This feature was added to Linux 5.10.

                  nrext64
                      Upgrade a filesystem to support large per-inode extent
                      counters. The maximum data fork extent count will be
                      2^48 - 1, while the maximum attribute fork extent count
                      will be 2^32 - 1. The filesystem cannot be downgraded
                      after this feature is enabled. Once enabled, the
                      filesystem will not be mountable by older kernels.
                      This feature was added to Linux 5.19.

                  exchange
                      Upgrade a filesystem to support atomic file content
                      exchanges through the XFS_IOC_EXCHANGE_RANGE ioctl, and
                      to support online repairs of directories, extended
                      attributes, symbolic links, and realtime free space
                      metadata.  The filesystem cannot be downgraded after
                      this feature is enabled.  Once enabled, the filesystem
                      will not be mountable by older kernels.

           -U uuid
                  Set the UUID of the filesystem to uuid.  A sample UUID
                  looks like this: "c1b9d5a2-f162-11cf-9ece-0020afc76f16".
                  The uuid may also be nil, which will set the filesystem
                  UUID to the null UUID.  The uuid may also be generate,
                  which will generate a new UUID for the filesystem.  Note
                  that on CRC-enabled filesystems, this will set an
                  incompatible flag such that older kernels will not be able
                  to mount the filesystem.  To remove this incompatible flag,
                  use restore, which will restore the original UUID and
                  remove the incompatible feature flag as needed.

           -r rtdev
                  Specifies the device special file where the filesystem's
                  realtime section resides.  Only for those filesystems which
                  use a realtime section.

           -V     Prints the version number and exits.

           The mount(8) manual entry describes how to mount a filesystem
           using its label or UUID, rather than its block special device
           name.

## [](#SEE_ALSO)SEE ALSO

           mkfs.xfs(8), mount(8), xfs_db(8), xfs_growfs(8), xfs_repair(8),
           xfs(5).

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

                                                                 xfs_admin(8)

------------------------------------------------------------------------

Pages that refer to this page: [fstab(5)](../man5/fstab.5.html),  [xfs(5)](../man5/xfs.5.html),  [lvmthin(7)](../man7/lvmthin.7.html),  [mount(8)](../man8/mount.8.html),  [xfs_db(8)](../man8/xfs_db.8.html),  [xfs_repair(8)](../man8/xfs_repair.8.html)

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
