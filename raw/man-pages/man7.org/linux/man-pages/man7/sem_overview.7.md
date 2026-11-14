---
{"title": "sem_overview(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/sem_overview.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sem_overview(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sem_overview(7)      Miscellaneous Information Manual     sem_overview(7)

## [](#NAME)NAME

           sem_overview - overview of POSIX semaphores

## [](#DESCRIPTION)DESCRIPTION

           POSIX semaphores allow processes and threads to synchronize their
           actions.

           A semaphore is an integer whose value is never allowed to fall
           below zero.  Two operations can be performed on semaphores:
           increment the semaphore value by one (sem_post(3)); and decrement
           the semaphore value by one (sem_wait(3)).  If the value of a
           semaphore is currently zero, then a sem_wait(3) operation will
           block until the value becomes greater than zero.

           POSIX semaphores come in two forms: named semaphores and unnamed
           semaphores.

           Named semaphores
                  A named semaphore is identified by a name of the form
                  /somename; that is, a null-terminated string of up to
                  NAME_MAX-4 (i.e., 251) characters consisting of an initial
                  slash, followed by one or more characters, none of which
                  are slashes.  Two processes can operate on the same named
                  semaphore by passing the same name to sem_open(3).

                  The sem_open(3) function creates a new named semaphore or
                  opens an existing named semaphore.  After the semaphore has
                  been opened, it can be operated on using sem_post(3) and
                  sem_wait(3).  When a process has finished using the
                  semaphore, it can use sem_close(3) to close the semaphore.
                  When all processes have finished using the semaphore, it
                  can be removed from the system using sem_unlink(3).

           Unnamed semaphores (memory-based semaphores)
                  An unnamed semaphore does not have a name.  Instead the
                  semaphore is placed in a region of memory that is shared
                  between multiple threads (a thread-shared semaphore) or
                  processes (a process-shared semaphore).  A thread-shared
                  semaphore is placed in an area of memory shared between the
                  threads of a process, for example, a global variable.  A
                  process-shared semaphore must be placed in a shared memory
                  region (e.g., a System V shared memory segment created
                  using shmget(2), or a POSIX shared memory object built
                  created using shm_open(3)).

                  Before being used, an unnamed semaphore must be initialized
                  using sem_init(3).  It can then be operated on using
                  sem_post(3) and sem_wait(3).  When the semaphore is no
                  longer required, and before the memory in which it is
                  located is deallocated, the semaphore should be destroyed
                  using sem_destroy(3).

           The remainder of this section describes some specific details of
           the Linux implementation of POSIX semaphores.

       Versions
           Before Linux 2.6, Linux supported only unnamed, thread-shared
           semaphores.  On a system with Linux 2.6 and a glibc that provides
           the NPTL threading implementation, a complete implementation of
           POSIX semaphores is provided.

       Persistence
           POSIX named semaphores have kernel persistence: if not removed by
           sem_unlink(3), a semaphore will exist until the system is shut
           down.

       Linking
           Programs using the POSIX semaphores API must be compiled with cc
           -pthread to link against the real-time library, librt.

       Accessing named semaphores via the filesystem
           On Linux, named semaphores are created in a virtual filesystem,
           normally mounted under /dev/shm, with names of the form
           sem.somename.  (This is the reason that semaphore names are
           limited to NAME_MAX-4 rather than NAME_MAX characters.)

           Since Linux 2.6.19, ACLs can be placed on files under this
           directory, to control object permissions on a per-user and per-
           group basis.

## [](#NOTES)NOTES

           System V semaphores (semget(2), semop(2), etc.) are an older
           semaphore API.  POSIX semaphores provide a simpler, and better
           designed interface than System V semaphores; on the other hand
           POSIX semaphores are less widely available (especially on older
           systems) than System V semaphores.

## [](#EXAMPLES)EXAMPLES

           An example of the use of various POSIX semaphore functions is
           shown in sem_wait(3).

## [](#SEE_ALSO)SEE ALSO

           sem_close(3), sem_destroy(3), sem_getvalue(3), sem_init(3),
           sem_open(3), sem_post(3), sem_unlink(3), sem_wait(3), pthreads(7),
           shm_overview(7)

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

    Linux man-pages 6.19            2026-02-08                sem_overview(7)

------------------------------------------------------------------------

Pages that refer to this page: [eventfd(2)](../man2/eventfd.2.html),  [execve(2)](../man2/execve.2.html),  [intro(2)](../man2/intro.2.html),  [semctl(2)](../man2/semctl.2.html),  [semget(2)](../man2/semget.2.html),  [semop(2)](../man2/semop.2.html),  [sem_close(3)](../man3/sem_close.3.html),  [sem_destroy(3)](../man3/sem_destroy.3.html),  [sem_getvalue(3)](../man3/sem_getvalue.3.html),  [sem_init(3)](../man3/sem_init.3.html),  [sem_open(3)](../man3/sem_open.3.html),  [sem_post(3)](../man3/sem_post.3.html),  [sem_unlink(3)](../man3/sem_unlink.3.html),  [sem_wait(3)](../man3/sem_wait.3.html),  [tmpfs(5)](../man5/tmpfs.5.html),  [shm_overview(7)](../man7/shm_overview.7.html),  [sysvipc(7)](../man7/sysvipc.7.html)

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
