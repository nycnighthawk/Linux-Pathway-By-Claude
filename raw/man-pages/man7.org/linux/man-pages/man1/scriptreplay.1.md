---
{"title": "scriptreplay(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/scriptreplay.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# scriptreplay(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXAMPLES](#EXAMPLES) \| [KEY BINDINGS](#KEY_BINDINGS) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SCRIPTREPLAY(1)               User Commands               SCRIPTREPLAY(1)

## [](#NAME)NAME

           scriptreplay - play back typescripts, using timing information

## [](#SYNOPSIS)SYNOPSIS

           scriptreplay [options] timingfile [typescript [divisor]]

## [](#DESCRIPTION)DESCRIPTION

           This program replays a typescript, using timing information to
           ensure that output happens in the same rhythm as it originally
           appeared when the script was recorded.

           The replay simply displays the information again; the programs
           that were run when the typescript was being recorded are not run
           again. Since the same information is simply being displayed,
           scriptreplay is only guaranteed to work properly if run on the
           same type of terminal the typescript was recorded on. Otherwise,
           any escape characters in the typescript may be interpreted
           differently by the terminal to which scriptreplay is sending its
           output.

           The timing information is what script(1) outputs to file specified
           by --log-timing.

           By default, the typescript to display is assumed to be named
           typescript, but other filenames may be specified, as the second
           parameter or with option --log-out.

           If the third parameter or --divisor is specified, it is used as a
           speed-up multiplier. For example, a speed-up of 2 makes
           scriptreplay go twice as fast, and a speed-down of 0.1 makes it go
           ten times slower than the original session.

           During the replay, you can interactively speed up, slow down,
           pause or step through the playback using the Up, Down, Space and
           Right keys.

## [](#OPTIONS)OPTIONS

           -I, --log-in file
               File containing script's terminal input.

           -O, --log-out file
               File containing script's terminal output.

           -B, --log-io file
               File containing script's terminal output and input.

           -t, --timing file
               File containing script's timing output. This option replaces
               the timingfile positional argument.

           -T, --log-timing file
               This is an alias for -t, maintained for compatibility with
               script(1) command-line options.

           -s, --typescript file
               Deprecated alias of --log-out.

           -c, --cr-mode mode
               Specifies how to handle the CR (carriage return, 0x0D)
               character from log files. The default mode is auto, in which
               case CR is replaced with a line break for the stdin log,
               because otherwise scriptreplay would overwrite the same line.
               The other modes are never and always.

           -d, --divisor number
               Speed up the replay displaying this number of times. The
               argument is a floating-point number. It’s called divisor
               because it divides the timings by this factor. This option
               overrides old-style arguments.

           -m, --maxdelay number
               Set the maximum delay between updates to number of seconds.
               The argument is a floating-point number. This can be used to
               avoid long pauses in the typescript replay.

           --summary
               Display details about the session recorded in the specified
               timing file and exit. The session must have been recorded
               using the advanced format (see script(1) option
               --logging-format for more details).

           -x, --stream type
               Forces scriptreplay to print only the specified stream. The
               supported stream types are in, out, signal, and info. This
               option is recommended for multi-stream logs (created with
               --log-io) in order to print only the desired data.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           SCRIPTREPLAY_DEBUG=all
               Enable scriptreplay debug output.

## [](#EXAMPLES)EXAMPLES

               % script --log-timing file.tm --log-out script.out
               Script started, file is script.out
               % ls
               <etc, etc>
               % exit
               Script done, file is script.out
               % scriptreplay --log-timing file.tm --log-out script.out

## [](#KEY_BINDINGS)KEY BINDINGS

           The following keys control the playback of the script:

           •   Space: Toggles pause and unpause. Press this key to pause the
               playback, and press it again to resume.

           •   Up Arrow: Increases the playback speed. Each press of this key
               will make the script replay faster by x0.1.

           •   Down Arrow: Decreases the playback speed. Each press of this
               key will slow down the script replay by x0.1.

           •   Right Arrow: Advances the playback by one step. Each press of
               this key will immediately display the current step instead of
               waiting its specified delay.

## [](#AUTHORS)AUTHORS

           The original scriptreplay program was written by Joey Hess
           <joey@kitenet.net>. The program was re-written in C by James
           Youngman <jay@gnu.org> and Karel Zak <kzak@redhat.com>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2008 James Youngman

           Copyright © 2008-2019 Karel Zak

           Copyright © 2024 Jonathan Ketchker

           This is free software; see the source for copying conditions.
           There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR
           A PARTICULAR PURPOSE.

           Released under the GNU General Public License version 2 or later.

## [](#SEE_ALSO)SEE ALSO

           script(1), scriptlive(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The scriptreplay command is part of the util-linux package which
           can be downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                SCRIPTREPLAY(1)

------------------------------------------------------------------------

Pages that refer to this page: [script(1)](../man1/script.1.html),  [scriptlive(1)](../man1/scriptlive.1.html)

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
