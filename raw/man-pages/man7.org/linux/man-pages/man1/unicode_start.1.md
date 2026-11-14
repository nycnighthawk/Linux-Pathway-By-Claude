---
{"title": "unicode_start(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/unicode_start.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# unicode_start(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTE](#NOTE) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UNICODE_START(1)         General Commands Manual         UNICODE_START(1)

## [](#NAME)NAME

           unicode_start - put keyboard and console in unicode mode

## [](#SYNOPSIS)SYNOPSIS

           unicode_start [font [umap]]

## [](#DESCRIPTION)DESCRIPTION

           The unicode_start command will put the keyboard and console into
           Unicode (UTF-8) mode.

           For the keyboard this means that one can attach 16-bit U+xxxx
           values to keyboard keys using loadkeys(1), and have these appear
           as UTF-8 input to user programs.  Also, that one can type
           hexadecimal Alt-xxxx using the numeric keypad, and again produce
           UTF-8.

           For the console this means that the kernel expects UTF-8 output
           from user programs, and displays the output accordingly.

           The parameter font is a font that is loaded. It should have a
           built-in Unicode map, or, if it hasn't, such a map can be given
           explicitly as second parameter.  When no font was specified, the
           current font is kept.

## [](#NOTE)NOTE

           Unicode mode is a parameter with a value per virtual console.
           However, usually the font and keymap is common to all consoles.

## [](#AUTHORS)AUTHORS

           Andries Brouwer <aeb@cwi.nl>

## [](#SEE_ALSO)SEE ALSO

           dumpkeys(1), kbd_mode(1), loadkeys(1), unicode_stop(1), utf-8(7),
           setfont(8)

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

    kbd                             3 Feb 2001               UNICODE_START(1)

------------------------------------------------------------------------

Pages that refer to this page: [unicode_stop(1)](../man1/unicode_stop.1.html),  [setfont(8)](../man8/setfont.8.html)

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
