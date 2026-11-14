---
{"title": "TIOCMSET(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/tiocmiwait.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# TIOCMSET(2const) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TIOCMSET(2const)                                         TIOCMSET(2const)

## [](#NAME)NAME

           TIOCMGET, TIOCMSET, TIOCMBIC, TIOCMBIS, TIOCMIWAIT, TIOCGICOUNT -
           modem control

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/termbits.h>  /* Definition of TIOC* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, TIOCMGET, int *argp);
           int ioctl(int fd, TIOCMSET, const int *argp);
           int ioctl(int fd, TIOCMBIC, const int *argp);
           int ioctl(int fd, TIOCMBIS, const int *argp);
           int ioctl(int fd, TIOCMIWAIT, int arg);
           int ioctl(int fd, TIOCGICOUNT, struct serial_icounter_struct *argp);

           #include <linux/serial.h>

           struct serial_icounter_struct;

## [](#DESCRIPTION)DESCRIPTION

           TIOCMGET
                  Get the status of modem bits.

           TIOCMSET
                  Set the status of modem bits.

           TIOCMBIC
                  Clear the indicated modem bits.

           TIOCMBIS
                  Set the indicated modem bits.

           The following bits are used by the above ioctls:

           TIOCM_LE    DSR (data set ready/line enable)
           TIOCM_DTR   DTR (data terminal ready)
           TIOCM_RTS   RTS (request to send)
           TIOCM_ST    Secondary TXD (transmit)
           TIOCM_SR    Secondary RXD (receive)
           TIOCM_CTS   CTS (clear to send)
           TIOCM_CAR   DCD (data carrier detect)
           TIOCM_CD    see TIOCM_CAR
           TIOCM_RNG   RNG (ring)
           TIOCM_RI    see TIOCM_RNG
           TIOCM_DSR   DSR (data set ready)

           TIOCMIWAIT
                  Wait for any of the 4 modem bits (DCD, RI, DSR, CTS) to
                  change.  The bits of interest are specified as a bit mask
                  in arg, by ORing together any of the bit values, TIOCM_RNG,
                  TIOCM_DSR, TIOCM_CD, and TIOCM_CTS.  The caller should use
                  TIOCGICOUNT to see which bit has changed.

           TIOCGICOUNT
                  Get counts of input serial line interrupts (DCD, RI, DSR,
                  CTS).  The counts are written to the serial_icounter_struct
                  structure pointed to by argp.

                  Note: both 1->0 and 0->1 transitions are counted, except
                  for RI, where only 0->1 transitions are counted.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#EXAMPLES)EXAMPLES

           Check the condition of DTR on the serial port.

           #include <asm/termbits.h>
           #include <fcntl.h>
           #include <stdio.h>
           #include <sys/ioctl.h>
           #include <unistd.h>

           int
           main(void)
           {
               int fd, serial;

               fd = open("/dev/ttyS0", O_RDONLY);
               ioctl(fd, TIOCMGET, &serial);
               if (serial & TIOCM_DTR)
                   puts("TIOCM_DTR is set");
               else
                   puts("TIOCM_DTR is not set");
               close(fd);
           }

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_tty(2)

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

    Linux man-pages 6.19            2026-02-08               TIOCMSET(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_tty(2)](../man2/ioctl_tty.2.html)

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
