---
{"title": "flatpak-repair(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-repair.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-repair(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK REPAIR(1)             flatpak repair            FLATPAK REPAIR(1)

## [](#NAME)NAME

           flatpak-repair - Repair a flatpak installation

## [](#SYNOPSIS)SYNOPSIS

           flatpak repair [OPTION...]

## [](#DESCRIPTION)DESCRIPTION

           Repair a flatpak installation by pruning and reinstalling invalid
           objects. The repair command does all of the following:

           •   Scan all locally available refs, removing any that don't
               correspond to a deployed ref.

           •   Verify each commit they point to, removing any invalid objects
               and noting any missing objects.

           •   Remove any refs that had an invalid object, and any
               non-partial refs that had missing objects.

           •   Prune all objects not referenced by a ref, which gets rid of
               any possibly invalid non-scanned objects.

           •   Enumerate all deployed refs and re-install any that are not in
               the repo (or are partial for a non-subdir deploy).

           Note that flatpak repair has to be run with root privileges to
           operate on the system installation.

           An alternative command for repairing OSTree repositories is ostree
           fsck.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               Repair per-user installation.

           --system
               Repair system-wide installation.

           --installation=NAME
               Repair the system-wide installation specified by NAME among
               those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --dry-run
               Only report inconsistencies, don't make any changes

           --reinstall-all
               Reinstall all refs, regardless of whether they were removed
               from the repo or not

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ sudo flatpak repair

           $ flatpak repair --user

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), ostree-fsck(1)

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

    flatpak                                                 FLATPAK REPAIR(1)

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
