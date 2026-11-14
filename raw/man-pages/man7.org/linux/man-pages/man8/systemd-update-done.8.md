---
{"title": "systemd-update-done.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-update-done.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-update-done.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8) systemd-update-done.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-update-done.service, systemd-update-done - Mark /etc/ and
           /var/ as fully updated

## [](#SYNOPSIS)SYNOPSIS

           systemd-update-done.service

           /usr/lib/systemd/systemd-update-done

## [](#DESCRIPTION)DESCRIPTION

           systemd-update-done.service is a service that is invoked as part
           of the first boot after the vendor operating system resources in
           /usr/ have been updated. This is useful to implement offline
           updates of /usr/ which might require updates to /etc/ or /var/ on
           the following boot.

           systemd-update-done.service updates the file modification time
           (mtime) stored in and "on" the files /etc/.updated and
           /var/.updated to the modification time of the /usr/ directory,
           unless the stamp files are already newer. (The timestamp is stored
           as the mtime field on the file, but also in the file to support
           filesystems that do not store full timestamp precision.)

           Services that shall run after offline upgrades of /usr/ should
           order themselves before systemd-update-done.service, and use the
           ConditionNeedsUpdate= (see systemd.unit(5)) condition to make sure
           to run when /etc/ or /var/ are older than /usr/ according to the
           modification times of the files described above. This requires
           that updates to /usr/ are always followed by an update of the
           modification time of /usr/, for example by invoking touch(1) on
           it.

           Note that if the systemd.condition_needs_update= kernel command
           line option is used it overrides the ConditionNeedsUpdate= unit
           condition checks. In that case systemd-update-done.service will
           not reset the condition state until a follow-up reboot where the
           kernel switch is not specified anymore.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --root=root
               Takes a directory path as an argument. The program will
               operate on paths below the specified root directory.

               Added in version 258.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.unit(5), touch(1)

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

Pages that refer to this page: [systemd.unit(5)](../man5/systemd.unit.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
