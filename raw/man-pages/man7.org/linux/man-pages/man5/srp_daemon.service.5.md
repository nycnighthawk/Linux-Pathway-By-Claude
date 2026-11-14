---
{"title": "srp_daemon.service(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/srp_daemon.service.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# srp_daemon.service(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SRP_DAEMON.SERVICE(5)       srp_daemon.service      SRP_DAEMON.SERVICE(5)

## [](#NAME)NAME

           srp_daemon.service - srp_daemon systemd service that controls all
           ports

## [](#SYNOPSIS)SYNOPSIS

           srp_daemon.service

## [](#DESCRIPTION)DESCRIPTION

           The srp_daemon.service controls whether or not any srp_daemon
           processes are running. Although no srp_daemon processes are
           controlled directly by the srp_daemon.service, this service
           controls whether or not any srp_daemon_port@.service are allowed
           to be active. Each srp_daemon_port@.service controls one
           srp_daemon process.

## [](#SEE_ALSO)SEE ALSO

           srp_daemon(1), srp_daemon_port@.service(5), systemctl(1)

## [](#COLOPHON)COLOPHON

           This page is part of the rdma-core (RDMA Core Userspace Libraries
           and Daemons) project.  Information about the project can be found
           at ⟨https://github.com/linux-rdma/rdma-core⟩.  If you have a bug
           report for this manual page, send it to
           linux-rdma@vger.kernel.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/linux-rdma/rdma-core.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    srp_daemon                                          SRP_DAEMON.SERVICE(5)

------------------------------------------------------------------------

Pages that refer to this page: [srp_daemon_port@.service(5)](../man5/srp_daemon_port@.service.5.html)

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
