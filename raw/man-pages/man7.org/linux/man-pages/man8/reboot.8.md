---
{"title": "poweroff(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/reboot.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# poweroff(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    POWEROFF(8)                      poweroff                     POWEROFF(8)

## [](#NAME)NAME

           poweroff, reboot, halt - Power off, reboot, or halt the machine

## [](#SYNOPSIS)SYNOPSIS

           poweroff [OPTIONS...]

           reboot [OPTIONS...]

           halt [OPTIONS...]

## [](#DESCRIPTION)DESCRIPTION

           poweroff, reboot, and halt may be used to power off, reboot, or
           halt the machine. All three commands take the same options.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --help
               Print a short help text and exit.

               Added in version 253.

           --halt
               Halt the machine, regardless of which one of the three
               commands is invoked.

               Added in version 253.

           -p, --poweroff
               Power off the machine, when either halt or poweroff is
               invoked. This option is ignored when reboot is invoked.

               Added in version 253.

           --reboot
               Reboot the machine, regardless of which one of the three
               commands is invoked.

               Added in version 253.

           -f, --force
               Force immediate power-off, halt, or reboot. If specified, the
               command does not contact the init system. In most cases,
               filesystems are not properly unmounted before shutdown. For
               example, the command reboot -f is mostly equivalent to
               systemctl reboot -ff, instead of systemctl reboot -f.

               Added in version 253.

           -w, --wtmp-only
               Only write wtmp shutdown entry, do not actually power off,
               reboot, or halt.

               Added in version 253.

           -d, --no-wtmp
               Do not write wtmp shutdown entry.

               Added in version 253.

           -n, --no-sync
               Do not sync hard disks/storage media before power-off, reboot,
               or halt.

               Added in version 253.

           --no-wall
               Do not send wall message before power-off, reboot, or halt.

               Added in version 253.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#NOTES)NOTES

           These commands are implemented in a way that preserves basic
           compatibility with the original SysV commands.  systemctl(1) verbs
           poweroff, reboot, halt provide the same functionality with some
           additional features.

           Note that on many SysV systems halt used to be synonymous to
           poweroff, i.e. both commands would equally result in powering the
           machine off. systemd is more accurate here, and halt results in
           halting the machine only (leaving power on), and poweroff is
           required to actually power it off.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), shutdown(8), wall(1)

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

    systemd 262~devel                                             POWEROFF(8)

------------------------------------------------------------------------

Pages that refer to this page: [reboot(2)](../man2/reboot.2.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [fsck.minix(8)](../man8/fsck.minix.8.html),  [mkfs.minix(8)](../man8/mkfs.minix.8.html),  [shutdown(8)](../man8/shutdown.8.html)

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
