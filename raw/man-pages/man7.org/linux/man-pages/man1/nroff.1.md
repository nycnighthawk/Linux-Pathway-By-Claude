---
{"title": "nroff(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/nroff.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nroff(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Synopsis](#Synopsis) \| [Description](#Description) \| [Exit status](#Exit_status) \| [Environment](#Environment) \| [Files](#Files) \| [Notes](#Notes) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nroff(1)                 General Commands Manual                 nroff(1)

## [](#Name)Name

           nroff - format documents with groff for terminal (“TTY”) devices

## [](#Synopsis)Synopsis

           nroff [-abcCEhikpRStUVzZ] [-d ctext] [-d string=text]
                 [-D fallback-input-encoding] [-I inclusion-directory]
                 [-K input-encoding] [-m macro-package] [-M macro-directory]
                 [-n page-number] [-o page-list] [-P postprocessor-argument]
                 [-r cnumeric-expression] [-r register=numeric-expression]
                 [-T output-device] [-w warning-category] [-W warning-
                 category] [file ...]

           nroff --help

           nroff -v [other-nroff-option ...]

           nroff --version [other-nroff-option ...]

## [](#Description)Description

           nroff formats documents written in the groff(7) language for
           typewriter-like devices such as terminal emulators.  GNU nroff
           emulates the AT&T nroff command using groff(1).  nroff generates
           output via grotty(1), groff's terminal output driver, which needs
           to know the character encoding scheme used by the device.
           Consequently, acceptable arguments to the -T option are ascii,
           latin1, and utf8; any others are ignored.  If neither the
           GROFF_TYPESETTER environment variable nor the -T command-line
           option (which overrides the environment variable) specifies a
           (valid) device, nroff consults the locale to select an appropriate
           output device.  It first tries the locale(1) program, then checks
           several locale-related environment variables; see section
           “Environment” below.  If all of the foregoing fail, nroff assumes
           “-T ascii”.

           The -a, -b, -c, -C, -d, -E, -i, -I, -m, -M, -n, -o, -r, -U, -w,
           -W, and -z options have the effects described in troff(1).  -c and
           -h imply “-P -c” and “-P -h”, respectively; -c is also meaningful
           to troff itself.  Further, GNU nroff ignores the AT&T nroff
           options -e, -q, and -s.  groff(1) documents options -D, -k, -K,
           -p, -P, -R, -t, -S, and -Z.  -V causes nroff to display the
           constructed groff command on the standard output stream, but does
           not execute it.  -v and --version show version information about
           nroff and the programs it runs, while --help displays a usage
           message; all exit afterward.

## [](#Exit_status)Exit status

           nroff exits with status 2 if there was a problem parsing its
           arguments, with status 0 if any of the options -V, -v, --version,
           or --help were specified, and with the status of groff otherwise.

## [](#Environment)Environment

           Normally, the path separator in environment variables ending with
           PATH is the colon; this may vary depending on the operating
           system.  For example, Windows uses a semicolon instead.

           GROFF_BIN_PATH
                  Locate groff commands in these directories, followed by
                  those in PATH.  If not set, the installation directory of
                  GNU roff executables, /usr/local/bin, is searched before
                  PATH.

           GROFF_TYPESETTER
                  specifies the default output device for groff.

           LC_ALL
           LC_CTYPE
           LANG
           LESSCHARSET
                  are pattern-matched in this order for contents matching
                  standard character encodings supported by groff in the
                  event no -T option is given and GROFF_TYPESETTER is unset,
                  or the values specified are invalid.

## [](#Files)Files

           /usr/local/share/groff/1.24.1/tmac/tty-char.tmac
                  defines fallback definitions of roff special characters.
                  These definitions more poorly optically approximate typeset
                  output than those of tty.tmac in favor of communicating
                  semantic information.  nroff loads it automatically.

## [](#Notes)Notes

           Pager programs like more(1) and less(1) may require command-line
           options to correctly handle some output sequences; see grotty(1).

## [](#See_also)See also

           groff(1), troff(1), grotty(1), locale(1), roff(7)

## [](#COLOPHON)COLOPHON

           This page is part of the groff (GNU troff) project.  Information
           about the project can be found at 
           ⟨http://www.gnu.org/software/groff/⟩.  If you have a bug report for
           this manual page, see ⟨http://www.gnu.org/software/groff/⟩.  This
           page was obtained from the tarball groff-1.24.1.tar.gz fetched
           from ⟨https://ftp.gnu.org/gnu/groff/⟩ on 2026-08-04.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    groff 1.24.1                    2026-03-14                       nroff(1)

------------------------------------------------------------------------

Pages that refer to this page: [col(1)](../man1/col.1.html),  [colcrt(1)](../man1/colcrt.1.html),  [less(1)](../man1/less.1.html),  [man(1)](../man1/man.1.html),  [ul(1)](../man1/ul.1.html),  [zsoelim(1)](../man1/zsoelim.1.html)

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
