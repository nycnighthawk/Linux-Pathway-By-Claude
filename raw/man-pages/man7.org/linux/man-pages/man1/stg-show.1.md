---
{"title": "stg-show(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-show.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-show(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-SHOW(1)                    StGit Manual                   STG-SHOW(1)

## [](#NAME)NAME

           stg-show - Show patch commits

## [](#SYNOPSIS)SYNOPSIS

           stg show [OPTIONS] [patch-or-rev]... [-- <path>...]
           stg show [OPTIONS] [--patch <patch-or-rev>]... [-- <path>...]
           stg show [OPTIONS] [-A] [-U] [-H] [-- <path>...]

## [](#DESCRIPTION)DESCRIPTION

           Show the commit log and diff corresponding to the given patches.
           The topmost patch is shown by default, or HEAD if no patches are
           applied. The output is similar to git-show(1).

## [](#OPTIONS)OPTIONS

           -p <patch-or-rev>, --patch=<patch-or-rev>
               Patch or revision to show

           -b <branch>, --branch=<branch>
               Use <branch> instead of current branch

           -s, --stat
               Show a diffstat summary instead of the full diff

           -O <option>, --diff-opt=<option>
               Pass additional <option> to git diff.

               See the git-diff(1) man page. This option may be specified
               multiple times.

           -A, --applied
               Show the applied patches

           -U, --unapplied
               Show the unapplied patches

           -H, --hidden
               Show the hidden patches

## [](#STGIT)STGIT

           Part of the StGit suite - see stg(1)

## [](#COLOPHON)COLOPHON

           This page is part of the stgit (Stacked Git) project.  Information
           about the project can be found at ⟨http://www.procode.org/stgit/⟩.
           If you have a bug report for this manual page, see
           ⟨http://www.procode.org/stgit/⟩.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/stacked-git/stgit.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-19.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    StGit 2.6.1                     08/04/2026                    STG-SHOW(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html)

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
