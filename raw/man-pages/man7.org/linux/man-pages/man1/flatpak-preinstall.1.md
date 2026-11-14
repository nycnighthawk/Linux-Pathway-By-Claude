---
{"title": "flatpak-preinstall(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-preinstall.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-preinstall(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK PREINSTALL(1)       flatpak preinstall      FLATPAK PREINSTALL(1)

## [](#NAME)NAME

           flatpak-preinstall - Install flatpaks that are part of the
           operating system

## [](#SYNOPSIS)SYNOPSIS

           flatpak preinstall [OPTION...]

## [](#DESCRIPTION)DESCRIPTION

           This command manages flatpaks that are part of the operating
           system. If no options are given, running flatpak preinstall will
           synchronize (install and remove) flatpaks to match the set that
           the OS vendor has chosen.

           Preinstalled flatpaks are defined by dropping .preinstall files
           into the directories /usr/share/flatpak/preinstall.d/ and
           /etc/flatpak/preinstall.d/. The OS runs flatpak preinstall -y (or
           its GUI equivalent) on system startup, which then does the actual
           installation.

           This system allows the OS vendor to define the list of flatpaks
           that are installed together with the OS, and also makes it
           possible for the OS vendor to make changes to the list in the
           future, which is then applied once flatpak preinstall is run next
           time. Users can opt out of preinstalled flatpaks by simply
           uninstalling them, at which point they won't get automatically
           reinstalled again.

## [](#FILE_FORMAT)FILE FORMAT

           The .preinstall file is using the same .ini file format that is
           used for systemd unit files or application .desktop files.

       [Flatpak Preinstall NAME]
           The NAME is the fully qualified name of the runtime or
           application. All the information for a single runtime or
           application is contained in one [Flatpak Preinstall NAME] group.
           Multiple groups can be defined in a single file.

           The following keys can be present in this group:

           Install (boolean)
               Whether this group should be installed. If this key is not
               specified, the group will be installed.

           Branch (string)
               The name of the branch from which to install the application
               or runtime. If this key is not specified, the "master" branch
               is used.

           IsRuntime (boolean)
               Whether this group refers to a runtime. If this key is not
               specified, the group is assumed to refer to an application.

           CollectionID (string)
               The collection ID of the remote to use, if it has one.

## [](#EXAMPLE)EXAMPLE

               [Flatpak Preinstall org.gnome.Loupe]
               Branch=stable
               IsRuntime=false

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

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

           --no-deploy
               Download the latest version, but don't deploy it.

           --no-pull
               Don't download the latest version, deploy whatever is locally
               available.

           --no-related
               Don't download related extensions, such as the locale data.

           --no-deps
               Don't verify runtime dependencies when installing.

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

           $ flatpak preinstall

## [](#SEE_ALSO)SEE ALSO

           flatpak(1),

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

    flatpak                                             FLATPAK PREINSTALL(1)

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
