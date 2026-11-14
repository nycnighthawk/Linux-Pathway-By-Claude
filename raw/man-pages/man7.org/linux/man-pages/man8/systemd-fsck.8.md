---
{"title": "systemd-fsck@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-fsck.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-fsck@.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [CREDENTIALS](#CREDENTIALS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-FSCK@.SERVICE(8)  systemd-fsck@.service  SYSTEMD-FSCK@.SERVICE(8)

## [](#NAME)NAME

           systemd-fsck@.service, systemd-fsck-root.service, systemd-fsck-
           usr.service, systemd-fsck - File system checker logic

## [](#SYNOPSIS)SYNOPSIS

               systemd-fsck@.service
               systemd-fsck-root.service
               systemd-fsck-usr.service
               /usr/lib/systemd/systemd-fsck

## [](#DESCRIPTION)DESCRIPTION

           systemd-fsck@.service, systemd-fsck-root.service, and
           systemd-fsck-usr.service are services responsible for file system
           checks. They are instantiated for each device that is configured
           for file system checking.  systemd-fsck-root.service and
           systemd-fsck-usr.service are responsible for file system checks on
           the root and /usr file system, respectively, but only if the root
           filesystem was not checked in the initrd.  systemd-fsck@.service
           is used for all other file systems and for the root file system in
           the initrd.

           These services are started at boot if passno in /etc/fstab for the
           file system is set to a value greater than zero, but only if it is
           also configured to be mounted at boot (i.e. without "noauto"
           option). The file system check for root is performed before the
           other file systems. Other file systems may be checked in parallel,
           except when they are on the same rotating disk.

           systemd-fsck does not know any details about specific filesystems,
           and simply executes file system checkers specific to each
           filesystem type (fsck.type). These checkers will decide if the
           filesystem should actually be checked based on the time since last
           check, number of mounts, unclean unmount, etc.

           systemd-fsck-root.service and systemd-fsck-usr.service will
           activate reboot.target if fsck(8) returns the "System should
           reboot" condition, or emergency.target if fsck returns the
           "Filesystem errors left uncorrected" condition.

           systemd-fsck@.service will fail if fsck(8) returns either the
           "System should reboot" or the "Filesystem errors left uncorrected"
           condition. For filesystems listed in /etc/fstab without "nofail"
           or "noauto" options, local-fs.target will then activate
           emergency.target.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-fsck understands these kernel command line parameters:

           fsck.mode=
               One of "auto", "force", "skip". Controls the mode of
               operation. The default is "auto", and ensures that file system
               checks are done when the file system checker deems them
               necessary.  "force" unconditionally results in full file
               system checks.  "skip" skips any file system checks.

               Added in version 186.

           fsck.repair=
               One of "preen", "yes", "no". Controls the mode of operation.
               The default is "preen", and will automatically repair problems
               that can be safely fixed.  "yes" will answer yes to all
               questions by fsck and "no" will answer no to all questions.

               Added in version 213.

## [](#CREDENTIALS)CREDENTIALS

           systemd-fsck supports the service credentials logic as implemented
           by ImportCredential=/LoadCredential=/SetCredential= (see
           systemd.exec(5) for details). The following credentials are used
           when passed in:

           fsck.mode, fsck.repair
               The contents of the credentials are parsed as same as the
               kernel command line options with the same name. See above for
               more details.

               Added in version 258.

           Note that by default the systemd-fsck@.service,
           systemd-fsck-root.service, and systemd-fsck-usr.service unit files
           are set up to inherit both fsck.mode and fsck.repair credentials
           from the service manager.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), fsck(8), systemd-quotacheck@.service(8),
           fsck.btrfs(8), fsck.cramfs(8), fsck.ext4(8), fsck.fat(8),
           fsck.hfsplus(8), fsck.minix(8), fsck.ntfs(8), fsck.xfs(8)

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                SYSTEMD-FSCK@.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-quotacheck@.service(8)](../man8/systemd-quotacheck@.service.8.html)

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
