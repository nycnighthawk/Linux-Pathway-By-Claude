---
{"title": "lxc-autostart(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lxc-autostart.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-autostart(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTOSTART AND SYSTEM BOOT](#AUTOSTART_AND_SYSTEM_BOOT) \| [STARTUP GROUP EXAMPLES](#STARTUP_GROUP_EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-autostart(1)                                         lxc-autostart(1)

## [](#NAME)NAME

           lxc-autostart - start/stop/kill auto-started containers

## [](#SYNOPSIS)SYNOPSIS

           lxc-autostart [-k] [-L] [-r] [-s] [-a] [-A] [-g groups] [-t
                         timeout]

## [](#DESCRIPTION)DESCRIPTION

           lxc-autostart  processes  containers  with  lxc.start.auto set. It
           lets the user start, shutdown, kill,  restart  containers  in  the
           right  order,  waiting  the  right  time.  Supports  filtering  by
           lxc.group or just run against all defined containers. It can  also
           be  used  by  external  tools in list mode where no action will be
           performed and the list of affected containers  (and  if  relevant,
           delays) will be shown.

           The [-r], [-s] and [-k] options specify the action to perform.  If
           none  is specified, then the containers will be started.  [-a] and
           [-g] are used to specify which containers will be affected. By de‐
           fault only containers without a lxc.group set  will  be  affected.
           [-t  TIMEOUT] specifies the maximum amount of time to wait for the
           container to complete the shutdown or reboot.

## [](#OPTIONS)OPTIONS

           -r,--reboot
                  Request a reboot of the container.

           -s,--shutdown
                  Request a clean shutdown. If a [-t timeout] greater than 0
                  is given and the container has not shut down within this
                  period, it will be killed as with the [-k kill] option.

           -k,--kill
                  Rather than requesting a clean shutdown of the container,
                  explicitly kill all tasks in the container.

           -L,--list
                  Rather than performing the action, just print the container
                  name and wait delays until starting the next container.

           -t,--timeout TIMEOUT
                  Wait TIMEOUT seconds before hard-stopping the container.

           -g,--groups GROUP
                  Comma separated list of groups to select (defaults to those
                  without a lxc.group - the NULL group).  This option may be
                  specified multiple times and the arguments concatenated.
                  The NULL or empty group may be specified as a leading com‐
                  ma, trailing comma, embedded double comma, or empty argu‐
                  ment where the NULL group should be processed.  Groups are
                  processed in the order specified on the command line. Mul‐
                  tiple invocations of the -g option may be freely intermixed
                  with the comma separated lists and will be combined in
                  specified order.

           -a,--all
                  Ignore lxc.group and select all auto-started containers.

           -A,--ignore-auto
                  Ignore the lxc.start.auto flag. Combined with -a, will se‐
                  lect all containers on the system.

## [](#AUTOSTART_AND_SYSTEM_BOOT)AUTOSTART AND SYSTEM BOOT

           The lxc-autostart command is used as part of the LXC system ser‐
           vice, when enabled to run on host system at bootup and at shut‐
           down. It's used to select which containers to start in what order
           and how much to delay between each startup when the host system
           boots.

           Each container can be part of any number of groups or no group at
           all.  Two groups are special. One is the NULL group, i.e. the con‐
           tainer does not belong to any group. The other group is the "on‐
           boot" group.

           When the system boots with the LXC service enabled, it will first
           attempt to boot any containers with lxc.start.auto == 1 that is a
           member of the "onboot" group. The startup will be in order of
           lxc.start.order.  If an lxc.start.delay has been specified, that
           delay will be honored before attempting to start the next contain‐
           er to give the current container time to begin initialization and
           reduce overloading the host system. After starting the members of
           the "onboot" group, the LXC system will proceed to boot containers
           with lxc.start.auto == 1 which are not members of any group (the
           NULL group) and proceed as with the onboot group.

## [](#STARTUP_GROUP_EXAMPLES)STARTUP GROUP EXAMPLES

           -g "onboot,"
                  Start the "onboot" group first then the NULL group.

                  This is the equivalent of: -g onboot -g "".

           -g "dns,web,,onboot"
                  Starts the "dns" group first, the "web" group second, then
                  the NULL group followed by the "onboot" group.

                  This is the equivalent of: -g dns,web -g ,onboot or -g dns
                  -g web -g "" -g onboot.

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

                                    2026-04-29               lxc-autostart(1)

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
