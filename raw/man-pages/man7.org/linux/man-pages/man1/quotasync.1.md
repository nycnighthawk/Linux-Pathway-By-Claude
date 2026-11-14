---
{"title": "quotasync(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/quotasync.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# quotasync(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    QUOTASYNC(1)             General Commands Manual             QUOTASYNC(1)

## [](#NAME)NAME

           quotasync - synchronize in-kernel file system usage and limits to
           disk format

## [](#SYNOPSIS)SYNOPSIS

           quotasync [ -ugP ] mount-point...
           quotasync [ -ugP ] -a
           quotasync -h | -V

## [](#DESCRIPTION)DESCRIPTION

           quotasync flushes file system usage and limits from kernel memory
           to quota files stored in the file system. By default only the user
           quotas are synchronized.

           This tool can be useful if you want to display accurate quotas by
           tools that parse quota files, like repquota(8).

## [](#OPTIONS)OPTIONS

           -u, --user
                  Synchronize user usage and limits.

           -g, --group
                  Synchronize group usage and limits.

           -P, --project
                  Synchronize project usage and limits.

           -a, --all
                  Synchronize usage and limits on all file systems. You have
                  to specify this option or to specify desired file systems.

           -V, --version
                  Show program version information and exit.

           -h, --help
                  Show program usage and exit.

## [](#DIAGNOSTICS)DIAGNOSTICS

           If requested synchronization fails, or invalid option is given,
           quotasync will terminate with non-zero exit code. Otherwise it
           will return zero.

## [](#FILES)FILES

           aquota.user  or  aquota.group
                  Quota file at the file system root (version 2 quota, non-
                  XFS/GFS2 file systems).
           quota.user  or  quota.group
                  Quota file at the file system root (version 1 quota, non-
                  XFS/GFS2 file systems).
           /etc/mtab
                  List of mounted file systems maintained by user space.
           /proc/mounts
                  List of mounted file systems maintained by kernel.

## [](#SEE_ALSO)SEE ALSO

           quota(1), quotactl(2), mount(8), quotacheck(8), quotaon(8),
           repquota(8), warnquota(8).

## [](#COLOPHON)COLOPHON

           This page is part of the quota (Linux Diskquota Tools) project.
           Information about the project can be found at [unknown -- if you
           know, please contact man-pages@man7.org] It is not known how to
           report bugs for this man page; if you know, please send a mail to
           man-pages@man7.org.  This page was obtained from the project's
           upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/quota/quota-tools.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2025-12-11.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                                                 QUOTASYNC(1)

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
