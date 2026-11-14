---
{"title": "warnquota(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/warnquota.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# warnquota(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WARNQUOTA(8)             System Manager's Manual             WARNQUOTA(8)

## [](#NAME)NAME

           warnquota - send mail to users over quota

## [](#SYNOPSIS)SYNOPSIS

           warnquota [ -ugsid ] [ -F quotaformat ] [ -q quotatab ] [ -c
           configfile ] [ -a adminsfile ] [ filesystem...  ]

## [](#DESCRIPTION)DESCRIPTION

           warnquota checks the disk quota for specified local filesystems
           (or for each local filesystem if none specified) and mails a
           warning message to those users who have reached their softlimit.
           It is typically run via cron(8).

           -F, --format=quotaformat
                  Perform setting for specified format (ie. don't perform
                  format autodetection).  Possible format names are: vfsold
                  Original quota format with 16-bit UIDs / GIDs, vfsv0 Quota
                  format with 32-bit UIDs / GIDs, 64-bit space usage, 32-bit
                  inode usage and limits, vfsv1 Quota format with 64-bit
                  quota limits and usage, xfs Quota on XFS filesystem.

           -q, --quota-tab=quotatab
                  Use quotatab instead of /etc/quotatab as file with device
                  description strings (see quotatab(5) for syntax).

           -c, --config=configfile
                  Use configfile instead of /etc/warnquota.conf as
                  configuration file (see warnquota.conf(5) for syntax).

           -a, --admins-file=adminsfile
                  Use adminsfile instead of /etc/quotagrpadmins as a file
                  with administrators of the groups (see quotagrpadmins(5)
                  for syntax).

           -u, --user
                  check whether users are not exceeding quotas (default).

           -g, --group
                  check whether groups are not exceeding quotas. If group is
                  exceeding quota a mail is sent to the user specified in
                  /etc/quotagrpadmins.

           -s, --human-readable[=units]
                  Try to report used space, number of used inodes and limits
                  in more appropriate units than the default ones. Units can
                  be also specified explicitely by an optional argument in
                  format [ kgt ],[ kgt ] where the first character specifies
                  space units and the second character specifies inode units.

           -i, --no-autofs
                  ignore mountpoints mounted by automounter.

           -d, --no-details
                  do not attach quota report in email.

## [](#FILES)FILES

           aquota.user
                  quota file at the filesystem root (version 2 quota, non-XFS
                  filesystems)
           quota.user
                  quota file at the filesystem root (version 1 quota, non-XFS
                  filesystems)
           /etc/warnquota.conf
                  configuration file
           /etc/quotatab
                  device description
           /etc/quotagrpadmins
                  administrators of the groups
           /etc/mtab
                  default filesystems
           /etc/passwd
                  default set of users

## [](#SEE_ALSO)SEE ALSO

           quota(1), quotatab(5), quotagrpadmins(5), warnquota.conf(5),
           cron(8), edquota(8).

## [](#AUTHORS)AUTHORS

           warnquota(8) was written by Marco van Wieringen
           <mvw@planets.elm.net>, modifications by Jan Kara <jack@suse.cz>.
           This reference page written by Heiko Schlittermann
           <heiko@lotte.sax.de>, modifications by Jan Kara

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

                                                                 WARNQUOTA(8)

------------------------------------------------------------------------

Pages that refer to this page: [quota(1)](../man1/quota.1.html),  [quotasync(1)](../man1/quotasync.1.html),  [quotagrpadmins(5)](../man5/quotagrpadmins.5.html),  [quotatab(5)](../man5/quotatab.5.html),  [warnquota.conf(5)](../man5/warnquota.conf.5.html),  [quotaon(8)](../man8/quotaon.8.html),  [repquota(8)](../man8/repquota.8.html),  [warnquota(8)](../man8/warnquota.8.html),  [xfs_quota(8)](../man8/xfs_quota.8.html)

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
