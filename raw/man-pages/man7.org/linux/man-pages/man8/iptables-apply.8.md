---
{"title": "iptables-apply(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/iptables-apply.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iptables-apply(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [LEGALESE](#LEGALESE) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPTABLES-APPLY(8)            iptables 1.8.13            IPTABLES-APPLY(8)

## [](#NAME)NAME

           iptables-apply — a safer way to update iptables remotely

## [](#SYNOPSIS)SYNOPSIS

           iptables-apply [-hV] [-t timeout] [-w savefile] {[rulesfile]|-c
           [runcmd]}

## [](#DESCRIPTION)DESCRIPTION

           iptables-apply will try to apply a new rulesfile (as output by
           iptables-save, read by iptables-restore) or run a command to
           configure iptables and then prompt the user whether the changes
           are okay. If the new iptables rules cut the existing connection,
           the user will not be able to answer affirmatively. In this case,
           the script rolls back to the previous working iptables rules after
           the timeout expires.

           Successfully applied rules can also be written to savefile and
           later used to roll back to this state. This can be used to
           implement a store last good configuration mechanism when
           experimenting with an iptables setup script: iptables-apply -w
           /etc/network/iptables.up.rules -c /etc/network/iptables.up.run

           When called as ip6tables-apply, the script will use
           ip6tables-save/-restore and IPv6 default values instead. Default
           value for rulesfile is '/etc/network/iptables.up.rules'.

## [](#OPTIONS)OPTIONS

           -t seconds, --timeout seconds
                  Sets the timeout in seconds after which the script will
                  roll back to the previous ruleset (default: 10).

           -w savefile, --write savefile
                  Specify the savefile where successfully applied rules will
                  be written to (default if empty string is given:
                  /etc/network/iptables.up.rules).

           -c runcmd, --command runcmd
                  Run command runcmd to configure iptables instead of
                  applying a rulesfile (default:
                  /etc/network/iptables.up.run).

           -h, --help
                  Display usage information.

           -V, --version
                  Display version information.

## [](#SEE_ALSO)SEE ALSO

           iptables-restore(8), iptables-save(8), iptables(8).

## [](#LEGALESE)LEGALESE

           Original iptables-apply - Copyright 2006 Martin F. Krafft
           <madduck@madduck.net>.  Version 1.1 - Copyright 2010 GW
           <gw.2010@tnode.com or http://gw.tnode.com/>.

           This manual page was written by Martin F. Krafft
           <madduck@madduck.net> and extended by GW <gw.2010@tnode.com or
           http://gw.tnode.com/>.

           Permission is granted to copy, distribute and/or modify this
           document under the terms of the Artistic License 2.0.

## [](#COLOPHON)COLOPHON

           This page is part of the iptables (administer and maintain packet
           filter rules) project.  Information about the project can be found
           at ⟨http://www.netfilter.org/⟩.  If you have a bug report for this
           manual page, see ⟨http://bugzilla.netfilter.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.netfilter.org/iptables⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-10.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    iptables 1.8.13                                         IPTABLES-APPLY(8)

------------------------------------------------------------------------

Pages that refer to this page: [iptables(8)](../man8/iptables.8.html),  [iptables-restore(8)](../man8/iptables-restore.8.html),  [iptables-save(8)](../man8/iptables-save.8.html)

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
