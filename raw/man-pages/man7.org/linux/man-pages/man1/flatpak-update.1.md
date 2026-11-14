---
{"title": "flatpak-update(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-update.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-update(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK UPDATE(1)             flatpak update            FLATPAK UPDATE(1)

## [](#NAME)NAME

           flatpak-update - Update an application or runtime

## [](#SYNOPSIS)SYNOPSIS

           flatpak update [OPTION...] [REF...]

           flatpak update [OPTION...] --appstream [REMOTE]

## [](#DESCRIPTION)DESCRIPTION

           Updates applications and runtimes.  REF is a reference to the
           application or runtime to update. If no REF is given, everything
           is updated, as well as appstream info for all remotes.

           Each REF argument is a full or partial identifier in the flatpak
           ref format, which looks like "(app|runtime)/ID/ARCH/BRANCH". All
           elements except ID are optional and can be left out, including the
           slashes, so most of the time you need only specify ID. Any part
           left out will be matched against what is installed, and if there
           are multiple matches an error message will list the alternatives.

           By default this looks for both apps and runtimes with the given
           REF, but you can limit this by using the --app or --runtime
           option, or by supplying the initial element in the REF.

           Normally, this command updates the application to the tip of its
           branch. But it is possible to check out another commit, with the
           --commit option.

           If the configured remote for a ref being updated has a collection
           ID configured on it, Flatpak will search the sideload-repos
           directories configured either with the --sideload-repo option, or
           on a per-installation or system-wide basis (see flatpak(1)).

           For OCI remotes, sideload repositories can also be specified as
           --sideload-repo=oci:PATH or --sideload-repo=oci-archive:PATH,
           where path points to an OCI image layout or archive of an OCI
           image layout. (See containers-transports(5).) When specified in
           this fashion, the images found in the image layout are available
           for all OCI remotes, without regard to collection ID. For this
           reason, there is no directory equivalent - it can only be
           specified on the command line.

           Note that updating a runtime is different from installing a
           different branch, and runtime updates are expected to keep strict
           compatibility. If an application update does cause a problem, it
           is possible to go back to the previous version, with the --commit
           option.

           In addition to updates, this command will offer to uninstall any
           unused end-of-life runtimes. Runtimes that were explicitly
           installed (not as a dependency) or explicitly pinned (see
           flatpak-pin(1)) are left installed even if unused and end-of-life.

           Unless overridden with the --user, --system or --installation
           option, this command updates any matching refs in the standard
           system-wide installation and the per-user one.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               Update a per-user installation.

           --system
               Update the default system-wide installation.

           --installation=NAME
               Updates a system-wide installation specified by NAME among
               those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --arch=ARCH
               The architecture to update for. See flatpak --supported-arches
               for architectures supported by the host.

           --subpath=PATH
               Install only a subpath of the ref. This is mainly used to
               install a subset of locales. This can be added multiple times
               to install multiple subpaths. If this is not specified the
               subpaths specified at install time are reused.

           --commit=COMMIT
               Update to this commit, instead of the tip of the branch. You
               can find commits using flatpak remote-info --log REMOTE REF.

           --no-deploy
               Download the latest version, but don't deploy it.

           --no-pull
               Don't download the latest version, deploy whatever is locally
               available.

           --no-related
               Don't download related extensions, such as the locale data.

           --no-deps
               Don't update or install runtime dependencies when installing.

           --app
               Only look for an app with the given name.

           --appstream
               Update appstream for REMOTE, or all remotes if no remote is
               specified.

           --runtime
               Only look for a runtime with the given name.

           --sideload-repo=PATH
               Adds an extra local ostree repo as a source for installation.
               This is equivalent to using the sideload-repos directories
               (see flatpak(1)), but can be done on a per-command basis. Any
               path added here is used in addition to ones in those
               directories.

           -y, --assumeyes
               Automatically answer yes to all questions (or pick the most
               prioritized answer). This is useful for automation.

           --noninteractive
               Produce minimal output and avoid most questions. This is
               suitable for use in non-interactive situations, e.g. in a
               build script.

           --force-remove
               Remove old files even if they're in use by a running
               application.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak --user update org.gnome.gedit

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-install(1), flatpak-list(1),
           ostree-find-remotes(1)

## [](#COLOPHON)COLOPHON

           This page is part of the flatpak (a tool for building and
           distributing desktop applications on Linux) project.  Information
           about the project can be found at ⟨http://flatpak.org/⟩.  It is
           not known how to report bugs for this man page; if you know,
           please send a mail to man-pages@man7.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/flatpak/flatpak⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    flatpak                                                 FLATPAK UPDATE(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-info(1)](../man1/flatpak-info.1.html),  [flatpak-install(1)](../man1/flatpak-install.1.html),  [flatpak-list(1)](../man1/flatpak-list.1.html),  [flatpak-mask(1)](../man1/flatpak-mask.1.html)

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
