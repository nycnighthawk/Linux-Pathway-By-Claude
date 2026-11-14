---
{"title": "fsck.minix(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/fsck.minix.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fsck.minix(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [WARNING](#WARNING) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [EXIT STATUS](#EXIT_STATUS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FSCK.MINIX(8)             System Administration             FSCK.MINIX(8)

## [](#NAME)NAME

           fsck.minix - check consistency of Minix filesystem

## [](#SYNOPSIS)SYNOPSIS

           fsck.minix [options] device

## [](#DESCRIPTION)DESCRIPTION

           fsck.minix performs a consistency check for the Linux MINIX
           filesystem.

           The program assumes the filesystem is quiescent. fsck.minix should
           not be used on a mounted device unless you can be sure nobody is
           writing to it. Remember that the kernel can write to device when
           it searches for files.

           The device name will usually have the following form:
              ┌────────────────┬─────────────┐
              │                │             │
              │ /dev/hda[1-63] │ IDE disk 1  │
              ├────────────────┼─────────────┤
              │                │             │
              │ /dev/hdb[1-63] │ IDE disk 2  │
              ├────────────────┼─────────────┤
              │                │             │
              │ /dev/sda[1-15] │ SCSI disk 1 │
              ├────────────────┼─────────────┤
              │                │             │
              │ /dev/sdb[1-15] │ SCSI disk 2 │
              └────────────────┴─────────────┘

           If the filesystem was changed, i.e., repaired, then
           fsck.minix will print "FILE SYSTEM HAS BEEN CHANGED" and
           will sync(2) three times before exiting. There is no need
           to reboot after check.

## [](#WARNING)WARNING

           fsck.minix should not be used on a mounted filesystem.
           Using fsck.minix on a mounted filesystem is very
           dangerous, due to the possibility that deleted files are
           still in use, and can seriously damage a perfectly good
           filesystem! If you absolutely have to run fsck.minix on a
           mounted filesystem, such as the root filesystem, make sure
           nothing is writing to the disk, and that no files are
           "zombies" waiting for deletion.

## [](#OPTIONS)OPTIONS

           -l, --list
               List all filenames.

           -r, --repair
               Perform interactive repairs.

           -a, --auto
               Perform automatic repairs. This option implies
               --repair and serves to answer all of the questions
               asked with the default. Note that this can be
               extremely dangerous in the case of extensive
               filesystem damage.

           -v, --verbose
               Be verbose.

           -s, --super
               Output superblock information.

           -m, --uncleared
               Activate MINIX-like "mode not cleared" warnings.

           -f, --force
               Force a filesystem check even if the filesystem was
               marked as valid. Marking is done by the kernel when
               the filesystem is unmounted.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#DIAGNOSTICS)DIAGNOSTICS

           There are numerous diagnostic messages. The ones mentioned
           here are the most commonly seen in normal usage.

           If the device does not exist, fsck.minix will print
           "unable to read super block". If the device exists, but is
           not a MINIX filesystem, fsck.minix will print "bad magic
           number in super-block".

## [](#EXIT_STATUS)EXIT STATUS

           The exit status returned by fsck.minix is the sum of the
           following:

           0
               No errors

           3
               Filesystem errors corrected, system should be rebooted
               if filesystem was mounted

           4
               Filesystem errors left uncorrected

           7
               Combination of exit statuses 3 and 4

           8
               Operational error

           16
               Usage or syntax error

## [](#AUTHORS)AUTHORS

           Linus Torvalds <torvalds@cs.helsinki.fi>. Exit status
           values by Rik Faith <faith@cs.unc.edu> Added support for
           filesystem valid flag: Dr. Wettstein
           <greg%wind.uucp@plains.nodak.edu>. Check to prevent fsck
           of mounted filesystem added by Daniel Quinlan
           <quinlan@yggdrasil.com>. Minix v2 fs support by Andreas
           Schwab <schwab@issan.informatik.uni-dortmund.de>, updated
           by Nicolai Langfeldt <janl@math.uio.no>. Portability patch
           by Russell King <rmk@ecs.soton.ac.uk>.

## [](#SEE_ALSO)SEE ALSO

           fsck(8), fsck.ext2(8), mkfs(8), mkfs.ext2(8),
           mkfs.minix(8), reboot(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The fsck.minix command is part of the util-linux package
           which can be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This
           page is part of the util-linux (a random collection of
           Linux utilities) project. Information about the project
           can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If
           you have a bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from
           the project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩
           on 2026-08-04. (At that time, the date of the most recent
           commit that was found in the repository was 2026-08-03.)
           If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or
           more up-to-date source for the page, or you have
           corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                  FSCK.MINIX(8)

------------------------------------------------------------------------

Pages that refer to this page: [fsck(8@@e2fsprogs)](../man8/fsck.8@@e2fsprogs.html),  [fsck(8)](../man8/fsck.8.html),  [systemd-fsck@.service(8)](../man8/systemd-fsck@.service.8.html)

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
