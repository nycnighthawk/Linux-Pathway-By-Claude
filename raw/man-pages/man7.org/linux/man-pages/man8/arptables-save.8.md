---
{"title": "arptables-nft-save(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/arptables-save.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# arptables-nft-save(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ARPTABLES-SAVE(8)                                       ARPTABLES-SAVE(8)

## [](#NAME)NAME

           arptables-save — dump arptables rules to stdout (nft-based)

## [](#SYNOPSIS)SYNOPSIS

           arptables-save [-M modprobe] [-c]

           arptables-save [-V]

## [](#DESCRIPTION)DESCRIPTION

           arptables-save is used to dump the contents of an ARP Table in
           easily parseable format to STDOUT. Use I/O-redirection provided by
           your shell to write to a file.

           -M, --modprobe modprobe_program
                  Specify the path to the modprobe program. By default,
                  arptables-save will inspect /proc/sys/kernel/modprobe to
                  determine the executable's path.

           -c, --counters
                  Include the current values of all packet and byte counters
                  in the output.

           -V, --version
                  Print version information and exit.

## [](#AUTHOR)AUTHOR

           Jesper Dangaard Brouer <brouer@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           arptables-restore(8), arptables(8)

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

                                    March 2019              ARPTABLES-SAVE(8)

------------------------------------------------------------------------

Pages that refer to this page: [arptables-nft-restore(8)](../man8/arptables-nft-restore.8.html)

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
