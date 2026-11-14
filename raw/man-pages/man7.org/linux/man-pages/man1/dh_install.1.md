---
{"title": "dh_install(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_install.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_install(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [LIMITATIONS](#LIMITATIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALL(1)                   Debhelper                   DH_INSTALL(1)

## [](#NAME)NAME

           dh_install - install files into package build directories

## [](#SYNOPSIS)SYNOPSIS

           dh_install [-Xitem] [--autodest] [--sourcedir=dir]
           [debhelper options] [file|dir ... destdir]

## [](#DESCRIPTION)DESCRIPTION

           dh_install is a debhelper program that handles installing files
           into package build directories. There are many dh_install*
           commands that handle installing specific types of files such as
           documentation, examples, man pages, and so on, and they should be
           used when possible as they often have extra intelligence for those
           particular tasks. dh_install, then, is useful for installing
           everything else, for which no particular intelligence is needed.
           It is a replacement for the old dh_movefiles command.

           This program may be used in one of two ways. If you just have a
           file or two that the upstream Makefile does not install for you,
           you can run dh_install on them to move them into place. On the
           other hand, maybe you have a large package that builds multiple
           binary packages. You can use the upstream Makefile to install it
           all into debian/tmp, and then use dh_install to copy directories
           and files from there into the proper package build directories.

           From debhelper compatibility level 7 on, dh_install will fall back
           to looking in debian/tmp for files, if it does not find them in
           the current directory (or wherever you've told it to look using
           --sourcedir).

## [](#FILES)FILES

           debian/package.install
               List the files to install into each package and the directory
               they should be installed to. The format is a set of lines,
               where each line lists a file or files to install, and at the
               end of the line tells the directory it should be installed in.
               The name of the files (or directories) to install should be
               given relative to the current directory, while the
               installation directory is given relative to the package build
               directory. You may use wildcards in the names of the files to
               install.

               Note that if you list exactly one filename or wildcard-pattern
               on a line by itself, with no explicit destination, then
               dh_install will automatically guess the destination to use,
               the same as if the --autodest option were used.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

           debian/not-installed
               Used with the deprecated --list-missing and --fail-missing
               options.  Please refer to dh_missing(1) for the documentation
               of this file.

## [](#OPTIONS)OPTIONS

           --list-missing
               Deprecated: Please use dh_missing --list-missing instead.  If
               you use this option, dh_install will call dh_missing with that
               option after it has processed all the files.  Please see
               dh_missing(1) for the documentation of this option.

               This option is removed in compat 12.

           --fail-missing
               Deprecated: Please use dh_missing --fail-missing instead.  If
               you use this option, dh_install will call dh_missing with that
               option after it has processed all the files.  Please see
               dh_missing(1) for the documentation of this option.

               This option is removed in compat 12.

           --sourcedir=dir
               Look in the specified directory for files to be installed.

               Note that this is not the same as the --sourcedirectory option
               used by the dh_auto_* commands. You rarely need to use this
               option, since dh_install automatically looks for files in
               debian/tmp in debhelper compatibility level 7 and above.

           --autodest
               Guess as the destination directory to install things to. If
               this is specified, you should not list destination directories
               in debian/package.install files or on the command line.
               Instead, dh_install will guess as follows:

               Strip off debian/tmp (or the sourcedir if one is given) from
               the front of the filename, if it is present, and install into
               the dirname of the filename. So if the filename is
               debian/tmp/usr/bin, then that directory will be copied to
               debian/package/usr/. If the filename is debian/tmp/etc/passwd,
               it will be copied to debian/package/etc/.

           file|dir ... destdir
               Lists files (or directories) to install and where to install
               them to.  The files will be installed into the first package
               dh_install acts on.

## [](#EXAMPLES)EXAMPLES

           Here are some small examples of configuration files for
           dh_install.

               # Install my-prog into usr/bin (as "usr/bin/my-prog")
               my-prog usr/bin

               # Install a plugins directory into usr/share/my-prog
               # (as "usr/share/my-prog/plugins/")
               plugins usr/share/my-prog

               # Install a file with spaces in into usr/share/my-prog/data
               # (as "usr/share/my-prog/data/my datafile with spaces.txt")
               # ASSUMES COMPAT 13, where substitution patterns are available
               my${Space}datafile${Space}with${Space}spaces.txt usr/share/my-prog/data

               # Install a library into the multi-arch lib directory
               # ASSUMES COMPAT 13, where substitution patterns are available
               build/output/libfrop*.so.* usr/lib/${DEB_HOST_MULTIARCH}

## [](#LIMITATIONS)LIMITATIONS

           dh_install cannot rename files or directories, it can only install
           them with the names they already have into wherever you want in
           the package build tree.

           There is also no way to filter out results based on build profiles
           or architecture. For documentation content, consider using
           dh_installdocs or dh_installexamples as those helpers account for
           the nodoc build profile.

           However, renaming and filtering can be achieved by using dh-exec
           with compatibility level 9 or later.  An example
           debian/package.install file using dh-exec could look like:

            #!/usr/bin/dh-exec
            debian/default.conf => /etc/my-package/start.conf
            build/foo /usr/bin <!pkg.bar.nofoo>

           Please remember the following three things:

           •   The package must be using compatibility level 9 or later (see
               debhelper(7))

           •   The package will need a build-dependency on dh-exec.

           •   The install file must be marked as executable.

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

    13.23                           2025-01-02                  DH_INSTALL(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh(1)](../man1/dh.1.html),  [dh_assistant(1)](../man1/dh_assistant.1.html),  [dh_auto_install(1)](../man1/dh_auto_install.1.html),  [dh_installdocs(1)](../man1/dh_installdocs.1.html),  [dh_installman(1)](../man1/dh_installman.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
