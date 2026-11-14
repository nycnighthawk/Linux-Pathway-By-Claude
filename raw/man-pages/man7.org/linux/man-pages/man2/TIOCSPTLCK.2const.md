---
{"title": "TIOCPKT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/TIOCSPTLCK.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# TIOCPKT(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TIOCPKT(2const)                                           TIOCPKT(2const)

## [](#NAME)NAME

           TIOCPKT, TIOCGPKT, TIOCSPTLCK, TIOCGPTLCK, TIOCGPTPEER -
           pseudoterminal ioctls

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/termbits.h>  /* Definition of TIOC* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, TIOCPKT, const int *mode);
           int ioctl(int fd, TIOCPKT, int *mode);

           int ioctl(int fd, TIOCSPTLCK, const int *lock);
           int ioctl(int fd, TIOCGPTLCK, int *lock);

           int ioctl(int fd, TIOCGPTPEER, int flags);

## [](#DESCRIPTION)DESCRIPTION

           TIOCPKT
                  Enable (when *mode is nonzero) or disable packet mode.  Can
                  be applied to the master side of a pseudoterminal only (and
                  will return ENOTTY otherwise).  In packet mode, each
                  subsequent read(2) will return a packet that either
                  contains a single nonzero control byte, or has a single
                  byte containing zero ('\0') followed by data written on the
                  slave side of the pseudoterminal.  If the first byte is not
                  TIOCPKT_DATA (0), it is an OR of one or more of the
                  following bits:

                  TIOCPKT_FLUSHREAD    The read queue for the
                                       terminal is flushed.
                  TIOCPKT_FLUSHWRITE   The write queue for the
                                       terminal is flushed.
                  TIOCPKT_STOP         Output to the terminal
                                       is stopped.
                  TIOCPKT_START        Output to the terminal
                                       is restarted.
                  TIOCPKT_DOSTOP       The start and stop
                                       characters are ^S/^Q.
                  TIOCPKT_NOSTOP       The start and stop
                                       characters are not
                                       ^S/^Q.

                  While packet mode is in use, the presence of control status
                  information to be read from the master side may be detected
                  by  a select(2) for exceptional conditions or a poll(2) for
                  the POLLPRI event.

                  This mode is used by rlogin(1) and rlogind(8) to  implement
                  a   remote-echoed,  locally  ^S/^Q  flow-controlled  remote
                  login.

           TIOCGPKT
                  Return the current packet mode setting in the integer
                  pointed to by mode.

           TIOCSPTLCK
                  Set (if *lock is nonzero) or remove (if *lock is zero) the
                  lock on the pseudoterminal slave device.  (See also
                  unlockpt(3).)

           TIOCGPTLCK
                  Place the current lock state of the pseudoterminal slave
                  device in the location pointed to by lock.

           TIOCGPTPEER
                  Given a file descriptor in fd that refers to a
                  pseudoterminal master, open (with the given open(2)-style
                  flags) and return a new file descriptor that refers to the
                  peer pseudoterminal slave device.  This operation can be
                  performed regardless of whether the pathname of the slave
                  device is accessible through the calling process's mount
                  namespace.

                  Security-conscious programs interacting with namespaces may
                  wish to use this operation rather than open(2) with the
                  pathname returned by ptsname(3), and similar library
                  functions that have insecure APIs.  (For example, confusion
                  can occur in some cases using ptsname(3) with a pathname
                  where a devpts filesystem has been mounted in a different
                  mount namespace.)

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           ENOTTY

## [](#HISTORY)HISTORY

           TIOCGPKT
                  Linux 3.8.

           TIOCGPTLCK
                  Linux 3.8.

           TIOCGPTPEER
                  Linux 4.13.

           The BSD ioctls TIOCSTOP, TIOCSTART, TIOCUCNTL, and TIOCREMOTE have
           not been implemented under Linux.

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

    Linux man-pages 6.19            2026-02-08                TIOCPKT(2const)

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
