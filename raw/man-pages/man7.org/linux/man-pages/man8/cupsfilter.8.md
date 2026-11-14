---
{"title": "cupsfilter(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cupsfilter.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cupsfilter(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cupsfilter(8)                  OpenPrinting                 cupsfilter(8)

## [](#NAME)NAME

           cupsfilter - convert a file to another format using cups filters
           (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           cupsfilter [ --list-all ] [ --list-filters ] [ -D ] [ -U user ] [
           -c config-file ] [ -d printer ] [ -e ] [ -i mime/type ] [ -j job-
           id[,N] ] [ -m mime/type ] [ -n copies ] [ -o name=value ] [ -p
           filename.ppd ] [ -t title ] [ -u ] filename

## [](#DESCRIPTION)DESCRIPTION

           cupsfilter is a front-end to the CUPS filter subsystem which
           allows you to convert a file to a specific format, just as if you
           had printed the file through CUPS. By default, cupsfilter
           generates a PDF file. The converted file is sent to the standard
           output.

## [](#OPTIONS)OPTIONS

           --list-all
                Do not actually run the filters, just print all of the
                filters used with the source and destination MIME media types
                to stdout.

           --list-filters
                Do not actually run the filters, just print the filters used
                to stdout.

           -D   Delete the input file after conversion.

           -U user
                Specifies the username passed to the filters. The default is
                the name of the current user.

           -c config-file
                Uses the named cups-files.conf configuration file.

           -d printer
                Uses information from the named printer.

           -e   Use every filter from the PPD file.

           -i mime/type
                Specifies the source file type. The default file type is
                guessed using the filename and contents of the file.

           -j job-id[,N]
                Converts document N from the specified job. If N is omitted,
                document 1 is converted.

           -m mime/type
                Specifies the destination file type. The default file type is
                application/pdf. Use printer/foo to convert to the printer
                format defined by the filters in the PPD file.

           -n copies
                Specifies the number of copies to generate.

           -o name=value
                Specifies options to pass to the CUPS filters.

           -p filename.ppd
                Specifies the PPD file to use.

           -t title
                Specifies the document title.

           -u   Delete the PPD file after conversion.

## [](#EXIT_STATUS)EXIT STATUS

           cupsfilter returns a non-zero exit status on any error.

## [](#ENVIRONMENT)ENVIRONMENT

           All of the standard cups(1) environment variables affect the
           operation of cupsfilter.

## [](#FILES)FILES

           /etc/cups/cups-files.conf
           /etc/cups/*.convs
           /etc/cups/*.types
           /usr/share/cups/mime/*.convs
           /usr/share/cups/mime/*.types

## [](#NOTES)NOTES

           CUPS printer drivers, filters, and backends are deprecated and
           will no longer be supported in a future feature release of CUPS.
           Printers that do not support IPP can be supported using
           applications such as ippeveprinter(1).

           Unlike when printing, filters run using the cupsfilter command use
           the current user and security session. This may result in
           different output or unexpected behavior.

## [](#EXAMPLE)EXAMPLE

           The following command will generate a PDF preview of job 42 for a
           printer named "myprinter" and save it to a file named
           "preview.pdf":

               cupsfilter -m application/pdf -d myprinter -j 42 >preview.pdf

## [](#SEE_ALSO)SEE ALSO

           cups(1), cupsd.conf(5), filter(7), mime.convs(7), mime.types(7),
           CUPS Online Help (http://localhost:631/help)

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

    2024-04-25                         CUPS                     cupsfilter(8)

------------------------------------------------------------------------

Pages that refer to this page: [mime.convs(5)](../man5/mime.convs.5.html),  [mime.types(5)](../man5/mime.types.5.html),  [filter(7)](../man7/filter.7.html)

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
