---
{"title": "openvt(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/openvt.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# openvt(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTE](#NOTE) \| [EXAMPLES](#EXAMPLES) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OPENVT(1)                General Commands Manual                OPENVT(1)

## [](#NAME)NAME

           openvt - start a program on a new virtual terminal (VT).

## [](#SYNOPSIS)SYNOPSIS

           openvt [-c vtnumber] [OPTIONS] [--] command

## [](#DESCRIPTION)DESCRIPTION

           openvt will find the first available VT, and run on it the given
           command with the given command options , standard input, output
           and error are directed to that terminal. The current search path
           ($PATH) is used to find the requested command. If no command is
           specified then the environment variable $SHELL is used.

       OPTIONS
           -c, --console=VTNUMBER
                  Use the given VT number and not the first available. Note
                  you must have write access to the supplied VT for this to
                  work.

           -f, --force
                  Force opening a VT without checking whether it is already
                  in use.

           -e, --exec
                  Directly execute the given command, without forking.  This
                  option is meant for use in /etc/inittab.

           -s, --switch
                  Switch to the new VT when starting the command. The VT of
                  the new command will be made the new current VT.

           -u, --user
                  Figure out the owner of the current VT, and run login as
                  that user.  Suitable to be called by init. Shouldn't be
                  used with -c or -l.  This option refuses to pre-
                  authenticate root and requires a process owned by the VT
                  owner whose controlling terminal is the current VT.

           -l, --login
                  Make the command a login shell. A - is prepended to the
                  name of the command to be executed.

           -v, --verbose
                  Be a bit more verbose.

           -w, --wait
                  wait for command to complete. If -w and -s are used
                  together then openvt will switch back to the controlling
                  terminal when the command completes.

           -V, --version
                  print program version and exit.

           -h, --help
                  show this text and exit.

           --     end of options to openvt.

## [](#NOTE)NOTE

           If openvt is compiled with a getopt_long() and you wish to set
           options to the command to be run, then you must supply the end of
           options -- flag before the command.

           The -u option uses login -f and therefore bypasses normal password
           authentication for the detected user.  It is intended only for
           controlled init or keyboard-request configurations.  Use a normal
           authenticated login command when authentication is required.

## [](#EXAMPLES)EXAMPLES

           openvt can be used to start a shell on the next free VT, by using
           the command:

           openvt bash

           To start the shell as a login shell, use:

           openvt -l bash

           To get a long listing you must supply the -- separator:

           openvt -- ls -l

## [](#HISTORY)HISTORY

           Earlier, openvt was called open.  It was written by Jon Tombs
           <jon@gtex02.us.es> or <jon@robots.ox.ac.uk>.  The -w idea is from
           "sam".

## [](#SEE_ALSO)SEE ALSO

           chvt(1), deallocvt(1), vlock(1), login(1)

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

    kbd                          24 October 2024                    OPENVT(1)

------------------------------------------------------------------------

Pages that refer to this page: [chvt(1)](../man1/chvt.1.html),  [deallocvt(1)](../man1/deallocvt.1.html),  [fgconsole(1)](../man1/fgconsole.1.html),  [vlock(1)](../man1/vlock.1.html)

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
