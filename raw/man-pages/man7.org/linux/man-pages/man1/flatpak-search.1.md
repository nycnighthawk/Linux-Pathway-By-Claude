---
{"title": "flatpak-search(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-search.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-search(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FIELDS](#FIELDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK SEARCH(1)             flatpak search            FLATPAK SEARCH(1)

## [](#NAME)NAME

           flatpak-search - Search for applications and runtimes

## [](#SYNOPSIS)SYNOPSIS

           flatpak search TEXT

## [](#DESCRIPTION)DESCRIPTION

           Searches for applications and runtimes matching TEXT. Note that
           this uses appstream data that can be updated with the flatpak
           update command. The appstream data is updated automatically only
           if it's at least a day old.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -u, --user
               Only search through remotes in the per-user installation.

           --system
               Only search through remotes in the default system-wide
               installation.

           --installation=NAME
               Show a system-wide installation by NAME among those defined in
               /etc/flatpak/installations.d/. Using --installation=default is
               equivalent to using --system.

           -h, --help
               Show help options and exit.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

           --columns=FIELD,...
               Specify what information to show about each result. You can
               list multiple fields, or use this option multiple times.

               Append :s[tart], :m[iddle], :e[nd] or :f[ull] to column names
               to change ellipsization.

## [](#FIELDS)FIELDS

           The following fields are understood by the --columns option:

           name
               Show the name

           description
               Show the description

           application
               Show the application ID

           version
               Show the version

           branch
               Show the branch

           remotes
               Show the remotes

           all
               Show all columns

           help
               Show the list of available columns

           Note that field names can be abbreviated to a unique prefix.

## [](#SEE_ALSO)SEE ALSO

           flatpak(1)

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

    flatpak                                                 FLATPAK SEARCH(1)

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
