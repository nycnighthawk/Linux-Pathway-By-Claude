---
{"title": "whatis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/whatis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# whatis(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WHATIS(1)                   Manual pager utils                  WHATIS(1)

## [](#NAME)NAME

           whatis - display one-line manual page descriptions

## [](#SYNOPSIS)SYNOPSIS

           whatis [-dlv?V] [-r|-w] [-s list] [-m system[,...]] [-M path] [-L
           locale] [-C file] name ...

## [](#DESCRIPTION)DESCRIPTION

           Each manual page has a short description available within it.
           whatis searches the manual page names and displays the manual page
           descriptions of any name matched.

           name may contain wildcards (-w) or be a regular expression (-r).
           Using these options, it may be necessary to quote the name or
           escape (\) the special characters to stop the shell from
           interpreting them.

           index databases are used during the search, and are updated by the
           mandb program.  Depending on your installation, this may be run by
           a periodic cron job, or may need to be run manually after new
           manual pages have been installed.  To produce an old style text
           whatis database from the relative index database, issue the
           command:

           whatis -M manpath -w '*' | sort > manpath/whatis

           where manpath is a manual page hierarchy such as /usr/man.

## [](#OPTIONS)OPTIONS

           -d, --debug
                  Print debugging information.

           -v, --verbose
                  Print verbose warning messages.

           -r, --regex
                  Interpret each name as a regular expression.  If a name
                  matches any part of a page name, a match will be made.
                  This option causes whatis to be somewhat slower due to the
                  nature of database searches.

           -w, --wildcard
                  Interpret each name as a pattern containing shell style
                  wildcards.  For a match to be made, an expanded name must
                  match the entire page name.  This option causes whatis to
                  be somewhat slower due to the nature of database searches.

           -l, --long
                  Do not trim output to the terminal width.  Normally, output
                  will be truncated to the terminal width to avoid ugly
                  results from poorly-written NAME sections.

           -s list, --sections=list, --section=list
                  Search only the given manual sections.  list is a colon- or
                  comma-separated list of sections.  If an entry in list is a
                  simple section, for example "3", then the displayed list of
                  descriptions will include pages in sections "3", "3perl",
                  "3x", and so on; while if an entry in list has an
                  extension, for example "3perl", then the list will only
                  include pages in that exact part of the manual section.

           -m system[,...], --systems=system[,...]
                  If this system has access to other operating systems'
                  manual page names, they can be accessed using this option.
                  To search NewOS's manual page names, use the option -m
                  NewOS.

                  The system specified can be a combination of comma
                  delimited operating system names.  To include a search of
                  the native operating system's manual page names, include
                  the system name man in the argument string.  This option
                  will override the $SYSTEM environment variable.

           -M path, --manpath=path
                  Specify an alternate set of colon-delimited manual page
                  hierarchies to search.  By default, whatis uses the
                  $MANPATH environment variable, unless it is empty or unset,
                  in which case it will determine an appropriate manpath
                  based on your $PATH environment variable.  This option
                  overrides the contents of $MANPATH.

           -L locale, --locale=locale
                  whatis will normally determine your current locale by a
                  call to the C function setlocale(3) which interrogates
                  various environment variables, possibly including
                  $LC_MESSAGES and $LANG.  To temporarily override the
                  determined value, use this option to supply a locale string
                  directly to whatis.  Note that it will not take effect
                  until the search for pages actually begins.  Output such as
                  the help message will always be displayed in the initially
                  determined locale.

           -C file, --config-file=file
                  Use this user configuration file rather than the default of
                  ~/.manpath.

           -?, --help
                  Print a help message and exit.

           --usage
                  Print a short usage message and exit.

           -V, --version
                  Display version information.

## [](#EXIT_STATUS)EXIT STATUS

           0      Successful program execution.

           1      Usage, syntax or configuration file error.

           2      Operational error.

           16     Nothing was found that matched the criteria specified.

## [](#ENVIRONMENT)ENVIRONMENT

           SYSTEM If $SYSTEM is set, it will have the same effect as if it
                  had been specified as the argument to the -m option.

           MANPATH
                  If $MANPATH is set, its value is interpreted as the colon-
                  delimited manual page hierarchy search path to use.

                  See the SEARCH PATH section of manpath(5) for the default
                  behaviour and details of how this environment variable is
                  handled.

           MANWIDTH
                  If $MANWIDTH is set, its value is used as the terminal
                  width (see the --long option).  If it is not set, the
                  terminal width will be calculated using the value of
                  $COLUMNS, and ioctl(2) if available, or falling back to 80
                  characters if all else fails.

## [](#FILES)FILES

           /usr/share/man/index.(bt|db|dir|pag)
                  A traditional global index database cache.

           /var/cache/man/index.(bt|db|dir|pag)
                  An FHS compliant global index database cache.

           /usr/share/man/.../whatis
                  A traditional whatis text database.

## [](#SEE_ALSO)SEE ALSO

           apropos(1), man(1), mandb(8)

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

    2.13.1                          2025-05-02                      WHATIS(1)

------------------------------------------------------------------------

Pages that refer to this page: [apropos(1)](../man1/apropos.1.html),  [lexgrog(1)](../man1/lexgrog.1.html),  [man(1)](../man1/man.1.html),  [manpath(1)](../man1/manpath.1.html),  [uri(7)](../man7/uri.7.html)

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
