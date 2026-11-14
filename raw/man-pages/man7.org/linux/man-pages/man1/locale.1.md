---
{"title": "locale(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/locale.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# locale(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    locale(1)                General Commands Manual                locale(1)

## [](#NAME)NAME

           locale - get locale-specific information

## [](#SYNOPSIS)SYNOPSIS

           locale [option]

           locale [option] -a

           locale [option] -m

           locale [option] name ...

## [](#DESCRIPTION)DESCRIPTION

           The locale command displays information about the current locale,
           or all locales, on standard output.

           When invoked without arguments, locale displays the current locale
           settings for each locale category (see locale(5)), based on the
           settings of the environment variables that control the locale (see
           locale(7)).  Values for variables set in the environment are
           printed without double quotes, implied values are printed with
           double quotes.

           If either the -a or the -m option (or one of their long-format
           equivalents) is specified, the behavior is as follows:

           --all-locales
           -a     Display a list of all available locales.  The -v option
                  causes the LC_IDENTIFICATION metadata about each locale to
                  be included in the output.

           --charmaps
           -m     Display the available charmaps (character set description
                  files).  To display the current character set for the
                  locale, use locale -c charmap.

           The locale command can also be provided with one or more
           arguments, which are the names of locale keywords (for example,
           date_fmt, ctype-class-names, yesexpr, or decimal_point) or locale
           categories (for example, LC_CTYPE or LC_TIME).  For each argument,
           the following is displayed:

           •  For a locale keyword, the value of that keyword to be
              displayed.

           •  For a locale category, the values of all keywords in that
              category are displayed.

           When arguments are supplied, the following options are meaningful:

           --category-name
           -c     For a category name argument, write the name of the locale
                  category on a separate line preceding the list of keyword
                  values for that category.

                  For a keyword name argument, write the name of the locale
                  category for this keyword on a separate line preceding the
                  keyword value.

                  This option improves readability when multiple name
                  arguments are specified.  It can be combined with the -k
                  option.

           --keyword-name
           -k     For each keyword whose value is being displayed, include
                  also the name of that keyword, so that the output has the
                  format:

                      keyword="value"

           The locale command also knows about the following options:

           --verbose
           -v     Display additional information for some command-line option
                  and argument combinations.

           --help
           -?     Display a summary of command-line options and arguments and
                  exit.

           --usage
                  Display a short usage message and exit.

           --version
           -V     Display the program version and exit.

## [](#FILES)FILES

           /usr/lib/locale/locale-archive
                  Usual default locale archive location.

           /usr/share/i18n/locales
                  Usual default path for locale definition files.

## [](#STANDARDS)STANDARDS

           POSIX.1-2008.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

## [](#EXAMPLES)EXAMPLES

           $ locale;
           LANG=en_US.UTF-8
           LC_CTYPE="en_US.UTF-8"
           LC_NUMERIC="en_US.UTF-8"
           LC_TIME="en_US.UTF-8"
           LC_COLLATE="en_US.UTF-8"
           LC_MONETARY="en_US.UTF-8"
           LC_MESSAGES="en_US.UTF-8"
           LC_PAPER="en_US.UTF-8"
           LC_NAME="en_US.UTF-8"
           LC_ADDRESS="en_US.UTF-8"
           LC_TELEPHONE="en_US.UTF-8"
           LC_MEASUREMENT="en_US.UTF-8"
           LC_IDENTIFICATION="en_US.UTF-8"
           LC_ALL=

           $ locale date_fmt;
           %a %b %e %H:%M:%S %Z %Y

           $ locale -k date_fmt;
           date_fmt="%a %b %e %H:%M:%S %Z %Y"

           $ locale -ck date_fmt;
           LC_TIME
           date_fmt="%a %b %e %H:%M:%S %Z %Y"

           $ locale LC_TELEPHONE;
           +%c (%a) %l
           (%a) %l
           11
           1
           UTF-8

           $ locale -k LC_TELEPHONE;
           tel_int_fmt="+%c (%a) %l"
           tel_dom_fmt="(%a) %l"
           int_select="11"
           int_prefix="1"
           telephone-codeset="UTF-8"

           The following example compiles a custom locale from the ./wrk
           directory with the localedef(1) utility under the $HOME/.locale
           directory, then tests the result with the date(1) command, and
           then sets the environment variables LOCPATH and LANG in the shell
           profile file so that the custom locale will be used in the
           subsequent user sessions:

           $ mkdir -p $HOME/.locale;
           $ I18NPATH=./wrk/ localedef -f UTF-8 -i fi_SE $HOME/.locale/fi_SE.UTF-8;
           $ LOCPATH=$HOME/.locale LC_ALL=fi_SE.UTF-8 date;
           $ echo "export LOCPATH=\$HOME/.locale" >> $HOME/.bashrc;
           $ echo "export LANG=fi_SE.UTF-8" >> $HOME/.bashrc;

## [](#SEE_ALSO)SEE ALSO

           localedef(1), charmap(5), locale(5), locale(7)

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

    Linux man-pages 6.19            2026-02-08                      locale(1)

------------------------------------------------------------------------

Pages that refer to this page: [iconv(1)](../man1/iconv.1.html),  [localedef(1)](../man1/localedef.1.html),  [localeconv(3)](../man3/localeconv.3.html),  [newlocale(3)](../man3/newlocale.3.html),  [nl_langinfo(3)](../man3/nl_langinfo.3.html),  [setlocale(3)](../man3/setlocale.3.html),  [sysconf(3)](../man3/sysconf.3.html),  [uselocale(3)](../man3/uselocale.3.html),  [charmap(5)](../man5/charmap.5.html),  [locale(5)](../man5/locale.5.html),  [repertoiremap(5)](../man5/repertoiremap.5.html),  [locale(7)](../man7/locale.7.html),  [unicode(7)](../man7/unicode.7.html),  [utf-8(7)](../man7/utf-8.7.html)

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
