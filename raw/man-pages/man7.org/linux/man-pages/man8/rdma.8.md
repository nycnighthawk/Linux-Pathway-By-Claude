---
{"title": "rdma(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rdma.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rdma(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RDMA(8)                           Linux                           RDMA(8)

## [](#NAME)NAME

           rdma - RDMA tool

## [](#SYNOPSIS)SYNOPSIS

           rdma [ OPTIONS ] OBJECT { COMMAND | help }

           rdma [ -force ] -batch filename

           OBJECT := { dev | link | resource | system | statistic | monitor }

           OPTIONS := { -V[ersion] | -d[etails] | -j[son] | -o[neline] |
                   -p[retty] }

## [](#OPTIONS)OPTIONS

           -V, -Version
                  Print the version of the rdma tool and exit.

           -b, -batch <FILENAME>
                  Read commands from provided file or standard input and
                  invoke them.  First failure will cause termination of rdma.

           -force Don't terminate rdma on errors in batch mode.  If there
                  were any errors during execution of the commands, the
                  application return code will be non-zero.

           -d, --details
                  Output detailed information.  Adding a second -d includes
                  driver-specific details.

           -r, --raw
                  Output includes driver-specific details in raw format.

           -p, --pretty
                  When combined with -j generate pretty JSON output.

           -j, --json
                  Generate JSON output.

           -o, -oneline
                  Output each record on a single line, replacing line feeds
                  with the '\' character.

       OBJECT
           dev    - RDMA device.

           link   - RDMA port related.

           resource
                  - RDMA resource configuration.

           sys    - RDMA subsystem related.

           statistic
                  - RDMA counter statistic related.

           monitor
                  - RDMA events monitor.

           The names of all objects may be written in full or abbreviated
           form, for example stats can be abbreviated as stat or just s.

       COMMAND
           Specifies the action to perform on the object.  The set of
           possible actions depends on the object type.  As a rule, it is
           possible to show (or list ) objects, but some objects do not allow
           all of these operations or have some additional commands. The help
           command is available for all objects. It prints out a list of
           available commands and argument syntax conventions.

           If no command is given, some default command is assumed.  Usually
           it is list or, if the objects of this class cannot be listed,
           help.

## [](#EXIT_STATUS)EXIT STATUS

           Exit status is 0 if command was successful or a positive integer
           upon failure.

## [](#SEE_ALSO)SEE ALSO

           rdma-dev(8), rdma-link(8), rdma-resource(8), rdma-system(8),
           rdma-statistic(8), rdma-monitor(8),

## [](#REPORTING_BUGS)REPORTING BUGS

           Report any bugs to the Linux RDMA mailing list <linux-
           rdma@vger.kernel.org> where the development and maintenance is
           primarily done.  You do not have to be subscribed to the list to
           send a message there.

## [](#AUTHOR)AUTHOR

           Leon Romanovsky <leonro@mellanox.com>

## [](#COLOPHON)COLOPHON

           This page is part of the iproute2 (utilities for controlling
           TCP/IP networking and traffic) project.  Information about the
           project can be found at 
           ⟨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2⟩.
           If you have a bug report for this manual page, send it to
           netdev@vger.kernel.org, shemminger@osdl.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/network/iproute2/iproute2.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iproute2                       28 Mar 2017                        RDMA(8)

------------------------------------------------------------------------

Pages that refer to this page: [rxe(7)](../man7/rxe.7.html),  [rdma-dev(8)](../man8/rdma-dev.8.html),  [rdma-link(8)](../man8/rdma-link.8.html),  [rdma-monitor(8)](../man8/rdma-monitor.8.html),  [rdma-resource(8)](../man8/rdma-resource.8.html),  [rdma-statistic(8)](../man8/rdma-statistic.8.html),  [rdma-system(8)](../man8/rdma-system.8.html)

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
