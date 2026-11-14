---
{"title": "lxc-usernsexec(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lxc-usernsexec.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-usernsexec(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-usernsexec(1)                                       lxc-usernsexec(1)

## [](#NAME)NAME

           lxc-usernsexec - Run a task as root in a new user namespace.

## [](#SYNOPSIS)SYNOPSIS

           lxc-usernsexec [-m uid-map] {-- command}

## [](#DESCRIPTION)DESCRIPTION

           lxc-usernsexec  can  be  used  to run a task as root in a new user
           namespace.

## [](#OPTIONS)OPTIONS

           -m uid-map
                  The uid map to use in the user namespace. Each map consists
                  of four colon-separate values. First a character 'u', 'g'
                  or 'b' to specify whether this map pertains to user ids,
                  group ids, or both; next the first userid in the user name‐
                  space; next the first userid as seen on the host; and fi‐
                  nally the number of ids to be mapped.

                  More than one map can be specified. If no map is specified,
                  then by default the full uid and gid ranges granted by
                  /etc/subuid and /etc/subgid will be mapped to the uids and
                  gids starting at 0 in the container.

                  Note that lxc-usernsexec always tries to setuid and setgid
                  to 0 in the namespace. Therefore uid 0 in the namespace
                  must be mapped.

## [](#EXAMPLES)EXAMPLES

           To spawn a shell with the full allotted subuids mapped into the
           container, use

                  lxc-usernsexec

           To run a different shell than /bin/sh, use

                  lxc-usernsexec -- /bin/bash

           If your user id is 1000, root in a container is mapped to 190000,
           and you wish to chown a file you own to root in the container, you
           can use:

                  lxc-usernsexec -m b:0:1000:1 -m b:1:190000:1 -- /bin/chown 1:1 $file

           This maps your userid to root in the user namespace, and 190000 to
           uid 1.  Since root in the user namespace is privileged over all
           userids mapped into the namespace, you are allowed to change the
           file ownership, which you could not do on the host using a simple
           chown.

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

                                    2026-04-29              lxc-usernsexec(1)

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
