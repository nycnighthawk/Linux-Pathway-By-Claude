---
{"title": "xtables-nft(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xtables-nft.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xtables-nft(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [USAGE](#USAGE) \| [DIFFERENCES TO LEGACY IPTABLES](#DIFFERENCES_TO_LEGACY_IPTABLES) \| [EXAMPLES](#EXAMPLES) \| [LIMITATIONS](#LIMITATIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    XTABLES-NFT(8)           System Manager's Manual           XTABLES-NFT(8)

## [](#NAME)NAME

           xtables-nft — iptables using nftables kernel api

## [](#DESCRIPTION)DESCRIPTION

           xtables-nft are versions of iptables that use the nftables API.
           This is a set of tools to help the system administrator migrate
           the ruleset from iptables(8), ip6tables(8), arptables(8), and
           ebtables(8) to nftables(8).

           The xtables-nft set is composed of several commands:

           • iptables-nft

           • iptables-nft-save

           • iptables-nft-restore

           • ip6tables-nft

           • ip6tables-nft-save

           • ip6tables-nft-restore

           • arptables-nft

           • ebtables-nft

             These tools use the libxtables framework extensions and hook to
             the nf_tables kernel subsystem using the nft_compat module.

## [](#USAGE)USAGE

           The xtables-nft tools allow you to manage the nf_tables backend
           using the native syntax of iptables(8), ip6tables(8),
           arptables(8), and ebtables(8).

           You should use the xtables-nft tools exactly the same way as you
           would use the corresponding original tools.

           Adding a rule will result in that rule being added to the
           nf_tables kernel subsystem instead.  Listing the ruleset will use
           the nf_tables backend as well.

           When these tools were designed, the main idea was to replace each
           legacy binary with a symlink to the xtables-nft program, for
           example:

                /sbin/iptables -> /usr/sbin/iptables-nft-multi
                /sbin/ip6tables -> /usr/sbin/ip6tables-nft-multi
                /sbin/arptables -> /usr/sbin/arptables-nft-multi
                /sbin/ebtables -> /usr/sbin/ebtables-nft-multi

           The iptables version string will indicate whether the legacy API
           (get/setsockopt) or the new nf_tables api is used:
                iptables -V
                iptables v1.7 (nf_tables)

## [](#DIFFERENCES_TO_LEGACY_IPTABLES)DIFFERENCES TO LEGACY IPTABLES

           Because the xtables-nft tools use the nf_tables kernel API, rule
           additions and deletions are always atomic.  Unlike iptables-
           legacy, iptables-nft -A ..  will NOT need to retrieve the current
           ruleset from the kernel, change it, and re-load the altered
           ruleset.  Instead, iptables-nft will tell the kernel to add one
           rule.  For this reason, the iptables-legacy --wait option is a no-
           op in iptables-nft.

           Use of the xtables-nft tools allow monitoring ruleset changes
           using the xtables-monitor(8) command.

           When using -j TRACE to debug packet traversal to the ruleset, note
           that you will need to use xtables-monitor(8) in --trace mode to
           obtain monitoring trace events.

## [](#EXAMPLES)EXAMPLES

           One basic example is creating the skeleton ruleset in nf_tables
           from the xtables-nft tools, in a fresh machine:

                root@machine:~# iptables-nft -L
                [...]
                root@machine:~# ip6tables-nft -L
                [...]
                root@machine:~# arptables-nft -L
                [...]
                root@machine:~# ebtables-nft -L
                [...]
                root@machine:~# nft list ruleset
                table ip filter {
                     chain INPUT {
                          type filter hook input priority 0; policy accept;
                     }

                     chain FORWARD {
                          type filter hook forward priority 0; policy accept;
                     }

                     chain OUTPUT {
                          type filter hook output priority 0; policy accept;
                     }
                }
                table ip6 filter {
                     chain INPUT {
                          type filter hook input priority 0; policy accept;
                     }

                     chain FORWARD {
                          type filter hook forward priority 0; policy accept;
                     }

                     chain OUTPUT {
                          type filter hook output priority 0; policy accept;
                     }
                }
                table bridge filter {
                     chain INPUT {
                          type filter hook input priority -200; policy accept;
                     }

                     chain FORWARD {
                          type filter hook forward priority -200; policy accept;
                     }

                     chain OUTPUT {
                          type filter hook output priority -200; policy accept;
                     }
                }
                table arp filter {
                     chain INPUT {
                          type filter hook input priority 0; policy accept;
                     }

                     chain FORWARD {
                          type filter hook forward priority 0; policy accept;
                     }

                     chain OUTPUT {
                          type filter hook output priority 0; policy accept;
                     }
                }

           (please note that in fresh machines, listing the ruleset for the
           first time results in all tables an chain being created).

           To migrate your complete filter ruleset, in the case of
           iptables(8), you would use:

                root@machine:~# iptables-legacy-save > myruleset # reads from x_tables
                root@machine:~# iptables-nft-restore myruleset   # writes to nf_tables
           or
                root@machine:~# iptables-legacy-save | iptables-translate-restore | less

           to see how rules would look like in the nft nft(8) syntax.

## [](#LIMITATIONS)LIMITATIONS

           You should use Linux kernel >= 4.17.

           The CLUSTERIP target is not supported.

           To get up-to-date information about this, please head to
           http://wiki.nftables.org/ .

## [](#SEE_ALSO)SEE ALSO

           nft(8), xtables-translate(8), xtables-monitor(8)

## [](#AUTHORS)AUTHORS

           The nftables framework is written by the Netfilter project
           (https://www.netfilter.org).

           This manual page was written by Arturo Borrero Gonzalez
           <arturo@debian.org> for the Debian project, but may be used by
           others.

           This documentation is free/libre under the terms of the GPLv2+.

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

                                    June 2018                  XTABLES-NFT(8)

------------------------------------------------------------------------

Pages that refer to this page: [arptables-nft(8)](../man8/arptables-nft.8.html),  [ebtables-nft(8)](../man8/ebtables-nft.8.html),  [xtables-legacy(8)](../man8/xtables-legacy.8.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man8/xtables-nft.8.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
