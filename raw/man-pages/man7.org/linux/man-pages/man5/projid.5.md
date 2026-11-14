---
{"title": "projid(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/projid.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# projid(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    projid(5)                  File Formats Manual                  projid(5)

## [](#NAME)NAME

           projid - the project name mapping file

## [](#DESCRIPTION)DESCRIPTION

           The /etc/projid file provides a mapping between numeric project
           identifiers and a simple human readable name (similar relationship
           to the one that exists between usernames and uids).  Its format is
           simply:

                # comments are hash-prefixed
                # ...
                cage:10
                logfiles:42

           This file is optional, if a project identifier cannot be mapped to
           a name, it will be parsed and displayed as a numeric value.

## [](#SEE_ALSO)SEE ALSO

           xfs_quota(8), xfsctl(3), projects(5).

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

                                                                    projid(5)

------------------------------------------------------------------------

Pages that refer to this page: [projects(5)](../man5/projects.5.html),  [xfs_quota(8)](../man8/xfs_quota.8.html)

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
