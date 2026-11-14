---
{"title": "lsusb(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lsusb.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lsusb(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [RETURN VALUE](#RETURN_VALUE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lsusb(8)                   Linux USB Utilities                   lsusb(8)

## [](#NAME)NAME

           lsusb - list USB devices

## [](#SYNOPSIS)SYNOPSIS

           lsusb [ options ]

## [](#DESCRIPTION)DESCRIPTION

           lsusb is a utility for displaying information about USB buses in
           the system and the devices connected to them. It uses udev's
           hardware database to associate a full human-readable name to the
           vendor ID and the product ID.

## [](#OPTIONS)OPTIONS

           -v, --verbose
                  Tells lsusb to be verbose and display detailed information
                  about the devices shown.  This includes configuration
                  descriptors for the device's current speed.  Class
                  descriptors will be shown, when available, for USB device
                  classes including hub, audio, HID, communications, and
                  chipcard. Can be used with the -t option.

           -s [[bus]:][devnum]
                  Show only devices in specified bus and/or devnum.  Both IDs
                  are given in decimal and may be omitted.

           -d [vendor]:[product]
                  Show only devices with the specified vendor and product ID.
                  Both IDs are given in hexadecimal.

           -D device
                  Do not scan the /dev/bus/usb directory, instead display
                  only information about the device whose device file is
                  given.  The device file should be something like
                  /dev/bus/usb/001/001.  This option displays detailed
                  information like the -v option; you must be root to do
                  this.

           -t, --tree
                  Tells lsusb to dump the physical USB device hierarchy as a
                  tree. Verbosity can be increased twice with the -v option.

           -V, --version
                  Print version information on standard output, then exit
                  successfully.

## [](#RETURN_VALUE)RETURN VALUE

           If the specified device is not found, a non-zero exit code is
           returned.

## [](#SEE_ALSO)SEE ALSO

           lspci(8), usbview(8).

## [](#AUTHOR)AUTHOR

           Thomas Sailer, <sailer@ife.ee.ethz.ch>.

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

    usbutils                     11 February 2019                    lsusb(8)

------------------------------------------------------------------------

Pages that refer to this page: [lsusb.py(1)](../man1/lsusb.py.1.html),  [usb-devices(1)](../man1/usb-devices.1.html),  [usbreset(1)](../man1/usbreset.1.html)

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
