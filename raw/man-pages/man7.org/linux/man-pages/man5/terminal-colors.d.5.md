---
{"title": "terminal-colors.d(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/terminal-colors.d.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# terminal-colors.d(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DEFAULT SCHEME FILES FORMAT](#DEFAULT_SCHEME_FILES_FORMAT) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [COMPATIBILITY](#COMPATIBILITY) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TERMINAL-COLORS.D(5)           File formats          TERMINAL-COLORS.D(5)

## [](#NAME)NAME

           terminal-colors.d - configure output colorization for various
           utilities

## [](#SYNOPSIS)SYNOPSIS

           /etc/terminal-colors.d/[name.|[name]@term.]type

## [](#DESCRIPTION)DESCRIPTION

           Files in this directory determine the default behavior for
           utilities when coloring output.

           The name is a utility name. The name is optional and when none is
           specified then the file is used for all unspecified utilities.

           The term is a terminal identifier (the TERM environment variable).
           The terminal identifier is optional and when none is specified
           then the file is used for all unspecified terminals.

           The type is a file type. Supported file types are:

              disable
                  Turns off output colorization for all compatible
                  utilities. See also the NO_COLOR environment variable
                  below.

              enable
                  Turns on output colorization; any matching disable
                  files are ignored.

              scheme
                  Specifies colors used for output. The file format may
                  be specific to the utility, the default format is
                  described below.

           If there are more files that match for a utility, then the file
           with the more specific filename wins. For example, the filename
           @xterm.scheme has less priority than dmesg@xterm.scheme. The
           lowest priority are those files without a utility name and
           terminal identifier (e.g., "disable").

           The user-specific $XDG_CONFIG_HOME/terminal-colors.d or
           $HOME/.config/terminal-colors.d overrides the global setting.

## [](#DEFAULT_SCHEME_FILES_FORMAT)DEFAULT SCHEME FILES FORMAT

           The following statement is recognized:

              name color-sequence

           The name is a logical name for the color sequence (for example:
           error). The names are specific to the utilities. For more details
           always see the COLORS section in the man page for the utility.

           The color-sequence can be a color name, an ANSI color sequence, or
           an escape sequence.

       Color names
           Valid color names are: black, blink, blue, bold, brown, cyan,
           darkgray, gray, green, halfbright, lightblue, lightcyan,
           lightgray, lightgreen, lightmagenta, lightred, magenta, red,
           reset, reverse, and yellow.

       ANSI color sequences
           An ANSI color sequence is composed of sequences of numbers
           separated by semicolons. The most common codes are:
           ┌────┬──────────────────────────┐
           │    │                          │
           │ 0  │ to restore default color │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 1  │ for brighter colors      │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 4  │ for underlined text      │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 5  │ for flashing text        │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 30 │ for black foreground     │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 31 │ for red foreground       │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 32 │ for green foreground     │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 33 │ for yellow (or brown)    │
           │    │ foreground               │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 34 │ for blue foreground      │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 35 │ for purple foreground    │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 36 │ for cyan foreground      │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 37 │ for white (or gray)      │
           │    │ foreground               │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 40 │ for black background     │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 41 │ for red background       │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 42 │ for green background     │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 43 │ for yellow (or brown)    │
           │    │ background               │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 44 │ for blue background      │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 45 │ for purple background    │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 46 │ for cyan background      │
           ├────┼──────────────────────────┤
           │    │                          │
           │ 47 │ for white (or gray)      │
           │    │ background               │
           └────┴──────────────────────────┘

           For example, to use a red background for alert messages in the
           output of dmesg(1), use:

             echo 'alert 37;41' >> /etc/terminal-colors.d/dmesg.scheme

       Escape sequences
           An escape sequence is needed to enter a space, backslash, caret,
           or any control character anywhere in a string, as well as a hash
           mark as the first character. These C-style backslash-escapes can
           be used:
           ┌─────┬─────────────────────────┐
           │     │                         │
           │ \a  │ Bell (ASCII 7)          │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \b  │ Backspace (ASCII 8)     │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \e  │ Escape (ASCII 27)       │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \f  │ Form feed (ASCII 12)    │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \n  │ Newline (ASCII 10)      │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \r  │ Carriage Return (ASCII  │
           │     │ 13)                     │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \t  │ Tab (ASCII 9)           │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \v  │ Vertical Tab (ASCII 11) │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \?  │ Delete (ASCII 127)      │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \_  │ Space                   │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \\  │ Backslash (\)           │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \^  │ Caret (^)               │
           ├─────┼─────────────────────────┤
           │     │                         │
           │ \\# │ Hash mark (#)           │
           └─────┴─────────────────────────┘

       Comments
           Lines where the first non-blank character is a # (hash) are
           ignored. Any other use of the hash character is not interpreted as
           introducing a comment.

## [](#ENVIRONMENT)ENVIRONMENT

           NO_COLOR
               Disable output colorization unless explicitly enabled by a
               command-line option. See https://no-color.org/ for more
               details. Supported since util-linux version 2.41.

           TERMINAL_COLORS_DEBUG=all
               Enable terminal colors debug output.

## [](#FILES)FILES

           $XDG_CONFIG_HOME/terminal-colors.d

           $HOME/.config/terminal-colors.d

           /etc/terminal-colors.d

## [](#EXAMPLES)EXAMPLES

           Disable colors for all compatible utilities:

              touch /etc/terminal-colors.d/disable

           Disable colors for all compatible utils on a vt100 terminal:

              touch /etc/terminal-colors.d/@vt100.disable

           Disable colors for all compatible utils except dmesg(1):

              touch /etc/terminal-colors.d/disable
              touch /etc/terminal-colors.d/dmesg.enable

## [](#COMPATIBILITY)COMPATIBILITY

           The terminal-colors.d functionality is currently supported by all
           util-linux utilities which provide colorized output. For more
           details always see the COLORS section in the man page for the
           utility.

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           terminal-colors.d is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24           TERMINAL-COLORS.D(5)

------------------------------------------------------------------------

Pages that refer to this page: [cal(1)](../man1/cal.1.html),  [column(1)](../man1/column.1.html),  [dmesg(1)](../man1/dmesg.1.html),  [hexdump(1)](../man1/hexdump.1.html),  [cfdisk(8)](../man8/cfdisk.8.html),  [fdisk(8)](../man8/fdisk.8.html),  [lsblk(8)](../man8/lsblk.8.html),  [sfdisk(8)](../man8/sfdisk.8.html)

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
