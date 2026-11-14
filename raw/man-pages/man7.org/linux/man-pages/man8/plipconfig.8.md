---
{"title": "plipconfig(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/plipconfig.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# plipconfig(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTE](#NOTE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PLIPCONFIG(8)      Linux System Administrator's Manual      PLIPCONFIG(8)

## [](#NAME)NAME

           plipconfig - fine tune PLIP device parameters

## [](#SYNOPSIS)SYNOPSIS

           plipconfig Interface [nibble NI] [trigger NT]

           plipconfig [-V] [--version] [-h] [--help]

## [](#DESCRIPTION)DESCRIPTION

           Plipconfig is used to (hopefully) improve PLIP performance by
           changing the default timing parameters used by the PLIP protocol.
           Results are dependent on the parallel port hardware, cable, and
           the CPU speed of each machine on each end of the PLIP link.

           If the single interface argument is given, plipconfig displays the
           status of the given interface only.  Otherwise, it will try to set
           the options.

## [](#OPTIONS)OPTIONS

           nibble  NI
                  Sets the nibble wait value in microseconds. Default is
                  3000.

           trigger NT
                  Sets the trigger wait value in microseconds. Default is
                  500.

           PLIP speed can in some cases be improved by lowering the default
           values.  Values which are too low may cause excess use of CPU,
           poor interrupt response time resulting in serial ports dropping
           characters, or in dropping of PLIP packets. Changing the plip MTU
           can also affect PLIP speed.

## [](#NOTE)NOTE

           If you get no response it is far more likely the irq is wrong and
           needs setting with ifconfig. The few cases where the default
           parameters will be too fast are those using very long cables.
           Something you should never do as the parallel port is not
           specified or designed for driving long cable runs.

## [](#SEE_ALSO)SEE ALSO

           Homepage of the net-tools project: 
           ⟨https://net-tools.sourceforge.io⟩

           ifconfig(8)

## [](#AUTHOR)AUTHOR

           John Paul Morrison
                  <jmorriso@bogomips.ee.ubc.ca>, <ve7jpm@ve7jpm.ampr.org>

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

    net-tools                       2025-09-10                  PLIPCONFIG(8)

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
