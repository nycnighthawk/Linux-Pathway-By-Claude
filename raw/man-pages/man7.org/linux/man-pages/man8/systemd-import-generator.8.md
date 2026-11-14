---
{"title": "systemd-import-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-import-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-import-generator(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [CREDENTIALS](#CREDENTIALS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-I...GENERATOR(8) systemd-import-generatorSYSTEMD-I...GENERATOR(8)

## [](#NAME)NAME

           systemd-import-generator - Generator for automatically downloading
           disk images at boot

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-import-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-import-generator may be used to automatically download
           disk images (tarballs or DDIs) via systemd-importd.service(8) at
           boot, based on parameters on the kernel command line or via system
           credentials. This is useful for automatically deploying an
           systemd-confext(8), systemd-sysext(8), systemd-nspawn(1)/
           systemd-vmspawn(1) or systemd-portabled.service(8) image at boot.
           This provides functionality equivalent to importctl(1), but
           accessible via the kernel command line and system credentials.

           systemd-import-generator implements systemd.generator(7).

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-import-generator understands the following
           kernel-command-line(7) parameters:

           systemd.pull=
               This option takes a colon separate triplet of option string,
               local target image name and remote URL. The local target image
               name can be specified as an empty string, in which case the
               name is derived from the specified remote URL. The remote URL
               must using the "http://", "https://", "file://" schemes. The
               option string itself is a comma separated list of options:

               rw, ro
                   Controls whether to mark the local image as read-only. If
                   not specified read-only defaults to off.

                   Added in version 257.

               verify=
                   Controls whether to cryptographically validate the
                   download before installing it in place. Takes one of "no",
                   "checksum", or "signature" (the default if not specified).
                   For details see the --verify= of importctl(1).

                   Added in version 257.

               sysext, confext, machine, portable
                   Controls the image class to download, and thus ultimately
                   the target directory for the image, depending on this
                   choice the target directory /var/lib/extensions/,
                   /var/lib/confexts/, /var/lib/machines/ or
                   /var/lib/portables/ is selected.

                   Specification of exactly one of these options is
                   mandatory.

                   Added in version 257.

               tar, raw
                   Controls the type of resource to download, i.e. a
                   (possibly compressed) tarball that needs to be unpacked
                   into a file system tree, or (possibly compressed) raw disk
                   image (DDI).

                   Specification of exactly one of these options is
                   mandatory.

                   Added in version 257.

               blockdev
                   If this option is specified the downloaded image is
                   attached to a loopback block device (via
                   systemd-loop@.service) after completion. This permits
                   booting from downloaded disk images. This is only
                   supported for "raw" disk images.

                   Note when this option is used with the purpose of mounting
                   a disk image conforming to the UAPI.3 Discoverable Disk
                   Image Specification[1] as root file system, and the
                   automatic GPT partition discovery logic as implemented by
                   systemd-gpt-auto-generator(8) shall process it, it's
                   essential to specify "rootdisk" as the local name for the
                   import. Moreover, "root=gpt-auto" must be specified on the
                   kernel command line explicitly. Also, prefix the
                   "systemd.pull=" command line option with "rd."  to ensure
                   it is executed in the initial RAM disk (initrd) already,
                   also see below.

                   Added in version 258.

               bootorigin
                   If this option is specified, in place of the URL a simple
                   filename may be specified. If the system is booted via
                   UEFI HTTP network booting the last component of the
                   network boot origin URL is replaced by this filename and
                   used as download source. This hence allows one to
                   automatically derive the URLs for disk images from the
                   original boot URL used to invoke the kernel or boot
                   loader.

                   If this option is used and the system is not actually
                   booted via UEFI HTTP network booting, the download is
                   gracefully skipped. Or in other words without other
                   modifications it is possible to put together an initrd
                   image that will boot from a local disk if available, or
                   from downloaded disk image if used via network booting.

                   Added in version 258.

               runtime=
                   Takes a boolean argument. If set to true, the image is
                   downloaded below the /run/ hierarchy, if set to false
                   below the /var/lib/ hierarchy. If not specified defaults
                   to true in the initial RAM disk (initrd) and to false on
                   the host system.

                   Added in version 258.

               Added in version 257.

           systemd.pull.success_action=, systemd.pull.failure_action=
               Controls whether to execute an action such as reboot,
               power-off and similar after completing the download
               successfully, or unsuccessfully. See
               SuccessAction=/FailureAction= on systemd.unit(5) for details
               about the available actions. If not specified, no action is
               taken, and the system will continue to boot normally.

               Added in version 257.

           These kernel command line options are interpreted by the host
           system only. If these options are prefixed with "rd."  they are
           interpreted by the initial RAM disk (initrd) instead.

## [](#CREDENTIALS)CREDENTIALS

           systemd-import-generator supports the system credentials logic.
           The following credentials are used when passed in:

           import.pull
               This credential should be a text file, with each line
               referencing one download operation. Each line should follow
               the same format as the value of the systemd.pull= kernel
               command line option described above.

               Added in version 257.

## [](#EXAMPLES)EXAMPLES

           Example 1. Download Configuration Extension

               systemd.pull=raw,confext::https://example.com/myconfext.raw.gz

           With a kernel command line option like the above a configuration
           extension DDI is downloaded automatically at boot from the
           specified URL, validated cryptographically, uncompressed and
           installed.

           Example 2. Download System Extension (Without Validation)

               systemd.pull=tar,sysext,verify=no::https://example.com/mysysext.tar.gz

           With a kernel command line option like the above a system
           extension tarball is downloaded automatically at boot from the
           specified URL, uncompressed and installed – without any
           cryptographic validation. This is useful for development purposes
           in virtual machines and containers. Warning: do not deploy a
           system with validation disabled like this!

           Example 3. Download root disk image (raw) into memory, for booting
           into it

               rd.systemd.pull=raw,machine,verify=no,blockdev:image:https://example.com/image.raw.xz root=/dev/disk/by-loop-ref/image.raw-part2

           This downloads the specified disk image, saving it locally under
           the name "image", and attaches it to a loopback block device on
           completion. It then boots from the 2nd partition in the image.

           Example 4. Boot into disk image (raw), with URL derived from UEFI
           HTTP network booting

               rd.systemd.pull=raw,machine,verify=no,blockdev,bootorigin:rootdisk:image.raw.xz root=gpt-auto

           This is similar to the previous example, but this time the source
           URL is automatically derived from the UEFI HTTP network boot URL.
           For example, if an UKI is booted from an URL
           "http://example.com/image.efi" this would result in a root disk
           being downloaded from "http://example.com/image.raw.xz". Moreover
           this uses the systemd-gpt-auto-generator(8) logic to mount the
           root file system from the disk image.

           Example 5. Boot into disk image (tar), with URL derived from UEFI
           HTTP network booting

               rd.systemd.pull=tar,machine,verify=no,bootorigin:root:image.tar.xz root=bind:/run/machines/root

           This is similar to the previous example, but instead of a raw
           (i.e. block device based) disk image the system boots into a
           tarball that is downloaded from the originating UEFI network
           server.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-importd.service(8), kernel-command-line(7),
           systemd.system-credentials(7), importctl(1),
           systemd-loop@.service(8), systemd-gpt-auto-generator(8)

## [](#NOTES)NOTES

            1. UAPI.3 Discoverable Disk Image Specification
               https://uapi-group.org/specifications/specs/discoverable_disk_image/

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

    systemd 262~devel                                SYSTEMD-I...GENERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-gpt-auto-generator(8)](../man8/systemd-gpt-auto-generator.8.html),  [systemd-loop@.service(8)](../man8/systemd-loop@.service.8.html)

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
