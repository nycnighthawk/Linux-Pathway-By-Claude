---
{"title": "mq_notify(3) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/mq_notify.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mq_notify(3) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [ATTRIBUTES](#ATTRIBUTES) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mq_notify(3)             Library Functions Manual            mq_notify(3)

## [](#NAME)NAME

           mq_notify - register for notification when a message is available

## [](#LIBRARY)LIBRARY

           Real-time library (librt, -lrt)

## [](#SYNOPSIS)SYNOPSIS

           #include <mqueue.h>
           #include <signal.h>           /* Definition of SIGEV_* constants */

           int mq_notify(mqd_t mqdes, const struct sigevent *sevp);

## [](#DESCRIPTION)DESCRIPTION

           mq_notify() allows the calling process to register or unregister
           for delivery of an asynchronous notification when a new message
           arrives on the empty message queue referred to by the message
           queue descriptor mqdes.

           The sevp argument is a pointer to a sigevent structure.  For the
           definition and general details of this structure, see
           sigevent(3type).

           If sevp is a non-null pointer, then mq_notify() registers the
           calling process to receive message notification.  The sigev_notify
           field of the sigevent structure to which sevp points specifies how
           notification is to be performed.  This field has one of the
           following values:

           SIGEV_NONE
                  A "null" notification: the calling process is registered as
                  the target for notification, but when a message arrives, no
                  notification is sent.

           SIGEV_SIGNAL
                  Notify the process by sending the signal specified in
                  sigev_signo.  See sigevent(3type) for general details.  The
                  si_code field of the siginfo_t structure will be set to
                  SI_MESGQ.  In addition, si_pid will be set to the PID of
                  the process that sent the message, and si_uid will be set
                  to the real user ID of the sending process.

           SIGEV_THREAD
                  Upon message delivery, invoke sigev_notify_function as if
                  it were the start function of a new thread.  See
                  sigevent(3type) for details.

           Only one process can be registered to receive notification from a
           message queue.

           If sevp is NULL, and the calling process is currently registered
           to receive notifications for this message queue, then the
           registration is removed; another process can then register to
           receive a message notification for this queue.

           Message notification occurs only when a new message arrives and
           the queue was previously empty.  If the queue was not empty at the
           time mq_notify() was called, then a notification will occur only
           after the queue is emptied and a new message arrives.

           If another process or thread is waiting to read a message from an
           empty queue using mq_receive(3), then any message notification
           registration is ignored: the message is delivered to the process
           or thread calling mq_receive(3), and the message notification
           registration remains in effect.

           Notification occurs once: after a notification is delivered, the
           notification registration is removed, and another process can
           register for message notification.  If the notified process wishes
           to receive the next notification, it can use mq_notify() to
           request a further notification.  This should be done before
           emptying all unread messages from the queue.  (Placing the queue
           in nonblocking mode is useful for emptying the queue of messages
           without blocking once it is empty.)

## [](#RETURN_VALUE)RETURN VALUE

           On success mq_notify() returns 0; on error, -1 is returned, with
           errno set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  The message queue descriptor specified in mqdes is invalid.

           EBUSY  Another process has already registered to receive
                  notification for this message queue.

           EINVAL sevp->sigev_notify is not one of the permitted values; or
                  sevp->sigev_notify is SIGEV_SIGNAL and sevp->sigev_signo is
                  not a valid signal number.

           ENOMEM Insufficient memory.

           POSIX.1-2008 says that an implementation may generate an EINVAL
           error if sevp is NULL, and the caller is not currently registered
           to receive notifications for the queue mqdes.

## [](#ATTRIBUTES)ATTRIBUTES

           For an explanation of the terms used in this section, see
           attributes(7).
           ┌──────────────────────────────────────┬───────────────┬─────────┐
           │ Interface                            │ Attribute     │ Value   │
           ├──────────────────────────────────────┼───────────────┼─────────┤
           │ mq_notify()                          │ Thread safety │ MT-Safe │
           └──────────────────────────────────────┴───────────────┴─────────┘

## [](#VERSIONS)VERSIONS

       C library/kernel differences
           In the glibc implementation, the mq_notify() library function is
           implemented on top of the system call of the same name.  When sevp
           is NULL, or specifies a notification mechanism other than
           SIGEV_THREAD, the library function directly invokes the system
           call.  For SIGEV_THREAD, much of the implementation resides within
           the library, rather than the kernel.  (This is necessarily so,
           since the thread involved in handling the notification is one that
           must be managed by the C library POSIX threads implementation.)
           The implementation involves the use of a raw netlink(7) socket and
           creates a new thread for each notification that is delivered to
           the process.

## [](#STANDARDS)STANDARDS

           POSIX.1-2008.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

## [](#EXAMPLES)EXAMPLES

           The following program registers a notification request for the
           message queue named in its command-line argument.  Notification is
           performed by creating a thread.  The thread executes a function
           which reads one message from the queue and then terminates the
           process.

       Program source
           #include <err.h>
           #include <mqueue.h>
           #include <pthread.h>
           #include <signal.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <unistd.h>

           static void                     /* Thread start function */
           tfunc(union sigval sv)
           {
               struct mq_attr attr;
               ssize_t nr;
               void *buf;
               mqd_t mqdes = *((mqd_t *) sv.sival_ptr);

               /* Determine max. msg size; allocate buffer to receive msg */

               if (mq_getattr(mqdes, &attr) == -1)
                   err(EXIT_FAILURE, "mq_getattr");
               buf = malloc(attr.mq_msgsize);
               if (buf == NULL)
                   err(EXIT_FAILURE, "malloc");

               nr = mq_receive(mqdes, buf, attr.mq_msgsize, NULL);
               if (nr == -1)
                   err(EXIT_FAILURE, "mq_receive");

               printf("Read %zd bytes from MQ\n", nr);
               free(buf);
               exit(EXIT_SUCCESS);         /* Terminate the process */
           }

           int
           main(int argc, char *argv[])
           {
               mqd_t mqdes;
               struct sigevent sev;

               if (argc != 2) {
                   fprintf(stderr, "Usage: %s <mq-name>\n", argv[0]);
                   exit(EXIT_FAILURE);
               }

               mqdes = mq_open(argv[1], O_RDONLY);
               if (mqdes == (mqd_t) -1)
                   err(EXIT_FAILURE, "mq_open");

               sev.sigev_notify = SIGEV_THREAD;
               sev.sigev_notify_function = tfunc;
               sev.sigev_notify_attributes = NULL;
               sev.sigev_value.sival_ptr = &mqdes;   /* Arg. to thread func.  */
               if (mq_notify(mqdes, &sev) == -1)
                   err(EXIT_FAILURE, "mq_notify");

               pause();    /* Process will be terminated by thread function */
           }

## [](#SEE_ALSO)SEE ALSO

           mq_close(3), mq_getattr(3), mq_open(3), mq_receive(3), mq_send(3),
           mq_unlink(3), mq_overview(7), sigevent(3type)

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

    Linux man-pages 6.19            2026-02-08                   mq_notify(3)

------------------------------------------------------------------------

Pages that refer to this page: [sigaction(2)](../man2/sigaction.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [mq_close(3)](../man3/mq_close.3.html),  [mq_getattr(3)](../man3/mq_getattr.3.html),  [mq_open(3)](../man3/mq_open.3.html),  [mq_receive(3)](../man3/mq_receive.3.html),  [mq_send(3)](../man3/mq_send.3.html),  [mq_unlink(3)](../man3/mq_unlink.3.html),  [sigevent(3type)](../man3/sigevent.3type.html),  [mq_overview(7)](../man7/mq_overview.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
