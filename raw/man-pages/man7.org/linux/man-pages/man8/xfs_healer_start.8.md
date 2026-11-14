---
{"title": "xfs_healer_start(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xfs_healer_start.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xfs_healer_start(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xfs_healer_start(8)      System Manager's Manual      xfs_healer_start(8)

## [](#NAME)NAME

           xfs_healer_start - starts xfs_healer instances

## [](#SYNOPSIS)SYNOPSIS

           xfs_healer_start [ OPTIONS ]
           xfs_healer_start -V

## [](#DESCRIPTION)DESCRIPTION

           xfs_healer_start starts the xfs_healer service whenever the kernel
           mounts an XFS filesystem in the current mount namespace.

           WARNING!  This program is EXPERIMENTAL, which means that its
           behavior and interface could change at any time!

           Normally this program runs as a systemd service.

## [](#OPTIONS)OPTIONS

           --supported
                  Check if the kernel supports listening for mount events.
                  Exits with 0 if it does, and non-zero if not.

           --mountns path
                  Monitor the given mount namespace.  Defaults to the mount
                  namespace associated with the process itself.

           -V     Prints the version number and exit.

## [](#SEE_ALSO)SEE ALSO

           xfs_healer(8).

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

                                                          xfs_healer_start(8)

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
