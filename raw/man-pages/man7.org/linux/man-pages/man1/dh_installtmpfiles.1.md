---
{"title": "dh_installtmpfiles(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installtmpfiles.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installtmpfiles(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLTMPFILES(1)           Debhelper           DH_INSTALLTMPFILES(1)

## [](#NAME)NAME

           dh_installtmpfiles - install tmpfiles.d configuration files

## [](#SYNOPSIS)SYNOPSIS

           dh_installtmpfiles [debhelper options][--name=name]

## [](#DESCRIPTION)DESCRIPTION

           dh_installtmpfiles is a debhelper program that is responsible for
           installing package maintainer supplied tmpfiles.d configuration
           files (e.g. for systemd-tmpfiles).

           It also finds the tmpfiles.d configuration files installed by a
           package and generates postinst code blocks for activating the
           tmpfiles.d configuration when the package is installed. These
           snippets are added to the maintainer scripts by dh_installdeb(1).

           In compat 14+, tmpfiles.d files are copied into the postrm script,
           and they are used with systemd-tmpfiles --remove after the package
           is removed and --purge when the package is purged. This allows one
           to use the tmpfiles.d mechanism to clean up files that are no
           longer needed after a package has been removed/purged.

           The dh_installtmpfiles command will also add dependencies for any
           installed tmpfiles configuration files via ${misc:Depends}.

## [](#OPTIONS)OPTIONS

           --name=name
               This option controls both a prefix used for looking up
               maintainer provided tmpfiles.d configuration files (those
               mentioned in the "FILES" section) and also the base name used
               for the installed version of the file.

## [](#FILES)FILES

           debian/package.tmpfiles
               If this exists, it is installed into usr/lib/tmpfiles.d/ in
               the package build directory.

           debian/package.tmpfile
               Deprecated name for debian/package.tmpfiles.

## [](#NOTES)NOTES

           This command is not idempotent. dh_prep(1) should be called
           between invocations of this command (with the same arguments).
           Otherwise, it may cause multiple instances of the same text to be
           added to maintainer scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

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

    14.3                            2026-08-03          DH_INSTALLTMPFILES(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_installsystemd(1)](../man1/dh_installsystemd.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
