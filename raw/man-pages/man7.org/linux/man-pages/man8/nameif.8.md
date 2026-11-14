---
{"title": "nameif(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/nameif.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nameif(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [SEE AlSO](#SEE_AlSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NAMEIF(8)          Linux System Administrator's Manual          NAMEIF(8)

## [](#NAME)NAME

           nameif - name network interfaces based on MAC addresses

## [](#SYNOPSIS)SYNOPSIS

           nameif [-c configfile] [-s]
           nameif [-c configfile] [-s] interface macaddress

## [](#DESCRIPTION)DESCRIPTION

           nameif renames network interfaces based on mac addresses.  When no
           arguments are given /etc/mactab is read.  Each line  of it
           contains an interface name and a Ethernet MAC address.  Comments
           are allowed starting with #.  Otherwise the interfaces specified
           on the command line are processed.  nameif looks for the interface
           with the given MAC address and renames it to the name given.

           When the -s argument is given all error messages go to the syslog.

           When the -c argument is given with a file name that file is read
           instead of /etc/mactab.

## [](#NOTES)NOTES

           nameif should be run before the interface is up, otherwise it'll
           fail.

## [](#FILES)FILES

           /etc/mactab

## [](#BUGS)BUGS

           Only works for Ethernet hardware address types.

           More modern alias name functions are available with the ip(8)
           command or management frameworks like udev(5) or netplan(5).

## [](#SEE_AlSO)SEE AlSO

           Homepage of the net-tools project: 
           ⟨https://net-tools.sourceforge.io⟩

           ifconfig(8), ip(8)
           netplan(5), udev(5)

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

    net-tools                       2025-09-10                      NAMEIF(8)

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
