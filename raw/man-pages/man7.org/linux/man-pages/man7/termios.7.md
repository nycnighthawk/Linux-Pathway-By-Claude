---
{"title": "termios(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/termios.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# termios(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    termios(7)           Miscellaneous Information Manual          termios(7)

## [](#NAME)NAME

           termios - terminal input/output settings

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <termios.h>

## [](#DESCRIPTION)DESCRIPTION

           The termios functions describe a general terminal interface that
           is provided to control asynchronous communications ports.

       Retrieving and changing terminal settings
           tcgetattr(3)
           tcsetattr(3)

       Canonical and noncanonical mode
           See termios(3type).

       Raw mode
           cfmakeraw(3)

       Line control
           tcsendbreak(3)
           tcdrain(3)
           tcflush(3)
           tcflow(3)

       Line speed
           cfgetospeed(3)
           cfsetospeed(3)
           cfgetispeed(3)
           cfsetispeed(3)
           cfsetspeed(3)

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, BSD.

## [](#SEE_ALSO)SEE ALSO

           reset(1), setterm(1), stty(1), tput(1), tset(1), tty(1),
           ioctl_console(2), ioctl_tty(2), cc_t(3type), speed_t(3type),
           tcflag_t(3type), setserial(8)

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

    Linux man-pages 6.19            2026-07-02                     termios(7)

------------------------------------------------------------------------

Pages that refer to this page: [FIONREAD(2const)](../man2/FIONREAD.2const.html),  [ioctl_console(2)](../man2/ioctl_console.2.html),  [ioctl_tty(2)](../man2/ioctl_tty.2.html),  [setpgid(2)](../man2/setpgid.2.html),  [TCSETS(2const)](../man2/TCSETS.2const.html),  [TCXONC(2const)](../man2/TCXONC.2const.html),  [cc_t(3type)](../man3/cc_t.3type.html),  [cfmakeraw(3)](../man3/cfmakeraw.3.html),  [\_exit(3)](../man3/_exit.3.html),  [stdin(3)](../man3/stdin.3.html),  [tcdrain(3)](../man3/tcdrain.3.html),  [tcflow(3)](../man3/tcflow.3.html),  [tcflush(3)](../man3/tcflush.3.html),  [tcsendbreak(3)](../man3/tcsendbreak.3.html),  [tcsetattr(3)](../man3/tcsetattr.3.html),  [termios(3type)](../man3/termios.3type.html),  [tty(4)](../man4/tty.4.html),  [pty(7)](../man7/pty.7.html),  [termio(7)](../man7/termio.7.html)

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
