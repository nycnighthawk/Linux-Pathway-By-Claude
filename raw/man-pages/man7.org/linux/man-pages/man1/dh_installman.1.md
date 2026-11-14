---
{"title": "dh_installman(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installman.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installman(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLMAN(1)                Debhelper                DH_INSTALLMAN(1)

## [](#NAME)NAME

           dh_installman - install man pages into package build directories

## [](#SYNOPSIS)SYNOPSIS

           dh_installman [debhelper options] [manpage ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_installman is a debhelper program that handles installing man
           pages into the correct locations in package build directories.

           In compat 10 and earlier, this program was primarily for when
           upstream's build system does not properly install them as a part
           of its install step (or it does not have an install step).  In
           compat 11 and later, it also supports the default searchdir plus
           --sourcedir like dh_install(1) and has the advantage that it
           respects the nodoc build profile (unlike dh_install(1)).

           Even if you prefer to use dh_install(1) for installing the
           manpages, dh_installman can still be useful for converting the
           manpage encoding to UTF-8 and for converting .so links (as
           described below).  However, that part happens automatically
           without any explicit configuration.

           You tell dh_installman what man pages go in your packages, and it
           figures out where to install them based on the section field in
           their .TH or .Dt line. If you have a properly formatted .TH or .Dt
           line, your man page will be installed into the right directory,
           with the right name (this includes proper handling of pages with a
           subsection, like 3perl, which are placed in man3, and given an
           extension of .3perl). If your .TH or .Dt line is incorrect or
           missing, the program may guess wrong based on the file extension.

           It also supports translated man pages, by looking for extensions
           like .ll.8 and .ll_LL.8, or by use of the --language switch.

           If dh_installman seems to install a man page into the wrong
           section or with the wrong extension, this is because the man page
           has the wrong section listed in its .TH or .Dt line. Edit the man
           page and correct the section, and dh_installman will follow suit.
           See man(7) for details about the .TH section, and mdoc(7) for the
           .Dt section. If dh_installman seems to install a man page into a
           directory like /usr/share/man/pl/man1/, that is because your
           program has a name like foo.pl, and dh_installman assumes that
           means it is translated into Polish. Use --language=C to avoid
           this.

           After the man page installation step, dh_installman will check to
           see if any of the man pages in the temporary directories of any of
           the packages it is acting on contain .so links. If so, it changes
           them to symlinks.

           Also, dh_installman will use man to guess the character encoding
           of each manual page and convert it to UTF-8. If the guesswork
           fails for some reason, you can override it using an encoding
           declaration. See manconv(1) for details.

           From debhelper compatibility level 11 on, dh_install will fall
           back to looking in debian/tmp for files, if it does not find them
           in the current directory (or wherever you've told it to look using
           --sourcedir).

## [](#FILES)FILES

           debian/package.manpages
               Lists man pages to be installed.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

## [](#OPTIONS)OPTIONS

           -A, --all
               Install all files specified by command line parameters in ALL
               packages acted on.

           --language=ll
               Use this to specify that the man pages being acted on are
               written in the specified language.

           --sourcedir=dir
               Look in the specified directory for files to be installed.
               This option requires compat 11 or later (it is silently
               ignored in compat 10 or earlier).

               Note that this is not the same as the --sourcedirectory option
               used by the dh_auto_* commands. You rarely need to use this
               option, since dh_installman automatically looks for files in
               debian/tmp in debhelper compatibility level 11 and above.

           manpage ...
               Install these man pages into the first package acted on. (Or
               in all packages if -A is specified).

## [](#EXAMPLES)EXAMPLES

           An example debian/package.manpages file could look like this:

             doc/man/foo.1
             # Translations
             doc/man/foo.da.1
             doc/man/foo.de.1
             doc/man/foo.fr.1
             # NB: The following line is considered a polish translation
             # of "foo.1" (and not a manpage written in perl called "foo.pl")
             doc/man/foo.pl.1
             # ...

## [](#NOTES)NOTES

           An older version of this program, dh_installmanpages(1), is still
           used by some packages, and so is still included in debhelper.  It
           is, however, deprecated, due to its counterintuitive and
           inconsistent interface. Use this program instead.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Joey Hess <joeyh@debian.org>

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

    13.23                           2025-01-02               DH_INSTALLMAN(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_installmanpages(1)](../man1/dh_installmanpages.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
