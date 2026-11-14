---
{"title": "ipcs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ipcs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ipcs(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMING TO](#CONFORMING_TO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPCS(1)                       User Commands                       IPCS(1)

## [](#NAME)NAME

           ipcs - show information on IPC facilities

## [](#SYNOPSIS)SYNOPSIS

           ipcs [options]

## [](#DESCRIPTION)DESCRIPTION

           ipcs shows information on System V inter-process communication
           facilities. By default it shows information about all three
           resources: shared memory segments, message queues, and semaphore
           arrays.

## [](#OPTIONS)OPTIONS

           -i, --id id
               Show full details on just the one resource element identified
               by id. This option needs to be combined with one of the three
               resource options: -m, -q or -s.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

       Resource options
           -m, --shmems
               Write information about active shared memory segments.

           -q, --queues
               Write information about active message queues.

           -s, --semaphores
               Write information about active semaphore sets.

           -a, --all
               Write information about all three resources (default).

       Output formats
           Of these options only one takes effect: the last one specified.

           -c, --creator
               Show creator and owner.

           -l, --limits
               Show resource limits.

           -p, --pid
               Show PIDs of creator and last operator.

           -t, --time
               Write time information. The time of the last control operation
               that changed the access permissions for all facilities, the
               time of the last msgsnd(2) and msgrcv(2) operations on message
               queues, the time of the last shmat(2) and shmdt(2) operations
               on shared memory, and the time of the last semop(2) operation
               on semaphores.

           -u, --summary
               Show status summary.

       Representation
           These affect only the -l (--limits) option.

           -b, --bytes
               Print sizes in bytes rather than in human-readable form.

               By default, sizes are shown in units that are powers of 1024
               bytes. The formal abbreviations for these units (KiB, MiB,
               GiB, ...) are further shortened to just their first letter: K,
               M, G, ....

           --human
               Print sizes in human-readable format.

## [](#CONFORMING_TO)CONFORMING TO

           The Linux ipcs utility is not fully compatible to the POSIX ipcs
           utility. The Linux version does not support the POSIX -a, -b and
           -o options, but does support the -l and -u options not defined by
           POSIX. A portable application shall not use the -a, -b, -o, -l,
           and -u options.

## [](#NOTES)NOTES

           The current implementation of ipcs obtains information about
           available IPC resources by parsing the files in /proc/sysvipc.
           Before util-linux version v2.23, an alternate mechanism was used:
           the IPC_STAT command of msgctl(2), semctl(2), and shmctl(2). This
           mechanism is also used in later util-linux versions in the case
           where /proc is unavailable. A limitation of the IPC_STAT mechanism
           is that it can only be used to retrieve information about IPC
           resources for which the user has read permission.

## [](#AUTHORS)AUTHORS

           Krishna Balasubramanian <balasub@cis.ohio-state.edu>

## [](#SEE_ALSO)SEE ALSO

           ipcmk(1), ipcrm(1), msgrcv(2), msgsnd(2), semget(2), semop(2),
           shmat(2), shmdt(2), shmget(2), sysvipc(7)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The ipcs command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                        IPCS(1)

------------------------------------------------------------------------

Pages that refer to this page: [ipcmk(1)](../man1/ipcmk.1.html),  [ipcrm(1)](../man1/ipcrm.1.html),  [lsipc(1)](../man1/lsipc.1.html),  [msgctl(2)](../man2/msgctl.2.html),  [semctl(2)](../man2/semctl.2.html),  [semget(2)](../man2/semget.2.html),  [shmctl(2)](../man2/shmctl.2.html),  [proc_sysvipc(5)](../man5/proc_sysvipc.5.html),  [sysvipc(7)](../man7/sysvipc.7.html)

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
