---
{"title": "ioctl_eventpoll(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/EPIOCGPARAMS.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_eventpoll(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioctl_eventpoll(2)         System Calls Manual         ioctl_eventpoll(2)

## [](#NAME)NAME

           ioctl_eventpoll, EPIOCSPARAMS, EPIOCGPARAMS - ioctl() operations
           for epoll file descriptors

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/epoll.h>  /* Definition of EPIOC* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, EPIOCSPARAMS, const struct epoll_params *argp);
           int ioctl(int fd, EPIOCGPARAMS, struct epoll_params *argp);

           #include <sys/epoll.h>

           struct epoll_params {
               uint32_t  busy_poll_usecs;   /* Number of usecs to busy poll */
               uint16_t  busy_poll_budget;  /* Max packets per poll */
               uint8_t   prefer_busy_poll;  /* Boolean preference  */

               /* pad the struct to a multiple of 64bits */
               uint8_t   __pad;             /* Must be zero */
           };

## [](#DESCRIPTION)DESCRIPTION

           EPIOCSPARAMS
                  Set the epoll_params structure to configure the operation
                  of epoll.  Refer to the structure description below to
                  learn what configuration is supported.

           EPIOCGPARAMS
                  Get the current epoll_params configuration settings.

           All operations documented above must be performed on an epoll file
           descriptor, which can be obtained with a call to epoll_create(2)
           or epoll_create1(2).

       The epoll_params structure
           argp.busy_poll_usecs denotes the number of microseconds that the
           network stack will busy poll.  During this time period, the
           network device will be polled repeatedly for packets.  This value
           cannot exceed INT_MAX.

           argp.busy_poll_budget denotes the maximum number of packets that
           the network stack will retrieve on each poll attempt.  This value
           cannot exceed NAPI_POLL_WEIGHT (which is 64 as of Linux 6.9),
           unless the process is run with CAP_NET_ADMIN.

           argp.prefer_busy_poll is a boolean field and must be either 0
           (disabled) or 1 (enabled).  If enabled, this indicates to the
           network stack that busy poll is the preferred method of processing
           network data and the network stack should give the application the
           opportunity to busy poll.  Without this option, very busy systems
           may continue to do network processing via the normal method of
           IRQs triggering softIRQ and NAPI.

           argp.__pad must be zero.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On failure, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EOPNOTSUPP
                  The kernel was not compiled with busy poll support.

           EINVAL fd is not a valid file descriptor.

           EINVAL argp.__pad is not zero.

           EINVAL argp.busy_poll_usecs exceeds INT_MAX.

           EINVAL argp.prefer_busy_poll is not 0 or 1.

           EPERM  The process is being run without CAP_NET_ADMIN and the
                  specified argp.busy_poll_budget exceeds NAPI_POLL_WEIGHT.

           EFAULT argp is an invalid address.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 6.9, glibc 2.40.

## [](#EXAMPLES)EXAMPLES

           /* Code to set the epoll params to enable busy polling */

           int epollfd = epoll_create1(0);
           struct epoll_params params;

           if (epollfd == -1) {
               perror("epoll_create1");
               exit(EXIT_FAILURE);
           }

           memset(&params, 0, sizeof(struct epoll_params));

           params.busy_poll_usecs = 25;
           params.busy_poll_budget = 8;
           params.prefer_busy_poll = 1;

           if (ioctl(epollfd, EPIOCSPARAMS, &params) == -1) {
               perror("ioctl");
               exit(EXIT_FAILURE);
           }

           /* Code to show how to retrieve the current settings */

           memset(&params, 0, sizeof(struct epoll_params));

           if (ioctl(epollfd, EPIOCGPARAMS, &params) == -1) {
               perror("ioctl");
               exit(EXIT_FAILURE);
           }

           /* params struct now contains the current parameters */

           fprintf(stderr, "epoll usecs: %lu\n", params.busy_poll_usecs);
           fprintf(stderr, "epoll packet budget: %u\n", params.busy_poll_budget);
           fprintf(stderr, "epoll prefer busy poll: %u\n", params.prefer_busy_poll);

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), epoll_create(2), epoll_create1(2), epoll(7)

           linux.git/Documentation/networking/napi.rst

           linux.git/Documentation/admin-guide/sysctl/net.rst

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

    Linux man-pages 6.19            2026-07-15             ioctl_eventpoll(2)

------------------------------------------------------------------------

Pages that refer to this page: [epoll_create(2)](../man2/epoll_create.2.html),  [epoll_ctl(2)](../man2/epoll_ctl.2.html),  [ioctl(2)](../man2/ioctl.2.html),  [epoll(7)](../man7/epoll.7.html)

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
