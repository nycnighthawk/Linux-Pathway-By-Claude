---
{"title": "setfont(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/setfont.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setfont(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FONT FORMATS](#FONT_FORMATS) \| [FONT HEIGHT](#FONT_HEIGHT) \| [CONSOLE MAPS](#CONSOLE_MAPS) \| [UNICODE FONT MAPS](#UNICODE_FONT_MAPS) \| [OPTIONS](#OPTIONS) \| [NOTE](#NOTE) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SETFONT(8)               System Manager's Manual               SETFONT(8)

## [](#NAME)NAME

           setfont - load EGA/VGA console screen font

## [](#SYNOPSIS)SYNOPSIS

           setfont [-O font+umap.orig] [-o font.orig] [-om cmap.orig] [-ou
           umap.orig] [-N] [font.new ...] [-m cmap] [-u umap] [-C console]
           [-hH] [-f] [-v] [-V]

## [](#DESCRIPTION)DESCRIPTION

           The setfont command reads a font from the file font.new and loads
           it into the EGA/VGA character generator, and optionally outputs
           the previous font.  It can also load various mapping tables and
           output the previous versions.

           If no args are given (or only the option -N for some number N),
           then a default (8xN) font is loaded (see below).  One may give
           several small fonts, all containing a Unicode table, and setfont
           will combine them and load the union.  Typical use:

           setfont
                  Load a default font.

           setfont drdos8x16
                  Load a given font (here the 448-glyph drdos font).

           setfont cybercafe -u cybercafe
                  Load a given font that does not have a Unicode map and
                  provide one explicitly.

           setfont LatArCyrHeb-19 -m 8859-2
                  Load a given font (here a 512-glyph font combining several
                  character sets) and indicate that one's local character set
                  is ISO 8859-2.

           Note: if a font has more than 256 glyphs, only 8 out of 16 colors
           can be used simultaneously. It can make console perception worse
           (loss of intensity and even some colors).

## [](#FONT_FORMATS)FONT FORMATS

           The standard Linux font format is the PSF font.  It has a header
           describing font properties like character size, followed by the
           glyph bitmaps, optionally followed by a Unicode mapping table
           giving the Unicode value for each glyph.  Several other (obsolete)
           font formats are recognized.  If the input file has code page
           format (probably with suffix .cp), containing three fonts with
           sizes e.g. 8x8, 8x14 and 8x16, then one of the options -8 or -14
           or -16 must be used to select one.  Raw font files are binary
           files of size 256*N bytes, containing bit images for each of 256
           characters, one byte per scan line, and N bytes per character (0 <
           N <= 32).  Most fonts have a width of 8 bits, but with the
           framebuffer device (fb) other widths can be used.

## [](#FONT_HEIGHT)FONT HEIGHT

           The program setfont has no built-in knowledge of VGA video modes,
           but just asks the kernel to load the character ROM of the video
           card with certain bitmaps. However, since Linux 1.3.1 the kernel
           knows enough about EGA/VGA video modes to select a different line
           distance. The default character height will be the number N
           inferred from the font or specified by option. However, the user
           can specify a different character height H using the -h option.

## [](#CONSOLE_MAPS)CONSOLE MAPS

           Several mappings are involved in the path from user program output
           to console display. If the console is in utf8 mode (see
           unicode_start(1)) then the kernel expects that user program output
           is coded as UTF-8 (see utf-8(7)), and converts that to Unicode
           (ucs2).  Otherwise, a translation table is used from the 8-bit
           program output to 16-bit Unicode values. Such a translation table
           is called a Unicode console map.  There are four of them: three
           built into the kernel, the fourth settable using the -m option of
           setfont.  An escape sequence chooses between these four tables;
           after loading a cmap, setfont will output the escape sequence Esc
           ( K that makes it the active translation.

           Suitable arguments for the -m option are for example 8859-1,
           8859-2, ..., 8859-15, cp437, ..., cp1250.

           Given the Unicode value of the symbol to be displayed, the kernel
           finds the right glyph in the font using the Unicode mapping info
           of the font and displays it.

           Old fonts do not have Unicode mapping info, and in order to handle
           them there are direct-to-font maps (also loaded using -m) that
           give a correspondence between user bytes and font positions.  The
           most common correspondence is the one given in the file trivial
           (where user byte values are used directly as font positions).
           Other correspondences are sometimes preferable since the PC video
           hardware expects line drawing characters in certain font
           positions.

           Giving a -m none argument inhibits the loading and activation of a
           mapping table.  The previous console map can be saved to a file
           using the -om file option.  These options of setfont render
           mapscrn(8) obsolete. (However, it may be useful to read that man
           page.)

## [](#UNICODE_FONT_MAPS)UNICODE FONT MAPS

           The correspondence between the glyphs in the font and Unicode
           values is described by a Unicode mapping table.  Many fonts have a
           Unicode mapping table included in the font file, and an explicit
           table can be indicated using the -u option. The program setfont
           will load such a Unicode mapping table, unless a -u none argument
           is given. The previous Unicode mapping table will be saved as part
           of the saved font file when the -O option is used. It can be saved
           to a separate file using the -ou file option.  These options of
           setfont render loadunimap(8) obsolete.

           The Unicode mapping table should assign some glyph to the `missing
           character' value U+fffd, otherwise missing characters are not
           translated, giving a usually very confusing result.

           Usually no mapping table is needed, and a Unicode mapping table is
           already contained in the font (sometimes this is indicated by the
           .psfu extension), so that most users need not worry about the
           precise meaning and functioning of these mapping tables.

           One may add a Unicode mapping table to a psf font using
           psfaddtable(1).

## [](#OPTIONS)OPTIONS

           -N, --default8x=N
                  Load default font (default8xN).

           -hN, --font-height=N
                  Override font height. The short option must not have a
                  space between the prefix and the number.

           -d, --double
                  Doubles the size of the font, by replicating all of its
                  pixels vertically and horizontally.  This is suitable for
                  high pixel density (e.g. "4k") displays on which the
                  standard fonts are too small to be easily legible.  Due to
                  kernel limitations, this is suitable only for 16x16 or
                  smaller fonts.

           -o, --output-font=FILE
                  Save previous font in FILE.

           -om, --output-consolemap=FILE
                  Store console map in FILE.

           -ou, --output-unicodemap=FILE
                  Save previous Unicode map in FILE.

           -O, --output-fullfont=FILE
                  Save previous font and Unicode map in FILE.

           -m, --consolemap=FILE
                  Load console map or Unicode console map from FILE.

           -u, --unicodemap=FILE
                  Load Unicode table describing the font from FILE.

           -C, --console=DEVICE
                  Set the font for the indicated console. (May require root
                  permissions.)

           -f, --force
                  Force-load unicode map: Setfont`issues the system call to
                  load the unicode map even if the specified map is empty.
                  This may be useful in unusual cases.

           -R, --reset
                  Reset the screen font, size, and Unicode mapping to the
                  bootup defaults.

           -v, --verbose
                  Be verbose.

           -V, --version
                  Print version and exit.

           -h, --help
                  Print a message describing the options and exit.

## [](#NOTE)NOTE

           PC video hardware allows one to use the "intensity" bit either to
           indicate brightness, or to address 512 (instead of 256) glyphs in
           the font. So, if the font has more than 256 glyphs, the console
           will be reduced to 8 (instead of 16) colors.

## [](#FILES)FILES

           /usr/local/share/consolefonts
                  The default font directory.

           /usr/local/share/unimaps
                  The default directory for Unicode maps.

           /usr/local/share/consoletrans
                  The default directory for screen mappings.

           The default font is a file default (or default8xN if the -N option
           was given for some number N) perhaps with suitable extension (like
           .psf).

## [](#SEE_ALSO)SEE ALSO

           psfaddtable(1), unicode_start(1), loadunimap(8), utf-8(7),
           mapscrn(8)

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

    kbd                          24 October 2024                   SETFONT(8)

------------------------------------------------------------------------

Pages that refer to this page: [psfaddtable(1)](../man1/psfaddtable.1.html),  [psfgettable(1)](../man1/psfgettable.1.html),  [psfstriptable(1)](../man1/psfstriptable.1.html),  [psfxtable(1)](../man1/psfxtable.1.html),  [unicode_start(1)](../man1/unicode_start.1.html),  [unicode_stop(1)](../man1/unicode_stop.1.html),  [ioctl_console(2)](../man2/ioctl_console.2.html),  [console_codes(4)](../man4/console_codes.4.html),  [vconsole.conf(5)](../man5/vconsole.conf.5.html),  [charsets(7)](../man7/charsets.7.html),  [loadunimap(8)](../man8/loadunimap.8.html),  [mapscrn(8)](../man8/mapscrn.8.html),  [resizecons(8)](../man8/resizecons.8.html),  [showconsolefont(8)](../man8/showconsolefont.8.html),  [systemd-vconsole-setup.service(8)](../man8/systemd-vconsole-setup.service.8.html)

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
