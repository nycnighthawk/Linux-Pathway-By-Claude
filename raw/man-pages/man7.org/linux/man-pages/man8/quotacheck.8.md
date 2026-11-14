---
{"title": "quotacheck(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/quotacheck.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# quotacheck(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTE](#NOTE) \| [SEE ALSO](#SEE_ALSO) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    quotacheck(8)            System Manager's Manual            quotacheck(8)

## [](#NAME)NAME

           quotacheck - scan a filesystem for disk usage, create, check and
           repair quota files

## [](#SYNOPSIS)SYNOPSIS

           quotacheck [ -gubcfinvdMmR ] [ -F quota-format ] -a | filesystem

## [](#DESCRIPTION)DESCRIPTION

           quotacheck examines each filesystem, builds a table of current
           disk usage, and compares this table against that recorded in the
           disk quota file for the filesystem (this step is omitted if option
           -c is specified). If any inconsistencies are detected, both the
           quota file and the current system copy of the incorrect quotas are
           updated (the latter only occurs if an active filesystem is checked
           which is not advised).  By default, only user quotas are checked.
           quotacheck expects each filesystem to be checked to have quota
           files named [a]quota.user and [a]quota.group located at the root
           of the associated filesystem.  If a file is not present,
           quotacheck will create it.

           If the quota file is corrupted, quotacheck tries to save as much
           data as possible.  Rescuing data may need user intervention. With
           no additional options quotacheck will simply exit in such a
           situation. When in interactive mode (option -i) , the user is
           asked for advice. Advice can also be provided from command line
           (see option -n) , which is useful when quotacheck is run
           automatically (ie. from script) and failure is unacceptable.

           quotacheck should be run each time the system boots and mounts
           non-valid filesystems.  This is most likely to happen after a
           system crash.

           It is strongly recommended to run quotacheck with quotas turned
           off for the filesystem. Otherwise, possible damage or loss to data
           in the quota files can result.  It is also unwise to run
           quotacheck on a live filesystem as actual usage may change during
           the scan.  To prevent this, quotacheck tries to remount the
           filesystem read-only before starting the scan.  After the scan is
           done it remounts the filesystem read-write. You can disable this
           with option -m.  You can also make quotacheck ignore the failure
           to remount the filesystem read-only with option -M.

## [](#OPTIONS)OPTIONS

           -b, --backup
                  Forces quotacheck to make backups of the quota file before
                  writing the new data.

           -v, --verbose
                  quotacheck reports its operation as it progresses.
                  Normally it operates silently.  If the option is specified
                  twice, also the current directory is printed (note that
                  printing can slow down the scan measurably).

           -d, --debug
                  Enable debugging mode.  It will result in a lot of
                  information which can be used in debugging the program. The
                  output is very verbose and the scan will be slow.

           -u, --user
                  Only user quotas listed in /etc/mtab or on the filesystems
                  specified are to be checked.  This is the default action.

           -g, --group
                  Only group quotas listed in /etc/mtab or on the filesystems
                  specified are to be checked.

           -c, --create-files
                  Don't read existing quota files. Just perform a new scan
                  and save it to disk.  quotacheck also skips scanning of old
                  quota files when they are not found.

           -f, --force
                  Forces checking and writing of new quota files on
                  filesystems with quotas enabled. This is not recommended as
                  the created quota files may be out of sync.

           -M, --try-remount
                  This flag forces checking of filesystem in read-write mode
                  if a remount fails. Do this only when you are sure no
                  process will write to a filesystem while scanning.

           -m, --no-remount
                  Don't try to remount filesystem read-only. See comment with
                  option -M.

           -i, --interactive
                  Interactive mode. By default quotacheck exits when it finds
                  an error. In interactive mode user is asked for input
                  instead.  See option -n.

           -n, --use-first-dquot
                  If the quota files become corrupted, it is possible for
                  duplicate entries for a single user or group ID to exist.
                  Normally in this case, quotacheck exits or asks user for
                  input. When this option is set, the first entry found is
                  always used (this option works in interactive mode too).

           -F, --format=format-name
                  Check and fix quota files of specified format (ie. don't
                  perform format auto-detection). This is recommended as
                  detection might not work well on corrupted quota files.
                  Possible format names are: vfsold Original quota format
                  with 16-bit UIDs / GIDs, vfsv0 Quota format with 32-bit
                  UIDs / GIDs, 64-bit space usage, 32-bit inode usage and
                  limits, vfsv1 Quota format with 64-bit quota limits and
                  usage, rpc (quota over NFS), xfs (quota on XFS filesystem)

           -a, --all
                  Check all mounted non-NFS filesystems in /etc/mtab

           -R, --exclude-root
                  When used together with the -a option, all filesystems
                  except for the root filesystem are checked for quotas.

## [](#NOTE)NOTE

           quotacheck should only be run by super-user. Non-privileged users
           are presumably not allowed to read all the directories on the
           given filesystem.

## [](#SEE_ALSO)SEE ALSO

           quota(1), quotactl(2), fstab(5), quotaon(8), repquota(8),
           convertquota(8), setquota(8), edquota(8), fsck(8), efsck(8),
           e2fsck(8), xfsck(8)

## [](#FILES)FILES

           aquota.user or aquota.group
                  located at filesystem root with quotas (version 2 quota,
                  non-XFS filesystems)
           quota.user or quota.group
                  located at filesystem root with quotas (version 1 quota,
                  non-XFS filesystems)
           /etc/mtab
                  names and locations of mounted filesystems

## [](#AUTHOR)AUTHOR

           Jan Kara <jack@suse.cz>
           Based on old quotacheck by:
           Edvard Tuinder <ed@elm.net>
           Marco van Wieringen <mvw@planets.elm.net>

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

                                 Fri Jul 20 2001                quotacheck(8)

------------------------------------------------------------------------

Pages that refer to this page: [quota(1)](../man1/quota.1.html),  [quotasync(1)](../man1/quotasync.1.html),  [Q_QUOTAON(2const)](../man2/Q_QUOTAON.2const.html),  [quotactl(2)](../man2/quotactl.2.html),  [convertquota(8)](../man8/convertquota.8.html),  [edquota(8)](../man8/edquota.8.html),  [repquota(8)](../man8/repquota.8.html),  [setquota(8)](../man8/setquota.8.html),  [systemd-quotacheck@.service(8)](../man8/systemd-quotacheck@.service.8.html)

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
