---
{"title": "ioctl_pipe(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_pipe.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_pipe(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioctl_pipe(2)              System Calls Manual              ioctl_pipe(2)

## [](#NAME)NAME

           ioctl_pipe - ioctl() operations for general notification mechanism

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/watch_queue.h>  /* Definition of IOC_WATCH_QUEUE_* */
           #include <sys/ioctl.h>

           int ioctl(int pipefd, IOC_WATCH_QUEUE_SET_SIZE, int size);
           int ioctl(int pipefd, IOC_WATCH_QUEUE_SET_FILTER,
                     struct watch_notification_filter *filter);

## [](#DESCRIPTION)DESCRIPTION

           The following ioctl(2) operations are provided to set up general
           notification queue parameters.  The notification queue is built on
           the top of a pipe(2) opened with the O_NOTIFICATION_PIPE flag.

           IOC_WATCH_QUEUE_SET_SIZE (since Linux 5.8)
                  Preallocates the pipe buffer memory so that it can fit size
                  notification messages.  Currently, size must be between 1
                  and 512.

           IOC_WATCH_QUEUE_SET_FILTER (since Linux 5.8)
                  Watch queue filter can limit events that are received.
                  Filters are passed in a struct watch_notification_filter
                  and each filter is described by a struct
                  watch_notification_type_filter structure.

                      struct watch_notification_filter {
                              __u32   nr_filters;
                              __u32   __reserved;
                              struct watch_notification_type_filter filters[];
                      };

                      struct watch_notification_type_filter {
                              __u32   type;
                              __u32   info_filter;
                              __u32   info_mask;
                              __u32   subtype_filter[8];
                      };

## [](#SEE_ALSO)SEE ALSO

           pipe(2), ioctl(2)

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

    Linux man-pages 6.19            2026-02-08                  ioctl_pipe(2)

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
