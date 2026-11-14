---
{"title": "systemd-quotacheck@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-quotacheck-root.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-quotacheck@.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [CREDENTIALS](#CREDENTIALS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8) systemd-quotacheck@.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-quotacheck@.service, systemd-quotacheck-root.service,
           systemd-quotacheck - File system quota checker logic

## [](#SYNOPSIS)SYNOPSIS

           systemd-quotacheck@.service

           systemd-quotacheck-root.service

           /usr/lib/systemd/systemd-quotacheck

## [](#DESCRIPTION)DESCRIPTION

           systemd-quotacheck@.service and systemd-quotacheck-root.service
           are services responsible for file system quota checks. They run
           once at boot after all necessary file systems are mounted. They
           are pulled in only if at least one file system has quotas enabled.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-quotacheck understands one kernel command line parameter:

           quotacheck.mode=
               One of "auto", "force", "skip". Controls the mode of
               operation. The default is "auto", and ensures that file system
               quota checks are done when the file system quota checker deems
               them necessary.  "force" unconditionally results in full file
               system quota checks.  "skip" skips any file system quota
               checks.

               Added in version 186.

## [](#CREDENTIALS)CREDENTIALS

           systemd-quotacheck supports the service credentials logic as
           implemented by ImportCredential=/LoadCredential=/SetCredential=
           (see systemd.exec(5) for details). The following credentials are
           used when passed in:

           quotacheck.mode
               The contents of the credential is parsed as same as the kernel
               command line option with the same name. See above for more
               details.

               Added in version 258.

           Note that by default the systemd-quotacheck@.service and
           systemd-quotacheck-root.service unit files are set up to inherit
           quotacheck.mode credential from the service manager.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), quotacheck(8), systemd-fsck@.service(8)

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

    systemd 262~devel                                  SYSTEMD-....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-fsck@.service(8)](../man8/systemd-fsck@.service.8.html)

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
