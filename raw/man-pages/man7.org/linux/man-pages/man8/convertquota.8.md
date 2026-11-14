---
{"title": "convertquota(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/convertquota.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# convertquota(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CONVERTQUOTA(8)          System Manager's Manual          CONVERTQUOTA(8)

## [](#NAME)NAME

           convertquota - convert quota from old file format to new one

## [](#SYNOPSIS)SYNOPSIS

           convertquota [ -ug ] -e filesystem

           convertquota [ -ug ] -f oldformat,newformat filesystem

## [](#DESCRIPTION)DESCRIPTION

           convertquota converts old quota files quota.user and quota.group
           to files aquota.user and aquota.group in new format currently used
           by 2.4.0-ac? and newer or by SuSE or Red Hat Linux 2.4 kernels on
           filesystem.

           New file format allows using quotas for 32-bit uids / gids,
           setting quotas for root, accounting used space in bytes (and so
           allowing use of quotas in ReiserFS) and it is also architecture
           independent. This format introduces Radix Tree (a simple form of
           tree structure) to quota file.

## [](#OPTIONS)OPTIONS

           -u, --user
                  convert user quota file. This is the default.

           -g, --group
                  convert group quota file.

           -f, --convert-format oldformat,newformat
                  convert quota file from oldformat to newformat.

           -e, --convert-endian
                  convert vfsv0 file format from big endian to little endian
                  (old kernels had a bug and did not store quota files in
                  little endian format).

           -V, --version
                  print version information.

## [](#FILES)FILES

           aquota.user
                  new user quota file

           aquota.group
                  new group quota file

## [](#SEE_ALSO)SEE ALSO

           quota(1), setquota(8), edquota(8), quotacheck(8), quotaon(8),
           repquota(8)

## [](#AUTHOR)AUTHOR

           Jan Kara <jack@suse.cz>

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

    4th Berkeley Distribution    Fri Aug 20 1999              CONVERTQUOTA(8)

------------------------------------------------------------------------

Pages that refer to this page: [quotacheck(8)](../man8/quotacheck.8.html)

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
