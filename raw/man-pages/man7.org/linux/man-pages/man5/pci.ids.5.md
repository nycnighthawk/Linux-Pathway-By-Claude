---
{"title": "pci.ids(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/pci.ids.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pci.ids(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [INTRODUCTION](#INTRODUCTION) \| [KEEPING THE LIST UP-TO-DATE](#KEEPING_THE_LIST_UP-TO-DATE) \| [FILE FORMAT](#FILE_FORMAT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    pci.ids(5)                  The PCI Utilities                  pci.ids(5)

## [](#NAME)NAME

           pci.ids - list of known identifiers related to PCI devices

## [](#INTRODUCTION)INTRODUCTION

           Devices on the PCI bus are identified by a combination of a vendor
           ID (assigned by the PCI SIG) and device ID (assigned by the
           vendor). Both IDs are 16-bit integers and the device itself
           provides no translation to a human-readable string.

           In addition to the vendor and device, devices also report several
           other identifiers:

           •  Device class and subclass (two 8-bit numbers)

           •  Programming interface (8-bit number, meaning specific for the
              subclass)

           •  Subsystem, which identifies the assembly in which the device is
              contained.  A typical example is an Ethernet add-in card: the
              device is the Ethernet controller chip, while the card plays
              the role of the subsystem. Subsystems have their vendor ID
              (from the same namespace as device vendors) and subsystem ID.
              Generally, the meaning of the subsystem ID depends on the
              device, but there are cases in which a single subsystem ID is
              used for many devices - e.g., laptop motherboards.

              The PCI utilities use the pci.ids file to translate all these
              numeric IDs to strings.

## [](#KEEPING_THE_LIST_UP-TO-DATE)KEEPING THE LIST UP-TO-DATE

           The pci.ids file is generated from the PCI ID database, which is
           maintained at https://pci-ids.ucw.cz/ ⟨https://pci-ids.ucw.cz/⟩.
           If you find any IDs missing from the list, please contribute them
           to the database.

           You can use the update-pciids command to download the current
           version of the list.

           Alternatively, you can use lspci -q to query the database online.

## [](#FILE_FORMAT)FILE FORMAT

           The pci.ids file is a text file in plain ASCII, interpreted line
           by line.  Lines starting with the hash sign are treated as
           comments are ignored.  Comments regarding a specific entry are
           written immediately before the entry.

           Vendor entries start with a 4-digit hexadecimal vendor ID,
           followed by one or more spaces, and the name of the vendor
           extending to the end of the line.

           Device entries are placed below the vendor entry. Each device
           entry consists of a single TAB character, a 4-digit hexadecimal
           device ID, followed by one or more spaces, and the name of the
           device extending to the end of the line.

           Subsystem entries are placed below the device entry. They start
           with two TAB characters, a 4-digit hexadecimal vendor ID (which
           must be defined elsewhere in the list), a single space, a 4-digit
           hexadecimal subsystem ID, one or more spaces, and the name of the
           subsystem extending to the end of the line.

           Class entries consist of "C", one space, 2-digit hexadecimal class
           ID, one or more spaces, and the name of the class. Subclasses are
           placed below the corresponding class, indented by a single TAB,
           followed by a 2-digit hexadecimal subclass ID, one or more spaces,
           and the name of the subclass.  Programming interfaces are below
           the subclass, indented by two TABs, followed by a 2-digit
           hexadecimal prog-if ID, one or more spaces, and the name.

           There can be device-independent subsystem IDs, although the web
           interface of the database does not support them yet. They start
           with a subsystem vendor line consisting of "S", one space, and a
           4-digit hexadecimal vendor ID (which must correspond to an already
           listed vendor). Subsystems follow on subsequent lines, each
           indented by one TAB, followed by a 4-digit hexadecimal subsystem
           ID, one or more spaces, and the name of the subsystem.

           To ensure extensibility of the format, lines starting with an
           unrecognized letter followed by a single space are ignored and so
           are all following TAB-indented lines.

## [](#FILES)FILES

           /usr/local/share/pci.ids.gz
                  Location of the list.

## [](#SEE_ALSO)SEE ALSO

           lspci(8), update-pciids(8), pcilib(7)

## [](#AUTHOR)AUTHOR

           The PCI Utilities are maintained by Martin Mares <mj@ucw.cz>.

## [](#COLOPHON)COLOPHON

           This page is part of the pciutils (PCI utilities) project.
           Information about the project can be found at 
           ⟨http://mj.ucw.cz/sw/pciutils/⟩.  If you have a bug report for this
           manual page, send it to linux-pci@vger.kernel.org.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/pciutils/pciutils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-08.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    pciutils-3.15.0                 2026-04-05                     pci.ids(5)

------------------------------------------------------------------------

Pages that refer to this page: [pcilib(7)](../man7/pcilib.7.html),  [lspci(8)](../man8/lspci.8.html),  [update-pciids(8)](../man8/update-pciids.8.html)

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
