---
{"title": "systemd-veritysetup-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-veritysetup-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-veritysetup-generator(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD...ENERATOR(8) systemd-veritysetup-generator SYSTEMD...ENERATOR(8)

## [](#NAME)NAME

           systemd-veritysetup-generator - Unit generator for verity
           protected block devices

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-veritysetup-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-veritysetup-generator is a generator that translates
           kernel command line options configuring verity protected block
           devices into native systemd units early at boot and when
           configuration of the system manager is reloaded. This will create
           systemd-veritysetup@.service(8) units as necessary.

           Currently, only two verity devices may be set up with this
           generator, backing the root and /usr file systems of the OS.

           systemd-veritysetup-generator implements systemd.generator(7).

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-veritysetup-generator understands the following kernel
           command line parameters:

           systemd.verity=, rd.systemd.verity=
               Takes a boolean argument. Defaults to "yes". If "no", disables
               the generator entirely.  rd.systemd.verity= is honored only in
               the initrd while systemd.verity= is honored by both the main
               system and in the initrd.

               Added in version 233.

           veritytab=, rd.veritytab=
               Takes a boolean argument. Defaults to "yes". If "no", causes
               the generator to ignore any devices configured in
               /etc/veritytab.  rd.veritytab= is honored only in the initrd
               while veritytab= is honored by both the main system and in the
               initrd.

               Added in version 248.

           roothash=
               Takes a root hash value for the root file system. Expects a
               hash value formatted in hexadecimal characters of the
               appropriate length (i.e. most likely 256 bit/64 characters, or
               longer). If not specified via systemd.verity_root_data= and
               systemd.verity_root_hash=, the hash and data devices to use
               are automatically derived from the specified hash value.
               Specifically, the data partition device is looked for under a
               GPT partition UUID derived from the first 128-bit of the root
               hash, the hash partition device is looked for under a GPT
               partition UUID derived from the last 128-bit of the root hash.
               Hence it is usually sufficient to specify the root hash to
               boot from a verity protected root file system, as device paths
               are automatically determined from it — as long as the
               partition table is properly set up.

               Added in version 233.

           systemd.verity_root_data=, systemd.verity_root_hash=
               These two settings take block device paths as arguments and
               may be used to explicitly configure the data partition and
               hash partition to use for setting up the verity protection for
               the root file system. If not specified, these paths are
               automatically derived from the roothash= argument (see above).

               Added in version 233.

           systemd.verity_root_options=
               Takes a comma-separated list of dm-verity options. Expects the
               following options superblock=BOOLEAN, format=NUMBER,
               data-block-size=BYTES, hash-block-size=BYTES,
               data-blocks=BLOCKS, hash-offset=BYTES, salt=HEX, uuid=UUID,
               ignore-corruption, restart-on-corruption, ignore-zero-blocks,
               check-at-most-once, panic-on-corruption, hash=HASH,
               fec-device=PATH, fec-offset=BYTES, fec-roots=NUM and
               root-hash-signature=PATH|base64:HEX. See veritysetup(8) for
               more details.

               Added in version 248.

           usrhash=, systemd.verity_usr_data=, systemd.verity_usr_hash=,
           systemd.verity_usr_options=
               Equivalent to their counterparts for the root file system as
               described above, but apply to the /usr/ file system instead.

               Added in version 250.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-veritysetup@.service(8), veritysetup(8),
           systemd-fstab-generator(8)

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

    systemd 262~devel                                   SYSTEMD...ENERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [veritytab(5)](../man5/veritytab.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-fstab-generator(8)](../man8/systemd-fstab-generator.8.html),  [systemd-veritysetup@.service(8)](../man8/systemd-veritysetup@.service.8.html)

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
