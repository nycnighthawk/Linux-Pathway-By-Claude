---
{"title": "proc_pid_mountinfo(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_mountinfo.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_mountinfo(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_mountinfo(5)      File Formats Manual      proc_pid_mountinfo(5)

## [](#NAME)NAME

           /proc/pid/mountinfo - mount information

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/mountinfo (since Linux 2.6.26)
                  This file contains information about mounts in the
                  process's mount namespace (see mount_namespaces(7)).  It
                  supplies various information (e.g., propagation state, root
                  of mount for bind mounts, identifier for each mount and its
                  parent) that is missing from the (older) /proc/pid/mounts
                  file, and fixes various other problems with that file
                  (e.g., nonextensibility, failure to distinguish per-mount
                  versus per-superblock options).

                  The file contains lines of the form:

                  36 35 98:0 /mnt1 /mnt2 rw,noatime master:1 - ext3 /dev/root rw,errors=continue
                  (1)(2)(3)   (4)   (5)      (6)      (7)   (8) (9)   (10)         (11)

                  The numbers in parentheses are labels for the descriptions
                  below:

                  (1)  mount ID: a unique ID for the mount (may be reused
                       after umount(2)).

                  (2)  parent ID: the ID of the parent mount (or of self for
                       the root of this mount namespace's mount tree).

                       If a new mount is stacked on top of a previous
                       existing mount (so that it hides the existing mount)
                       at pathname P, then the parent of the new mount is the
                       previous mount at that location.  Thus, when looking
                       at all the mounts stacked at a particular location,
                       the top-most mount is the one that is not the parent
                       of any other mount at the same location.  (Note,
                       however, that this top-most mount will be accessible
                       only if the longest path subprefix of P that is a
                       mount point is not itself hidden by a stacked mount.)

                       If the parent mount lies outside the process's root
                       directory (see chroot(2)), the ID shown here won't
                       have a corresponding record in mountinfo whose mount
                       ID (field 1) matches this parent mount ID (because
                       mounts that lie outside the process's root directory
                       are not shown in mountinfo).  As a special case of
                       this point, the process's root mount may have a parent
                       mount (for the initramfs filesystem) that lies outside
                       the process's root directory, and an entry for that
                       mount will not appear in mountinfo.

                  (3)  major:minor: the value of st_dev for files on this
                       filesystem (see stat(2)).

                  (4)  root: the pathname of the directory in the filesystem
                       which forms the root of this mount.

                  (5)  mount point: the pathname of the mount point relative
                       to the process's root directory.

                  (6)  mount options: per-mount options (see mount(2)).

                  (7)  optional fields: zero or more fields of the form
                       "tag[:value]"; see below.

                  (8)  separator: the end of the optional fields is marked by
                       a single hyphen.

                  (9)  filesystem type: the filesystem type in the form
                       "type[.subtype]".

                  (10) mount source: filesystem-specific information or
                       "none".

                  (11) super options: per-superblock options (see mount(2)).

                  Currently, the possible optional fields are shared, master,
                  propagate_from, and unbindable.  See mount_namespaces(7)
                  for a description of these fields.  Parsers should ignore
                  all unrecognized optional fields.

                  For more information on mount propagation see
                  Documentation/filesystems/sharedsubtree.rst in the Linux
                  kernel source tree.

## [](#SEE_ALSO)SEE ALSO

           proc(5)

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

    Linux man-pages 6.19            2026-02-08          proc_pid_mountinfo(5)

------------------------------------------------------------------------

Pages that refer to this page: [statmount(2)](../man2/statmount.2.html),  [proc_pid(5)](../man5/proc_pid.5.html)

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
