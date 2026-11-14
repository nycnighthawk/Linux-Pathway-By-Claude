---
{"title": "deallocvt(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/deallocvt.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deallocvt(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DEALLOCVT(1)             General Commands Manual             DEALLOCVT(1)

## [](#NAME)NAME

           deallocvt - deallocate unused virtual consoles

## [](#SYNOPSIS)SYNOPSIS

           deallocvt [option...]  [N ...]

## [](#DESCRIPTION)DESCRIPTION

           The command deallocvt deallocates kernel memory and data
           structures for all unused virtual consoles.  If one or more
           arguments N ...  are given, only the corresponding consoles
           /dev/ttyN are deallocated.

           A virtual console is unused if it is not the foreground console,
           and no process has it open for reading or writing, and no text has
           been selected on its screen.

## [](#OPTIONS)OPTIONS

           -C, --console=DEV
                  the console device to be used.

           -V, --version
                  print version number.

           -h, --help
                  print this usage message.

## [](#AUTHORS)AUTHORS

           Andries Brouwer <aeb@cwi.nl>

## [](#SEE_ALSO)SEE ALSO

           chvt(1), openvt(1)

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

    kbd                          24 October 2024                 DEALLOCVT(1)

------------------------------------------------------------------------

Pages that refer to this page: [chvt(1)](../man1/chvt.1.html),  [fgconsole(1)](../man1/fgconsole.1.html),  [openvt(1)](../man1/openvt.1.html),  [vlock(1)](../man1/vlock.1.html)

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
