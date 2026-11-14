---
{"title": "git-count-objects(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-count-objects.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-count-objects(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-COUNT-OBJECTS(1)            Git Manual           GIT-COUNT-OBJECTS(1)

## [](#NAME)NAME

           git-count-objects - Count unpacked number of objects and their
           disk consumption

## [](#SYNOPSIS)SYNOPSIS

           git count-objects [-v] [-H | --human-readable]

## [](#DESCRIPTION)DESCRIPTION

           Counts the number of unpacked object files and disk space consumed
           by them, to help you decide when it is a good time to repack.

## [](#OPTIONS)OPTIONS

           -v, --verbose
               Provide more detailed reports:

               count: the number of loose objects

               size: disk space consumed by loose objects, in KiB (unless -H
               is specified)

               in-pack: the number of in-pack objects

               packs: the number of pack files

               size-pack: disk space consumed by the packs, in KiB (unless -H
               is specified)

               prune-packable: the number of loose objects that are also
               present in the packs. These objects could be pruned using git
               prune-packed.

               garbage: the number of files in the object database that are
               neither valid loose objects nor valid packs

               size-garbage: disk space consumed by garbage files, in KiB
               (unless -H is specified)

               alternate: absolute path of alternate object databases; may
               appear multiple times, one line per path. Note that if the
               path contains non-printable characters, it may be surrounded
               by double-quotes and contain C-style backslashed escape
               sequences.

           -H, --human-readable
               Print sizes in human readable format

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

    Git 2.55.0.493.g5b2471          2026-08-03           GIT-COUNT-OBJECTS(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html)

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
