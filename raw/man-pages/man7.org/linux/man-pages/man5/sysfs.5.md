---
{"title": "sysfs(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/sysfs.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysfs(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sysfs(5)                   File Formats Manual                   sysfs(5)

## [](#NAME)NAME

           sysfs - a filesystem for exporting kernel objects

## [](#DESCRIPTION)DESCRIPTION

           The sysfs filesystem is a pseudo-filesystem which provides an
           interface to kernel data structures.  (More precisely, the files
           and directories in sysfs provide a view of the kobject structures
           defined internally within the kernel.)  The files under sysfs
           provide information about devices, kernel modules, filesystems,
           and other kernel components.

           The sysfs filesystem is commonly mounted at /sys.  Typically, it
           is mounted automatically by the system, but it can also be mounted
           manually using a command such as:

               mount -t sysfs sysfs /sys

           Many of the files in the sysfs filesystem are read-only, but some
           files are writable, allowing kernel variables to be changed.  To
           avoid redundancy, symbolic links are heavily used to connect
           entries across the filesystem tree.

       Files and directories
           The following list describes some of the files and directories
           under the /sys hierarchy.

           /sys/block
                  This subdirectory contains one symbolic link for each block
                  device that has been discovered on the system.  The
                  symbolic links point to corresponding directories under
                  /sys/devices.

           /sys/bus
                  This directory contains one subdirectory for each of the
                  bus types in the kernel.  Inside each of these directories
                  are two subdirectories:

                  devices
                         This subdirectory contains symbolic links to entries
                         in /sys/devices that correspond to the devices
                         discovered on this bus.

                  drivers
                         This subdirectory contains one subdirectory for each
                         device driver that is loaded on this bus.

           /sys/class
                  This subdirectory contains a single layer of further
                  subdirectories for each of the device classes that have
                  been registered on the system (e.g., terminals, network
                  devices, block devices, graphics devices, sound devices,
                  and so on).  Inside each of these subdirectories are
                  symbolic links for each of the devices in this class.
                  These symbolic links refer to entries in the /sys/devices
                  directory.

           /sys/class/net
                  Each of the entries in this directory is a symbolic link
                  representing one of the real or virtual networking devices
                  that are visible in the network namespace of the process
                  that is accessing the directory.  Each of these symbolic
                  links refers to entries in the /sys/devices directory.

           /sys/dev
                  This directory contains two subdirectories block/ and
                  char/, corresponding, respectively, to the block and
                  character devices on the system.  Inside each of these
                  subdirectories are symbolic links with names of the form
                  major-ID:minor-ID, where the ID values correspond to the
                  major and minor ID of a specific device.  Each symbolic
                  link points to the sysfs directory for a device.  The
                  symbolic links inside /sys/dev thus provide an easy way to
                  look up the sysfs interface using the device IDs returned
                  by a call to stat(2) (or similar).

                  The following shell session shows an example from /sys/dev:

                      $ stat -c "%t %T" /dev/null;
                      1 3
                      $ readlink /sys/dev/char/1\:3;
                      ../../devices/virtual/mem/null
                      $ ls -Fd /sys/devices/virtual/mem/null;
                      /sys/devices/virtual/mem/null/
                      $ ls -d1 /sys/devices/virtual/mem/null/*;
                      /sys/devices/virtual/mem/null/dev
                      /sys/devices/virtual/mem/null/power/
                      /sys/devices/virtual/mem/null/subsystem@
                      /sys/devices/virtual/mem/null/uevent

           /sys/devices
                  This is a directory that contains a filesystem
                  representation of the kernel device tree, which is a
                  hierarchy of device structures within the kernel.

           /sys/firmware
                  This subdirectory contains interfaces for viewing and
                  manipulating firmware-specific objects and attributes.

           /sys/fs
                  This directory contains subdirectories for some
                  filesystems.  A filesystem will have a subdirectory here
                  only if it chose to explicitly create the subdirectory.

           /sys/fs/cgroup
                  This directory conventionally is used as a mount point for
                  a tmpfs(5) filesystem containing mount points for
                  cgroups(7) filesystems.

           /sys/fs/smackfs
                  The directory contains configuration files for the SMACK
                  LSM.  See the kernel source file
                  Documentation/admin-guide/LSM/Smack.rst.

           /sys/hypervisor
                  [To be documented]

           /sys/kernel
                  This subdirectory contains various files and subdirectories
                  that provide information about the running kernel.

           /sys/kernel/cgroup/
                  For information about the files in this directory, see
                  cgroups(7).

           /sys/kernel/debug/tracing
                  Mount point for the tracefs filesystem used by the kernel's
                  ftrace facility.  (For information on ftrace, see the
                  kernel source file Documentation/trace/ftrace.rst.)

           /sys/kernel/mm
                  This subdirectory contains various files and subdirectories
                  that provide information about the kernel's memory
                  management subsystem.

           /sys/kernel/mm/hugepages
                  This subdirectory contains one subdirectory for each of the
                  huge page sizes that the system supports.  The subdirectory
                  name indicates the huge page size (e.g., hugepages-2048kB).
                  Within each of these subdirectories is a set of files that
                  can be used to view and (in some cases) change settings
                  associated with that huge page size.  For further
                  information, see the kernel source file
                  Documentation/admin-guide/mm/hugetlbpage.rst.

           /sys/module
                  This subdirectory contains one subdirectory for each module
                  that is loaded into the kernel.  The name of each directory
                  is the name of the module.  In each of the subdirectories,
                  there may be following files:

                  coresize
                         [to be documented]

                  initsize
                         [to be documented]

                  initstate
                         [to be documented]

                  refcnt [to be documented]

                  srcversion
                         [to be documented]

                  taint  [to be documented]

                  uevent [to be documented]

                  version
                         [to be documented]

                  In each of the subdirectories, there may be following
                  subdirectories:

                  drivers
                         [To be documented]

                  holders
                         [To be documented]

                  notes  [To be documented]

                  parameters
                         This directory contains one file for each module
                         parameter, with each file containing the value of
                         the corresponding parameter.  Some of these files
                         are writable, allowing the parameters to be changed.

                  sections
                         This subdirectories contains files with information
                         about module sections.  This information is mainly
                         used for debugging.

                  [To be documented]

           /sys/power
                  [To be documented]

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.0.

## [](#NOTES)NOTES

           This manual page is incomplete, possibly inaccurate, and is the
           kind of thing that needs to be updated very often.

## [](#SEE_ALSO)SEE ALSO

           proc(5), udev(7)

           P. Mochel (2005).  The sysfs filesystem.  Proceedings of the 2005
           Ottawa Linux Symposium.

           The kernel source file Documentation/filesystems/sysfs.rst and
           various other files in Documentation/ABI and
           Documentation/*/sysfs.rst.

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

    Linux man-pages 6.19            2026-02-08                       sysfs(5)

------------------------------------------------------------------------

Pages that refer to this page: [madvise(2)](../man2/madvise.2.html),  [sysfs(2)](../man2/sysfs.2.html),  [filesystems(5)](../man5/filesystems.5.html),  [proc(5)](../man5/proc.5.html),  [network_namespaces(7)](../man7/network_namespaces.7.html)

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
