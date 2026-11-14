---
{"title": "flatpak-remotes(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-remotes.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-remotes(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FIELDS](#FIELDS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK REMOTES(1)           flatpak remotes           FLATPAK REMOTES(1)

## [](#NAME)NAME

           flatpak-remotes - List remote repositories

## [](#SYNOPSIS)SYNOPSIS

           flatpak remotes [OPTION...]

## [](#DESCRIPTION)DESCRIPTION

           Lists the known remote repositories, in priority order.

           By default, both per-user and system-wide installations are shown.
           Use the --user, --system or --installation options to change this.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               Show the per-user configuration.

           --system
               Show the default system-wide configuration.

           --installation=NAME
               Show a system-wide installation by NAME among those defined in
               /etc/flatpak/installations.d/. Using --installation=default is
               equivalent to using --system.

           -d, --show-details
               Show more information for each repository in addition to the
               name. Equivalent to --columns=all.

           --show-disabled
               Show disabled repos.

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
               Show the name of the remote

           title
               Show the title of the remote

           url
               Show the URL of the remote

           filter
               Show the path to the client-side filter of the remote.

           collection
               Show the collection ID of the remote

           priority
               Show the priority of the remote

           options
               Show options

           comment
               Show comment

           description
               Show description

           homepage
               Show homepage

           icon
               Show icon

           all
               Show all columns

           help
               Show the list of available columns

           Note that field names can be abbreviated to a unique prefix.

## [](#EXAMPLES)EXAMPLES

           $ flatpak remotes --user --show-details

               testrepo  Test Repository      http://209.132.179.91/repo/ no-gpg-verify

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-remote-add(1), flatpak-remote-delete(1)

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

    flatpak                                                FLATPAK REMOTES(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-remote-add(1)](../man1/flatpak-remote-add.1.html),  [flatpak-remote-delete(1)](../man1/flatpak-remote-delete.1.html),  [flatpak-remote-info(1)](../man1/flatpak-remote-info.1.html),  [flatpak-remote-ls(1)](../man1/flatpak-remote-ls.1.html),  [flatpak-remote-modify(1)](../man1/flatpak-remote-modify.1.html)

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
