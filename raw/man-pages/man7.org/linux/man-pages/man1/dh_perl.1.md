---
{"title": "dh_perl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_perl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_perl(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMS TO](#CONFORMS_TO) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_PERL(1)                      Debhelper                      DH_PERL(1)

## [](#NAME)NAME

           dh_perl - calculates Perl dependencies and cleans up after
           MakeMaker

## [](#SYNOPSIS)SYNOPSIS

           dh_perl [debhelper options] [-d] [library dirs ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_perl is a debhelper program that is responsible for generating
           the ${perl:Depends} substitutions and adding them to substvars
           files.

           The program will look at Perl scripts and modules in your package,
           and will use this information to generate a dependency on perl or
           perlapi. The dependency will be substituted into your package's
           control file wherever you place the token ${perl:Depends}.

           dh_perl also cleans up empty directories that MakeMaker can
           generate when installing Perl modules.

## [](#OPTIONS)OPTIONS

           -d  In some specific cases you may want to depend on perl-base
               rather than the full perl package. If so, you can pass the -d
               option to make dh_perl generate a dependency on the correct
               base package. This is only necessary for some packages that
               are included in the base system.

               Note that this flag may cause no dependency on perl-base to be
               generated at all. perl-base is Essential, so its dependency
               can be left out, unless a versioned dependency is needed.

           -V  By default, scripts and architecture independent modules don't
               depend on any specific version of perl. The -V option causes
               the current version of the perl (or perl-base with -d) package
               to be specified.

           library dirs
               If your package installs Perl modules in non-standard
               directories, you can make dh_perl check those directories by
               passing their names on the command line. It will only check
               the vendorlib and vendorarch directories by default.

## [](#CONFORMS_TO)CONFORMS TO

           Debian policy, version 3.8.3

           Perl policy, version 1.20

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Brendan O'Dea <bod@debian.org>

## [](#COLOPHON)COLOPHON

           This page is part of the debhelper (helper programs for
           debian/rules) project.  Information about the project can be found
           at [unknown -- if you know, please contact man-pages@man7.org] If
           you have a bug report for this manual page, send it to
           submit@bugs.debian.org.  This page was obtained from the project's
           upstream Git repository
           ⟨https://salsa.debian.org/debian/debhelper.git⟩ on 2026-08-03.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    13.29                           2026-01-15                     DH_PERL(1)

------------------------------------------------------------------------

Pages that refer to this page: [debhelper(7)](../man7/debhelper.7.html)

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
