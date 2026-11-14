---
{"title": "git-unpack-objects(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-unpack-objects.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-unpack-objects(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-UNPACK-OBJECTS(1)           Git Manual          GIT-UNPACK-OBJECTS(1)

## [](#NAME)NAME

           git-unpack-objects - Unpack objects from a packed archive

## [](#SYNOPSIS)SYNOPSIS

           git unpack-objects [-n] [-q] [-r] [--strict]

## [](#DESCRIPTION)DESCRIPTION

           Read a packed archive (.pack) from the standard input, expanding
           the objects contained within and writing them into the repository
           in "loose" (one object per file) format.

           Objects that already exist in the repository will not be unpacked
           from the packfile. Therefore, nothing will be unpacked if you use
           this command on a packfile that exists within the target
           repository.

           See git-repack(1) for options to generate new packs and replace
           existing ones.

## [](#OPTIONS)OPTIONS

           -n
               Dry run. Check the pack file without actually unpacking the
               objects.

           -q
               The command usually shows percentage progress. This flag
               suppresses it.

           -r
               When unpacking a corrupt packfile, the command dies at the
               first corruption. This flag tells it to keep going and make
               the best effort to recover as many objects as possible.

           --strict
               Don’t write objects with broken content or links.

           --max-input-size=<size>
               Die, if the pack is larger than <size>.

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

    Git 2.55.0.493.g5b2471          2026-08-03          GIT-UNPACK-OBJECTS(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-config(1)](../man1/git-config.1.html)

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
