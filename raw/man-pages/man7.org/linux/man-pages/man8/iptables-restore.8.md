---
{"title": "iptables-restore(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/iptables-restore.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iptables-restore(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPTABLES-RESTORE(8)          iptables 1.8.13          IPTABLES-RESTORE(8)

## [](#NAME)NAME

           iptables-restore — Restore IP Tables

           ip6tables-restore — Restore IPv6 Tables

## [](#SYNOPSIS)SYNOPSIS

           iptables-restore [-chntvV] [-w seconds] [-M modprobe] [-T name]
           [file]

           ip6tables-restore [-chntvV] [-w seconds] [-M modprobe] [-T name]
           [file]

## [](#DESCRIPTION)DESCRIPTION

           iptables-restore and ip6tables-restore are used to restore IP and
           IPv6 Tables from data specified on STDIN or in file. Use I/O
           redirection provided by your shell to read from a file or specify
           file as an argument.

           -c, --counters
                  Restore the values of all packet and byte counters.

           -h, --help
                  Print a short option summary.

           -n, --noflush
                  Don't flush the previous contents of the table. If not
                  specified, both commands flush (delete) all previous
                  contents of the respective table.  Note that this option
                  will flush user-defined chains if they are declared.
                  Example:

               *filter
               :FILTERS - [0:0]
               -A FILTERS ...

               will flush and re-build the FILTERS chain from scratch, while
               retaining the content of all other chains in the table.

           -t, --test
                  Only parse and construct the ruleset, but do not commit it.

           -v, --verbose
                  Print additional debug info during ruleset processing.
                  Specify multiple times to increase debug level.

           -V, --version
                  Print the program version number.

           -w, --wait [seconds]
                  Wait for the xtables lock.  To prevent multiple instances
                  of the program from running concurrently, an attempt will
                  be made to obtain an exclusive lock at launch.  By default,
                  the program will exit if the lock cannot be obtained.  This
                  option will make the program wait (indefinitely or for
                  optional seconds) until the exclusive lock can be obtained.

           -M, --modprobe modprobe
                  Specify the path to the modprobe(8) program. By default,
                  iptables-restore will inspect /proc/sys/kernel/modprobe to
                  determine the executable's path.

           -T, --table name
                  Restore only the named table even if the input stream
                  contains other ones.

## [](#BUGS)BUGS

           None known as of iptables-1.2.1 release

## [](#AUTHORS)AUTHORS

           Harald Welte <laforge@gnumonks.org> wrote iptables-restore based
           on code from Rusty Russell.
           Andras Kis-Szabo <kisza@sch.bme.hu> contributed ip6tables-restore.

## [](#SEE_ALSO)SEE ALSO

           iptables-apply(8), iptables-save(8), iptables(8)

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

    iptables 1.8.13                                       IPTABLES-RESTORE(8)

------------------------------------------------------------------------

Pages that refer to this page: [iptables-xml(1)](../man1/iptables-xml.1.html),  [iptables(8)](../man8/iptables.8.html),  [iptables-apply(8)](../man8/iptables-apply.8.html),  [iptables-save(8)](../man8/iptables-save.8.html)

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
