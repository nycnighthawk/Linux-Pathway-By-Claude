---
{"title": "captoinfo(1m) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/captoinfo.1m.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# captoinfo(1m) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [EXTENSIONS](#EXTENSIONS) \| [PORTABILITY](#PORTABILITY) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    captoinfo(1M)                 User commands                 captoinfo(1M)

## [](#NAME)NAME

           captoinfo - convert a termcap description into a terminfo
           description

## [](#SYNOPSIS)SYNOPSIS

           captoinfo [tic-option] [file ...]

           captoinfo -V

## [](#DESCRIPTION)DESCRIPTION

           captoinfo translates terminal descriptions.  It looks in each
           given text file for termcap entries and, for each one found,
           writes an equivalent terminfo description to the standard output
           stream.  termcap tc capabilities translate to terminfo “use”
           capabilities.

           If no files are specified, captoinfo interprets the content of the
           environment variable TERMCAP as a file name, and extracts only the
           entry for the terminal type named in the environment variable TERM
           from it.  If the environment variable TERMCAP is not set,
           captoinfo reads /etc/termcap.

           This utility is implemented as a link to tic(1M), with the
           latter's -I option implied.  You can use other tic options such as
           -1, -f, -v, -w, and -x.  The -V option reports the version of
           ncurses associated with this program and exits with a successful
           status.

       Translations from Nonstandard Capabilities
           captoinfo translates some obsolete, nonstandard capabilities into
           standard terminfo capabilities.  It issues a diagnostic to the
           standard error stream for each, inviting the user to check that it
           has not mistakenly translated an unknown or mistyped capability
           name.

                   [1mtermcap[24m Code
                Obsolete   Standard    Origin      terminfo capability
                ─────────────────────────────────────────────────────────
                   BO         mr        AT&T      enter_reverse_mode
                   CI         vi        AT&T      cursor_invisible
                   CV         ve        AT&T      cursor_normal
                   DS         mh        AT&T      enter_dim_mode
                   EE         me        AT&T      exit_attribute_mode
                   FE         LF        AT&T      label_on
                   FL         LO        AT&T      label_off
                   XS         mk        AT&T      enter_secure_mode
                   EN         @7        XENIX     key_end
                   GE         ae        XENIX     exit_alt_charset_mode
                   GS         as        XENIX     enter_alt_charset_mode
                   HM         kh        XENIX     key_home
                   LD         kL        XENIX     key_dl
                   PD         kN        XENIX     key_npage
                   PN         po        XENIX     prtr_off
                   PS         pf        XENIX     prtr_on
                   PU         kP        XENIX     key_ppage
                   RT         @8        XENIX     kent
                   UP         ku        XENIX     kcuu1
                   KA         k;      Tektronix   key_f10
                   KB         F1      Tektronix   key_f11
                   KC         F2      Tektronix   key_f12
                   KD         F3      Tektronix   key_f13
                   KE         F4      Tektronix   key_f14
                   KF         F5      Tektronix   key_f15
                   BC         Sb      Tektronix   set_background
                   FC         Sf      Tektronix   set_foreground
                   HS         mh        IRIX      enter_dim_mode

           XENIX termcap had a set of extension capabilities, corresponding
           to box drawing characters of CCSID (“code page”) 437, as follows.

                        [1mtermcap[24m Code            Graphic
                        ─────────────────────────────────────────
                             G2        upper left corner
                             G3        lower left corner
                             G1        upper right corner
                             G4        lower right corner
                             GR        tee pointing right
                             GL        tee pointing left
                             GU        tee pointing up
                             GD        tee pointing down
                             GH        horizontal line
                             GV        vertical line
                             GC        intersection
                             G6        double upper left corner
                             G7        double lower left corner
                             G5        double upper right corner
                             G8        double lower right corner
                             Gr        double tee pointing right
                             Gr        double tee pointing left
                             Gu        double tee pointing up
                             Gd        double tee pointing down
                             Gh        double horizontal line
                             Gv        double vertical line
                             Gc        double intersection
                             GG        ACS magic cookie count

           captoinfo composes single-line box-drawing capabilities into a
           terminfo acs_chars (acsc) string capability, and discards GG and
           double-line capabilities with a warning diagnostic.

           AIX has a terminfo facility descended from SVr2 terminfo, but
           which is incompatible with the SVr4 format.  captoinfo translates
           the following AIX extensions.

                                      IBM    X/Open
                                     ───────────────
                                     ksel    kslt
                                     kbtab   kcbt
                                     font0   s0ds
                                     font1   s1ds
                                     font2   s2ds
                                     font3   s3ds

           It furthermore translates the AIX box1 capability to an acs_chars
           (acsc) string capability.

           The HP-UX terminfo library supports two nonstandard terminfo
           capabilities: memory_lock (meml) and memory_unlock (memu).
           captoinfo discards these with a warning message.

## [](#FILES)FILES

           /etc/termcap
                  default termcap terminal capability database

## [](#EXTENSIONS)EXTENSIONS

           This command is an SVr4 curses and ncurses extension.

## [](#PORTABILITY)PORTABILITY

           X/Open Curses Issue 7 (2009) does not specify this command.

           SVr4 systems provide captoinfo as a separate application from tic.
           Its -v option does not accept a trace level argument n; repeat -v
           n times instead.

           NetBSD does not provide this application.

## [](#AUTHORS)AUTHORS

           Eric S. Raymond <esr@snark.thyrsus.com> and
           Thomas E. Dickey <dickey@invisible-island.net>

## [](#SEE_ALSO)SEE ALSO

           infocmp(1M), tic(1M), curses(3X), terminfo(5)

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

    ncurses @NCURSES_MAJOR@.@NCU... 2025-11-11                  captoinfo(1M)

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
