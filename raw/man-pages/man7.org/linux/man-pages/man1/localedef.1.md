---
{"title": "localedef(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/localedef.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# localedef(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    localedef(1)             General Commands Manual             localedef(1)

## [](#NAME)NAME

           localedef - compile locale definition files

## [](#SYNOPSIS)SYNOPSIS

           localedef [options] outputpath

           localedef --add-to-archive [options] compiledpath

           localedef --delete-from-archive [options] localename ...

           localedef --list-archive [options]

           localedef --help

           localedef --usage

           localedef --version

## [](#DESCRIPTION)DESCRIPTION

           The localedef program reads the indicated charmap and input files,
           compiles them to a binary form quickly usable by the locale
           functions in the C library (setlocale(3), localeconv(3), etc.),
           and places the output in outputpath.

           The outputpath argument is interpreted as follows:

           •  If outputpath contains a slash character ('/'), it is
              interpreted as the name of the directory where the output
              definitions are to be stored.  In this case, there is a
              separate output file for each locale category (LC_TIME,
              LC_NUMERIC, and so on).

           •  If the --no-archive option is used, outputpath is the name of a
              subdirectory in /usr/lib/locale where per-category compiled
              files are placed.

           •  Otherwise, outputpath is the name of a locale and the compiled
              locale data is added to the archive file
              /usr/lib/locale/locale-archive.  A locale archive is a memory-
              mapped file which contains all the system-provided locales; it
              is used by all localized programs when the environment variable
              LOCPATH is not set.

           In any case, localedef aborts if the directory in which it tries
           to write locale files has not already been created.

           If no charmapfile is given, the value ANSI_X3.4-1968 (for ASCII)
           is used by default.  If no inputfile is given, or if it is given
           as a dash (-), localedef reads from standard input.

## [](#OPTIONS)OPTIONS

       Operation-selection options
           A few options direct localedef to do something other than compile
           locale definitions.  Only one of these options should be used at a
           time.

           --add-to-archive
                  Add the compiledpath directories to the locale archive
                  file.  The directories should have been created by previous
                  runs of localedef, using --no-archive.

           --delete-from-archive
                  Delete the named locales from the locale archive file.

           --list-archive
                  List the locales contained in the locale archive file.

       Other options
           Some of the following options are sensible only for certain
           operations; generally, it should be self-evident which ones.
           Notice that -f and -c are reversed from what you might expect;
           that is, -f is not the same as --force.

           -f charmapfile
           --charmap=charmapfile
                  Specify the file that defines the character set that is
                  used by the input file.  If charmapfile contains a slash
                  character ('/'), it is interpreted as the name of the
                  character map.  Otherwise, the file is sought in the
                  current directory and the default directory for character
                  maps.  If the environment variable I18NPATH is set,
                  $I18NPATH/charmaps/ and $I18NPATH/ are also searched after
                  the current directory.  The default directory for character
                  maps is printed by localedef --help.

           -i inputfile
           --inputfile=inputfile
                  Specify the locale definition file to compile.  The file is
                  sought in the current directory and the default directory
                  for locale definition files.  If the environment variable
                  I18NPATH is set, $I18NPATH/locales/ and $I18NPATH are also
                  searched after the current directory.  The default
                  directory for locale definition files is printed by
                  localedef --help.

           -u repertoirefile
           --repertoire-map=repertoirefile
                  Read mappings from symbolic names to Unicode code points
                  from repertoirefile.  If repertoirefile contains a slash
                  character ('/'), it is interpreted as the pathname of the
                  repertoire map.  Otherwise, the file is sought in the
                  current directory and the default directory for repertoire
                  maps.  If the environment variable I18NPATH is set,
                  $I18NPATH/repertoiremaps/ and $I18NPATH are also searched
                  after the current directory.  The default directory for
                  repertoire maps is printed by localedef --help.

           -A aliasfile
           --alias-file=aliasfile
                  Use aliasfile to look up aliases for locale names.  There
                  is no default aliases file.

           --force
           -c     Write the output files even if warnings were generated
                  about the input file.

           --verbose
           -v     Generate extra warnings about errors that are normally
                  ignored.

           --big-endian
                  Generate big-endian output.

           --little-endian
                  Generate little-endian output.

           --no-archive
                  Do not use the locale archive file, instead create
                  outputpath as a subdirectory in the same directory as the
                  locale archive file, and create separate output files for
                  locale categories in it.  This is helpful to prevent system
                  locale archive updates from overwriting custom locales
                  created with localedef.

           --no-hard-links
                  Do not create hard links between installed locales.

           --no-warnings=warnings
                  Comma-separated list of warnings to disable.  Supported
                  warnings are ascii and intcurrsym.

           --posix
                  Conform strictly to POSIX.  Implies --verbose.  This option
                  currently has no other effect.  POSIX conformance is
                  assumed if the environment variable POSIXLY_CORRECT is set.

           --prefix=pathname
                  Set the prefix to be prepended to the full archive
                  pathname.  By default, the prefix is empty.  Setting the
                  prefix to foo, the archive would be placed in
                  foo/usr/lib/locale/locale-archive.

           --quiet
                  Suppress all notifications and warnings, and report only
                  fatal errors.

           --replace
                  Replace a locale in the locale archive file.  Without this
                  option, if the locale is in the archive file already, an
                  error occurs.

           --warnings=warnings
                  Comma-separated list of warnings to enable.  Supported
                  warnings are ascii and intcurrsym.

           --help
           -?     Print a usage summary and exit.  Also prints the default
                  paths used by localedef.

           --usage
                  Print a short usage summary and exit.

           --version
           -V     Print the version number, license, and disclaimer of
                  warranty for localedef.

## [](#EXIT_STATUS)EXIT STATUS

           One of the following exit values can be returned by localedef:

           0      Command completed successfully.

           1      Warnings or errors occurred, output files were written.

           4      Errors encountered, no output created.

## [](#ENVIRONMENT)ENVIRONMENT

           POSIXLY_CORRECT
                  The --posix flag is assumed if this environment variable is
                  set.

           I18NPATH
                  A colon-separated list of search directories for files.

## [](#FILES)FILES

           /usr/share/i18n/charmaps
                  Usual default character map path.

           /usr/share/i18n/locales
                  Usual default path for locale definition files.

           /usr/share/i18n/repertoiremaps
                  Usual default repertoire map path.

           /usr/lib/locale/locale-archive
                  Usual default locale archive location.

           /usr/lib/locale
                  Usual default path for compiled individual locale data
                  files.

           outputpath/LC_ADDRESS
                  An output file that contains information about formatting
                  of addresses and geography-related items.

           outputpath/LC_COLLATE
                  An output file that contains information about the rules
                  for comparing strings.

           outputpath/LC_CTYPE
                  An output file that contains information about character
                  classes.

           outputpath/LC_IDENTIFICATION
                  An output file that contains metadata about the locale.

           outputpath/LC_MEASUREMENT
                  An output file that contains information about locale
                  measurements (metric versus US customary).

           outputpath/LC_MESSAGES/SYS_LC_MESSAGES
                  An output file that contains information about the language
                  messages should be printed in, and what an affirmative or
                  negative answer looks like.

           outputpath/LC_MONETARY
                  An output file that contains information about formatting
                  of monetary values.

           outputpath/LC_NAME
                  An output file that contains information about salutations
                  for persons.

           outputpath/LC_NUMERIC
                  An output file that contains information about formatting
                  of nonmonetary numeric values.

           outputpath/LC_PAPER
                  An output file that contains information about settings
                  related to standard paper size.

           outputpath/LC_TELEPHONE
                  An output file that contains information about formats to
                  be used with telephone services.

           outputpath/LC_TIME
                  An output file that contains information about formatting
                  of data and time values.

## [](#STANDARDS)STANDARDS

           POSIX.1-2008.

## [](#EXAMPLES)EXAMPLES

           Compile the locale files for Finnish in the UTF-8 character set
           and add it to the default locale archive with the name
           fi_FI.UTF-8:

               localedef -f UTF-8 -i fi_FI fi_FI.UTF-8

           The next example does the same thing, but generates files into the
           fi_FI.UTF-8 directory which can then be used by programs when the
           environment variable LOCPATH is set to the current directory (note
           that the last argument must contain a slash):

               localedef -f UTF-8 -i fi_FI ./fi_FI.UTF-8

## [](#SEE_ALSO)SEE ALSO

           locale(1), charmap(5), locale(5), repertoiremap(5), locale(7)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08                   localedef(1)

------------------------------------------------------------------------

Pages that refer to this page: [locale(1)](../man1/locale.1.html),  [localeconv(3)](../man3/localeconv.3.html),  [setlocale(3)](../man3/setlocale.3.html),  [sysconf(3)](../man3/sysconf.3.html),  [charmap(5)](../man5/charmap.5.html),  [locale(5)](../man5/locale.5.html),  [repertoiremap(5)](../man5/repertoiremap.5.html),  [locale(7)](../man7/locale.7.html)

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
