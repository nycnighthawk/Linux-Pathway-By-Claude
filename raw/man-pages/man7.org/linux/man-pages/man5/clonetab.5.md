---
{"title": "clonetab(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/clonetab.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# clonetab(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CLONETAB(5)                      clonetab                     CLONETAB(5)

## [](#NAME)NAME

           clonetab - Configuration for dm-clone block devices

## [](#SYNOPSIS)SYNOPSIS

           /etc/clonetab

## [](#DESCRIPTION)DESCRIPTION

           The /etc/clonetab file describes dm-clone block devices that are
           set up during system boot.

           Empty lines and lines starting with the "#" character are ignored.
           Each of the remaining lines describes one dm-clone device. Fields
           are delimited by white space.

           Each line is in the form

               name source-device destination-device metadata-device [options]

           The first four fields are mandatory, the fifth is optional.

           The five fields of /etc/clonetab are defined as follows:

            1. The first field contains the name of the resulting dm-clone
               device; its block device is set up below /dev/mapper/.

            2. The second field contains a path to the read-only source block
               device. This is the device whose data is cloned to the
               destination device. Reads to regions not yet hydrated are
               served directly from this device.

            3. The third field contains a path to the writable destination
               block device. The source device's data is copied here in the
               background. It must be at least as large as the source device.

            4. The fourth field contains a path to the metadata block device.
               This small device tracks which regions of the destination have
               been hydrated and is managed exclusively by dm-clone.

            5. The fifth field, if present, contains comma-separated
               "key=value" options. The following option is supported:

               region-size=BYTES
                   Controls the granularity of background hydration copying —
                   how much data is copied at a time. Region size is
                   specified in bytes (standard suffixes like "K", "M", "G"
                   are supported), and must correspond to a power of two
                   between 4 KiB and 1 GiB. For example, "region-size=4K" or
                   "region-size=4096" sets a 4 KiB region size.

                   One region is the atomic unit dm-clone tracks: it is
                   either fully hydrated (copied to the destination) or not,
                   never partially. If a copy is interrupted mid-region, that
                   whole region is retried from scratch on next boot. Smaller
                   regions mean finer progress tracking; larger regions
                   reduce metadata overhead. Defaults to "4K". For
                   background, see dm-clone kernel documentation[1].

                   Added in version 262.

               If no options are needed, the field may be omitted entirely or
               "-" may be used as a placeholder.

           At early boot and when the system manager configuration is
           reloaded, this file is translated into native systemd units by
           systemd-clonesetup-generator(8).

## [](#EXAMPLES)EXAMPLES

           Example 1. Simple clone without options

           Clone a source device to a destination, using a separate metadata
           device:

               mydevice /dev/sdb /dev/sdc /dev/sdd

           Example 2. Clone with custom region size

           Clone a source device to a destination with a custom region size
           of 8 KiB:

               mydevice /dev/sdb /dev/sdc /dev/sdd region-size=8K

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-clonesetup-generator(8), dmsetup(8)

## [](#NOTES)NOTES

            1. dm-clone kernel documentation
               https://www.kernel.org/doc/html/latest/admin-guide/device-mapper/dm-clone.html

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                             CLONETAB(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-clonesetup(8)](../man8/systemd-clonesetup.8.html),  [systemd-clonesetup-generator(8)](../man8/systemd-clonesetup-generator.8.html)

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
