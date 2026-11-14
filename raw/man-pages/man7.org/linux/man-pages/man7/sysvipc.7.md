---
{"title": "sysvipc(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/sysvipc.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysvipc(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    sysvipc(7)           Miscellaneous Information Manual          sysvipc(7)

## [](#NAME)NAME

           sysvipc - System V interprocess communication mechanisms

## [](#DESCRIPTION)DESCRIPTION

           System V IPC is the name given to three interprocess communication
           mechanisms that are widely available on UNIX systems: message
           queues, semaphore, and shared memory.

       Message queues
           System V message queues allow data to be exchanged in units called
           messages.  Each message can have an associated priority.  POSIX
           message queues provide an alternative API for achieving the same
           result; see mq_overview(7).

           The System V message queue API consists of the following system
           calls:

           msgget(2)
                  Create a new message queue or obtain the ID of an existing
                  message queue.  This call returns an identifier that is
                  used in the remaining APIs.

           msgsnd(2)
                  Add a message to a queue.

           msgrcv(2)
                  Remove a message from a queue.

           msgctl(2)
                  Perform various control operations on a queue, including
                  deletion.

       Semaphore sets
           System V semaphores allow processes to synchronize their actions.
           System V semaphores are allocated in groups called sets; each
           semaphore in a set is a counting semaphore.  POSIX semaphores
           provide an alternative API for achieving the same result; see
           sem_overview(7).

           The System V semaphore API consists of the following system calls:

           semget(2)
                  Create a new set or obtain the ID of an existing set.  This
                  call returns an identifier that is used in the remaining
                  APIs.

           semop(2)
                  Perform operations on the semaphores in a set.

           semctl(2)
                  Perform various control operations on a set, including
                  deletion.

       Shared memory segments
           System V shared memory allows processes to share a region a memory
           (a "segment").  POSIX shared memory is an alternative API for
           achieving the same result; see shm_overview(7).

           The System V shared memory API consists of the following system
           calls:

           shmget(2)
                  Create a new segment or obtain the ID of an existing
                  segment.  This call returns an identifier that is used in
                  the remaining APIs.

           shmat(2)
                  Attach an existing shared memory object into the calling
                  process's address space.

           shmdt(2)
                  Detach a segment from the calling process's address space.

           shmctl(2)
                  Perform various control operations on a segment, including
                  deletion.

       IPC namespaces
           For a discussion of the interaction of System V IPC objects and
           IPC namespaces, see ipc_namespaces(7).

## [](#SEE_ALSO)SEE ALSO

           ipcmk(1), ipcrm(1), ipcs(1), lsipc(1), ipc(2), msgctl(2),
           msgget(2), msgrcv(2), msgsnd(2), semctl(2), semget(2), semop(2),
           shmat(2), shmctl(2), shmdt(2), shmget(2), ftok(3),
           ipc_namespaces(7)

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

    Linux man-pages 6.19            2026-02-08                     sysvipc(7)

------------------------------------------------------------------------

Pages that refer to this page: [ipcmk(1)](../man1/ipcmk.1.html),  [ipcrm(1)](../man1/ipcrm.1.html),  [ipcs(1)](../man1/ipcs.1.html),  [lsipc(1)](../man1/lsipc.1.html),  [intro(2)](../man2/intro.2.html),  [ipc(2)](../man2/ipc.2.html),  [msgctl(2)](../man2/msgctl.2.html),  [msgget(2)](../man2/msgget.2.html),  [msgop(2)](../man2/msgop.2.html),  [semctl(2)](../man2/semctl.2.html),  [semget(2)](../man2/semget.2.html),  [semop(2)](../man2/semop.2.html),  [shmctl(2)](../man2/shmctl.2.html),  [shmget(2)](../man2/shmget.2.html),  [shmop(2)](../man2/shmop.2.html),  [ftok(3)](../man3/ftok.3.html),  [proc_sysvipc(5)](../man5/proc_sysvipc.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [ipc_namespaces(7)](../man7/ipc_namespaces.7.html)

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
