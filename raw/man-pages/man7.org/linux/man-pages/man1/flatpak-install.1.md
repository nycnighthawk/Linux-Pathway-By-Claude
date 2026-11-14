---
{"title": "flatpak-install(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-install.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-install(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK INSTALL(1)           flatpak install           FLATPAK INSTALL(1)

## [](#NAME)NAME

           flatpak-install - Install an application or runtime

## [](#SYNOPSIS)SYNOPSIS

           flatpak install [OPTION...] [REMOTE] REF...

           flatpak install [OPTION...] [--from|--bundle|--image] LOCATION

## [](#DESCRIPTION)DESCRIPTION

           Installs an application or runtime. The primary way to install is
           to specify a REMOTE name as the source and one or more REFs to
           specify the application or runtime to install. If REMOTE is
           omitted, the configured remotes are searched for the first REF and
           the user is asked to confirm the resulting choice.

           Each REF argument is a full or partial identifier in the flatpak
           ref format, which looks like "(app|runtime)/ID/ARCH/BRANCH". All
           elements except ID are optional and can be left out, including the
           slashes, so most of the time you need only specify ID. Any part
           left out will be matched against what is in the remote, and if
           there are multiple matches you will be prompted to choose one of
           them. You will also be prompted with choices if REF doesn't match
           anything in the remote exactly but is similar to one or more refs
           in the remote (e.g. "devhelp" is similar to "org.gnome.Devhelp"),
           but this fuzzy matching behavior is disabled if REF contains any
           slashes or periods.

           By default this looks for both apps and runtimes with the given
           REF in the specified REMOTE, but you can limit this by using the
           --app or --runtime option, or by supplying the initial element in
           the REF.

           If REMOTE is a uri or a path (absolute or relative starting with
           ./) to a local repository, then that repository will be used as
           the source, and a temporary remote will be created for the
           lifetime of the REF.

           If the specified REMOTE has a collection ID configured on it,
           Flatpak will search the sideload-repos directories configured
           either with the --sideload-repo option, or on a per-installation
           or system-wide basis (see flatpak(1)).

           For OCI remotes, sideload repositories can also be specified as
           --sideload-repo=oci:PATH or --sideload-repo=oci-archive:PATH,
           where path points to an OCI image layout or archive of an OCI
           image layout. (See containers-transports(5).) When specified in
           this fashion, the images found in the image layout are available
           for all OCI remotes, without regard to collection ID. For this
           reason, there is no directory equivalent - it can only be
           specified on the command line.

           The alternative form of the command (with --from, --bundle, or
           --image) allows to install directly from a source. The source can
           be a .flatpak single-file bundle, .flatpakref application
           description, or a reference to an OCI image. The options are
           optional if the first argument has the expected filename extension
           or prefix.

           Note that flatpak allows to have multiple branches of an
           application and runtimes installed and used at the same time.
           However, only one version of an application can be current,
           meaning its exported files (for instance desktop files and icons)
           are visible to the host. The last installed version is made
           current by default, but this can manually changed with flatpak
           make-current.

           Unless overridden with the --user or the --installation option,
           this command installs the application or runtime in the default
           system-wide installation.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           --bundle
               Treat LOCATION as a single-bundle file. This is assumed if the
               argument ends with .flatpak.

           --from
               Treat LOCATION as an application description file. This is
               assumed if the argument ends with .flatpakref.

           --image
               Treat LOCATION as the location of a Flatpak in OCI image
               format.  [LOCATION] is in the format of
               containers-transports(5). Supported schemes are docker://,
               oci:, and oci-archive:. This is assumed if the argument starts
               with one of these schemes.

           --reinstall
               Uninstall first if already installed.

           -u, --user
               Install the application or runtime in a per-user installation.

           --system
               Install the application or runtime in the default system-wide
               installation.

           --installation=NAME
               Install the application or runtime in a system-wide
               installation specified by NAME among those defined in
               /etc/flatpak/installations.d/. Using --installation=default is
               equivalent to using --system.

           --arch=ARCH
               The default architecture to install for, if not given
               explicitly in the REF. See flatpak --supported-arches for
               architectures supported by the host.

           --subpath=PATH
               Install only a subpath of REF. This is mainly used to install
               a subset of locales. This can be added multiple times to
               install multiple subpaths.

           --gpg-file=FILE
               Check bundle signatures with GPG key from FILE (- for stdin).

           --no-deploy
               Download the latest version, but don't deploy it.

           --no-pull
               Don't download the latest version, deploy whatever is locally
               available.

           --no-related
               Don't download related extensions, such as the locale data.

           --no-deps
               Don't verify runtime dependencies when installing.

           --or-update
               Normally install just ignores things that are already
               installed (printing a warning), but if --or-update is
               specified it silently turns it into an update operation
               instead.

           --app
               Assume that all REFs are apps if not explicitly specified.

           --runtime
               Assume that all REFs are runtimes if not explicitly specified.

           --sideload-repo=PATH
               Adds an extra local ostree repo as a source for installation.
               This is equivalent to using the sideload-repos directories
               (see flatpak(1)), but can be done on a per-command basis. Any
               path added here is used in addition to ones in those
               directories.

           --include-sdk
               For each app being installed, also installs the SDK that was
               used to build it. Implies --or-update; incompatible with
               --no-deps.

           --include-debug
               For each ref being installed, as well as all dependencies,
               also installs its debug info. Implies --or-update;
               incompatible with --no-deps.

           -y, --assumeyes
               Automatically answer yes to all questions (or pick the most
               prioritized answer). This is useful for automation.

           --noninteractive
               Produce minimal output and avoid most questions. This is
               suitable for use in non-interactive situations, e.g. in a
               build script.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak install gedit

           $ flatpak install flathub org.gnome.gedit

           $ flatpak --installation=default install flathub org.gnome.gedit

           $ flatpak --user install flathub org.gnome.gedit//3.30

           $ flatpak --user install
           https://flathub.org/repo/appstream/org.gnome.gedit.flatpakref 

           $ flatpak --system install org.gnome.gedit.flatpakref

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-update(1), flatpak-list(1),
           flatpak-build-bundle(1), flatpakref(5), flatpak-make-current(1),
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

    flatpak                                                FLATPAK INSTALL(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-create-usb(1)](../man1/flatpak-create-usb.1.html),  [flatpak-info(1)](../man1/flatpak-info.1.html),  [flatpak-list(1)](../man1/flatpak-list.1.html),  [flatpak-make-current(1)](../man1/flatpak-make-current.1.html),  [flatpak-update(1)](../man1/flatpak-update.1.html),  [flatpakref(5)](../man5/flatpakref.5.html)

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
