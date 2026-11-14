---
{"title": "msgget(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/msgget.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# msgget(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    msgget(2)                  System Calls Manual                  msgget(2)

## [](#NAME)NAME

           msgget - get a System V message queue identifier

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/msg.h>

           int msgget(key_t key, int msgflg);

## [](#DESCRIPTION)DESCRIPTION

           The msgget() system call returns the System V message queue
           identifier associated with the value of the key argument.  It may
           be used either to obtain the identifier of a previously created
           message queue (when msgflg is zero and key does not have the value
           IPC_PRIVATE), or to create a new set.

           A new message queue is created if key has the value IPC_PRIVATE or
           key isn't IPC_PRIVATE, no message queue with the given key key
           exists, and IPC_CREAT is specified in msgflg.

           If msgflg specifies both IPC_CREAT and IPC_EXCL and a message
           queue already exists for key, then msgget() fails with errno set
           to EEXIST.  (This is analogous to the effect of the combination
           O_CREAT | O_EXCL for open(2).)

           Upon creation, the least significant bits of the argument msgflg
           define the permissions of the message queue.  These permission
           bits have the same format and semantics as the permissions
           specified for the mode argument of open(2).  (The execute
           permissions are not used.)

           If a new message queue is created, then its associated data
           structure msqid_ds (see msgctl(2)) is initialized as follows:

           •  msg_perm.cuid and msg_perm.uid are set to the effective user ID
              of the calling process.

           •  msg_perm.cgid and msg_perm.gid are set to the effective group
              ID of the calling process.

           •  The least significant 9 bits of msg_perm.mode are set to the
              least significant 9 bits of msgflg.

           •  msg_qnum, msg_lspid, msg_lrpid, msg_stime, and msg_rtime are
              set to 0.

           •  msg_ctime is set to the current time.

           •  msg_qbytes is set to the system limit MSGMNB.

           If the message queue already exists the permissions are verified,
           and a check is made to see if it is marked for destruction.

## [](#RETURN_VALUE)RETURN VALUE

           On success, msgget() returns the message queue identifier (a
           nonnegative integer).  On failure, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES A message queue exists for key, but the calling process
                  does not have permission to access the queue, and does not
                  have the CAP_IPC_OWNER capability in the user namespace
                  that governs its IPC namespace.

           EEXIST IPC_CREAT and IPC_EXCL were specified in msgflg, but a
                  message queue already exists for key.

           ENOENT No message queue exists for key and msgflg did not specify
                  IPC_CREAT.

           ENOMEM A message queue has to be created but the system does not
                  have enough memory for the new data structure.

           ENOSPC A message queue has to be created but the system limit for
                  the maximum number of message queues (MSGMNI) would be
                  exceeded.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024 XSI.

## [](#HISTORY)HISTORY

           SVr4, SUSv1, POSIX.1-2001 XSI.

       Linux
           Until Linux 2.3.20, Linux would return EIDRM for a msgget() on a
           message queue scheduled for deletion.

## [](#NOTES)NOTES

           IPC_PRIVATE isn't a flag field but a key_t type.  If this special
           value is used for key, the system call ignores everything but the
           least significant 9 bits of msgflg and creates a new message queue
           (on success).

           The following is a system limit on message queue resources
           affecting a msgget() call:

           MSGMNI System-wide limit on the number of message queues.  Before
                  Linux 3.19, the default value for this limit was calculated
                  using a formula based on available system memory.  Since
                  Linux 3.19, the default value is 32,000.  On Linux, this
                  limit can be read and modified via /proc/sys/kernel/msgmni.

## [](#BUGS)BUGS

           The name choice IPC_PRIVATE was perhaps unfortunate, IPC_NEW would
           more clearly show its function.

## [](#SEE_ALSO)SEE ALSO

           msgctl(2), msgrcv(2), msgsnd(2), ftok(3), capabilities(7),
           mq_overview(7), sysvipc(7)

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

    Linux man-pages 6.19            2026-02-11                      msgget(2)

------------------------------------------------------------------------

Pages that refer to this page: [ipcrm(1)](../man1/ipcrm.1.html),  [ipc(2)](../man2/ipc.2.html),  [msgctl(2)](../man2/msgctl.2.html),  [msgop(2)](../man2/msgop.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [umask(2)](../man2/umask.2.html),  [ftok(3)](../man3/ftok.3.html),  [mq_overview(7)](../man7/mq_overview.7.html),  [sysvipc(7)](../man7/sysvipc.7.html)

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
