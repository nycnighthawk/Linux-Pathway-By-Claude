---
{"title": "tmpfs(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/tmpfs.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tmpfs(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    tmpfs(5)                   File Formats Manual                   tmpfs(5)

## [](#NAME)NAME

           tmpfs - a virtual memory filesystem

## [](#DESCRIPTION)DESCRIPTION

           The tmpfs facility allows the creation of filesystems whose
           contents reside in virtual memory.  Since the files on such
           filesystems typically reside in RAM, file access is extremely
           fast.

           The filesystem is automatically created when mounting a filesystem
           with the type tmpfs via a command such as the following:

               $ sudo mount -t tmpfs -o size=10M tmpfs /mnt/mytmpfs

           A tmpfs filesystem has the following properties:

           •  The filesystem can employ swap space when physical memory
              pressure demands it.

           •  The filesystem consumes only as much physical memory and swap
              space as is required to store the current contents of the
              filesystem.

           •  During a remount operation (mount -o remount), the filesystem
              size can be changed (without losing the existing contents of
              the filesystem).

           If a tmpfs filesystem is unmounted, its contents are discarded
           (lost).

       Mount options
           The tmpfs filesystem supports the following mount options:

           size=bytes
                  Specify an upper limit on the size of the filesystem.  The
                  size is given in bytes, and rounded up to entire pages.
                  The limit is removed if the size is 0.

                  The size may have a k, m, or g suffix for Ki, Mi, Gi
                  (binary kilo (kibi), binary mega (mebi), and binary giga
                  (gibi)).

                  The size may also have a % suffix to limit this instance to
                  a percentage of physical RAM.

                  The default, when neither size nor nr_blocks is specified,
                  is size=50%.

           nr_blocks=blocks
                  The same as size, but in blocks of PAGE_CACHE_SIZE.

                  Blocks may be specified with k, m, or g suffixes like size,
                  but not a % suffix.

           nr_inodes=inodes
                  The maximum number of inodes for this instance.  The
                  default is half of the number of your physical RAM pages,
                  or (on a machine with highmem) the number of lowmem RAM
                  pages, whichever is smaller.  The limit is removed if the
                  number is 0.

                  Inodes may be specified with k, m, or g suffixes like size,
                  but not a % suffix.

           noswap(since Linux 6.4)
                  Disables swap.  Remounts must respect the original
                  settings.  By default swap is enabled.

           mode=mode
                  Set initial permissions of the root directory.

           gid=gid (since Linux 2.5.7)
                  Set the initial group ID of the root directory.

           uid=uid (since Linux 2.5.7)
                  Set the initial user ID of the root directory.

           huge=huge_option (since Linux 4.7.0)
                  Set the huge table memory allocation policy for all files
                  in this instance (if CONFIG_TRANSPARENT_HUGEPAGE is
                  enabled).

                  The huge_option value is one of the following:

                  never  Do not allocate huge pages.  This is the default.

                  always Attempt to allocate huge pages every time a new page
                         is needed.

                  within_size
                         Only allocate huge page if it will be fully within
                         i_size.  Also respect fadvise(2) and madvise(2)
                         hints

                  advise Only allocate huge pages if requested with
                         fadvise(2) or madvise(2).

                  deny   For use in emergencies, to force the huge option off
                         from all mounts.

                  force  Force the huge option on for all mounts; useful for
                         testing.

           mpol=mpol_option (since Linux 2.6.15)
                  Set the NUMA memory allocation policy for all files in this
                  instance (if CONFIG_NUMA is enabled).

                  The mpol_option value is one of the following:

                  default
                         Use the process allocation policy (see
                         set_mempolicy(2)).

                  prefer:node
                         Preferably allocate memory from the given node.

                  bind:nodelist
                         Allocate memory only from nodes in nodelist.

                  interleave
                         Allocate from each node in turn.

                  interleave:nodelist
                         Allocate from each node of in turn.

                  local  Preferably allocate memory from the local node.

                  In the above, nodelist is a comma-separated list of decimal
                  numbers and ranges that specify NUMA nodes.  A range is a
                  pair of hyphen-separated decimal numbers, the smallest and
                  largest node numbers in the range.  For example,
                  mpol=bind:0-3,5,7,9-15.

## [](#VERSIONS)VERSIONS

           The tmpfs facility was added in Linux 2.4, as a successor to the
           older ramfs facility, which did not provide limit checking or
           allow for the use of swap space.

## [](#NOTES)NOTES

           In order for user-space tools and applications to create tmpfs
           filesystems, the kernel must be configured with the CONFIG_TMPFS
           option.

           The tmpfs filesystem supports extended attributes (see xattr(7)),
           but user extended attributes are not permitted.

           An internal shared memory filesystem is used for System V shared
           memory (shmget(2)) and shared anonymous mappings (mmap(2) with the
           MAP_SHARED and MAP_ANONYMOUS flags).  This filesystem is available
           regardless of whether the kernel was configured with the
           CONFIG_TMPFS option.

           A tmpfs filesystem mounted at /dev/shm is used for the
           implementation of POSIX shared memory (shm_overview(7)) and POSIX
           semaphores (sem_overview(7)).

           The amount of memory consumed by all tmpfs filesystems is shown in
           the Shmem field of /proc/meminfo and in the shared field displayed
           by free(1).

           The tmpfs facility was formerly called shmfs.

## [](#SEE_ALSO)SEE ALSO

           df(1), du(1), memfd_create(2), mmap(2), set_mempolicy(2),
           shm_open(3), mount(8)

           The kernel source files Documentation/filesystems/tmpfs.rst and
           Documentation/admin-guide/mm/transhuge.rst.

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

    Linux man-pages 6.19            2026-02-08                       tmpfs(5)

------------------------------------------------------------------------

Pages that refer to this page: [fallocate(2)](../man2/fallocate.2.html),  [lseek(2)](../man2/lseek.2.html),  [madvise(2)](../man2/madvise.2.html),  [memfd_create(2)](../man2/memfd_create.2.html),  [mmap(2)](../man2/mmap.2.html),  [remap_file_pages(2)](../man2/remap_file_pages.2.html),  [seccomp_unotify(2)](../man2/seccomp_unotify.2.html),  [swapon(2)](../man2/swapon.2.html),  [UFFDIO_API(2const)](../man2/UFFDIO_API.2const.html),  [shm_open(3)](../man3/shm_open.3.html),  [filesystems(5)](../man5/filesystems.5.html),  [namespace.conf(5)](../man5/namespace.conf.5.html),  [proc_meminfo(5)](../man5/proc_meminfo.5.html),  [proc_pid_status(5)](../man5/proc_pid_status.5.html),  [proc_vmstat(5)](../man5/proc_vmstat.5.html),  [sysfs(5)](../man5/sysfs.5.html),  [cgroups(7)](../man7/cgroups.7.html),  [keyrings(7)](../man7/keyrings.7.html),  [shm_overview(7)](../man7/shm_overview.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [mount(8)](../man8/mount.8.html),  [systemd-fstab-generator(8)](../man8/systemd-fstab-generator.8.html)

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
