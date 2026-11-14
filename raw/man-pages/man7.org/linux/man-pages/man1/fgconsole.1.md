---
{"title": "fgconsole(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/fgconsole.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fgconsole(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FGCONSOLE(1)             General Commands Manual             FGCONSOLE(1)

## [](#NAME)NAME

           fgconsole - print the number of the active VT.

## [](#SYNOPSIS)SYNOPSIS

           fgconsole [options]

## [](#DESCRIPTION)DESCRIPTION

           If the active Virtual Terminal is /dev/ttyN, then prints N on
           standard output.

           If the console is a serial console, then "serial" is printed
           instead.

## [](#OPTIONS)OPTIONS

           -n, --next-available
                  Will show the next unallocated virtual terminal. Normally 6
                  virtual terminals are allocated, with number 7 used for X;
                  this will return "8" in this case.

           -C, --console=DEV
                  the console device to be used.

           -V, --version
                  print version number.

           -h, --help
                  print this usage message.

## [](#NOTES)NOTES

           Under devfs, the consoles are in /dev/vc/N.  devfsd may maintain
           symlinks for compatibility.

## [](#AUTHORS)AUTHORS

           Andries Brouwer <aeb@cwi.nl>
           Manpage by Alastair McKinstry <mckinstry@computer.org>

## [](#SEE_ALSO)SEE ALSO

           chvt(1), deallocvt(1), openvt(1)

## [](#COLOPHON)COLOPHON

           This page is part of the kbd (Linux keyboard tools) project.
           Information about the project can be found at 
           ⟨http://www.kbd-project.org/⟩.  If you have a bug report for this
           manual page, send it to kbd@lists.altlinux.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/legionus/kbd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-26.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    kbd                          24 October 2024                 FGCONSOLE(1)

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
