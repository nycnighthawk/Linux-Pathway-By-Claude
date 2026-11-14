---
{"title": "integritytab(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/integritytab.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# integritytab(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    INTEGRITYTAB(5)                integritytab               INTEGRITYTAB(5)

## [](#NAME)NAME

           integritytab - Configuration for integrity block devices

## [](#SYNOPSIS)SYNOPSIS

           /etc/integritytab

## [](#DESCRIPTION)DESCRIPTION

           The /etc/integritytab file describes integrity protected block
           devices that are set up during system boot.

           Empty lines and lines starting with the "#" character are ignored.
           Each of the remaining lines describes one verity integrity
           protected block device. Fields are delimited by white space.

           Each line is in the form

               volume-name block-device
                   [keyfile|-] [options|-]

           The first two fields are mandatory, the remaining two are optional
           and only required if user specified non-default options during
           integrity format.

           The first field contains the name of the resulting integrity
           volume; its block device is set up below /dev/mapper/.

           The second field contains a path to the underlying block device,
           or a specification of a block device via "UUID=" followed by the
           UUID, "PARTUUID=" followed by the partition UUID, "LABEL="
           followed by the label, "PARTLABEL=" followed by the partition
           label.

           The third field if present contains an absolute filename path to a
           key file or a "-" to specify none. When the filename is present,
           the "integrity-algorithm" defaults to "hmac-sha256" with the key
           length derived from the number of bytes in the key file. At this
           time the only supported integrity algorithms when using key file
           are hmac-sha256, hmac-sha512, phmac-sha256, and hmac-sha512. The
           maximum size of the key file is 4096 bytes.

           The fourth field, if present, is a comma-delimited list of options
           or a "-" to specify none. The following options are recognized:

           allow-discards
               Allow the use of discard (TRIM) requests for the device. This
               option is available since the Linux kernel version 5.7.

               Added in version 250.

           mode=(journal|bitmap|direct)
               Enable journaled, bitmapped or direct (passthrough) mode.
               Journaled mode is the default when this option is not
               specified. It provides safety against crashes, but can be slow
               because all data has to be written twice. Bitmap mode is more
               efficient since it requires only a single write, but it is
               less reliable because if data corruption happens when the
               machine crashes, it might not be detected. Direct mode
               disables the journal and the bitmap. Corresponds to the
               "direct writes" mode documented in the dm-integrity
               documentation[1]. Note that without a journal, if there is a
               crash, it is possible that the integrity tags and data will
               not match. If used, the journal-* options below will have no
               effect if passed.

               Added in version 254.

           journal-watermark=[0..100]%
               Journal watermark in percent. When the journal percentage
               exceeds this watermark, the journal flush will be started.
               Setting a value of "0%" uses default value.

               Added in version 250.

           journal-commit-time=[0..N]
               Commit time in milliseconds. When this time passes (and no
               explicit flush operation was issued), the journal is written.
               Setting a value of zero uses default value.

               Added in version 250.

           data-device=/dev/disk/by-...
               Specify a separate block device that contains existing data.
               The second field specified in the integritytab for block
               device then will contain calculated integrity tags and journal
               for data-device, but not the end user data.

               Added in version 250.

           integrity-algorithm=[crc32c|crc32|xxhash64|sha1|sha256|hmac-sha256|hmac-sha512|phmac-sha256|phmac-sha512]
               The algorithm used for integrity checking. The default is
               crc32c. Must match option used during format.

               Added in version 250.

           _netdev
               Marks this veritysetup device as requiring network. It will be
               started after the network is available, similarly to
               systemd.mount(5) units marked with _netdev. The service unit
               to set up this device will be ordered between
               remote-fs-pre.target and remote-integritysetup.target, instead
               of integritysetup-pre.target and integritysetup.target.

               Hint: if this device is used for a mount point that is
               specified in fstab(5), the _netdev option should also be used
               for the mount point. Otherwise, a dependency loop might be
               created where the mount point will be pulled in by
               local-fs.target, while the service to configure the network is
               usually only started after the local file system has been
               mounted.

               Added in version 258.

           noauto
               This device will not be added to integritysetup.target. This
               means that it will not be automatically enabled on boot,
               unless something else pulls it in. In particular, if the
               device is used for a mount point, it'll be enabled
               automatically during boot, unless the mount point itself is
               also disabled with noauto.

               Added in version 258.

           nofail
               This device will not be a hard dependency of
               integritysetup.target. It'll still be pulled in and started,
               but the system will not wait for the device to show up and be
               enabled, and boot will not fail if this is unsuccessful. Note
               that other units that depend on the enabled device may still
               fail. In particular, if the device is used for a mount point,
               the mount point itself also needs to have the nofail option,
               or the boot will fail if the device is not enabled
               successfully.

               Added in version 258.

           At early boot and when the system manager configuration is
           reloaded, this file is translated into native systemd units by
           systemd-integritysetup-generator(8).

## [](#EXAMPLES)EXAMPLES

           Example 1. /etc/integritytab

           Set up two integrity protected block devices.

               home PARTUUID=4973d0b8-1b15-c449-96ec-94bab7f6a7b8 - journal-commit-time=10,allow-discards,journal-watermark=55%
               data PARTUUID=5d4b1808-be76-774d-88af-03c4c3a41761 - allow-discards

           Example 2. /etc/integritytab

           Set up 1 integrity protected block device using defaults

               home PARTUUID=4973d0b8-1b15-c449-96ec-94bab7f6a7b8

           Example 3. /etc/integritytab

           Set up 1 integrity device using existing data block device which
           contains user data

               home PARTUUID=4973d0b8-1b15-c449-96ec-94bab7f6a7b8 - data-device=/dev/disk/by-uuid/9276d9c0-d4e3-4297-b4ff-3307cd0d092f

           Example 4. /etc/integritytab

           Set up 1 integrity device using a HMAC key file using defaults

               home PARTUUID=4973d0b8-1b15-c449-96ec-94bab7f6a7b8 /etc/hmac.key

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-integritysetup@.service(8),
           systemd-integritysetup-generator(8), integritysetup(8)

## [](#NOTES)NOTES

            1. the dm-integrity documentation
               https://docs.kernel.org/admin-guide/device-mapper/dm-integrity.html

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

    systemd 262~devel                                         INTEGRITYTAB(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [integritysetup(8)](../man8/integritysetup.8.html),  [systemd-integritysetup@.service(8)](../man8/systemd-integritysetup@.service.8.html)

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
