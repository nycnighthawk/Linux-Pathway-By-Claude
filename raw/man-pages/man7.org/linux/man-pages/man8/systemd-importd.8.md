---
{"title": "systemd-importd.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-importd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-importd.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-I....SERVICE(8)  systemd-importd.service  SYSTEMD-I....SERVICE(8)

## [](#NAME)NAME

           systemd-importd.service, systemd-importd - VM and container image
           import and export service

## [](#SYNOPSIS)SYNOPSIS

           systemd-importd.service

           /usr/lib/systemd/systemd-importd

## [](#DESCRIPTION)DESCRIPTION

           systemd-importd is a system service that allows importing,
           exporting and downloading of disk images. It provides the
           implementation for importctl(1)'s pull-raw, pull-tar, import-raw,
           import-tar, import-fs, export-raw, and export-tar commands.

           See org.freedesktop.import1(5) and org.freedesktop.LogControl1(5)
           for a description of the D-Bus API.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), importctl(1), systemd-machined.service(8),
           systemd-nspawn(1), org.freedesktop.import1(5)

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

    systemd 262~devel                                 SYSTEMD-I....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [importctl(1)](../man1/importctl.1.html),  [org.freedesktop.import1(5)](../man5/org.freedesktop.import1.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-import-generator(8)](../man8/systemd-import-generator.8.html),  [systemd-machined.service(8)](../man8/systemd-machined.service.8.html)

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
