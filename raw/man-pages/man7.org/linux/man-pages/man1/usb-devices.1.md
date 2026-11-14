---
{"title": "usb-devices(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/usb-devices.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# usb-devices(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    usb-devices(1)             Linux USB Utilities             usb-devices(1)

## [](#NAME)NAME

           usb-devices - print USB device details

## [](#SYNOPSIS)SYNOPSIS

           usb-devices

## [](#DESCRIPTION)DESCRIPTION

           usb-devices is a shell script that can be used to display details
           of USB buses in the system and the devices connected to them.

           The output of the script is similar to the usb/devices file
           available either under /proc/bus (if usbfs is mounted), or under
           /sys/kernel/debug (if debugfs is mounted there). The script is
           primarily intended to be used if the file is not available.

           In contrast to the usb/devices file, this script only lists active
           interfaces (those marked with a "*" in the usb/devices file) and
           their endpoints.

           Be advised that there can be differences in the way information is
           sorted, as well as in the format of the output.

## [](#RETURN_VALUE)RETURN VALUE

           If sysfs is not mounted, a non-zero exit code is returned.

## [](#FILES)FILES

           /sys/bus/usb/devices/usb*
                  The part of the sysfs tree the script walks through to
                  assemble the printed information.

           /proc/bus/usb/devices
                  Location where the usb/devices file can normally be found
                  for Linux kernels before 2.6.31, if usbfs is mounted.

           /sys/kernel/debug/usb/devices
                  Location where the usb/devices file can normally be found
                  for Linux kernel 2.6.31 and later, if debugfs is mounted.

## [](#SEE_ALSO)SEE ALSO

           lsusb(8), usbview(8).

## [](#AUTHORS)AUTHORS

           Greg Kroah-Hartman <greg@kroah.com>

           Randy Dunlap <rdunlap@xenotime.net>

           Frans Pop <elendil@planet.nl>

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

    usbutils                       23 June 2009                usb-devices(1)

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
