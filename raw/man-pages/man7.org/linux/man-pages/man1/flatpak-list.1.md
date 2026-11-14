---
{"title": "flatpak-list(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-list.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-list(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FIELDS](#FIELDS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK LIST(1)                flatpak list               FLATPAK LIST(1)

## [](#NAME)NAME

           flatpak-list - List installed applications and/or runtimes

## [](#SYNOPSIS)SYNOPSIS

           flatpak list [OPTION...]

## [](#DESCRIPTION)DESCRIPTION

           Lists the names of the installed applications and runtimes.

           By default, both apps and runtimes are shown, but you can change
           this by using the --app or --runtime options.

           By default, both per-user and system-wide installations are shown.
           Use the --user, --installation or --system options to change this.

           The list command can also be used to find installed apps that use
           a certain runtime, with the --app-runtime option.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               List per-user installations.

           --system
               List the default system-wide installations.

           --installation=NAME
               List a system-wide installation specified by NAME among those
               defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --arch=ARCH
               List apps/runtimes for this architecture. See flatpak
               --supported-arches for architectures supported by the host.

           -d, --show-details
               Show origin, sizes and other extra information. Equivalent to
               --columns=all.

           --app
               List applications.

           --runtime
               List runtimes.

           --all, -a
               List all installed runtimes, including locale and debug
               extensions. These are hidden by default.

           --app-runtime=RUNTIME
               List applications that use the given runtime.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

           --columns=FIELD,...
               Specify what information to show about each ref. You can list
               multiple fields, or use this option multiple times.

               Append :s[tart], :m[iddle], :e[nd] or :f[ull] to column names
               to change ellipsization.

## [](#FIELDS)FIELDS

           The following fields are understood by the --columns option:

           name
               Show the name

           description
               Show the description

           application
               Show the application or runtime ID

           arch
               Show the architecture

           branch
               Show the branch

           runtime
               Show the used runtime

           version
               Show the version

           ref
               Show the ref

           origin
               Show the origin remote

           installation
               Show the installation

           active
               Show the active commit

           latest
               Show the latest commit

           size
               Show the installed size

           options
               Show options

           all
               Show all columns

           help
               Show the list of available columns

           Note that field names can be abbreviated to a unique prefix.

## [](#EXAMPLES)EXAMPLES

           $ flatpak --user --columns=app list

               Application
               org.gnome.Builder
               org.freedesktop.glxgears
               org.gnome.MyApp
               org.gnome.gedit

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-install(1), flatpak-update(1)

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

    flatpak                                                   FLATPAK LIST(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-create-usb(1)](../man1/flatpak-create-usb.1.html),  [flatpak-install(1)](../man1/flatpak-install.1.html),  [flatpak-make-current(1)](../man1/flatpak-make-current.1.html),  [flatpak-update(1)](../man1/flatpak-update.1.html)

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
