---
{"title": "cryptsetup-refresh(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cryptsetup-refresh.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cryptsetup-refresh(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [CRYPTSETUP](#CRYPTSETUP) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CRYPTSETUP-REFRESH(8)      Maintenance Commands     CRYPTSETUP-REFRESH(8)

## [](#NAME)NAME

           cryptsetup-refresh - refresh parameters of an active mapping

## [](#SYNOPSIS)SYNOPSIS

           cryptsetup refresh [<options>] <name>

## [](#DESCRIPTION)DESCRIPTION

           Refreshes parameters of active mapping <name>.

           Update parameters of active device <name> without the need to
           deactivate the device (and unmount the filesystem). Currently, it
           supports parameter refresh on the following devices: LUKS1, LUKS2
           (including authenticated encryption), plain crypt and loop-AES.

           Mandatory parameters are identical to those of an open action for
           the respective device type.

           You may change the following parameters on all devices
           --perf-same_cpu_crypt, --perf-submit_from_crypt_cpus,
           --perf-no_read_workqueue, --perf-no_write_workqueue and
           --allow-discards.

           Refreshing the device without any optional parameter will refresh
           the device with the default setting (respective to device type).

           LUKS2 only:

           The --integrity-no-journal parameter affects only LUKS2 devices
           with the underlying dm-integrity device.

           Adding option --persistent stores any combination of device
           parameters above in LUKS2 metadata (only after successful refresh
           operation).

           The --disable-keyring parameter refreshes a device with the volume
           key passed in the dm-crypt driver.

           <options> can be [--allow-discards, --perf-same_cpu_crypt,
           --perf-submit_from_crypt_cpus, --perf-no_read_workqueue,
           --perf-no_write_workqueue, --header, --disable-keyring,
           --disable-locks, --persistent, --integrity-no-journal].

## [](#OPTIONS)OPTIONS

           --allow-discards
               Allow the use of discard (TRIM) requests for the device. This
               is also not supported for LUKS2 devices with data integrity
               protection.

               WARNING: This command can have a negative security impact
               because it can make filesystem-level operations visible on the
               physical device. For example, information leaking filesystem
               type, used space, etc., may be extractable from the physical
               device if the discarded blocks can be located later. If in
               doubt, do not use it.

               A kernel version of 3.1 or later is needed. For earlier
               kernels, this option is ignored.

           --batch-mode, -q
               Suppresses all confirmation questions. Use with care!

               If the --verify-passphrase option is not specified, this
               option also switches off the passphrase verification.

           --debug or --debug-json
               Run in debug mode with full diagnostic logs. Debug output
               lines are always prefixed by #.

               If --debug-json is used, additional LUKS2 JSON data structures
               are printed.

           --disable-keyring
               Do not load the volume key in the kernel keyring; store it
               directly in the dm-crypt target instead. This option is
               supported only for the LUKS2 type.

           --disable-locks
               Disable lock protection for metadata on disk. This option is
               valid only for LUKS2 and is ignored for other formats.

               WARNING: Do not use this option unless you run cryptsetup in a
               restricted environment where locking is impossible to perform
               (where /run directory cannot be used).

           --header <device or file storing the LUKS header>
               Use a detached (separated) metadata device or file where the
               LUKS header is stored. This option allows one to store the
               ciphertext and LUKS header on different devices.

               For commands that change the LUKS header (e.g., luksAddKey),
               specify the device or file with the LUKS header directly as
               the LUKS device.

           --help, -?
               Show help text and default parameters.

           --integrity-no-journal
               Activate device with integrity protection without using data
               journal (direct write of data and integrity tags). Note that
               without a journal, a power failure can cause non-atomic writes
               and data corruption. Use only if journaling is performed on a
               different storage layer.

           --perf-high_priority
               Set dm-crypt workqueues and the writer thread to high
               priority. This improves throughput and latency of dm-crypt
               while degrading the general responsiveness of the system.

               This option is available only for low-level dm-crypt
               performance tuning, use only if you need a change to the
               default dm-crypt behaviour. Needs kernel 6.10 or later.

           --perf-no_read_workqueue, --perf-no_write_workqueue
               Bypass dm-crypt internal workqueue and process read or write
               requests synchronously.

               These options are available only for low-level dm-crypt
               performance tuning, use only if you need a change to the
               default dm-crypt behaviour. Needs kernel 5.9 or later.

           --perf-same_cpu_crypt
               Perform encryption using the same CPU on which that IO was
               submitted. The default is to use an unbound workqueue so that
               encryption work is automatically balanced between available
               CPUs.

               This option is available only for low-level dm-crypt
               performance tuning, use only if you need a change to the
               default dm-crypt behaviour.

           --perf-submit_from_crypt_cpus
               Disable offloading writes to a separate thread after
               encryption. There are some situations where offloading write
               bios from the encryption threads to a single thread degrades
               performance significantly. The default is to offload write
               bios to the same thread.

               This option is available only for low-level dm-crypt
               performance tuning, use only if you need a change to the
               default dm-crypt behaviour.

           --persistent
               If used with LUKS2 devices and activation commands like open
               or refresh, the specified activation flags are persistently
               written into metadata and used next time automatically, even
               for normal activation. (No need to use cryptab or other system
               configuration files.)

               If you need to remove a persistent flag, use --persistent
               without the flag you want to remove (e.g., to disable the
               persistently stored discard flag, use --persistent without
               --allow-discards).

               Only --allow-discards, --perf-same_cpu_crypt,
               --perf-submit_from_crypt_cpus, --perf-no_read_workqueue,
               --perf-no_write_workqueue and --integrity-no-journal can be
               stored persistently.

           --usage
               Show short option help.

           --version, -V
               Show the program version.

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

    cryptsetup 2.9.0-git            2025-08-09          CRYPTSETUP-REFRESH(8)

------------------------------------------------------------------------

Pages that refer to this page: [cryptsetup(8)](../man8/cryptsetup.8.html),  [cryptsetup-open(8)](../man8/cryptsetup-open.8.html)

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
