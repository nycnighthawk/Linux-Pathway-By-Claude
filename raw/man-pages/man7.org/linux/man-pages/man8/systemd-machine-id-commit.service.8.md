---
{"title": "systemd-machine-id-commit.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-machine-id-commit.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-machine-id-commit.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEM...ERVICE(8)  systemd-machine-id-commit.service  SYSTEM...ERVICE(8)

## [](#NAME)NAME

           systemd-machine-id-commit.service - Commit a transient machine ID
           to disk

## [](#SYNOPSIS)SYNOPSIS

           systemd-machine-id-commit.service

## [](#DESCRIPTION)DESCRIPTION

           systemd-machine-id-commit.service is an early boot service
           responsible for committing transient /etc/machine-id files to a
           writable disk file system. See machine-id(5) for more information
           about machine IDs.

           This service is started after local-fs.target in case
           /etc/machine-id is a mount point of its own (usually from a memory
           file system such as "tmpfs") and /etc is writable. The service
           will invoke systemd-machine-id-setup --commit, which writes the
           current transient machine ID to disk and unmount the
           /etc/machine-id file in a race-free manner to ensure that file is
           always valid and accessible for other processes. See
           systemd-machine-id-setup(1) for details.

           The main use case of this service are systems where
           /etc/machine-id is read-only and initially not initialized. In
           this case, the system manager will generate a transient machine ID
           file on a memory file system, and mount it over /etc/machine-id,
           during the early boot phase. This service is then invoked in a
           later boot phase, as soon as /etc/ has been remounted writable and
           the ID may thus be committed to disk to make it permanent.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-machine-id-setup(1), machine-id(5),
           systemd-firstboot(1)

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

    systemd 262~devel                                      SYSTEM...ERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [systemd-machine-id-setup(1)](../man1/systemd-machine-id-setup.1.html),  [machine-id(5)](../man5/machine-id.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
