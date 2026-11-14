---
{"title": "slattach(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/slattach.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slattach(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLATTACH(8)        Linux System Administrator's Manual        SLATTACH(8)

## [](#NAME)NAME

           slattach - attach a network interface to a serial line

## [](#SYNOPSIS)SYNOPSIS

           slattach [-dehlLmnqv] [-c command ] [-p proto ] [-s speed] [tty]

## [](#DESCRIPTION)DESCRIPTION

           Slattach is a tiny program that can be used to put a normal
           terminal ("serial") line into one of several "network" modes, thus
           allowing you to use it for point-to-point links to other
           computers.

## [](#OPTIONS)OPTIONS

           tty    Path to a serial device like /dev/ttyS*, /dev/cua* or
                  /dev/ptmx to spawn a new pseudo tty.

           -c command
                  Execute command when the line is hung up. This can be used
                  to run scripts or re-establish connections when a link goes
                  down.

           -d     Enable debugging output.  Useful when determining why a
                  given setup doesn't work.

           -h     Exit when the carrier is lost. This works on both /dev/tty
                  and /dev/cua devices by directly monitoring the carrier
                  status every 15 seconds.

           -v     Enable verbose output.  Useful in shell scripts.

           -q     Operate in quiet mode - no messages at all.

           -l     Create an UUCP-style lockfile for the device in /var/lock.

           -n     Equivalent to the "mesg n" command.

           -m     Do not initialize the line into 8-bit raw mode.

           -e     Exit right after initializing device, instead of waiting
                  for the line to hang up.

           -L     Enable 3 wire operation. The terminal is moved into CLOCAL
                  mode, carrier watching is disabled.

           -p proto
                  Set a specific kind of protocol to use on the line.  The
                  default is set to cslip, i.e. compressed SLIP.  Other
                  possible values are slip (normal SLIP), adaptive (adaptive
                  CSLIP/SLIP), ppp (Point-to-Point Protocol) and kiss (a
                  protocol used for communicating with AX.25 packet radio
                  terminal node controllers).  The special argument tty can
                  be used to put the device back into normal serial
                  operation.  Using 'ppp' mode normally requires an
                  additional ppp daemon pppd to be active on the line. For
                  kiss connections the kissattach program should be used.

           -s speed
                  Set a specific line speed, other than the default.

           If no arguments are given, the current terminal line (usually: the
           login device) is used.  Otherwise, an attempt is made to claim the
           indicated terminal port, lock it, and open it.

## [](#FILES)FILES

           /dev/cua* /var/lock/LCK.* /dev/ttyS* /dev/ptmx

## [](#SEE_ALSO)SEE ALSO

           Homepage of the net-tools project: 
           ⟨https://net-tools.sourceforge.io⟩

           kissattach(8), dip(8), pppd(8), sliplogin(8)

## [](#AUTHORS)AUTHORS

           Fred N. van Kempen <waltje@uwalt.nl.mugnet.org>,
           Alan Cox <Alan.Cox@linux.org>,
           Miquel van Smoorenburg <miquels@drinkel.ow.org>,
           George Shearer <gshearer@one.net>,
           Yossi Gottlieb <yogo@math.tau.ac.il>,
           Bernd Eckenfels <net-tools@lina.inka.de>.

## [](#COLOPHON)COLOPHON

           This page is part of the net-tools (networking utilities) project.
           Information about the project can be found at 
           ⟨http://net-tools.sourceforge.net/⟩.  If you have a bug report for
           this manual page, see ⟨http://net-tools.sourceforge.net/⟩.  This
           page was obtained from the project's upstream Git repository
           ⟨git://git.code.sf.net/p/net-tools/code⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-12.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    net-tools                       2025-09-10                    SLATTACH(8)

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
