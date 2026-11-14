---
{"title": "TIOCLINUX(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/TIOCLINUX.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# TIOCLINUX(2const) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TIOCLINUX(2const)                                       TIOCLINUX(2const)

## [](#NAME)NAME

           TIOCLINUX - ioctls for console terminal and virtual consoles

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/tiocl.h>  /* Definition of TIOCL_* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, TIOCLINUX, void *argp);

## [](#DESCRIPTION)DESCRIPTION

           The action of the following ioctls depends on the first byte in
           the struct pointed to by argp, referred to here as the subcode.
           These are legal only for the superuser or the owner of the current
           terminal.

           subcode=0
                  Dump the screen.  Disappeared in Linux 1.1.92.  (With Linux
                  1.1.92 or later, read from /dev/vcsN or /dev/vcsaN
                  instead.)

           subcode=1
                  Get task information.  Disappeared in Linux 1.1.92.

           subcode=TIOCL_SETSEL
                  Set selection.  argp points to a

                      struct {
                          char  subcode;
                          short xs, ys, xe, ye;
                          short sel_mode;
                      };

                  xs and ys are the starting column and row.  xe and ye are
                  the ending column and row.  (Upper left corner is
                  row=column=1.)  sel_mode may be one of the following
                  operations:

                  TIOCL_SELCHAR
                         Select character-by-character.  The indicated screen
                         characters are highlighted and saved in a kernel
                         buffer.

                         Since Linux 6.7, using this selection mode requires
                         the CAP_SYS_ADMIN capability.

                  TIOCL_SELWORD
                         Select word-by-word, expanding the selection
                         outwards to align with word boundaries.  The
                         indicated screen characters are highlighted and
                         saved in a kernel buffer.

                         Since Linux 6.7, using this selection mode requires
                         the CAP_SYS_ADMIN capability.

                  TIOCL_SELLINE
                         Select line-by-line, expanding the selection
                         outwards to select full lines.  The indicated screen
                         characters are highlighted and saved in a kernel
                         buffer.

                         Since Linux 6.7, using this selection mode requires
                         the CAP_SYS_ADMIN capability.

                  TIOCL_SELPOINTER
                         Show the pointer at position (xs, ys) or (xe, ye),
                         whichever is later in text flow order.

                  TIOCL_SELCLEAR
                         Remove the current selection highlight, if any, from
                         the console holding the selection.

                         This does not affect the stored selected text.

                  TIOCL_SELMOUSEREPORT
                         Make the terminal report (xs, ys) as the current
                         mouse location using the xterm(1) mouse tracking
                         protocol (see console_codes(4)).  The lower 4 bits
                         of sel_mode (TIOCL_SELBUTTONMASK) indicate the
                         desired button press and modifier key information
                         for the mouse event.

                         If mouse reporting is not enabled for the terminal,
                         this operation yields an EINVAL error.

                         Since Linux 6.7, using this selection mode requires
                         the CAP_SYS_ADMIN capability.

           subcode=TIOCL_PASTESEL
                  Paste selection.  The characters in the selection buffer
                  are written to fd.

                  Since Linux 6.7, using this subcode requires the
                  CAP_SYS_ADMIN capability.

           subcode=TIOCL_UNBLANKSCREEN
                  Unblank the screen.

           subcode=TIOCL_SELLOADLUT
                  Sets contents of a 256-bit look up table defining
                  characters in a "word", for word-by-word selection.  (Since
                  Linux 1.1.32.)

                  Since Linux 6.7, using this subcode requires the
                  CAP_SYS_ADMIN capability.

           subcode=TIOCL_GETSHIFTSTATE
                  argp points to a char which is set to the value of the
                  kernel variable shift_state.  (Since Linux 1.1.32.)

           subcode=TIOCL_GETMOUSEREPORTING
                  argp points to a char which is set to the value of the
                  kernel variable report_mouse.  (Since Linux 1.1.33.)

           subcode=8
                  Dump screen width and height, cursor position, and all the
                  character-attribute pairs.  (Linux 1.1.67 through Linux
                  1.1.91 only.  With Linux 1.1.92 or later, read from
                  /dev/vcsa* instead.)

           subcode=9
                  Restore screen width and height, cursor position, and all
                  the character-attribute pairs.  (Linux 1.1.67 through Linux
                  1.1.91 only.  With Linux 1.1.92 or later, write to
                  /dev/vcsa* instead.)

           subcode=TIOCL_SETVESABLANK
                  Handles the Power Saving feature of the new generation of
                  monitors.  VESA screen blanking mode is set to argp[1],
                  which governs what screen blanking does:

                  0      Screen blanking is disabled.

                  1      The current video adapter register settings are
                         saved, then the controller is programmed to turn off
                         the vertical synchronization pulses.  This puts the
                         monitor into "standby" mode.  If your monitor has an
                         Off_Mode timer, then it will eventually power down
                         by itself.

                  2      The current settings are saved, then both the
                         vertical and horizontal synchronization pulses are
                         turned off.  This puts the monitor into "off" mode.
                         If your monitor has no Off_Mode timer, or if you
                         want your monitor to power down immediately when the
                         blank_timer times out, then you choose this option.
                         (Caution: Powering down frequently will damage the
                         monitor.)  (Since Linux 1.1.76.)

           subcode=TIOCL_SETKMSGREDIRECT
                  Change target of kernel messages ("console"): by default,
                  and if this is set to 0, messages are written to the
                  currently active VT.  The VT to write to is a single byte
                  following subcode.  (Since Linux 2.5.36.)

           subcode=TIOCL_GETFGCONSOLE
                  Returns the number of VT currently in foreground.  (Since
                  Linux 2.5.36.)

           subcode=TIOCL_SCROLLCONSOLE
                  Scroll the foreground VT by the specified amount of lines
                  down, or half the screen if 0.  lines is *(((int32_t
                  *)&subcode) + 1).  (Since Linux 2.5.67.)

           subcode=TIOCL_BLANKSCREEN
                  Blank the foreground VT, ignoring "pokes" (typing): can
                  only be unblanked explicitly (by switching VTs, to text
                  mode, etc.).  (Since Linux 2.5.71.)

           subcode=TIOCL_BLANKEDSCREEN
                  Returns the number of VT currently blanked, 0 if none.
                  (Since Linux 2.5.71.)

           subcode=16
                  Never used.

           subcode=TIOCL_GETKMSGREDIRECT
                  Returns target of kernel messages.  (Since Linux 2.6.17.)

           subcode=TIOCL_GETBRACKETEDPASTE
                  Returns 1 if the application advertised bracketed paste
                  compatibility to the terminal, 0 otherwise.  (Since Linux
                  6.16.)

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned (except where indicated).  On failure,
           -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL argp is invalid.

           EPERM  Insufficient permission.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_console(2)

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

    Linux man-pages 6.19            2026-02-08              TIOCLINUX(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_console(2)](../man2/ioctl_console.2.html),  [ioctl_tty(2)](../man2/ioctl_tty.2.html)

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
