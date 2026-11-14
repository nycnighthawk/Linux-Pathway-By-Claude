---
{"title": "statmount(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/statmount.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# statmount(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    statmount(2)               System Calls Manual               statmount(2)

## [](#NAME)NAME

           statmount - get a mount status

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/mount.h>  /* Definition of STATMOUNT_* constants */
           #include <unistd.h>

           int syscall(SYS_statmount, struct mnt_id_req *req,
                       struct statmount *smbuf, size_t bufsize,
                       unsigned int flags);

           #include <linux/mount.h>

           struct mnt_id_req {
               __u32  size;        /* sizeof(struct mnt_id_req) */
               union {
                   __u32  mnt_ns_fd;  /* fd of mnt_ns to query the mnt_id in */
                   __u32  mnt_fd;     /* fd on the mount being queried */
               };
               __u64  mnt_id;      /* The mnt_id being queried */
               __u64  param;       /* ORed combination of the STATMOUNT_ constants */
               __u32  mnt_ns_id;   /* The id of mnt_ns to query the mnt_id in */
           };

           struct statmount {
               __u32  size;
               __u32  mnt_opts;
               __u64  mask;
               __u32  sb_dev_major;
               __u32  sb_dev_minor;
               __u64  sb_magic;
               __u32  sb_flags;
               __u32  fs_type;
               __u64  mnt_id;
               __u64  mnt_parent_id;
               __u32  mnt_id_old;
               __u32  mnt_parent_id_old;
               __u64  mnt_attr;
               __u64  mnt_propagation;
               __u64  mnt_peer_group;
               __u64  mnt_master;
               __u64  propagate_from;
               __u32  mnt_root;
               __u32  mnt_point;
               __u64  mnt_ns_id;
               __u32  fs_subtype;
               __u32  sb_source;
               __u32  opt_num;
               __u32  opt_array;
               __u32  opt_sec_num;
               __u32  opt_sec_array;
               __u32  mnt_uidmap_num;
               __u32  mnt_uidmap;
               __u32  mnt_gidmap_num;
               __u32  mnt_gidmap;
               __u64  supported_mask;
               char   str[];
           };

           Note: glibc provides no wrapper for statmount(), necessitating the
           use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           To access a mount's status, the caller must have CAP_SYS_ADMIN in
           the user namespace.  In case of accessing a mount in a foreign
           mount namespace (specified via req.mnt_ns_id or req.mnt_ns_fd),
           the foreign mount namespace should be child of the current
           namespace.

           This function returns information about a mount, storing it in the
           buffer pointed to by smbuf.  The returned buffer is a struct
           statmount which is of size bufsize with the fields filled in as
           described below.  flags must either be 0 or STATMOUNT_BY_FD.

           (Note that reserved space and padding is omitted.)

       The mnt_id_req structure
           req.size is used by the kernel to determine which
           struct mnt_id_req is being passed in; it should always be set to
           sizeof(struct mnt_id_req).

           req.mnt_ns_fd can be obtained from PIDFD_GET_MNT_NAMESPACE
           ioctl(2) operation or by opening a file descriptor to
           /proc/pid/ns/mnt and is used to specify a foreign mount namespace
           in which to query req.mnt_id (since Linux 6.18).

           req.mnt_fd is a file descriptor on a mount.  If STATMOUNT_BY_FD
           flag is specified, req.mnt_id and req.mnt_ns_id are zeroed, the
           function will return information about the mount the file
           descriptor is on (since Linux 7.0).

           The fd can also be on a mount that has been lazily unmounted (see
           umount2(2) with MNT_DETACH).  In this case, STATMOUNT_MNT_POINT
           and STATMOUNT_MNT_NS_ID will be unset, since an unmounted mount is
           no longer a part of the filesystem.

           req.mnt_id can be obtained from either statx(2) using
           STATX_MNT_ID_UNIQUE or from listmount(2) and is used as the
           identifier to query the status of the desired mount point.

           req.param is used to tell the kernel which fields the caller is
           interested in.  It is an ORed combination of the following
           constants

               STATMOUNT_SB_BASIC         /* Want/got sb_* */
               STATMOUNT_MNT_BASIC        /* Want/got mnt_* */
               STATMOUNT_PROPAGATE_FROM   /* Want/got propagate_from */
               STATMOUNT_MNT_ROOT         /* Want/got mnt_root  */
               STATMOUNT_MNT_POINT        /* Want/got mnt_point */
               STATMOUNT_FS_TYPE          /* Want/got fs_type */
               STATMOUNT_MNT_NS_ID        /* Want/got mnt_ns_id */
               STATMOUNT_MNT_OPTS         /* Want/got mnt_opts */
               STATMOUNT_FS_SUBTYPE       /* Want/got fs_subtype */
               STATMOUNT_SB_SOURCE        /* Want/got sb_source */
               STATMOUNT_OPT_ARRAY        /* Want/got opt_{num,array} */
               STATMOUNT_OPT_SEC_ARRAY    /* Want/got opt_sec_{num,array} */
               STATMOUNT_MNT_UIDMAP       /* Want/got uidmap{_num,} */
               STATMOUNT_MNT_GIDMAP       /* Want/got gidmap{_num,} */
               STATMOUNT_SUPPORTED_MASK   /* Want/got supported mask flags */

           In general, the kernel does not reject values in req.param other
           than the above.  (For an exception, see EINVAL in errors.)
           Instead, it simply informs the caller which values are supported
           by this kernel and filesystem via the statmount.mask field.
           Therefore, do not simply set req.param to UINT_MAX (all bits set),
           as one or more bits may, in the future, be used to specify an
           extension to the buffer.

           req.mnt_ns_id can be obtained from NS_GET_MNTNS_ID ioctl(2)
           operation and is used to specify a foreign mount namespace in
           which to query req.mnt_id (since Linux 6.11).

       The returned information
           The status information for the target mount is returned in the
           statmount structure pointed to by smbuf.

           The fields in the statmount structure are:

           smbuf.size
                  The size of the returned smbuf structure, including any of
                  the strings fields that were filled.

           smbuf.mnt_opts (since Linux 6.11)
                  The offset to the location in the smbuf.str buffer that
                  contains a comma separated list of mount options, similiar
                  to those in proc_pid_mountinfo(5).  It is a null-terminated
                  string.

           smbuf.mask
                  The ORed combination of STATMOUNT_* flags indicating which
                  fields were filled in and thus valid.  The kernel may
                  return fields that weren't requested, and may fail to
                  return fields that were requested, depending on what the
                  backing file system and kernel supports.  In either case,
                  req.param will not be equal to mask.

           smbuf.sb_dev_major
           smbuf.sb_dev_minor
                  The device that is mounted at this mount point.

           smbuf.sb_magic
                  The file system specific super block magic.

           smbuf.sb_flags
                  The flags that are set on the super block, an ORed
                  combination of SB_RDONLY, SB_SYNCHRONOUS, SB_DIRSYNC,
                  SB_LAZYTIME.

           smbuf.fs_type
                  The offset to the location in the smbuf.str buffer that
                  contains the string representation of the mounted file
                  system.  It is a null-terminated string.

           smbuf.mnt_id
                  The unique mount ID of the mount.

           smbuf.mnt_parent_id
                  The unique mount ID of the parent mount point of this
                  mount.  If this is the root mount point then
                  smbuf.mnt_id == smbuf.parent_mount_id.

           smbuf.mnt_id_old
                  This corresponds to the mount ID that is exported by
                  /proc/pid/mountinfo.

           smbuf.mnt_parent_id_old
                  This corresponds to the parent mount ID that is exported by
                  /proc/pid/mountinfo.

           smbuf.mnt_attr
                  The MOUNT_ATTR_* flags set on this mount point.

           smbuf.mnt_propagation
                  The mount propagation flags, which can be one of MS_SHARED,
                  MS_SLAVE, MS_PRIVATE, MS_UNBINDABLE.

           smbuf.mnt_peer_group
                  The ID of the shared peer group.

           smbuf.mnt_master
                  The mount point receives its propagation from this mount
                  ID.

           smbuf.propagate_from
                  The ID from the namespace we propagated from.

           smbuf.mnt_root
                  The offset to the location in the smbuf.str buffer that
                  contains the string representation of the mount relative to
                  the root of the file system.  It is a null-terminated
                  string.

           smbuf.mnt_point
                  The offset to the location in the smbuf.str buffer that
                  contains the string representation of the mount relative to
                  the current root (ie if you are in a chroot).  It is a
                  null-terminated string.

           smbuf.mnt_ns_id (since Linux 6.11)
                  The unique ID of the mount namespace the mount belongs to.

           smbuf.fs_subtype (since Linux 6.13)
                  The offset to the location in the smbuf.str buffer that
                  contains the string representation of the file system
                  subtype.  This is particularly useful for disambiguating
                  FUSE mounts.  It is a null-terminated string.

           smbuf.sb_source (since Linux 6.13)
                  The offset to the location in the smbuf.str that contains
                  the source of the mount.  It is a null-terminated string.

           smbuf.opt_num (since Linux 6.13)
                  The number of filesystem options set on the mount.

           smbuf.opt_array (since Linux 6.13)
                  The offset to the location in the smbuf.str buffer that
                  contains file system options separated by null bytes.  They
                  can be iterated over with the help of smbuf.opt_num.

           smbuf.opt_sec_num (since Linux 6.13)
                  The number of security options set on the mount.

           smbuf.opt_sec_array (since Linux 6.13)
                  The offset to the location in the smbuf.str buffer that
                  contains security options separated by null bytes.  They
                  can be iterated over with the help of smbuf.opt_sec_num.

           smbuf.mnt_uidmap_num (since Linux 6.15)
                  The number of uid mappings applied on the mount.  If
                  smbuf.mask has STATMOUNT_MNT_UIDMAP set and this field is
                  0, then uid mappings applied on the mount cannot be
                  resolved in the user namespace of the caller.

           smbuf.mnt_uidmap (since Linux 6.15)
                  The offset to the location in the smbuf.str buffer that
                  contains uid mappings as consecutive null-terminated
                  strings.  They can be iterated over with the help of
                  smbuf.mnt_uidmap_num.  The whole range of uid mappings must
                  be resolvable in the user namespace of the caller.

           smbuf.mnt_gidmap_num (since Linux 6.15)
                  The number of gid mappings applied on the mount.  If
                  smbuf.mask has STATMOUNT_MNT_GIDMAP set and this field is
                  0, then gid mappings applied on the mount cannot be
                  resolved in the user namespace of the caller.

           smbuf.mnt_gidmap (since Linux 6.15)
                  The offset to the location in the smbuf.str buffer that
                  contains gid mappings as consecutive null-terminated
                  strings.  They can be iterated over with the help of
                  smbuf.mnt_gidmap_num.  The whole range of gid mappings must
                  be resolvable in the user namespace of the caller.

           smbuf.supported_mask (since Linux 6.15)
                  The ORed combination of STATMOUNT_* flags supported by the
                  current kernel.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EPERM  Permission is denied for accessing this mount.

           EFAULT req or smbuf points to a location outside the process's
                  accessible address space.

           EINVAL Invalid flag specified in flags.

           EINVAL req is of insufficient size to be utilized.

           EINVAL Both req.mnt_ns_id and req.mnt_ns_fd were set.

           EINVAL req.mnt_id or req.mnt_ns_id was specified alongside
                  req.mnt_fd.

           EBADF  req.mnt_fd is an invalid file descriptor.

           E2BIG  req is too large.

           EOVERFLOW
                  The size of smbuf is too small to contain either the
                  smbuf.fs_type, smbuf.mnt_root, or smbuf.mnt_point.
                  Allocate a larger buffer and retry the call.

           ENOENT The specified req.mnt_id doesn't exist.

           ENOMEM Out of memory (i.e., kernel memory).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#SEE_ALSO)SEE ALSO

           listmount(2), statx(2)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-08-22                   statmount(2)

------------------------------------------------------------------------

Pages that refer to this page: [mountpoint(1)](../man1/mountpoint.1.html),  [listmount(2)](../man2/listmount.2.html),  [statx(2)](../man2/statx.2.html),  [findmnt(8)](../man8/findmnt.8.html),  [xfs_io(8)](../man8/xfs_io.8.html)

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
