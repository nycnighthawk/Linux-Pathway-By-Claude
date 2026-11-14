---
{"title": "proc_scsi(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_scsi.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_scsi(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_scsi(5)               File Formats Manual               proc_scsi(5)

## [](#NAME)NAME

           /proc/scsi/ - SCSI

## [](#DESCRIPTION)DESCRIPTION

           /proc/scsi/
                  A directory with the scsi mid-level pseudo-file and various
                  SCSI low-level driver directories, which contain a file for
                  each SCSI host in this system, all of which give the status
                  of some part of the SCSI IO subsystem.  These files contain
                  ASCII structures and are, therefore, readable with cat(1).

                  You can also write to some of the files to reconfigure the
                  subsystem or switch certain features on or off.

           /proc/scsi/scsi
                  This is a listing of all SCSI devices known to the kernel.
                  The listing is similar to the one seen during bootup.  scsi
                  currently supports only the add-single-device command which
                  allows root to add a hotplugged device to the list of known
                  devices.

                  The command

                      echo 'scsi add-single-device 1 0 5 0' > /proc/scsi/scsi

                  will cause host scsi1 to scan on SCSI channel 0 for a
                  device on ID 5 LUN 0.  If there is already a device known
                  on this address or the address is invalid, an error will be
                  returned.

           /proc/scsi/drivername/
                  drivername can currently be NCR53c7xx, aha152x, aha1542,
                  aha1740, aic7xxx, buslogic, eata_dma, eata_pio, fdomain,
                  in2000, pas16, qlogic, scsi_debug, seagate, t128, u15-24f,
                  ultrastore, or wd7000.  These directories show up for all
                  drivers that registered at least one SCSI HBA.  Every
                  directory contains one file per registered host.  Every
                  host-file is named after the number the host was assigned
                  during initialization.

                  Reading these files will usually show driver and host
                  configuration, statistics, and so on.

                  Writing to these files allows different things on different
                  hosts.  For example, with the latency and nolatency
                  commands, root can switch on and off command latency
                  measurement code in the eata_dma driver.  With the lockup
                  and unlock commands, root can control bus lockups simulated
                  by the scsi_debug driver.

## [](#SEE_ALSO)SEE ALSO

           proc(5)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08                   proc_scsi(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc(5)](../man5/proc.5.html)

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
