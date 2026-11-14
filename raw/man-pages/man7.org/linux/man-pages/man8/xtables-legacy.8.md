---
{"title": "xtables-legacy(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xtables-legacy.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xtables-legacy(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [USAGE](#USAGE) \| [LIMITATIONS](#LIMITATIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    XTABLES-LEGACY(8)        System Manager's Manual        XTABLES-LEGACY(8)

## [](#NAME)NAME

           xtables-legacy — iptables using old getsockopt/setsockopt-based
           kernel api

## [](#DESCRIPTION)DESCRIPTION

           xtables-legacy are the original versions of iptables that use old
           getsockopt/setsockopt-based kernel interface.  This kernel
           interface has some limitations, therefore iptables can also be
           used with the newer nf_tables based API.  See xtables-nft(8) for
           information about the xtables-nft variants of iptables.

## [](#USAGE)USAGE

           The xtables-legacy-multi binary can be linked to the traditional
           names:

                /sbin/iptables -> /sbin/iptables-legacy-multi
                /sbin/ip6tables -> /sbin/ip6tables-legacy-multi
                /sbin/iptables-save -> /sbin/ip6tables-legacy-multi
                /sbin/iptables-restore -> /sbin/ip6tables-legacy-multi

           The iptables version string will indicate whether the legacy API
           (get/setsockopt) or the new nf_tables API is used:
                iptables -V
                iptables v1.7 (legacy)

## [](#LIMITATIONS)LIMITATIONS

           When inserting a rule using iptables -A or iptables -I, iptables
           first needs to retrieve the current active ruleset, change it to
           include the new rule, and then commit back the result.  This means
           that if two instances of iptables are running concurrently, one of
           the updates might be lost.  This can be worked around partially
           with the --wait option.

           There is also no method to monitor changes to the ruleset, except
           periodically calling iptables-legacy-save and checking for any
           differences in output.  xtables-monitor(8) will need the
           xtables-nft(8) versions to work, it cannot display changes made
           using the iptables-legacy tools.

## [](#SEE_ALSO)SEE ALSO

           xtables-nft(8), xtables-translate(8)

## [](#AUTHORS)AUTHORS

           Rusty Russell originally wrote iptables, in early consultation
           with Michael Neuling.

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

                                    June 2018               XTABLES-LEGACY(8)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man8/xtables-legacy.8.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
