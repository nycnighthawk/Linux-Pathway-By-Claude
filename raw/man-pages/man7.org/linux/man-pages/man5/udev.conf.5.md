---
{"title": "udev.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/udev.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# udev.conf(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UDEV.CONF(5)                    udev.conf                    UDEV.CONF(5)

## [](#NAME)NAME

           udev.conf, udev.conf.d - Configuration for device event managing
           daemon

## [](#SYNOPSIS)SYNOPSIS

               /etc/udev/udev.conf
               /run/udev/udev.conf
               /usr/local/lib/udev/udev.conf
               /usr/lib/udev/udev.conf
               /etc/udev/udev.conf.d/*.conf
               /run/udev/udev.conf.d/*.conf
               /usr/local/lib/udev/udev.conf.d/*.conf
               /usr/lib/udev/udev.conf.d/*.conf

## [](#DESCRIPTION)DESCRIPTION

           These files contain configuration options for systemd-udevd(8).
           The syntax of these files is very simple: a list of assignments,
           one per line. All empty lines or lines beginning with "#" are
           ignored.

           The following options can be set:

           udev_log=
               The log level. Valid values are the numerical syslog
               priorities or their textual representations: err, info and
               debug.

                   Note
                   This option is also honored by udevadm(8).
               Added in version 216.

           children_max=
               An integer. The maximum number of events executed in parallel.
               When unspecified or 0 is specified, the maximum is determined
               based on the system resources.

               This is the same as the --children-max= option.

               Added in version 240.

           exec_delay=
               An integer. Delay the execution of each RUN{program} parameter
               by the given number of seconds. This option might be useful
               when debugging system crashes during coldplug caused by
               loading non-working kernel modules.

               This is the same as the --exec-delay= option.

               Added in version 240.

           event_timeout=
               An integer. The number of seconds to wait for events to
               finish. After this time, the event will be terminated. The
               default is 180 seconds.

               This is the same as the --event-timeout= option.

               Added in version 240.

           resolve_names=
               Specifies when systemd-udevd should resolve names of users and
               groups. When set to early (the default), names will be
               resolved when the rules are parsed. When set to late, names
               will be resolved for every event. When set to never, names
               will never be resolved and all devices will be owned by root.

               This is the same as the --resolve-names= option.

               Added in version 240.

           timeout_signal=
               Specifies a signal that systemd-udevd will send on worker
               timeouts. Note that both workers and spawned processes will be
               killed using this signal. Defaults to SIGKILL.

               Added in version 246.

           In addition, systemd-udevd can be configured by command line
           options and the kernel command line (see systemd-udevd(8)).

## [](#SEE_ALSO)SEE ALSO

           systemd-udevd(8), udev(7), udevadm(8)

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

    systemd 262~devel                                            UDEV.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-udevd.service(8)](../man8/systemd-udevd.service.8.html),  [udevadm(8)](../man8/udevadm.8.html)

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
