---
{"title": "lxc-stop(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lxc-stop.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-stop(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT VALUE](#EXIT_VALUE) \| [DIAGNOSTIC](#DIAGNOSTIC) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-stop(1)                                                   lxc-stop(1)

## [](#NAME)NAME

           lxc-stop - stop the application running inside a container

## [](#SYNOPSIS)SYNOPSIS

           lxc-stop {-n name} [-W] [-r] [-t timeout] [-k] [--nokill]
                    [--nolock]

## [](#DESCRIPTION)DESCRIPTION

           lxc-stop  reboots,  cleanly shuts down, or kills all the processes
           inside the container. By default, it will request a clean shutdown
           of the container by sending lxc.signal.halt (defaults  to  SIGPWR)
           to  the container's init process, waiting up to 60 seconds for the
           container to exit, and then returning. If the container  fails  to
           cleanly  exit  in  60 seconds, it will be sent the lxc.signal.stop
           (defaults to SIGKILL) to force it to shut down. A request  to  re‐
           boot  will  send the lxc.signal.reboot (defaults to SIGINT) to the
           container's init process.

           The [-W], [-r], [-k] and [--nokill] options specify the action  to
           perform.   [-W]  indicates that after performing the specified ac‐
           tion, lxc-stop should immediately exit, while [-t TIMEOUT]  speci‐
           fies  the maximum amount of time to wait for the container to com‐
           plete the shutdown or reboot.

## [](#OPTIONS)OPTIONS

           -r,--reboot
                  Request a reboot of the container.

           -k,--kill
                  Rather than requesting a clean shutdown of the container,
                  explicitly kill all tasks in the container. This is the
                  legacy lxc-stop behavior.

           --nokill
                  Only request a clean shutdown, do not kill the container
                  tasks if the clean shutdown fails.

           --nolock
                  This option avoids the use of any of the API lxc locking,
                  and should only be used if lxc-stop is hanging due to a bad
                  system state.

           -W,--nowait
                  Simply perform the requestion action (reboot, shutdown, or
                  hard kill) and exit.

           -t,--timeout TIMEOUT
                  Wait TIMEOUT seconds before hard-stopping the container.

## [](#EXIT_VALUE)EXIT VALUE

           0      The container was successfully stopped.

           1      An error occurred while stopping the container.

           2      The specified container exists but was not running.

## [](#DIAGNOSTIC)DIAGNOSTIC

           The container was not found
                  The specified container was not created before with the
                  lxc-create command.

## [](#SEE_ALSO)SEE ALSO

           lxc(7), lxc-create(1), lxc-copy(1), lxc-destroy(1), lxc-start(1),
           lxc-stop(1), lxc-execute(1), lxc-console(1), lxc-monitor(1),
           lxc-wait(1), lxc-cgroup(1), lxc-ls(1), lxc-info(1), lxc-freeze(1),
           lxc-unfreeze(1), lxc-attach(1), lxc.conf(5)

## [](#COLOPHON)COLOPHON

           This page is part of the lxc (Linux containers) project.  Informa‐
           tion about the project can be found at 
           ⟨http://linuxcontainers.org/⟩.  If you have a bug report for this
           manual page, send it to lxc-devel@lists.linuxcontainers.org.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/lxc/lxc.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-23.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2026-04-29                    lxc-stop(1)

------------------------------------------------------------------------

Pages that refer to this page: [lxc-attach(1)](../man1/lxc-attach.1.html),  [lxc-autostart(1)](../man1/lxc-autostart.1.html),  [lxc-cgroup(1)](../man1/lxc-cgroup.1.html),  [lxc-checkconfig(1)](../man1/lxc-checkconfig.1.html),  [lxc-checkpoint(1)](../man1/lxc-checkpoint.1.html),  [lxc-config(1)](../man1/lxc-config.1.html),  [lxc-console(1)](../man1/lxc-console.1.html),  [lxc-copy(1)](../man1/lxc-copy.1.html),  [lxc-create(1)](../man1/lxc-create.1.html),  [lxc-destroy(1)](../man1/lxc-destroy.1.html),  [lxc-device(1)](../man1/lxc-device.1.html),  [lxc-execute(1)](../man1/lxc-execute.1.html),  [lxc-freeze(1)](../man1/lxc-freeze.1.html),  [lxc-info(1)](../man1/lxc-info.1.html),  [lxc-ls(1)](../man1/lxc-ls.1.html),  [lxc-monitor(1)](../man1/lxc-monitor.1.html),  [lxc-snapshot(1)](../man1/lxc-snapshot.1.html),  [lxc-start(1)](../man1/lxc-start.1.html),  [lxc-stop(1)](../man1/lxc-stop.1.html),  [lxc-top(1)](../man1/lxc-top.1.html),  [lxc-unfreeze(1)](../man1/lxc-unfreeze.1.html),  [lxc-unshare(1)](../man1/lxc-unshare.1.html),  [lxc-update-config(1)](../man1/lxc-update-config.1.html),  [lxc-usernsexec(1)](../man1/lxc-usernsexec.1.html),  [lxc-wait(1)](../man1/lxc-wait.1.html),  [lxc.container.conf(5)](../man5/lxc.container.conf.5.html),  [lxc.system.conf(5)](../man5/lxc.system.conf.5.html),  [lxc(7)](../man7/lxc.7.html)

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
