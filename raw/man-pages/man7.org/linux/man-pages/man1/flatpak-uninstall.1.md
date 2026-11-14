---
{"title": "flatpak-uninstall(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-uninstall.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-uninstall(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK UNINSTALL(1)        flatpak uninstall        FLATPAK UNINSTALL(1)

## [](#NAME)NAME

           flatpak-uninstall - Uninstall an application or runtime

## [](#SYNOPSIS)SYNOPSIS

           flatpak uninstall [OPTION...] [REF...]

## [](#DESCRIPTION)DESCRIPTION

           Uninstalls an application or runtime.  REF is a reference to the
           application or runtime to uninstall.

           Each REF argument is a full or partial identifier in the flatpak
           ref format, which looks like "(app|runtime)/ID/ARCH/BRANCH". All
           elements except ID are optional and can be left out, including the
           slashes, so most of the time you need only specify ID. Any part
           left out will be matched against what is installed, and if there
           are multiple matches you will be prompted to choose between them.
           You will also be prompted if REF doesn't match any installed ref
           exactly but is similar (e.g. "gedit" is similar to
           "org.gnome.gedit"), but this fuzzy matching behavior is disabled
           if REF contains any slashes or periods.

           By default this looks for both installed apps and runtimes with
           the given REF, but you can limit this by using the --app or
           --runtime option, or by supplying the initial element in the REF.

           Normally, this command removes the ref for this
           application/runtime from the local OSTree repository and purges
           any objects that are no longer needed to free up disk space. If
           the same application is later reinstalled, the objects will be
           pulled from the remote repository again. The --keep-ref option can
           be used to prevent this.

           When --delete-data is specified while removing an app, its data
           directory in ~/.var/app and any permissions it might have are
           removed. When --delete-data is used without a REF, all 'unowned'
           app data is removed.

           Unless overridden with the --system, --user, or --installation
           options, this command searches both the system-wide installation
           and the per-user one for REF and errors out if it exists in more
           than one.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           --keep-ref
               Keep the ref for the application and the objects belonging to
               it in the local repository.

           -u, --user
               Uninstalls from a per-user installation.

           --system
               Uninstalls from the default system-wide installation.

           --installation=NAME
               Uninstalls from a system-wide installation specified by NAME
               among those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --arch=ARCH
               The architecture to uninstall, instead of the architecture of
               the host system. See flatpak --supported-arches for
               architectures supported by the host.

           --all
               Remove all refs on the system.

           --unused
               Remove unused refs on the system.

           -y, --assumeyes
               Automatically answer yes to all questions. This is useful for
               automation.

           --noninteractive
               Produce minimal output and avoid most questions. This is
               suitable for use in non-interactive situations, e.g. in a
               build script.

           --app
               Only look for an app with the given name.

           --runtime
               Only look for a runtime with the given name.

           --no-related
               Don't uninstall related extensions, such as the locale data.

           --force-remove
               Remove files even if they're in use by a running application.

           --delete-data
               Remove app data in ~/.var/app and in the permission store.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak --user uninstall org.gnome.gedit

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

    flatpak                                              FLATPAK UNINSTALL(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-pin(1)](../man1/flatpak-pin.1.html)

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
