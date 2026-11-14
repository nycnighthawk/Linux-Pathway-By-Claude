---
{"title": "lxc-update-config(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lxc-update-config.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-update-config(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-update-config(1)                                 lxc-update-config(1)

## [](#NAME)NAME

           lxc-update-config - update a legacy pre LXC 2.1 configuration file

## [](#SYNOPSIS)SYNOPSIS

           lxc-update-config {-c config}

## [](#DESCRIPTION)DESCRIPTION

           lxc-update-config  detects  any  legacy  configuration keys in the
           given config file and will replace them with the  appropriate  new
           configuration keys.

           lxc-update-config  will  first  create  a backup of the old config
           file in the same directory and name it config.backup and then  up‐
           date  the  original config file in place. In case the update fails
           to apply or leads to an invalid config file that cannot be used to
           start a container  users  can  either  compare  config  with  con‐
           fig.backup  and  try to manually repair any the invalid configura‐
           tion keys or simply rollback to the legacy configuration  file  by
           copying config.backup to config.

           Any  failures  for  lxc-update-config to generate a useable config
           file are a bug and should be reported upstream.

## [](#OPTIONS)OPTIONS

           -c, --config
                  Path to the configuration file to update.

           -h, --help

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

                                    2026-04-29           lxc-update-config(1)

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
