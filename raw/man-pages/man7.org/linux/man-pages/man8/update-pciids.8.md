---
{"title": "update-pciids(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/update-pciids.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# update-pciids(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    update-pciids(8)            The PCI Utilities            update-pciids(8)

## [](#NAME)NAME

           update-pciids - download new version of the PCI ID list

## [](#SYNOPSIS)SYNOPSIS

           update-pciids [-q]

## [](#DESCRIPTION)DESCRIPTION

           update-pciids fetches the current version of the pci.ids file from
           the primary distribution site and installs it.

           This utility requires curl, wget or lynx to be installed. If gzip
           or bzip2 are available, it automatically downloads the compressed
           version of the list.

## [](#OPTIONS)OPTIONS

           -q     Be quiet and do not report anything except errors.

## [](#FILES)FILES

           /usr/local/share/pci.ids.gz
                  Here we install the new list.

## [](#SEE_ALSO)SEE ALSO

           lspci(8), pci.ids(5), curl(1), wget(1), lynx(1), gzip(1), bzip2(1)

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

    pciutils-3.15.0                 2026-04-05               update-pciids(8)

------------------------------------------------------------------------

Pages that refer to this page: [pci.ids(5)](../man5/pci.ids.5.html),  [pcilib(7)](../man7/pcilib.7.html),  [lspci(8)](../man8/lspci.8.html)

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
