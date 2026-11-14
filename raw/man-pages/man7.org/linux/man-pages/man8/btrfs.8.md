---
{"title": "btrfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/btrfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# btrfs(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMAND SYNTAX](#COMMAND_SYNTAX) \| [COMMANDS](#COMMANDS) \| [STANDALONE TOOLS](#STANDALONE_TOOLS) \| [EXIT STATUS](#EXIT_STATUS) \| [AVAILABILITY](#AVAILABILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BTRFS(8)                       Btrfs Manual                      BTRFS(8)

## [](#NAME)NAME

           btrfs - a toolbox to manage btrfs filesystems

## [](#SYNOPSIS)SYNOPSIS

           btrfs <command> [<args>]

## [](#DESCRIPTION)DESCRIPTION

           The btrfs utility is a toolbox for managing btrfs filesystems.
           There are command groups to work with subvolumes, devices, for
           whole filesystem or other specific actions. See section COMMANDS.

           There are also standalone tools for some tasks like btrfs-convert
           or btrfstune that were separate historically and/or haven’t been
           merged to the main utility. See section STANDALONE TOOLS for more
           details.

           For other topics (mount options, etc) please refer to the separate
           manual page btrfs(5).

## [](#COMMAND_SYNTAX)COMMAND SYNTAX

           Any command name can be shortened so long as the shortened form is
           unambiguous, however, it is recommended to use full command names
           in scripts. All command groups have their manual page named
           btrfs-<group>.

           For example: it is possible to run btrfs sub snaps instead of
           btrfs subvolume snapshot. But btrfs file s is not allowed, because
           file s may be interpreted both as filesystem show and as
           filesystem sync.

           If the command name is ambiguous, the list of conflicting options
           is printed.

           For an overview of a given command use btrfs command --help or
           btrfs [command...] --help --full to print all available options.

## [](#COMMANDS)COMMANDS

           balance
               Balance btrfs filesystem chunks across single or several
               devices.

               See btrfs-balance(8) for details.

           check
               Do off-line check on a btrfs filesystem.

               See btrfs-check(8) for details.

           device
               Manage devices managed by btrfs, including add/delete/scan and
               so on.

               See btrfs-device(8) for details.

           filesystem
               Manage a btrfs filesystem, including label setting/sync and so
               on.

               See btrfs-filesystem(8) for details.

           inspect-internal
               Debug tools for developers/hackers.

               See btrfs-inspect-internal(8) for details.

           property
               Get/set a property from/to a btrfs object.

               See btrfs-property(8) for details.

           qgroup
               Manage quota group(qgroup) for btrfs filesystem.

               See btrfs-qgroup(8) for details.

           quota
               Manage quota on btrfs filesystem like enabling/rescan and etc.

               See btrfs-quota(8) and btrfs-qgroup(8) for details.

           receive
               Receive subvolume data from stdin/file for restore and etc.

               See btrfs-receive(8) for details.

           replace
               Replace btrfs devices.

               See btrfs-replace(8) for details.

           rescue
               Try to rescue damaged btrfs filesystem.

               See btrfs-rescue(8) for details.

           restore
               Try to restore files from a damaged btrfs filesystem.

               See btrfs-restore(8) for details.

           scrub
               Scrub a btrfs filesystem.

               See btrfs-scrub(8) for details.

           send
               Send subvolume data to stdout/file for backup and etc.

               See btrfs-send(8) for details.

           subvolume
               Create/delete/list/manage btrfs subvolume.

               See btrfs-subvolume(8) for details.

## [](#STANDALONE_TOOLS)STANDALONE TOOLS

           New functionality could be provided using a standalone tool. If
           the functionality proves to be useful, then the standalone tool is
           declared obsolete and its functionality is copied to the main
           tool. Obsolete tools are removed after a long (years) depreciation
           period.

           Tools that are still in active use without an equivalent in btrfs:

           btrfs-convert
               in-place conversion from ext2/3/4 filesystems to btrfs

           btrfstune
               tweak some filesystem properties on a unmounted filesystem

           btrfs-select-super
               rescue tool to overwrite primary superblock from a spare copy

           btrfs-find-root
               rescue helper to find tree roots in a filesystem

           Deprecated and obsolete tools:

           btrfs-debug-tree
               moved to btrfs inspect-internal dump-tree. Removed from source
               distribution.

           btrfs-show-super
               moved to btrfs inspect-internal dump-super, standalone
               removed.

           btrfs-zero-log
               moved to btrfs rescue zero-log, standalone removed.

           For space-constrained environments, it’s possible to build a
           single binary with functionality of several standalone tools. This
           is following the concept of busybox where the file name selects
           the functionality. This works for symlinks or hardlinks. The full
           list can be obtained by btrfs help --box.

## [](#EXIT_STATUS)EXIT STATUS

           btrfs returns a zero exit status if it succeeds. Non zero is
           returned in case of failure.

## [](#AVAILABILITY)AVAILABILITY

           btrfs is part of btrfs-progs. Please refer to the btrfs wiki
           http://btrfs.wiki.kernel.org for further details.

## [](#SEE_ALSO)SEE ALSO

           btrfs(5), btrfs-balance(8), btrfs-check(8), btrfs-convert(8),
           btrfs-device(8), btrfs-filesystem(8), btrfs-inspect-internal(8),
           btrfs-property(8), btrfs-qgroup(8), btrfs-quota(8),
           btrfs-receive(8), btrfs-replace(8), btrfs-rescue(8),
           btrfs-restore(8), btrfs-scrub(8), btrfs-send(8),
           btrfs-subvolume(8), btrfstune(8), mkfs.btrfs(8)

## [](#COLOPHON)COLOPHON

           This page is part of the btrfs-progs (btrfs filesystem tools)
           project.  Information about the project can be found at 
           ⟨https://btrfs.wiki.kernel.org/index.php/Btrfs_source_repositories⟩.
           If you have a bug report for this manual page, see
           ⟨https://btrfs.wiki.kernel.org/index.php/Problem_FAQ#How_do_I_report_bugs_and_issues.3F⟩.
           This page was obtained from the project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/linux/kernel/git/kdave/btrfs-progs.git⟩
           on 2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-05-10.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Btrfs v5.16.1                   02/06/2022                       BTRFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [importctl(1)](../man1/importctl.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [org.freedesktop.import1(5)](../man5/org.freedesktop.import1.5.html),  [repart.d(5)](../man5/repart.d.5.html),  [fsck.btrfs(8)](../man8/fsck.btrfs.8.html),  [mkfs.btrfs(8)](../man8/mkfs.btrfs.8.html),  [systemd-gpt-auto-generator(8)](../man8/systemd-gpt-auto-generator.8.html)

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
