---
{"title": "TCSETS(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/TCSETAF.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# TCSETS(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TCSETS(2const)                                             TCSETS(2const)

## [](#NAME)NAME

           TCGETS, TCSETS, TCSETSW, TCSETSF, TCGETS2, TCSETS2, TCSETSW2,
           TCSETSF2, TCGETA, TCSETA, TCSETAW, TCSETAF - get and set terminal
           attributes

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/termbits.h>  /* Definition of TC* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, TCGETS, struct termios *argp);
           int ioctl(int fd, TCSETS, const struct termios *argp);
           int ioctl(int fd, TCSETSW, const struct termios *argp);
           int ioctl(int fd, TCSETSF, const struct termios *argp);

           int ioctl(int fd, TCGETS2, struct termios2 *argp);
           int ioctl(int fd, TCSETS2, const struct termios2 *argp);
           int ioctl(int fd, TCSETSW2, const struct termios2 *argp);
           int ioctl(int fd, TCSETSF2, const struct termios2 *argp);

           [[deprecated]] int ioctl(int fd, TCGETA, struct termio *argp);
           [[deprecated]] int ioctl(int fd, TCSETA, const struct termio *argp);
           [[deprecated]] int ioctl(int fd, TCSETAW, const struct termio *argp);
           [[deprecated]] int ioctl(int fd, TCSETAF, const struct termio *argp);

           #include <asm/termbits.h>

           struct termios;
           struct termios2;
           struct [[deprecated]] termio;

## [](#DESCRIPTION)DESCRIPTION

           TCGETS Equivalent to tcgetattr(fd, argp).

                  Get the current serial port settings.

           TCSETS Equivalent to tcsetattr(fd, TCSANOW, argp).

                  Set the current serial port settings.

           TCSETSW
                  Equivalent to tcsetattr(fd, TCSADRAIN, argp).

                  Allow the output buffer to drain, and set the current
                  serial port settings.

           TCSETSF
                  Equivalent to tcsetattr(fd, TCSAFLUSH, argp).

                  Allow the output buffer to drain, discard pending input,
                  and set the current serial port settings.

           The following four ioctls are just like TCGETS, TCSETS, TCSETSW,
           TCSETSF, except that they take a struct termios2 * instead of a
           struct termios *.  If the structure member c_cflag contains the
           flag BOTHER, then the baud rate is stored in the structure members
           c_ispeed and c_ospeed as integer values.  These ioctls are not
           supported on all architectures.

                  TCGETS2
                  TCSETS2
                  TCSETSW2
                  TCSETSF2

           The following four ioctls are just like TCGETS, TCSETS, TCSETSW,
           TCSETSF, except that they take a struct termio * instead of a
           struct termios *.

                  TCGETA
                  TCSETA
                  TCSETAW
                  TCSETAF

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EPERM  Insufficient permission.

## [](#HISTORY)HISTORY

           TCGETS2
           TCSETS2
           TCSETSW2
           TCSETSF2
                  Linux 2.6.20.

## [](#CAVEATS)CAVEATS

           struct termios from <asm/termbits.h> is different and incompatible
           with struct termios from <termios.h>.  These ioctl calls require
           struct termios from <asm/termbits.h>.

## [](#EXAMPLES)EXAMPLES

           Get or set arbitrary baudrate on the serial port.

           /* SPDX-License-Identifier: GPL-2.0-or-later */

           #include <asm/termbits.h>
           #include <fcntl.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <sys/ioctl.h>
           #include <unistd.h>

           int
           main(int argc, char *argv[])
           {
           #if !defined BOTHER
               fprintf(stderr, "BOTHER is unsupported\n");
               /* Program may fallback to TCGETS/TCSETS with Bnnn constants */
               exit(EXIT_FAILURE);
           #else
               /* Declare tio structure, its type depends on supported ioctl */
           # if defined TCGETS2
               struct termios2 tio;
           # else
               struct termios tio;
           # endif
               int fd, rc;

               if (argc != 2 && argc != 3 && argc != 4) {
                   fprintf(stderr, "Usage: %s device [output [input] ]\n", argv[0]);
                   exit(EXIT_FAILURE);
               }

               fd = open(argv[1], O_RDWR | O_NONBLOCK | O_NOCTTY);
               if (fd < 0) {
                   perror("open");
                   exit(EXIT_FAILURE);
               }

               /* Get the current serial port settings via supported ioctl */
           # if defined TCGETS2
               rc = ioctl(fd, TCGETS2, &tio);
           # else
               rc = ioctl(fd, TCGETS, &tio);
           # endif
               if (rc) {
                   perror("TCGETS");
                   close(fd);
                   exit(EXIT_FAILURE);
               }

               /* Change baud rate when more arguments were provided */
               if (argc == 3 || argc == 4) {
                   /* Clear the current output baud rate and fill a new value */
                   tio.c_cflag &= ~CBAUD;
                   tio.c_cflag |= BOTHER;
                   tio.c_ospeed = atoi(argv[2]);

                   /* Clear the current input baud rate and fill a new value */
                   tio.c_cflag &= ~(CBAUD << IBSHIFT);
                   tio.c_cflag |= BOTHER << IBSHIFT;
                   /* When 4th argument is not provided reuse output baud rate */
                   tio.c_ispeed = (argc == 4) ? atoi(argv[3]) : atoi(argv[2]);

                   /* Set new serial port settings via supported ioctl */
           # if defined TCSETS2
                   rc = ioctl(fd, TCSETS2, &tio);
           # else
                   rc = ioctl(fd, TCSETS, &tio);
           # endif
                   if (rc) {
                       perror("TCSETS");
                       close(fd);
                       exit(EXIT_FAILURE);
                   }

                   /* And get new values which were really configured */
           # if defined TCGETS2
                   rc = ioctl(fd, TCGETS2, &tio);
           # else
                   rc = ioctl(fd, TCGETS, &tio);
           # endif
                   if (rc) {
                       perror("TCGETS");
                       close(fd);
                       exit(EXIT_FAILURE);
                   }
               }

               close(fd);

               printf("output baud rate: %u\n", tio.c_ospeed);
               printf("input baud rate: %u\n", tio.c_ispeed);

               exit(EXIT_SUCCESS);
           #endif
           }

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_tty(2), termios(7)

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

    Linux man-pages 6.19            2026-07-02                 TCSETS(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_tty(2)](../man2/ioctl_tty.2.html),  [TIOCSLCKTRMIOS(2const)](../man2/TIOCSLCKTRMIOS.2const.html)

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
