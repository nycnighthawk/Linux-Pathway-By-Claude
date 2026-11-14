---
{"title": "kbd_mode(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/kbd_mode.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# kbd_mode(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KBD_MODE(1)              General Commands Manual              KBD_MODE(1)

## [](#NAME)NAME

           kbd_mode - report or set the keyboard mode

## [](#SYNOPSIS)SYNOPSIS

           kbd_mode [ -a | -u | -k | -s | -d ] [ -f ] [ -C CONSOLE ]

## [](#DESCRIPTION)DESCRIPTION

           Without argument, kbd_mode prints the current keyboard mode (RAW,
           MEDIUMRAW or XLATE). Using the options it is possible to switch
           the keyboard mode of the current console or the specified console.

## [](#OPTIONS)OPTIONS

           -a, --ascii
                  set ASCII mode (XLATE).

           -k, --keycode
                  set keycode mode (MEDIUMRAW).

           -s, --scancode
                  set scancode mode (RAW).

           -u, --unicode
                  set UTF-8 mode (UNICODE).

           -d, --disable
                  set Disable mode (OFF).

           -f, --force
                  switch the mode even if it makes the keyboard unusable.

           -C, --console=DEV
                  the console device to be used.

           Of course the "-a" is only traditional, and the code used can be
           any 8-bit character set.  With "-u" a 16-bit character set is
           expected, and these chars are transmitted to the kernel as 1, 2,
           or 3 bytes (following the UTF-8 coding).  In these latter two
           modes the key mapping defined by loadkeys(1) is used.

           The Didable mode for the virtual console keyboard OFF to
           compliment RAW in which all key events are ignored. The mode
           prevents vt input buffers from overflowing when a program opens
           but doesn't read from a tty, like Xorg using only evdev for input.

           kbd_mode operates on the console specified by the "-C" option; if
           there is none, the console associated with stdin is used.

           Warning: changing the keyboard mode, other than between ASCII and
           Unicode, will probably make your keyboard unusable. Set the "-f"
           option to force such changes.  This command is only meant for use
           (say via remote login) when some program left your keyboard in the
           wrong state.  Note that in some obsolete versions of this program
           the "-u" option was a synonym for "-s" and older versions of this
           program may not recognize the "-f" option.

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

    kbd                             6 Apr 1994                    KBD_MODE(1)

------------------------------------------------------------------------

Pages that refer to this page: [kbdinfo(1)](../man1/kbdinfo.1.html),  [loadkeys(1)](../man1/loadkeys.1.html),  [unicode_start(1)](../man1/unicode_start.1.html),  [unicode_stop(1)](../man1/unicode_stop.1.html),  [ioctl_console(2)](../man2/ioctl_console.2.html)

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
