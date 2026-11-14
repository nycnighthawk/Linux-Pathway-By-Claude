---
{"title": "ldattach(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ldattach.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ldattach(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [LINE DISCIPLINES](#LINE_DISCIPLINES) \| [OPTIONS](#OPTIONS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LDATTACH(8)               System Administration               LDATTACH(8)

## [](#NAME)NAME

           ldattach - attach a line discipline to a serial line

## [](#SYNOPSIS)SYNOPSIS

           ldattach [-1278denoVh] [-i iflag] [-s speed] [-m mtu] ldisc device

## [](#DESCRIPTION)DESCRIPTION

           The ldattach daemon opens the specified device file (which should
           refer to a serial device) and attaches the line discipline ldisc
           to it for processing of the sent and/or received data. It then
           goes into the background keeping the device open so that the line
           discipline stays loaded.

           The line discipline ldisc may be specified either by name or by
           number.

           In order to detach the line discipline, kill(1) the ldattach
           process.

           With no arguments, ldattach prints usage information.

## [](#LINE_DISCIPLINES)LINE DISCIPLINES

           Depending on the kernel release, the following line disciplines
           are supported:

           TTY(0)
               The default line discipline, providing transparent operation
               (raw mode) as well as the habitual terminal line editing
               capabilities (cooked mode).

           SLIP(1)
               Serial Line IP (SLIP) protocol processor for transmitting
               TCP/IP packets over serial lines.

           MOUSE(2)
               Device driver for RS232 connected pointing devices (serial
               mice).

           PPP(3)
               Point to Point Protocol (PPP) processor for transmitting
               network packets over serial lines.

           STRIP(4); AX25(5); X25(6)
               Line driver for transmitting X.25 packets over asynchronous
               serial lines.

           6PACK(7); R3964(9)
               Driver for Simatic R3964 module.

           IRDA(11)
               Linux IrDa (infrared data transmission) driver - see
               http://irda.sourceforge.net/

           HDLC(13)
               Synchronous HDLC driver.

           SYNC_PPP(14)
               Synchronous PPP driver.

           HCI(15)
               Bluetooth HCI UART driver.

           GIGASET_M101(16)
               Driver for Siemens Gigaset M101 serial DECT adapter.

           PPS(18)
               Driver for serial line Pulse Per Second (PPS) source.

           GSM0710(21)
               Driver for GSM 07.10 multiplexing protocol modem (CMUX).

## [](#OPTIONS)OPTIONS

           -1, --onestopbit
               Set the number of stop bits of the serial line to one.

           -2, --twostopbits
               Set the number of stop bits of the serial line to two.

           -7, --sevenbits
               Set the character size of the serial line to 7 bits.

           -8, --eightbits
               Set the character size of the serial line to 8 bits.

           -d, --debug
               Keep ldattach in the foreground so that it can be interrupted
               or debugged, and to print verbose messages about its progress
               to standard error output.

           -e, --evenparity
               Set the parity of the serial line to even.

           -i, --iflag value...
               Set the specified bits in the c_iflag word of the serial line.
               The given value may be a number or a symbolic name. If value
               is prefixed by a minus sign, the specified bits are cleared
               instead. Several comma-separated values may be given in order
               to set and clear multiple bits.

           -n, --noparity
               Set the parity of the serial line to none.

           -o, --oddparity
               Set the parity of the serial line to odd.

           -s, --speed value
               Set the speed (the baud rate) of the serial line to the
               specified value.

           -c, --intro-command string
               Define an intro command that is sent through the serial line
               before the invocation of ldattach. E.g. in conjunction with
               line discipline GSM0710, the command 'AT+CMUX=0\r' is commonly
               suitable to switch the modem into the CMUX mode.

           -p, --pause value
               Sleep for value seconds before the invocation of ldattach.
               Default is one second.

           -m, --mtu value
               Set maximum frame size for GSM0710 CMUX. If not specified,
               traditionally the default of 127 have been set by ldattach.
               This differs from 3GPP TS 27.010 default value of 31 bytes, so
               it is recommended to specify

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#AUTHORS)AUTHORS

           Tilman Schmidt <tilman@imap.cc>

## [](#SEE_ALSO)SEE ALSO

           inputattach(1), ttys(4)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The ldattach command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                    LDATTACH(8)

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
