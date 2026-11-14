---
{"title": "shutdown(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/shutdown.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# shutdown(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [COMPATIBILITY](#COMPATIBILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SHUTDOWN(8)                      shutdown                     SHUTDOWN(8)

## [](#NAME)NAME

           shutdown - Halt, power off or reboot the machine

## [](#SYNOPSIS)SYNOPSIS

           shutdown [OPTIONS...] [TIME] [WALL...]

## [](#DESCRIPTION)DESCRIPTION

           shutdown may be used to halt, power off, or reboot the machine.

           The first argument may be a time string (which is usually "now").
           Optionally, this may be followed by a wall message to be sent to
           all logged-in users before going down.

           The time string may either be in the format "hh:mm" for
           hour/minutes specifying the time to execute the shutdown at,
           specified in 24h clock format. Alternatively it may be in the
           syntax "+m" referring to the specified number of minutes m from
           now.  "now" is an alias for "+0", i.e. for triggering an immediate
           shutdown. If no time argument is specified, "+1" is implied.

           The time string specifies the earliest point in time the shutdown
           may take place; it is a lower bound only: the shutdown is executed
           as soon as possible, but not before the specified time. Specifying
           a time that already elapsed (for example an "hh:mm" time earlier
           today) is not an error and results in an immediate shutdown. See
           the discussion of --when= in systemctl(1) for details.

           Note that to specify a wall message you must specify a time
           argument, too.

           If the time argument is used, 5 minutes before the system goes
           down the /run/nologin file is created to ensure that further
           logins shall not be allowed.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --help
               Print a short help text and exit.

           -H, --halt
               Halt the machine.

           -P, --poweroff
               Power the machine off (the default).

           -r, --reboot
               Reboot the machine.

           -h
               The same as --poweroff, but does not override the action to
               take if it is "halt". E.g.  shutdown --reboot -h means
               "poweroff", but shutdown --halt -h means "halt".

           -k
               Do not halt, power off, or reboot, but just write the wall
               message.

           --no-wall
               Do not send wall message before halt, power off, or reboot.

           -c
               Cancel a pending shutdown. This may be used to cancel the
               effect of an invocation of shutdown with a time argument that
               is not "+0" or "now".

           --show
               Show a pending shutdown action and time if there is any.

               Added in version 250.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#COMPATIBILITY)COMPATIBILITY

           The
            shutdown command in previous init systems (including sysvinit)
           defaulted to single-user mode instead of powering off the machine.
           To change into single-user mode, use systemctl rescue instead.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), halt(8), wall(1)

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

    systemd 262~devel                                             SHUTDOWN(8)

------------------------------------------------------------------------

Pages that refer to this page: [last(1@@util-linux)](../man1/last.1@@util-linux.html),  [login(1)](../man1/login.1.html),  [wall(1)](../man1/wall.1.html),  [reboot(2)](../man2/reboot.2.html),  [nologin(5)](../man5/nologin.5.html),  [boot(7)](../man7/boot.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [kexec(8)](../man8/kexec.8.html),  [poweroff(8)](../man8/poweroff.8.html)

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
