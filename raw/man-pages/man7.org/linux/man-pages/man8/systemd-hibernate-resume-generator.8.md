---
{"title": "systemd-hibernate-resume-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-hibernate-resume-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-hibernate-resume-generator(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEM...ERATOR(8)  systemd-hibernate-resume-generator SYSTEM...ERATOR(8)

## [](#NAME)NAME

           systemd-hibernate-resume-generator - Unit generator for resume=
           kernel parameter

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-hibernate-resume-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-hibernate-resume-generator is a generator that initiates
           the procedure to resume the system from hibernation. When resume=
           kernel command line option or HibernateLocation EFI variable is
           detected, it enables the systemd-hibernate-resume.service(8) unit,
           which will instruct the kernel to resume the system from the
           hibernation image.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-hibernate-resume-generator understands the following
           kernel command line parameters:

           resume=
               Takes a path to the resume device. Both persistent block
               device paths like /dev/disk/by-foo/bar and fstab(5)-style
               specifiers like "FOO=bar" are supported.

               Added in version 217.

           resume_offset=
               Takes the page offset of the swap space from the resume
               device. Defaults to "0".

               Added in version 254.

           resumeflags=
               Takes the resume device mount options to use. Defaults
               rootflags= if not specified.

               Added in version 243.

           noresume
               Do not try to resume from hibernation. If this parameter is
               present, resume= is ignored.

               Added in version 240.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-hibernate-resume.service(8),
           kernel-command-line(7)

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

    systemd 262~devel                                      SYSTEM...ERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.generator(7)](../man7/systemd.generator.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-hibernate-resume.service(8)](../man8/systemd-hibernate-resume.service.8.html)

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
