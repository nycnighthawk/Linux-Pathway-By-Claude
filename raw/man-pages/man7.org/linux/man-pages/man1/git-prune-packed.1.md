---
{"title": "git-prune-packed(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-prune-packed.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-prune-packed(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-PRUNE-PACKED(1)             Git Manual            GIT-PRUNE-PACKED(1)

## [](#NAME)NAME

           git-prune-packed - Remove extra objects that are already in pack
           files

## [](#SYNOPSIS)SYNOPSIS

           git prune-packed [-n | --dry-run] [-q | --quiet]

## [](#DESCRIPTION)DESCRIPTION

           This program searches the $GIT_OBJECT_DIRECTORY for all objects
           that currently exist in a pack file as well as in the independent
           object directories.

           All such extra objects are removed.

           A pack is a collection of objects, individually compressed, with
           delta compression applied, stored in a single file, with an
           associated index file.

           Packs are used to reduce the load on mirror systems, backup
           engines, disk storage, etc.

## [](#OPTIONS)OPTIONS

           -n, --dry-run
               Don’t actually remove any objects, only show those that would
               have been removed.

           -q, --quiet
               Squelch the progress indicator.

## [](#SEE_ALSO)SEE ALSO

           git-pack-objects(1) git-repack(1)

## [](#GIT)GIT

           Part of the git(1) suite

## [](#COLOPHON)COLOPHON

           This page is part of the git (Git distributed version control
           system) project.  Information about the project can be found at 
           ⟨http://git-scm.com/⟩.  If you have a bug report for this manual
           page, see ⟨http://git-scm.com/community⟩.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/git/git.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Git 2.55.0.493.g5b2471          2026-08-03            GIT-PRUNE-PACKED(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-pack-objects(1)](../man1/git-pack-objects.1.html),  [git-pack-redundant(1)](../man1/git-pack-redundant.1.html),  [git-repack(1)](../man1/git-repack.1.html)

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
