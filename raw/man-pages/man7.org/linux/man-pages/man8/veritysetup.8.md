---
{"title": "veritysetup(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/veritysetup.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# veritysetup(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [BASIC ACTIONS](#BASIC_ACTIONS) \| [OPTIONS](#OPTIONS) \| [RETURN CODES](#RETURN_CODES) \| [EXAMPLES](#EXAMPLES) \| [DM-VERITY ON-DISK SPECIFICATION](#DM-VERITY_ON-DISK_SPECIFICATION) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [CRYPTSETUP](#CRYPTSETUP) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    VERITYSETUP(8)             Maintenance Commands            VERITYSETUP(8)

## [](#NAME)NAME

           veritysetup - utility for configuring and managing dm-verity
           devices

## [](#SYNOPSIS)SYNOPSIS

           veritysetup <action> [<options>] <action args>

## [](#DESCRIPTION)DESCRIPTION

           Veritysetup is a utility for configuring and managing kernel
           dm-verity devices.

           Kernel device-mapper dm-verity target provides read-only
           transparent data integrity protection of block devices.

           When you configure the dm-verity device, veritysetup creates a new
           mapping that applications can access like any regular storage
           device. The kernel performs the verification transparently by
           comparing each block against pre-computed cryptographic hashes.
           The verification uses a Merkle tree and happens transparently at
           the kernel level without affecting applications.

           Verity devices can be activated during boot through veritytab(5),
           which is part of systemd(1).

## [](#BASIC_ACTIONS)BASIC ACTIONS

           Veritysetup supports these operations:

       FORMAT
           format <data_device> <hash_device>

           Calculates and permanently stores hash verification data for the
           data_device. Hash area can be located on the same device after
           data, if specified by --hash-offset option.

           You need to provide the root hash string for device verification
           or activation. Root hash must be trusted.

           The data or hash device argument can be a block device or a file
           image. If the hash device path doesn’t exist, it will be created
           as a file.

           <options> can be [--hash, --no-superblock, --format,
           --data-block-size, --hash-block-size, --data-blocks,
           --hash-offset, --salt, --uuid, --root-hash-file].

           If option --root-hash-file is used, the root hash is stored in
           hex-encoded text format in <path>.

       OPEN
           open <data_device> <name> <hash_device> <root_hash>
           open <data_device> <name> <hash_device> --root-hash-file <path>
           create <name> <data_device> <hash_device> <root_hash> (OBSOLETE
           syntax)

           Creates a mapping with <name> backed by device <data_device> and
           using <hash_device> for in-kernel verification.

           The <root_hash> is a hexadecimal string.

           <options> can be [--hash-offset, --no-superblock,
           --ignore-corruption or --restart-on-corruption,
           --panic-on-corruption, --ignore-zero-blocks, --check-at-most-once,
           --root-hash-signature, --root-hash-file, --use-tasklets,
           --shared].

           If option --root-hash-file is used, the root hash is read from
           <path> instead of the command line parameter. Expects hex-encoded
           text, without a terminating newline.

           If --no-superblock is used, you must use the same options as in
           the initial format operation.

       VERIFY
           verify <data_device> <hash_device> <root_hash>
           verify <data_device> <hash_device> --root-hash-file <path>

           Verifies data on data_device using hash blocks stored on
           hash_device.

           This command performs userspace verification; no kernel device is
           created.

           The <root_hash> is a hexadecimal string.

           If option --root-hash-file is used, the root hash is read from
           <path> instead of the command line parameter. Expects hex-encoded
           text, without a terminating newline.

           <options> can be [--hash-offset, --no-superblock,
           --root-hash-file].

           If --no-superblock is used, you must use the same options as in
           the initial format operation.

       CLOSE
           close <name>
           remove <name> (OBSOLETE syntax)

           Removes existing mapping <name>.

           <options> can be [--deferred] or [--cancel-deferred].

       STATUS
           status <name>

           Reports status for the active verity mapping <name>.

       DUMP
           dump <hash_device>

           Report parameters of the verity device from the on-disk stored
           superblock.

           <options> can be [--hash-offset].

## [](#OPTIONS)OPTIONS

           --batch-mode, -q
               Do not ask for confirmation.

           --cancel-deferred
               Cancels a previously configured deferred device removal in the
               close command.

           --check-at-most-once
               Instruct the kernel to verify blocks only once they are read
               from the data device, rather than every time.

               WARNING: It provides a reduced level of security because only
               offline tampering of the data device’s content will be
               detected, not online tampering.

           --data-blocks blocks
               Size of the data device used in verification. If not
               specified, the whole device is used.

           --data-block-size bytes
               Used block size for the data device. Maximum is the page size
               used by the kernel.

           --debug
               Run in debug mode with full diagnostic logs. Debug output
               lines are always prefixed by #.

           --deferred
               Defers device removal in the close command until the last user
               closes it.

           --error-as-corruption
               Handle device I/O errors the same as data corruption. This
               option must be combined with --restart-on-corruption or
               --panic-on-corruption.

           --fec-device device
               Use forward error correction (FEC) to recover from corruption
               if hash verification fails. Use encoding data from the
               specified device.

               The FEC device argument can be a block device or a file image.
               For format, if the FEC device path doesn’t exist, it will be
               created as a file.

               Block sizes for data and hash devices must match. Also, if the
               verity data_device is encrypted, the fec_device should be too.

               FEC calculation covers data, hash area, and optional foreign
               metadata stored on the same device as the hash tree
               (additional space after the hash area). The size of this
               optional additional area protected by FEC is calculated from
               image sizes, so you must use the same images for activation.

               If the hash device is in a separate image, metadata covers the
               entire image after the hash area.

               The metadata ends on the FEC area offset if the hash and FEC
               device are in the image.

           --fec-offset bytes
               This is the offset, in bytes, from the start of the FEC device
               to the beginning of the encoding data.

           --fec-roots number
               Number of generator roots. This equals the number of parity
               bytes in the encoding data. In RS(M, N) encoding, the number
               of roots is M-N. M is 255, and M-N is between 2 and 24
               (including).

           --format number
               Specifies the hash version type. Format type 0 is the original
               Chrome OS version. Format type 1 is the current version.

           --hash hash
               Hash algorithm for dm-verity. For default, see --help option.

           --hash-block-size bytes
               Used block size for the hash device. Maximum is the page size
               used by the kernel.

           --hash-offset bytes
               Offset of hash area/superblock on hash_device. Value must be
               aligned with the disk sector offset.

           --help, -?
               Show help text and default parameters.

           --ignore-corruption, --restart-on-corruption,
           --panic-on-corruption
               Defines what to do if a data integrity problem (data
               corruption) is detected.

               Without these options, the kernel fails the I/O operation with
               an I/O error. With --ignore-corruption option, the corruption
               is only logged. With --restart-on-corruption or
               --panic-on-corruption, the kernel is restarted (panicked)
               immediately. (You have to provide a way to avoid restart
               loops.)

               Use these options only for very specific cases.

           --ignore-zero-blocks
               Instruct the kernel not to verify blocks expected to contain
               zeroes and always directly return zeroes instead.

               Use this option only in very specific cases.

           --no-superblock
               Create or use dm-verity without a permanent on-disk
               superblock.

           --root-hash-file file*
               Path to file with stored root hash in hex-encoded text.

           --root-hash-signature file*
               A path to the root hash signature file used to verify the root
               hash (in kernel). This feature requires a Linux kernel version
               5.4 or more recent.

           --salt=hex string
               Salt used for formatting or verification. Format is a
               hexadecimal string.

           --shared
               Allows the data device to be used in shared mode. The data
               device is not checked for exclusive access before the device
               activation and may be mapped in multiple verity mappings.

           --usage
               Show short option help.

           --use-tasklets
               Try to use kernel tasklets in the dm-verity driver for
               performance reasons. This option is available since Linux
               kernel version 6.0.

           --uuid UUID
               Use the provided UUID for the format command instead of
               generating a new one.

               The UUID must be provided in standard UUID format, e.g.,
               12345678-1234-1234-1234-123456789abc.

           --verbose, -v
               Print more information on command execution.

           --version, -V
               Show the program version.

## [](#RETURN_CODES)RETURN CODES

           Veritysetup returns 0 on success and a non-zero value on error.

           Error codes are: 1 wrong parameters, 2 no permission, 3 out of
           memory, 4 wrong device specified, 5 device already exists or
           device is busy.

## [](#EXAMPLES)EXAMPLES

           veritysetup --data-blocks=256 format <data_device> <hash_device>

           Calculates and stores verification data on hash_device for the
           first 256 blocks (of block size). If hash_device does not exist,
           it is created (as a file image).

           veritysetup format --root-hash-file <path> <data_device>
           <hash_device>

           Calculates and stores verification data on hash_device for the
           whole data_device, and stores the root hash as hex-encoded text in
           <path>.

           veritysetup --data-blocks=256 --hash-offset=1052672 format
           <device> <device>

           Verification data (hashes) is stored on the same device as data
           (starting at hash-offset). Hash offset must be greater than the
           number of blocks in the data area.

           veritysetup --data-blocks=256 --hash-offset=1052672 create
           test-device <device> <device> <root_hash>

           Activates the verity device named test-device. Options
           --data-blocks and --hash-offset are the same as in the format
           command. The <root_hash> was calculated in the format command.

           veritysetup --data-blocks=256 --hash-offset=1052672 verify
           <data_device> <hash_device> <root_hash>

           Verifies device without activation (in userspace).

           veritysetup --data-blocks=256 --hash-offset=1052672
           --root-hash-file <path> verify <data_device> <hash_device>

           Verifies device without activation (in userspace). Root hash is
           passed via file rather than inline.

           veritysetup --fec-device=<fec_device> --fec-roots=10 format
           <data_device> <hash_device>

           Calculates and stores verification and encoding data for the
           data_device.

## [](#DM-VERITY_ON-DISK_SPECIFICATION)DM-VERITY ON-DISK SPECIFICATION

           The on-disk format specification is available on the DMVerity
           <https://gitlab.com/cryptsetup/cryptsetup/wikis/DMVerity> page.

## [](#AUTHORS)AUTHORS

           The first implementation of veritysetup was written by Chrome OS
           authors.

           This version is based on verification code written by Mikulas
           Patocka <mpatocka@redhat.com> and rewritten for libcryptsetup by
           Milan Broz <gmazyland@gmail.com>.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs at cryptsetup mailing list
           <cryptsetup@lists.linux.dev> or in Issues project section
           <https://gitlab.com/cryptsetup/cryptsetup/-/issues/new>.

           Please attach the output of the failed command with --debug option
           added.

## [](#SEE_ALSO)SEE ALSO

           Cryptsetup FAQ
           <https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions>

           cryptsetup(8), integritysetup(8) and veritysetup(8)

## [](#CRYPTSETUP)CRYPTSETUP

           Part of cryptsetup project
           <https://gitlab.com/cryptsetup/cryptsetup/>. This page is part of
           the Cryptsetup ((open-source disk encryption)) project.
           Information about the project can be found at 
           ⟨https://gitlab.com/cryptsetup/cryptsetup⟩. If you have a bug
           report for this manual page, send it to dm-crypt@saout.de. This
           page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/cryptsetup/cryptsetup.git⟩ on 2026-08-03. (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-21.) If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    veritysetup 2.9.0-git           2025-08-09                 VERITYSETUP(8)

------------------------------------------------------------------------

Pages that refer to this page: [veritytab(5)](../man5/veritytab.5.html),  [cryptsetup(8)](../man8/cryptsetup.8.html),  [cryptsetup-benchmark(8)](../man8/cryptsetup-benchmark.8.html),  [cryptsetup-bitlkDump(8)](../man8/cryptsetup-bitlkDump.8.html),  [cryptsetup-close(8)](../man8/cryptsetup-close.8.html),  [cryptsetup-config(8)](../man8/cryptsetup-config.8.html),  [cryptsetup-convert(8)](../man8/cryptsetup-convert.8.html),  [cryptsetup-erase(8)](../man8/cryptsetup-erase.8.html),  [cryptsetup-fvault2Dump(8)](../man8/cryptsetup-fvault2Dump.8.html),  [cryptsetup-isLuks(8)](../man8/cryptsetup-isLuks.8.html),  [cryptsetup-luksAddKey(8)](../man8/cryptsetup-luksAddKey.8.html),  [cryptsetup-luksChangeKey(8)](../man8/cryptsetup-luksChangeKey.8.html),  [cryptsetup-luksConvertKey(8)](../man8/cryptsetup-luksConvertKey.8.html),  [cryptsetup-luksDump(8)](../man8/cryptsetup-luksDump.8.html),  [cryptsetup-luksFormat(8)](../man8/cryptsetup-luksFormat.8.html),  [cryptsetup-luksHeaderBackup(8)](../man8/cryptsetup-luksHeaderBackup.8.html),  [cryptsetup-luksHeaderRestore(8)](../man8/cryptsetup-luksHeaderRestore.8.html),  [cryptsetup-luksKillSlot(8)](../man8/cryptsetup-luksKillSlot.8.html),  [cryptsetup-luksRemoveKey(8)](../man8/cryptsetup-luksRemoveKey.8.html),  [cryptsetup-luksResume(8)](../man8/cryptsetup-luksResume.8.html),  [cryptsetup-luksSuspend(8)](../man8/cryptsetup-luksSuspend.8.html),  [cryptsetup-luksUUID(8)](../man8/cryptsetup-luksUUID.8.html),  [cryptsetup-open(8)](../man8/cryptsetup-open.8.html),  [cryptsetup-reencrypt(8)](../man8/cryptsetup-reencrypt.8.html),  [cryptsetup-refresh(8)](../man8/cryptsetup-refresh.8.html),  [cryptsetup-repair(8)](../man8/cryptsetup-repair.8.html),  [cryptsetup-resize(8)](../man8/cryptsetup-resize.8.html),  [cryptsetup-ssh(8)](../man8/cryptsetup-ssh.8.html),  [cryptsetup-status(8)](../man8/cryptsetup-status.8.html),  [cryptsetup-tcryptDump(8)](../man8/cryptsetup-tcryptDump.8.html),  [cryptsetup-token(8)](../man8/cryptsetup-token.8.html),  [integritysetup(8)](../man8/integritysetup.8.html),  [systemd-veritysetup-generator(8)](../man8/systemd-veritysetup-generator.8.html),  [systemd-veritysetup@.service(8)](../man8/systemd-veritysetup@.service.8.html),  [veritysetup(8)](../man8/veritysetup.8.html)

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
