---
{"title": "xattr(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/xattr.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xattr(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xattr(7)             Miscellaneous Information Manual            xattr(7)

## [](#NAME)NAME

           xattr - Extended attributes

## [](#DESCRIPTION)DESCRIPTION

           Extended attributes are name:value pairs associated permanently
           with files and directories, similar to the environment strings
           associated with a process.  An attribute may be defined or
           undefined.  If it is defined, its value may be empty or non-empty.

           Extended attributes are extensions to the normal attributes which
           are associated with all inodes in the system (i.e., the stat(2)
           data).  They are often used to provide additional functionality to
           a filesystem—for example, additional security features such as
           Access Control Lists (ACLs) may be implemented using extended
           attributes.

           Users with search access to a file or directory may use
           listxattr(2) to retrieve a list of attribute names defined for
           that file or directory.

           Extended attributes are accessed as atomic objects.  Reading
           (getxattr(2)) retrieves the whole value of an attribute and stores
           it in a buffer.  Writing (setxattr(2)) replaces any previous value
           with the new value.

           Space consumed for extended attributes may be counted towards the
           disk quotas of the file owner and file group.

       Extended attribute namespaces
           Attribute names are null-terminated strings.  The attribute name
           is always specified in the fully qualified namespace.attribute
           form, for example, user.mime_type, trusted.md5sum,
           system.posix_acl_access, or security.selinux.

           The namespace mechanism is used to define different classes of
           extended attributes.  These different classes exist for several
           reasons; for example, the permissions and capabilities required
           for manipulating extended attributes of one namespace may differ
           to another.

           Currently, the security, system, trusted, and user extended
           attribute classes are defined as described below.  Additional
           classes may be added in the future.

       Extended security attributes
           The security attribute namespace is used by kernel security
           modules, such as Security Enhanced Linux, and also to implement
           file capabilities (see capabilities(7)).  Read and write access
           permissions to security attributes depend on the policy
           implemented for each security attribute by the security module.
           When no security module is loaded, all processes have read access
           to extended security attributes, and write access is limited to
           processes that have the CAP_SYS_ADMIN capability.

       System extended attributes
           System extended attributes are used by the kernel to store system
           objects such as Access Control Lists.  Read and write access
           permissions to system attributes depend on the policy implemented
           for each system attribute implemented by filesystems in the
           kernel.

       Trusted extended attributes
           Trusted extended attributes are visible and accessible only to
           processes that have the CAP_SYS_ADMIN capability.  Attributes in
           this class are used to implement mechanisms in user space (i.e.,
           outside the kernel) which keep information in extended attributes
           to which ordinary processes should not have access.

       User extended attributes
           User extended attributes may be assigned to files and directories
           for storing arbitrary additional information such as the mime
           type, character set or encoding of a file.  The access permissions
           for user attributes are defined by the file permission bits: read
           permission is required to retrieve the attribute value, and writer
           permission is required to change it.

           The file permission bits of regular files and directories are
           interpreted differently from the file permission bits of special
           files and symbolic links.  For regular files and directories the
           file permission bits define access to the file's contents, while
           for device special files they define access to the device
           described by the special file.  The file permissions of symbolic
           links are not used in access checks.  These differences would
           allow users to consume filesystem resources in a way not
           controllable by disk quotas for group or world writable special
           files and directories.

           For this reason, user extended attributes are allowed only for
           regular files and directories, and access to user extended
           attributes is restricted to the owner and to users with
           appropriate capabilities for directories with the sticky bit set
           (see the chmod(1) manual page for an explanation of the sticky
           bit).

       Filesystem differences
           The kernel and the filesystem may place limits on the maximum
           number and size of extended attributes that can be associated with
           a file.  The VFS-imposed limits on attribute names and values are
           255 bytes and 64 kB, respectively.  The list of attribute names
           that can be returned is also limited to 64 kB (see BUGS in
           listxattr(2)).

           Some filesystems, such as Reiserfs (and, historically, ext2 and
           ext3), require the filesystem to be mounted with the user_xattr
           mount option in order for user extended attributes to be used.

           In the current ext2, ext3, and ext4 filesystem implementations,
           the total bytes used by the names and values of all of a file's
           extended attributes must fit in a single filesystem block (1024,
           2048 or 4096 bytes, depending on the block size specified when the
           filesystem was created).

           In the Btrfs, XFS, and Reiserfs filesystem implementations, there
           is no practical limit on the number of extended attributes
           associated with a file, and the algorithms used to store extended
           attribute information on disk are scalable.

           In the JFS, XFS, and Reiserfs filesystem implementations, the
           limit on bytes used in an EA value is the ceiling imposed by the
           VFS.

           In the Btrfs filesystem implementation, the total bytes used for
           the name, value, and implementation overhead bytes is limited to
           the filesystem nodesize value (16 kB by default).

## [](#STANDARDS)STANDARDS

           Extended attributes are not specified in POSIX.1, but some other
           systems (e.g., the BSDs and Solaris) provide a similar feature.

## [](#NOTES)NOTES

           Since the filesystems on which extended attributes are stored
           might also be used on architectures with a different byte order
           and machine word size, care should be taken to store attribute
           values in an architecture-independent format.

           This page was formerly named attr(5).

## [](#SEE_ALSO)SEE ALSO

           attr(1), getfattr(1), setfattr(1), getxattr(2),
           FS_IOC_GETFLAGS(2const), FS_IOC_SETFLAGS(2const), listxattr(2),
           removexattr(2), setxattr(2), acl(5), capabilities(7), selinux(8)

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

    Linux man-pages 6.19            2026-02-08                       xattr(7)

------------------------------------------------------------------------

Pages that refer to this page: [attr(1)](../man1/attr.1.html),  [getfattr(1)](../man1/getfattr.1.html),  [setfattr(1)](../man1/setfattr.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [capget(2)](../man2/capget.2.html),  [FS_IOC_SETFLAGS(2const)](../man2/FS_IOC_SETFLAGS.2const.html),  [getxattr(2)](../man2/getxattr.2.html),  [listxattr(2)](../man2/listxattr.2.html),  [mount_setattr(2)](../man2/mount_setattr.2.html),  [removexattr(2)](../man2/removexattr.2.html),  [setxattr(2)](../man2/setxattr.2.html),  [errno(3)](../man3/errno.3.html),  [selabel_get_digests_all_partial_matches(3)](../man3/selabel_get_digests_all_partial_matches.3.html),  [selinux_restorecon(3)](../man3/selinux_restorecon.3.html),  [os-release(5)](../man5/os-release.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.resource-control(5)](../man5/systemd.resource-control.5.html),  [tmpfs(5)](../man5/tmpfs.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [mount(8)](../man8/mount.8.html),  [systemd-sysext(8)](../man8/systemd-sysext.8.html)

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
