---
{"title": "debhelper-obsolete-compat(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/debhelper-obsolete-compat.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# debhelper-obsolete-compat(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [UPGRADE LIST FOR COMPAT LEVELS](#UPGRADE_LIST_FOR_COMPAT_LEVELS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    debhelper(7)                    Debhelper                    debhelper(7)

## [](#NAME)NAME

           debhelper-obsolete-compat - List of no longer supported compat
           levels

## [](#SYNOPSIS)SYNOPSIS

           This document contains the upgrade guidelines from all compat
           levels which are no longer supported.  Accordingly it is mostly
           for historical purposes and to assist people upgrading from a non-
           supported compat level to a supported level.

           For upgrades from supported compat levels, please see
           debhelper(7).

## [](#UPGRADE_LIST_FOR_COMPAT_LEVELS)UPGRADE LIST FOR COMPAT LEVELS

           The following is the list of now obsolete compat levels and their
           changes.

           v7  This is the lowest supported compatibility level.

               Changes from v6 are:

               -       dh_install, will fall back to looking for files in
                       debian/tmp if it doesn't find them in the current
                       directory (or wherever you tell it look using
                       --sourcedir). This allows dh_install to interoperate
                       with dh_auto_install, which installs to debian/tmp,
                       without needing any special parameters.

               -       dh_clean will read debian/clean and delete files
                       listed there.

               -       dh_clean will delete toplevel *-stamp files.

               -       dh_installchangelogs will guess at what file is the
                       upstream changelog if none is specified.

           v6  Changes from v5 are:

               -       Commands that generate maintainer script fragments
                       will order the fragments in reverse order for the
                       prerm and postrm scripts.

               -       dh_installwm will install a slave manpage link for
                       x-window-manager.1.gz, if it sees the man page in
                       usr/share/man/man1 in the package build directory.

               -       dh_builddeb did not previously delete everything
                       matching DH_ALWAYS_EXCLUDE, if it was set to a list of
                       things to exclude, such as CVS:.svn:.git. Now it does.

               -       dh_installman allows overwriting existing man pages in
                       the package build directory. In previous compatibility
                       levels it silently refuses to do this.

               This mode is deprecated.

           v5  Changes from v4 are:

               -       Comments are ignored in debhelper config files.

               -       dh_strip --dbg-package now specifies the name of a
                       package to put debugging symbols in, not the packages
                       to take the symbols from.

               -       dh_installdocs skips installing empty files.

               -       dh_install errors out if wildcards expand to nothing.

           v4  Changes from v3 are:

               -       dh_makeshlibs -V will not include the Debian part of
                       the version number in the generated dependency line in
                       the shlibs file.

               -       You are encouraged to put the new ${misc:Depends} into
                       debian/control to supplement the ${shlibs:Depends}
                       field.

               -       dh_fixperms will make all files in bin/ directories
                       and in etc/init.d executable.

               -       dh_link will correct existing links to conform with
                       policy.

               This mode is deprecated.

           v3  This mode works like v2, with the following additions:

               -       Debhelper config files support globbing via * and ?,
                       when appropriate. To turn this off and use those
                       characters raw, just prefix with a backslash.

               -       dh_makeshlibs makes the postinst and postrm scripts
                       call ldconfig.

               -       Every file in etc/ is automatically flagged as a
                       conffile by dh_installdeb.

               This mode is deprecated.

           v2  In this mode, debhelper will consistently use debian/package
               as the package tree directory for every package that is built.

               This mode is deprecated.

           v1  This is the original debhelper compatibility level, and so it
               is the default one. In this mode, debhelper will use
               debian/tmp as the package tree directory for the first binary
               package listed in the control file, while using debian/package
               for all other packages listed in the control file.

               This mode is deprecated.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

## [](#AUTHORS)AUTHORS

           Niels Thykier <niels@thykier.net>

           Joey Hess

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

    13.11.7                         2023-09-12                   debhelper(7)

------------------------------------------------------------------------

Pages that refer to this page: [debhelper-compat-upgrade-checklist(7)](../man7/debhelper-compat-upgrade-checklist.7.html)

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
