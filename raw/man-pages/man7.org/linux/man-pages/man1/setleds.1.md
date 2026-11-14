---
{"title": "setleds(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/setleds.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setleds(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SETLEDS(1)               General Commands Manual               SETLEDS(1)

## [](#NAME)NAME

           setleds - set the keyboard leds

## [](#SYNOPSIS)SYNOPSIS

           setleds [-v] [-L] [-D] [-F] [{+|-}num] [{+|-}caps] [{+|-}scroll]

## [](#DESCRIPTION)DESCRIPTION

           Setleds reports and changes the led flag settings of a VT (namely
           NumLock, CapsLock and ScrollLock).  Without arguments, setleds
           prints the current settings.  With arguments, it sets or clears
           the indicated flags (and leaves the others unchanged). The
           settings before and after the change are reported if the -v flag
           is given.

           The led flag settings are specific for each VT (and the VT
           corresponding to stdin is used).

           By default (or with option -F), setleds will only change the VT
           flags (and their setting may be reflected by the keyboard leds).

           With option -D, setleds will change both the VT flags and their
           default settings (so that a subsequent reset will not undo the
           change).  This might be useful for people who always want to have
           numlock set.

           With option -L, setleds will not touch the VT flags, but only
           change the leds.  From this moment on, the leds will no longer
           reflect the VT flags (but display whatever is put into them). The
           command setleds -L (without further arguments) will restore the
           situation in which the leds reflect the VT flags.

           One might use setleds in /etc/rc to define the initial and default
           state of NumLock, e.g. by
                INITTY=/dev/tty[1-8]
                for tty in $INITTY; do
                     setleds -D +num < $tty
                done

## [](#OPTIONS)OPTIONS

           -num +num
                  Clear or set NumLock.  (At present, the NumLock setting
                  influences the interpretation of keypad keys.  Pressing the
                  NumLock key complements the NumLock setting.)

           -caps +caps
                  Clear or set CapsLock.  (At present, the CapsLock setting
                  complements the Shift key when applied to letters.
                  Pressing the CapsLock key complements the CapsLock
                  setting.)

           -scroll +scroll
                  Clear or set ScrollLock.  (At present, pressing the
                  ScrollLock key (or ^S/^Q) stops/starts console output.)

## [](#BUGS)BUGS

           In keyboard application mode the NumLock key does not influence
           the NumLock flag setting.

## [](#AUTHORS)AUTHORS

           Andries Brouwer <aeb@cwi.nl>

## [](#SEE_ALSO)SEE ALSO

           loadkeys(1)

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

    kbd                            24 Sep 1994                     SETLEDS(1)

------------------------------------------------------------------------

Pages that refer to this page: [kbdinfo(1)](../man1/kbdinfo.1.html),  [ioctl_console(2)](../man2/ioctl_console.2.html)

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
