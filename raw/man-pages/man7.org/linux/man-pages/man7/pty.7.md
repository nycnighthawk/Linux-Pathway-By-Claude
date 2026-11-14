---
{"title": "pty(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/pty.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pty(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    pty(7)               Miscellaneous Information Manual              pty(7)

## [](#NAME)NAME

           pty - pseudoterminal interfaces

## [](#DESCRIPTION)DESCRIPTION

           A pseudoterminal (sometimes abbreviated "pty") is a pair of
           virtual character devices that provide a bidirectional
           communication channel.  One end of the channel is called the
           master; the other end is called the slave.

           The slave end of the pseudoterminal provides an interface that
           behaves exactly like a classical terminal.  A process that expects
           to be connected to a terminal, can open the slave end of a
           pseudoterminal and then be driven by a program that has opened the
           master end.  Anything that is written on the master end is
           provided to the process on the slave end as though it was input
           typed on a terminal.  For example, writing the interrupt character
           (usually control-C) to the master device would cause an interrupt
           signal (SIGINT) to be generated for the foreground process group
           that is connected to the slave.  Conversely, anything that is
           written to the slave end of the pseudoterminal can be read by the
           process that is connected to the master end.

           Data flow between master and slave is handled asynchronously, much
           like data flow with a physical terminal.  Data written to the
           slave will be available at the master promptly, but may not be
           available immediately.  Similarly, there may be a small processing
           delay between a write to the master, and the effect being visible
           at the slave.

           Historically, two pseudoterminal APIs have evolved: BSD and System
           V.  SUSv1 standardized a pseudoterminal API based on the System V
           API, and this API should be employed in all new programs that use
           pseudoterminals.

           Linux provides both BSD-style and (standardized) System V-style
           pseudoterminals.  System V-style terminals are commonly called
           UNIX 98 pseudoterminals on Linux systems.

           Since Linux 2.6.4, BSD-style pseudoterminals are considered
           deprecated: support can be disabled when building the kernel by
           disabling the CONFIG_LEGACY_PTYS option.  (Starting with Linux
           2.6.30, that option is disabled by default in the mainline
           kernel.)  UNIX 98 pseudoterminals should be used in new
           applications.

       UNIX 98 pseudoterminals
           An unused UNIX 98 pseudoterminal master is opened by calling
           posix_openpt(3).  (This function opens the master clone device,
           /dev/ptmx; see pts(4).)  After performing any program-specific
           initializations, changing the ownership and permissions of the
           slave device using grantpt(3), and unlocking the slave using
           unlockpt(3)), the corresponding slave device can be opened by
           passing the name returned by ptsname(3) in a call to open(2).

           The Linux kernel imposes a limit on the number of available UNIX
           98 pseudoterminals.  Up to and including Linux 2.6.3, this limit
           is configured at kernel compilation time (CONFIG_UNIX98_PTYS), and
           the permitted number of pseudoterminals can be up to 2048, with a
           default setting of 256.  Since Linux 2.6.4, the limit is
           dynamically adjustable via /proc/sys/kernel/pty/max, and a
           corresponding file, /proc/sys/kernel/pty/nr, indicates how many
           pseudoterminals are currently in use.  For further details on
           these two files, see proc(5).

       BSD pseudoterminals
           BSD-style pseudoterminals are provided as precreated pairs, with
           names of the form /dev/ptyXY (master) and /dev/ttyXY (slave),
           where X is a letter from the 16-character set [p-za-e], and Y is a
           letter from the 16-character set [0-9a-f].  (The precise range of
           letters in these two sets varies across UNIX implementations.)
           For example, /dev/ptyp1 and /dev/ttyp1 constitute a BSD
           pseudoterminal pair.  A process finds an unused pseudoterminal
           pair by trying to open(2) each pseudoterminal master until an open
           succeeds.  The corresponding pseudoterminal slave (substitute
           "tty" for "pty" in the name of the master) can then be opened.

## [](#FILES)FILES

           /dev/ptmx
                  UNIX 98 master clone device

           /dev/pts/*
                  UNIX 98 slave devices

           /dev/pty[p-za-e][0-9a-f]
                  BSD master devices

           /dev/tty[p-za-e][0-9a-f]
                  BSD slave devices

## [](#NOTES)NOTES

           Pseudoterminals are used by applications such as network login
           services (ssh(1), rlogin(1), telnet(1)), terminal emulators such
           as xterm(1), script(1), screen(1), tmux(1), unbuffer(1), and
           expect(1).

           A description of the TIOCPKT ioctl(2), which controls packet mode
           operation, can be found in ioctl_tty(2).

           The BSD ioctl(2) operations TIOCSTOP, TIOCSTART, TIOCUCNTL, and
           TIOCREMOTE have not been implemented under Linux.

## [](#SEE_ALSO)SEE ALSO

           ioctl_tty(2), select(2), setsid(2), forkpty(3), openpty(3),
           termios(7), pts(4), tty(4)

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

    Linux man-pages 6.19            2026-07-02                         pty(7)

------------------------------------------------------------------------

Pages that refer to this page: [screen(1)](../man1/screen.1.html),  [intro(2)](../man2/intro.2.html),  [ioctl_tty(2)](../man2/ioctl_tty.2.html),  [getpt(3)](../man3/getpt.3.html),  [grantpt(3)](../man3/grantpt.3.html),  [openpty(3)](../man3/openpty.3.html),  [posix_openpt(3)](../man3/posix_openpt.3.html),  [ptsname(3)](../man3/ptsname.3.html),  [unlockpt(3)](../man3/unlockpt.3.html),  [pts(4)](../man4/pts.4.html),  [tty(4)](../man4/tty.4.html)

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
