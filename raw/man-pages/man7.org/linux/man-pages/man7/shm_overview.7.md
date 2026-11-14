---
{"title": "shm_overview(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/shm_overview.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# shm_overview(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    shm_overview(7)      Miscellaneous Information Manual     shm_overview(7)

## [](#NAME)NAME

           shm_overview - overview of POSIX shared memory

## [](#DESCRIPTION)DESCRIPTION

           The POSIX shared memory API allows processes to communicate
           information by sharing a region of memory.

           The interfaces employed in the API are:

           shm_open(3)
                  Create and open a new object, or open an existing object.
                  This is analogous to open(2).  The call returns a file
                  descriptor for use by the other interfaces listed below.

           ftruncate(2)
                  Set the size of the shared memory object.  (A newly created
                  shared memory object has a length of zero.)

           mmap(2)
                  Map the shared memory object into the virtual address space
                  of the calling process.

           munmap(2)
                  Unmap the shared memory object from the virtual address
                  space of the calling process.

           shm_unlink(3)
                  Remove a shared memory object name.

           close(2)
                  Close the file descriptor allocated by shm_open(3) when it
                  is no longer needed.

           fstat(2)
                  Obtain a stat structure that describes the shared memory
                  object.  Among the information returned by this call are
                  the object's size (st_size), permissions (st_mode), owner
                  (st_uid), and group (st_gid).

           fchown(2)
                  To change the ownership of a shared memory object.

           fchmod(2)
                  To change the permissions of a shared memory object.

       Versions
           POSIX shared memory is supported since Linux 2.4 and glibc 2.2.

       Persistence
           POSIX shared memory objects have kernel persistence: a shared
           memory object will exist until the system is shut down, or until
           all processes have unmapped the object and it has been deleted
           with shm_unlink(3)

       Linking
           Programs using the POSIX shared memory API must be compiled with
           cc -lrt to link against the real-time library, librt.

       Accessing shared memory objects via the filesystem
           On Linux, shared memory objects are created in a (tmpfs(5))
           virtual filesystem, normally mounted under /dev/shm.  Since Linux
           2.6.19, Linux supports the use of access control lists (ACLs) to
           control the permissions of objects in the virtual filesystem.

## [](#NOTES)NOTES

           Typically, processes must synchronize their access to a shared
           memory object, using, for example, POSIX semaphores.

           System V shared memory (shmget(2), shmop(2), etc.) is an older
           shared memory API.  POSIX shared memory provides a simpler, and
           better designed interface; on the other hand POSIX shared memory
           is somewhat less widely available (especially on older systems)
           than System V shared memory.

## [](#SEE_ALSO)SEE ALSO

           fchmod(2), fchown(2), fstat(2), ftruncate(2), memfd_create(2),
           mmap(2), mprotect(2), munmap(2), shmget(2), shmop(2), shm_open(3),
           shm_unlink(3), sem_overview(7)

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

    Linux man-pages 6.19            2025-05-17                shm_overview(7)

------------------------------------------------------------------------

Pages that refer to this page: [intro(2)](../man2/intro.2.html),  [mmap(2)](../man2/mmap.2.html),  [shmget(2)](../man2/shmget.2.html),  [shmop(2)](../man2/shmop.2.html),  [shm_open(3)](../man3/shm_open.3.html),  [tmpfs(5)](../man5/tmpfs.5.html),  [sem_overview(7)](../man7/sem_overview.7.html),  [sysvipc(7)](../man7/sysvipc.7.html)

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
