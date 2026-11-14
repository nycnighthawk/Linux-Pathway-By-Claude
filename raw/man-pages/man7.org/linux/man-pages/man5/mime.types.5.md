---
{"title": "mime.types(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/mime.types.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mime.types(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mime.types(5)                  OpenPrinting                 mime.types(5)

## [](#NAME)NAME

           mime.types - mime type description file for cups

## [](#DESCRIPTION)DESCRIPTION

           The mime.types file defines the recognized file types.

           Additional file types are specified in files with the extension
           .types in the CUPS configuration directory.

           Each line in the mime.types file is a comment, blank, or rule
           line.  Comment lines start with the # character.  Rule lines start
           with the MIME media type and are optionally followed by a series
           of file recognition rules:

               mime/type [ rule ... rule ]

           Rules can be extended over multiple lines using the backslash
           character (\):

               mime/type [ really-really-really-long-rule ... \
                 rule ]

           MIME media types specified by the mime/type field are case-
           insensitive and are sorted in ascending alphanumeric order for the
           purposes of matching.  See the "TYPE MATCHING AND PRIORITY"
           section for more information.

           The rules may be grouped using parenthesis, joined using "+" for a
           logical AND, joined using "," or whitespace for a logical OR, and
           negated using "!".

       RULES
           Rules take two forms - a filename extension by itself and
           functions with test values inside parenthesis.  The following
           functions are available:

           match("PATTERN")
                True if the filename matches the given shell wildcard
                PATTERN.

           ascii(OFFSET,LENGTH)
                True if the LENGTH bytes starting at OFFSET are valid
                printable ASCII (CR, NL, TAB, BS, 32-126).  LENGTH cannot
                exceed 8192 bytes.

           printable(OFFSET,LENGTH)
                True if the LENGTH bytes starting at OFFSET are printable
                8-bit chars (CR, NL, TAB, BS, 32-126, 128-254).  LENGTH
                cannot exceed 8192 bytes.

           priority(NUMBER)
                Specifies the relative priority of this MIME media type.  The
                default priority is 100.  Larger values have higher priority
                while smaller values have lower priority.

           string(OFFSET,"STRING")
                True if the bytes starting at OFFSET are identical to STRING.

           istring(OFFSET,"STRING")
                True if the bytes starting at OFFSET match STRING without
                respect to case.

           char(OFFSET,VALUE)
                True if the byte at OFFSET is identical to VALUE.

           short(OFFSET,VALUE)
                True if the 16-bit big-endian integer at OFFSET is identical
                to VALUE.

           int(OFFSET,VALUE)
                True if the 32-bit big-endian integer at OFFSET is identical
                to VALUE.

           locale("STRING")
                True if current locale matches STRING.

           contains(OFFSET,LENGTH,"STRING")
                True if the bytes starting at OFFSET for LENGTH bytes
                contains STRING.  LENGTH cannot exceed 8192 bytes.

       STRING CONSTANTS
           String constants can be specified inside quotes ("") for strings
           containing whitespace and angle brackets (<>) for hexadecimal
           strings.

       TYPE MATCHING AND PRIORITY
           When CUPS needs to determine the MIME media type of a given file,
           it checks every MIME media type defined in the .types files.  When
           two or more types match a given file, the type chosen will depend
           on the type name and priority, with higher-priority types being
           used over lower-priority ones.  If the types have the same
           priority, the type names are sorted alphanumerically in ascending
           order and the first type is chosen.

           For example, if two types "text/bar" and "text/foo" are defined as
           matching the extension "doc", normally the type "text/bar" will be
           chosen since its name is alphanumerically smaller than "text/foo".
           However, if "text/foo" also defines a higher priority than
           "text/bar", "text/foo" will be chosen instead.

## [](#FILES)FILES

           /etc/cups - Typical CUPS configuration directory.

## [](#EXAMPLES)EXAMPLES

           Define two MIME media types for raster data, with one being a
           subset with higher priority:

               application/vnd.cups-raster  string(0,"RaSt") string(0,"tSaR") \
                                             string(0,"RaS2") string(0,"2SaR") \
                                             string(0,"RaS3") string(0,"3SaR")

               image/pwg-raster              string(0,"RaS2") + \
                                             string(4,PwgRaster<00>) priority(150)

## [](#SEE_ALSO)SEE ALSO

           cups-files.conf(5), cupsd.conf(5), cupsd(8), cupsfilter(8),
           mime.convs(5), CUPS Online Help (http://localhost:631/help)

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2020-2024 by OpenPrinting.

## [](#COLOPHON)COLOPHON

           This page is part of the CUPS (a standards-based, open source
           printing system) project.  Information about the project can be
           found at ⟨https://github.com/openprinting/cups⟩.  If you have a
           bug report for this manual page, see
           ⟨https://github.com/OpenPrinting/cups/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/openprinting/cups⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    2024-04-18                         CUPS                     mime.types(5)

------------------------------------------------------------------------

Pages that refer to this page: [classes.conf(5)](../man5/classes.conf.5.html),  [cupsd.conf(5)](../man5/cupsd.conf.5.html),  [cups-files.conf(5)](../man5/cups-files.conf.5.html),  [gitweb.conf(5)](../man5/gitweb.conf.5.html),  [mime.convs(5)](../man5/mime.convs.5.html),  [printers.conf(5)](../man5/printers.conf.5.html),  [subscriptions.conf(5)](../man5/subscriptions.conf.5.html),  [cupsd(8)](../man8/cupsd.8.html)

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
