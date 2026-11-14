---
{"title": "ioctl_vt(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/VT_WAITACTIVE.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_vt(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioctl_vt(2)                System Calls Manual                ioctl_vt(2)

## [](#NAME)NAME

           ioctl_vt - ioctls for console terminal and virtual consoles

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/vt.h>  /* Definition of VT_* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, unsigned long op, void *argp);

## [](#DESCRIPTION)DESCRIPTION

           The following Linux-specific ioctl(2) operations are supported for
           console terminals and virtual consoles.

           VT_OPENQRY
                  Returns the first available (non-opened) console.  argp
                  points to an int which is set to the number of the vt (1 <=
                  *argp <= MAX_NR_CONSOLES).

           VT_GETMODE
                  Get mode of active vt.  argp points to a

                      struct vt_mode {
                          char  mode;    /* vt mode */
                          char  waitv;   /* if set, hang on writes if not active */
                          short relsig;  /* signal to raise on release op */
                          short acqsig;  /* signal to raise on acquisition */
                          short frsig;   /* unused (set to 0) */
                      };

                  which is set to the mode of the active vt.  mode is set to
                  one of these values:
                  VT_AUTO      auto vt switching
                  VT_PROCESS   process controls switching
                  VT_ACKACQ    acknowledge switch

           VT_SETMODE
                  Set mode of active vt.  argp points to a struct vt_mode.

           VT_GETSTATE
                  Get global vt state info.  argp points to a

                      struct vt_stat {
                          unsigned short v_active;  /* active vt */
                          unsigned short v_signal;  /* signal to send */
                          unsigned short v_state;   /* vt bit mask */
                      };

                  For each vt in use, the corresponding bit in the v_state
                  member is set.  (Linux 1.0 through Linux 1.1.92.)

           VT_RELDISP
                  Release a display.

           VT_ACTIVATE
                  Switch to vt argp (1 <= argp <= MAX_NR_CONSOLES).

           VT_WAITACTIVE
                  Wait until vt argp has been activated.

           VT_DISALLOCATE
                  Deallocate the memory associated with vt argp.  (Since
                  Linux 1.1.54.)

           VT_RESIZE
                  Set the kernel's idea of screensize.  argp points to a

                      struct vt_sizes {
                          unsigned short v_rows;       /* # rows */
                          unsigned short v_cols;       /* # columns */
                          unsigned short v_scrollsize; /* no longer used */
                      };

                  Note that this does not change the videomode.  See
                  resizecons(8).  (Since Linux 1.1.54.)

           VT_RESIZEX
                  Set the kernel's idea of various screen parameters.  argp
                  points to a

                      struct vt_consize {
                          unsigned short v_rows;  /* number of rows */
                          unsigned short v_cols;  /* number of columns */
                          unsigned short v_vlin;  /* number of pixel rows
                                                     on screen */
                          unsigned short v_clin;  /* number of pixel rows
                                                     per character */
                          unsigned short v_vcol;  /* number of pixel columns
                                                     on screen */
                          unsigned short v_ccol;  /* number of pixel columns
                                                     per character */
                      };

                  Any parameter may be set to zero, indicating "no change",
                  but if multiple parameters are set, they must be self-
                  consistent.  Note that this does not change the videomode.
                  See resizecons(8).  (Since Linux 1.3.3.)

           VT_GETCONSIZECSRPOS
                  Get console size and cursor position.  argp points to a

                      struct vt_consizecsrpos {
                          __u16 con_rows;  /* number of console rows */
                          __u16 con_cols;  /* number of console columns */
                          __u16 csr_row;   /* current cursor's row */
                          __u16 csr_col;   /* current cursor's column */
                      };

                  (Since Linux 6.16.)

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned (except where indicated).  On failure,
           -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL argp is invalid.

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

    Linux man-pages 6.19            2026-02-08                    ioctl_vt(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_console(2)](../man2/ioctl_console.2.html)

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
