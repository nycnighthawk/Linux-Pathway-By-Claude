---
{"title": "scriptlive(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/scriptlive.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# scriptlive(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXAMPLES](#EXAMPLES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SCRIPTLIVE(1)                 User Commands                 SCRIPTLIVE(1)

## [](#NAME)NAME

           scriptlive - re-run session typescripts, using timing information

## [](#SYNOPSIS)SYNOPSIS

           scriptlive [options] timingfile typescript

## [](#DESCRIPTION)DESCRIPTION

           This program re-runs a typescript, using stdin typescript and
           timing information to ensure that input happens in the same rhythm
           as it originally appeared when the script was recorded.

           The session is executed in a newly created pseudoterminal with the
           user’s $SHELL, the shell from the user’s passwd(5) entry, or
           /bin/sh as the fallback.

           Be careful! The typescript may contain arbitrary commands. It is
           recommended to use "scriptreplay --stream in --log-in typescript"
           (or with --log-io instead of --log-in) to verify the typescript
           before it is executed with scriptlive.

           The timing information is what script(1) outputs to the file
           specified by --log-timing. The typescript has to contain stdin
           information, and is what script(1) outputs to the file specified
           by --log-in or --log-io.

## [](#OPTIONS)OPTIONS

           -c, --command command
               Execute command instead of an interactive shell. The command
               is passed as argument to the -c option of the execution shell.
               The used shell is either $SHELL, the shell defined in the
               user’s passwd(5) database or _PATH_BSHELL, selected in
               respective order.

           -I, --log-in file
               File containing script's terminal input.

           -B, --log-io file
               File containing script's terminal output and input.

           -E, --echo when
               This option controls the ECHO flag for the slave end of the
               session’s pseudoterminal. The supported modes are always,
               never, and auto.

               The default is auto — in which case ECHO is enabled. This
               default behavior is subject to change.

           -t, --timing file
               File containing script's timing output. This option replaces
               the timingfile positional argument.

           -T, --log-timing file
               An alias for -t; maintained for compatibility with the
               script(1) command-line options.

           -d, --divisor number
               Speed up the replay displaying this number of times. The
               argument is a floating-point number. It’s called divisor
               because it divides the timings by this factor. This option
               overrides old-style arguments.

           -m, --maxdelay number
               Set the maximum delay between updates to number of seconds.
               The argument is a floating-point number. This can be used to
               avoid long pauses in the typescript replay.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           SHELL
               Override the default shell. If SHELL is not set, the shell
               from the user’s passwd(5) entry is used. If no shell is
               defined there either, /bin/sh is used as the fallback.

           SCRIPTREPLAY_DEBUG=all
               Enable scriptreplay debug output.

           ULPTY_DEBUG=all
               Enable pty debug output.

## [](#EXAMPLES)EXAMPLES

               % script --log-timing file.tm --log-in script.in
               Script started, file is script.out
               % date
               <etc, etc>
               % exit
               Script done, file is script.out
               % scriptlive --log-timing file.tm --log-in script.in

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2019 Karel Zak

           This is free software; see the source for copying conditions.
           There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR
           A PARTICULAR PURPOSE.

           Released under the GNU General Public License version 2 or later.

## [](#SEE_ALSO)SEE ALSO

           script(1), scriptreplay(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The scriptlive command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                  SCRIPTLIVE(1)

------------------------------------------------------------------------

Pages that refer to this page: [script(1)](../man1/script.1.html),  [scriptreplay(1)](../man1/scriptreplay.1.html)

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
