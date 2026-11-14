---
{"title": "flatpak-remote-info(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-remote-info.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-remote-info(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK REMOTE-INFO(1)     flatpak remote-info     FLATPAK REMOTE-INFO(1)

## [](#NAME)NAME

           flatpak-remote-info - Show information about an application or
           runtime in a remote

## [](#SYNOPSIS)SYNOPSIS

           flatpak remote-info [OPTION...] REMOTE REF

## [](#DESCRIPTION)DESCRIPTION

           Shows information about the runtime or application REF from the
           remote repository with the name REMOTE. You can find all
           configured remote repositories with flatpak remotes.

           By default, the output is formatted in a friendly format. If you
           specify one of the --show-...  options, the output is instead
           formatted in a machine-readable format.

           Unless overridden with the --system, --user, or --installation
           options, this command uses either the default system-wide
           installation or the per-user one, depending on which has the
           specified REMOTE.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               Use the per-user configuration.

           --system
               Use the default system-wide configuration.

           --installation=NAME
               Use a system-wide installation specified by NAME among those
               defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --cached
               Prefer to use locally cached information if possible, even
               though it may be out of date. This is faster, but risks
               returning stale information. Also, some information is not
               cached so will not be available.

           --runtime
               Assume that REF is a runtime if not explicitly specified.

           --app
               Assume that REF is an app if not explicitly specified.

           --arch=ARCH
               The default architecture to look for, if not given explicitly
               in the REF. See flatpak --supported-arches for architectures
               supported by the host.

           --commit=COMMIT
               Show information about the specific commit, rather than the
               latest version.

           --log
               Display a log of previous versions.

           -r, --show-ref
               Show the matched ref.

           -c, --show-commit
               Show the commit id.

           -p, --show-parent
               Show the parent commit id.

           -m, --show-metadata
               Show the metadata.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak --user remote-info flathub org.gnome.gedit

               Ref: app/org.gnome.gedit/x86_64/stable
               ID: org.gnome.gedit
               Arch: x86_64
               Branch: stable
               Date: 2017-07-31 16:05:22 +0000
               Subject: Build org.gnome.gedit at 3ec291fc1ce4d78220527fa79576f4cc1481ebe5
               Commit: 3de7e9dde3bb8382aad9dfbbff20eccd9bf2100bc1887a3619ec0372e8066bf7
               Parent: -
               Download size: 3,4 MB
               Installed size: 11,1 MB
               Runtime: org.gnome.Platform/x86_64/3.24

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-remotes(1) flatpak-remote-ls(1)

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

    flatpak                                            FLATPAK REMOTE-INFO(1)

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
