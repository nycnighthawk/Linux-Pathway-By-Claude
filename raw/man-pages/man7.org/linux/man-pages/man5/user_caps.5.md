---
{"title": "user_caps(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/user_caps.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# user_caps(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PORTABILITY](#PORTABILITY) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    user_caps(5)                   File formats                  user_caps(5)

## [](#NAME)NAME

           user_caps - user-defined terminfo capability format

## [](#SYNOPSIS)SYNOPSIS

           infocmp -x

           tic -x

## [](#DESCRIPTION)DESCRIPTION

       Background
           Prior to ncurses 5.0 (1999), terminfo databases used a fixed
           repertoire of terminal capabilities designed for the SVr2 terminal
           database in 1984, added to in stages through SVr4 (1989), and
           standardized in X/Open Curses starting in 1995.

           Most such additions to this fixed repertoire suppelmented the
           tables of Boolean, numeric, and string capabilities.  Rather than
           changing the meaning of an existing capability, a new name was
           added.  The terminfo database uses a binary format; binary
           compatibility was ensured by using a header that counted the
           number of items in the tables for each type of capability.
           Because each curses vendor extended the standard capability lists
           in distinct ways, a library could be programmed to recognize only
           compiled terminfo entries that it was prepared to interpret.
           Standardization was incomplete.

           •   X/Open Curses describes only the source format, not its binary
               representation on disk.

               Library developers rely upon SVr4 documentation and reverse
               engineering of compiled terminfo files to match the binary
               format.

           •   Lacking a standard for the binary format, most implementations
               copy the SVr2 binary format, which uses 16-bit signed
               integers, and is limited to 4096-byte entries.

               The SVr2 format cannot represent very large numeric capability
               values, nor can it represent large numbers of key definitions,
               as are required to distinguish multiple modifier keys used in
               combination with a function key.

           •   The tables of capability names differ between implementations.

               Although they may provide all of the standard capability
               names, each arranges its table entries differently because
               some features were added as needed, while others were added —
               out of order — for X/Open Curses conformance.

               While ncurses's capability repertoire is closest to that of
               Solaris, the set of capabilities supported by each vendor's
               terminfo database differs from the list published by X/Open
               Curses.  ncurses can be configured with tables that match the
               terminal databases for AIX, HP-UX, or OSF/1, rather than the
               default Solaris-like configuration.

           •   In SVr4 curses and ncurses, the terminal database is defined
               at compile time by interpolating a text file that lists the
               different terminal capabilities.

               In principle, the text file can be extended, but doing so
               requires recompiling and reinstalling the library.  The text
               file used by ncurses for terminal capabilities includes
               details of extensions to X/Open Curses made by various
               systems.  For example, ncurses supports the following
               nonstandard capabilities in each configuration.

                   memory_lock
                        (meml) lock memory above cursor

                   memory_unlock
                        (memu) unlock memory

                   box_chars_1
                        (box1) box characters primary set

               The memory lock/unlock capabilities were included because they
               were used in the X11R6 terminal description for xterm(1).  tic
               uses the box1 capability to cope with terminal descriptions
               written for AIX.

           During the 1990s, some application developers were reluctant to
           use terminfo in spite of its performance (and other) advantages
           over termcap.

           •   The fixed repertoire prevented users from adding support for
               terminal features unanticipated by X/Open Curses (or required
               them to reuse existing capabilities as a workaround).

           •   The limitation to 16-bit signed integers was also mentioned.
               Because termcap stores everything as a string, it could
               represent larger numbers.

           Although termcap's extensibility was rarely used — the claimant
           was never an implementor who had actually exercised it — the
           criticism had a point.  ncurses 5.0 provided a way to detect
           nonstandard capabilities, to determine their type, and to
           optionally store and retrieve them in a way that did not interfere
           with other applications.  ncurses terms these user-defined
           capabilities because no modifications to the standard capability
           list are needed.

           The ncurses utilities tic and infocmp have a command-line option
           “-x” to control whether the nonstandard capabilities are stored or
           retrieved.  ncurses provides use_extended_names(3X) to programs
           for the same purpose.

           When compiling a terminal database, if “-x” is used, tic stores a
           user-defined capability if the capability name is not standard.

           Because ncurses provides a termcap library interface, these user-
           defined capabilities may be visible to termcap applications.

           •   The termcap interface (like all implementations of termcap)
               restricts capability names to two characters.

               When the capability is simple enough for use in a termcap
               application, it is provided as a two-character name.

           •   Other user-defined capabilities employ features not usable in
               termcap, such as parameterized strings that use more than two
               parameters or require more powerful expressions than termcap
               supports.  Such capabilities should, in the terminfo database,
               have names at least three characters in length.

           •   Some terminals can send distinct strings for special keys
               (cursor-, keypad- or function-keys) depending on modifier keys
               (shift, control, etc.).  While terminfo and termcap define a
               set of sixty function key names, to which a series of keys can
               be assigned, that is insufficient for more than a dozen keys
               multiplied by more than a couple of modifier combinations.
               The ncurses database uses a convention based on xterm(1) to
               provide extended special-key names.

               Fitting that into termcap's limitation of 2-character names
               would be pointless.  These extended keys are available only
               with terminfo.

       Recognized Capabilities
           The ncurses library employs user-definable capabilities.  While
           the terminfo database may have other extensions, ncurses makes
           explicit checks for the following.

              AX (Boolean) asserts that the terminal interprets SGR 39 and
                 SGR 49 by resetting the foreground and background colors,
                 respectively, to the default.

                 screen(1) recognizes this capability as well.

              E3 (string) tells an application how to clear the terminal's
                 scrollback buffer.  When present, the clear(1) program sends
                 this before clearing the terminal.

                 The command “tput clear” does the same thing.

              NQ (Boolean) suppresses a consistency check in tic for the
                 ncurses string capabilities user6 (u6) through user9 (u9),
                 which tell an application how to query the terminal's cursor
                 position and its device attributes.

              RGB
                 (Boolean, numeric, or string) asserts that the
                 set_a_foreground (setaf) and set_a_background (setab)
                 capabilities employ direct colors, using an RGB
                 (red/green/blue) convention.  This capability allows
                 color_content(3X) to return appropriate values without
                 requiring the application to initialize colors using
                 init_color(3X).

                 The capability type determines the values ncurses sees.

                 Boolean
                    implies that the number of bits for red, green, and blue
                    are the same.  Starting with the value of the capability
                    max_colors (colors; termcap: co), ncurses adds two,
                    divides the sum by three, and assigns the result to red,
                    green, and blue, in that order.

                    If the number of bits needed for the number of colors is
                    not a multiple of three, the blue (and green) color
                    channels lose in comparison to red.

                 numeric
                    tells ncurses what result to add to red, green, and blue.
                    If ncurses runs out of bits, blue (and green) lose just
                    as in the Boolean case.

                 string
                    specify the quantity of bits used for red, green, and
                    blue color channels as a slash-separated list of decimal
                    integers.

                 Because there are several RGB encodings in use, applications
                 that make assumptions about the number of bits per color
                 channel are unlikely to work reliably.  As a trivial case,
                 one could define RGB#1 to represent the standard eight
                 ANSI X3.64/ECMA-48/ISO 6429 colors using one bit per color
                 channel.

              U8 (numeric) asserts whether ncurses must use Unicode values
                 for line-drawing characters, and that it should ignore the
                 alternate character set (ACS) capabilities when the locale
                 uses UTF-8 encoding.  See the discussion of
                 NCURSES_NO_UTF8_ACS in section “ENVIRONMENT” of ncurses(3X).

                 Set this capability to a nonzero value to enable it.

              XM (string) override ncurses's built-in string that directs
                 xterm(1) to enable or disable mouse mode.

                 ncurses sends a character sequence to the terminal to
                 initialize mouse mode, and when the user clicks the mouse
                 buttons or (in certain modes) moves the mouse, handles the
                 characters sent back by the terminal to tell the application
                 what was done with the mouse.

                 The mouse protocol is enabled when the mask argument to the
                 mousemask(3X) function is nonzero.  By default, ncurses
                 handles the responses for the X11 xterm mouse protocol.  It
                 also knows about the SGR 1006 xterm mouse protocol, but must
                 to be told to look for it specifically.  ncurses is not be
                 able to guess which of the two modes is used, because the
                 responses are enough alike that only confusion would result.

                 The XM capability has a single numeric parameter.  If
                 nonzero, the mouse protocol should be enabled.  If zero, the
                 mouse protocol should be disabled.  ncurses inspects this
                 capability if it is present, to see whether the 1006
                 protocol is used.  If so, it expects the responses to use
                 the SGR 1006 xterm mouse protocol.

                 The xterm mouse protocol is used by other terminal
                 emulators.  The terminal database uses building blocks for
                 the various xterm mouse protocols usable in customized
                 terminal descriptions.

                 The terminal database building blocks for this mouse feature
                 also have an experimental capability, xm, that describes the
                 mouse response.  No known interpreter uses this information,
                 which could make mouse support completely data-driven.

                 xm shows the format of the mouse responses.  In this
                 experimental capability, the parameters are as follows.

                   p1   y-ordinate

                   p2   x-ordinate

                   p3   button

                   p4   state, e.g., pressed or released

                   p5   y-ordinate starting region

                   p6   x-ordinate starting region

                   p7   y-ordinate ending region

                   p8   x-ordinate ending region

                 Here are examples from the terminal database for the most
                 commonly used xterm mouse protocols.

                   xterm+x11mouse|X11 xterm mouse protocol,
                           kmous=\E[M, XM=\E[?1000%?%p1%{1}%=%th%el%;,
                           xm=\E[M
                              %?%p4%t%p3%e%{3}%;%' '%+%c
                              %p2%'!'%+%c
                              %p1%'!'%+%c,

                   xterm+sm+1006|xterm SGR-mouse,
                           kmous=\E[<, XM=\E[?1006;1000%?%p1%{1}%=%th%el%;,
                           xm=\E[<%i%p3%d;
                              %p1%d;
                              %p2%d;
                              %?%p4%tM%em%;,

       Extended Key Definitions
           Several terminals provide the ability to send distinct strings for
           combinations of modified special keys.  There is no standard for
           what those keys can send.

           Since 1999, xterm(1) has supported shift, control, alt, and meta
           modifiers which produce distinct special-key strings.  In a
           terminal description, ncurses has no special knowledge of the
           modifiers used.  Applications can use the naming convention
           established for xterm to find these special keys in the terminal
           description.

           Starting with the curses convention that capability codes
           describing the input generated by a terminal's key caps begin with
           “k”, and that shifted special keys use uppercase letters in their
           names, ncurses's terminal database defines the following names and
           codes to which a suffix is added.

                Code   Description
                ──────────────────────────────────────────────────────────────
                kDC    shifted kdch1 (delete character)
                kDN    shifted kcud1 (cursor down)
                kEND   shifted kend (end)
                kHOM   shifted khome (home)
                kLFT   shifted kcub1 (cursor back)
                kNXT   shifted knext (next)
                kPRV   shifted kprev (previous)
                kRIT   shifted kcuf1 (cursor forward)
                kUP    shifted kcuu1 (cursor up)

           Keycap nomenclature on the Unix systems for which curses was
           developed differs from today's ubiquitous descendants of the IBM
           PC/AT keyboard layout.  In the foregoing, interpret “backward” as
           “left”, “forward” as “right”, “next” as “page down”, and
           “prev(ious)” as “page up”.

           These are the suffixes used to denote the modifiers:

                Value   Description
                ──────────────────────────────────
                2       Shift
                3       Alt
                4       Shift + Alt
                5       Control
                6       Shift + Control
                7       Alt + Control
                8       Shift + Alt + Control
                9       Meta
                10      Meta + Shift
                11      Meta + Alt
                12      Meta + Alt + Shift
                13      Meta + Ctrl
                14      Meta + Ctrl + Shift
                15      Meta + Ctrl + Alt
                16      Meta + Ctrl + Alt + Shift

           ncurses defines no capabilities for modified F-keys; terminal
           descriptions can refer to names that ncurses allocates at runtime
           to key codes.  To use these keys in an ncurses program, an
           application could do this:

           •   using a list of extended key names, ask tigetstr(3X) for their
               values, and

           •   given the list of values, ask key_defined(3X) for the key-code
               which would be returned for those keys by wgetch(3X).

## [](#PORTABILITY)PORTABILITY

           The “-x” extension feature of tic and infocmp has been adopted in
           NetBSD curses.  That implementation stores user-defined
           capabilities, but makes no use of these capabilities itself.

## [](#AUTHORS)AUTHORS

           Thomas E. Dickey
           beginning with ncurses 5.0 (1999)

## [](#SEE_ALSO)SEE ALSO

           infocmp(1M), tic(1M)

           In the source form of the terminal database, terminfo.src, the
           section “NCURSES USER-DEFINABLE CAPABILITIES”.  summarizes
           commonly-used user-defined capabilities employed in the terminal
           descriptions.  Some of those features are mentioned in screen(1)
           or tmux(1).

           XTerm Control Sequences provides further information on the
           xterm(1) features that are used in these extended capabilities.

## [](#COLOPHON)COLOPHON

           This page is part of the ncurses (new curses) project.
           Information about the project can be found at 
           ⟨https://invisible-island.net/ncurses/ncurses.html⟩.  If you have a
           bug report for this manual page, send it to bug-ncurses@gnu.org.
           This page was obtained from the tarball ncurses-6.6.tar.gz fetched
           from ⟨https://ftp.gnu.org/gnu/ncurses/⟩ on 2026-08-04.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    ncurses @NCURSES_MAJOR@.@NCU... 2025-11-11                   user_caps(5)

------------------------------------------------------------------------

Pages that refer to this page: [infocmp(1m)](../man1/infocmp.1m.html),  [tic(1m)](../man1/tic.1m.html),  [tput(1)](../man1/tput.1.html),  [curs_termcap(3x)](../man3/curs_termcap.3x.html),  [ncurses(3x)](../man3/ncurses.3x.html),  [term(5)](../man5/term.5.html),  [terminfo(5)](../man5/terminfo.5.html)

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
