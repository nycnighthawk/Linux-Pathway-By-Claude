---
{"title": "lxc.system.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/lxc.system.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc.system.conf(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc.system.conf(5)                                     lxc.system.conf(5)

## [](#NAME)NAME

           lxc.system.conf - LXC system configuration file

## [](#DESCRIPTION)DESCRIPTION

           The system configuration is located at /etc/lxc/lxc.conf or
           ~/.config/lxc/lxc.conf for unprivileged containers.

           This configuration file is used to set values such as default
           lookup paths and storage backend settings for LXC.

       CONFIGURATION PATHS
           lxc.lxcpath
                  The location in which all containers are stored.

           lxc.default_config
                  The path to the default container configuration.

       CONTROL GROUPS
           lxc.cgroup.use
                  Comma separated list of cgroup controllers to setup.  If
                  none is specified, all available controllers will be used.

           lxc.cgroup.pattern
                  Format string used to generate the cgroup path (e.g.
                  lxc/%n).

       LVM
           lxc.bdev.lvm.vg
                  Default LVM volume group name.

           lxc.bdev.lvm.thin_pool
                  Default LVM thin pool name.

       ZFS
           lxc.bdev.zfs.root
                  Default ZFS root name.

    %%%SH%%%
           lxc(1), lxc.container.conf(5), lxc.system.conf(5), lxc-usernet(5)

## [](#SEE_ALSO)SEE ALSO

           lxc(7), lxc-create(1), lxc-copy(1), lxc-destroy(1), lxc-start(1),
           lxc-stop(1), lxc-execute(1), lxc-console(1), lxc-monitor(1),
           lxc-wait(1), lxc-cgroup(1), lxc-ls(1), lxc-info(1), lxc-freeze(1),
           lxc-unfreeze(1), lxc-attach(1), lxc.conf(5)

## [](#COLOPHON)COLOPHON

           This page is part of the lxc (Linux containers) project.
           Information about the project can be found at 
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

                                    2026-04-29             lxc.system.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [lxc.conf(5)](../man5/lxc.conf.5.html),  [lxc.system.conf(5)](../man5/lxc.system.conf.5.html)

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
