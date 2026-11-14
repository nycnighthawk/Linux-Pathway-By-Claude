---
{"title": "genl(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/genl.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# genl(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GENL(8)                           Linux                           GENL(8)

## [](#NAME)NAME

           genl - generic netlink utility frontend

## [](#SYNOPSIS)SYNOPSIS

           genl[ OPTIONS ] OBJECT
           genl { -V[ersion] | -h[elp] }

           OPTIONS := { -s[tatistics] | -d[etails] | -j[son] | -p[retty] }

           OBJECT := { ctrl CTRL_OPTS }

           CTRL_OPTS := { help | list | monitor | get PARMS }

           PARMS := { name NAME | id ID }

## [](#DESCRIPTION)DESCRIPTION

           The genl utility provides a simple frontend to the generic netlink
           library. Although it's designed to support multiple OBJECTs, for
           now only the ctrl object is available, which is used to query the
           generic netlink controller.

       ctrl
           The generic netlink controller can be queried in various ways:

           help   This command just prints a help text for the ctrl object.

           list   Show the registered netlink users.

           monitor
                  Listen for generic netlink notifications.

           get    Query the controller for a given user, identified either by
                  name or id.

## [](#OPTIONS)OPTIONS

           genl supports the following options.

           -h, -help
                  Show summary of options.

           -V, -Version
                  Show version of program.

           -s, -stats, -statistics
                  Show object statistics.

           -d, -details
                  Show object details.

           -j, -json
                  Output results in JavaScript Object Notation (JSON).

           -p, -pretty
                  Add indentation for readability.

           -r, -raw
                  Dump raw output only.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           genl was written by Jamal Hadi Salim <hadi@cyberus.ca>.

           This manual page was written by Petr Sabata <contyk@redhat.com>.

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

    iproute2                       29 Oct 2015                        GENL(8)

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
