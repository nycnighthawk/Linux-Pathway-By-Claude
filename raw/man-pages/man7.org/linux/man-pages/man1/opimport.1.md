---
{"title": "opimport(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/opimport.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# opimport(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [VERSION](#VERSION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OPIMPORT(1)              General Commands Manual              OPIMPORT(1)

## [](#NAME)NAME

           opimport - converts sample database files

## [](#SYNOPSIS)SYNOPSIS

           opimport [ options ] input_file

## [](#DESCRIPTION)DESCRIPTION

           opimport converts sample database files from a foreign binary
           format (abi) to the native format.

## [](#OPTIONS)OPTIONS

           --abi / -a
                  Input abi file description location.

           --force / -f
                  Force conversion even if the input and output abi are
                  identical.

           --output / -o filename
                  Specify the output filename. If the output file already
                  exists it is not overwritten but data are accumulated in.
                  Sample filename are informative for post profile tools and
                  must be kept identical, in other word the pathname from the
                  first path component containing a '{' must be kept as it in
                  the output filename.

           --help / -? / --usage
                  Show help message.

           --verbose / -V
                  Give verbose debugging output.

           --version / -v
                  Show version.

## [](#ENVIRONMENT)ENVIRONMENT

           No special environment variables are recognized by opimport

## [](#FILES)FILES

           <session_dir>/abi
                  The abi file description of the sample database files

## [](#VERSION)VERSION

           This man page is current for oprofile-1.5.0git.

## [](#SEE_ALSO)SEE ALSO

           /usr/local/share/doc/oprofile/, oprofile(1)

## [](#COLOPHON)COLOPHON

           This page is part of the oprofile (a system-wide profiler for
           Linux) project.  Information about the project can be found at 
           ⟨http://oprofile.sourceforge.net/news/⟩.  If you have a bug report
           for this manual page, see ⟨http://oprofile.sourceforge.net/bugs/⟩.
           This page was obtained from the project's upstream Git repository
           ⟨git://git.code.sf.net/p/oprofile/oprofile⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2024-12-10.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    4th Berkeley Distribution    Sun 24 May 2026                  OPIMPORT(1)

------------------------------------------------------------------------

Pages that refer to this page: [oparchive(1)](../man1/oparchive.1.html)

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
