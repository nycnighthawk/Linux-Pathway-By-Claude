---
{"title": "dh_installsystemduser(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installsystemduser.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installsystemduser(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLSYSTEMDUSER(1)        Debhelper        DH_INSTALLSYSTEMDUSER(1)

## [](#NAME)NAME

           dh_installsystemduser - install systemd unit files

## [](#SYNOPSIS)SYNOPSIS

           dh_installsystemduser [debhelper options] [--no-enable]
           [--name=name] [unit file ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_installsystemduser finds the systemd user instance service
           files installed by a package and generates preinst, postinst, and
           prerm code blocks for enabling, disabling, starting, stopping, and
           restarting the corresponding systemd user instance services, when
           the package is installed, updated, or removed. These snippets are
           added to the maintainer scripts by dh_installdeb(1).

           deb-systemd-helper(1) is used to enable and disable the systemd
           units, thus it is not necessary that the machine actually runs
           systemd during package installation time, enabling happens on all
           machines.

           dh_installsystemduser operates on all user instance unit files
           installed by a package. For only generating blocks for specific
           unit files, pass them as arguments. Specific unit files can be
           excluded from processing using the -X common debhelper(1) option.

## [](#FILES)FILES

           debian/package.user.path, debian/package@.user.path,
           debian/package.user.service, debian/package@.user.service,
           debian/package.user.socket, debian/package@.user.socket,
           debian/package.user.target, debian/package@.user.target,
           debian/package.user.timer, debian/package@.user.timer
               If any of those files exists, they are installed into
               usr/lib/systemd/user/ in the package build directory removing
               the .user file name part.

## [](#OPTIONS)OPTIONS

           --name=name
               Install the service file as name.service instead of the
               default filename package.service. When this parameter is used,
               dh_installsystemd looks for and installs files named
               debian/package.name.user.service instead of the usual
               debian/package.user.service.  Moreover, maintainer scripts are
               only generated for units that match the given name.

           --no-enable
               Disable the service(s) on purge, but do not enable them on
               install.

## [](#NOTES)NOTES

           This command is not idempotent. dh_prep(1) should be called
           between invocations of this command (with the same arguments).
           Otherwise, it may cause multiple instances of the same text to be
           added to maintainer scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7), dh_installsystemd(1), deb-systemd-helper(1)

## [](#AUTHORS)AUTHORS

           pkg-systemd-maintainers@lists.alioth.debian.org

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

    13.31                           2026-05-24       DH_INSTALLSYSTEMDUSER(1)

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
