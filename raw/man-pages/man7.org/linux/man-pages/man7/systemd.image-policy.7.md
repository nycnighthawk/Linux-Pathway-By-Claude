---
{"title": "systemd.image-policy(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/systemd.image-policy.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.image-policy(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SPECIAL POLICIES](#SPECIAL_POLICIES) \| [USE](#USE) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD.IMAGE-POLICY(7)    systemd.image-policy   SYSTEMD.IMAGE-POLICY(7)

## [](#NAME)NAME

           systemd.image-policy - Disk Image Dissection Policy

## [](#DESCRIPTION)DESCRIPTION

           In systemd, whenever a disk image (DDI) implementing the UAPI.2
           Discoverable Partitions Specification[1] is activated, a policy
           may be specified controlling which partitions to mount and what
           kind of cryptographic protection to require, and which type of
           filesystem is allowed. Such a disk image dissection policy is a
           string that contains per-partition-type rules, separated by colons
           (":"). The individual rules consist of a partition identifier, an
           equal sign ("="), and one or more flags which may be set per
           partition. If multiple flags are specified per partition they are
           separated by a plus sign ("+").

           The partition identifiers currently defined are: root, usr, home,
           srv, esp, xbootldr, swap, root-verity, root-verity-sig,
           usr-verity, usr-verity-sig, tmp, var. These identifiers match the
           relevant partition types in the Discoverable Partitions
           Specification, but are agnostic to CPU architectures. If the
           partition identifier is left empty it defines the default policy
           for partitions defined in the Discoverable Partitions
           Specification for which no policy flags are explicitly listed in
           the policy string.

           The following partition policy flags are defined that dictate the
           existence/absence, the use, and the protection level of
           partitions:

           •   unprotected for partitions that shall exist and be used, but
               shall come without cryptographic protection, lacking both
               Verity authentication and LUKS encryption.

           •   verity for partitions that shall exist and be used, with
               Verity authentication. (Note: if a DDI image carries a data
               partition, along with a Verity partition and a signature
               partition for it, and only the verity flag is set (signed is
               not), then the image will be set up with Verity, but the
               signature data will not be used. Or in other words: any DDI
               with a set of partitions that qualify for signature also
               implicitly qualifies for verity, and in fact also
               unprotected).

           •   signed for partitions that shall exist and be used, with
               Verity authentication, which are also accompanied by a PKCS#7
               signature of the Verity root hash.

           •   encrypted for partitions which shall exist and be used and are
               encrypted with LUKS.

           •   unused for partitions that shall exist but shall not be used.

           •   absent for partitions that shall not exist on the image.

           The following filesystem policy flags are defined that dictate
           which filesystem types are allowed for which partition:

           Table 1.  Filesystems types supported by the policy
           ┌─────────────────┐
           │ Filesystem flag │
           ├─────────────────┤
           │ "btrfs"         │
           ├─────────────────┤
           │ "erofs"         │
           ├─────────────────┤
           │ "ext4"          │
           ├─────────────────┤
           │ "f2fs"          │
           ├─────────────────┤
           │ "squashfs"      │
           ├─────────────────┤
           │ "vfat"          │
           ├─────────────────┤
           │ "xfs"           │
           └─────────────────┘

           By setting a combination of the flags above, alternatives can be
           declared. For example the combination "unused+absent" means: the
           partition may exist (in which case it shall not be used) or may be
           absent. The combination of
           "unprotected+verity+signed+encrypted+unused+absent" may be
           specified via the special shortcut "open", and indicates that the
           partition may exist or may be absent, but if it exists is used,
           regardless of the protection level.

           As special rule: if none of the flags above are set for a listed
           partition identifier, the default policy of open is implied, i.e.
           setting none of these flags listed above means effectively all
           flags listed above will be set.

           The following partition policy flags are defined that dictate the
           state of specific GPT partition flags:

           •   read-only-off, read-only-on to require that the partitions
               have the read-only partition flag off or on.

           •   growfs-off, growfs-on to require that the partitions have the
               growfs partition flag off or on.

           If both read-only-off and read-only-on are set for a partition,
           then the state of the read-only flag on the partition is not
           dictated by the policy. Setting neither flag is equivalent to
           setting both, i.e. setting neither of these two flags means
           effectively both will be set. A similar logic applies to
           growfs-off/growfs-on.

           If partitions are not listed within an image policy string, the
           default policy flags are applied (configurable via an empty
           partition identifier, see above). If no default policy flags are
           configured in the policy string, it is implied to be
           "absent+unused", except for the Verity partition and their
           signature partitions where the policy is automatically derived
           from minimal protection level of the data partition they protect,
           as encoded in the policy.

## [](#SPECIAL_POLICIES)SPECIAL POLICIES

           The special image policy string "*" is short for "use everything",
           i.e. is equivalent to:

               =verity+signed+encrypted+unprotected+unused+absent

           The special image policy string "-" is short for "use nothing",
           i.e. is equivalent to:

               =unused+absent

           The special image policy string "~" is short for "everything must
           be absent", i.e. is equivalent to:

               =absent

## [](#USE)USE

           Most systemd components that support operating with disk images
           support a --image-policy= command line option to specify the image
           policy to use, and default to relatively open policies (typically
           the "*" policy, as described above), under the assumption that
           trust in disk images is established before the images are passed
           to the program in question.

           For the host image itself systemd-gpt-auto-generator(8) is
           responsible for processing the GPT partition table and making use
           of the included discoverable partitions. It accepts an image
           policy via the kernel command line option systemd.image_policy=.

           Note that image policies do not dictate how the components will
           mount and use disk images — they only dictate which parts to avoid
           and which protection level and arrangement to require while
           mounting/using them. For example, systemd-sysext(8) only cares for
           the /usr/ and /opt/ trees inside a disk image, and thus ignores
           any /home/ partitions (and similar) in all cases, which might be
           included in the image, regardless whether the configured image
           policy would allow access to it or not. Similar, systemd-nspawn(1)
           is not going to make use of any discovered swap device, regardless
           of whether the policy would allow that or not.

           Use the image-policy command of the systemd-analyze(1) tool to
           analyze image policy strings, and determine what a specific policy
           string means for a specific partition.

## [](#EXAMPLES)EXAMPLES

           The following image policy string dictates one read-only
           Verity-enabled /usr/ partition must exist, plus encrypted root and
           swap partitions. All other partitions are ignored:

               usr=verity+read-only-on:root=encrypted:swap=encrypted

           The following image policy string dictates an encrypted, writable
           root file system, and optional /srv/ file system that must be
           encrypted if it exists and no swap partition may exist:

               root=encrypted+read-only-off:srv=encrypted+absent:swap=absent

           The following image policy string dictates a single root partition
           that may be encrypted, but does not have to be, and ignores swap
           partitions, and uses all other partitions if they are available,
           possibly with encryption.

               root=unprotected+encrypted:swap=absent+unused:=unprotected+encrypted+absent

           The following image policy string dictates a single root partition
           that can only be erofs or squashfs, and ignores swap partitions,
           and uses all other partitions if they are available, possibly with
           encryption.

               root=erofs+squashfs:swap=absent+unused:=unprotected+encrypted+absent

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-dissect(1), systemd-gpt-auto-generator(8),
           systemd-sysext(8), systemd-analyze(1)

## [](#NOTES)NOTES

            1. UAPI.2 Discoverable Partitions Specification
               https://uapi-group.org/specifications/specs/discoverable_partitions_specification

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

    systemd 262~devel                                 SYSTEMD.IMAGE-POLICY(7)

------------------------------------------------------------------------

Pages that refer to this page: [bootctl(1)](../man1/bootctl.1.html),  [coredumpctl(1)](../man1/coredumpctl.1.html),  [journalctl(1)](../man1/journalctl.1.html),  [portablectl(1)](../man1/portablectl.1.html),  [systemctl(1)](../man1/systemctl.1.html),  [systemd-analyze(1)](../man1/systemd-analyze.1.html),  [systemd-dissect(1)](../man1/systemd-dissect.1.html),  [systemd-machine-id-setup(1)](../man1/systemd-machine-id-setup.1.html),  [systemd-mstack(1)](../man1/systemd-mstack.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [sysext.conf(5)](../man5/sysext.conf.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.image-filter(7)](../man7/systemd.image-filter.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [kernel-install(8)](../man8/kernel-install.8.html),  [systemd-gpt-auto-generator(8)](../man8/systemd-gpt-auto-generator.8.html),  [systemd-repart(8)](../man8/systemd-repart.8.html),  [systemd-sysext(8)](../man8/systemd-sysext.8.html),  [systemd-sysupdate(8)](../man8/systemd-sysupdate.8.html),  [systemd-sysusers(8)](../man8/systemd-sysusers.8.html),  [systemd-tmpfiles(8)](../man8/systemd-tmpfiles.8.html)

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
