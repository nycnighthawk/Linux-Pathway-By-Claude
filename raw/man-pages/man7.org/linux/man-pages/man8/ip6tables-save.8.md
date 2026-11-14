---
{"title": "iptables-save(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip6tables-save.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iptables-save(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPTABLES-SAVE(8)             iptables 1.8.13             IPTABLES-SAVE(8)

## [](#NAME)NAME

           iptables-save — dump iptables rules

           ip6tables-save — dump iptables rules

## [](#SYNOPSIS)SYNOPSIS

           iptables-save [-M modprobe] [-c] [-t table] [-f filename]

           ip6tables-save [-M modprobe] [-c] [-t table] [-f filename]

## [](#DESCRIPTION)DESCRIPTION

           iptables-save and ip6tables-save are used to dump the contents of
           IP or IPv6 Table in easily parseable format either to STDOUT or to
           a specified file.

           -M, --modprobe modprobe
                  Specify the path to the modprobe(8) program. By default,
                  iptables-save will inspect /proc/sys/kernel/modprobe to
                  determine the executable's path.

           -f, --file filename
                  Specify a filename to log the output to. If not specified,
                  iptables-save will log to STDOUT.

           -c, --counters
                  Include the current values of all packet and byte counters
                  in the output.

           -t, --table tablename
                  Restrict output to only one table. If the kernel is
                  configured with automatic module loading, an attempt will
                  be made to load the appropriate module for that table if it
                  is not already there.
                  If not specified, output includes all available tables. No
                  module loading takes place, so in order to include a
                  specific table in the output, the respective module
                  (something like iptable_mangle or ip6table_raw) must be
                  loaded first.

## [](#BUGS)BUGS

           None known as of iptables-1.2.1 release

## [](#AUTHORS)AUTHORS

           Harald Welte <laforge@gnumonks.org>
           Rusty Russell <rusty@rustcorp.com.au>
           Andras Kis-Szabo <kisza@sch.bme.hu> contributed ip6tables-save.

## [](#SEE_ALSO)SEE ALSO

           iptables-apply(8), iptables-restore(8), iptables(8)

           The iptables-HOWTO, which details more iptables usage, the NAT-
           HOWTO, which details NAT, and the netfilter-hacking-HOWTO which
           details the internals.

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

    iptables 1.8.13                                          IPTABLES-SAVE(8)

------------------------------------------------------------------------

Pages that refer to this page: [iptables-xml(1)](../man1/iptables-xml.1.html),  [iptables(8)](../man8/iptables.8.html),  [iptables-apply(8)](../man8/iptables-apply.8.html),  [iptables-restore(8)](../man8/iptables-restore.8.html),  [xtables-translate(8)](../man8/xtables-translate.8.html)

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
