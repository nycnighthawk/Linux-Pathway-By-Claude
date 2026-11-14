---
{"title": "slabinfo(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slabinfo.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slabinfo(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    slabinfo(5)                File Formats Manual                slabinfo(5)

## [](#NAME)NAME

           slabinfo - kernel slab allocator statistics

## [](#SYNOPSIS)SYNOPSIS

           cat /proc/slabinfo

## [](#DESCRIPTION)DESCRIPTION

           Frequently used objects in the Linux kernel (buffer heads, inodes,
           dentries, etc.)  have their own cache.  The file /proc/slabinfo
           gives statistics on these caches.  The following (edited) output
           shows an example of the contents of this file:

           $ sudo cat /proc/slabinfo;
           slabinfo - version: 2.1
           # name    <active_objs> <num_objs> <objsize> <objperslab> <pagesperslab> ...
           sigqueue      100  100  160   25  1 : tunables  0  0  0 : slabdata   4   4  0
           sighand_cache 355   405 2112  15  8 : tunables  0  0  0 : slabdata  27  27  0
           kmalloc-8192   96   96  8192   4  8 : tunables  0  0  0 : slabdata  24  24  0
           ...

           The first line of output includes a version number, which allows
           an application that is reading the file to handle changes in the
           file format.  (See VERSIONS, below.)  The next line lists the
           names of the columns in the remaining lines.

           Each of the remaining lines displays information about a specified
           cache.  Following the cache name, the output shown in each line
           shows three components for each cache:

           •  statistics

           •  tunables

           •  slabdata

           The statistics are as follows:

           active_objs
                  The number of objects that are currently active (i.e., in
                  use).

           num_objs
                  The total number of allocated objects (i.e., objects that
                  are both in use and not in use).

           objsize
                  The size of objects in this slab, in bytes.

           objperslab
                  The number of objects stored in each slab.

           pagesperslab
                  The number of pages allocated for each slab.

           The tunables entries in each line show tunable parameters for the
           corresponding cache.  When using the default SLUB allocator, there
           are no tunables, the /proc/slabinfo file is not writable, and the
           value 0 is shown in these fields.  When using the older SLAB
           allocator, the tunables for a particular cache can be set by
           writing lines of the following form to /proc/slabinfo:

               # echo 'name limit batchcount sharedfactor' > /proc/slabinfo;

           Here, name is the cache name, and limit, batchcount, and
           sharedfactor are integers defining new values for the
           corresponding tunables.  The limit value should be a positive
           value, batchcount should be a positive value that is less than or
           equal to limit, and sharedfactor should be nonnegative.  If any of
           the specified values is invalid, the cache settings are left
           unchanged.

           The tunables entries in each line contain the following fields:

           limit  The maximum number of objects that will be cached.

           batchcount
                  On SMP systems, this specifies the number of objects to
                  transfer at one time when refilling the available object
                  list.

           sharedfactor
                  [To be documented]

           The slabdata entries in each line contain the following fields:

           active_slabs
                  The number of active slabs.

           nums_slabs
                  The total number of slabs.

           sharedavail
                  [To be documented]

           Note that because of object alignment and slab cache overhead,
           objects are not normally packed tightly into pages.  Pages with
           even one in-use object are considered in-use and cannot be freed.

           Kernels configured with CONFIG_DEBUG_SLAB will also have
           additional statistics fields in each line, and the first line of
           the file will contain the string "(statistics)".  The statistics
           field include: the high water mark of active objects; the number
           of times objects have been allocated; the number of times the
           cache has grown (new pages added to this cache); the number of
           times the cache has been reaped (unused pages removed from this
           cache); and the number of times there was an error allocating new
           pages to this cache.

## [](#VERSIONS)VERSIONS

           The /proc/slabinfo file first appeared in Linux 2.1.23.  The file
           is versioned, and over time there have been a number of versions
           with different layouts:

           1.0    Present throughout the Linux 2.2.x kernel series.

           1.1    Present in the Linux 2.4.x kernel series.

           1.2    A format that was briefly present in the Linux 2.5
                  development series.

           2.0    Present in Linux 2.6.x kernels up to and including Linux
                  2.6.9.

           2.1    The current format, which first appeared in Linux 2.6.10.

## [](#NOTES)NOTES

           Only root can read and (if the kernel was configured with
           CONFIG_SLAB) write the /proc/slabinfo file.

           The total amount of memory allocated to the SLAB/SLUB cache is
           shown in the Slab field of /proc/meminfo.

## [](#SEE_ALSO)SEE ALSO

           slabtop(1)

           The kernel source file Documentation/mm/slab.rst and
           tools/mm/slabinfo.c.

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

    Linux man-pages 6.19            2026-02-08                    slabinfo(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc(5)](../man5/proc.5.html),  [proc_meminfo(5)](../man5/proc_meminfo.5.html),  [proc_slabinfo(5)](../man5/proc_slabinfo.5.html),  [vmstat(8)](../man8/vmstat.8.html)

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
