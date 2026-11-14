---
{"title": "dh_installdocs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installdocs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installdocs(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLDOCS(1)               Debhelper               DH_INSTALLDOCS(1)

## [](#NAME)NAME

           dh_installdocs - install documentation into package build
           directories

## [](#SYNOPSIS)SYNOPSIS

           dh_installdocs [debhelper options] [-A] [-Xitem] [file ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_installdocs is a debhelper program that is responsible for
           installing documentation into usr/share/doc/package in package
           build directories.

           In compat 10 and earlier, dh_install(1) may be a better tool for
           handling the upstream documentation, when upstream's own build
           system installs all the desired documentation correctly.  In this
           case, dh_installdocs is still useful for installing packaging
           related documentation (e.g. the debian/copyright file).

           From debhelper compatibility level 11 on, dh_install will fall
           back to looking in debian/tmp for files, if it does not find them
           in the current directory (or wherever you've told it to look using
           --sourcedir).

           In compat 11 and later, dh_installdocs offers many of the features
           that dh_install(1) also has.  Furthermore, dh_installdocs also
           supports the nodoc build profile to exclude documentation
           (regardless of compat level).

## [](#FILES)FILES

           debian/package.docs
               List documentation files to be installed into package.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

           debian/copyright
               The copyright file is installed into all packages, unless a
               more specific copyright file is available.

           debian/package.copyright
           debian/package.README.Debian
           debian/package.TODO
               Each of these files is automatically installed if present for
               a package.

           debian/README.Debian
           debian/TODO
               These files are installed into the first binary package listed
               in debian/control.

               Note that README.debian files are also installed as
               README.Debian, and TODO files will be installed as TODO.Debian
               in non-native packages.

           debian/package.doc-base
               Installed as doc-base control files. Note that the doc-id will
               be determined from the Document: entry in the doc-base control
               file in question.

           debian/package.doc-base.*
               If your package needs to register more than one document, you
               need multiple doc-base files, and can name them like this.

               Please be aware that the files are deduplicated in memory
               based on their doc-id. To work correctly, it requires
               dh_installdocs to be called no more than once during the
               package build. Calling dh_installdocs -ppackage in combination
               with using debian/package.doc-base.* files can lead to
               uninstallable packages. See <https://bugs.debian.org/980903>
               for details.

## [](#OPTIONS)OPTIONS

           -A, --all
               Install all files specified by command line parameters in ALL
               packages acted on.

           -Xitem, --exclude=item
               Exclude files that contain item anywhere in their filename
               from being installed. Note that this includes doc-base files.

           --sourcedir=dir
               Look in the specified directory for files to be installed.
               This option requires compat 11 or later (it is silently
               ignored in compat 10 or earlier).

               Note that this is not the same as the --sourcedirectory option
               used by the dh_auto_* commands. You rarely need to use this
               option, since dh_installman automatically looks for files in
               debian/tmp in debhelper compatibility level 11 and above.

           --doc-main-package=main-package
               Set the main package for a documentation package.  This is
               used to install the documentation of the documentation package
               in /usr/share/doc/main-package as recommended by the Debian
               policy manual 3.9.7 in §12.3.

               In compat 11 (or later), this option is only useful if
               debhelper's auto-detection of the main package is wrong.  The
               option can also be used to silence a warning from debhelper
               when the auto-detection fails but the default happens to be
               correct.

               This option cannot be used when dh_installdocs is instructed
               to act on multiple packages.  If you need this option, you
               will generally need to combine it with -p to ensure exactly
               one package is acted on.

               The X-Doc-Main-Package field can be used instead since
               debhelper/13.28. It has similar semantics but does not require
               command line options.

               Please keep in mind that some documentation (the copyright
               file, README.Debian, etc.) will be unaffected by this option
               and the X-Doc-Main-Package field.

           --link-doc=package
               Make the documentation directory of all packages acted on be a
               symlink to the documentation directory of package. This has no
               effect when acting on package itself, or if the documentation
               directory to be created already exists when dh_installdocs is
               run. To comply with policy, package must be a binary package
               that comes from the same source package.

               debhelper will try to avoid installing files into linked
               documentation directories that would cause conflicts with the
               linked package. The -A option will have no effect on packages
               with linked documentation directories, and copyright,
               changelog, README.Debian, and TODO files will not be
               installed.

               (An older method to accomplish the same thing, which is still
               supported, is to make the documentation directory of a package
               be a dangling symlink, before calling dh_installdocs.)

               Please note that this option only applies to the documentation
               directory for the package itself.  When the package ships
               documentation for another package (e.g. see
               --doc-main-package), it will not use a symlink for the
               documentation of the other package.

               CAVEAT 1: If a previous version of the package was built
               without this option and is now built with it (or vice-versa),
               it requires a "dir to symlink" (or "symlink to dir")
               migration.  Since debhelper has no knowledge of previous
               versions, you have to enable this migration itself.

               This can be done by providing a "debian/package.maintscript"
               file and using dh_installdeb(1) to provide the relevant
               maintainer script snippets.

               CAVEAT 2: The use of --link-doc should only be done when the
               packages have same "architecture" type.  A link from an
               architecture independent package to an architecture dependent
               package (or vice versa) will not work.  Since compat 10,
               debhelper will actively reject unsupported combinations.

           file ...
               Install these files as documentation into the first package
               acted on. (Or in all packages if -A is specified).

## [](#EXAMPLES)EXAMPLES

           This is an example of a debian/package.docs file:

             README
             TODO
             debian/notes-for-maintainers.txt
             docs/manual.txt
             docs/manual.pdf
             docs/manual-html/

## [](#NOTES)NOTES

           Note that dh_installdocs will happily copy entire directory
           hierarchies if you ask it to (similar to cp -a). If it is asked to
           install a directory, it will install the complete contents of the
           directory.

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

    14.3                            2026-08-03              DH_INSTALLDOCS(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_assistant(1)](../man1/dh_assistant.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
