---
{"title": "ipcrm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ipcrm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ipcrm(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPCRM(1)                      User Commands                      IPCRM(1)

## [](#NAME)NAME

           ipcrm - remove certain IPC resources

## [](#SYNOPSIS)SYNOPSIS

           ipcrm [options]

           ipcrm [shm|msg|sem] ID ...

## [](#DESCRIPTION)DESCRIPTION

           ipcrm removes POSIX and System V inter-process communication (IPC)
           objects and associated data structures from the system. In order
           to delete such objects, you must be superuser, or the creator or
           owner of the object.

           POSIX and System V IPC objects are of three types: shared memory,
           message queues, and semaphores. Deletion of a message queue or
           semaphore object is immediate (regardless of whether any process
           still holds an IPC identifier for the object). A shared memory
           object is only removed after all currently attached processes have
           detached (shmdt(2)) the object from their virtual address space.

           Two syntax styles are supported. The old Linux historical syntax
           specifies a three-letter keyword indicating which class of object
           is to be deleted, followed by one or more IPC identifiers for
           objects of this type.

           The SUS-compliant syntax allows the specification of zero or more
           objects of all three types in a single command line, with objects
           specified either by key or by identifier (see below). Both keys
           and identifiers may be specified in decimal, hexadecimal
           (specified with an initial '0x' or '0X'), or octal (specified with
           an initial '0').

           The details of the removes are described in shmctl(2),
           shm_unlink(3), msgctl(2), mq_unlink(3), semctl(2), and
           sem_unlink(3). The identifiers and keys can be found by using
           lsipc(1) or ipcs(1).

## [](#OPTIONS)OPTIONS

           -a, --all [shm] [pshm] [msg] [pmsg] [sem] [psem]
               Remove all resources. When an option argument is provided, the
               removal is performed only for the specified resource types.

               Warning! Do not use -a if you are unsure how the software
               using the resources might react to missing objects. Some
               programs create these resources at startup and may not have
               any code to deal with an unexpected disappearance.

           -M, --shmem-key shmkey
               Remove the shared memory segment created with shmkey after the
               last detach is performed.

           -m, --shmem-id shmid
               Remove the shared memory segment identified by shmid after the
               last detach is performed.

           --posix-shmem name
               Remove the POSIX shared memory segment created with name.

           -Q, --queue-key msgkey
               Remove the message queue created with msgkey.

           -q, --queue-id msgid
               Remove the message queue identified by msgid.

           --posix-mqueue name
               Remove the POSIX message queue created with name.

           -S, --semaphore-key semkey
               Remove the semaphore created with semkey.

           -s, --semaphore-id semid
               Remove the semaphore identified by semid.

           --posix-semaphore name
               Remove the POSIX named semaphore created with name.

           -v, --verbose
               Enable verbose messaging.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#NOTES)NOTES

           In its first Linux implementation, ipcrm used the deprecated
           syntax shown in the second line of the SYNOPSIS. Functionality
           present in other *nix implementations of ipcrm has since been
           added, namely the ability to delete resources by key (not just
           identifier), and to respect the same command-line syntax. For
           backward compatibility the previous syntax is still supported.

## [](#SEE_ALSO)SEE ALSO

           ipcmk(1), ipcs(1), lsipc(1), msgctl(2), mq_unlink(3), msgget(2),
           semctl(2), semget(2), sem_unlink(3), shmctl(2), shmdt(2),
           shmget(2), shm_unlink(3), ftok(3), sysvipc(7)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The ipcrm command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                       IPCRM(1)

------------------------------------------------------------------------

Pages that refer to this page: [ipcmk(1)](../man1/ipcmk.1.html),  [ipcs(1)](../man1/ipcs.1.html),  [lsipc(1)](../man1/lsipc.1.html),  [pcp-ipcs(1)](../man1/pcp-ipcs.1.html),  [sysvipc(7)](../man7/sysvipc.7.html)

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
