---
{"title": "catman(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/catman.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# catman(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CATMAN(8)                   Manual pager utils                  CATMAN(8)

## [](#NAME)NAME

           catman - create or update the pre-formatted manual pages

## [](#SYNOPSIS)SYNOPSIS

           catman [-d?V] [-M path] [-C file] [section] ...

## [](#DESCRIPTION)DESCRIPTION

           catman is used to create an up to date set of pre-formatted manual
           pages known as cat pages.  Cat pages are generally much faster to
           display than the original manual pages, but require extra storage
           space.  The decision to support cat pages is that of the local
           administrator, who must provide suitable directories to contain
           them.

           The options available to catman are the manual page hierarchies
           and sections to pre-format.  The default hierarchies are those
           specified as system hierarchies in the man-db configuration file,
           and the default sections are either the colon-delimited contents
           of the environment variable $MANSECT or the standard set compiled
           into man if $MANSECT is undefined.  Supplying catman with a set of
           whitespace-delimited section names will override both of the
           above.

           catman makes use of the index database cache associated with each
           hierarchy to determine which files need to be formatted.

## [](#OPTIONS)OPTIONS

           -d, --debug
                  Print debugging information.

           -M path, --manpath=path
                  Specify an alternate colon-delimited manual page hierarchy
                  search path.  By default, this is all paths indicated as
                  system hierarchies in the man-db configuration file.

           -C file, --config-file=file
                  Use this user configuration file rather than the default of
                  ~/.manpath.

           -?, --help
                  Print a help message and exit.

           --usage
                  Print a short usage message and exit.

           -V, --version
                  Display version information.

## [](#ENVIRONMENT)ENVIRONMENT

           MANSECT
                  If $MANSECT is set, its value is a colon-delimited list of
                  sections and it is used to determine which manual sections
                  to search and in what order.  The default is "1 n l 8 3 0 2
                  3type 5 4 9 6 7", unless overridden by the SECTION
                  directive in /usr/local/etc/man_db.conf.

           MANPATH
                  If $MANPATH is set, its value is interpreted as the colon-
                  delimited manual page hierarchy search path to use.

                  See the SEARCH PATH section of manpath(5) for the default
                  behaviour and details of how this environment variable is
                  handled.

## [](#FILES)FILES

           /usr/local/etc/man_db.conf
                  man-db configuration file.

           /usr/man/index.(bt|db|dir|pag)
                  A traditional global index database cache.

           /var/catman/index.(bt|db|dir|pag)
                  An alternate or FSSTND compliant global index database
                  cache.

## [](#SEE_ALSO)SEE ALSO

           man(1), manpath(5), mandb(8)

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

    2.13.1                          2025-05-02                      CATMAN(8)

------------------------------------------------------------------------

Pages that refer to this page: [man(1)](../man1/man.1.html),  [mandb(8)](../man8/mandb.8.html)

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
