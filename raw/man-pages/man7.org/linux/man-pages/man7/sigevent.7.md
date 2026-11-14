---
{"title": "sigevent(3type) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/sigevent.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sigevent(3type) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sigevent(3type)                                           sigevent(3type)

## [](#NAME)NAME

           sigevent, sigval - structure for notification from asynchronous
           routines

## [](#SYNOPSIS)SYNOPSIS

           #include <signal.h>

           struct sigevent {
               int             sigev_notify;  /* Notification type */
               int             sigev_signo;   /* Signal number */
               union sigval    sigev_value;   /* Data passed with notification */

               typeof(void (union sigval))  *sigev_notify_function;
                                              /* Notification function
                                                 (SIGEV_THREAD) */
               pthread_attr_t *sigev_notify_attributes;
                                              /* Notification attributes */

               /* Linux only: */
               pid_t           sigev_notify_thread_id;
                                              /* ID of thread to signal
                                                 (SIGEV_THREAD_ID) */
           };

           union sigval {                     /* Data passed with notification */
               int             sival_int;     /* Integer value */
               void           *sival_ptr;     /* Pointer value */
           };

## [](#DESCRIPTION)DESCRIPTION

       sigevent
           The sigevent structure is used by various APIs to describe the way
           a process is to be notified about an event (e.g., completion of an
           asynchronous request, expiration of a timer, or the arrival of a
           message).

           The definition shown in the SYNOPSIS is approximate: some of the
           fields in the sigevent structure may be defined as part of a
           union.  Programs should employ only those fields relevant to the
           value specified in sigev_notify.

           The sigev_notify field specifies how notification is to be
           performed.  This field can have one of the following values:

           SIGEV_NONE
                  A "null" notification: don't do anything when the event
                  occurs.

           SIGEV_SIGNAL
                  Notify the process by sending the signal specified in
                  sigev_signo.

                  If the signal is caught with a signal handler that was
                  registered using the sigaction(2) SA_SIGINFO flag, then the
                  following fields are set in the siginfo_t structure that is
                  passed as the second argument of the handler:

                  si_code
                         This field is set to a value that depends on the API
                         delivering the notification.

                  si_signo
                         This field is set to the signal number (i.e., the
                         same value as in sigev_signo).

                  si_value
                         This field is set to the value specified in
                         sigev_value.

                  Depending on the API, other fields may also be set in the
                  siginfo_t structure.

                  The same information is also available if the signal is
                  accepted using sigwaitinfo(2).

           SIGEV_THREAD
                  Notify the process by invoking sigev_notify_function "as
                  if" it were the start function of a new thread.  (Among the
                  implementation possibilities here are that each timer
                  notification could result in the creation of a new thread,
                  or that a single thread is created to receive all
                  notifications.)  The function is invoked with sigev_value
                  as its sole argument.  If sigev_notify_attributes is not
                  NULL, it should point to a pthread_attr_t structure that
                  defines attributes for the new thread (see
                  pthread_attr_init(3)).

           SIGEV_THREAD_ID (Linux-specific)
                  Currently used only by POSIX timers; see timer_create(2).

       sigval
           Data passed with a signal.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-1996.

           <aio.h> and <time.h> define sigevent since POSIX.1-2008.

## [](#NOTES)NOTES

           The following headers also provide sigevent: <aio.h>, <mqueue.h>,
           and <time.h>.

## [](#SEE_ALSO)SEE ALSO

           timer_create(2), getaddrinfo_a(3), lio_listio(3), mq_notify(3),
           pthread_sigqueue(3), sigqueue(3), aiocb(3type), siginfo_t(3type)

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

    Linux man-pages 6.19            2026-02-08                sigevent(3type)

------------------------------------------------------------------------

Pages that refer to this page: [timer_create(2)](../man2/timer_create.2.html),  [aio_cancel(3)](../man3/aio_cancel.3.html),  [aio_fsync(3)](../man3/aio_fsync.3.html),  [aio_read(3)](../man3/aio_read.3.html),  [aio_write(3)](../man3/aio_write.3.html),  [getaddrinfo_a(3)](../man3/getaddrinfo_a.3.html),  [lio_listio(3)](../man3/lio_listio.3.html),  [mq_notify(3)](../man3/mq_notify.3.html),  [aio(7)](../man7/aio.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [signal(7)](../man7/signal.7.html)

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
