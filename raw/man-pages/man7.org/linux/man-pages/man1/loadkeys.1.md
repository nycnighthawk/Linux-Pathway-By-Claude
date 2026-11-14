---
{"title": "loadkeys(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/loadkeys.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# loadkeys(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RESET TO DEFAULT](#RESET_TO_DEFAULT) \| [LOAD KERNEL KEYMAP](#LOAD_KERNEL_KEYMAP) \| [CONVERT XKB LAYOUTS](#CONVERT_XKB_LAYOUTS) \| [LOAD KERNEL ACCENT TABLE](#LOAD_KERNEL_ACCENT_TABLE) \| [LOAD KERNEL STRING TABLE](#LOAD_KERNEL_STRING_TABLE) \| [CREATE KERNEL SOURCE TABLE](#CREATE_KERNEL_SOURCE_TABLE) \| [CREATE BINARY KEYMAP](#CREATE_BINARY_KEYMAP) \| [CREATE TEXT KEYMAP](#CREATE_TEXT_KEYMAP) \| [UNICODE MODE](#UNICODE_MODE) \| [OTHER OPTIONS](#OTHER_OPTIONS) \| [WARNING](#WARNING) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LOADKEYS(1)              General Commands Manual              LOADKEYS(1)

## [](#NAME)NAME

           loadkeys - load keyboard translation tables

## [](#SYNOPSIS)SYNOPSIS

           loadkeys [OPTION]... FILENAME...
           loadkeys --default
           loadkeys --mktable
           loadkeys --bkeymap
           loadkeys --tkeymap[=shape]
           loadkeys --parse
           loadkeys --xkb-layout layout [XKB OPTION]...

## [](#DESCRIPTION)DESCRIPTION

           The program loadkeys reads the file or files specified by
           FILENAME....  Its main purpose is to load the kernel keymap for
           the console.  You can specify console device by the -C (or
           --console ) option.

## [](#RESET_TO_DEFAULT)RESET TO DEFAULT

           If the -d (or --default ) option is given, loadkeys loads a
           default keymap, probably the file defkeymap.map either in
           /usr/local/share/keymaps or in /usr/src/linux/drivers/tty/vt.
           (Probably the former was user-defined, while the latter is a
           qwerty keyboard map for PCs - maybe not what was desired.)
           Sometimes, with a strange keymap loaded (with the minus on some
           obscure unknown modifier combination) it is easier to type
           `loadkeys defkeymap.map'.

## [](#LOAD_KERNEL_KEYMAP)LOAD KERNEL KEYMAP

           The main function of loadkeys is to load or modify the keyboard
           driver's translation tables.  When specifying the file names,
           standard input can be denoted by dash (-). If no file is
           specified, the data is read from the standard input.

           For many countries and keyboard types appropriate keymaps are
           available already, and a command like `loadkeys uk' might do what
           you want. On the other hand, it is easy to construct one's own
           keymap. The user has to tell what symbols belong to each key. She
           can find the keycode for a key by use of showkey(1), while the
           keymap format is given in keymaps(5) and can also be seen from the
           output of dumpkeys(1).

## [](#CONVERT_XKB_LAYOUTS)CONVERT XKB LAYOUTS

           When loadkeys is built with XKB support, it can construct a Linux
           console keymap from XKB layout descriptions using libxkbcommon.
           This uses XKB as an input format for the Linux virtual console; it
           does not configure keyboard layouts for X11 or Wayland sessions.

           The XKB conversion path is selected when any --xkb-* option is
           used.  The selected XKB model, layout, variant and options are
           resolved through the standard evdev XKB rules.  The resulting
           symbols and compose entries are converted to the kernel keymap
           format and then handled like a parsed keymap file: the keymap can
           be loaded, checked with --parse, or written with output options
           such as --tkeymap.

           Not every XKB semantic has a direct Linux console equivalent.  The
           conversion preserves the console keymap behavior that can be
           represented by the kernel interfaces, including common layout,
           modifier, compose, keypad and virtual console switching mappings.

## [](#LOAD_KERNEL_ACCENT_TABLE)LOAD KERNEL ACCENT TABLE

           If the input file does not contain any compose key definitions,
           the kernel accent table is left unchanged, unless the -c (or
           --clearcompose ) option is given, in which case the kernel accent
           table is emptied.  If the input file does contain compose key
           definitions, then all old definitions are removed, and replaced by
           the specified new entries.  The kernel accent table is a sequence
           of (by default 68) entries describing how dead diacritical signs
           and compose keys behave.  For example, a line

                  compose ',' 'c' to ccedilla

           means that <ComposeKey><,><c> must be combined to <ccedilla>.  The
           current content of this table can be see using `dumpkeys
           --compose-only'.

## [](#LOAD_KERNEL_STRING_TABLE)LOAD KERNEL STRING TABLE

           The option -s (or --clearstrings ) clears the kernel string table.
           If this option is not given, loadkeys will only add or replace
           strings, not remove them.  (Thus, the option -s is required to
           reach a well-defined state.)  The kernel string table is a
           sequence of strings with names like F31. One can make function key
           F5 (on an ordinary PC keyboard) produce the text `Hello!', and
           Shift+F5 `Goodbye!' using lines

                  keycode 63 = F70 F71
                  string F70 = "Hello!"
                  string F71 = "Goodbye!"

           in the keymap.  The default bindings for the function keys are
           certain escape sequences mostly inspired by the VT100 terminal.

## [](#CREATE_KERNEL_SOURCE_TABLE)CREATE KERNEL SOURCE TABLE

           If the -m (or --mktable ) option is given loadkeys prints to the
           standard output a file that may be used as
           /usr/src/linux/drivers/tty/vt/defkeymap.c, specifying the default
           key bindings for a kernel (and does not modify the current
           keymap).

## [](#CREATE_BINARY_KEYMAP)CREATE BINARY KEYMAP

           If the -b (or --bkeymap ) option is given loadkeys prints to the
           standard output a file that may be used as a binary keymap as
           expected by Busybox loadkmap command (and does not modify the
           current keymap).

## [](#CREATE_TEXT_KEYMAP)CREATE TEXT KEYMAP

           If the -t (or --tkeymap ) option is given loadkeys prints to the
           standard output a file that may be used as a text keymap as
           expected by loadkeys command (and does not modify the current
           keymap).  An optional argument can be used to select the shape of
           the output format: -tshape (or --tkeymap=shape ).

           Available shapes:

                  2 default output.

                  4 one line for each keycode.

                  8 one line for each (modifier,keycode) pair.

                  16 one line for each keycode until 1st hole.

## [](#UNICODE_MODE)UNICODE MODE

           loadkeys automatically detects whether the console is in Unicode
           or ASCII (XLATE) mode.  When a keymap is loaded, literal keysyms
           (such as section) are resolved accordingly; numerical keysyms are
           converted to fit the current console mode, regardless of the way
           they are specified (decimal, octal, hexadecimal or Unicode).

           The -u (or --unicode) switch forces loadkeys to convert all
           keymaps to Unicode.  If the keyboard is in a non-Unicode mode,
           such as XLATE, loadkeys will change it to Unicode for the time of
           its execution.  A warning message will be printed in this case.

           It is recommended to run kbd_mode(1) before loadkeys instead of
           using the -u option.

## [](#OTHER_OPTIONS)OTHER OPTIONS

           -a --ascii
                  Force conversion to ASCII.

           -h --help
                  loadkeys prints its version number and a short usage
                  message to the programs standard error output and exits.

           -p --parse
                  loadkeys searches and parses keymap without action.

           --xkb-model=model
                  Use model when choosing XKB component names.

           --xkb-layout=layout
                  Use layout when choosing XKB component names.

           --xkb-variant=variant
                  Use variant when choosing XKB component names.

           --xkb-options=options
                  Use options when choosing XKB component names.

           --xkb-locale=locale
                  Use locale to find an appropriate XKB compose file.  If
                  this option is not given, loadkeys tries LC_ALL, LC_CTYPE,
                  LANG, and then C.

           -q --quiet
                  loadkeys suppresses all normal output.

           -V --version
                  loadkeys prints version number and exits.

## [](#WARNING)WARNING

           Note that anyone having read access to /dev/console can run
           loadkeys and thus change the keyboard layout, possibly making it
           unusable. Note that the keyboard translation table is common for
           all the virtual consoles, so any changes to the keyboard bindings
           affect all the virtual consoles simultaneously.

           Note that because the changes affect all the virtual consoles,
           they also outlive your session. This means that even at the login
           prompt the key bindings may not be what the user expects.

## [](#FILES)FILES

           /usr/local/share/keymaps
                  default directory for keymaps.

           /usr/src/linux/drivers/tty/vt/defkeymap.map
                  default kernel keymap.

## [](#SEE_ALSO)SEE ALSO

           dumpkeys(1), keymaps(5)

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

    kbd                             6 Feb 1994                    LOADKEYS(1)

------------------------------------------------------------------------

Pages that refer to this page: [dumpkeys(1)](../man1/dumpkeys.1.html),  [kbd_mode(1)](../man1/kbd_mode.1.html),  [localectl(1)](../man1/localectl.1.html),  [setleds(1)](../man1/setleds.1.html),  [setmetamode(1)](../man1/setmetamode.1.html),  [showkey(1)](../man1/showkey.1.html),  [unicode_start(1)](../man1/unicode_start.1.html),  [ioctl_console(2)](../man2/ioctl_console.2.html),  [reboot(2)](../man2/reboot.2.html),  [keymaps(5)](../man5/keymaps.5.html),  [vconsole.conf(5)](../man5/vconsole.conf.5.html),  [setkeycodes(8)](../man8/setkeycodes.8.html),  [systemd-localed.service(8)](../man8/systemd-localed.service.8.html),  [systemd-vconsole-setup.service(8)](../man8/systemd-vconsole-setup.service.8.html)

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
