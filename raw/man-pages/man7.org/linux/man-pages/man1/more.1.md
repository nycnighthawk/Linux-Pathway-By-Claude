---
{"title": "more(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/more.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# more(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMANDS](#COMMANDS) \| [SECURITY](#SECURITY) \| [ENVIRONMENT](#ENVIRONMENT) \| [HISTORY](#HISTORY) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MORE(1)                       User Commands                       MORE(1)

## [](#NAME)NAME

           more - display the contents of a file in a terminal

## [](#SYNOPSIS)SYNOPSIS

           more [options] file ...

## [](#DESCRIPTION)DESCRIPTION

           more is a filter for paging through text one screenful at a time.
           This version is especially primitive. Users should realize that
           less(1) provides more(1) emulation plus extensive enhancements.

## [](#OPTIONS)OPTIONS

           Options are also taken from the environment variable MORE (make
           sure to precede them with a dash (-)) but command-line options
           will override those.

           -d, --silent
               Prompt with "[Press space to continue, 'q' to quit.]", and
               display "[Press 'h' for instructions.]" instead of ringing the
               bell when an illegal key is pressed.

           -l, --logical
               Do not pause after any line containing a ^L (form feed).

           -e, --exit-on-eof
               Exit on End-Of-File, enabled by default if POSIXLY_CORRECT
               environment variable is not set or if not executed on
               terminal.

           -f, --no-pause
               Count logical lines, rather than screen lines (i.e., long
               lines are not folded).

           -p, --print-over
               Do not scroll. Instead, clear the whole screen and then
               display the text. Notice that this option is switched on
               automatically if the executable is named page.

           -c, --clean-print
               Do not scroll. Instead, paint each screen from the top,
               clearing the remainder of each line as it is displayed.

           -s, --squeeze
               Squeeze multiple blank lines into one.

           -u, --plain
               Suppress underlining. This option is silently ignored as
               backwards compatibility.

           -n, --lines number
               Specify the number of lines per screenful. The number argument
               is a positive decimal integer. The --lines option shall
               override any values obtained from any other source, such as
               number of lines reported by terminal.

           -number
               A numeric option means the same as --lines option argument.

           +number
               Start displaying each file at line number.

           +/string
               The string to be searched in each file before starting to
               display it.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#COMMANDS)COMMANDS

           Interactive commands for more are based on vi(1). Some commands
           may be preceded by a decimal number, called k in the descriptions
           below. In the following descriptions, ^X means control-X.

           h or ?
               Help; display a summary of these commands. If you forget all
               other commands, remember this one.

           SPACE
               Display next k lines of text. Defaults to current screen size.

           z
               Display next k lines of text. Defaults to current screen size.
               Argument becomes new default.

           RETURN
               Display next k lines of text. Defaults to 1. Argument becomes
               new default.

           d or ^D
               Scroll k lines. Default is current scroll size, initially 11.
               Argument becomes new default.

           q or Q or INTERRUPT
               Exit.

           s
               Skip forward k lines of text. Defaults to 1.

           f
               Skip forward k screenfuls of text. Defaults to 1.

           b or ^B
               Skip backwards k screenfuls of text. Defaults to 1. Only works
               with files, not pipes.

           '
               Go to the place where the last search started.

           =
               Display current line number.

           /pattern
               Search for kth occurrence of regular expression. Defaults to
               1.

           n
               Search for kth occurrence of last regular expression. Defaults
               to 1.

           !command or :!command
               Execute command in a subshell.

           v
               Start up an editor at current line. The editor is taken from
               the environment variable VISUAL if defined, or EDITOR if
               VISUAL is not defined, or defaults to vi(1) if neither VISUAL
               nor EDITOR is defined.

           ^L
               Redraw screen.

           :n
               Go to kth next file. Defaults to 1.

           :p
               Go to kth previous file. Defaults to 1.

           :f
               Display current filename and line number.

           .
               Repeat previous command.

## [](#SECURITY)SECURITY

           When either MORESECURE or PAGERSECURE is set, more will run in
           "secure" mode and effectively disable the following commands:

           !command or :!command
               Execute command in a subshell.

           v
               Start up an editor.

## [](#ENVIRONMENT)ENVIRONMENT

           EDITOR
               Override the default editor when VISUAL is not specified.

           MORE
               Specify favored options for more.

           MORESECURE
               Run more in "secure" mode. See SECURITY for details.

           MORE_SHELL_LINES
               Specify the number of lines the shell prompt occupies on the
               terminal screen. If this value is set, the number of lines for
               the shell prompt is subtracted from the number of lines used
               to print a page on the screen. The value must be greater than
               zero and less than the current number of lines per screen;
               otherwise it is silently ignored. This is useful in situations
               where the printed page has to remain on the screen after
               exiting more(1) without scrolling up too much as the shell
               prints a new prompt.

           PAGERSECURE
               Equivalent to MORESECURE.

           POSIXLY_CORRECT
               Disable exit-on-eof (see option -e for more details).

           SHELL
               Override the default shell. If SHELL is not set, the shell
               from the user’s passwd(5) entry is used. If no shell is
               defined there either, /bin/sh is used as the fallback.

           TERM
               Specify the terminal type used by more to get the terminal
               characteristics necessary to manipulate the screen.

           VISUAL
               Override the default editor to use when command key v is
               pressed.

## [](#HISTORY)HISTORY

           The more command appeared in 3.0BSD. This man page documents more
           version 5.19 (Berkeley 6/29/88), which is currently in use in the
           Linux community. Documentation was produced using several other
           versions of the man page, and extensive inspection of the source
           code.

## [](#AUTHORS)AUTHORS

           Eric Shienbrood, UC Berkeley.

           Modified by Geoff Peck, UCB to add underlining, single spacing.

           Modified by John Foderaro, UCB to add -c and MORE environment
           variable.

           Modified by Christian Goeschel Ndjomouo to add MORESECURE,
           PAGERSECURE and MORE_SHELL_LINES environment variables, and a
           SECURITY section

## [](#SEE_ALSO)SEE ALSO

           less(1), vi(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The more command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                        MORE(1)

------------------------------------------------------------------------

Pages that refer to this page: [bash(1)](../man1/bash.1.html),  [colcrt(1)](../man1/colcrt.1.html),  [dpkg(1)](../man1/dpkg.1.html),  [dpkg-query(1)](../man1/dpkg-query.1.html),  [homectl(1)](../man1/homectl.1.html),  [importctl(1)](../man1/importctl.1.html),  [journalctl(1)](../man1/journalctl.1.html),  [less(1)](../man1/less.1.html),  [localectl(1)](../man1/localectl.1.html),  [loginctl(1)](../man1/loginctl.1.html),  [machinectl(1)](../man1/machinectl.1.html),  [more(1)](../man1/more.1.html),  [portablectl(1)](../man1/portablectl.1.html),  [storagectl(1)](../man1/storagectl.1.html),  [systemctl(1)](../man1/systemctl.1.html),  [systemd(1)](../man1/systemd.1.html),  [systemd-analyze(1)](../man1/systemd-analyze.1.html),  [systemd-inhibit(1)](../man1/systemd-inhibit.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [systemd-vmspawn(1)](../man1/systemd-vmspawn.1.html),  [timedatectl(1)](../man1/timedatectl.1.html),  [updatectl(1)](../man1/updatectl.1.html),  [userdbctl(1)](../man1/userdbctl.1.html),  [readline(3)](../man3/readline.3.html),  [environ(7)](../man7/environ.7.html),  [systemd-tmpfiles(8)](../man8/systemd-tmpfiles.8.html)

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
