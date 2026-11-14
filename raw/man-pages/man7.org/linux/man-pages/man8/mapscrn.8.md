---
{"title": "mapscrn(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mapscrn.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mapscrn(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [USE](#USE) \| [INPUT FORMAT](#INPUT_FORMAT) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MAPSCRN(8)               System Manager's Manual               MAPSCRN(8)

## [](#NAME)NAME

           mapscrn - load screen output mapping table

## [](#SYNOPSIS)SYNOPSIS

           mapscrn [options] mapfile

## [](#DESCRIPTION)DESCRIPTION

           The mapscrn command is obsolete - its function is now built-in
           into setfont.  However, for backwards compatibility it is still
           available as a separate command.

           The mapscrn command loads a user defined output character mapping
           table into the console driver. The console driver may be later put
           into use user-defined mapping table mode by outputting a special
           escape sequence to the console device.  This sequence is <esc>(K
           for the G0 character set and <esc>)K for the G1 character set.
           When the -o option is given, the old map is saved in map.orig.

## [](#USE)USE

           There are two kinds of mapping tables: direct-to-font tables, that
           give a font position for each user byte value, and user-to-unicode
           tables that give a unicode value for each user byte. The
           corresponding glyph is now found using the unicode index of the
           font.  The command
                  mapscrn trivial
           sets up a one-to-one direct-to-font table where user bytes
           directly address the font. This is useful for fonts that are in
           the same order as the character set one uses.  A command like
                  mapscrn 8859-2
           sets up a user-to-unicode table that assumes that the user uses
           ISO 8859-2.

## [](#INPUT_FORMAT)INPUT FORMAT

           The mapscrn command can read the map in either of two formats:
           1. 256 or 512 bytes binary data
           2. two-column text file
           Format (1) is a direct image of the translation table. The
           256-bytes tables are direct-to-font, the 512-bytes tables are
           user-to-unicode tables.  Format (2) is used to fill the table as
           follows: cell with offset mentioned in the first column is filled
           with the value mentioned in the second column.  When values larger
           than 255 occur, or values are written using the U+xxxx notation,
           the table is assumed to be a user-to-unicode table, otherwise it
           is a direct-to-font table.

           Values in the file may be specified in one of several formats:
           1. Decimal: String of decimal digits not starting with '0'
           2. Octal: String of octal digits beginning with '0'.
           3. Hexadecimal: String of hexadecimal digits preceded by "0x".
           4. Unicode: String of four hexadecimal digits preceded by "U+".
           5. Character: Single character enclosed in single quotes. (And the
           binary value is used.)  Note that blank, comma, tab character and
           '#' cannot be specified with this format.
           6. UTF-8 Character: Single (possibly multi-byte) UTF-8 character,
           enclosed in single quotes.

           Note that control characters (with codes < 32) cannot be re-mapped
           with mapscrn because they have special meaning for the driver.

## [](#OPTIONS)OPTIONS

           -o, --output=FILE
                  save the old map to the FILE.

           -C, --console=DEV
                  the console device to be used.

           -v, --verbose
                  be more verbose.

           -V, --version
                  print version number.

           -h, --help
                  print this usage message.

## [](#FILES)FILES

           /usr/local/share/consoletrans
                  The default directory for screen mappings.

## [](#SEE_ALSO)SEE ALSO

           setfont(8)

## [](#AUTHOR)AUTHOR

           Copyright (C) 1993 Eugene G. Crosser
           <crosser@pccross.msk.su>
           This software and documentation may be distributed freely.

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

    kbd                          24 October 2024                   MAPSCRN(8)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_console(2)](../man2/ioctl_console.2.html),  [console_codes(4)](../man4/console_codes.4.html),  [loadunimap(8)](../man8/loadunimap.8.html),  [setfont(8)](../man8/setfont.8.html)

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
