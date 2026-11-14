---
{"title": "usbreset(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/usbreset.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# usbreset(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    usbreset(1)                Linux USB Utilities                usbreset(1)

## [](#NAME)NAME

           usbreset - send a USB port reset to a USB device

## [](#SYNOPSIS)SYNOPSIS

           usbreset [ device ]

## [](#DESCRIPTION)DESCRIPTION

           usbreset is a utility that performs resets on USB devices.  It is
           particularly useful for situations where a USB device is
           unresponsive or exhibits erratic behavior.  The USB device to be
           reset can be specified in one of three formats:

           VVVV:PPPP
                  Reset by vendor and product IDs

           BBB/DDD
                  Reset by bus and device number

           SN:SERIAL
                  Reset by serial number

           Product
                  Reset by product name

           When run without any arguments, usbreset provides usage
           information and a list of connected USB devices, including their
           vendor and product IDs, bus and device numbers, and product names.

## [](#RETURN_VALUE)RETURN VALUE

           If the specified device is not found, a non-zero exit code is
           returned.

## [](#EXAMPLES)EXAMPLES

           Reset device with vendor ID 1234 and product ID 5678:
                  usbreset 1234:5678

           Reset device 002 on bus 001:
                  usbreset 001/002

           Reset device with serial number ABCDEF0
                  usbreset SN:ABCDEF0

           Reset device named USB2.0 Hub:
                  usbreset "USB2.0 Hub"

## [](#SEE_ALSO)SEE ALSO

           lsusb(8).

## [](#AUTHOR)AUTHOR

           Alan Stern <stern@rowland.harvard.edu>

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

    usbutils                     04 January 2024                  usbreset(1)

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
