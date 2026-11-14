---
{"title": "systemd-hibernate-resume.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-hibernate-resume.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-hibernate-resume.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEM...SERVICE(8)  systemd-hibernate-resume.service SYSTEM...SERVICE(8)

## [](#NAME)NAME

           systemd-hibernate-resume.service, systemd-hibernate-clear.service,
           systemd-hibernate-resume - Resume from hibernation

## [](#SYNOPSIS)SYNOPSIS

           systemd-hibernate-resume.service

           systemd-hibernate-clear.service

           /usr/lib/systemd/systemd-hibernate-resume

## [](#DESCRIPTION)DESCRIPTION

           systemd-hibernate-resume.service initiates the resume from
           hibernation.

           systemd-hibernate-resume only supports the in-kernel hibernation
           implementation, see Swap suspend[1]. Internally, it works by
           writing the major:minor of selected device node to
           /sys/power/resume, along with the offset in memory pages
           (/sys/power/resume_offset) if supported.

           The resume device node is either passed directly through
           arguments, or automatically acquired from kernel command line
           options and/or HibernateLocation EFI variable. The latter will
           normally be cleared by systemd-hibernate-resume.service on
           resumption. If a stale variable is detected, it would be cleared
           by systemd-hibernate-clear.service.

           Failing to initiate a resume is not an error condition. It may
           mean that there was no resume image (e. g. if the system has been
           simply powered off and not hibernated). In such cases, the boot is
           ordinarily continued.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-hibernate-resume-generator(8)

## [](#NOTES)NOTES

            1. Swap suspend
               https://docs.kernel.org/power/swsusp.html

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

    systemd 262~devel                                     SYSTEM...SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-hibernate-resume-generator(8)](../man8/systemd-hibernate-resume-generator.8.html)

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
