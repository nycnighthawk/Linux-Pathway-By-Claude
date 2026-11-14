---
{"title": "vlock(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/vlock.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# vlock(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    VLOCK(1)                 General Commands Manual                 VLOCK(1)

## [](#NAME)NAME

           vlock - Virtual Console lock program

## [](#SYNOPSIS)SYNOPSIS

           vlock

           vlock [ -a,--all ] [ -c,--current ] [ -h,--help ] [ -v,--version ]

## [](#DESCRIPTION)DESCRIPTION

           vlock is a program to lock one or more sessions on the Linux
           console.  This is especially useful for Linux machines which have
           multiple users with access to the console.  One user may lock his
           or her session(s) while still allowing other users to use the
           system on other virtual consoles.  If desired, the entire console
           may be locked and virtual console switching disabled.

           By default, only the current VC (virtual console) is locked.  With
           the -a,-all option all VCs are locked.  The locked VCs cannot be
           unlocked without the invoker's password.  And, for the paranoid,
           vlock makes it a trying experience for those attempting to guess
           the password, so unauthorized access to session(s) is highly
           unlikely.

           Please note that it is entirely possible to completely lock
           yourself out of the console with the -a,--all option if you cannot
           remember your password!  Unless you are able to kill vlock by
           logging in remotely via a serial terminal or network, a hard reset
           is the only method of ``unlocking'' the display.

           vlock works for console sessions primarily.  However, there is
           support for trying to lock non-console sessions as well, but that
           support has not been well tested.

## [](#OPTIONS)OPTIONS

           -a,--all

                  Lock all console sessions and disable VC switching.

           -c,--current

                  Lock the current session (this is the default).

           -h,--help

                  Print a brief help message.

           -v,--version

                  Print the version number of vlock.

## [](#AUTHORS)AUTHORS

           Michael K. Johnson <johnsonm@redhat.com>

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

    kbd                            16 May 1996                       VLOCK(1)

------------------------------------------------------------------------

Pages that refer to this page: [openvt(1)](../man1/openvt.1.html)

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
