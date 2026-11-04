---
{"title": "ioctl_tty(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_tty.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_tty(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioctl_tty(2)               System Calls Manual               ioctl_tty(2)

## [](#NAME)NAME

           ioctl_tty - ioctls for terminals and serial lines

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/termbits.h>  /* Definition of constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, int op, ...);

## [](#DESCRIPTION)DESCRIPTION

           The ioctl(2) call for terminals and serial ports accepts many
           possible operation arguments.  Most require a third argument, of
           varying type, here called argp or arg.

           Use of ioctl() makes for nonportable programs.  Use the POSIX
           interface described in termios(7) whenever possible.

       Get and set terminal attributes
           TCGETS(2const)
           TCSETS(2const)
           TCSETSW(2const)
           TCSETSF(2const)

           TCGETS2(2const)
           TCSETS2(2const)
           TCSETSW2(2const)
           TCSETSF2(2const)

           TCGETA(2const)
           TCSETA(2const)
           TCSETAW(2const)
           TCSETAF(2const)

       Locking the termios structure
           TIOCGLCKTRMIOS(2const)
           TIOCSLCKTRMIOS(2const)

       Get and set window size
           TIOCGWINSZ(2const)
           TIOCSWINSZ(2const)

       Sending a break
           TCSBRK(2const)
           TCSBRKP(2const)
           TIOCSBRK(2const)
           TIOCCBRK(2const)

       Software flow control
           TCXONC(2const)

       Buffer count and flushing
           FIONREAD(2const)
           TIOCINQ(2const)
           TIOCOUTQ(2const)
           TCFLSH(2const)
           TIOCSERGETLSR(2const)

       Faking input
           TIOCSTI(2const)

       Redirecting console output
           TIOCCONS(2const)

       Controlling terminal
           TIOCSCTTY(2const)
           TIOCNOTTY(2const)

       Process group and session ID
           TIOCGPGRP(2const)
           TIOCSPGRP(2const)
           TIOCGSID(2const)

       Exclusive mode
           TIOCEXCL(2const)
           TIOCGEXCL(2const)
           TIOCNXCL(2const)

       Line discipline
           TIOCGETD(2const)
           TIOCSETD(2const)

       Pseudoterminal ioctls
           TIOCPKT(2const)
           TIOCGPKT(2const)

           TIOCSPTLCK(2const)
           TIOCGPTLCK(2const)

           TIOCGPTPEER(2const)

       Modem control
           TIOCMGET(2const)
           TIOCMSET(2const)
           TIOCMBIC(2const)
           TIOCMBIS(2const)

           TIOCMIWAIT(2const)

           TIOCGICOUNT(2const)

       Marking a line as local
           TIOCGSOFTCAR(2const)
           TIOCSSOFTCAR(2const)

       Linux-specific
           For the TIOCLINUX(2const) ioctl, see ioctl_console(2).

       Kernel debugging
           TIOCTTYGSTRUCT(2const)

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ldattach(8), ioctl_console(2), termios(7), pty(7)

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

    Linux man-pages 6.19            2026-07-02                   ioctl_tty(2)

------------------------------------------------------------------------

Pages that refer to this page: [FIONREAD(2const)](../man2/FIONREAD.2const.html),  [ioctl(2)](../man2/ioctl.2.html),  [ioctl_console(2)](../man2/ioctl_console.2.html),  [poll(2)](../man2/poll.2.html),  [TCSBRK(2const)](../man2/TCSBRK.2const.html),  [TCSETS(2const)](../man2/TCSETS.2const.html),  [TCXONC(2const)](../man2/TCXONC.2const.html),  [TIOCCONS(2const)](../man2/TIOCCONS.2const.html),  [TIOCEXCL(2const)](../man2/TIOCEXCL.2const.html),  [TIOCMSET(2const)](../man2/TIOCMSET.2const.html),  [TIOCPKT(2const)](../man2/TIOCPKT.2const.html),  [TIOCSCTTY(2const)](../man2/TIOCSCTTY.2const.html),  [TIOCSETD(2const)](../man2/TIOCSETD.2const.html),  [TIOCSLCKTRMIOS(2const)](../man2/TIOCSLCKTRMIOS.2const.html),  [TIOCSPGRP(2const)](../man2/TIOCSPGRP.2const.html),  [TIOCSSOFTCAR(2const)](../man2/TIOCSSOFTCAR.2const.html),  [TIOCSTI(2const)](../man2/TIOCSTI.2const.html),  [TIOCTTYGSTRUCT(2const)](../man2/TIOCTTYGSTRUCT.2const.html),  [cfsetspeed(3)](../man3/cfsetspeed.3.html),  [termios(3type)](../man3/termios.3type.html),  [tty(4)](../man4/tty.4.html),  [pty(7)](../man7/pty.7.html),  [termio(7)](../man7/termio.7.html),  [termios(7)](../man7/termios.7.html)

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
