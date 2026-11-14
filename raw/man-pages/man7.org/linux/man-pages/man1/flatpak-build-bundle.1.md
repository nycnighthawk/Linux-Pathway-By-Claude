---
{"title": "flatpak-build-bundle(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-build-bundle.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-build-bundle(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK BUILD-BUNDL(1)     flatpak build-bundle    FLATPAK BUILD-BUNDL(1)

## [](#NAME)NAME

           flatpak-build-bundle - Create a single-file bundle from a local
           repository

## [](#SYNOPSIS)SYNOPSIS

           flatpak build-bundle [OPTION...] LOCATION FILENAME NAME [BRANCH]

## [](#DESCRIPTION)DESCRIPTION

           Creates a single-file named FILENAME for the application (or
           runtime) named NAME in the repository at LOCATION. If a BRANCH is
           specified, this branch of the application is used.

           The collection ID set on the repository at LOCATION (if set) will
           be used for the bundle.

           Unless --oci is used, the format of the bundle file is that of an
           ostree static delta (against an empty base) with some flatpak
           specific metadata for the application icons and appdata.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           --runtime
               Export a runtime instead of an application.

           --arch=ARCH
               The arch to create a bundle for. See flatpak
               --supported-arches for architectures supported by the host.

           --repo-url=URL
               The URL for the repository from which the application can be
               updated. Installing the bundle will automatically configure a
               remote for this URL.

           --runtime-repo=URL
               The URL for a .flatpakrepo file that contains the information
               about the repository that supplies the runtimes required by
               the app.

           --gpg-keys=FILE
               Add the GPG key from FILE (use - for stdin).

           --gpg-homedir=PATH
               GPG Homedir to use when looking for keyrings.

           --from-commit=COMMIT
               The OSTree commit to create a delta bundle from.

           --oci
               Export to an OCI image instead of a Flatpak bundle.

           --oci-layer-compress=gzip|zstd
               Choose how to compress the layers in OCI images. gzip (the
               default) is universally supported, but zstd compresses faster
               and results in smaller images. As of 2023, zstd support is
               present in most major registries.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak build-bundle /var/lib/flatpak/repo
           gnome-calculator.flatpak org.gnome.Calculator stable

           $ flatpak build-bundle ~/.local/share/flatpak/repo
           gnome-calculator.flatpak org.gnome.Calculator stable

## [](#SEE_ALSO)SEE ALSO

           ostree(1), flatpak(1), flatpak-build-init(1), flatpak-build(1),
           flatpak-build-finish(1), flatpak-build-import-bundle(1),
           flatpak-build-update-repo(1)

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

    flatpak                                            FLATPAK BUILD-BUNDL(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-build-import-bundle(1)](../man1/flatpak-build-import-bundle.1.html),  [flatpak-install(1)](../man1/flatpak-install.1.html)

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
