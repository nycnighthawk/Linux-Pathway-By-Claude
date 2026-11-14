---
{"title": "flatpak-create-usb(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-create-usb.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-create-usb(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK CREATE-USB(1)       flatpak create-usb      FLATPAK CREATE-USB(1)

## [](#NAME)NAME

           flatpak-create-usb - Copy apps and/or runtimes onto removable
           media.

## [](#SYNOPSIS)SYNOPSIS

           flatpak create-usb [OPTION...] MOUNT-PATH REF...

## [](#DESCRIPTION)DESCRIPTION

           Copies the specified apps and/or runtimes REFs onto the removable
           media mounted at MOUNT-PATH, along with all the dependencies and
           metadata needed for installing them. This is one way of
           transferring flatpaks between computers that doesn't require an
           Internet connection. After using this command, the USB drive can
           be connected to another computer which already has the relevant
           remote(s) configured, and Flatpak will install or update from the
           drive offline (see below). If online, the drive will be used as a
           cache, meaning some objects will be pulled from it and others from
           the Internet. For this process to work a collection ID must be
           configured on the relevant remotes on both the source and
           destination computers, and on the remote server.

           On the destination computer one can install from the USB (or any
           mounted filesystem) using the --sideload-repo option with flatpak
           install. It's also possible to configure sideload paths using
           symlinks; see flatpak(1). Flatpak also includes systemd units to
           automatically sideload from hot-plugged USB drives, but these may
           or may not be enabled depending on your Linux distribution.

           Each REF argument is a full or partial identifier in the flatpak
           ref format, which looks like "(app|runtime)/ID/ARCH/BRANCH". All
           elements except ID are optional and can be left out, including the
           slashes, so most of the time you need only specify ID. Any part
           left out will be matched against what is installed, and if there
           are multiple matches an error message will list the alternatives.

           By default this looks for both installed apps and runtimes with
           the given REF, but you can limit this by using the --app or
           --runtime option.

           All REFs must be in the same installation (user, system, or
           other). Otherwise it's ambiguous which repository metadata refs to
           put on the USB drive.

           By default flatpak create-usb uses .ostree/repo as the destination
           directory under MOUNT-PATH but if you specify another location
           using --destination-repo a symbolic link will be created for you
           in .ostree/repos.d. This ensures that either way the repository
           will be found by flatpak (and other consumers of libostree) for
           install/update operations.

           Unless overridden with the --system, --user, or --installation
           options, this command searches both the system-wide installation
           and the per-user one for REF and errors out if it exists in more
           than one.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               Copy refs from the per-user installation.

           --system
               Copy refs from the default system-wide installation.

           --installation=NAME
               Copy refs from a system-wide installation specified by NAME
               among those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --app
               Assume that all REFs are apps if not explicitly specified.

           --runtime
               Assume that all REFs are runtimes if not explicitly specified.

           --destination-repo=DEST
               Create the repository in DEST under MOUNT-PATH, rather than
               the default location.

           --allow-partial
               Don't print a warning when exporting partially installed
               commits, for example locale extensions without all languages.
               These can cause problems when installing them, for example if
               the language config is different on the installing side.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak create-usb
           /run/media/mwleeds/1a9b4cb2-a7ef-4d9b-91a5-6eaf8fdd2bf6/
           com.endlessm.wiki_art.en

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak remote-modify(1), flatpak-install(1),
           flatpak-list(1), ostree-create-usb(1)

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

    flatpak                                             FLATPAK CREATE-USB(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html)

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
