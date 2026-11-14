---
{"title": "quotaon(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/quotaon.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# quotaon(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES ON XFS FILESYSTEMS](#NOTES_ON_XFS_FILESYSTEMS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    QUOTAON(8)               System Manager's Manual               QUOTAON(8)

## [](#NAME)NAME

           quotaon, quotaoff - turn filesystem quotas on and off

## [](#SYNOPSIS)SYNOPSIS

           quotaon [ -vugfp ] [ -F format-name ] filesystem...
           quotaon [ -avugPfp ] [ -F format-name ]

           quotaoff [ -vugPp ] [ -x state ] filesystem...
           quotaoff [ -avugp ]

## [](#DESCRIPTION)DESCRIPTION

       quotaon
           quotaon announces to the system that disk quotas should be enabled
           on one or more filesystems. The filesystem quota files must be
           present in the root directory of the specified filesystem and be
           named either aquota.user (for version 2 user quota), quota.user
           (for version 1 user quota), aquota.group (for version 2 group
           quota), or quota.group (for version 1 group quota).

           XFS filesystems are a special case - XFS considers quota
           information as filesystem metadata and uses journaling to provide
           a higher level guarantee of consistency.  There are two components
           to the XFS disk quota system: accounting and limit enforcement.
           XFS filesystems require that quota accounting be turned on at
           mount time.  It is possible to enable and disable limit
           enforcement on an XFS filesystem after quota accounting is already
           turned on.  The default is to turn on both accounting and
           enforcement.

           The XFS quota implementation does not maintain quota information
           in user-visible files, but rather stores this information
           internally.

       quotaoff
           quotaoff announces to the system that the specified filesystems
           should have any disk quotas turned off.

## [](#OPTIONS)OPTIONS

       quotaon
           -F, --format=format-name
                  Report quota for specified format (ie. don't perform format
                  autodetection).  Possible format names are: vfsold Original
                  quota format with 16-bit UIDs / GIDs, vfsv0 Quota format
                  with 32-bit UIDs / GIDs, 64-bit space usage, 32-bit inode
                  usage and limits, vfsv1 Quota format with 64-bit quota
                  limits and usage, xfs (quota on XFS filesystem)

           -a, --all
                  All automatically mounted (no noauto option) non-NFS
                  filesystems in /etc/fstab with quotas will have their
                  quotas turned on.  This is normally used at boot time to
                  enable quotas.

           -v, --verbose
                  Display a message for each filesystem where quotas are
                  turned on.

           -u, --user
                  Manipulate user quotas. This is the default.

           -g, --group
                  Manipulate group quotas.

           -P, --project
                  Manipulate project quotas.

           -p, --print-state
                  Instead of turning quotas on just print state of quotas
                  (ie. whether. quota is on or off)

           -x, --xfs-command enforce
                  Switch on limit enforcement for XFS filesystems. This is
                  the default action for any XFS filesystem. This option is
                  only applicable to XFS, and is silently ignored for other
                  filesystem types.

           -f, --off
                  Make quotaon behave like being called as quotaoff.

       quotaoff
           -F, --format=format-name
                  Report quota for specified format (ie. don't perform format
                  autodetection).  Possible format names are: vfsold (version
                  1 quota), vfsv0 (version 2 quota), xfs (quota on XFS
                  filesystem)

           -a, --all
                  Force all filesystems in /etc/fstab to have their quotas
                  disabled.

           -v, --verbose
                  Display a message for each filesystem affected.

           -u, --user
                  Manipulate user quotas. This is the default.

           -g, --group
                  Manipulate group quotas.

           -P, --project
                  Manipulate project quotas.

           -p, --print-state
                  Instead of turning quotas off just print state of quotas
                  (ie. whether. quota is on or off)

           -x, --xfs-command delete
                  Free up the space used to hold quota information
                  (maintained internally) within XFS.  This option is only
                  applicable to XFS, and is silently ignored for other
                  filesystem types.  It can only be used on a filesystem with
                  quota previously turned off.

           -x, --xfs-command enforce
                  Switch off limit enforcement for XFS filesystems (perform
                  quota accounting only). This is the default action for any
                  XFS filesystem.  This option is only applicable to XFS, and
                  is silently ignored for other filesystem types.

           -x, --xfs-command account
                  This option can be used to disable quota accounting. It is
                  not possible to enable quota accounting by quota tools. Use
                  mount(8) for that. This option is only applicable to XFS
                  filesystems, and is silently ignored for other filesystem
                  types.

## [](#NOTES_ON_XFS_FILESYSTEMS)NOTES ON XFS FILESYSTEMS

           To enable quotas on an XFS filesystem, use mount(8) or /etc/fstab
           quota option to enable both accounting and limit enforcement.
           quotaon utility cannot be used for this purpose.

           Turning on quotas on an XFS root filesystem requires the quota
           mount options be passed into the kernel at boot time through the
           Linux rootflags boot option.

           To turn off quota limit enforcement on any XFS filesystem, first
           make sure that quota accounting and enforcement are both turned on
           using repquota -v filesystem.  Then, use quotaoff -v filesystem to
           disable limit enforcement.  This may be done while the filesystem
           is mounted.

           Turning on quota limit enforcement on an XFS filesystem is
           achieved using quotaon -v filesystem.  This may be done while the
           filesystem is mounted.

## [](#FILES)FILES

           aquota.user or aquota.group
                  quota file at the filesystem root (version 2 quota, non-XFS
                  filesystems)
           quota.user or quota.group
                  quota file at the filesystem root (version 1 quota, non-XFS
                  filesystems)
           /etc/fstab
                  default filesystems

## [](#SEE_ALSO)SEE ALSO

           quotactl(2), fstab(5), quota_nld(8), repquota(8), warnquota(8)

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

    4th Berkeley Distribution                                      QUOTAON(8)

------------------------------------------------------------------------

Pages that refer to this page: [quota(1)](../man1/quota.1.html),  [quotasync(1)](../man1/quotasync.1.html),  [quotactl(2)](../man2/quotactl.2.html),  [convertquota(8)](../man8/convertquota.8.html),  [edquota(8)](../man8/edquota.8.html),  [quotacheck(8)](../man8/quotacheck.8.html),  [repquota(8)](../man8/repquota.8.html),  [setquota(8)](../man8/setquota.8.html)

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
