---
{"title": "mime.convs(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/mime.convs.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mime.convs(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mime.convs(5)                  OpenPrinting                 mime.convs(5)

## [](#NAME)NAME

           mime.convs - mime type conversion file for cups (deprecated)

## [](#DESCRIPTION)DESCRIPTION

           The mime.convs file defines the filters that are available for
           converting files from one format to another.  The standard filters
           support text, PDF, PostScript, and many types of image files.

           Additional filters are specified in files with the extension
           .convs in the CUPS configuration directory.

           Each line in the mime.convs file is a comment, blank, or filter
           line.  Comment lines start with the # character.  Filter lines
           specify the source and destination MIME types along with a
           relative cost associated with the filter and the filter to run:

               source/type destination/type cost filter

           The source/type field specifies the source MIME media type that is
           consumed by the filter.

           The destination/type field specifies the destination MIME media
           type that is produced by the filter.

           The cost field specifies the relative cost for running the filter.
           A value of 100 means that the filter uses a large amount of
           resources while a value of 0 means that the filter uses very few
           resources.

           The filter field specifies the filter program filename.  Filenames
           are relative to the CUPS filter directory.

## [](#FILES)FILES

           /etc/cups - Typical CUPS configuration directory.
           /usr/lib/cups/filter - Typical CUPS filter directory.
           /usr/libexec/cups/filter - CUPS filter directory on macOS.

## [](#EXAMPLES)EXAMPLES

           Define a filter that converts PostScript documents to CUPS Raster
           format:

               application/vnd.cups-postscript application/vnd.cups-raster 50 pstoraster

## [](#NOTES)NOTES

           CUPS filters are deprecated and will no longer be supported in a
           future feature release of CUPS.  Printers that do not support IPP
           can be supported using applications such as ippeveprinter(1).

## [](#SEE_ALSO)SEE ALSO

           cups-files.conf(5), cupsd.conf(5), cupsd(8), cupsfilter(8),
           mime.types(5), CUPS Online Help (http://localhost:631/help)

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

    2021-02-28                         CUPS                     mime.convs(5)

------------------------------------------------------------------------

Pages that refer to this page: [classes.conf(5)](../man5/classes.conf.5.html),  [cupsd.conf(5)](../man5/cupsd.conf.5.html),  [cups-files.conf(5)](../man5/cups-files.conf.5.html),  [mime.types(5)](../man5/mime.types.5.html),  [printers.conf(5)](../man5/printers.conf.5.html),  [subscriptions.conf(5)](../man5/subscriptions.conf.5.html),  [cupsd(8)](../man8/cupsd.8.html)

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
