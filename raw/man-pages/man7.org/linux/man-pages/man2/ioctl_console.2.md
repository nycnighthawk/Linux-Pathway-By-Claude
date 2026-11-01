---
{"title": "ioctl_console(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_console.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_console(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioctl_console(2)           System Calls Manual           ioctl_console(2)

## [](#NAME)NAME

           ioctl_console - ioctls for console terminal and virtual consoles

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/ioctl.h>

           int ioctl(int fd, unsigned long op, ...);

## [](#DESCRIPTION)DESCRIPTION

           The following Linux-specific ioctl(2) operations are supported for
           console terminals and virtual consoles.

           KDGETLED(2const)
           KDSETLED(2const)
           KDGKBLED(2const)
           KDSKBLED(2const)
           KDGKBTYPE(2const)
           KDADDIO(2const)
           KDDELIO(2const)
           KDENABIO(2const)
           KDDISABIO(2const)
           KDSETMODE(2const)
           KDGETMODE(2const)
           KDMKTONE(2const)
           KIOCSOUND(2const)
           GIO_CMAP(2const)
           PIO_CMAP(2const)
           GIO_FONT(2const)
           GIO_FONTX(2const)
           PIO_FONT(2const)
           PIO_FONTX(2const)
           PIO_FONTRESET(2const)
           GIO_SCRNMAP(2const)
           GIO_UNISCRNMAP(2const)
           PIO_SCRNMAP(2const)
           PIO_UNISCRNMAP(2const)
           GIO_UNIMAP(2const)
           PIO_UNIMAP(2const)
           PIO_UNIMAPCLR(2const)
           KDGKBMODE(2const)
           KDSKBMODE(2const)
           KDGKBMETA(2const)
           KDSKBMETA(2const)
           KDGKBENT(2const)
           KDSKBENT(2const)
           KDGKBSENT(2const)
           KDSKBSENT(2const)
           KDGKBDIACR(2const)
           KDGETKEYCODE(2const)
           KDSETKEYCODE(2const)
           KDSIGACCEPT(2const)
                  See ioctl_kd(2).

           TIOCLINUX(2const)

           VT_OPENQRY(2const)
           VT_GETMODE(2const)
           VT_SETMODE(2const)
           VT_GETSTATE(2const)
           VT_RELDISP(2const)
           VT_ACTIVATE(2const)
           VT_WAITACTIVE(2const)
           VT_DISALLOCATE(2const)
           VT_RESIZE(2const)
           VT_RESIZEX(2const)
                  See ioctl_vt(2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned (except where indicated).  On failure,
           -1 is returned, and errno is set to indicate the error.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#CAVEATS)CAVEATS

           Do not regard this man page as documentation of the Linux console
           ioctls.  This is provided for the curious only, as an alternative
           to reading the source.  Ioctl's are undocumented Linux internals,
           liable to be changed without warning.  (And indeed, this page more
           or less describes the situation as of kernel version 1.1.94; there
           are many minor and not-so-minor differences with earlier
           versions.)

           Very often, ioctls are introduced for communication between the
           kernel and one particular well-known program (fdisk, hdparm,
           setserial, tunelp, loadkeys, selection, setfont, etc.), and their
           behavior will be changed when required by this particular program.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), TIOCLINUX(2const), ioctl_kd(2), ioctl_vt(2),
           dumpkeys(1), kbd_mode(1), loadkeys(1), mknod(1), setleds(1),
           setmetamode(1), execve(2), fcntl(2), ioctl_tty(2), ioperm(2),
           console_codes(4), mt(4), sd(4), tty(4), ttyS(4), vcs(4), vcsa(4),
           charsets(7), termios(7), mapscrn(8), resizecons(8), setfont(8)

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

    Linux man-pages 6.19            2026-07-02               ioctl_console(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl(2)](../man2/ioctl.2.html),  [ioctl_kd(2)](../man2/ioctl_kd.2.html),  [ioctl_tty(2)](../man2/ioctl_tty.2.html),  [ioctl_vt(2)](../man2/ioctl_vt.2.html),  [TIOCLINUX(2const)](../man2/TIOCLINUX.2const.html),  [console_codes(4)](../man4/console_codes.4.html),  [tty(4)](../man4/tty.4.html),  [vcs(4)](../man4/vcs.4.html),  [termios(7)](../man7/termios.7.html)

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
