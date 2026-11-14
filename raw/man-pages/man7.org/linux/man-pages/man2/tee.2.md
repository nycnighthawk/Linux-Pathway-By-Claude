---
{"title": "tee(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/tee.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tee(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    tee(2)                     System Calls Manual                     tee(2)

## [](#NAME)NAME

           tee - duplicating pipe content

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE         /* See feature_test_macros(7) */
           #include <fcntl.h>

           ssize_t tee(int fd_in, int fd_out, size_t size, unsigned int flags);

## [](#DESCRIPTION)DESCRIPTION

           tee() duplicates up to size bytes of data from the pipe referred
           to by the file descriptor fd_in to the pipe referred to by the
           file descriptor fd_out.  It does not consume the data that is
           duplicated from fd_in; therefore, that data can be copied by a
           subsequent splice(2).

           flags is a bit mask that is composed by ORing together zero or
           more of the following values:

           SPLICE_F_MOVE
                  Currently has no effect for tee(); see splice(2).

           SPLICE_F_NONBLOCK
                  Do not block on I/O; see splice(2) for further details.

           SPLICE_F_MORE
                  Currently has no effect for tee(), but may be implemented
                  in the future; see splice(2).

           SPLICE_F_GIFT
                  Unused for tee(); see vmsplice(2).

## [](#RETURN_VALUE)RETURN VALUE

           Upon successful completion, tee() returns the number of bytes that
           were duplicated between the input and output.  A return value of 0
           means that there was no data to transfer, and it would not make
           sense to block, because there are no writers connected to the
           write end of the pipe referred to by fd_in.

           On error, tee() returns -1 and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN SPLICE_F_NONBLOCK was specified in flags or one of the file
                  descriptors had been marked as nonblocking (O_NONBLOCK),
                  and the operation would block.

           EINVAL fd_in or fd_out does not refer to a pipe; or fd_in and
                  fd_out refer to the same pipe.

           ENOMEM Out of memory.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.17, glibc 2.5.

## [](#NOTES)NOTES

           Conceptually, tee() copies the data between the two pipes.  In
           reality no real data copying takes place though: under the covers,
           tee() assigns data to the output by merely grabbing a reference to
           the input.

## [](#EXAMPLES)EXAMPLES

           The example below implements a basic tee(1) program using the
           tee() system call.  Here is an example of its use:

               $ date | ./a.out out.log | cat;
               Tue Oct 28 10:06:00 CET 2014
               $ cat out.log;
               Tue Oct 28 10:06:00 CET 2014

       Program source

           #define _GNU_SOURCE
           #include <errno.h>
           #include <fcntl.h>
           #include <limits.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <sys/types.h>
           #include <unistd.h>

           int
           main(int argc, char *argv[])
           {
               int      fd;
               ssize_t  size, ssize;

               if (argc != 2) {
                   fprintf(stderr, "Usage: %s <file>\n", argv[0]);
                   exit(EXIT_FAILURE);
               }

               fd = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC, 0644);
               if (fd == -1) {
                   perror("open");
                   exit(EXIT_FAILURE);
               }

               for (;;) {
                   /*
                    * tee stdin to stdout.
                    */
                   size = tee(STDIN_FILENO, STDOUT_FILENO,
                             INT_MAX, SPLICE_F_NONBLOCK);
                   if (size < 0) {
                       if (errno == EAGAIN)
                           continue;
                       perror("tee");
                       exit(EXIT_FAILURE);
                   }
                   if (size == 0)
                       break;

                   /*
                    * Consume stdin by splicing it to a file.
                    */
                   while (size > 0) {
                       ssize = splice(STDIN_FILENO, NULL, fd, NULL,
                                     size, SPLICE_F_MOVE);
                       if (ssize < 0) {
                           perror("splice");
                           exit(EXIT_FAILURE);
                       }
                       size -= ssize;
                   }
               }

               close(fd);
               exit(EXIT_SUCCESS);
           }

## [](#SEE_ALSO)SEE ALSO

           splice(2), vmsplice(2), pipe(7)

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

    Linux man-pages 6.19            2026-02-08                         tee(2)

------------------------------------------------------------------------

Pages that refer to this page: [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [pipe(2)](../man2/pipe.2.html),  [splice(2)](../man2/splice.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [vmsplice(2)](../man2/vmsplice.2.html),  [io_uring_prep_tee(3)](../man3/io_uring_prep_tee.3.html),  [pipe(7)](../man7/pipe.7.html)

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
