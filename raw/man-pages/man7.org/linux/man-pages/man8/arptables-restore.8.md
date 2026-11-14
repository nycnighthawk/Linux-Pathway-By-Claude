---
{"title": "arptables-nft-restore(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/arptables-restore.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# arptables-nft-restore(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ARPTABLES-RESTORE(8)                                 ARPTABLES-RESTORE(8)

## [](#NAME)NAME

           arptables-restore — Restore ARP Tables (nft-based)

## [](#SYNOPSIS)SYNOPSIS

           arptables-restore

## [](#DESCRIPTION)DESCRIPTION

           arptables-restore is used to restore ARP Tables from data
           specified on STDIN or via a file as first argument.  Use I/O
           redirection provided by your shell to read from a file

           arptables-restore
                  flushes (deletes) all previous contents of the respective
                  ARP Table.

## [](#AUTHOR)AUTHOR

           Jesper Dangaard Brouer <brouer@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           arptables-save(8), arptables(8)

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

                                    March 2019           ARPTABLES-RESTORE(8)

------------------------------------------------------------------------

Pages that refer to this page: [arptables-nft-save(8)](../man8/arptables-nft-save.8.html)

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
