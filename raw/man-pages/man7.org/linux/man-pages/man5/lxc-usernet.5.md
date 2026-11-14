---
{"title": "lxc-usernet(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/lxc-usernet.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-usernet(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-usernet(5)                                             lxc-usernet(5)

## [](#NAME)NAME

           lxc-usernet - unprivileged user network administration file.

## [](#DESCRIPTION)DESCRIPTION

           /etc/lxc/lxc-usernet controls the limits which the program lxc-
           user-nic places on network interfaces which an unprivileged user
           may create.

       CONFIGURATION
           This file consists of multiple entries, one per line, of the form:

           user type bridge number

           or

           @group type bridge number

           Where

           user   is the username to whom this entry applies.

           @group is the groupname to which this entry applies.

           type   is the type of network interface being allowed. Only veth
                  is currently supported.

           bridge is the bridge to which the network interfaces may be
                  attached, for instance lxcbr0.

           number is the number or quota of network interfaces of the given
                  type which the given user or group may attach to the given
                  bridge, for instance 2.

           Since a user can be specified both by username as well as one or
           more usergroups, it is possible that several configuration lines
           enable that user to create network interfaces. In such cases, any
           interfaces create are counted towards the quotas of the user or
           group in the order in which they appear in the file. If the quota
           of one line is full, the rest will be parsed until one is found or
           the end of the file.

## [](#SEE_ALSO)SEE ALSO

           lxc(1), lxc-user-nic(1)

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

                                    2026-04-29                 lxc-usernet(5)

------------------------------------------------------------------------

Pages that refer to this page: [lxc-user-nic(1)](../man1/lxc-user-nic.1.html),  [lxc.conf(5)](../man5/lxc.conf.5.html),  [lxc.system.conf(5)](../man5/lxc.system.conf.5.html)

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
