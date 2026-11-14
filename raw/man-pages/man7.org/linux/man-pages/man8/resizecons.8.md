---
{"title": "resizecons(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/resizecons.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# resizecons(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RESIZECONS(8)            System Manager's Manual            RESIZECONS(8)

## [](#NAME)NAME

           resizecons - change kernel idea of the console size

## [](#SYNOPSIS)SYNOPSIS

           resizecons COLSxROWS
           resizecons -lines ROWS

## [](#DESCRIPTION)DESCRIPTION

           The resizecons command tries to change the videomode of the
           console.  There are several aspects to this: (a) the kernel must
           know about it, (b) the hardware must know about it, (c) user
           programs must know about it, (d) the console font may have to be
           adapted.

           (a) The kernel is told about the change using the ioctl VT_RESIZE.
           This causes the kernel to reallocate console screen memory for all
           virtual consoles, and might fail if there is not enough memory.
           (In that case, try to disallocate some virtual consoles first.)
           If this ioctl succeeds, but a later step fails (e.g., because you
           do not have root permissions), you may be left with a very messy
           screen.

           The most difficult part of this is (b), since it requires detailed
           knowledge of the video card hardware, and the setting of numerous
           registers. Only changing the number of rows is slightly easier,
           and resizecons will try to do that itself, when given the -lines
           option. (Probably, root permission will be required.)  The command
           resizecons COLSxROWS will execute restoretextmode -r COLSxROWS
           (and hence requires that you have svgalib installed). Here
           COLSxROWS is a file that was created earlier by restoretextmode -w
           COLSxROWS.  Again, either root permissions are required, or
           restoretextmode has to be suid root.

           In order to deal with (c), resizecons does a `stty rows ROWS cols
           COLS' for each active console (in the range tty0..tty15), and
           sends a SIGWINCH signal to selection if it finds the file
           /tmp/selection.pid.

           Finally, (d) is dealt with by executing a setfont command. Most
           likely, the wrong font is loaded, and you may want to do another
           setfont yourself afterwards.

## [](#BUGS)BUGS

           resizecons does not work on all hardware.  This command used to be
           called resize, but was renamed to avoid conflict with another
           command with the same name.

## [](#SEE_ALSO)SEE ALSO

           setfont(8), stty(1), selection(1), restoretextmode(8), disalloc(8)

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

    kbd                            17 Jan 1995                  RESIZECONS(8)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_console(2)](../man2/ioctl_console.2.html),  [ioctl_vt(2)](../man2/ioctl_vt.2.html),  [console_codes(4)](../man4/console_codes.4.html)

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
