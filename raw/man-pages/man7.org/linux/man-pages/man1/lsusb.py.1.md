---
{"title": "lsusb.py(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lsusb.py.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lsusb.py(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lsusb.py(1)                Linux USB Utilities                lsusb.py(1)

## [](#NAME)NAME

           lsusb.py - list USB devices

## [](#SYNOPSIS)SYNOPSIS

           lsusb.py [ options ]

## [](#DESCRIPTION)DESCRIPTION

           lsusb.py is a utility for displaying information about USB buses
           in the system and the devices connected to them. It uses the
           usb.ids file to associate a human-readable name to the vendor and
           product IDs.

           In comparison with lsusb(8), this program can display additional
           information such as the interface speed of a device, and details
           of a device's interfaces including the driver bound to them and
           Linux devices provided by the driver, and the details of device
           and interface endpoints.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Displays options supported by lsusb(1).

           -i, --interfaces
                  Display information about the interfaces of each device,
                  excluding hubs.

           -I, --hub-interfaces
                  Display information about the interfaces of each device,
                  including hubs., excluding hubs.

           -u, --hide-empty-hubs
                  Suppress information about hubs that have no devices
                  connected.

           -U, --hide-hubs
                  Suppress information about hubs, even if they have devices
                  connected.

           -c, --color
                  Use color

           -C, --no-color
                  Don't use color

           -e, --endpoints
                  Include information about device (and interface, with -i)
                  endpoints.

           -f, --usbids-path
                  Overrides the path of the usb.ids file.

## [](#SEE_ALSO)SEE ALSO

           lspci(8), lsusb(8), usbview(8).

## [](#AUTHOR)AUTHOR

           Thomas Sailer, <sailer@ife.ee.ethz.ch>, Sam Morris
           <sam@robots.org.uk>.

## [](#COLOPHON)COLOPHON

           This page is part of the usbutils (USB utilities for Linux)
           project.  Information about the project can be found at 
           ⟨http://www.linux-usb.org/⟩.  If you have a bug report for this
           manual page, send it to linux-usb@vger.kernel.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/gregkh/usbutils.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-12.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    usbutils                     03 January 2024                  lsusb.py(1)

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
