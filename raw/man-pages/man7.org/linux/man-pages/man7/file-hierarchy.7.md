---
{"title": "file-hierarchy(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/file-hierarchy.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# file-hierarchy(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FILE-HIERARCHY(7)             file-hierarchy            FILE-HIERARCHY(7)

## [](#NAME)NAME

           file-hierarchy - systemd file system hierarchy requirements

## [](#DESCRIPTION)DESCRIPTION

           Operating systems using the systemd(1) system and service manager
           are organized based on a file system hierarchy inspired by UNIX,
           as described in UAPI.9 Linux File System Hierarchy[1]. Additional
           requirements on when given parts of the hierarchy must be
           available during boot are listed in Mount Requirements[2].

           Many of the paths described here can be queried with the
           systemd-path(1) tool.

## [](#SEE_ALSO)SEE ALSO

               hier(7)
               File System Hierarchy[3]
               XDG Base Directory Specification[4]
               XDG User Directories[5]

## [](#NOTES)NOTES

            1. UAPI.9 Linux File System Hierarchy
               https://uapi-group.org/specifications/specs/linux_file_system_hierarchy/

            2. Mount Requirements
               https://systemd.io/MOUNT_REQUIREMENTS/

            3. File System Hierarchy
               http://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html

            4. XDG Base Directory Specification
               https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html

            5. XDG User Directories
               https://www.freedesktop.org/wiki/Software/xdg-user-dirs

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

    systemd 262~devel                                       FILE-HIERARCHY(7)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-path(1)](../man1/systemd-path.1.html),  [daemon(7)](../man7/daemon.7.html),  [hier(7)](../man7/hier.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
