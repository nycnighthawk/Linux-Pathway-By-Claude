---
{"title": "dh_installinit(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installinit.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installinit(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLINIT(1)               Debhelper               DH_INSTALLINIT(1)

## [](#NAME)NAME

           dh_installinit - install service init files into package build
           directories

## [](#SYNOPSIS)SYNOPSIS

           dh_installinit [debhelper options] [--name=name] [-n] [-R] [-r]
           [-d] [-- params]

## [](#DESCRIPTION)DESCRIPTION

           dh_installinit is a debhelper program that is responsible for
           installing init scripts with associated defaults files.  In
           compatibility levels up to and including 10, dh_installinit will
           also install some systemd related files provided by the debian
           packaging (see the "FILES" section below).  In compatibility
           levels up to and including 11, dh_installinit will also handle
           upstart jobs provided in the debian packaging (see the "FILES" for
           more information on this as well).

           It also automatically generates the postinst and postrm and prerm
           commands needed to set up the symlinks in /etc/rc*.d/ to start and
           stop the init scripts.

           In compat 10 or earlier: If a package only ships a systemd service
           file and no sysvinit script is provided, you may want to exclude
           the call to dh_installinit for that package (e.g. via -N).
           Otherwise, you may get warnings from lintian about init.d scripts
           not being included in the package.

## [](#FILES)FILES

           debian/package.init
               If this exists, it is installed into etc/init.d/package in the
               package build directory.

           debian/package.default
               If this exists, it is installed into etc/default/package in
               the package build directory.

           debian/package.upstart
               In compatibility level 11, this file will trigger an error
               with a reminder about ensuring the proper removal of the
               upstart file in the previous package version.  Please consider
               using the "rm_conffile" feature from dh_installdeb(1) to
               ensure the proper removal of previous upstart files.

               In compatibility level 10, if this file exists, it is
               installed into etc/init/package.conf in the package build
               directory.

           debian/package.service
               If this exists, it is installed into
               usr/lib/systemd/system/package.service in the package build
               directory. Only used in compat levels 10 and below.

           debian/package.tmpfile
               If this exists, it is installed into
               usr/lib/tmpfiles.d/package.conf in the package build
               directory. Only used in compat levels 10 and below.

## [](#OPTIONS)OPTIONS

           -n, --no-scripts
               Do not modify postinst/postrm/prerm scripts.

           -o, --only-scripts
               Only modify postinst/postrm/prerm scripts, do not actually
               install any init script, default files, upstart job or systemd
               service file. May be useful if the file is shipped and/or
               installed by upstream in a way that doesn't make it easy to
               let dh_installinit find it.

               Caveat: This will bypass all the regular checks and
               unconditionally modify the scripts.  You will almost certainly
               want to use this with -p to limit, which packages are affected
               by the call.  Example:

                override_dh_installinit:
                       dh_installinit -pfoo --only-scripts
                       dh_installinit --remaining

           -R, --restart-after-upgrade
               Do not stop the init script until after the package upgrade
               has been completed.  This is the default behaviour in compat
               10.

               In early compat levels, the default was to stop the script in
               the prerm, and starts it again in the postinst.

               This can be useful for daemons that should not have a possibly
               long downtime during upgrade. But you should make sure that
               the daemon will not get confused by the package being upgraded
               while it's running before using this option.

           --no-restart-after-upgrade
               Undo a previous --restart-after-upgrade (or the default of
               compat 10).  If no other options are given, this will cause
               the service to be stopped in the prerm script and started
               again in the postinst script.

           -r, --no-stop-on-upgrade, --no-restart-on-upgrade
               Do not stop init script on upgrade.  This has the side-effect
               of not restarting the service as a part of the upgrade.

               If you want to restart the service with minimal downtime,
               please use --restart-after-upgrade (default in compat 10 or
               later).  If you want the service to be restarted but be
               stopped during the upgrade, then please use
               --no-restart-after-upgrade (note the "after-upgrade").

               Note that the --no-restart-on-upgrade alias is deprecated and
               will be removed in compat 12.  This is to avoid confusion with
               the --no-restart-after-upgrade option.  The
               --no-stop-on-upgrade variant was introduced in debhelper 10.2
               (included in Debian stretch).

           --no-start
               Do not start the init script on install or upgrade, or stop it
               on removal.  Only call update-rc.d. Useful for rcS scripts.

           --no-enable
               Disable the init script on purge, but do not enable them on
               install.  Note that this requires init-system-helpers >= 1.51
               as it is the first (functional) version that supports
               update-rc.d <script> defaults-disabled.

               Note that this option does not affect whether the services are
               started.  Please remember to also use --no-start if the
               service should not be started.

               Cannot be combined with -uparams, --update-rcd-params=params,
               or -- params.

           -d, --remove-d
               Remove trailing d from the name of the package, and use the
               result for the filename the upstart job file is installed as
               in etc/init/ , and for the filename the init script is
               installed as in etc/init.d and the default file is installed
               as in etc/default/. This may be useful for daemons with names
               ending in d. (Note: this takes precedence over the
               --init-script parameter described below.)

           -uparams --update-rcd-params=params
           -- params
               Pass params to update-rc.d(8). If not specified, defaults (or
               defaults-disabled with --no-enable) will be passed to
               update-rc.d(8).

               Cannot be combined with --no-enable.

           --name=name
               Install the init script (and default file) as well as upstart
               job file using the filename name instead of the default
               filename, which is the package name. When this parameter is
               used, dh_installinit looks for and installs files named
               debian/package.name.init, debian/package.name.default and
               debian/package.name.upstart instead of the usual
               debian/package.init, debian/package.default and
               debian/package.upstart.

           --init-script=scriptname
               Use scriptname as the filename the init script is installed as
               in etc/init.d/ (and also use it as the filename for the
               defaults file, if it is installed). If you use this parameter,
               dh_installinit will look to see if a file in the debian/
               directory exists that looks like package.scriptname and if so
               will install it as the init script in preference to the files
               it normally installs.

               This parameter is deprecated, use the --name parameter
               instead. This parameter is incompatible with the use of
               upstart jobs.

           --error-handler=function
               Call the named shell function if running the init script
               fails. The function should be provided in the prerm and
               postinst scripts, before the #DEBHELPER# token.

## [](#NOTES)NOTES

           Note that this command is not idempotent. dh_prep(1) should be
           called between invocations of this command. Otherwise, it may
           cause multiple instances of the same text to be added to
           maintainer scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7), dh_installsystemd(1)

           This program is a part of debhelper.

## [](#AUTHORS)AUTHORS

           Joey Hess <joeyh@debian.org>

           Steve Langasek <steve.langasek@canonical.com>

           Michael Stapelberg <stapelberg@debian.org>

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

    13.31                           2026-05-24              DH_INSTALLINIT(1)

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
