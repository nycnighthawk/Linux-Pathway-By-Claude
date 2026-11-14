---
{"title": "dh_shlibdeps(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_shlibdeps.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_shlibdeps(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_SHLIBDEPS(1)                 Debhelper                 DH_SHLIBDEPS(1)

## [](#NAME)NAME

           dh_shlibdeps - calculate shared library dependencies

## [](#SYNOPSIS)SYNOPSIS

           dh_shlibdeps [debhelper options] [-Lpackage] [-ldirectory]
           [-Xitem] [-- params]

## [](#DESCRIPTION)DESCRIPTION

           dh_shlibdeps is a debhelper program that is responsible for
           calculating shared library dependencies for packages.

           This program is merely a wrapper around dpkg-shlibdeps(1) that
           calls it once for each package listed in the control file, passing
           it a list of ELF executables and shared libraries it has found.

## [](#OPTIONS)OPTIONS

           -Xitem, --exclude=item
               Exclude files that contain item anywhere in their filename
               from being passed to dpkg-shlibdeps. This will make their
               dependencies be ignored.  This may be useful in some
               situations, but use it with caution. This option may be used
               more than once to exclude more than one thing.

           -- params
               Pass params to dpkg-shlibdeps(1).

           -uparams, --dpkg-shlibdeps-params=params
               This is another way to pass params to dpkg-shlibdeps(1).  It
               is deprecated; use -- instead.

           -ldirectory[:directory ...]
               With recent versions of dpkg-shlibdeps, this option is
               generally not needed.

               It tells dpkg-shlibdeps (via its -l parameter), to look for
               private package libraries in the specified directory (or
               directories -- separate with colons). With recent versions of
               dpkg-shlibdeps, this is mostly only useful for packages that
               build multiple flavors of the same library, or other
               situations where the library is installed into a directory not
               on the regular library search path.

           -Lpackage, --libpackage=package
               With recent versions of dpkg-shlibdeps, this option is
               generally not needed, unless your package builds multiple
               flavors of the same library or is relying on
               debian/shlibs.local for an internal library.

               It tells dpkg-shlibdeps (via its -S parameter) to look first
               in the package build directory for the specified package, when
               searching for libraries, symbol files, and shlibs files.

               If needed, this can be passed multiple times with different
               package names.

## [](#EXAMPLES)EXAMPLES

           Suppose that your source package produces libfoo1, libfoo-dev, and
           libfoo-bin binary packages. libfoo-bin links against libfoo1, and
           should depend on it. In your rules file, first run dh_makeshlibs,
           then dh_shlibdeps:

                   dh_makeshlibs
                   dh_shlibdeps

           This will have the effect of generating automatically a shlibs
           file for libfoo1, and using that file and the libfoo1 library in
           the debian/libfoo1/usr/lib directory to calculate shared library
           dependency information.

           If a libbar1 package is also produced, that is an alternate build
           of libfoo, and is installed into /usr/lib/bar/, you can make
           libfoo-bin depend on libbar1 as follows:

                   dh_shlibdeps -Llibbar1 -l/usr/lib/bar

## [](#SEE_ALSO)SEE ALSO

           debhelper(7), dpkg-shlibdeps(1)

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

    14.3                            2026-08-03                DH_SHLIBDEPS(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh(1)](../man1/dh.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
