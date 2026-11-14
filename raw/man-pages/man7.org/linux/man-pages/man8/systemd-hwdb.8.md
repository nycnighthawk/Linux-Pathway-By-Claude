---
{"title": "systemd-hwdb(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-hwdb.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-hwdb(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-HWDB(8)                systemd-hwdb               SYSTEMD-HWDB(8)

## [](#NAME)NAME

           systemd-hwdb - hardware database management tool

## [](#SYNOPSIS)SYNOPSIS

           systemd-hwdb [options] update

           systemd-hwdb [options] query modalias

## [](#DESCRIPTION)DESCRIPTION

           systemd-hwdb expects a command and command specific arguments. It
           manages the binary hardware database.

## [](#OPTIONS)OPTIONS

           --usr
               Generate in /usr/lib/udev instead of /etc/udev.

               Added in version 219.

           -r, --root=PATH
               Alternate root path in the filesystem.

               Added in version 219.

           -s, --strict
               When updating, return non-zero exit value on any parsing
               error.

               Added in version 239.

           -h, --help
               Print a short help text and exit.

       systemd-hwdb [options] update
           Update the binary database.

       systemd-hwdb [options] query MODALIAS
           Query database and print result.

## [](#SEE_ALSO)SEE ALSO

           systemd(1) hwdb(7)

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

    systemd 262~devel                                         SYSTEMD-HWDB(8)

------------------------------------------------------------------------

Pages that refer to this page: [sd-hwdb(3)](../man3/sd-hwdb.3.html),  [sd_hwdb_get(3)](../man3/sd_hwdb_get.3.html),  [sd_hwdb_new(3)](../man3/sd_hwdb_new.3.html),  [hwdb(7)](../man7/hwdb.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
