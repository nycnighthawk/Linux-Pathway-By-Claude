---
{"title": "umount(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/umount.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# umount(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NON-SUPERUSER UMOUNTS](#NON-SUPERUSER_UMOUNTS) \| [LOOP DEVICE](#LOOP_DEVICE) \| [EXIT STATUS](#EXIT_STATUS) \| [EXTERNAL HELPERS](#EXTERNAL_HELPERS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UMOUNT(8)                 System Administration                 UMOUNT(8)

## [](#NAME)NAME

           umount - unmount filesystems

## [](#SYNOPSIS)SYNOPSIS

           umount -a [-dflnrv] [-t fstype] [-O option...]

           umount [-dflnrv] {directory|device}

           umount -h|-V

## [](#DESCRIPTION)DESCRIPTION

           The umount command detaches the mentioned filesystem(s) from the
           file hierarchy. A filesystem is specified by giving the directory
           where it has been mounted. Giving the special device on which the
           filesystem lives may also work, but is obsolete, mainly because it
           will fail in case this device was mounted on more than one
           directory.

           Note that a filesystem cannot be unmounted when it is 'busy' - for
           example, when there are open files on it, or when some process has
           its working directory there, or when a swap file on it is in use.
           The offending process could even be umount itself - it opens libc,
           and libc in its turn may open for example locale files. A lazy
           unmount avoids this problem, but it may introduce other issues.
           See --lazy description below.

## [](#OPTIONS)OPTIONS

           -a, --all
               All of the filesystems described in /proc/self/mountinfo (or
               in deprecated /etc/mtab) are unmounted, except the proc,
               devfs, devpts, sysfs, rpc_pipefs and nfsd filesystems. This
               list of the filesystems may be replaced by --types umount
               option.

           -A, --all-targets
               Unmount all mountpoints in the current mount namespace for the
               specified filesystem. The filesystem can be specified by one
               of the mountpoints or the device name (or UUID, etc.). When
               this option is used together with --recursive, then all nested
               mounts within the filesystem are recursively unmounted. This
               option is only supported on systems where /etc/mtab is a
               symbolic link to /proc/mounts.

           -c, --no-canonicalize
               Do not canonicalize paths. The paths canonicalization is based
               on stat(2) and readlink(2) system calls. These system calls
               may hang in some cases (for example on NFS if server is not
               available). The option has to be used with canonical path to
               the mount point.

               This option is silently ignored by umount for unprivileged
               users.

               For more details about this option see the mount(8) man page.
               Note that umount does not pass this option to the
               /sbin/umount.type helpers.

           -d, --detach-loop
               When the unmounted device was a loop device, also free this
               loop device. This option is unnecessary for devices
               initialized by mount(8), in this case "autoclear"
               functionality is enabled by default.

           --fake
               Causes everything to be done except for the actual system call
               or umount helper execution; this 'fakes' unmounting the
               filesystem. It can be used to remove entries from the
               deprecated /etc/mtab that were unmounted earlier with the -n
               option.

           -f, --force
               Force an unmount (in case of an unreachable NFS system).

               Note that this option does not guarantee that umount command
               does not hang. It’s strongly recommended to use absolute paths
               without symbolic links to avoid unwanted readlink(2) and
               stat(2) system calls on unreachable NFS in umount.

           -i, --internal-only
               Do not call the /sbin/umount.filesystem helper even if it
               exists. By default such a helper program is called if it
               exists.

           -l, --lazy
               Lazy unmount. Detach the filesystem from the file hierarchy
               now, and clean up all references to this filesystem as soon as
               it is not busy anymore.

               A system reboot would be expected in near future if you’re
               going to use this option for network filesystem or local
               filesystem with submounts. The recommended use-case for umount
               -l is to prevent hangs on shutdown due to an unreachable
               network share where a normal umount will hang due to a downed
               server or a network partition. Remounts of the share will not
               be possible.

           -N, --namespace ns
               Perform umount in the mount namespace specified by ns. ns is
               either PID of process running in that namespace or special
               file representing that namespace.

               umount switches to the namespace when it reads /etc/fstab,
               writes /etc/mtab (or writes to /run/mount) and calls umount(2)
               system call, otherwise it runs in the original namespace. It
               means that the target mount namespace does not have to contain
               any libraries or other requirements necessary to execute
               umount(2) command.

               See mount_namespaces(7) for more information.

           -n, --no-mtab
               Unmount without writing in /etc/mtab.

           -O, --test-opts option...
               Unmount only the filesystems that have the specified option
               set in /etc/fstab. More than one option may be specified in a
               comma-separated list. Each option can be prefixed with no to
               indicate that no action should be taken for this option.

           -q, --quiet
               Suppress "not mounted" error messages.

           -g, --graceful
               Exit successfully even if the target is not mounted or does
               not exist. This option is designed for use in shutdown scripts
               and service managers where idempotent unmount behavior is
               desired. Only effective for the root user.

           -R, --recursive
               Recursively unmount each specified directory. Recursion for
               each directory will stop if any unmount operation in the chain
               fails for any reason. The relationship between mountpoints is
               determined by /proc/self/mountinfo entries. The filesystem
               must be specified by mountpoint path; a recursive unmount by
               device name (or UUID) is unsupported. Since version 2.37 it
               umounts also all over-mounted filesystems (more filesystems on
               the same mountpoint).

           -r, --read-only
               When an unmount fails, try to remount the filesystem
               read-only.

           -t, --types type...
               Indicate that the actions should only be taken on filesystems
               of the specified type. More than one type may be specified in
               a comma-separated list. The list of filesystem types can be
               prefixed with no to indicate that no action should be taken
               for all of the mentioned types. Note that umount reads
               information about mounted filesystems from kernel
               (/proc/mounts) and filesystem names may be different than
               filesystem names used in the /etc/fstab (e.g., "nfs4" vs.
               "nfs").

           -v, --verbose
               Verbose mode.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#NON-SUPERUSER_UMOUNTS)NON-SUPERUSER UMOUNTS

           Normally, only the superuser can umount filesystems. However, when
           fstab contains the user option on a line, anybody can umount the
           corresponding filesystem. For more details see mount(8) man page.

           Non-root users must specify the filesystem by mountpoint path
           only. Device names, tags (LABEL=, UUID=, etc.) and loop device
           resolution are not supported for unprivileged users.

           Since version 2.34 the umount command can be used to perform
           umount operation also for fuse filesystems if kernel mount table
           contains user’s ID. In this case fstab user= mount option is not
           required.

           Since version 2.35 umount command does not exit when user
           permissions are inadequate by internal libmount security rules. It
           drops suid permissions and continue as regular unprivileged user.
           This can be used to support use-cases where root permissions are
           not necessary (e.g., fuse filesystems, user namespaces, etc).

## [](#LOOP_DEVICE)LOOP DEVICE

           The umount command will automatically detach loop device
           previously initialized by mount(8) command independently of
           /etc/mtab.

           In this case the device is initialized with "autoclear" flag (see
           losetup(8) output for more details), otherwise it’s necessary to
           use the option --detach-loop or call losetup -d device. The
           autoclear feature is supported since Linux 2.6.25.

           Note that since Linux v3.7 kernel uses "lazy device destruction".
           The system just marks the loop device by autoclear flag and
           destroys it later. If you need to wait for a complete removal of
           the loop device, call udevadm settle after umount.

## [](#EXIT_STATUS)EXIT STATUS

           umount has the following exit status values (the bits can be
           ORed):

           0
               success

           1
               incorrect invocation or permissions

           2
               system error (out of memory, cannot fork, no more loop
               devices)

           4
               internal mount bug

           8
               user interrupt

           16
               problems writing or locking /etc/mtab

           32
               mount failure

           64
               some umount succeeded

               The command umount -a returns 0 (all succeeded), 32 (all
               failed), or 64 (some failed, some succeeded).

           126
               failed to execute external /sbin/umount.<type> mount helper
               (since util-linux v2.41)

## [](#EXTERNAL_HELPERS)EXTERNAL HELPERS

           The syntax of external unmount helpers is:

              umount.suffix {directory|device} [-flnrv] [-N namespace]
              [-t type.subtype]

           where suffix is the filesystem type (or the value from a uhelper=
           or helper= marker in the mtab file). The -t option can be used for
           filesystems that have subtype support. For example:

              umount.fuse -t fuse.sshfs

           A uhelper=something marker (unprivileged helper) can appear in the
           /etc/mtab file when ordinary users need to be able to unmount a
           mountpoint that is not defined in /etc/fstab (for example for a
           device that was mounted by udisks(1)).

           A helper=type marker in the mtab file will redirect all unmount
           requests to the /sbin/umount.type helper independently of UID.

           Note that /etc/mtab is currently deprecated and helper= and other
           userspace mount options are maintained by libmount.

           The exit status value of the helper is returned as the exit status
           of umount(8). The value 126 is used if the mount helper program is
           found, but the execl(3) failed.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBMOUNT_DEBUG=all
               Enable libmount debug output.

           LIBMOUNT_FSTAB=<path>
               Override the default location of the fstab file (ignored for
               suid).

## [](#FILES)FILES

           /etc/mtab
               table of mounted filesystems (deprecated and usually replaced
               by symbolic link to /proc/mounts)

           /etc/fstab
               table of known filesystems

           /proc/self/mountinfo
               table of mounted filesystems generated by kernel.

## [](#HISTORY)HISTORY

           A umount command appeared in Version 6 AT&T UNIX.

## [](#SEE_ALSO)SEE ALSO

           umount(2), losetup(8), mount_namespaces(7), mount(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The umount command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-1062-f... 2026-08-03                      UMOUNT(8)

------------------------------------------------------------------------

Pages that refer to this page: [eject(1)](../man1/eject.1.html),  [systemd-dissect(1)](../man1/systemd-dissect.1.html),  [systemd-mstack(1)](../man1/systemd-mstack.1.html),  [unshare(1)](../man1/unshare.1.html),  [mount(2)](../man2/mount.2.html),  [umount(2)](../man2/umount.2.html),  [fstab(5)](../man5/fstab.5.html),  [nfs(5)](../man5/nfs.5.html),  [systemd.mount(5)](../man5/systemd.mount.5.html),  [cgroups(7)](../man7/cgroups.7.html),  [mount_namespaces(7)](../man7/mount_namespaces.7.html),  [blkdeactivate(8)](../man8/blkdeactivate.8.html),  [mount(8)](../man8/mount.8.html),  [pivot_root(8)](../man8/pivot_root.8.html),  [umount(8)](../man8/umount.8.html),  [umount.nfs(8)](../man8/umount.nfs.8.html),  [xfs_repair(8)](../man8/xfs_repair.8.html)

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
