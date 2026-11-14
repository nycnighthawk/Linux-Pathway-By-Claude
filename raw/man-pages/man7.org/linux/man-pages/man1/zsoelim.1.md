---
{"title": "zsoelim(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/zsoelim.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# zsoelim(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ZSOELIM(1)                  Manual pager utils                 ZSOELIM(1)

## [](#NAME)NAME

           zsoelim - satisfy .so requests in roff input

## [](#SYNOPSIS)SYNOPSIS

           zsoelim [-CVh] [file ...]

## [](#DESCRIPTION)DESCRIPTION

           zsoelim parses file arguments, or if none are specified, its
           standard input for lines of the form:

           .so <filename>

           These requests are replaced by the contents of the filename
           specified.  If the request cannot be met, zsoelim looks for
           filename.ext where .ext can be one of .gz, .Z or .z.  Other
           extension types may be supported depending upon compile time
           options.  If the request can be met by a compressed file, this
           file is decompressed using an appropriate decompressor and its
           output is used to satisfy the request.

           Traditionally, soelim programs were used to allow roff
           preprocessors to be able to preprocess the files referred to by
           the requests.  This particular version was written to circumvent
           problems created by support for compressed manual pages.

## [](#OPTIONS)OPTIONS

           -C, --compatible
                  This flag is available for compatibility with other soelim
                  programs.  Its use is to enable .so requests followed by
                  something other than whitespace.  As this is already the
                  default behaviour, it is ignored.

           -h, --help
                  Print a help message and exit.

           -V, --version
                  Display version information.

## [](#SEE_ALSO)SEE ALSO

           groff(1), man(1), nroff(1), troff(1)

## [](#AUTHOR)AUTHOR

           Wilf. (G.Wilford@ee.surrey.ac.uk).
           Fabrizio Polacco (fpolacco@debian.org).
           Colin Watson (cjwatson@debian.org).

## [](#BUGS)BUGS

           https://gitlab.com/man-db/man-db/-/issues
           https://savannah.nongnu.org/bugs/?group=man-db

## [](#COLOPHON)COLOPHON

           This page is part of the man-db (manual pager suite) project.
           Information about the project can be found at 
           ⟨http://www.nongnu.org/man-db/⟩.  If you have a bug report for this
           manual page, send it to man-db-devel@nongnu.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://gitlab.com/cjwatson/man-db⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-13.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    2.13.1                          2025-05-02                     ZSOELIM(1)

------------------------------------------------------------------------

Pages that refer to this page: [man(1)](../man1/man.1.html)

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
