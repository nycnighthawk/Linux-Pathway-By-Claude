---
{"title": "stg-uncommit(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-uncommit.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-uncommit(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-UNCOMMIT(1)                StGit Manual               STG-UNCOMMIT(1)

## [](#NAME)NAME

           stg-uncommit - Convert regular Git commits into StGit patches

## [](#SYNOPSIS)SYNOPSIS

           stg uncommit <patchname-1> [<patchname-2> ...]
           stg uncommit -n number [<patchname-prefix>]
           stg uncommit -t <committish> [-x]

## [](#DESCRIPTION)DESCRIPTION

           Convert one or more Git commits from the base of the current stack
           into StGit patches. The original Git commits are not modified; the
           StGit stack extends to incorporate these commits as the bottommost
           applied patches. This is the opposite of stg-commit(1).

           By default, the number of patches to uncommit is determined by the
           number of patch names provided on the command line. The first
           provided name is used for the first patch to uncommit, i.e. for
           the newest patch.

           The -n/--number option specifies the number of patches to
           uncommit. In this case, at most one patch name may be specified.
           It is used as prefix to which the patch number is appended. If no
           patch names are provided on the command line, StGit automatically
           generates names based on the first lines of the commit messages.

           The -t/--to option specifies that all commits up to and including
           the given commit should be uncommitted. The -x/--exclusive option
           may be used to exclude the "to" commit.

           Only commits with exactly one parent can be uncommitted; in other
           words, merge commits may not be uncommitted.

## [](#OPTIONS)OPTIONS

           -n <number>, --number=<number>
               Uncommit the specified number of commits

           -t <committish>, --to=<committish>
               Uncommit to the specified committish

           -x, --exclusive
               Exclude the commit specified by the --to option

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

    StGit 2.6.1                     08/04/2026                STG-UNCOMMIT(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html),  [stg-commit(1)](../man1/stg-commit.1.html)

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
