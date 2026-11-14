---
{"title": "mq_receive(3) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/mq_timedreceive.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mq_receive(3) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [ATTRIBUTES](#ATTRIBUTES) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mq_receive(3)            Library Functions Manual           mq_receive(3)

## [](#NAME)NAME

           mq_receive, mq_timedreceive - receive a message from a message
           queue

## [](#LIBRARY)LIBRARY

           Real-time library (librt, -lrt)

## [](#SYNOPSIS)SYNOPSIS

           #include <mqueue.h>

           ssize_t mq_receive(size_t msg_len;
                              mqd_t mqdes, char msg_ptr[msg_len],
                              size_t msg_len, unsigned int *msg_prio);

           #include <time.h>
           #include <mqueue.h>

           ssize_t mq_timedreceive(size_t msg_len;
                              mqd_t mqdes, char *restrict msg_ptr[msg_len],
                              size_t msg_len, unsigned int *restrict msg_prio,
                              const struct timespec *restrict abs_timeout);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           mq_timedreceive():
               _POSIX_C_SOURCE >= 200112L

## [](#DESCRIPTION)DESCRIPTION

           mq_receive() removes the oldest message with the highest priority
           from the message queue referred to by the message queue descriptor
           mqdes, and places it in the buffer pointed to by msg_ptr.  The
           msg_len argument specifies the size of the buffer pointed to by
           msg_ptr; this must be greater than or equal to the mq_msgsize
           attribute of the queue (see mq_getattr(3)).  If msg_prio is not
           NULL, then the buffer to which it points is used to return the
           priority associated with the received message.

           If the queue is empty, then, by default, mq_receive() blocks until
           a message becomes available, or the call is interrupted by a
           signal handler.  If the O_NONBLOCK flag is enabled for the message
           queue description, then the call instead fails immediately with
           the error EAGAIN.

           mq_timedreceive() behaves just like mq_receive(), except that if
           the queue is empty and the O_NONBLOCK flag is not enabled for the
           message queue description, then abs_timeout points to a structure
           which specifies how long the call will block.  This value is an
           absolute timeout in seconds and nanoseconds since the Epoch,
           1970-01-01 00:00:00 +0000 (UTC), specified in a timespec(3)
           structure.

           If no message is available, and the timeout has already expired by
           the time of the call, mq_timedreceive() returns immediately.

## [](#RETURN_VALUE)RETURN VALUE

           On success, mq_receive() and mq_timedreceive() return the number
           of bytes in the received message; on error, -1 is returned, with
           errno set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN The queue was empty, and the O_NONBLOCK flag was set for
                  the message queue description referred to by mqdes.

           EBADF  The descriptor specified in mqdes was invalid or not opened
                  for reading.

           EINTR  The call was interrupted by a signal handler; see
                  signal(7).

           EINVAL The call would have blocked, and abs_timeout was invalid,
                  either because tv_sec was less than zero, or because
                  tv_nsec was less than zero or greater than 1000 million.

           EMSGSIZE
                  msg_len was less than the mq_msgsize attribute of the
                  message queue.

           ETIMEDOUT
                  The call timed out before a message could be transferred.

## [](#ATTRIBUTES)ATTRIBUTES

           For an explanation of the terms used in this section, see
           attributes(7).
           ┌──────────────────────────────────────┬───────────────┬─────────┐
           │ Interface                            │ Attribute     │ Value   │
           ├──────────────────────────────────────┼───────────────┼─────────┤
           │ mq_receive(), mq_timedreceive()      │ Thread safety │ MT-Safe │
           └──────────────────────────────────────┴───────────────┴─────────┘

## [](#VERSIONS)VERSIONS

           On Linux, mq_timedreceive() is a system call, and mq_receive() is
           a library function layered on top of that system call.

## [](#STANDARDS)STANDARDS

           POSIX.1-2008.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

## [](#SEE_ALSO)SEE ALSO

           mq_close(3), mq_getattr(3), mq_notify(3), mq_open(3), mq_send(3),
           mq_unlink(3), timespec(3), mq_overview(7), time(7)

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

    Linux man-pages 6.19            2026-02-08                  mq_receive(3)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [mq_close(3)](../man3/mq_close.3.html),  [mq_getattr(3)](../man3/mq_getattr.3.html),  [mq_notify(3)](../man3/mq_notify.3.html),  [mq_open(3)](../man3/mq_open.3.html),  [mq_send(3)](../man3/mq_send.3.html),  [mq_unlink(3)](../man3/mq_unlink.3.html),  [mq_overview(7)](../man7/mq_overview.7.html),  [signal(7)](../man7/signal.7.html)

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
